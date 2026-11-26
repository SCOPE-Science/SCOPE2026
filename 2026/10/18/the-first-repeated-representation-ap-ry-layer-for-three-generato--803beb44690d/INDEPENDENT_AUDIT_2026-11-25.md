# Independent mathematical audit

## correctness

PASS

Writing N=mk+r, each pair (y,z) is uniquely in row t≥0 with y+(b+1)z=r+tm. Divide r+tm by b+1 to get quotient h_t and remainder s_t. With j=h_t−z in [0,h_t], the threshold k for a nonnegative x is t+h_t+s_t+bj. Distinct (t,j) count separately, including ties. Since m=b(b+1)+1, row minima rise by b+2 without carry and by 2 with carry. Thus beyond the cheapest pair at (t,j)=(0,0), the next threshold is the minimum of row one's first threshold and, if q≥1, row zero's second threshold. This gives q+b+2 for s=b (including the tie when b=2,q≥1), s+b+2 for q=0,s<b and q+s+b otherwise, including q=b,s=0. Upon adding m, incrementing x retains all representations. Thus n_1 is the sum of the heights, and g_1 is max W_r−m. The four maxima of W_r are (2b+2)m−2, (3b−1)m−3, (2b+1)m+b−1 and (2b+1)m−1 for s=b, interior q≥1 and s<b, q=0 and s<b, and the endpoint q=b,s=0 respectively. Only the first two compete; their difference in the order second minus first is (b−3)m−1. Summing the three branches over q=0 and s<b, 1≤q≤b−1 and s<b, s=b, and the endpoint gives b(4b²+b+11)/2, counting zero as deficient. An independent x=0 pair-threshold enumeration corroborates all 3097 thresholds and both invariants for bases 2–20: python3 /workspace/branches/independent_replay.py 3. The row argument proves the unbounded b claim.

## originality

PASS

Pass is for the uniform b-dependent classification and its invariant formulas, not the first-repeat method or the exact b=3 case. A distinct same-day Resultary finding gives the identical p=1 layer at b=3 by the same row-cost technique for fixed gap 4. Its theorem does not cover the varying gap b+1 or the comparison between residue maximizers as b crosses 4. The generalized repunit literature covers the same triple for one representation; other inspected positive-p formulas have different generator or count-range hypotheses.

## value

PASS

The three minimal generators arise from a named family already studied at the ordinary Apéry layer. This complete second layer resolves all deficient residues at once, and the controlling maximum actually changes at b=4 rather than following the smallest cases. The explicit layer, transition and uniform count give useful exact information for comparisons with higher representation levels; the advancement is not the shared b=3 datum or the existence of a counting algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
