#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter, defaultdict
import hashlib
import math

def da_stack(m_prefs, w_prefs):
    n = len(m_prefs)
    wrank = [{m:r for r,m in enumerate(p)} for p in w_prefs]
    next_pos = [0]*n
    wife = [-1]*n
    husband = [-1]*n
    free = list(range(n))
    while free:
        m = free.pop()
        w = m_prefs[m][next_pos[m]]
        next_pos[m] += 1
        if husband[w] == -1:
            husband[w] = m
            wife[m] = w
        else:
            old = husband[w]
            if wrank[w][m] < wrank[w][old]:
                husband[w] = m
                wife[m] = w
                wife[old] = -1
                free.append(old)
            else:
                free.append(m)
    return tuple(wife), tuple(husband)

def da_rounds(m_prefs, w_prefs):
    n = len(m_prefs)
    wrank = [{m:r for r,m in enumerate(p)} for p in w_prefs]
    next_pos = [0]*n
    wife = [-1]*n
    husband = [-1]*n
    while any(x == -1 for x in wife):
        proposals = [[] for _ in range(n)]
        for m in range(n):
            if wife[m] == -1:
                w = m_prefs[m][next_pos[m]]
                next_pos[m] += 1
                proposals[w].append(m)
        for w in range(n):
            candidates = proposals[w][:]
            if husband[w] != -1:
                candidates.append(husband[w])
            if candidates:
                best = min(candidates, key=lambda m: wrank[w][m])
                old = husband[w]
                husband[w] = best
                wife[best] = w
                for m in candidates:
                    if m != best:
                        wife[m] = -1
    return tuple(wife), tuple(husband)

def stable_matchings(m_prefs, w_prefs):
    n = len(m_prefs)
    mrank = [{w:r for r,w in enumerate(p)} for p in m_prefs]
    wrank = [{m:r for r,m in enumerate(p)} for p in w_prefs]
    out = []
    for wife in permutations(range(n)):
        husband = [-1]*n
        for m,w in enumerate(wife):
            husband[w] = m
        ok = True
        for m in range(n):
            for w in range(n):
                if wife[m] == w:
                    continue
                if mrank[m][w] < mrank[m][wife[m]] and wrank[w][m] < wrank[w][husband[w]]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append((tuple(wife), tuple(husband)))
    return out

def manipulators(m_prefs, w_prefs):
    n = len(m_prefs)
    prefs = list(permutations(range(n)))
    base_a = da_stack(m_prefs, w_prefs)
    base_b = da_rounds(m_prefs, w_prefs)
    assert base_a == base_b
    _, husband0 = base_a
    result = []
    for w in range(n):
        true_rank = {m:r for r,m in enumerate(w_prefs[w])}
        gains = []
        for report in prefs:
            if report == w_prefs[w]:
                continue
            altered = list(w_prefs)
            altered[w] = report
            altered = tuple(altered)
            out_a = da_stack(m_prefs, altered)
            out_b = da_rounds(m_prefs, altered)
            assert out_a == out_b
            wife1, husband1 = out_a
            if true_rank[husband1[w]] < true_rank[husband0[w]]:
                gains.append((report, wife1, husband1))
        if gains:
            result.append((w, tuple(gains)))
    return tuple(result)

def relabel_profile(m_prefs, w_prefs, sigma_m, sigma_w):
    n = len(m_prefs)
    new_m = [None]*n
    new_w = [None]*n
    for old_m in range(n):
        new_m[sigma_m[old_m]] = tuple(sigma_w[w] for w in m_prefs[old_m])
    for old_w in range(n):
        new_w[sigma_w[old_w]] = tuple(sigma_m[m] for m in w_prefs[old_w])
    return tuple(new_m), tuple(new_w)

def encode_profile(profile, pref_index):
    m_prefs, w_prefs = profile
    return tuple(pref_index[p] for p in m_prefs + w_prefs)

def canonical_profile(m_prefs, w_prefs, perms, pref_index):
    best = None
    for sm in perms:
        for sw in perms:
            code = encode_profile(relabel_profile(m_prefs, w_prefs, sm, sw), pref_index)
            if best is None or code < best:
                best = code
    return best

# Sharp boundary at n=2.
for n in (1,2):
    prefs = list(permutations(range(n)))
    bad = 0
    for m_prefs in product(prefs, repeat=n):
        for w_prefs in product(prefs, repeat=n):
            if manipulators(m_prefs, w_prefs):
                bad += 1
    assert bad == 0

# Full n=3 census.
n = 3
prefs = list(permutations(range(n)))
pref_index = {p:i for i,p in enumerate(prefs)}
group = list(permutations(range(n)))

profile_count = 0
bad_count = 0
manipulator_count_hist = Counter()
stable_joint = Counter()
beneficial_reports_per_manipulator = Counter()
bad_canon_counts = Counter()
all_profitable_true_stable = True

# Store bad profiles compactly for independent Burnside pass.
bad_profiles = []

for m_prefs in product(prefs, repeat=n):
    for w_prefs in product(prefs, repeat=n):
        profile_count += 1
        mans = manipulators(m_prefs, w_prefs)
        if not mans:
            continue

        bad_count += 1
        bad_profiles.append((m_prefs, w_prefs))
        manipulator_count_hist[len(mans)] += 1

        stables = stable_matchings(m_prefs, w_prefs)
        stable_wives = {s[0] for s in stables}
        stable_joint[(len(stables), len(mans))] += 1

        for w,gains in mans:
            beneficial_reports_per_manipulator[len(gains)] += 1
            for _, wife1, _ in gains:
                if wife1 not in stable_wives:
                    all_profitable_true_stable = False

        can = canonical_profile(m_prefs, w_prefs, group, pref_index)
        bad_canon_counts[can] += 1

assert profile_count == 6**6 == 46656
assert bad_count == 864
assert manipulator_count_hist == Counter({1:648, 2:216})
assert stable_joint == Counter({(2,1):540, (2,2):216, (3,1):108})
assert beneficial_reports_per_manipulator == Counter({1:1080})
assert all_profitable_true_stable
assert len(bad_canon_counts) == 24
assert Counter(bad_canon_counts.values()) == Counter({36:24})

# Independent Burnside count on the already classified bad subset.
fixed_sum = 0
fixed_hist = Counter()
for sm in group:
    for sw in group:
        fixed = 0
        for m_prefs, w_prefs in bad_profiles:
            if relabel_profile(m_prefs, w_prefs, sm, sw) == (m_prefs, w_prefs):
                fixed += 1
        fixed_sum += fixed
        fixed_hist[fixed] += 1
assert fixed_sum % 36 == 0
assert fixed_sum // 36 == 24
assert fixed_hist[864] == 1
assert sum(k*v for k,v in fixed_hist.items()) == fixed_sum

# Canonical-class digest makes the exact quotient reproducible without bloating output.
canon_lines = "\n".join(",".join(map(str,k)) for k in sorted(bad_canon_counts))
canon_sha256 = hashlib.sha256(canon_lines.encode("ascii")).hexdigest()

print("VERIFY_OK")
print("n_le_2_manipulable_profiles", 0)
print("n3_total_profiles", profile_count)
print("n3_manipulable_profiles", bad_count)
print("n3_probability", "1/54")
print("n3_manipulator_hist", dict(sorted(manipulator_count_hist.items())))
print("n3_stable_count_by_manipulator_count", dict(sorted(stable_joint.items())))
print("profitable_reports_per_manipulator", dict(beneficial_reports_per_manipulator))
print("all_profitable_reports_induce_true_stable_matching", all_profitable_true_stable)
print("n3_role_preserving_symmetry_classes", len(bad_canon_counts))
print("n3_bad_orbit_size_hist", dict(Counter(bad_canon_counts.values())))
print("burnside_bad_classes", fixed_sum // 36)
print("bad_class_digest_sha256", canon_sha256)
