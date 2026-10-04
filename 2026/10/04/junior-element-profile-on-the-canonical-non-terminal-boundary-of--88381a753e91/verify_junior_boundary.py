def ages_for_chart(m, r, c):
    if m <= 1:
        return []
    return [(r*k + ((k*c) % m), m) for k in range(1, m)]

def direct_status(r,a,b):
    can=True; term=True
    for num,den in ages_for_chart(a,r,b):
        if num < den: can=False
        if num <= den: term=False
    for num,den in ages_for_chart(b,r,a):
        if num < den: can=False
        if num <= den: term=False
    return can,term

def junior_lists(r,a,b):
    A=[]; B=[]
    if a>1:
        A=[k for k in range(1,a) if r*k + ((k*b)%a) == a]
    if b>1:
        B=[k for k in range(1,b) if r*k + ((k*a)%b) == b]
    return A,B

def predicted_junior_lists(r,a,b):
    d=b-a
    assert d==r or a==r+d
    if d==r:
        if a<r:
            return [], [1]
        if a==r:
            return [1], [1,2]
        if a<2*r:
            return [], [1,2]
        assert a==2*r
        return [1,2], [1,2,3]
    if d==0:
        return [1],[1]
    return [1],[]

# Full direct Reid-Tai replay in a box containing the canonical triangle.
for r in range(2,31):
    boundary=[]
    for a in range(1,2*r+1):
        for b in range(a,3*r+1):
            can,term=direct_status(r,a,b)
            expected_can=(b-a<=r and a<=r+(b-a))
            expected_term=(b-a<r and a<r+(b-a))
            assert can==expected_can, (r,a,b,'can',can,expected_can)
            assert term==expected_term, (r,a,b,'term',term,expected_term)
            if can and not term:
                A,B=junior_lists(r,a,b)
                pA,pB=predicted_junior_lists(r,a,b)
                assert A==pA and B==pB, (r,a,b,A,B,pA,pB)
                boundary.append((a,b,len(A)+len(B)))
    assert len(boundary)==3*r
    hist={}
    for _,_,j in boundary:
        hist[j]=hist.get(j,0)+1
    assert hist=={1:2*r-2,2:r,3:1,5:1}, (r,hist)
    assert sum(j for _,_,j in boundary)==4*r+6

# Boundary-only direct replay much farther out.
for r in range(2,301):
    vals=[]
    for a in range(1,2*r+1):
        b=a+r
        A,B=junior_lists(r,a,b)
        assert (A,B)==predicted_junior_lists(r,a,b)
        vals.append(len(A)+len(B))
    for d in range(0,r):
        a=r+d; b=r+2*d
        A,B=junior_lists(r,a,b)
        assert (A,B)==predicted_junior_lists(r,a,b)
        vals.append(len(A)+len(B))
    hist={}
    for j in vals:
        hist[j]=hist.get(j,0)+1
    assert hist=={1:2*r-2,2:r,3:1,5:1}
    assert sum(vals)==4*r+6

print('VERIFY_OK')
