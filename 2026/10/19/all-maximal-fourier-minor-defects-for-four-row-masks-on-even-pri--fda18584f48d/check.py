"""Exact cyclotomic maximal-minor checker for selected even semiprime Fourier frames.
Only integer arithmetic is used: a polynomial of degree less than p vanishes at
primitive p-th roots exactly when all of its p coefficients are equal.
"""
import itertools, math

PERMS=[]
for perm in itertools.permutations(range(4)):
    inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    PERMS.append((perm,-1 if inv%2 else 1))

def exact_zero(p, d, columns):
    rows=(0,1,2,d)
    multiplier=(p+1)//2
    coefficients=[0]*p
    for perm,sgn in PERMS:
        weighted=sum(rows[i]*columns[perm[i]] for i in range(4))
        coefficients[(weighted*multiplier)%p]+=sgn*(-1 if weighted%2 else 1)
    return all(coef==coefficients[0] for coef in coefficients)

def predicted(p,d,columns):
    parity={c%2 for c in columns}
    if d%2:
        return d in (p,p+2) and len(parity)==1
    if d==p+1:
        if len(parity)==1:
            return True
        plus=[c for c in columns if c%2==0]
        minus=[c for c in columns if c%2==1]
        if len(plus)!=2:
            return False
        # (w**c1)*(w**c2) = (w**c3)*(w**c4) iff their sums match modulo 2p.
        return (sum(plus)-sum(minus))%(2*p)==0
    residues=[c%p for c in columns]
    return len(set(residues))==2 and all(residues.count(x)==2 for x in set(residues))

def check(p,ds):
    N=2*p
    allcols=list(itertools.combinations(range(N),4))
    output=[]
    for d in ds:
        count=0; predicted_count=0
        for columns in allcols:
            actual=exact_zero(p,d,columns)
            count+=actual
            expected=predicted(p,d,columns)
            assert actual==expected,(p,d,columns,actual,expected)
            predicted_count+=expected
        if d%2:
            expect=2*math.comb(p,4) if d in (p,p+2) else 0
            assert count==expect,(p,d,count,expect)
        elif d==p+1:
            expect=2*math.comb(p,4)+(p-1)//2*math.comb(p,2)
            assert count==expect,(p,d,count,expect)
        elif d%2==0:
            assert count==math.comb(p,2),(p,d,count)
        output.append((d,count))
    return output

def main():
    for p in (5,7,11):
        info=check(p,range(3,2*p))
        print('p=',p,'all d=3,...,',2*p-1,'exact singular minor counts:',info)
    for p in (13,):
        ds=list(range(3,2*p,2))+[p+1]
        print('p=',p,'selected d:',check(p,ds))
    print('PASS: all checked minors match the theorem; the infinite statement is proved analytically.')

if __name__=='__main__':main()
