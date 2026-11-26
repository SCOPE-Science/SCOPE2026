# Independent mathematical audit

## correctness

PASS

The main counterexample is correct as frozen. With tail sum s, C1 holds by linear nonnegative coordinates, C2 is s/4≤s/2, C3 is s/8≤3s/16, and the geometric g iterates sum to 3t. For a=1/4, P_n=P+a^n(E−P), so there is norm summability, P_nP=P, but PP_n≠P under the interior hypothesis. Every row of P_n⋯P_(k+1) is in the convex hull of the rows of the rightmost P_(k+1), giving the positive lower and stated upper tail bounds independently of n. The Dobrushin coefficients of the factors are a^n δ(E); submultiplicativity gives the exact exponent in the bound. The column extrema form nested intervals with widths tending to zero, so the limits are rank-one, never P for a fixed k, and approach P as k→∞. They cannot all be the same; pairwise distinctness for every pair of indices is not required or asserted. In two states the scalar row difference multiplies at each step by a^n/2 for the stated witness. This disproves the published fixed-k convergence to the common P, not weak ergodicity. The frozen checker at line 24 tests (3/4)^(k+1) instead of the claimed (3/4)·4^(−k−1) upper bound, and its loop has sum_(k=0)^7 (19−k)=124 pairs, not the hard-coded 152 reported in the notes. The corrected complete check.py, RESULT.md, and VERIFICATION.md in /workspace/repairs/2/ fix both scientific reproducibility issues without altering the theorem proof or the frozen evidence. I inspected the uploaded checker rather than running it. An independent scalar recursion for the two second-column entries verifies both intended bounds and the exact width for all 124 pairs; replay python3 /tmp/opencode/nov02-independent-checks.py 2. This finite check corroborates the two-state example; the general proof is analytic.

## originality

PASS

The supported contribution is the specific all-interior, all-simplex-dimension counterexample to Theorem 3.5 in the 2024 paper's explicit reverse order, with rank-one start-dependent limits and a quantitative separation from weak mixing. The general distinction between different ergodicities and earlier projection-commuting perturbation theory are not claimed as new. No compared primary or indexed claim gave this correction.

## value

PASS

A strictly interior, rational and simplex-linear construction refutes a named theorem under all its listed assumptions, not by a boundary pathology. It locates the missing two-sided condition and explains precisely how summably convergent generators and superexponential row mixing coexist with persistent memory of the rightmost factor. This is a meaningful correction for downstream uses of the theorem; it asserts no automatic refutation of a separate quantum-chain claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
