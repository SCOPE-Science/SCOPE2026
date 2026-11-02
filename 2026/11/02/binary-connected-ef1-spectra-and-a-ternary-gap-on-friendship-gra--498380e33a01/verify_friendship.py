"""Finite checks for the friendship-graph connected EF1 classification.
Run: python verify_friendship.py. Python 3 standard library only.
The exhaustive tests are independent of the all-order mathematical proof.
"""
from itertools import product
from collections import deque


def graph(k):
    n = 2 * k + 1
    adj = [set() for _ in range(n)]
    for j in range(k):
        a, b = 2*j+1, 2*j+2
        for u, v in ((0,a), (0,b), (a,b)):
            adj[u].add(v); adj[v].add(u)
    return adj


def connected(S, adj):
    if not S: return False
    seen = {min(S)}
    todo = [min(S)]
    while todo:
        for v in adj[todo.pop()] & S:
            if v not in seen:
                seen.add(v);todo.append(v)
    return seen == S


def ef1(blocks, weight):
    sums = [sum(weight[v] for v in B) for B in blocks]
    residuals = [x-max(weight[v] for v in B) for x,B in zip(sums,blocks)]
    return min(sums) >= max(residuals)


def check(blocks,k,weight):
    adj=graph(k);n=2*k+1
    assert set.union(*blocks) == set(range(n))
    assert sum(map(len,blocks)) == n
    assert all(connected(B,adj) for B in blocks)
    assert ef1(blocks,weight)


def binary_allocation(k,weight):
    assert all(x in (0,1) for x in weight)
    petals=[{2*j+1,2*j+2} for j in range(k)]
    classes={q:[P for P in petals if sum(weight[v] for v in P)==q] for q in (0,1,2)}
    r0,r1,r2=map(lambda q:len(classes[q]),(0,1,2))
    h=weight[0];total=sum(weight)
    blocks=[]
    def add_petals(Ps):
        for P in Ps:blocks.append(set(P))
    def add_split(Ps):
        for P in Ps:
            for v in P:blocks.append({v})
    if total<k:
        s=r0-r2-1
        assert s>=0
        center={0}|set().union(*(classes[0][s:]))
        blocks.append(center)
        add_petals(classes[0][:s]);add_petals(classes[1]);add_split(classes[2])
    elif total<2*k:
        if r0==0:
            selected=classes[1][0] if h else (classes[1]+classes[2])[0]
            blocks.append({0}|selected)
            add_petals([P for P in petals if P != selected])
        elif h:
            blocks.append({0}|set().union(*classes[0]))
            add_petals(classes[1]);add_split(classes[2][:r0-1]);add_petals(classes[2][r0-1:])
        elif r1:
            selected=classes[1][0]
            blocks.append({0}|set().union(*classes[0])|selected)
            add_petals(classes[1][1:]);add_split(classes[2][:r0]);add_petals(classes[2][r0:])
        else:
            selected=classes[2][0]
            a,b=sorted(selected)
            blocks.append({0,a}|set().union(*classes[0]))
            blocks.append({b})
            add_split(classes[2][1:r0]);add_petals(classes[2][r0:])
    else:
        if total==2*k+1:
            selected=petals[0]
        else:
            selected=classes[1][0] if h else petals[0]
        blocks.append({0}|selected)
        add_petals([P for P in petals if P!=selected])
    assert len(blocks)==k
    check(blocks,k,weight)
    return blocks


def split_connected(B,adj,weight):
    base=min(B);seen={base};todo=deque([base]);tree={base:set()}
    while todo:
        u=todo.popleft()
        for v in sorted(adj[u]&B):
            if v not in seen:
                seen.add(v);todo.append(v)
                tree.setdefault(u,set()).add(v)
                tree[v]={u}
    assert seen==B
    two=(sum(weight[v] for v in B)==2)
    for u in sorted(B):
        for v in sorted(tree[u]):
            if u>=v:continue
            S={u};todo=[u]
            while todo:
                z=todo.pop()
                for t in tree[z]:
                    if {z,t}=={u,v}:continue
                    if t not in S:S.add(t);todo.append(t)
            T=B-S
            if not two or (sum(weight[x] for x in S)==1 and sum(weight[x] for x in T)==1):
                return S,T
    raise AssertionError('No admissible connected split')


def refine_to_n(blocks,k,weight,num):
    adj=graph(k)
    blocks=[set(B) for B in blocks]
    while len(blocks)<num:
        sums=[sum(weight[v] for v in B) for B in blocks]
        if max(sums)==3:
            i=sums.index(3);B=blocks.pop(i)
            assert 0 in B
            blocks.extend(({0},B-{0}))
        else:
            candidates=[i for i,B in enumerate(blocks) if len(B)>1 and sum(weight[x] for x in B)==2]
            if not candidates:
                candidates=[i for i,B in enumerate(blocks) if len(B)>1]
            i=candidates[0];B=blocks.pop(i)
            S,T=split_connected(B,adj,weight)
            blocks.extend((S,T))
        check(blocks,k,weight)
    return blocks


def connected_partitions(k):
    adj=graph(k);n=2*k+1
    connected_masks=[]
    for mask in range(1,1<<n):
        S={i for i in range(n) if mask>>i&1}
        if connected(S,adj):connected_masks.append(mask)
    by_bit={b:[m for m in connected_masks if m&(1<<b)] for b in range(n)}
    def visit(rem,blocks):
        if rem==0:
            yield tuple(blocks);return
        first=(rem&-rem).bit_length()-1
        for m in by_bit[first]:
            if (m&rem)==m:
                yield from visit(rem^m,blocks+[m])
    return visit((1<<n)-1,[])


def exhaustive_negative(k,weight,agents):
    count=0
    for partition in connected_partitions(k):
        if len(partition)!=agents:continue
        count+=1
        sets=[{i for i in range(2*k+1) if m>>i&1} for m in partition]
        assert not ef1(sets,weight)
    assert count>0
    return count


def main():
    checked=0
    for k in range(3,6):
        for weight in product((0,1),repeat=2*k+1):
            alloc=binary_allocation(k,weight)
            for n in range(k,2*k+2):
                check(refine_to_n(alloc,k,weight,n),k,weight)
                checked+=1
        print('binary family checked k=',k,flush=True)
    for k in range(3,6):
        v=[1]+[1,0]*k
        for n in range(2,k):
            print('lower-spectrum',k,n,exhaustive_negative(k,v,n),flush=True)
    for k in (4,5):
        v=[1]+[0,1]*(k-1)+[2,2]
        print('ternary witness',k,exhaustive_negative(k,v,k),flush=True)
    print('PASS: validated',checked,'binary size/valuation cases; tested explicit negative witnesses')

if __name__=='__main__':main()
