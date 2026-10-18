# Scientific review: equal-block coarsening preserves ultra-log-concavity

## Correctness — PASS
The precise hypotheses are nonnegative integer support with no internal zeros and ultra-log-concavity \(n a_n^2\ge(n+1)a_{n-1}a_{n+1}\). The proof converts this to ordinary log-concavity of \(c_n=n!a_n\), applies a two-middle versus two-outer product inequality at each pair of block residues, and independently proves the sharp factorial-weight comparison by monotonicity in the two residues. Summation gives the target ULC inequality at every integer block index. Positive outer blocks force all middle original coordinates positive, so the strictness conclusion follows from the strictly positive \((0,0)\) summand for \(m\ge2\). The Poisson/Erlang interpretation is exactly pathwise; covariance with the strictly decreasing size-biased adjacent-mass ratio yields strict variance underdispersion. The finite exact-rational verifier confirms sampled identities, not infinite quantifiers.

## Originality — PASS, subject to independent priority verification
The most relevant open-access 2023 article by Puig, Valero and Fernández-Fontelo proves/quotes renewal-count underdispersion from an IFR interarrival law (Section 2.1, Proposition 1), which is weaker than ultra-log-concavity. Badiella, del Castillo and Puig (2023) establish ULC for *order statistics* (its main theorem), whereas \(X\mapsto\lfloor X/mfloor\) is a different, deterministic coarsening operation. Neither statement implies the present universal preservation result. General ULC closure under convolution and binomial thinning likewise does not subsume this nonrandom many-to-one map. Mathematical-record searches and previous-claim comparisons did not identify coverage, but 2026 grouped-Poisson modeling articles were only inspectable at abstract level and differently named older results remain a priority risk.

## Value — PASS
The assertion supplies an all-distributions closure theorem for a natural grouped-count observation mechanism, not merely a fitted numerical example. Its strictness theorem upgrades the known underdispersion conclusion for ordinary integer-shape Erlang renewal counts to a full adjacent-probability shape constraint. Equal block size is integral to the sharp factorial comparison, establishing a structural reason for the condition. The result does not classify noninteger Gamma renewals or unequal-width grouping.

## Sources and limits
- Badiella, del Castillo and Puig, *Ultra log-concavity of discrete order statistics*, 2023, DOI: 10.1016/j.spl.2023.109900. First online 26 June 2023. The publisher-indexed text includes the definition, main theorem/proof, synchronized-sequence proposition and corollary; direct full PDF access was denied.
- Puig, Valero and Fernández-Fontelo, *Some mechanisms leading to underdispersion*, 2023 first-online / 2024 issue, DOI: 10.1111/sjos.12677. Open-access full text, especially Section 2.1 and discussion of renewal underdispersion.
- Johnson, *Log-concavity and the maximum entropy property of the Poisson distribution*, 2007, DOI: 10.1016/j.spa.2006.10.006, for classical ULC context.

Self-review: passed. Independent audit: not yet performed.
