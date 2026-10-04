# Same-model review

## Correctness

PASS. The source's linearized logarithmic process retains additive compensated Poisson jumps. For a Hurwitz drift, the stationary jump convolution has fourth cumulant
\[
\int_0^\infty\!\!\int_Z
\bigl(v^\top e^{As}h(u)\bigr)^4\,\nu(du)\,ds.
\]
The explicit one-atom witness has a nonzero susceptible jump, so this integral is strictly positive for \(v=e_1\). An exact Gaussian law is therefore impossible. The source forward equation also omits the shifted-density jump operator, and its diagonal jump coefficient differs from the true log-jump second cumulant.

## Originality

PASS. Non-Gaussian Lévy-driven Ornstein–Uhlenbeck stationary laws are established prior theory and are treated as such. The new result is the exact application to the published SVI theorem: a source-admissible epidemic parameter set satisfies the theorem threshold, has a Hurwitz quasi-endemic linearization, and still has a nonzero stationary fourth cumulant. Exact source-title, DOI, density, correction, and jump-generator searches found no published source-specific repair.

## Value

PASS. The source presents the density formula as a central technique for describing fluctuations near the quasi-endemic state. The correction shows that the claimed Gaussian/log-normal law is structurally incompatible with the model's own nonzero Lévy jumps and even uses the wrong second-order jump coefficient. It identifies the correct Brownian-only boundary and the nonlocal operator needed for a genuine jump-density calculation.

## Closest literature and limitations

The primary source is DOI 10.3934/math.2023148. The closest general literature is the Lévy-driven Ornstein–Uhlenbeck theory of Jongbloed, van der Meulen, and van der Vaart (2005), DOI 10.3150/bj/1130077593, and the non-Gaussian OU construction of Barndorff-Nielsen and Shephard (2001), DOI 10.1111/1467-9868.00282.

The result corrects the exact density claim for the linearized process. It does not classify the nonlinear stationary law or rule out separately justified diffusion approximations.

Same-model review: passed. Independent audit: not yet performed.
