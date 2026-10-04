from itertools import product
import random


def q_bound(r, k):
    q = 1
    while q ** (k - 1) < r:
        q += 1
    return q


def slice_code(coords, q):
    last = coords[-1]
    return tuple((coords[j] - last) % q for j in range(len(coords) - 1))


def check_slice_bijections():
    for k in range(2, 6):
        for q in range(1, 5):
            Q = range(q)
            target = set(product(Q, repeat=k - 1))
            for i in range(k):
                for fixed in Q:
                    image = {
                        slice_code(coords, q)
                        for coords in product(Q, repeat=k)
                        if coords[i] == fixed
                    }
                    assert image == target


def derive_effectivity(actions, outcome, k):
    sigma = []
    for i in range(k):
        family = set()
        for action in actions[i]:
            outputs = {
                outcome[profile]
                for profile in product(*actions)
                if profile[i] == action
            }
            family.add(frozenset(outputs))
        sigma.append(family)
    return sigma


def realize(sigma, common_range):
    k = len(sigma)
    R = sorted(common_range)
    r = len(R)
    q = q_bound(r, k)
    Q = range(q)

    tuples = list(product(Q, repeat=k - 1))
    pi = {t: R[j % r] for j, t in enumerate(tuples)}

    def key(s):
        return (len(s), tuple(sorted(s)))

    actions = [
        [(s, c) for s in sorted(sigma[i], key=key) for c in Q]
        for i in range(k)
    ]

    def outcome_of(profile):
        sets = [set(x[0]) for x in profile]
        labels = [x[1] for x in profile]
        intersection = set.intersection(*sets)
        assert intersection
        candidate = pi[slice_code(labels, q)]
        return candidate if candidate in intersection else min(intersection)

    outcome = {profile: outcome_of(profile) for profile in product(*actions)}
    return actions, outcome, q


def random_replay():
    for k in (2, 3, 4):
        for ambient_r in range(1, 8):
            for seed in range(20):
                random.seed(10000 * k + 100 * ambient_r + seed)
                actions = [list(range(random.randint(1, 4))) for _ in range(k)]
                outcome = {
                    profile: random.randrange(ambient_r)
                    for profile in product(*actions)
                }
                sigma = derive_effectivity(actions, outcome, k)
                common_range = set().union(*sigma[0])
                assert common_range
                assert all(set().union(*sigma[i]) == common_range for i in range(k))
                assert all(
                    set.intersection(*[set(s) for s in chosen])
                    for chosen in product(*[list(fam) for fam in sigma])
                )
                new_actions, new_outcome, q = realize(sigma, common_range)
                new_sigma = derive_effectivity(new_actions, new_outcome, k)
                assert new_sigma == sigma
                for i in range(k):
                    assert len(new_actions[i]) == q * len(sigma[i])


def check_sharp_arithmetic():
    for k in range(2, 7):
        for r in (1, 2, 3, 4, 5, 8, 9, 10, 16, 17, 25, 32):
            q = q_bound(r, k)
            assert (q - 1) ** (k - 1) < r <= q ** (k - 1)
            if q > 1:
                # If every agent had at most q-1 actions in the single-neighborhood
                # full-range frame, a fixed action could see at most this many
                # completions, fewer than the r required outputs.
                assert (q - 1) ** (k - 1) < r


if __name__ == "__main__":
    check_slice_bijections()
    random_replay()
    check_sharp_arithmetic()
    print("VERIFY_OK")
