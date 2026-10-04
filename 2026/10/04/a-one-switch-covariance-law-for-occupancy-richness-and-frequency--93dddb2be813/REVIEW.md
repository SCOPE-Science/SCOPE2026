# Review

## Correctness

PASS. The covariance is reconstructed from the box indicators \(I_i=\mathbf 1_{\{N_i>0\}}\) and \(J_{i,r}=\mathbf 1_{\{N_i=r\}}\). The same-box and distinct-box probabilities are exact multinomial probabilities, and summing them gives the displayed closed form.

For \(m\ge3\), the covariance sign reduces exactly to whether
\[
q^{\,n-1}(q/s)^{n-r}
\]
is greater or less than one. The threshold in the finding is therefore exact. Equality would force
\[
(m-1)^{n+k-1}=m^{n-1}(m-2)^k,
\]
which is impossible because \(m-1\) is coprime to both factors on the right. Hence there is one strict sign switch and no zero case.

## Originality

PASS with a residual classical-urn risk. The complete Barbour--Gnedin paper was inspected at its definitions of \(K_n\) and \(X_{n,r}\), its statement that \(K_n=\sum_rX_{n,r}\), and its moment/covariance section. It studies joint normal approximation and covariance structures of the \(r\)-counts, including exact Poissonized covariance formulas, but the inspected statements do not give the finite uniform \(\operatorname{Cov}(K,K_r)\) phase diagram.

Barbour's univariate occupancy paper was also inspected at its setup and main-statistic discussion. It treats \(K_n\) and the \(r\)-counts separately through distributional approximation rather than the exact cross-covariance sign transition.

Semantic and exact-language searches for richness/singleton covariance, \(K_n\) versus \(K_{n,r}\), and finite multinomial occupancy did not locate the explicit one-switch threshold. Search failure is not treated as proof of novelty; the residual risk is recorded below.

## Value

PASS. \(K\) is observed richness and \(K_r\) is the occupancy frequency spectrum used to describe rare versus common classes. The theorem gives a complete finite-sample answer to which frequency counts move with versus against richness under the canonical equal-probability null model. In particular, it explains structurally why singletons always co-move positively with richness while sufficiently high occupancies move negatively, and it locates the unique transition exactly.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK formula_checks=80 brute_checks=80 singleton_checks=9801 nton_checks=9801 nozero_checks=499851 one_switch_checks=9801`.
