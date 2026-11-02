"""Independent point-count and bitangent-contact verification of the 78-row census.

Only the table of equations and orbit sizes is read; all arithmetic invariants
are reconstructed by separately implemented polynomial-quotient arithmetic and
homogeneous symbolic line substitution over the binary field.
"""
import csv
from pathlib import Path
import sympy as sp

PATH = Path(__file__).with_name('quartic_joint_census.csv')
ROWS = [{k:int(v) for k,v in r.items()} for r in csv.DictReader(PATH.open(encoding='utf-8'))]
assert len(ROWS)==78
MON = [(a,b,4-a-b) for a in range(5) for b in range(5-a)]
MODS = {1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}
X,Y,Z,S,T=sp.symbols('X Y Z S T')

def poly_terms(mask):
    return [MON[i] for i in range(15) if (mask>>i)&1]

def gf_product(a,b,n):
    product=0
    for shift in range(n):
        if (b>>shift)&1:product ^= a<<shift
    modulus=MODS[n]
    while product.bit_length()>n:
        product ^= modulus << (product.bit_length()-n-1)
    return product

def count_projective(mask,n):
    q=1<<n
    power={a:[1]+[0]*4 for a in range(q)}
    for a in range(q):
        for e in range(1,5):power[a][e]=gf_product(power[a][e-1],a,n)
    terms=poly_terms(mask)
    # Unique projective representatives Z=1, or Z=0,Y=1, or [1:0:0].
    total=0
    for u in range(q):
        for v in range(q):
            value=0
            for a,b,c in terms:
                value ^= gf_product(power[u][a],power[v][b],n)
            if value==0:total+=1
    for u in range(q):
        value=0
        for a,b,c in terms:
            if c==0:value ^= power[u][a]
        if value==0:total+=1
    if not (mask & (1<<14)):total+=1
    return total

VECTORS=[(a,b,c) for a in range(2) for b in range(2) for c in range(2) if a or b or c]

def line_profile(mask):
    expr=sum(X**a*Y**b*Z**c for a,b,c in poly_terms(mask))
    result=[0,0,0]
    for normal in VECTORS:
        ker=[v for v in VECTORS if sum(a*b for a,b in zip(normal,v))%2==0]
        assert len(ker)==3
        u,v=ker[0],ker[1]
        restriction=sp.Poly(sp.expand(expr.subs({X:u[0]*S+v[0]*T,Y:u[1]*S+v[1]*T,Z:u[2]*S+v[2]*T},simultaneous=True)),S,T,modulus=2)
        coeff=[int(restriction.coeff_monomial(S**(4-i)*T**i))%2 for i in range(5)]
        assert any(coeff)  # Smooth quartic contains no entire projective line.
        if coeff[1] or coeff[3]:continue
        a,b,c=coeff[0],coeff[2],coeff[4]
        roots=int(a==0)+int(c==0)+int((a^b^c)==0)
        assert roots in (0,1,2)
        result[roots]+=1
    return tuple(result)

def predicted_counts(r):
    a1,a2,a3=(r['a1'],r['a2'],r['a3'])
    a=[1,a1,a2,a3,2*a2,4*a1,8]
    power_sums={}
    for n in range(1,7):
        power_sums[n]=-sum(a[j]*power_sums[n-j] for j in range(1,n)) -n*a[n]
    return [2**n+1-power_sums[n] for n in range(1,7)]

seen=set()
for row in ROWS:
    mask=row['coefficient_mask']
    assert mask not in seen
    seen.add(mask)
    assert line_profile(mask)==(row['theta_n0'],row['theta_n1'],row['theta_n2'])
    predicted=predicted_counts(row)
    for n in (1,2,3):
        assert count_projective(mask,n)==row['N'+str(n)]==predicted[n-1],(mask,n)
for m in (4249,4469,4347,4415):
    row=next(r for r in ROWS if r['coefficient_mask']==m)
    for n in (4,5,6):
        assert count_projective(m,n)==predicted_counts(row)[n-1],(m,n)
print('INDEPENDENT_OK',len(ROWS),'full_profiles',len(ROWS)*7,'extended_examples',4)
