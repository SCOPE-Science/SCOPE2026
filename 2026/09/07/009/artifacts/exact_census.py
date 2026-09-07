"""Exact rational census for S_{8,4} via birth-death recursion with Fractions.
H depends only on rows 0..6. Enumerates 4*6^6=186624 patterns.
Also tracks aperiodicity (some r>0 among rows 0..7) and q7 multiplicity.
"""
from fractions import Fraction
import time

p0_opts = [(Fraction(1,4),Fraction(3,4)),(Fraction(1,2),Fraction(1,2)),(Fraction(3,4),Fraction(1,4)),(Fraction(1,1),Fraction(0,1))]
# (p,q,r) interior, p,q>0 multiples of 1/4
interior = [
 (Fraction(1,4),Fraction(1,4),Fraction(1,2)),
 (Fraction(1,4),Fraction(1,2),Fraction(1,4)),
 (Fraction(1,4),Fraction(3,4),Fraction(0,1)),
 (Fraction(1,2),Fraction(1,4),Fraction(1,4)),
 (Fraction(1,2),Fraction(1,2),Fraction(0,1)),
 (Fraction(3,4),Fraction(1,4),Fraction(0,1)),
]

def H_of(p_list, q_list):
    # p_list length 7 (p0..p6), q_list length 7 (q0=0..q6)
    d_prev = Fraction(1,1)/p_list[0]  # d0
    total = d_prev
    for i in range(1,7):
        d = (Fraction(1,1) + q_list[i]*d_prev)/p_list[i]
        total += d
        d_prev = d
    return total

t0=time.time()
maxH = Fraction(-1,1)
max_args = []
# distinct value -> example arg
from collections import defaultdict
val_to_ex = {}
count=0
count_aperiodic_patterns=0  # patterns on rows0..6 with some r>0 in rows0..6
for i0 in range(4):
    p0,r0 = p0_opts[i0]
    for i1 in range(6):
        for i2 in range(6):
            for i3 in range(6):
                for i4 in range(6):
                    for i5 in range(6):
                        for i6 in range(6):
                            js=(i1,i2,i3,i4,i5,i6)
                            ps=[p0]+[interior[j][0] for j in js]
                            qs=[Fraction(0,1)]+[interior[j][1] for j in js]
                            rs=[r0]+[interior[j][2] for j in js]
                            H=H_of(ps,qs)
                            count+=1
                            has_hold_rows06 = any(r!=0 for r in rs)
                            # For full chains, aperiodicity also can come from row7.
                            # Count later with q7 multiplicity.
                            if H not in val_to_ex:
                                val_to_ex[H]=(i0,js,has_hold_rows06)
                            if H>maxH:
                                maxH=H
                                max_args=[(i0,js)]
                            elif H==maxH:
                                max_args.append((i0,js))
print(f"patterns {count} time {time.time()-t0:.1f}s")
print(f"maxH={maxH} = {float(maxH)} num_max_patterns={len(max_args)}")
print("max_args sample:", max_args[:5])
# distinct sorted descending
uniq_sorted=sorted(val_to_ex.keys(), reverse=True)
print("num distinct exact H values (rows0..6 patterns):", len(uniq_sorted))
print("top 10 exact:", [(str(v), float(v)) for v in uniq_sorted[:10]])
for v in uniq_sorted[:5]:
    print(f" value {v} ex {val_to_ex[v]}")
# Aperiodicity analysis:
# A pattern on rows0..6 with has_hold=True yields 4 aperiodic full chains (any q7).
# A pattern with has_hold=False (i.e., r0..r6 all zero) needs r7>0 (q7<1) for aperiodicity: 3 of 4 q7 choices.
# Count full aperiodic chains and check whether max pattern is aperiodic.
# r0=0 iff i0==3 (p0=1). interior r=0 iff j in {2,4,5}.
zero_interior={2,4,5}
# max pattern check
print("--- max pattern aperiodicity ---")
for (i0,js) in max_args:
    r0=p0_opts[i0][1]
    print(i0,js,"r0=",r0,"holds_interior=",[interior[j][2] for j in js])
# total counts
n_irred=4*6**6*4
n_periodic=1*3**6*1  # p0=1, interior in {2,4,5}, q7=1
print(f"n_irreducible={n_irred} n_periodic(all r=0)={n_periodic} n_aperiodic={n_irred-n_periodic}")
# Second: verify top-5 distinct values all have aperiodic representatives
for v in uniq_sorted[:5]:
    i0,js,has06=val_to_ex[v]
    print(f"H={v} has_hold_rows06={has06} -> has aperiodic rep: {has06 or True} (if not, q7<1 gives one)")
    # actually if has06 False, still aperiodic via q7 choices 1/4,1/2,3/4
