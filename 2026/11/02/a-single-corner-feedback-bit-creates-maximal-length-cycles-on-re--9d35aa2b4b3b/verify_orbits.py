"""Independent direct state evolution on a 3x7 binary parity grid."""
def evolve(v,n=7,feedback=True):
    out=0
    for i in range(3):
        for j in range(n):
            a=0
            for k,l in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0<=k<3 and 0<=l<n:a ^= (v>>(k*n+l))&1
            if feedback and i==j==0:a^=v&1
            out |= a<<(i*n+j)
    return out

def rank(vs):
    piv={}
    for v in vs:
        while v:
            k=v.bit_length()-1
            if k not in piv:piv[k]=v;break
            v^=piv[k]
    return len(piv)

n=7;dim=21
states=[1<<k for k in range(dim)]
for _ in range(30):states=[evolve(v) for v in states]
assert rank(states)==7
basis=[];rank_seen=0
for v in states:
    new=rank(basis+[v])
    if new>rank_seen:basis.append(v);rank_seen=new
assert len(basis)==7
nonzero=set()
for z in range(1,1<<7):
    v=0
    for j,b in enumerate(basis):
        if (z>>j)&1:v ^=b
    assert v not in nonzero
    nonzero.add(v)
    w=evolve(v)
    for t in range(1,127):
        assert w!=v,('early return',z,t)
        w=evolve(w)
    assert w==v,('late return',z)
assert len(nonzero)==127
for v in basis:assert evolve(v,feedback=False)!=v
print('VERIFY_ORBITS_OK: 127 distinct nonzero periodic states, all primitive period 127; 7-dimensional periodic space')
