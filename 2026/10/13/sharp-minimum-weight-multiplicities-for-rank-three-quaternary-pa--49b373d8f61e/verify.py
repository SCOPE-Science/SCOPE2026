"""Exact quaternary locality-one rank-three minimum-weight multiplicity census.

Pure Python 3.9+; no external dependencies. Time O(2^21*5).
"""
from array import array
from itertools import product
from math import comb

TARGET = {
    7:(3,2520),8:(6,10080),9:(9,1120),10:(15,10080),
    11:(21,2520),12:(28,210),13:(40,1680),14:(52,2520),
    15:(65,336),16:(80,21),17:(104,105),18:(128,210),
    19:(153,210),20:(180,21),21:(210,1),
}

def multiply(a,b):
    # GF(4) = F2[t]/(t^2+t+1), represented as 0,1,t,1+t.
    z=0
    for shift in range(2):
        if (b>>shift)&1:
            z ^= a << shift
    if z & 4:
        z ^= 7  # reduce t^2 = t+1
    return z

def dot(v,w):
    out=0
    for a,b in zip(v,w):
        out ^= multiply(a,b)
    return out

# Build exactly the 21 normalized projective points and 21 dual lines.
points = sorted({min(tuple(multiply(s,x) for x in v) for s in (1,2,3))
                 for v in product(range(4),repeat=3) if v != (0,0,0)})
assert len(points)==21
lines = []
for normal in points:
    line=sum(1<<i for i,p in enumerate(points) if dot(normal,p)==0)
    assert line.bit_count()==5
    lines.append(line)
assert len(set(lines))==21
assert all(sum(bool((line>>i)&1 and (line>>j)&1) for line in lines)==1
           for i in range(21) for j in range(i+1,21))
assert all(sum(bool((line>>i)&1) for line in lines)==5 for i in range(21))

def moments_lower_bound(u):
    # Independent integer relaxation of projective-line occupancy equations.
    configs=[]
    for n3 in range(22):
      for n4 in range(22-n3):
       for n5 in range(22-n3-n4):
        n2=comb(u,2)-3*n3-6*n4-10*n5
        n1=5*u-2*n2-3*n3-4*n4-5*n5
        n0=21-n1-n2-n3-n4-n5
        if min(n0,n1,n2)>=0 and max(n0,n1,n2,n3,n4,n5)<=21:
            configs.append((n3+4*n4+10*n5,(n0,n1,n2,n3,n4,n5)))
    lower=min(c for c,_ in configs)
    minimizers=[profile for c,profile in configs if c==lower]
    return lower,minimizers

for u in range(7,22):
    lb,profiles=moments_lower_bound(u)
    expected=TARGET[u][0]
    if u in (10,11):
        assert lb==expected-1
        assert profiles==({10:[(2,2,3,14,0,0)],11:[(2,1,1,16,1,0)]}[u])
    else:
        assert lb==expected,(u,lb,expected)

# Independently count collinear triples and enumerate subset optimum.
line_through=[]
for j in range(21):
    through=[L^(1<<j) for L in lines if L & (1<<j)]
    assert len(through)==5
    line_through.append(tuple(through))

minscore=[999]*22
n_opt=[0]*22
rep=[0]*22
score=array('B',[0])*(1<<21)
for mask in range(1,1<<21):
    bit=mask & -mask
    j=bit.bit_length()-1
    rest=mask ^ bit
    # New triples contain the newly inserted point and two old collinear points.
    inc=0
    for line in line_through[j]:
        b=(rest&line).bit_count()
        inc += b*(b-1)//2
    val=score[rest]+inc
    assert val<=210
    score[mask]=val
    u=mask.bit_count()
    if val<minscore[u]:
        minscore[u]=val;n_opt[u]=1;rep[u]=mask
    elif val==minscore[u]:
        n_opt[u]+=1

# A second route checks the representative directly using the 21 line occupancies.
for u,(want,count) in TARGET.items():
    assert minscore[u]==want and n_opt[u]==count,(u,minscore[u],n_opt[u])
    witness=rep[u]
    occ=[(witness&line).bit_count() for line in lines]
    direct=sum(comb(a,3) for a in occ)
    assert direct==want
    assert sum(occ)==5*u
    assert sum(comb(a,2) for a in occ)==comb(u,2)

# Independent coding-theoretic check: enumerate every kernel codeword in four
# small parameter instances. This does not reuse the triple-incidence DP.
def enumerate_kernel_weight_three(u):
    selected=[points[i] for i in range(21) if rep[u]&(1<<i)]
    matrix=[[v[row] for v in selected] for row in range(3)]
    pivot_cols=[]
    for col in range(u):
        pivot=next((r for r in range(len(pivot_cols),3)
                    if matrix[r][col]!=0),None)
        if pivot is None: continue
        r=len(pivot_cols)
        matrix[r],matrix[pivot]=matrix[pivot],matrix[r]
        scale=multiply(matrix[r][col],matrix[r][col])  # inverse in GF(4)^*
        matrix[r]=[multiply(scale,v) for v in matrix[r]]
        for rr in range(3):
            if rr!=r and matrix[rr][col]:
                fac=matrix[rr][col]
                matrix[rr]=[x^multiply(fac,y) for x,y in zip(matrix[rr],matrix[r])]
        pivot_cols.append(col)
        if len(pivot_cols)==3: break
    assert len(pivot_cols)==3
    free=[i for i in range(u) if i not in pivot_cols]
    counted=0
    for values in product(range(4),repeat=len(free)):
        word=[0]*u
        for c,v in zip(free,values):word[c]=v
        for row,piv in enumerate(pivot_cols):
            word[piv]=0
            for c in free: word[piv]^=multiply(matrix[row][c],word[c])
        for coord in range(3):
            value=0
            for c,coefficient in enumerate(word):
                value ^= multiply(selected[c][coord],coefficient)
            assert value==0
        if sum(bool(x) for x in word)==3: counted+=1
    return counted
for u in (7,8,10,11):
    assert enumerate_kernel_weight_three(u)==3*TARGET[u][0]

# The two strict moment-bound exceptions have short geometric obstructions:
# n0=2 disjoint selected-point-free lines, meeting at an unselected point p.
# Through p the other three lines contain all u selected points; with each
# carrying at most four selected points, u=10 implies some 4-secant and
# u=11 implies at least two distinct 4-secants. The respective moment minima
# demand no 4-secant and only one 4-secant, a contradiction.
for u in (10,11):
    lb,profiles=moments_lower_bound(u)
    assert len(profiles)==1 and profiles[0][0]==2
    assert (u==10 and profiles[0][4]==0) or (u==11 and profiles[0][4]==1)

print('u\tmin_collinear_triples\tmin_A6\tcount_optimal_point_subsets\trepresentative_indices')
for u,(want,count) in TARGET.items():
    print(u,want,3*want,count,','.join(str(i) for i in range(21) if (rep[u]>>i)&1),sep='\t')
print('VERIFY_OK')
