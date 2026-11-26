# Independent mathematical audit

## correctness

PASS

The frozen exponential example's assertion that all 2^n coefficients are nonzero is false under the stated hypotheses: θ(x)=2^x−1 is a permitted principal angle (α=1, c=log 2, θ₀=−1) and its coefficient at the empty monomial is θ(0)=0. The complete corrected RESULT.md under /workspace/repairs/5 states the exact nonempty count, and the correct total according to the intercept; the frozen source remains intact. Re-auditing the corrected claim: iterating the fundamental theorem of calculus identifies D with the integral of θ^(q) over increments 2^{j−n}, j=0,…,q−1. Their product is exactly 2^{q(q−1)/2−qn}. Every evaluation of the derivative in the integral is within one block of its base, and every point of [0,1], including 1, is within one block of some base; the two modulus comparisons give the stated error inequality. A positive scalar multiple of x^q in the allowed angle range gives a constant qth derivative and exact normalization. Degree at most q−1 kills the alternating difference on every q-bit face; if it vanishes on all sufficiently fine grids the recovered derivative is zero, while ordinary polynomials give the converse by reducing b_j^k=b_j. This includes d=0. On the fixed most significant q-bit face (n≥q), the signed derivative assumption and product 2^{−q(q+1)/2} give a discrepancy at least that product times m₀; the alternating-sum functional has sup-norm dual norm 2^q, giving the uniform lower bound. Exponential factorization gives precisely the corrected nonempty coefficients and full degree n for all n≥1. On the q-face the alternating sign residual a/2^q times parity has highest coefficient a, so removing it attains the dual lower bound on that face. The unchanged script tests only the nonempty exponential coefficients; its loop counts sum independently to 2644, not a fresh assertion replay. Corrected verification documentation requires Python 3.10 because of int.bit_count and retains the frozen status metadata.

## originality

PASS

For the final corrected claim, credit the fixed-grid angle hierarchy and Möbius criteria to prior work, and the mixed difference and exponential-product identities to standard calculus and Boolean algebra. The supported distinct result is the cross-resolution derivative diagnostic and classification of a single smooth angle, with a refinement-independent approximation obstruction tied to the same hierarchy. No independent priority is asserted for the repaired coefficient arithmetic or the general parity duality.

## value

PASS

A fixed-grid classification does not decide what can remain low-degree while a quadrature grid is refined. In the natural principal-angle class the repaired theorem gives a complete smooth continuum classification and a normalized diagnostic for the derivative responsible for a degree violation. Its persistent leading-face lower bound explains why convergence of the low-bit differences to zero without normalization does not certify good compression. Correcting the count of constant terms leaves the full degree and exact face obstruction unchanged; neither the value nor the scientific scope relies on an all-circuit complexity claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
