"""Independent abstract-state verifier for friendship domination moves.

Creates the Boolean-ball/transversal/doubled-blade model without testing
any domination predicate. Checks exact all-pairs distance formulas against
breadth-first search on the abstract graph. Python 3 standard library only.
"""
from collections import defaultdict, deque
from itertools import combinations, product


def make(r):
    full=(1<<(2*r))-1
    trans=[]
    for selector in product((0,1),repeat=r):
        trans.append(sum(1<<(2*i+bit) for i,bit in enumerate(selector)))
    hstates=[('H',sum(1<<i for i in picked))
             for k in range(r+1) for picked in combinations(range(2*r),k)]
    lstates=[('L',t) for t in trans]
    ustates=sorted({('U', t | (3<<(2*i))) for t in trans for i in range(r)})
    states=hstates+lstates+ustates
    index={s:i for i,s in enumerate(states)}
    assert len(states)==len(index)
    edges=set()
    def add(a,b):
        i,j=index[a],index[b]
        edges.add((min(i,j),max(i,j)))
    for kind,mask in hstates:
        if mask.bit_count()<r:
            for i in range(2*r):
                if not (mask & (1<<i)):
                    add(('H',mask),('H',mask | (1<<i)))
    for _,t in lstates:
        add(('H',t),('L',t))
        for i in range(r):
            add(('L',t),('U',t | (3 << (2*i))))
    adj=[[] for s in states]
    for i,j in edges:
        adj[i].append(j);adj[j].append(i)
    return states,adj


def double_blade(u,r):
    bs=[j for j in range(r) if ((u>>(2*j))&3)==3]
    assert len(bs)==1
    return bs[0]


def floors(u,r):
    i=double_blade(u,r)
    return (u^(1<<(2*i)),u^(1<<(2*i+1)))


def hamming(x,y):
    return (x^y).bit_count()


def predicted(s,t,r):
    kind,x=s
    kind2,y=t
    if kind=='H' and kind2=='H':
        return hamming(x,y)
    if kind2=='H' and kind!='H':
        return predicted(t,s,r)
    if kind=='H' and kind2=='L':
        return 1+hamming(x,y)
    if kind=='H' and kind2=='U':
        return 2+min(hamming(x,b) for b in floors(y,r))
    if kind=='L' and kind2=='L':
        return hamming(x,y)
    if kind=='U' and kind2=='L':
        return predicted(t,s,r)
    if kind=='L' and kind2=='U':
        return 1+min(hamming(x,b) for b in floors(y,r))
    assert kind==kind2=='U'
    if x==y:return 0
    if double_blade(x,r)==double_blade(y,r):
        return hamming(x,y)+2
    return hamming(x,y)


def distance_vector(adj,src):
    d=[-1]*len(adj);d[src]=0
    q=deque([src])
    while q:
        a=q.popleft()
        for b in adj[a]:
            if d[b]==-1:d[b]=d[a]+1;q.append(b)
    assert all(x>=0 for x in d)
    return d


def main():
    for r in range(2,7):
        states,adj=make(r)
        if r<=5:
            origins=range(len(states))
        else:
            types={}
            for i,(kind,x) in enumerate(states):
                if kind=='H':
                    pair_values=[(x>>(2*j))&3 for j in range(r)]
                    a=sum(v==1 or v==2 for v in pair_values)
                    b=sum(v==3 for v in pair_values)
                    key=('H',a,b)
                else:key=(kind,)
                types.setdefault(key,i)
            origins=types.values()
        nchecks=0
        for a in origins:
            distances=distance_vector(adj,a)
            for b,t in enumerate(states):
                exp=predicted(states[a],t,r)
                got=distances[b]
                assert exp==got,(r,states[a],t,exp,got)
                nchecks+=1
        print(f'EXACT_METRIC_PASS r={r} states={len(states)} checks={nchecks}',flush=True)
    print('ALL_ABSTRACT_METRIC_CHECKS_PASS')


if __name__=='__main__':
    main()
