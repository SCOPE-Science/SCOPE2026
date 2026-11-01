"""Exact checks of the facet-network product spectral formula.

Only sympy is required (tested with sympy 1.13+).
All entries are rational, so all characteristic polynomials are exact.
The mathematical proof in RESULT.md covers arbitrary polytopes, not just these examples.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from sympy import Matrix, Rational, Symbol, expand

def factor_data(N):
    if N == 4:
        return Rational(1, 2), {1:2, 2:1}
    if N == 6:
        return Rational(1), {1:2, 3:2, 4:1}
    raise ValueError('only exact rational square and hexagon checks')

def full_operator(Ns):
    r = len(Ns)
    offsets=[sum(Ns[:i]) for i in range(r)]
    labels=[(i,a) for i,N in enumerate(Ns) for a in range(N)]
    M = Matrix.zeros(len(labels))
    for k,(i,a) in enumerate(labels):
        rho,_ = factor_data(Ns[i])
        M[k,k] = 2*rho + 2*(r-1)
        for l,(j,b) in enumerate(labels):
            if l==k:continue
            if j==i and ((a-b)%Ns[i] in (1,Ns[i]-1)):
                M[k,l] = -rho
            elif i!=j:
                M[k,l] = -Rational(2,Ns[j])
    return M

def expected(Ns):
    n=2*len(Ns)
    E=Counter({0:1,n:len(Ns)-1})
    for N in Ns:
        _, spec =factor_data(N)
        for eig,m in spec.items():E[eig+n-2] +=m
    return E

def even_expected(Ns):
    n=2*len(Ns)
    E=Counter({0:1,n:len(Ns)-1})
    for N in Ns:
        if N==4:E[n]+=1
        elif N==6:E[n+1]+=2
    return E

def exact_test(Ns):
    A=full_operator(Ns)
    eigen=A.eigenvals()
    observed=Counter({int(k):int(v) for k,v in eigen.items()})
    expect=expected(Ns)
    assert observed==expect,(Ns,observed,expect)
    # Even subspace: variables at antipodal normals must be equal.
    labels=[(i,a) for i,N in enumerate(Ns) for a in range(N)]
    evenpairs=[(i,a) for i,N in enumerate(Ns) for a in range(N//2)]
    full_pos={lab:k for k,lab in enumerate(labels)}
    embed=Matrix.zeros(len(labels),len(evenpairs))
    mass=Matrix.diag(*[Rational(2,Ns[i]) for i,a in labels])
    for j,(i,a) in enumerate(evenpairs):
        embed[full_pos[(i,a)],j]=1
        embed[full_pos[(i,a+Ns[i]//2)],j]=1
    Me=embed.T*mass*embed
    Le=embed.T*mass*A*embed
    evenop=Me.inv()*Le
    even_spectrum=Counter({int(k):int(v) for k,v in evenop.eigenvals().items()})
    assert even_spectrum==even_expected(Ns),(Ns,even_spectrum,even_expected(Ns))
    # Mass self-adjointness, constant eigenvector and direct even/odd count.
    assert mass*A == (mass*A).T
    assert A*Matrix.ones(len(labels),1)==Matrix.zeros(len(labels),1)
    print('PASSED',Ns,'total facets',len(labels),'full',dict(sorted(observed.items())),
          'even',dict(sorted(even_spectrum.items())))

def octahedron_square_test():
    """Build a 3D octahedron times a unit-area square from its actual facet data."""
    from itertools import product
    signs=list(product((-1,1),repeat=3))
    labels=[('o',s) for s in signs]+[('s',j) for j in range(4)]
    m_o=Rational(1,2)  # octahedron: support 1/sqrt(3), facet area sqrt(3)/2
    c_o=Rational(1,2)  # adjacent octahedron facets, by ridge and normal angle
    v_o=Rational(4,3)  # octahedron volume
    m_s=Rational(1,2)  # square facet mass with square area one
    c_s=Rational(1,4)  # square adjacent facet conductance
    masses=[m_o]*8+[m_s*v_o]*4
    C=Matrix.zeros(12)
    for i,(typ,a) in enumerate(labels):
        for j,(typeb,b) in enumerate(labels):
            if i>=j:continue
            if typ==typeb=='o' and sum(x!=y for x,y in zip(a,b))==1:
                C[i,j]=C[j,i]=c_o
            elif typ==typeb=='s' and ((a-b)%4 in (1,3)):
                C[i,j]=C[j,i]=c_s*v_o
            elif typ!=typeb:
                C[i,j]=C[j,i]=m_o*m_s
    L=Matrix.zeros(12)
    for i in range(12):
        for j in range(12):
            if i!=j:
                L[i,j]=-C[i,j]
                L[i,i]+=C[i,j]
    W=Matrix.diag(*masses)
    A=W.inv()*L
    assert W*A==(W*A).T
    observed=Counter({int(k):int(v) for k,v in A.eigenvals().items()})
    expected=Counter({0:1,4:5,5:2,6:3,8:1})
    assert observed==expected,(observed,expected)
    # The antipodal pairing on octahedral facets negates sign vectors.
    even_embed=Matrix.zeros(12,6)
    for j,s in enumerate(signs):
        if s[0]!=-1:continue
        k=sum(1 for a in signs[:j] if a[0]==-1)
        even_embed[j,k]=1
        even_embed[signs.index(tuple(-x for x in s)),k]=1
    for j in range(2):
        even_embed[8+j,j+4]=1
        even_embed[8+j+2,j+4]=1
    Em=even_embed.T*W*even_embed
    Ee=even_embed.T*L*even_embed
    eig=Counter({int(k):int(v) for k,v in (Em.inv()*Ee).eigenvals().items()})
    assert eig==Counter({0:1,5:2,6:3}),eig
    print('PASSED',('octahedron','square'),'full',dict(sorted(observed.items())),
          'even',dict(sorted(eig.items())))

if __name__=='__main__':
    for Ns in ((4,4),(4,6),(6,6),(4,4,4),(4,6,4),(6,6,6)):
        exact_test(Ns)
    octahedron_square_test()
