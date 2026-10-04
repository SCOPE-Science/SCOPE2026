from fractions import Fraction as F

V=[(F(0),F(1)),(F(2,3),F(2,3)),(F(1),F(1,7)),(F(1),F(-1)),(F(0),F(-1)),(F(-2,3),F(-2,3)),(F(-1),F(-1,7)),(F(-1),F(1))]
b=F(5,13)
def q(p):
    x,y=p
    return x*x+2*b*x*y+y*y

def mat(v):
    x,y=v
    return ((x*x,x*y),(x*y,y*y))
def madd(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))
def smul(c,A):
    return tuple(tuple(c*A[i][j] for j in range(2)) for i in range(2))

v1=(F(2,3),F(2,3)); v2=(F(1),F(-1))
z1=(F(1),F(-5,13)); z2=(F(5,13),F(-1))
L=madd(smul(F(4,13),mat(v1)),smul(F(9,13),mat(v2)))
R=smul(F(13,18),madd(mat(z1),mat(z2)))
assert L==R

vals=[q(v) for v in V]
M=max(vals)
assert M==F(16,13)

def edge_min(v,w):
    x0,y0=v; x1,y1=w
    dx=x1-x0; dy=y1-y0
    A=dx*dx+2*b*dx*dy+dy*dy
    B=2*(x0*dx+b*(x0*dy+y0*dx)+y0*dy)
    cand=[F(0),F(1)]
    t=-B/(2*A)
    if F(0)<=t<=F(1): cand.append(t)
    def qt(t): return q((x0+t*dx,y0+t*dy))
    return min(qt(t) for t in cand)
mins=[edge_min(V[i],V[(i+1)%len(V)]) for i in range(len(V))]
expected=[F(64,65),F(72,65),F(144,169),F(144,169)]*2
assert mins==expected, (mins,expected)
m=min(mins)
assert m==F(144,169)
D=M/m
assert D==F(13,9)
print('VERIFY_OK d2=13/9')
