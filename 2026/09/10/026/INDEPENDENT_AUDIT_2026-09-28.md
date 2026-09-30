# Independent audit — 2026-09-28

Record: `2026/09/10/026`  
Audited tree: `3b0fa472fc7859b9a425db041bf617459eba8b45`  
Disposition: **passed**

## Correctness
The central corrected claim survives independent arithmetic checks. The discriminant of `x^5-5x^3+4x+1` is `38569`, so reduction at 7 is good. Exact substitution gives squares at
`x=-2,-1,0,1,2,3,-7/4,4/9`, producing 16 signed affine rational points plus the unique point at infinity, hence at least 17 rational points. Direct counting gives `#C(F_7)=14` including infinity. Under the rank-one hypothesis, Coleman's genus-two bound at `p=7>2g` would give at most `14+2=16` rational points, contradicting the 17 exhibited points. Therefore `rank J(Q)>=2`.

The additional torsion/Galois computations are consistent with the stated exact finite-field and factorization arguments; they are not needed for the rank-floor conclusion.

## Originality
The same polynomial's `S5` Galois group was publicly discussed before this record, so that ingredient is not new. I did not locate the exact 17-point floor plus Coleman rank-2 contradiction in the targeted prior-art search. This supports, but does not prove, originality of the corrected census-floor package.

## Scientific value
The record is a useful correction: it decisively refutes a rank-one/six-point premise and supplies a rigorous lower bound. It does not provide a complete rational-point census or exact Mordell–Weil rank.

## Sources
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/026
- https://doi.org/10.1215/S0012-7094-85-05240-8
- https://math.stackexchange.com/questions/4205705/galois-group-of-x5-5x34x1-in-mathbbqx
- https://arxiv.org/abs/2509.24604
