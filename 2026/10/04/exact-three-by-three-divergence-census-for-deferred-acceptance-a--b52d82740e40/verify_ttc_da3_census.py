#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
from fractions import Fraction
import math
import hashlib


def da_stack(student_prefs, school_prios):
    n=len(student_prefs)
    srank=[{s:r for r,s in enumerate(p)} for p in student_prefs]
    prank=[{i:r for r,i in enumerate(p)} for p in school_prios]
    nxt=[0]*n
    school_of=[-1]*n
    held=[-1]*n
    free=list(range(n))
    while free:
        i=free.pop()
        s=student_prefs[i][nxt[i]]; nxt[i]+=1
        if held[s] == -1:
            held[s]=i; school_of[i]=s
        else:
            j=held[s]
            if prank[s][i] < prank[s][j]:
                held[s]=i; school_of[i]=s; school_of[j]=-1; free.append(j)
            else:
                free.append(i)
    return tuple(school_of)


def da_rounds(student_prefs, school_prios):
    n=len(student_prefs)
    prank=[{i:r for r,i in enumerate(p)} for p in school_prios]
    nxt=[0]*n
    school_of=[-1]*n
    held=[-1]*n
    while -1 in school_of:
        props=[[] for _ in range(n)]
        for i in range(n):
            if school_of[i] == -1:
                s=student_prefs[i][nxt[i]]; nxt[i]+=1; props[s].append(i)
        for s in range(n):
            cand=props[s][:]
            if held[s] != -1: cand.append(held[s])
            if not cand: continue
            best=min(cand,key=lambda i:prank[s][i])
            old=held[s]
            held[s]=best; school_of[best]=s
            for i in cand:
                if i != best: school_of[i]=-1
    return tuple(school_of)


def ttc_all_cycles(student_prefs, school_prios):
    n=len(student_prefs)
    active_i=set(range(n)); active_s=set(range(n)); out=[-1]*n
    prank=[{i:r for r,i in enumerate(p)} for p in school_prios]
    while active_i:
        nxt={}
        for i in active_i:
            s=next(s for s in student_prefs[i] if s in active_s)
            nxt=('i',i)
        # functional graph mapping, students point to schools; schools to best active student
        f={}
        for i in active_i:
            s=next(s for s in student_prefs[i] if s in active_s)
            f[('i',i)]=('s',s)
        for s in active_s:
            i=min(active_i,key=lambda x:prank[s][x])
            f[('s',s)]=('i',i)
        cycle_nodes=set()
        seen_global=set()
        for start in list(f):
            if start in seen_global: continue
            path=[]; pos={}; x=start
            while x not in seen_global and x not in pos:
                pos[x]=len(path); path.append(x); x=f[x]
            if x in pos:
                cycle_nodes.update(path[pos[x]:])
            seen_global.update(path)
        chosen=[]
        for node in cycle_nodes:
            if node[0]=='i':
                i=node[1]; s=f[node][1]
                chosen.append((i,s))
        assert chosen
        for i,s in chosen:
            out[i]=s
        for i,s in chosen:
            active_i.remove(i); active_s.remove(s)
    return tuple(out)


def ttc_one_cycle(student_prefs, school_prios):
    n=len(student_prefs)
    active_i=set(range(n)); active_s=set(range(n)); out=[-1]*n
    prank=[{i:r for r,i in enumerate(p)} for p in school_prios]
    while active_i:
        f={}
        for i in active_i:
            f[('i',i)]=('s',next(s for s in student_prefs[i] if s in active_s))
        for s in active_s:
            f[('s',s)]=('i',min(active_i,key=lambda x:prank[s][x]))
        start=('i',min(active_i)); path=[]; pos={}; x=start
        while x not in pos:
            pos[x]=len(path); path.append(x); x=f[x]
        cyc=path[pos[x]:]
        chosen=[]
        for node in cyc:
            if node[0]=='i': chosen.append((node[1],f[node][1]))
        assert chosen
        for i,s in chosen: out[i]=s
        for i,s in chosen:
            active_i.remove(i); active_s.remove(s)
    return tuple(out)


def pareto_relation(a,b,prefs):
    # relation of b versus a: 'b_dom', 'a_dom', 'equal', 'incomp'
    ranks=[{s:r for r,s in enumerate(p)} for p in prefs]
    if a==b: return 'equal'
    b_weak=all(ranks[i][b[i]] <= ranks[i][a[i]] for i in range(len(prefs)))
    b_str=any(ranks[i][b[i]] < ranks[i][a[i]] for i in range(len(prefs)))
    a_weak=all(ranks[i][a[i]] <= ranks[i][b[i]] for i in range(len(prefs)))
    a_str=any(ranks[i][a[i]] < ranks[i][b[i]] for i in range(len(prefs)))
    if b_weak and b_str: return 'b_dom'
    if a_weak and a_str: return 'a_dom'
    return 'incomp'


def pareto_efficient(match,prefs):
    n=len(prefs); ranks=[{s:r for r,s in enumerate(p)} for p in prefs]
    for other in permutations(range(n)):
        if other==match: continue
        if all(ranks[i][other[i]] <= ranks[i][match[i]] for i in range(n)) and any(ranks[i][other[i]] < ranks[i][match[i]] for i in range(n)):
            return False
    return True


def justified_envy_pairs(match,prefs,priorities):
    n=len(prefs); ranks=[{s:r for r,s in enumerate(p)} for p in prefs]; prank=[{i:r for r,i in enumerate(p)} for p in priorities]
    owner=[-1]*n
    for i,s in enumerate(match): owner[s]=i
    pairs=[]
    for i in range(n):
        for s in range(n):
            j=owner[s]
            if ranks[i][s] < ranks[i][match[i]] and prank[s][i] < prank[s][j]:
                pairs.append((i,s,j))
    return tuple(pairs)


def relabel_profile(student_prefs, school_prios, si, ss):
    n=len(student_prefs)
    new_sp=[None]*n; new_pr=[None]*n
    for old_i in range(n):
        new_sp[si[old_i]]=tuple(ss[s] for s in student_prefs[old_i])
    for old_s in range(n):
        new_pr[ss[old_s]]=tuple(si[i] for i in school_prios[old_s])
    return tuple(new_sp),tuple(new_pr)


def canonical(profile, perms, pref_index):
    sp,pr=profile; best=None
    for si in perms:
        for ss in perms:
            a,b=relabel_profile(sp,pr,si,ss)
            code=tuple(pref_index[p] for p in a+b)
            if best is None or code<best: best=code
    return best

# Minimal-size equality.
for n in (1,2):
    prefs=list(permutations(range(n)))
    total=0
    for sp in product(prefs, repeat=n):
        for pr in product(prefs, repeat=n):
            d1=da_stack(sp,pr); d2=da_rounds(sp,pr); t1=ttc_all_cycles(sp,pr); t2=ttc_one_cycle(sp,pr)
            assert d1==d2 and t1==t2 and d1==t1
            total+=1
    assert total==math.factorial(n)**(2*n)

n=3; prefs=list(permutations(range(n))); perms=prefs; pref_index={p:i for i,p in enumerate(prefs)}
counts=Counter(); eff_refine=Counter(); envy_hist=Counter(); divergent=[]
for sp in product(prefs, repeat=n):
    for pr in product(prefs, repeat=n):
        d1=da_stack(sp,pr); d2=da_rounds(sp,pr); t1=ttc_all_cycles(sp,pr); t2=ttc_one_cycle(sp,pr)
        assert d1==d2 and t1==t2
        rel=pareto_relation(d1,t1,sp)
        counts[rel]+=1
        de=pareto_efficient(d1,sp)
        eff_refine[(de,rel)]+=1
        if rel!='equal':
            divergent.append((sp,pr,rel,de))
            envy_hist[len(justified_envy_pairs(t1,sp,pr))]+=1

assert counts==Counter({'equal':42336,'incomp':3240,'b_dom':1080})
assert counts['a_dom']==0
assert eff_refine==Counter({(True,'equal'):42336,(True,'incomp'):3024,(False,'b_dom'):1080,(False,'incomp'):216})
assert envy_hist==Counter({1:3456,2:864})
assert Fraction(4320,46656)==Fraction(5,54)
assert Fraction(1080,46656)==Fraction(5,216)
assert Fraction(1296,46656)==Fraction(1,36)
assert Fraction(216,46656)==Fraction(1,216)

# Role-preserving quotient on all divergent profiles.
class_counts=Counter(); orbit_members=Counter()
for sp,pr,rel,de in divergent:
    c=canonical((sp,pr),perms,pref_index)
    key=(c,rel,de)
    orbit_members[key]+=1
for (c,rel,de),sz in orbit_members.items():
    class_counts[(rel,de)]+=1
    assert sz==36
assert class_counts==Counter({('incomp',True):84,('b_dom',False):30,('incomp',False):6})
assert len(orbit_members)==120

# Independent Burnside count restricted to each divergent stratum.
burnside=Counter()
for si in perms:
    for ss in perms:
        fixed=Counter()
        for sp,pr,rel,de in divergent:
            if relabel_profile(sp,pr,si,ss)==(sp,pr):
                fixed[(rel,de)]+=1
        for k,v in fixed.items(): burnside[k]+=v
for k in class_counts:
    assert burnside[k]//36==class_counts[k]

# Abdulkadiroglu-Sonmez 2003 Example 1, relabeled: students 0,1,2; schools 0,1,2.
# Student prefs: 0: 0>1>2, 1:0>1>2, 2:1>0>2.
# Priorities: school0:2>0>1, school1:0>1>2, school2 arbitrary 0>1>2.
ex_sp=((1,0,2),(0,1,2),(0,1,2))
ex_pr=((0,2,1),(1,0,2),(1,0,2))
ex_da=da_stack(ex_sp,ex_pr); ex_ttc=ttc_all_cycles(ex_sp,ex_pr)
assert pareto_relation(ex_da,ex_ttc,ex_sp)=='b_dom'

canon_lines='\n'.join(','.join(map(str,k[0]))+f'|{k[1]}|{int(k[2])}|{v}' for k,v in sorted(orbit_members.items()))
digest=hashlib.sha256(canon_lines.encode('ascii')).hexdigest()

print('VERIFY_OK')
print('n1_n2_da_equals_ttc', True)
print('n3_total_profiles', 46656)
print('n3_equal', counts['equal'])
print('n3_ttc_pareto_dominates_da', counts['b_dom'])
print('n3_incomparable', counts['incomp'])
print('n3_da_pareto_dominates_ttc', counts['a_dom'])
print('n3_divergence_probability', '5/54')
print('n3_ttc_dominance_probability', '5/216')
print('n3_da_pareto_inefficient', 1296)
print('n3_da_inefficient_ttc_incomparable', 216)
print('n3_da_inefficient_ttc_incomparable_probability', '1/216')
print('n3_ttc_justified_envy_pair_hist', dict(sorted(envy_hist.items())))
print('n3_divergent_symmetry_classes', 120)
print('n3_class_refinement', dict(sorted((str(k),v) for k,v in class_counts.items())))
print('all_divergent_orbits_size_36', True)
print('burnside_classes', dict(sorted((str(k), burnside[k]//36) for k in class_counts)))
print('class_digest_sha256', digest)
print('source_example_da', ex_da)
print('source_example_ttc', ex_ttc)

