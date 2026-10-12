import sympy as sp

l=sp.symbols("lambda")
B=sp.Matrix([[1,l],[0,1]])
S=sp.simplify(B.inv()*B.T)
assert S==sp.Matrix([[1-l**2,-l],[l,1]])
assert sp.simplify(sp.trace(S)-(2-l**2))==0
assert sp.simplify(S.det()-1)==0

D=sp.diag(1,-1)
Bm=sp.Matrix([[1,-l],[0,1]])
assert sp.simplify(D.T*Bm*D-B)==sp.zeros(2)

# Other Theorem 4.1 forms: AD5 and AD6 have rank one.
B5=sp.Matrix([[1,0],[0,0]])
B6=sp.Matrix([[0,1],[0,0]])
assert B.rank()==2 and B5.rank()==1 and B6.rank()==1

# AD4 is alternating, with scalar asymmetry -I.
J=sp.Matrix([[0,1],[-1,0]])
SJ=J.inv()*J.T
assert SJ==-sp.eye(2)
for val in (2,-2):
    Sv=S.subs(l,val)
    assert sp.trace(Sv)==-2
    assert Sv!=-sp.eye(2)
    assert (Sv+sp.eye(2)).rank()==1

print("VERIFY_OK")
