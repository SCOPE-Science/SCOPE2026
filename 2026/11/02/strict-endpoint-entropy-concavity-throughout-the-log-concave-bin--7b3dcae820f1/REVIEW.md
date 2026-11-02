# Review of the binary-Gaussian endpoint-curvature finding

## Correctness — PASS

The initial mixture's log-density has a second derivative whose supremum occurs at zero; it is nonpositive exactly through \(\alpha=1/2\). The independent normalized half-thermalized mixture has variance one and a smooth strictly positive Gaussian-tail density. Its score admits three explicit derivatives. Integration by parts exactly identifies the curvature correction \(B=\mathbb E[\rho^{(3)}]\). Gaussian-reference tilting by \(\operatorname{sech}\) and negative covariance with \(Z^2\) show \(B<0\) strictly for the complete parameter range. The fourth cumulant is \(-\alpha^2/2\), and the previously established endpoint identity then gives the claimed strict negativity. Dominated convergence gives the exact fourth-order coefficient. Independent mixture-entropy quadrature agrees with the score method on tested parameters. The code tests are finite and do not replace the proof.

## Originality — PASS, qualified

The closest primary source, Abu-Ajamieh (arXiv:2610.22386), already proves the endpoint identity and a general *conditional* sign rule; neither is claimed here. Its generalized-Gaussian and Hermite-mode theorems do not directly treat the separated-mean binary normal mixture. Eskenazis–Gavalakis (arXiv:2308.15997) prove a stronger full-interval theorem for centered Gaussian *scale* mixtures, but every such scale mixture has nonnegative fourth cumulant, whereas the present family has strictly negative fourth cumulant. Luo (arXiv:2609.11418) supplies an asymmetric counterexample, not coverage of this symmetric family. Literature and mathematical-record searches did not locate this exact continuous-parameter sign theorem or its fourth-order coefficient; search failure is not proof of uniqueness. A broader, still-unlocated location-mixture theorem is the material residual risk.

## Value — PASS

The family is the simplest two-well Gaussian preparation, naturally relevant to Ornstein–Uhlenbeck thermalization and entropy geometry. The parameter cutoff is not arbitrarily selected: \(\alpha=1/2\) is exactly the boundary of log-concavity, so the result exhausts the whole physically and mathematically motivated subfamily. The sign follows from a nontrivial weighted \(\operatorname{sech}\) inequality, not just evaluating the published identity. The sharp quartic coefficient measures how fast strict curvature emerges as Gaussian equilibrium is departed from. No full interior concavity or general symmetric-log-concave conjecture is asserted.

## Limitations and comparison

Independent mathematical and publication-priority audits have not been performed. The strict statement is local to mixing endpoints; no theorem for all \(0<t<1\) is claimed. Numerical verification checks are bounded. Priority remains qualified for unlocated broader Gaussian-location-mixture literature.

Self-review: passed. Independent audit: not yet performed.
