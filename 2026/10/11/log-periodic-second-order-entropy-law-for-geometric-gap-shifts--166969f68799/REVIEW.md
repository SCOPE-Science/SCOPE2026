# Scientific review: geometric-gap constrained-entropy asymptotics

## Correctness — PASS

The claim specifies the bilateral \(S\)-gap shift, the symbol-frequency constraint, entropy normalization, and the limiting order. The proof first splits off the all-zero fixed-point atom before applying Kac and Abramov, so no invalid return-mean identity is assumed for mixtures. The relative-entropy inequality with \(\lambda>0\) shows both optimality and uniqueness of the stationary independent-renewal measure. The geometric tails yield **uniform** \(O_b(b^{-K})\) errors, and the logarithmic inversion yields a uniform \(O_b((\log L)^2/L^2)\) remainder. The phase's nonconstancy follows from its Fourier coefficient \(\Gamma(1-2\pi i/\log b)/\log b\ne0\), the derivative factorization, and periodicity; the exact cluster interval follows by phase sampling. The independent stdlib checker actually passed 19 finite diagnostics; these are not substituted for proofs.

## Originality — PASS, with specified residual risk

The 2026 Haydarov–Kadyrov–Makhmudov–Mamayusupov paper provides arbitrary-\(S\) induced Bernoulli weights and strict pressure results, and its atom-splitting discussion is explicitly incorporated. The constrained renewal formula is therefore **not** presented as a new general technique; applying their framework to a marker chemical potential is natural. Ramirez–Somers (2025) study topological entropy of gap shifts and explicitly mention power-of-two gaps, but do not compute frequency-constrained asymptotics. Climenhaga (2014) gives the classical topological-entropy equation and induction argument. The exact normalized sparse-frequency coefficient \(\Xi_b\), its gamma-function nonconstancy and the resulting full cluster interval do not follow as stated from these inspected results without new lacunary asymptotic analysis. Actual searches of published-finding corpus and public literature using geometric gaps, density spectrum, renewal entropy, and log-periodic aliases yielded no equivalent claim. Since Mellin asymptotics are classical, an older formulation could exist outside the sources inspected; originality is not a claim of global uniqueness.

## Mathematical value — PASS

The problem is natural because geometric return lengths form a standard sparse \(S\)-gap family, and fixing the rare-marker frequency is a canonical multifractal/thermodynamic constraint. The result measures the exact cost of rare markers, proves an iterated-logarithmic first order instead of the ordinary finite-gap entropy scale, and identifies a genuinely nonconstant second-order lattice invariant for **all** integral geometric bases. The phase correction survives a precise normalization and is not a cosmetic reparameterization of the usual unconstrained pressure equation. It can inform quantitative density spectra and benchmarks for renewal thermodynamic asymptotics. No paper-sized downstream theorem is asserted.

## Closest literature and limitations

Primary comparisons: arXiv:2606.17031v1 (full publicly available manuscript, Sections 1–8), arXiv:2501.08438v1 (complete HTML mathematical text), and Climenhaga's 2014 exposition (complete text). The result concerns an exactly defined family and one low-density endpoint; it does not address other return sets or claim an independent audit.

Same-model review: passed. Independent audit: not yet performed.
