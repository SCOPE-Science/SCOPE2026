"""Independent finite-field point-count replay for the smooth Ciani coefficient family.
No nonstandard Python libraries are needed.
"""
import itertools
from collections import Counter

# Model GF(3^n) = GF(3)[t]/(m(t)), with little-endian base-three encoding.
MODULI={1:(1,1),2:(1,0,1),3:(1,2,0,1)}

def make_field(n):
    modulus=MODULI[n]
    q=3**n
    vectors=[tuple((u//3**j)%3 for j in range(n)) for u in range(q)]
    def enc(v): return sum((int(k)%3)*3**j for j,k in enumerate(v))
    add=[[enc(tuple((vectors[a][i]+vectors[b][i])%3 for i in range(n))) for b in range(q)] for a in range(q)]
    mul=[]
    for a in range(q):
        row=[]
        for b in range(q):
            p=[0]*(2*n-1)
            for i in range(n):
                for j in range(n):p[i+j]=(p[i+j]+vectors[a][i]*vectors[b][j])%3
            for k in range(2*n-2,n-1,-1):
                top=p[k]
                for j in range(n):p[k-n+j]=(p[k-n+j]-top*modulus[j])%3
            row.append(enc(p[:n]))
        mul.append(row)
    # The point (1,u,v), (0,1,v), (0,0,1) enumerate P^2(GF(q)) exactly.
    points=[(1,u,v) for u in range(q) for v in range(q)] + [(0,1,v) for v in range(q)] + [(0,0,1)]
    sq=[mul[u][u] for u in range(q)]
    fourth=[mul[u][u] for u in sq]
    def count(coeff):
        out=0
        for x,y,z in points:
            terms=(fourth[x],fourth[y],fourth[z],mul[sq[x]][sq[y]],mul[sq[x]][sq[z]],mul[sq[y]][sq[z]])
            val=0
            for a,u in zip(coeff,terms):
                if a==1:val=add[val][u]
                elif a==2:val=add[val][add[u][u]]
            out+=val==0
        return out
    return count

def smooth_criterion(v):
    a,b,c,d,e,f=v
    if a*b*c==0: return False
    edges=((a,b,d),(a,c,e),(b,c,f))
    return sum(t!=0 for _,_,t in edges)<=1 and all(t==0 or i!=j for i,j,t in edges)

count_functions={n:make_field(n) for n in (1,2,3)}
profile_counts=Counter()
for v in itertools.product(range(3),repeat=6):
    if not smooth_criterion(v):continue
    ns=tuple(count_functions[n](v) for n in (1,2,3))
    s1=4-ns[0];s2=10-ns[1];s3=28-ns[2]
    assert (s1*s1-s2)%2==0
    assert (-s1**3+3*s1*s2-2*s3)%6==0
    a1=-s1
    a2=(s1*s1-s2)//2
    a3=(-s1**3+3*s1*s2-2*s3)//6
    p=(1,a1,a2,a3,3*a2,9*a1,27)
    profile_counts[(ns,p)]+=1
expected={
 ((4,28,28),(1,0,9,0,27,0,27)):8,
 ((2,24,38),(1,-2,9,-12,27,-18,27)):12,
 ((6,24,18),(1,2,9,12,27,18,27)):12,
}
assert profile_counts==expected,(profile_counts,expected)
print('ZETA_POINT_COUNTS_OK')
print('field_degrees=1,2,3')
for (ns,p),num in sorted(profile_counts.items()):
    print('N_1,N_2,N_3=',ns,'Weil_coefficients=',p,'coefficient_vectors=',num,'normalized=',num//2)

# The isogeny factors corresponding to the three profiles are
# (1+3T^2)^3 and (1±2T+3T^2)(1+3T^2)^2.
