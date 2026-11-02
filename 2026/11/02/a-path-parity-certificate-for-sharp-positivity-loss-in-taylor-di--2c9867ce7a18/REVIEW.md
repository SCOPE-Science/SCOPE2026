# Scientific review

## Correctness

**PASS.** The identity \(T_s(h)=\sum_{j=0}^s h^jE_{s-j}(-dh)A^j/j!\) follows by binomial expansion, and the alternating-series bound \(E_m(-x)\ge0\) for \(0\le x\le1\) proves the entire sufficient interval. Under the walk gap, only \(A^{s-1}\) survives, giving one exactly negative entry beyond the bound. The directed/undirected bipartite corollary follows from shortest-path minimality and parity. The exact checker passed 698 grouped assertions in 29 cases. No spectral inference or finite-to-infinite extrapolation is used.

## Originality

**PASS, with historical risk.** General positivity and SSP time-step bounds are known. Horváth (1998), Sections 4–5, and Horváth (2005), Theorem 8 and Section 4, concern universal problem-class thresholds and invariant cones. Gottlieb–Grant–Higgs (2014), Section 2, explicitly supplies the known linear-order-\(s\) SSP coefficient-one sufficiency; that part is not novel. The present statement instead proves per-network necessity for every weighted regular bipartite graph of enough diameter, via a specific pair whose short and opposite-parity walk powers vanish. The available primary full texts and mathematical-record searches did not state an equivalent graph-distance characterization, but absence from those sources is not a proof of absolute uniqueness.

## Value

**PASS.** A graph-theoretic certificate exactly identifies when an arbitrary-order positive Markov diffusion approximation cannot use a timestep larger than forward Euler, despite its higher accuracy order. It applies to large structured and irregularly weighted (but constant-exit-rate) network families and supplies a concrete negative transition entry, not merely a stability bound. This distinguishes entrywise positivity from spectral stability and gives a sharp numerical safety cutoff that cannot be improved on the stated networks.

## Closest sources and limitations

- Gottlieb, Grant and Higgs, arXiv:1403.6519v1, inspected complete accessible HTML sections: generic SSP theory and the linear-order-\(s\) coefficient-one construction; no per-bipartite-graph sharpness.
- Horváth, DOI:10.1016/j.apnum.2004.08.026, complete 16-page authorized text inspected: classwise sharp thresholds and initial-data cones, not a shortest-walk parity certificate for Taylor matrix polynomials.
- Horváth, DOI:10.1016/S0168-9274(98)00050-6, complete 18-page authorized text inspected: absolute monotonicity and general positivity radius, not the stated all-graph necessary witness.
- Residual risks: specialized graph-specific Runge–Kutta literature may have derived the same sharpness criterion, and the theorem deliberately makes no claim for nonconstant-degree graphs or networks without the indicated walk gap.

Self-review: passed. Independent audit: not yet performed.
