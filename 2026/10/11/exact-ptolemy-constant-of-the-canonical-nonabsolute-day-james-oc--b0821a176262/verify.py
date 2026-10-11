from fractions import Fraction as F
V=[(F(0),F(-1)),(F(1),F(-1)),(F(1),F(1,7)),(F(2,3),F(2,3)),(F(0),F(1))]
def q(p):
    x,y=p
    return x*x+F(10,13)*x*y+y*y
def edge_min(a,b):
    x0,y0=a; x1,y1=b
    dx=x1-x0; dy=y1-y0
    A=q((dx,dy))
    B=2*x0*dx+F(10,13)*(x0*dy+y0*dx)+2*y0*dy
    t=-B/(2*A)
    cand=[F(0),F(1)]
    if F(0)<=t<=F(1): cand.append(t)
    vals=[]
    for s in cand:
        p=(x0+s*dx,y0+s*dy)
        vals.append((q(p),s))
    return min(vals)
mins=[edge_min(V[i],V[i+1]) for i in range(4)]
assert mins==[(F(144,169),F(5,13)),(F(144,169),F(7,13)),(F(72,65),F(3,10)),(F(64,65),F(4,5))]
vals=[q(p) for p in V]
assert vals==[F(1),F(16,13),F(720,637),F(16,13),F(1)]
m=min(v for v,t in mins); M=max(vals)
assert m==F(144,169) and M==F(16,13) and M/m==F(13,9)

def same(a,b):
    a=abs(a); b=abs(b)
    if a==0 and b==0: return F(0)
    t=b/(a+b)
    if t<=F(1,8): psi=1-t
    elif t<=F(1,2): psi=(11-4*t)/12
    else: psi=(1+t)/2
    return (a+b)*psi
def N(p):
    a,b=p
    return same(a,b) if a*b>=0 else max(abs(a),abs(b))
sub=lambda a,b:(a[0]-b[0],a[1]-b[1])
x=(F(-2,3),F(-2,3)); y=(F(3,2),F(-3,2)); z=(F(5,6),F(-13,6))
six=[N(x),N(y),N(z),N(sub(x,y)),N(sub(x,z)),N(sub(z,y))]
assert six==[F(1),F(3,2),F(13,6),F(13,6),F(3,2),F(1)]
ratio=N(sub(x,y))*N(z)/(N(sub(x,z))*N(y)+N(sub(z,y))*N(x))
assert ratio==F(13,9)
print("VERIFY_OK Cpt=13/9")
