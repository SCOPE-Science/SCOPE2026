# Research review — Optimal Cho certificates for directed \(\ell_p\) Rips filtrations

## Correctness (PASS)

The theorem is quantified over every zero-diagonal directed nonnegative dissimilarity, any ordered finite tuple, every \(p\in(0,\infty]\), and every inclusive scale. The key finite-exponent identity is the longest increasing-index path recurrence \(D_j=\max_{i<j}(D_i+G(v_i,v_j)^p)\). Positivity gives monotonicity of \(D_j\), making the differences \(D_j-D_{j-1}\) admissible \(p\)-th power Cho parameters. The recurrence bounds all pair intervals from below and gives a telescope with total exactly \(D_n\). The converse is certified by summing disjoint intervals along each subsequence. Separate arguments cover \(p=\infty\), infinite weights, degree zero, and the infinite filtration scale. Finite tests corroborate rather than replace this general proof.

The direct countercheck to the published four-vertex example is completely explicit: \(D=(0,1,10,16)\) yields \((r_1,r_2,r_3)=(1,3,\sqrt6)\) at radius four, satisfying every displayed pair inequality. The exclusion argument on page 15 of the journal PDF uses the incorrect direction of the inequality for the \((0,2)\) pair.

## Originality (PASS, with specific proximity risk)

Cho's 2019 preprint supplies the nerve and all-graph definitions, but not the directed equality with monoidal Rips. Ivanov–Xu's 2024 Proposition 2.6 proves the comparison on **metric spaces**, and its inductive certificate construction is mathematically very close; the proof seems extensible without metric axioms. Accordingly no novelty is claimed for the metric-space case or the general idea of inductively building certificates. Blaser–Brun–Gardaa–Salbu's 2025 preprint and 2026 publication make the opposite assertion for directed graphs, even giving an alleged explicit counterexample. The proposed contribution is the correction of that assertion together with a precise all-directed-network theorem, closed-form optimal certificates and a quadratic-time algorithm. The inspected primary sources do not state this combination. Published research-record searches for the names, equivalences, source example, and longest-path certificates identified no covering statement. A mathematically equivalent unindexed exposition, or a recognition that Ivanov–Xu's proof implicitly establishes the extension, remains a genuine external novelty risk.

## Value (PASS)

A purported failure of equivalence between two natural persistent simplicial constructions is central to how directed-network filtrations are compared. Establishing equality across all \(\ell_p\) monoids corrects an explicit published separation claim and rules out such a separation in a broad, non-metric setting. The \(O(n^2)\) optimal-certificate formula also replaces existential interval parameters and an exponential subsequence maximum with a constructive algorithm, meaningful for simplex membership and implementation. This goes beyond observing a wrong sign in a single inequality: the universal theorem proves the exact structural boundary for the whole \(\ell_p\) family. No statement is made about arbitrary lattice-valued monoids.

## Sources and residual risk

Relevant full text was consulted for Cho, arXiv:1910.02905 (Proposition 13 and graph setup); Ivanov–Xu, arXiv:2411.01857 / DOI 10.1007/s41468-026-00247-x (Proposition 2.6 and proof); and Blaser–Brun–Gardaa–Salbu, arXiv:2503.14019 / DOI 10.1007/s41468-026-00237-z (Definition 3.1 and Examples 3.5–3.6, including the published graph and inequalities). Independent review should examine precisely the comparison with the inductive metric argument of Ivanov–Xu. The theorem has no independent validation yet; the 1,510-case tests are limited checks and do not certify all dimensions or edge weights.

Self-review: passed. Independent audit: not yet performed.
