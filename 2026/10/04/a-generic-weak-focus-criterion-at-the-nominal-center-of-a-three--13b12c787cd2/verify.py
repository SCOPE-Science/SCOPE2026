import sympy as s
I=s.I
a=s.Integer(5); b=s.Integer(50); c=s.Integer(-6); d=s.Integer(13)
z0=s.cancel(b*c/d)
w=s.sqrt(s.cancel(b*c*(b*c-a*d)/d**2))
A=s.Matrix([[0,a-z0,0],[z0,0,0],[c,b,-d]])
# exact linear spectrum check
lam=s.symbols('lam')
assert s.simplify(A.charpoly(lam).as_expr()-(lam+d)*(lam**2+w**2))==0
q=(A-I*w*s.eye(3)).nullspace()[0]
p=(A.T+I*w*s.eye(3)).nullspace()[0]
inn=(s.conjugate(p).T*q)[0]
p=p/s.conjugate(inn)
assert s.simplify((s.conjugate(p).T*q)[0]-1)==0

def B(u,v):
    return s.Matrix([-(u[1]*v[2]+u[2]*v[1]), u[0]*v[2]+u[2]*v[0], u[0]*v[1]+u[1]*v[0]])
term=-2*B(q,A.inv()*B(q,s.conjugate(q)))+B(s.conjugate(q),(2*I*w*s.eye(3)-A).inv()*B(q,q))
G=(s.conjugate(p).T*term)[0]
ell=s.simplify(s.re(s.together(G))/(2*w))
assert ell>0
# independent sign factor from general factorization
assert -a*b*c*(b*b-d*d)>0
print('VERIFY_OK')
print('omega =', w)
print('ell =', ell)
print('ell_float =', s.N(ell,16))
