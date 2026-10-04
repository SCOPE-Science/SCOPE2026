# Same-model review

## Correctness
PASS. The proof reduces the singleton fingerprint to a one-dimensional scale function along each odds ray. Its logarithmic derivative has the exact sign of \(1-\sum_i p_i\), which proves injectivity on \(\sum_i p_i\le1\). The homogeneous function \(u(1-u)^{n-1}\) supplies the exact fold beyond \(1/n\), and the boundary Taylor expansion is checked against the explicit second derivative. Total variation is lower-bounded by the marginal difference under coordinate projection.

## Originality
PASS. The recent general product-TV proxy uses full midpoint-score information, not the singleton slice. The precursor Bernoulli paper proves singleton control only on \([0,1/(2n)]^n\) and does not state the exact injectivity threshold, the loss of Lipschitz stability at \(1/n\), or nonidentifiability above it. research-index and public-literature searches using singleton-slice, odds-ray, exactly-one-success, inverse Poisson-binomial and \(1/n\)-threshold aliases found no implication-equivalent statement. Residual risk from differently named inverse-problem literature remains.

## Value
PASS. The result gives a sharp structural boundary for the specific low-complexity statistic used to approximate a generally hard product total-variation problem. It shows that the earlier \(1/(2n)\) regime is not an identifiability limit, pinpoints the exact point where identifiability ends, and distinguishes that from the earlier loss of uniform stability at the boundary. This directly constrains what any extension based only on singleton probabilities can achieve.

## Closest literature and limitations
The closest sources are arXiv:2609.21049v1, which gives a universal product-TV proxy and cites the Bernoulli small-parameter program, and arXiv:2602.21828v1, whose Theorem 1.2 and Lemma 4.3 control total variation and parameters by the singleton slice on \([0,1/(2n)]^n\). The present result does not determine whether a useful dimension-free singleton comparison extends through any or all of the open interval between \(1/(2n)\) and \(1/n\).

Same-model review: passed. Independent audit: not yet performed.
