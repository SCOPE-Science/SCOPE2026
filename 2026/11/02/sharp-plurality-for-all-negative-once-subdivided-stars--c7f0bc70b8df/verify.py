#!/usr/bin/env python3
"""Standalone direct simulator for signed burning of subdivided stars.
Only the Python standard library is required.
"""
from collections import deque

def graph(m):
    n = 2*m+1
    adj = [[] for _ in range(n)]
    for i in range(m):
        a,b = 2*i+1,2*i+2
        for u,v in ((0,a),(a,b)):
            adj[u].append(v)
            adj[v].append(u)
    return adj

def spread(state,adj):
    new=list(state)
    for v,color in enumerate(state):
        if color: continue
        influence=-sum(state[w] for w in adj[v])
        if influence: new[v] = 1 if influence>0 else -1
    return tuple(new)

def exhaustive_original(m):
    adj=graph(m);n=len(adj)
    start=(0,)*n
    todo=deque([start]); seen={start}; finished=set()
    while todo:
        state=todo.popleft()
        if all(state):
            finished.add(state)
            continue
        after=spread(state,adj)
        if all(after):
            if after not in seen:
                seen.add(after);todo.append(after)
            continue
        for v in range(n):
            if after[v]==0:
                for col in (-1,1):
                    new=list(after);new[v]=col;new=tuple(new)
                    if new not in seen:
                        seen.add(new);todo.append(new)
    return len(seen),len(finished),max(sum(v==1 for v in st) for st in finished)

def orbit_original(m):
    # Exact orbit compression of the same original graph transitions.
    s=(0,tuple(sorted([(0,0)]*m)))
    q=deque([s]);seen={s};finished=set()
    while q:
        c, arms=q.popleft()
        if c and all(a and b for a,b in arms):
            finished.add((c,arms));continue
        adj_states=(c,arms)
        influence_c=-sum(a for a,b in arms)
        cc=c or (1 if influence_c>0 else -1 if influence_c<0 else 0)
        newarms=[]
        for a,b in arms:
            influence_a=-(c+b)
            aa=a or (1 if influence_a>0 else -1 if influence_a<0 else 0)
            bb=b or (-a)
            newarms.append((aa,bb))
        newarms=tuple(sorted(newarms))
        candidates=[]
        if cc and all(a and b for a,b in newarms):
            candidates=[(cc,newarms)]
        else:
            if not cc:
                for colour in (-1,1): candidates.append((colour,newarms))
            for i,(a,b) in enumerate(newarms):
                for j in range(2):
                    if (a,b)[j] == 0:
                        for colour in (-1,1):
                            nextarms=list(newarms)
                            pair=list(nextarms[i]);pair[j]=colour
                            nextarms[i]=tuple(pair)
                            candidates.append((cc,tuple(sorted(nextarms))))
        for new in candidates:
            if new not in seen:
                seen.add(new);q.append(new)
    maximum=max((c==1)+sum((a==1)+(b==1) for a,b in arms) for c,arms in finished)
    return len(seen),len(finished),maximum

def explicit_schedule(m):
    assert m>=3
    adj=graph(m)
    st=(0,)*(2*m+1)
    for t,(v,col) in enumerate([(1,1),(4,1),(6,1),(3,1)],start=1):
        st=spread(st,adj)
        assert not st[v],('invalid ignition',m,t,v,st)
        ar=list(st);ar[v]=col;st=tuple(ar)
    assert all(st),(m,st)
    return sum(v==1 for v in st)

def main():
    # Enumerate every labelled intermediate state, not only the proposed witness.
    for m in range(1,7):
        states,finals,obtained=exhaustive_original(m)
        expected=(2 if m==1 else 3 if m==2 else m+2)
        assert obtained==expected,(m,obtained,expected)
        print('DIRECT_ALL_LABELLED_PROCESSES_OK',m,states,finals,obtained)
    # Independent arm-orbit enumeration extends the check to large branching orders.
    for m in range(3,61):
        states,finals,obtained=orbit_original(m)
        assert obtained==m+2,(m,obtained)
        assert explicit_schedule(m)==m+2
        if m in (3,4,5,10,20,40,60):
            print('ARM_ORBITS_AND_EXPLICIT_WITNESS_OK',m,states,finals,obtained)
    print('VERIFY_OK')
if __name__=='__main__':main()
