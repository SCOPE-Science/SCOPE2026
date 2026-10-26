from itertools import product

def state_data(k):
    q=2**k
    states=[(r,0) for r in range(q)]
    for r in range(q):
        for subset in range(1<<q):
            if subset&~(1<<r): states.append((r,subset))
    # terminal state (r,0); rooted states (r,S), where S contains off-color leaf
    ix={s:i for i,s in enumerate(states)}
    R=[]
    for i,(r,S) in enumerate(states):
        targets={i}
        for s in range(q):
            if (S>>s)&1: targets.add(ix[(s,0)])
        R.append(targets)
    return states,R

def stabilize(k):
    states,R=state_data(k)
    q=2**k
    cells=[tuple(i for i,(r,_) in enumerate(states) if r==c) for c in range(q)]
    stages=[len(cells)]
    while True:
        new=[]
        for cell in cells:
            bins={}
            for i in cell:
                sig=tuple(int(bool(R[i]&set(b))) for b in cells)
                bins.setdefault(sig,[]).append(i)
            new.extend(tuple(x) for x in bins.values())
        if len(new)==len(cells):break
        cells=new;stages.append(len(cells))
    return len(states),stages,len(cells)
for k in range(1,4):
    n,stages,classes=stabilize(k)
    print(k,n,stages,classes,'expected',2**k*(2**(2**k)-1))
    assert classes==n

# k=1: explicit modal subalgebra closure (Boolean operations and Diamond)
states,R=state_data(1); m=len(states); whole=(1<<m)-1
G={0,whole}
for bit in range(1):
    mask=sum(1<<i for i,(r,s) in enumerate(states) if (r>>bit)&1)
    G.add(mask);G.add(mask^whole)
while True:
    new=set(G)
    for a in G:
        diamond=sum(1<<i for i,targets in enumerate(R) if any((a>>j)&1 for j in targets))
        new.update([diamond,diamond^whole])
        for b in G:new.update([a&b,a|b])
    if len(new)==len(G):break
    G=new
print('k=1 Boolean modal free universe',len(G),'expected',2**m)
assert len(G)==2**m
print('TWO_LEVEL_MODAL_TYPES_EXACT_OK')
