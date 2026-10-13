# Review

## Correctness
PASS. The source recursion specializes exactly to the invariant ray \(L=\{[r:r:1:1]\}\) with scalar map \(f(r)=(r^3+2)/(2r^3+1)\). The exact factorization of \(f^{\circ2}(r)-r\) proves global attraction on \(r>0\), and the cubic normal form \(g(1+u)=1+u-(4/3)u^3+O(u^4)\) yields \(m u_m^2\to3/8\), hence the sharp full-iterate amplitude \(\sqrt3/2\). The checker independently replays the polynomial identities with exact arithmetic.

## Originality
PASS. The primary source gives the projective recursion and highlights \((q,d)=(4,3)\) as exceptional, but does not state the zero-temperature pair-symmetric global dynamics or sharp amplitude. The later Gu--Wu--Yang positive-temperature uniqueness/power-law result assumes uniqueness at the critical point and does not cover the non-unique endpoint \(q=d+1,w=0\). Jonasson establishes global non-uniqueness for proper colourings at this endpoint, not the invariant-ray relaxation. Targeted scientific searches for the pair-symmetric recurrence, zero-temperature critical ray, and \(\sqrt n\) law returned no covering statement. Residual risk remains from older Bethe-lattice literature available only at abstract level.

## Value
PASS. The endpoint \(q=d+1\) is the exact boundary where global uniqueness fails through frozen colourings. Showing that the most natural balanced 2+2 symmetry channel is instead marginally stable, with a universal \(n^{-1/2}\) amplitude, separates that channel from the mechanism of non-uniqueness and gives a sharp dynamical boundary fact rather than a routine restatement of non-uniqueness.

Closest literature and limitations are described in `RESULT.md` and `AUDIT.json`. The statement is deliberately restricted to the invariant pair-symmetric ray and makes no claim of full Gibbs uniqueness.

Self-review: passed. Independent audit: not yet performed.
