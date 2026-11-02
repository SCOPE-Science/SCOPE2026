"""Independent enumerative checks for consecutive-size approval coalitions.
Usage: python verify.py
All arithmetic is exact. No external libraries required.
"""
from itertools import product
from random import Random


def fast(intervals):
    n = len(intervals)
    if n == 0:
        return (0, 0, [], [])
    fixed = [0]*(n+1)
    flex = [0]*(n+1)
    f_agents = [[] for _ in range(n+1)]
    a_agents = [[] for _ in range(n+1)]
    for i, (l, r) in enumerate(intervals):
        assert 1 <= l <= r <= n and r-l <= 1
        if l == r:
            fixed[l] += 1
            a_agents[l].append(i)
        else:
            flex[l] += 1
            f_agents[l].append(i)
    INF = n+1
    prev_min = [0]
    prev_max = [0]
    par_min = [[-1]]
    par_max = [[-1]]
    reachable = [True]
    best_lo = [-1]*(n+1)
    best_hi = [-1]*(n+1)
    stamp = [0]*(n+1)
    for s in range(1,n+1):
        for y, yes in enumerate(reachable):
            if not yes:
                continue
            residue = y%s
            if stamp[residue] != s:
                stamp[residue] = s
                best_lo[residue] = y
                best_hi[residue] = y
            else:
                if s*prev_min[y]+y < s*prev_min[best_lo[residue]]+best_lo[residue]:
                    best_lo[residue] = y
                if s*prev_max[y]+y > s*prev_max[best_hi[residue]]+best_hi[residue]:
                    best_hi[residue] = y
        cur_min = [INF]*(flex[s]+1)
        cur_max = [-INF]*(flex[s]+1)
        cur_r = [False]*(flex[s]+1)
        cur_pmin = [-1]*(flex[s]+1)
        cur_pmax = [-1]*(flex[s]+1)
        for t in range(flex[s]+1):
            residue = (t-fixed[s]-flex[s])%s
            if stamp[residue] != s:
                continue
            y = best_lo[residue]
            z = best_hi[residue]
            assert (fixed[s]+flex[s]-t+y)%s == 0
            cur_r[t] = True
            cur_min[t] = prev_min[y]+(fixed[s]+flex[s]-t+y)//s
            cur_max[t] = prev_max[z]+(fixed[s]+flex[s]-t+z)//s
            cur_pmin[t] = y
            cur_pmax[t] = z
        par_min.append(cur_pmin)
        par_max.append(cur_pmax)
        prev_min, prev_max, reachable = cur_min, cur_max, cur_r
    if not reachable[0]:
        return None

    def reconstruct(par):
        counts = [0]*(n+1)
        t = 0
        for s in range(n,0,-1):
            counts[s] = t
            t = par[s][t]
            assert t >= 0
        assert t == 0
        groups = [[] for _ in range(n+1)]
        for s in range(1,n+1):
            groups[s].extend(a_agents[s])
            groups[s].extend(f_agents[s][:flex[s]-counts[s]])
            if s<n:
                groups[s+1].extend(f_agents[s][flex[s]-counts[s]:])
        partition=[]
        for s in range(1,n+1):
            assert len(groups[s])%s == 0
            partition.extend([tuple(groups[s][p:p+s]) for p in range(0,len(groups[s]),s)])
        return partition
    lo_witness = reconstruct(par_min)
    hi_witness = reconstruct(par_max)
    assert len(lo_witness)==prev_min[0]
    assert len(hi_witness)==prev_max[0]
    for pp in (lo_witness, hi_witness):
        assert sorted(i for G in pp for i in G) == list(range(n))
        assert all(intervals[i][0] <= len(G) <= intervals[i][1] for G in pp for i in G)
    return (prev_min[0],prev_max[0],lo_witness,hi_witness)


def brute(intervals):
    n=len(intervals)
    feasible=[]
    def partition(j,blocks):
        if j==n:
            if all(all(intervals[i][0]<=len(B)<=intervals[i][1] for i in B) for B in blocks):
                feasible.append(len(blocks))
            return
        for B in blocks:
            B.append(j)
            partition(j+1,blocks)
            B.pop()
        blocks.append([j])
        partition(j+1,blocks)
        blocks.pop()
    partition(0,[])
    return (min(feasible),max(feasible)) if feasible else None


def choices(n):
    return [(s,s) for s in range(1,n+1)] + [(s,s+1) for s in range(1,n)]

if __name__=='__main__':
    rng=Random(44616)
    checked=0
    for n in range(1,5):
        options=choices(n)
        for inst in product(options,repeat=n):
            ans=fast(inst)
            truth=brute(inst)
            assert (ans[:2] if ans else None)==truth,(n,inst,ans,truth)
            checked+=1
    print('exhaustive small interval profiles:',checked)
    for n in range(5,9):
        options=choices(n)
        for _ in range(1250):
            inst=[rng.choice(options) for i in range(n)]
            ans=fast(inst)
            truth=brute(inst)
            assert (ans[:2] if ans else None)==truth,(n,inst,ans,truth)
            checked+=1
    print('brute set-partition comparisons:',checked)
    cnt=0
    for n in (9,10,11,12,15):
        options=choices(n)
        for _ in range(250):
            inst=[rng.choice(options) for i in range(n)]
            ans=fast(inst)
            B=[0]*(n+1)
            F=[0]*(n+1)
            for l,r in inst:
                (B if l==r else F)[l]+=1
            feasible=[]
            for allocation in product(*(range(F[s]+1) for s in range(1,n+1))):
                y=0;total=0
                for s in range(1,n+1):
                    t=allocation[s-1]
                    a=B[s]+F[s]-t+y
                    if a%s:break
                    total+=a//s
                    y=t
                else:
                    if y==0: feasible.append(total)
            truth=(min(feasible),max(feasible)) if feasible else None
            assert (ans[:2] if ans else None)==truth,(n,inst,ans,truth)
            cnt+=1
    print('independent binary assignment comparisons:',cnt)
    print('PASS: feasibility, exact extrema, and constructed witnesses')
