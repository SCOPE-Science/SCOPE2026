"""Find all patterns attaining 5088,4608,4464 to describe tie structure beyond q7."""
from fractions import Fraction
p0f=[Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1,1)]
interior=[(Fraction(1,4),Fraction(1,4),Fraction(1,2)),(Fraction(1,4),Fraction(1,2),Fraction(1,4)),(Fraction(1,4),Fraction(3,4),Fraction(0,1)),(Fraction(1,2),Fraction(1,4),Fraction(1,4)),(Fraction(1,2),Fraction(1,2),Fraction(0,1)),(Fraction(3,4),Fraction(1,4),Fraction(0,1))]
def H_recur(i0,js):
    p_list=[p0f[i0]]+[interior[j][0] for j in js]
    q_list=[Fraction(0,1)]+[interior[j][1] for j in js]
    d=Fraction(1,1)/p_list[0]; tot=d
    for i in range(1,7):
        d=(Fraction(1,1)+q_list[i]*d)/p_list[i]
        tot+=d
    return tot
for target in [Fraction(5088,1),Fraction(4608,1),Fraction(4464,1),Fraction(4358,1),Fraction(6544,1)]:
    hits=[]
    for i0 in range(4):
        for i1 in range(6):
            for i2 in range(6):
                for i3 in range(6):
                    for i4 in range(6):
                        for i5 in range(6):
                            for i6 in range(6):
                                js=(i1,i2,i3,i4,i5,i6)
                                if H_recur(i0,js)==target:
                                    hits.append((i0,js))
    print(f"H={target}: {len(hits)} patterns: {hits}")
