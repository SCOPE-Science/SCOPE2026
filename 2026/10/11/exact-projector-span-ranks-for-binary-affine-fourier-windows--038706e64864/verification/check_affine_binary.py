"""Exact modular rank calculations for binary finite-field affine projectors.
All calculations are finite consistency checks, not proofs of general rank formulas.
"""

P=1009
I=next(v for v in range(1,P) if (v*v+1)%P==0)
MODS={2:0b111,3:0b1011,4:0b10011}

def ff_mul(a,b,n):
    poly=MODS[n];out=0
    for _ in range(n):
        if b&1:out^=a
        b>>=1;a<<=1
        if a&(1<<n):a^=poly
    assert b==0
    return out

def ff_trace(a,n):
    x=a;z=0
    for _ in range(n):
        z^=x;x=ff_mul(x,x,n)
    assert z in (0,1)
    return z

def rankmod(A, prime=P):
    A=[[int(v)%prime for v in row] for row in A]
    m=len(A); n=len(A[0]) if A else 0
    r=0
    for col in range(n):
        pivot=next((j for j in range(r,m) if A[j][col]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][col],-1,prime)
        A[r][col:]=[(v*inv)%prime for v in A[r][col:]]
        pivrow=A[r]
        for j in range(r+1,m):
            coeff=A[j][col]
            if coeff:
                row=A[j]
                for k in range(col,n):
                    row[k]=(row[k]-coeff*pivrow[k])%prime
        r+=1
        if r==m:break
    return r

def calc(n,re,im,verbose=True):
    q=2**n; elems=list(range(1,q)); z=(re+im*I)%P; zb=(re-im*I)%P
    def h(a):return z if a==1 else 1
    def hb(a):return zb if a==1 else 1
    # Nonzero-difference block, d=1: a and a+1 both nonzero.
    cols=[a for a in elems if a!=1]
    B=[[h(ff_mul(a,l,n))*hb(ff_mul(a^1,l,n))%P for a in cols] for l in elems]
    rb=rankmod(B)
    D=[[h(ff_mul(a,l,n))*hb(ff_mul(a,l,n))%P for a in elems] for l in elems]
    rd=rankmod(D)
    # Direct projector measurement matrix, not via block formula.
    signs=[[(-1)**ff_trace(ff_mul(a,k,n),n) for a in elems] for k in range(q)]
    rows=[]
    for l in elems:
      hl=[h(ff_mul(a,l,n)) for a in elems]
      hbl=[hb(ff_mul(a,l,n)) for a in elems]
      for k in range(q):
        sg=signs[k]
        rows.append([(hl[i]*hbl[j]*sg[i]*sg[j])%P for i in range(q-1) for j in range(q-1)])
    full=rankmod(rows)
    expected=rd+(q-1)*rb
    assert full==expected,(q,z,full,expected,rd,rb)
    if verbose:print(f'q={q:2d} z={re}{im:+}i block_diag={rd} block_diff={rb} full_span={full} / {(q-1)**2}')
    return rd,rb,full

if __name__=='__main__':
    print('GF residue',P,'i ->',I)
    for n in (2,3,4):
      for re,im in ((2,1),(2,0),(1,1),(0,1),(1,0)):
        calc(n,re,im)
    print('ALL EXACT MODULAR RANK CHECKS PASSED')
