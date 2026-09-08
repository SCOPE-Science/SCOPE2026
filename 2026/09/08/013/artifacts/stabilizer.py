"""Stabilizer order of the (17,3)-arc A in PGL(3,9): enumerate target frames."""
import itertools, json

def add(x,y): return ((x%3)+(y%3))%3 + 3*(((x//3)+(y//3))%3)
def neg(x): return ((-x)%3)+3*((-(x//3))%3)
def mul(x,y):
    u1,v1=x%3,x//3; u2,v2=y%3,y//3
    return (u1*u2-v1*v2)%3+3*((u1*v2+u2*v1)%3)
def inv(x):
    for z in range(1,9):
        if mul(x,z)==1: return z
def sub(x,y): return add(x,neg(y))
def det3(M):
    (a1,b1,c1),(a2,b2,c2),(a3,b3,c3)=M
    return add(add(mul(a1,sub(mul(b2,c3),mul(b3,c2))),mul(a2,sub(mul(b3,c1),mul(b1,c3)))),mul(a3,sub(mul(b1,c2),mul(b2,c1))))
def matvec(M,v):
    return tuple(add(add(mul(M[r][0],v[0]),mul(M[r][1],v[1])),mul(M[r][2],v[2])) for r in range(3))
def solve_frame(src,dst):
    # find M with M*src_i ~ dst_i: unknowns 9 entries, each col condition up to scale.
    # brute force: M rows r1,r2,r3; use linear algebra over F9 by elimination.
    # equations: M s_i ^ d_i = 0 (cross product zero): 2 indep eqs per i (pick 2 rows of cross matrix).
    import copy
    eqs=[]
    for s,d in zip(src,dst):
        Ms=[(s[0],s[1],s[2])]  # M s = (r1.s, r2.s, r3.s); require parallel to d
        # (r1.s)d2-(r2.s)d1=0 etc: linear in r1,r2,r3 entries
        for (A2,B2) in ( ((0,1),(0,)), ):
            pass
        # rows: cross((r.s), d)=0 -> 3 eqs, use first two nonzero-pattern-independent (all 3 fine)
        for (p,q,dp,dq) in ((0,1,0,1),(0,2,0,2)):
            pass
        # general: (r_p.s)*d_q - (r_q.s)*d_p = 0
        for p,q in ((0,1),(0,2),(1,2)):
            row=[0]*9
            for k in range(3):
                row[3*p+k]=mul(s[k],d[q])
                row[3*q+k]=mul(s[k],neg(d[p]))
            eqs.append(row)
    # nullspace of eqs (12x9)
    M=[r[:] for r in eqs]
    piv=[]; r=0
    nrows=len(M); ncols=9
    where=[-1]*ncols
    for c in range(ncols):
        pivr=None
        for i in range(r,nrows):
            if M[i][c]!=0: pivr=i; break
        if pivr is None: continue
        M[r],M[pivr]=M[pivr],M[r]
        iv=inv(M[r][c]); M[r]=[mul(v,iv) for v in M[r]]
        for i in range(nrows):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[sub(a,mul(f,b)) for a,b in zip(M[i],M[r])]
        where[c]=r; r+=1
    free=[c for c in range(ncols) if where[c]==-1]
    sols=[]
    for vals in itertools.product(range(9),repeat=len(free)):
        sol=[0]*ncols
        for c,v in zip(free,vals): sol[c]=v
        for c in range(ncols):
            if where[c]!=-1:
                s2=0
                for cc,v in zip(free,vals): s2=add(s2,mul(M[where[c]][cc],v))
                sol[c]=neg(s2)
        if any(sol):
            Mm=[sol[0:3],sol[3:6],sol[6:9]]
            if det3(Mm)!=0: sols.append(Mm)
    return sols

pts=[]; seen=set()
for x in range(9):
    for y in range(9):
        for z in range(9):
            if x==y==z==0: continue
            v=(x,y,z)
            for c in v:
                if c: s=inv(c); break
            key=(mul(x,s),mul(y,s),mul(z,s))
            if key not in seen: seen.add(key); pts.append(key)
R=json.load(open("output/artifacts/maxcap_result.json"))
Wf=json.load(open("output/artifacts/witness_analysis.json"))
A=Wf["A"]; Aset=set(A)
Avec=[pts[i] for i in A]
# source frame: first 4 pts of A with no 3 collinear
src=None
for q in itertools.combinations(range(len(Avec)),4):
    P=[Avec[i] for i in q]
    if all(det3([P[a],P[b],P[c]])!=0 for a,b,c in itertools.combinations(range(4),3)):
        src=(q,P); break
print("source frame idx:",src[0])
gl_count=0; proj=set(); examples=[]
for q in itertools.combinations(range(len(Avec)),4):
    P=[Avec[i] for i in q]
    if not all(det3([P[a],P[b],P[c]])!=0 for a,b,c in itertools.combinations(range(4),3)): continue
    for sols in [solve_frame(src[1],P)]:
        for Mm in sols:
            img=set()
            for v in Avec:
                w=matvec(Mm,v)
                for c in w:
                    if c: s=inv(c); break
                key=(mul(w[0],s),mul(w[1],s),mul(w[2],s))
                img.add(key)
            if img==set(Avec):
                gl_count+=1
                # canonicalize up to F9* scalars: normalize first nonzero entry to 1
                flat=[e for row in Mm for e in row]
                for e in flat:
                    if e: s=inv(e); break
                proj.add(tuple(mul(e,s) for e in flat))
                if len(examples)<2: examples.append(Mm)
print("GL stabilizer matrix count:",gl_count)
print("PGL(3,9) stabilizer order:",len(proj))
json.dump({"stabilizer_order":len(proj),"gl_matrix_count":gl_count,
 "note":"projective PGL(3,9) order; each projective class has 8 F9* scalar multiples, hence gl_matrix_count == 8*stabilizer_order"},
 open("output/artifacts/stabilizer.json","w"))
