# Scientific review: collision-profile positivity

## Correctness — PASS

The claim is an exact finite polynomial identity, not an extrapolation from examples. The characteristic function of a sum of independent Bernoulli variables factors, Plancherel converts its squared modulus into a collision probability, and each factor equals the sum of a nonnegative cosine square and a nonnegative squared-bias multiple of a sine square. Every coefficient is an integral of products positive almost everywhere, since the positive integer weights have only finitely many trigonometric zeros. This proves strict positivity at every polynomial order and gives the derivative hierarchy including boundary values. The two global inequalities follow term by term, and their equality conditions follow from strict positivity. Exact rational tests (9,681 assertions) independently verify finite instances and normalization. No numerical extrapolation is used in the proof.

## Originality — PASS, subject to priority risks

The motivating 2026 overlap-Bernoulli paper concerns Shannon entropy and does not state the all-order positivity of the order-two collision profile. The closely related 2026 work on Rényi entropies of weighted Bernoulli sums compares different Rényi orders for fair inputs and explicitly identifies biased extensions as a separate direction; its inspected results are not statements about variation along a shared Bernoulli bias. The earlier binomial index-of-coincidence work treats equal weights, and the Shepp–Olkin entropy theorem concerns Shannon entropy of ordinary sums. These cannot imply a universal statement about all integer weights by changing terminology alone. Actual targeted scholarly and mathematical-record searches found no statement dominating the theorem. A generic earlier Fourier positive-product theorem or a different formulation of the collision kernel could nonetheless contain it; the 2023 Fourier-based Rényi paper was not fully accessible. Independent priority assessment remains necessary.

## Value — PASS

The Shannon concavity problem for recursively overlapping Bernoulli distributions has been explicitly proposed for all overlap sequences. Collision entropy is a natural, analytically distinct information functional; it is also the probability that two independent recursive samples meet, and controls order-two entropy estimates. The result determines its **complete finite-degree bias profile sign structure**, not merely a numerical minimum: every coefficient is positive for arbitrary additive collisions, every derivative with respect to \(p(1-p)\) has a fixed strict alternating sign, and a universal sharp quadratic upper envelope is available in terms of the fair-bias collision probability. These structural bounds are valid uniformly over all finite overlap sequences and do not need an asymptotic regime. They do not prove the original Shannon conjecture or optimize fixed-length envelopes.

## Literature and limitations

Neunhäuserer, arXiv:2609.05546v1 (2026), provides the overlapping-distribution model and the separate open Shannon conjecture. Li, arXiv:2609.01529 (2026), provides general Rényi comparisons in the fair-input case, not the bias profile. Raşa, arXiv:1706.05178 (2017), treats the equal-weight binomial index of coincidence. Hillion–Johnson (2017) concerns Shepp–Olkin Shannon concavity. Madiman–Melbourne–Roberto (2023) studies Fourier-based bounds for Rényi entropy; complete inspection of that paper was not possible. The Fourier method itself is classical and is not claimed as original. A prior general positivity theorem could cover the present application.

Self-review: passed. Independent audit: not yet performed.
