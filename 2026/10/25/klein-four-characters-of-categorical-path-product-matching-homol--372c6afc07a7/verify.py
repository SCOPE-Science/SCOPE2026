"""Independent finite tests for reflection characters of direct-product path matching complexes.
No external files or packages are required; execute with Python 3.9+.
"""
from functools import lru_cache

def edges(length):
    return tuple(sorted(tuple(sorted(((i,j),(i+1,jj))))
      for i in range(length-1) for j in range(3) for jj in range(3)
      if abs(j-jj)==1))

def transform(e, length, group):
    def image(p):
        i,j=p
        if group & 1:i=length-1-i
        if group & 2:j=2-j
        return i,j
    return tuple(sorted(map(image,e)))

def trace_from_edge_orbits(length,group):
    all_edges=edges(length)
    pending=set(all_edges); orbits=[]
    while pending:
        e=min(pending)
        f=transform(e,length,group)
        orbit=frozenset((e,f))
        assert orbit <= pending
        pending-=orbit
        vertices=[v for edge in orbit for v in edge]
        if len(set(vertices))!=2*len(orbit):continue
        mask=0
        for i,j in vertices:mask|=1<<(3*i+j)
        orbits.append(mask)
    @lru_cache(None)
    def recur(i,used):
        if i==len(orbits):return 1
        out=recur(i+1,used)
        if used & orbits[i]==0:out-=recur(i+1,used|orbits[i])
        return out
    return recur(0,0),len(orbits),recur.cache_info().currsize

def prediction(length,group):
    if length%2==0:
        r=length//2
        return 1 if group in (0,2) else (-1)**r
    r=(length-1)//2
    rank=2**(r+1)-1
    h=1 if r%2==0 else 2**((r+1)//2)-1
    hv=2**(r//2+1)-1 if r%2==0 else -h
    return (rank,h,1,hv)[group]

def transfer_matrix():
    eligible=[(0,1),(1,0),(1,2),(2,1)]
    T=[[0]*8 for _ in range(8)]
    for a in range(8):
        for mask in range(16):
            picked=[eligible[j] for j in range(4) if mask>>j &1]
            left=[i for i,j in picked];right=[j for i,j in picked]
            if len(left)!=len(set(left)) or len(right)!=len(set(right)):continue
            if any(a & (1<<i) for i in left):continue
            b=sum(1<<j for j in right)
            T[a][b]+=(-1)**len(picked)
    return T

def seq(length,terminal):
    T=transfer_matrix()
    state=[1]+[0]*7
    for _ in range(length-1):
        state=[sum(state[i]*T[i][j] for i in range(8)) for j in range(8)]
    return sum(state[j] for j in range(8) if terminal(j))

def predicted_seqs(t):
    if t%2:
        s=(t-1)//2;return (2**(s+1)-1,2**(s+1)-1,2**s)
    s=t//2;return (1,1-2**s,0)

if __name__=='__main__':
    count=0; maxstates=0
    for t in range(1,28):
        got=tuple(seq(t,condition) for condition in
          [lambda m:True,lambda m: not(m&2),lambda m:not(m&3)])
        want=predicted_seqs(t)
        assert got==want,('TRANSFER',t,got,want)
    print('TRANSFER_MATRIX_EXACT_27_OK')
    for length in range(2,15):
        chars=[prediction(length,g) for g in range(4)]
        for a,b in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            multiplicity=(chars[0]+a*chars[1]+b*chars[2]+a*b*chars[3])//4
            assert (chars[0]+a*chars[1]+b*chars[2]+a*b*chars[3])%4==0
            assert multiplicity>=0
        for group in ((0,1,2,3) if length<=9 else (1,2,3)):
            actual,_,states=trace_from_edge_orbits(length,group)
            expected=prediction(length,group)
            assert actual==expected,('ORBIT',length,group,actual,expected)
            count+=1; maxstates=max(states,maxstates)
    print('GROUP_ACTION_ORBIT_SUMS_VERIFIED',count,'MAX_STATES',maxstates)
