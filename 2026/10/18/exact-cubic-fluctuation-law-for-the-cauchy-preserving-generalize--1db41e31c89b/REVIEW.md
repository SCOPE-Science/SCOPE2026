# Scientific review

## Correctness

**PASS.** The claim is for Cauchy-stationary \(T_{\alpha,\beta}(x)=\alpha x-\beta/x\) with \(0<\alpha<1\), \(\beta>0\), and the bounded rational Cayley observable. Direct Cayley algebra gives the finite Blaschke product \(B_t(z)=z(z+t)/(1+tz)\) with \(t=2\alpha-1\); since \(B_t(0)=0\), Haar invariance follows by analytic Fourier moments. Extracting the first two Taylor coefficients of iterates and using exact analytic quotient factorizations establishes the two- and three-time correlation identities, including repeated-index boundaries. Combinatorial multiplicities then give the exact finite-horizon cumulant. Absolute convergence at every fixed \(|t|<1\) justifies the asymptotic limit. The standalone verification script returned `VERIFY_OK`, but finite checks are not used as proofs.

## Originality

**PASS within inspected evidence, with residual bibliographic risk.** Umeno and Okubo, arXiv:1510.08569, supply the Cauchy invariant state, mixing regime and mean Lyapunov law. Nicolau, arXiv:2103.07238, and Nicolau–Soler i Gibert, arXiv:2305.02042, supply general inner-function iterate theory, including the second-order variance and central limit theorem. Their inspected statements establish those antecedents but do not provide the exact parameterized third-cumulant rate \(3\alpha/[8(1-\alpha)^2]\) for this natural generalized Boole sensor or its opposing endpoint scalings. General correlation estimates are not equivalent to an explicit coefficient. An unlocated exact formula or specialization in broader analytic-dynamics literature remains possible; this review does not certify literature exhaustiveness.

## Mathematical value

**PASS.** This is a motivated fluctuation invariant, not a sample integer or a routine renaming of the mean exponent. The probe \((x^2-s^2)/(x^2+s^2)\) is the real Cayley phase, is bounded under a heavy-tailed invariant state, and is canonical under the known rational-to-Blaschke conjugacy. The complete exact three-time function determines all finite third cumulants and a sharp asymptotic coefficient. In the two zero-Lyapunov limits, the cubic coefficient exhibits opposite vanishing and divergence, distinguishing alternating and persistent long-memory approaches to nonmixing. The variance and CLT are background, not a novelty claim. No assertion about generic observables or uniform critical-limit CLTs is made.

## Closest literature and limitations

The nearest broad result is The Central Limit Theorem for inner functions II, especially the covariance normalization in equation (1.2) and the higher-order correlation estimates of Section 4. The nearest model-specific source is Exact Lyapunov exponents of the generalized Boole transformations. The novelty claim concerns a *closed third-order coefficient*, not mixing, Haar invariance, the Lyapunov formula, or the already known second-order covariance. Only a defined observable, interior parameters, and sequential parameter/horizon limits are covered. Literature coverage is qualified by the possibility of an equivalent calculation elsewhere.

Self-review: passed. Independent audit: not yet performed.
