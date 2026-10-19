# Scientific review: Gaussian first-exit crossover for randomly switched intermittent maps

## Correctness

**PASS.** The exact neutral-branch conjugacy sends an initial point approaching zero to a decreasing positive coordinate \(z\). One-step Taylor bounds are uniform on \(z\ge1\); the positive potential \(H_t(z)=\int_0^z(1+u)^{-t}\,du\) gives integrable stopping-time weighted occupations, including the terminal region. These bounds yield the stopping identity (2) with \(O_{\mathsf P}(\log Z)\) remainder, a fluid clock, and a weighted slow-choice law. A Bernoulli invariance principle evaluated at the asymptotically deterministic random stopping time supplies the normal component. Each of the three limits follows at its stated scale. The included finite checker also verifies exact rational cases and numerical consistency. Infinite limits do not depend on simulation.

## Originality

**PASS, with residual historical-priority risk.** Bahsoun--Bose--Duan (arXiv:1305.6588, Sections 2 and 4) analyze the identical random LSV family and derive polynomial return-interval bounds, not a second-order distribution for a small deterministic starting point. Bahsoun--Bose (arXiv:1503.06157, Theorem 1.1 and Section 2) establish a sharp almost-sure **first-order** random backward-interval location. Bahsoun--Bose--Ruziboev (arXiv:1706.04158, Section 5 and Proposition 5.5) establish quenched first-order scaling; they do not establish the proposed forward first-exit fluctuation or critical mean shift. Nicol--Török--Vaienti (arXiv:1510.03214, Introduction and Sections 3 and 5) give CLTs for Birkhoff sums of observables, not for an initial-state-dependent laminar stopping clock. The earlier technical bound \(\beta<3\alpha/2\) mentioned in arXiv:1305.6588 concerns a distinct correlation-decay argument and implies none of the three probability limits here. Published-paper and mathematical-record searches found no equivalent or stronger specific result; a negative search is not a uniqueness proof. Broader generic Markov-process first-passage theory and historically unindexed treatments remain risks.

## Mathematical value

**PASS.** A large neutral-point residence time is a canonical observable for intermittency, and its first-order speed was already an object of published study. The present law resolves the competition between rare slow-map corrections and unavoidable Bernoulli fluctuations: it identifies a genuine trichotomy, a sharp exponent ratio, the drift coefficient, and the variance. The threshold is not an arbitrary parameter slice and changes the limiting distribution, providing a natural finite-size refinement of first-order intermittent escape.

## Limitations and external validation

Only iid map choices and a deterministic small initial state are covered. This is an annealed first-exit theorem, not an invariant-measure or fixed-environment CLT. A further centered CLT in the subcritical range would require additional drift terms and is not claimed. Independent historical-priority review remains open.

Self-review: passed. Independent audit: not yet performed.
