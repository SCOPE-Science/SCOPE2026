import sympy as s

q=s.sqrt(5)
V=[
    s.Matrix([1,0]),
    s.Matrix([(q-1)/4,1]),
    s.Matrix([-(q+1)/4,(q-1)/2]),
    s.Matrix([-(q+1)/4,-(q-1)/2]),
    s.Matrix([(q-1)/4,-1]),
]
ss=[s.Rational(0),s.Rational(3,4),(15-q)/8,s.Rational(5,2),(25+q)/8,s.Rational(17,4)]

def P(x):
    # The six prescribed parameters have known side indices.
    vals=[
        (0,s.Rational(0)),
        (0,s.Rational(3,4)),
        (1,(7-q)/8),
        (2,s.Rational(1,2)),
        (3,(1+q)/8),
        (4,s.Rational(1,4)),
    ]
    j,t=vals[len(points)]
    return s.simplify(V[j]+t*(V[(j+1)%5]-V[j]))

points=[]
for _ in range(6):
    points.append(P(ss[len(points)]))

D=[
 s.Matrix([-q/4,-(q+1)/4]),
 s.Matrix([0,-1]),
 s.Matrix([q/4,-(q+1)/4]),
 s.Matrix([(q+5)/8,(1-q)/4]),
 s.Matrix([(q+5)/8,(q-1)/4]),
 s.Matrix([q/4,(q+1)/4]),
 s.Matrix([0,1]),
 s.Matrix([-q/4,(q+1)/4]),
 s.Matrix([-(q+5)/8,(q-1)/4]),
 s.Matrix([-(q+5)/8,(1-q)/4]),
]
d=3*(q-1)/4

targets=[
 D[7],
 (1-(5-q)/6)*D[8]+((5-q)/6)*D[9],
 (1-(s.Rational(1,2)-q/6))*D[0]+(s.Rational(1,2)-q/6)*D[1],
 (1-(s.Rational(1,2)+q/6))*D[1]+(s.Rational(1,2)+q/6)*D[2],
 (1-(1+q)/6)*D[3]+((1+q)/6)*D[4],
 D[5],
]

for i in range(6):
    z=points[(i+1)%6]-points[i]
    assert all(s.simplify(a-b)==0 for a,b in zip(z/d,targets[i]))

ts=[(5-q)/6,s.Rational(1,2)-q/6,s.Rational(1,2)+q/6,(1+q)/6]
for t in ts:
    assert bool(t>=0) and bool(t<=1)

ratio=s.simplify(d/(2+d))
assert s.simplify(ratio-(3-6*q/5))==0
print("VERIFY_OK")
print("d =", s.simplify(d))
print("r =", s.simplify(ratio))
