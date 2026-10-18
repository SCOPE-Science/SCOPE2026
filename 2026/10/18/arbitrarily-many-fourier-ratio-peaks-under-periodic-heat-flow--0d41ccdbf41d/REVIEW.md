# Scientific assessment

## Correctness — PASS

With normalized Fourier coefficients, a positive cosine amplitude contributes exactly two symmetric frequencies; this yields equation (1) in RESULT.md. The explicit logarithmic coefficient differences yield the crossing identity (2), and the minimum squared-frequency gap is \(3L^2\). Direct comparisons to the immediately adjacent crossing establish the \(\eta^2\) suppression at high times and \(\eta\) suppression at low times. Bounds (3)--(4) have a strict numerical gap for all allowed parameters; real analyticity turns each separated interior extremum into a strict one. The distinct amplification construction makes all paired Fourier coefficients equal at the selected time, while only the highest pair survives asymptotically at time zero. The standalone checker corroborated 197 finite identities/inequalities, including physical-grid Fourier transforms.

## Originality — PASS, with historical-priority risk

The relevant accessible primary literature studies fixed-time upper bounds (arXiv:2603.07851), spectral approximation and sampling (arXiv:2601.17493), stationary Fourier-ratio complexity classes (arXiv:2511.19560), and class metric entropy (arXiv:2606.24229). Their stated conclusions do not imply multiple strict temporal extrema or arbitrarily large actual trajectorywise amplification. Related indexed results on heat semigroup maximal regularity use a different mixed operator norm, not the Fourier \(\ell^1/\ell^2\) quotient. The searches do not prove uniqueness: an earlier unindexed exponential-family or heat-semigroup construction may cover this theorem.

## Value — PASS

Fourier ratio is used as an effective spectral dimension in recent sampling and recovery bounds. The theorem gives a structurally decisive limitation on a natural interpretation of dissipative spectral preconditioning: for individual signals, a smoothing semigroup can repeatedly raise and lower this measured complexity, even arbitrarily strongly. It provides a reproducible, all-order family of counterexamples, not merely a small numerical anomaly. It does not purport to contradict established parameter-dependent fixed-time estimates or supply new sampling guarantees.

Self-review: passed. Independent audit: not yet performed.
