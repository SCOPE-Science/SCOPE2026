"""Independent finite checks for the Cerny subset extension-time formula.
Standard library only.  Run: python verify.py.
"""
from collections import Counter, deque
from itertools import product


def inverse_a(n, s):
    return (s >> 1) | ((s & 1) << (n-1))


def inverse_b(n, s):
    # b(0)=1 and b(q)=q for q>0.
    if s & 2:
        return s | 1
    return s & ~1


def bfs_minimum(n, s):
    k=s.bit_count()
    seen={s}; q=deque([(s,0)])
    while q:
        x,t=q.popleft()
        if x.bit_count()>k:return t
        for y in (inverse_a(n,x),inverse_b(n,x)):
            if y not in seen:
                seen.add(y);q.append((y,t+1))
    raise AssertionError('no extension')


def boundary_minimum(n, s):
    for j in range(n):
        if ((s>>j)&1)==0 and ((s>>((j+1)%n))&1)==1:
            return j+1
    raise AssertionError('nontrivial subset must have a boundary')


def predicted_count(n,t):
    return t*2**(n-t-1) if 1<=t<n else (n-1 if t==n else 0)


def direct_forward_maps(n):
    a=tuple((q+1)%n for q in range(n))
    b=tuple(1 if q==0 else q for q in range(n))
    identity=tuple(range(n))
    current=[('', identity)]
    yield 0,current
    for t in range(1,n+1):
        new=[]
        for word, mapping in current:
            for name,letter in (('a',a),('b',b)):
                new.append((word+name,tuple(letter[mapping[q]] for q in range(n))))
        current=new
        yield t,current


def direct_shortest_all(n):
    full=(1<<n)-1
    ans={}
    for t,maps in direct_forward_maps(n):
        for s in range(1,full):
            if s in ans:continue
            size=s.bit_count()
            hits=[word for word,mapping in maps if sum((s>>mapping[q])&1 for q in range(n))>size]
            if hits:
                assert hits==['b'+'a'*(t-1)],(n,s,t,hits)
                ans[s]=t
    assert len(ans)==full-1
    return ans


def main():
    for n in range(2,14):
        full=(1<<n)-1
        data={s:bfs_minimum(n,s) for s in range(1,full)}
        counted=Counter(data.values())
        for t in range(1,n+1):
            assert counted[t]==predicted_count(n,t),(n,t,counted[t])
        for s,t in data.items():
            assert t==boundary_minimum(n,s),(n,s,t)
        stuck={s for s,t in data.items() if t==n}
        expected={sum(1<<q for q in range(k)) for k in range(1,n)}
        assert stuck==expected,(n,stuck,expected)
        if n<=8:
            direct=direct_shortest_all(n)
            assert direct==data,('independent direct forward check',n)
        print(f'n={n} subsets={full-1} stuck={len(stuck)} histogram='+','.join(str(counted[t]) for t in range(1,n+1)))
    print('VERIFY_OK')
if __name__=='__main__':main()
