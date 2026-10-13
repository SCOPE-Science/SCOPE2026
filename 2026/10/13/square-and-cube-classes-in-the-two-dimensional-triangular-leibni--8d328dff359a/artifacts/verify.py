from itertools import product
from collections import Counter
from math import gcd

# Vectors (e,f), tensors coordinates ee,ef,fe,ff.

def brA(x,y,q):
    return ((x[1]*y[1])%q,0)

def brB(x,y,q):
    return ((x[1]*(y[0]+y[1]))%q,0)

def phiA(t,u,q): # columns phi(e),phi(f)
    return (t*t%q,u%q,0,t%q)

def phiB(t,q):
    return (t%q,(t-1)%q,0,1)

def det(M,q): return (M[0]*M[3]-M[1]*M[2])%q

def inv(M,q):
    z=pow(det(M,q),-1,q)
    return (M[3]*z%q,-M[1]*z%q,-M[2]*z%q,M[0]*z%q)

def mv(M,x,q):
    return ((M[0]*x[0]+M[1]*x[1])%q,(M[2]*x[0]+M[3]*x[1])%q)

def is_aut(M,br,q):
    if det(M,q)==0:return False
    E=((1,0),(0,1))
    for x,y in product(E,repeat=2):
        if mv(M,br(x,y,q),q)!=br(mv(M,x,q),mv(M,y,q),q):return False
    return True

def tensor_push(M,T,q):
    # T dict pair indices -> coefficient; apply M⊗M
    out=[0]*4
    for i in range(2):
      for j in range(2):
        coeff=T[2*i+j]%q
        if not coeff:continue
        col_i=(M[i],M[2+i])
        col_j=(M[j],M[2+j])
        for a in range(2):
          for b in range(2):
            out[2*a+b]=(out[2*a+b]+coeff*col_i[a]*col_j[b])%q
    return tuple(out)

def lin_delta(delta,x,q):
    # delta=(delta(e),delta(f)), each tensor tuple len4
    return tuple((x[0]*delta[0][k]+x[1]*delta[1][k])%q for k in range(4))

def push_delta(delta,M,q):
    Mi=inv(M,q)
    E=((1,0),(0,1)); out=[]
    for x in E:
        pre=mv(Mi,x,q)
        out.append(tensor_push(M,lin_delta(delta,pre,q),q))
    return tuple(out)

def dA(g,q):
    return ((0,0,0,0),(g%q,0,0,0))

def dBI(A,g,q):
    return ((0,0,0,0),(A%q,g%q,0,0))

def dBII(l,q):
    T=(0,1,-1%q,0)
    T=tuple((l*z)%q for z in T)
    return (T,T)

# Verify displayed coalgebras satisfy Definition 2.4 by direct tensor arithmetic.
def coalgebra_identity(delta,q):
    # For each basis x, check (id⊗δ)δ = (δ⊗id)δ + term b1⊗a⊗b2.
    for xidx in range(2):
        D=delta[xidx]
        lhs=[0]*8; rhs=[0]*8
        for a in range(2):
          for b in range(2):
            coeff=D[2*a+b]%q
            if not coeff:continue
            db=delta[b]
            da=delta[a]
            for b1 in range(2):
              for b2 in range(2):
                lhs[4*a+2*b1+b2]=(lhs[4*a+2*b1+b2]+coeff*db[2*b1+b2])%q
                rhs[4*b1+2*a+b2]=(rhs[4*b1+2*a+b2]+coeff*db[2*b1+b2])%q
            for a1 in range(2):
              for a2 in range(2):
                rhs[4*a1+2*a2+b]=(rhs[4*a1+2*a2+b]+coeff*da[2*a1+a2])%q
        if tuple(lhs)!=tuple(rhs):return False
    return True

def bracket_basis(br,i,j,q): return br((1 if i==0 else 0,1 if i==1 else 0),(1 if j==0 else 0,1 if j==1 else 0),q)

def compatibility(delta,br,q):
    E=((1,0),(0,1))
    # Eq 4 and Eq 5 directly from source Definition 2.4.
    for xi,x in enumerate(E):
      for yi,y in enumerate(E):
        Dx=delta[xi]; Dy=delta[yi]
        eq4=[0]*4
        # x2 ⊗ [x1,y]
        for x1 in range(2):
          for x2 in range(2):
            c=Dx[2*x1+x2]
            z=br(E[x1],y,q)
            for j in range(2): eq4[2*x2+j]=(eq4[2*x2+j]+c*z[j])%q
        # - [y1,x] ⊗ y2
        for y1 in range(2):
          for y2 in range(2):
            c=Dy[2*y1+y2]
            z=br(E[y1],x,q)
            for i in range(2): eq4[2*i+y2]=(eq4[2*i+y2]-c*z[i])%q
        if any(z%q for z in eq4): return False
        # Eq5 RHS
        rhs=[0]*4
        def add_tensor(v,w,coef=1):
            for i in range(2):
              for j in range(2): rhs[2*i+j]=(rhs[2*i+j]+coef*v[i]*w[j])%q
        for x1 in range(2):
          for x2 in range(2):
            c=Dx[2*x1+x2]
            add_tensor(E[x1],br(E[x2],y,q),c)
            add_tensor(br(y,E[x1],q),E[x2],-c)
            add_tensor(br(E[x1],y,q),E[x2],-c)
            add_tensor(E[x2],br(E[x1],y,q),c)
            add_tensor(br(y,E[x2],q),E[x1],-c)
            add_tensor(br(E[x2],y,q),E[x1],-c)
        for y1 in range(2):
          for y2 in range(2):
            c=Dy[2*y1+y2]
            add_tensor(br(x,E[y1],q),E[y2],c)
            add_tensor(E[y1],br(x,E[y2],q),c)
        left=lin_delta(delta,br(x,y,q),q)
        if tuple(z%q for z in rhs)!=left:return False
    return True

for q in (2,3,5,7,11):
    mats=list(product(range(q),repeat=4))
    autA={M for M in mats if is_aut(M,brA,q)}
    predA={phiA(t,u,q) for t in range(1,q) for u in range(q)}
    assert autA==predA
    autB={M for M in mats if is_aut(M,brB,q)}
    predB={phiB(t,q) for t in range(1,q)}
    assert autB==predB

    # Verify every displayed base-changed structure is a Leibniz bialgebra.
    for g in range(q):
        D=dA(g,q); assert coalgebra_identity(D,q) and compatibility(D,brA,q)
    for A,g in product(range(q),repeat=2):
        D=dBI(A,g,q); assert coalgebra_identity(D,q) and compatibility(D,brB,q)
    for l in range(q):
        D=dBII(l,q); assert coalgebra_identity(D,q) and compatibility(D,brB,q)

    # Orbit A.
    SA={dA(g,q) for g in range(q)}
    seen=set(); orbitsA=[]
    for D in SA:
        if D in seen:continue
        O={push_delta(D,M,q) for M in autA}
        assert O<=SA
        seen|=O; orbitsA.append(O)
    g3=gcd(3,q-1)
    assert len(orbitsA)==1+g3

    # Orbit B on union of Type I and Type II, zero deduplicated.
    SBI={dBI(A,g,q) for A,g in product(range(q),repeat=2)}
    SBII={dBII(l,q) for l in range(q)}
    SB=SBI|SBII
    assert len(SB)==q*q+q-1
    seen=set(); orbitsB=[]
    for D in SB:
        if D in seen:continue
        O={push_delta(D,M,q) for M in autB}
        assert O<=SB
        seen|=O; orbitsB.append(O)
    g2=gcd(2,q-1)
    assert len(orbitsB)==2*q+g2

    # Verify transformation formulas exhaustively.
    for t in range(1,q):
      M=phiB(t,q)
      for A,g in product(range(q),repeat=2):
        got=push_delta(dBI(A,g,q),M,q)
        Ap=(t*t*A+t*(t-1)*g)%q; gp=t*g%q
        assert got==dBI(Ap,gp,q)
      for l in range(q):
        assert push_delta(dBII(l,q),M,q)==dBII(l,q)
    for t in range(1,q):
      for u in range(q):
        M=phiA(t,u,q)
        for g in range(q): assert push_delta(dA(g,q),M,q)==dA((t**3*g)%q,q)

    print({'q':q,'autA':len(autA),'rawA':len(SA),'classesA':len(orbitsA),'g3':g3,
           'autB':len(autB),'rawB':len(SB),'classesB':len(orbitsB),'g2':g2,
           'total_raw':len(SA)+len(SB),'total_classes':len(orbitsA)+len(orbitsB)})
print('VERIFY_OK')
