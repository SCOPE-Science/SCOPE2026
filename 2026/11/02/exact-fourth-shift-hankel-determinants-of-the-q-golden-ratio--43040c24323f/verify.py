from sympy import symbols, factor, together, cancel, Poly, Matrix, Integer
q,t=symbols('q t')

def step(A,B,C,k,a,D):
    assert cancel(Poly(A,q).nth(k)-a)==0
    assert all(cancel(Poly(A,q).nth(i))==0 for i in range(k))
    assert cancel(D.subs(q,0)-1)==0
    assert Poly(D,q).degree()<=k+1
    assert cancel(B.subs(q,0)-1)==0 and cancel(C.subs(q,0))==0
    residual=a*q**k*B/A-a*q**k*C/B-D
    assert cancel(residual.series(q,0,k+2).removeO())==0
    aa=cancel((-D**2*A/a+B*D*q**k-C*a*q**(2*k))/q**(2*k+2))
    bb=cancel(2*A*D/(a*q**k)-B)
    cc=cancel(-A*q**2/a)
    assert cancel(bb.subs(q,0)-1)==0 and cancel(cc.subs(q,0))==0
    assert all(Poly(cancel(v),q).is_univariate for v in (aa,bb,cc))
    return aa,bb,cc

def eq(x,y):return all(cancel(u-v)==0 for u,v in zip(x,y))

def X1(t):
    return ((t-1)*q/t, 1+q-q*q+2*q**3/t, q**2*(q**3-t*q**2+t*q-t*(t-1))/(t*(t-1)))

def X2(t):
    return (-(q**3+t*q*q-t*q-t*(t+1))/t**2, 1+q-q*q-2*q**3/t,-q**3)

def X3(t):
    return (t*(q**3-(t+2)*q**2+(t+2)*q-(t+2)*(t+1))/(t+1)**3, -(2*q**4-2*q**3-((t+1)**2-2)*q**2-(t+1)**2*q-(t+1)**2)/(t+1)**2, q**2*(q**3+t*q**2-t*q-t*(t+1))/(t*(t+1)))

base=(-2+2*q-2*q**2+q**3,1+q-q**2+2*q**3-2*q**4,q**5)
assert eq(step(*base,0,-2,1+2*q),X1(Integer(2)))
assert eq(step(*X1(t),1,(t-1)/t,1+q-q**2),X2(t))
assert eq(step(*X2(t),0,(t+1)/t,1+t*q/(t+1)),X3(t))
assert eq(step(*X3(t),0,-t*(t+2)/(t+1)**2,1+(t+2)*q/(t+1)),X1(t+2))
print('SYMBOLIC_NEXTABC_OK initial_and_three_generic_transitions')

N=50
A={0:-2,1:2,2:-2,3:1}; B={0:1,1:1,2:-1,3:2,4:-2}
f=[]
for n in range(N):
    z= -A.get(n,0) - sum(B[i]*f[n-i] for i in range(1,5) if n>=i)
    if n>=5: z-=sum(f[i]*f[n-5-i] for i in range(n-4))
    f.append(z)
assert f[:8]==[2,-4,8,-17,37,-82,185,-423]
for j in range(0,23):
    v=Matrix(j,j,lambda a,b:f[a+b]).det(method='bareiss') if j else 1
    m,r=divmod(j,4)
    expected=((-1)**m*(2*m+1) if r==0 else (-1)**m*(2*m+2) if r==1 else 0 if r==2 else (-1)**(m+1)*(2*m+2))
    assert v==expected,(j,v,expected)
print('INDEPENDENT_HANKEL_OK sizes=0..22 coefficients='+str(N))
