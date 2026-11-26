# Independent mathematical audit

## correctness

PASS

Count distinct strings: a factor with at most three minority ones can be an Abelian square only with zero or two ones. A two-one factor 0^x 1 0^b 1 0^y has one one in each half exactly when x+y≡b (mod 2) and |x−y|≤b. For three ones the two consecutive pairs therefore contribute distinct families unless their internal zero gaps agree; in that case subtract the intersection with the smaller outer bounds. In W_k the two families coincide. In V_k the middle gaps differ and the two counts are k(k+1)/2 and k(k+3)/2. For the latter, the k admissible diagonals e=x−y in [−(k−1),k−1] contribute k+1−|e|+1_{e>0} points each. Adding the zero-only squares proves both formulas, including k=1. The middle one moves right by one site; the counts differ by k²/2+O(k), with ratio tending to 2. For at most two minority occurrences an outer gap change adds or subtracts at most one row or column; a one-step internal gap change changes at most two permitted boundary points and the parity count by at most one per row. The two perturbed gap coordinates and the all-zero term therefore give O(n), including adjacent markers or empty end gaps. With zero or one minority occurrence, only majority-letter powers can count. The independent direct enumerator reproduced both families through k=12, all three-marker gap tuples with at most eight zeros, and checked 3,254 directed low-support swaps through length 14. These checks corroborate the algebra, not the universal bound by themselves.

## originality

PASS

The supported distinct claim is the sharp threshold of three minority occurrences for quadratic sensitivity under one adjacent interchange. Quadratic counts themselves with two occurrences and the exact three-marker classification are already covered by inspected works; neither is credited independently. The covering count formula gives the two witness values once the words are specified, but the checked sources do not choose these swap neighbors or establish the universal low-support sensitivity bound.

## value

PASS

This identifies a sharp boundary in a natural local perturbation problem. Sparse words already support quadratic complexity with two minority symbols, but two symbols cannot support a quadratic change under a single swap. Three suffice because the displacement destroys the coincidence of two extensively overlapping families of strings. The separation of complexity from sensitivity and the explicit matching-order witness give mathematical content beyond a count formula or a finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
