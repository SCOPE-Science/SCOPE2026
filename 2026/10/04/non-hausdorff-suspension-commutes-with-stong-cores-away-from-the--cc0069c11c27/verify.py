#!/usr/bin/env python3
from itertools import product


def posets(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    for choices in product((-1,0,1), repeat=len(pairs)):
        lt=[[False]*n for _ in range(n)]
        for (i,j),c in zip(pairs,choices):
            if c==-1: lt[i][j]=True
            elif c==1: lt[j][i]=True
        ok=True
        # transitivity of strict relation
        for i in range(n):
            for j in range(n):
                if lt[i][j]:
                    for k in range(n):
                        if lt[j][k] and not lt[i][k]:
                            ok=False; break
                    if not ok: break
            if not ok: break
        if ok:
            yield lt


def restrict(lt, keep):
    return [[lt[i][j] for j in keep] for i in keep]


def beat_info(lt,x):
    n=len(lt)
    ups=[y for y in range(n) if lt[x][y]]
    downs=[y for y in range(n) if lt[y][x]]
    upw=None
    for y in ups:
        if all(y==z or lt[y][z] for z in ups):
            upw=y; break
    downw=None
    for y in downs:
        if all(y==z or lt[z][y] for z in downs):
            downw=y; break
    return upw,downw


def is_minimal(lt):
    return all(beat_info(lt,x)==(None,None) for x in range(len(lt)))


def suspend(lt):
    n=len(lt); m=n+2
    r=[[False]*m for _ in range(m)]
    for i in range(n):
        for j in range(n): r[i][j]=lt[i][j]
    for i in range(n):
        r[i][n]=True; r[i][n+1]=True
    return r


def core_reduce(lt, check_lift=False):
    cur=[row[:] for row in lt]
    steps=[]
    while True:
        found=None
        for x in range(len(cur)):
            u,d=beat_info(cur,x)
            if u is not None:
                found=(x,'up',u); break
            if d is not None:
                found=(x,'down',d); break
        if found is None: break
        x,typ,w=found
        if check_lift:
            s=suspend(cur)
            su,sd=beat_info(s,x)
            if typ=='up':
                assert su==w, (typ,w,su,sd,len(cur))
            else:
                assert sd==w, (typ,w,su,sd,len(cur))
        keep=[i for i in range(len(cur)) if i!=x]
        cur=restrict(cur,keep)
        steps.append(found)
    assert is_minimal(cur)
    return cur,steps


def predicted_core_size(lt,k):
    c,_=core_reduce(lt)
    return 1 if len(c)==1 else len(c)+2*k


def actual_core_size_after_suspensions(lt,k):
    s=[row[:] for row in lt]
    for _ in range(k): s=suspend(s)
    c,_=core_reduce(s)
    return len(c)


total=0
by_n={}
lift_steps=0
checks=0
for n in range(1,6):
    cnt=0
    for lt in posets(n):
        cnt+=1; total+=1
        c,steps=core_reduce(lt, check_lift=True)
        lift_steps += len(steps)
        # Exact minimality criterion for one suspension.
        sm=is_minimal(suspend(lt))
        pred=is_minimal(lt) and n>=2
        assert sm==pred
        checks+=1
        # Exact core-cardinality formula for first three iterates.
        for k in (1,2,3):
            a=actual_core_size_after_suspensions(lt,k)
            p=1 if len(c)==1 else len(c)+2*k
            assert a==p, (n,k,len(c),a,p)
            checks+=1
    by_n[n]=cnt

print('VERIFY_OK')
print('labeled_posets_by_n=' + ','.join(f'{n}:{by_n[n]}' for n in sorted(by_n)))
print('total_labeled_posets=',total)
print('lifted_beat_deletions_checked=',lift_steps)
print('theorem_instances_checked=',checks)
