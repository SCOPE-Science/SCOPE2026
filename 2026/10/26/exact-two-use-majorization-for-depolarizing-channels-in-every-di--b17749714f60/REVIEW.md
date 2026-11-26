# Independent mathematical audit

## correctness

PASS

The frozen full-range theorem is mathematically sound, but the assessed replacement is the negative physical branch 1<p<=d^2/(d^2-1) for d>=3. For pure input with Schmidt probabilities lambda, the output is b^2 I-bc T+c^2|psi><psi|, T=Lambda⊗I+I⊗Lambda, b=p/d, c=p-1, and c/b<=1/d. Off-diagonal-sector eigenvalues are at least (b-c)b. The exact positive Gram sum I+vv*−2Lambda makes the diagonal block at least (b-c)b I−c(b-c) vv*, so at most one eigenvalue drops below (b-c)b and none is below (b-c)^2. Cauchy–Schwarz gives |psi><psi| <= (d/2)T and hence Z<=b^2 I. These bounds match the sorted product Lorenz curve by top partial sums up to (d−1)^2 and bottom partial sums thereafter, with equal trace. Ky Fan convexity extends the result to mixed states, and product inputs attain the comparator. The CP endpoint and zero Schmidt coefficients are allowed in all estimates. For the frozen nonnegative branch the same Gram inequality instead gives an upper rank-one bound and the universal lower floor b^2, also giving the corresponding partial sums. The supplied script was inspected but not executed; independent rational Gram checks and 1,050 pure-state numerical checks plus 30 endpoint checks, including the repaired regime, were run via /workspace/branches/77559ff2-0670-406a-a8b1-fe426208f64b/record4_check.py (logs record4-small.txt and record4-large.txt). Maximum residual was 2.665e-15; that does not prove the theorem. Corrected RESULT.md and VERIFICATION.md are in /workspace/repairs/4/ and the unchanged verifier is ancillary.

## originality

PASS

The full-range original could not pass originality as presented because it does not credit the known positive-coefficient two-use branch. The actual replacement strictly narrows to the negative branch in d>=3, credits Fujiwara–Hashizumé through the explicit attribution in Song et al. v2, and excludes the qubit sign-equivalence corollary. Exact spectral majorization in this remaining branch is not supplied by the inspected earlier norm, entropy, approximate-majorization or log-determinant results.

## value

PASS

The remaining branch is not an arbitrary parameter slice: the depolarizing coefficient changes sign at p=1 and reverses the product-spectrum ordering. In dimensions at least three the negative branch does not reduce to the positive case by the qubit spectrum symmetry. The replacement resolves every spectral partial sum through the CP endpoint in that unresolved part of the natural two-use problem, strictly more informative than entropy optimization or approximate order in this regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
