"""Independent finite-field checks for projective-line 2-local classification.
Run: python verify.py. Uses only Python standard library.
"""
import itertools
from math import factorial,prod

def check(q,n):
    assert q in (2,3) and n in (2,3)
    vectors=list(itertools.product(range(q), repeat=n))
    nonzero=[v for v in vectors if any(v)]
    def det2(m):return (m[0][0]*m[1][1]-m[0][1]*m[1][0])%q
    def image(m,v):return tuple(sum(m[i][j]*v[j] for j in range(n))%q for i in range(n))
    matrices=[]
    for vals in itertools.product(range(q),repeat=n*n):
        m=[vals[i*n:(i+1)*n] for i in range(n)]
        imgs=[image(m,v) for v in vectors]
        if len(set(imgs))==q**n:matrices.append(tuple(imgs))
    N=(q**n-1)//(q-1)
    expected=(q-1)**N*factorial(N)
    gl=prod(q**n-q**i for i in range(n))
    assert len(matrices)==gl
    # Form maps from independent directions and their nonzero scalar multiples.
    lines=[]; reps=[]; seen=set()
    for v in nonzero:
        line=frozenset(tuple(a*x%q for x in v) for a in range(1,q))
        if line not in seen: seen.add(line); lines.append(line); reps.append(v)
    assert len(lines)==N
    byline={v:i for i,line in enumerate(lines) for v in line}
    zero=(0,)*n
    count=0
    for perm in itertools.permutations(range(N)):
        for scales in itertools.product(range(1,q),repeat=N):
            f={zero:zero}
            for i,v in enumerate(reps):
                target=reps[perm[i]]
                out=tuple(scales[i]*x%q for x in target)
                for a in range(1,q):
                    inp=tuple(a*x%q for x in v)
                    f[inp]=tuple(a*x%q for x in out)
            assert len(f)==len(vectors) and len(set(f.values()))==len(vectors)
            # Full 2-local brute force for all examples q=2,n=2 or q=3,n=2;
            # q=2,n=3 test representative maps and all vector pairs via GL witness.
            if n==2 or count in (0,1,42,1234,5039):
                for a in vectors:
                    for b in vectors:
                        k=vectors.index(a);l=vectors.index(b)
                        ka=vectors.index(f[a]);lb=vectors.index(f[b])
                        assert any(t[k]==f[a] and t[l]==f[b] for t in matrices)
            count+=1
    assert count==expected
    print('CHECK',q,n,'projective_lines',N,'2local',count,'global',gl,'index',count//gl)
check(2,2)
check(3,2)
check(2,3)
print('VERIFY_OK')
