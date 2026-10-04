from fractions import Fraction as F

def slope(a,b,c,d):
    w=abs(d-c)
    v=abs(b-a)
    if w+v==0:
        return (b+c)/2
    return (w*b+v*c)/(w+v)

# Corroborate the universal derivative lemma on a finite exact box.
for a in range(9):
  for b in range(9):
    for c in range(9):
      for d in range(9):
        m=slope(F(a),F(b),F(c),F(d))
        assert m>=0
        assert 2*m <= a+b+c+d

# Hermite basis and extrema.
def basis(t):
    h00=2*t**3-3*t**2+1
    h10=t**3-2*t**2+t
    h01=-2*t**3+3*t**2
    h11=t**3-t**2
    return h00,h10,h01,h11

for k in range(101):
    t=F(k,100)
    h00,h10,h01,h11=basis(t)
    assert h00>=0 and h01>=0 and h00+h01==1
    assert h10>=0 and h11<=0
assert F(2,3)**2*(1-F(2,3))==F(4,27)
assert F(1,3)*(1-F(1,3))**2==F(4,27)

def eval_segment(y0,y1,m0,m1,t):
    h00,h10,h01,h11=basis(t)
    return h00*y0+h10*m0+h01*y1+h11*m1

# Sharpness family.
for eps in [F(1,1000),F(1,500),F(1,104),F(1,80)]:
    assert F(0)<eps<F(1,8)
    a=F(1,2)-2*eps
    ds=[eps,eps,2*eps,a,a]
    m2=slope(ds[0],ds[1],ds[2],ds[3])
    m3=slope(ds[1],ds[2],ds[3],ds[4])
    assert m2==eps
    assert m3==a
    y2=2*eps
    y3=4*eps
    p=eval_segment(y2,y3,m2,m3,F(2,3))
    assert p==(104*eps-2)/27

# Strictly positive witness after affine vertical transformation.
eps=F(1,104)
a=F(1,2)-2*eps
y=[F(0),eps,2*eps,4*eps,F(1,2)+2*eps,F(1)]
z=[F(1,100)+F(99,100)*u for u in y]
assert z==[F(1,100),F(203,10400),F(151,5200),F(5,104),F(109,208),F(1)]
assert all(z[i]<z[i+1] for i in range(5))
# Slopes scale by 99/100 and constants shift the cubic.
ds=[y[i+1]-y[i] for i in range(5)]
m2=slope(ds[0],ds[1],ds[2],ds[3])
m3=slope(ds[1],ds[2],ds[3],ds[4])
p=eval_segment(y[2],y[3],m2,m3,F(2,3))
zp=F(1,100)+F(99,100)*p
assert p==F(-1,27)
assert zp==F(-2,75)
print('VERIFY_OK')
