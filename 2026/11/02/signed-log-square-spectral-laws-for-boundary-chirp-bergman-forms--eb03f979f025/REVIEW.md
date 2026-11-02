# Review: signed log-square spectral laws for boundary-chirp Bergman forms

## Correctness

**PASS (self-review).** Normalized disk Bergman monomials give the diagonal moments \(s\int_0^\infty e^{-su}u^{-\beta}\sin(1/u)\,du\). The radial-cutoff improper integral converges for precisely \(0\le\beta<2\); the Macdonald integral, approached from its damped half-plane, gives the exact complex-\(K\) formula. The fixed-ray Bessel expansion yields the positive envelope \(\sqrt\pi s^{(2\beta+1)/4}e^{-\sqrt{2s}}\) and a uniform absolute-envelope error \(O_\beta(s^{-1/2})\). Integer-point counting in \(x=\sqrt{2s}\) gives \(O(L)\) exceptions near sine zeros and near the spectral threshold, proving both sharp second coefficients. The special half-integer case is exact. The checker completed 93 finite assertions, including independent oscillatory quadrature; finite checks do not replace the analytical infinite proofs.

## Originality

**PASS, with historical-priority qualifications.** Taskinen and Virtanen (arXiv:1703.09896, especially Proposition 3.2) already construct a closely related inverse-boundary sine symbol whose generalized Bergman Toeplitz operator is bounded while its absolute-value counterpart is not. Their paper is not cited as evidence that cancellation or generalized boundedness is new. Hagger, Liu, Taskinen and Virtanen (arXiv:2011.04699, Section 6) broaden such examples to arbitrarily large radial oscillation with bounded or compact operators, but the inspected treatment does not give this exact complex-Bessel spectrum or the two-term **sign-resolved** counting asymptotics. Rozenblum (arXiv:1012.3528, Section 5) proves a different radial cancellation effect for Fock-type symbols at infinity, while Rozenblum and Vasilevski (arXiv:1912.05855) develop trace-class form machinery and legitimate Berezin trace formulas, not this divergent naive symbol-diagonal integral. Le (2010, author-hosted PDF) constructs positive unbounded trace-class radial symbols supported on small sets; its trace-diagonal argument explicitly uses positivity and a convergent kernel integral, so does not dominate this sign-changing case. Published mathematical-results searches and an accessible local claims ledger yielded no identical or dominating signed-count theorem. Equivalent earlier formulations under a different radial coordinate remain a residual risk; absence in search results is not proof of priority.

## Mathematical value

**PASS.** The result supplies a sharp spectral invariant for a canonical boundary-chirp scale: the leading \(L^2\) count is universal, while its explicit \(L\log L\) coefficient determines \(\beta\), even though positive and negative modes have extensive cancellation. The exact half-integer spectrum gives an injective, sign-indefinite, all-Schatten example with a non-\(L^1\) symbol. The naive kernel-diagonal trace integral diverges although the operator is trace class, giving a concrete boundary between formal and justified trace manipulations. These structural properties are stronger than mere boundedness or a generic compactness example.

## Scientific limits

The classification is for fixed \(0\le\beta<2\), normalized analytic Bergman disk and radial-cutoff regularization. Alternative generalized forms for \(\beta\ge2\) are not excluded. No optimal error below \(O_\beta(L)\) or individual higher-order spectral expansions at sine zeros are claimed. The numerical checks are supplementary; historical priority is qualified; independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
