# Review of A sharp oracle tuning envelope for Gaussian-mixture sequential \(t\)-martingales

## Correctness
PASS. The source martingale formula was inspected in Wang--Ramdas, Theorem 4.9 and equation (41). Squaring the formula and writing \(x=c^2\), \(t=T_{n-1}^2\) gives an elementary rational expression whose logarithmic derivative factors exactly as
\[
-\frac{n(n-1)(x(t-1)-n)}{x(n+x)(n(n-1)+(n-1+t)x)}.
\]
This proves the unique interior optimizer for \(t>1\), the boundary behavior for \(t\le1\), and the closed-form envelope. The barrier monotonicity and Lambert-\(W\) limit follow from one-variable monotonicity. The bundled verifier independently evaluates these identities and constants. The main limit is analytic; finite numerical checks are supporting verification, not the proof.

## Originality
PASS with residual risk. Wang--Ramdas state that \(c\) affects nonasymptotic power, express the martingale through \(T_{n-1}\), and note that both very small and very large \(c\) destroy fixed-time evidence. Lindon et al. derive the same martingale family and tune the Gaussian prior through expected log-growth, minimum detectable effect, and confidence-set width. Neither inspected source states the realized-statistic optimizer \(c_*^2=n/(T_{n-1}^2-1)\), the resulting pointwise envelope, or the Lambert-\(W\) limiting crossing barrier. Targeted database and exact-form searches found no equivalent statement. Older Bayes-factor or empirical-Bayes literature remains a plausible alias risk.

## Value
PASS. The precision hyperparameter is explicitly identified by the source papers as controlling finite-time power and confidence-sequence tightness. The envelope answers the natural tuning-robust question of how much evidence *any* member of this published family could possibly produce at a fixed observed \(t\)-statistic. It yields a sharp necessary rejection threshold independent of the chosen precision and quantifies irreducible fixed-time conservatism of the family, even under an oracle comparison. The result also marks the exact boundary between legitimate fixed-precision martingales and an invalidly interpreted post-hoc maximum.

## Closest literature and limitations
The closest sources are Lindon et al., arXiv:2210.08589, and Wang--Ramdas, arXiv:2310.03722. The claim is restricted to their one-dimensional full-Gaussian-prior scale-invariant martingale. It does not claim validity for post-hoc tuning and does not dominate universal-inference, half-Gaussian, or other sequential \(t\)-test constructions.

Same-model review: passed. Independent audit: not yet performed.
