"""Independent binomial-coefficient/Hasse-Witt calculation of the Cartier rank.
Uses coefficient sums instead of polynomial expansion and makes no basis divisions.
"""
from math import comb
from collections import Counter
from pathlib import Path
import csv
p=3;m=82;r=13; b=6
def gaussian_rank(rows):
    piv={}
    for vec in rows:
        v=dict((i,int(x)%p) for i,x in vec.items() if x%p)
        while v:
            i=min(v)
            if i not in piv:
                z=pow(v[i],-1,p)
                piv[i]={j:(x*z)%p for j,x in v.items() if x%p}
                break
            f=v[i]
            for j,x in piv[i].items():
                a=(v.get(j,0)-f*x)%p
                if a: v[j]=a
                elif j in v: del v[j]
    return len(piv)
rank_sum=0
rows_for_certificate=[]
for j in range(1,m):
    d=max(0,j-1-b*(j*r//m))
    if not d:
        rows_for_certificate.append((j,(55*j)%82,d,max(0,(55*j)%82-1-6*(13*((55*j)%82)//82)),(3*((55*j)%82)-j)//82,0))
        continue
    jj=(55*j)%82
    t=(3*jj-j)//82
    h=j*r//82+13*t
    columns=[]
    for k in range(d):
        Q={}
        for v in range(h+1):
            ch=comb(h,v)
            for i in range(2*v+t+1):
                exponent=k+(2*v+t)+2*i
                if exponent%3 !=2:continue
                coeff=(ch*comb(2*v+t,i)*(-1)**(2*v+t-i))%3
                if coeff:
                    idx=(exponent-2)//3
                    Q[idx]=(Q.get(idx,0)+coeff)%3
        columns.append(Q)
    rank_here=gaussian_rank(columns)
    rank_sum+=rank_here
    rows_for_certificate.append((j,jj,d,max(0,jj-1-6*(13*jj//82)),t,rank_here))
print({'Cartier_rank':rank_sum, 'genus':324,'a_number':324-rank_sum})
assert rank_sum==222

cert_path=Path(__file__).with_name("cartier_blocks.csv")
if cert_path.exists():
    with cert_path.open(newline="", encoding="utf-8") as fh:
        actual=[tuple(int(x) for x in row.values()) for row in csv.DictReader(fh)]
    assert actual==rows_for_certificate, "CSV block rank certificate mismatch"
    print("All 81 Cartier block ranks agree with cartier_blocks.csv")
