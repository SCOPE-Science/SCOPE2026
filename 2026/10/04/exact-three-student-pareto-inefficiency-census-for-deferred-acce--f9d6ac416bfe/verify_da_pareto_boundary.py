#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter


def ranks(profile):
    n=len(profile)
    out=[]
    for pref in profile:
        r=[0]*n
        for k,x in enumerate(pref): r[x]=k
        out.append(r)
    return out


def da_queue(prefs, prios):
    n=len(prefs); sr=ranks(prios)
    nxt=[0]*n; held=[None]*n; free=list(range(n))
    while free:
        i=free.pop(0)
        s=prefs[i][nxt[i]]; nxt[i]+=1
        j=held[s]
        if j is None:
            held[s]=i
        elif sr[s][i] < sr[s][j]:
            held[s]=i; free.append(j)
        else:
            free.append(i)
    M=[None]*n
    for s,i in enumerate(held): M[i]=s
    return tuple(M)


def da_rounds(prefs, prios):
    n=len(prefs); sr=ranks(prios)
    nxt=[0]*n; held=[None]*n
    engaged=[False]*n
    while not all(engaged):
        batches=[[] for _ in range(n)]
        proposers=[i for i in range(n) if not engaged[i]]
        for i in proposers:
            s=prefs[i][nxt[i]]; nxt[i]+=1; batches[s].append(i)
        for s,arr in enumerate(batches):
            if not arr: continue
            if held[s] is not None: arr.append(held[s])
            best=min(arr,key=lambda i:sr[s][i])
            for i in arr: engaged[i]=(i==best)
            held[s]=best
    M=[None]*n
    for s,i in enumerate(held): M[i]=s
    return tuple(M)


def stable(M,prefs,prios):
    n=len(prefs); pr=ranks(prefs); sr=ranks(prios)
    inv=[None]*n
    for i,s in enumerate(M): inv[s]=i
    for i in range(n):
        for s in range(n):
            if M[i]==s: continue
            if pr[i][s] < pr[i][M[i]] and sr[s][i] < sr[s][inv[s]]:
                return False
    return True


def pareto_improvements(M,prefs):
    n=len(prefs); pr=ranks(prefs); out=[]
    for N in permutations(range(n)):
        if N==M: continue
        weak=True; strict=False
        for i in range(n):
            if pr[i][N[i]] > pr[i][M[i]]:
                weak=False; break
            strict |= pr[i][N[i]] < pr[i][M[i]]
        if weak and strict: out.append(tuple(N))
    return out


def has_trading_cycle(M,prefs):
    # directed edge i -> j if i strictly prefers j's assigned school to own school
    n=len(prefs); pr=ranks(prefs)
    edge=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            edge[i][j]=pr[i][M[j]] < pr[i][M[i]]
    reach=[row[:] for row in edge]
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    if reach[k][j]: reach[i][j]=True
    return any(reach[i][i] for i in range(n))


def ergin_cyclic(prios):
    # Unit-capacity Ergin cycle: distinct schools x,y and students i,j,k with
    # i >_x j >_x k and k >_y i.
    n=len(prios); sr=ranks(prios)
    for x in range(n):
        for y in range(n):
            if y==x: continue
            for i in range(n):
                for j in range(n):
                    if j==i: continue
                    for k in range(n):
                        if k==i or k==j: continue
                        if sr[x][i] < sr[x][j] < sr[x][k] and sr[y][k] < sr[y][i]:
                            return True
    return False


def exhaustive(n):
    orders=list(permutations(range(n)))
    inefficient=0; unique_imp=Counter(); rankmult=Counter(); strict_improvers=Counter()
    by_priority=Counter(); priority_cycle=Counter(); zero_priority=[]
    for prios in product(orders, repeat=n):
        count=0
        cyc=ergin_cyclic(prios)
        priority_cycle[cyc]+=1
        for prefs in product(orders, repeat=n):
            M1=da_queue(prefs,prios); M2=da_rounds(prefs,prios)
            assert M1==M2
            assert stable(M1,prefs,prios)
            # independently check student-optimality among all stable matchings
            pr=ranks(prefs)
            st=[N for N in permutations(range(n)) if stable(N,prefs,prios)]
            assert M1 in st
            assert all(all(pr[i][M1[i]] <= pr[i][N[i]] for i in range(n)) for N in st)
            imps=pareto_improvements(M1,prefs)
            # Pareto inefficiency iff envy/trading graph has a directed cycle
            assert bool(imps)==has_trading_cycle(M1,prefs)
            if imps:
                inefficient+=1; count+=1
                unique_imp[len(imps)]+=1
                ranks_assigned=tuple(sorted(pr[i][M1[i]]+1 for i in range(n)))
                rankmult[ranks_assigned]+=1
                for N in imps:
                    strict_improvers[sum(pr[i][N[i]]<pr[i][M1[i]] for i in range(n))]+=1
        by_priority[count]+=1
        if count==0: zero_priority.append(prios)
        # Ergin theorem finite shadow: exactly the acyclic priorities have no inefficient DA profile.
        assert (count==0)==(not cyc)
    return {
      'inefficient':inefficient,
      'total':len(orders)**(2*n),
      'unique_imp':unique_imp,
      'rankmult':rankmult,
      'strict_improvers':strict_improvers,
      'by_priority':by_priority,
      'priority_cycle':priority_cycle,
      'zero_priority':len(zero_priority),
    }

r2=exhaustive(2)
assert r2['total']==16 and r2['inefficient']==0
assert r2['by_priority']==Counter({0:4})

r3=exhaustive(3)
assert r3['total']==46656 and r3['inefficient']==1296
assert r3['unique_imp']==Counter({1:1296})
assert r3['strict_improvers']==Counter({2:1296})
assert r3['rankmult']==Counter({(2,2,2):648,(2,2,3):648})
assert r3['by_priority']==Counter({8:126,0:42,4:36,12:12})
assert r3['priority_cycle']==Counter({True:174,False:42})
assert r3['zero_priority']==42

print('VERIFY_OK')
print('n2_total',r2['total'],'n2_inefficient',r2['inefficient'])
print('n3_total',r3['total'],'n3_inefficient',r3['inefficient'],'probability','1/36')
print('unique_pareto_improvement_counts',dict(r3['unique_imp']))
print('strict_improvers_per_inefficient_profile',dict(r3['strict_improvers']))
print('da_rank_multisets',dict(r3['rankmult']))
print('priority_inefficiency_histogram',dict(sorted(r3['by_priority'].items())))
print('priority_ergin_cycle_counts',dict(r3['priority_cycle']))
