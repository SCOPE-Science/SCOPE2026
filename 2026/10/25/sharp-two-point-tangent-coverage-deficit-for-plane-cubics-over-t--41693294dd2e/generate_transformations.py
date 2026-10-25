"""Generate the five matrices acting on ternary cubics by coordinate changes.

All polynomial arithmetic is exact in the prime field with five elements.
The coefficient order agrees with the other verification programs.
"""
E = ((3,0,0),(0,3,0),(0,0,3),(2,1,0),(2,0,1),
     (1,2,0),(0,2,1),(1,0,2),(0,1,2),(1,1,1))
# Each coordinate is specified by the coefficients of (X,Y,Z).
GENERATORS = (
    ((1,1,0),(0,1,0),(0,0,1)),
    ((1,0,0),(0,1,1),(0,0,1)),
    ((1,0,0),(0,1,0),(1,0,1)),
    ((2,0,0),(0,1,0),(0,0,1)),
    ((0,1,0),(1,0,0),(0,0,1)),
)

def mul(a,b):
    out = {}
    for ex,va in a.items():
        for ey,vb in b.items():
            ez = tuple(ex[i]+ey[i] for i in range(3))
            out[ez] = (out.get(ez,0)+va*vb)%5
    return {e:v for e,v in out.items() if v}

def action_columns(substitution):
    lin = []
    for row in substitution:
        lin.append({tuple(int(i==j) for i in range(3)):c for j,c in enumerate(row) if c%5})
    out = []
    for e in E:
        polynomial = {(0,0,0):1}
        for var in range(3):
            for _ in range(e[var]):
                polynomial=mul(polynomial,lin[var])
        out.append([polynomial.get(ee,0) for ee in E])
    return out

with open('generators.txt','w',encoding='ascii') as output:
    for substitution in GENERATORS:
        columns=action_columns(substitution)
        print(' '.join(str(columns[j][i]) for i in range(10) for j in range(10)),file=output)
print('five invertible cubic-substitution matrices written')
