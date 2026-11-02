# Scientific review

**Correctness (C): PASS.** Exact CRT local distributions give independent Bernoulli variables. For all residues the limiting log moment-generating function divided by \(H_Y\) is \(\cosh t-1\); for unit quadratic sums it is \(e^t-1\). Mertens' theorem in the classes modulo four supplies the required normalization. Both upper bounds follow by exponential Markov, and exponentially tilted bounded Bernoulli arrays have diverging variances, so their central limit theorems provide matching lower bounds. Exact-rational computation checks the underlying finite CRT identities. No finite experiment is treated as an infinite proof.

**Originality (O): PASS with residual risks.** Yan and Xu's Lemma 2.1 obtains only \(4/H\) and \(10/H\) by Chebyshev. Neither implies a positive sharp exponent on the logarithmic \(H\)-scale; the present proof additionally establishes exact tilted cumulant limits and matching lower bounds. Search comparisons covered the two event definitions, character prime sums, prime-square sieve exceptions, and general large-deviation equivalences; no explicit pair of sharp arithmetic rates was found. General mod-Poisson and large-deviation theorems are potential broader frameworks and remain a real priority risk, especially because the local CRT inputs are elementary.

**Mathematical value (V): PASS.** Both rates quantify *exactly* how exceptional the two sieve branches are at the canonical prime cutoff, improving the source's polynomial-in-\(H\) error bounds to provably optimal exponential-in-\(H\) scales. The two constants are different, reflecting respectively signed prime-splitting fluctuations and the absence of anisotropic local roots for quadratic sums. This supplies natural precise invariants for evaluating sharper Romanoff sieve arguments; no theorem about the original representation-set density rate is asserted.

**Closest comparison:** Yan–Xu arXiv:2610.28237v1, Lemma 2.1 and proof. The cited Dai–Pan representation theorem is complementary, not an upper-tail statement. Classical general large-deviation tools could yield related consequences but do not name the two arithmetic rates here without specializing local splitting data.

**Limitations:** Results are logarithmic only and concern the fixed all-odd-primes family; no uniform effective bounds over arbitrary finite prime sets. Earlier implicit large-deviation treatments may exist.

Self-review: passed. Independent audit: not yet performed.
