"""Finite-field direct substitution census for two-variable truncated local algebras."""
from itertools import product
from math import prod

def monoms(N):
    return [(a,s-a) for s in range(1,N) for a in range(s,-1,-1)]

def compose(f,g,N,p,mons):
    # evaluate f(g_x,g_y) mod (x,y)^N, monomial dicts including zero
    def mul(x,y):
        z={}
        for (a,b),u in x.items():
            for (c,d),v in y.items():
                if a+b+c+d<N:
                    k=(a+c,b+d);z[k]=(z.get(k,0)+u*v)%p
        return {k:v for k,v in z.items() if v}
    out=[]
    for fc in f:
        acc={}; powerx={(0,0):1}
        for a in range(N):
            powery={(0,0):1}
            for b in range(N-a):
                c=fc.get((a,b),0)
                if c:
                    for k,v in mul(powerx,powery).items():acc[k]=(acc.get(k,0)+c*v)%p
                powery=mul(powery,g[1])
            powerx=mul(powerx,g[0])
        out.append({k:v for k,v in acc.items() if v%p})
    return tuple(out)

def matmul(a,b,p):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))%p for j in range(2)) for i in range(2))

def check_small(q,N):
    assert N==3
    I=((1,0),(0,1));ms=monoms(N)
    quadr=[m for m in ms if sum(m)==2]
    cnt={"scalar_plus":0,"scalar_minus":0,"mixed":0}
    classcounts={}
    tested=0
    for vals in product(range(q),repeat=4):
        a=(vals[:2],vals[2:]);assert len(a)==2
        if matmul(a,a,q)!=I:continue
        kind="scalar_plus" if a==I else "scalar_minus" if a==((q-1,0),(0,q-1)) else "mixed"
        n=0
        for cof in product(range(q),repeat=6):
            f=({(1,0):a[0][0],(0,1):a[0][1]}, {(1,0):a[1][0],(0,1):a[1][1]})
            f=list(f)
            for j in range(2):
                for k,m in enumerate(quadr):
                    if cof[3*j+k]:f[j][m]=cof[3*j+k]
            f=tuple(f)
            tested+=1
            if compose(f,f,N,q,ms)==({(1,0):1},{(0,1):1}):n+=1
        exp=1 if kind=="scalar_plus" else q**6 if kind=="scalar_minus" else q**3
        assert n==exp,(q,N,a,n,exp)
        classcounts[str(a)]=n
        cnt[kind]+=n
    total=1+q**6+q*(q+1)*q**3
    assert sum(cnt.values())==total,(q,cnt,total)
    return tested,cnt

def count_linear_extensions_odd3_N4(L):
    """Independent triangular polynomial-equation solver for all cubic coefficients."""
    p=3;N=4
    quad=[(2,0),(1,1),(0,2)]
    cubic=[(3,0),(2,1),(1,2),(0,3)]
    points=[(j,mon) for j in range(2) for mon in cubic]
    dest=[(j,mon) for j in range(2) for mon in quad]
    def ident():return ({(1,0):1}, {(0,1):1})
    def make(cof, cube=None):
        out=[{(1,0):L[j][0],(0,1):L[j][1]} for j in range(2)]
        for j in range(2):
            for k,m in enumerate(quad):
                if cof[3*j+k]:out[j][m]=cof[3*j+k]
        if cube:
            for v,(j,m) in zip(cube,points):
                if v:out[j][m]=v
        return tuple(out)
    def system_count(A,b):
        # rows equation 8, vars 8, count all solutions modulo p
        nvars=len(A[0]);rows=[list(row)+[rhs%p] for row,rhs in zip(A,b)]
        piv=0
        for col in range(nvars):
            i=next((j for j in range(piv,len(rows)) if rows[j][col]%p),None)
            if i is None:continue
            rows[piv],rows[i]=rows[i],rows[piv]
            inv=pow(rows[piv][col],-1,p)
            rows[piv]=[(v*inv)%p for v in rows[piv]]
            for j in range(len(rows)):
                if j!=piv and rows[j][col]:
                    v=rows[j][col]
                    rows[j]=[(x-v*y)%p for x,y in zip(rows[j],rows[piv])]
            piv+=1
        if any(all(not c for c in row[:nvars]) and row[-1] for row in rows):return 0
        return p**(nvars-piv)
    I=ident(); count=0; viable=0
    for cof in product(range(p),repeat=6):
        f0=make(cof)
        base=compose(f0,f0,N,p,[])
        if any(base[j].get(m,0)!=0 for j,m in dest):continue
        viable+=1
        cvals=[base[j].get(m,0) for j,m in points]
        cols=[]
        for k in range(len(points)):
            e=[0]*len(points);e[k]=1
            ef=make(cof,e)
            comp=compose(ef,ef,N,p,[])
            cols.append([(comp[j].get(m,0)-base[j].get(m,0))%p for j,m in points])
        A=[[cols[col][row] for col in range(len(points))] for row in range(len(points))]
        count+=system_count(A,[(-v)%p for v in cvals])
    return count,viable

def verify_formula():
    for N in range(3,12):
        D=N*(N+1)-6
        E=2*sum(s+1 for s in range(2,N,2))
        assert D%2==0
        # check rank centralizer dimensions by direct parity count
        cm=0;ci=0
        for s in range(2,N):
            for a in range(s+1):
                b=s-a
                for target in (0,1):
                    cm+= ((-1)**s== -1)
                    ci+= ((-1)**b==((-1)**target))
        assert D-cm==E and ci==D//2,(N,D,E,cm,ci)
        if N%2:
            r=(N-1)//2;assert E-D//2==r*(0)+r+2,(N,E,D)
        else:
            r=N//2;assert E-D//2==1-r
    checked3, data3=check_small(3,3)
    checked5, data5=check_small(5,3)
    n4=[]
    for L,expected in [(((1,0),(0,1)),1),(((2,0),(0,2)),3**6),(((1,0),(0,2)),3**7)]:
        got,partial=count_linear_extensions_odd3_N4(L)
        assert got==expected,(L,got,expected)
        n4.append((L,got,partial))
    print('VERIFY_OK exhaustive polynomial-composition censuses q=3,5 at N=3: ',checked3+checked5,'maps;',data3,data5,'; independent N=4 cubic-extension solver: ',n4,'; 9 degree-parity checks')

if __name__=='__main__':verify_formula()
