# Scientific review: sharp one-point odd-order completion

**Correctness — PASS.** Each open path can be joined to exactly one successor path; every completion corresponds bijectively to a permutation of the path components. The completed cycle length is the sum of the component lengths and is odd exactly when it contains an odd number of odd components. This proves the parity reduction. The labeled exponential formula gives the square-root series and exact factorial coefficients. A fresh isolated point is a new odd component: it is necessary only when there are even components but no odd ones, and then yields precisely \(v!\) solutions. Existing even cycles cannot be repaired. Exhaustive checks cover 1,798 partial injections up to five points and 296 one-point cases, but the proof does not depend on these finite checks.

**Originality — PASS relative to inspected literature.** Etedadialiabadi and Gao's 2026 paper proves qualitative extension results for sets of partial permutations and cyclic-fundamental-group cases. The classical all-odd-cycle permutation formula is a recognized subcase and not separately claimed. Kim, Kim and Seo (2017) consider the different no-monochromatic-cycle constraint. No inspected source directly supplies the fixed-carrier parity-profile count together with the exact one-point enlargement bound. An uninspected general colored-cycle formula could nevertheless subsume the enumerator; the original 2017 article was checked at abstract level only.

**Value — PASS.** The theorem gives a sharp universal baseline for the one-generator odd-extension question, a single-vertex resource bound and the exact number of realizations. Dependence only on the parity counts of paths is a substantive invariant simplification, motivated by odd-order finite-group actions rather than an arbitrary enumeration slice.

**Scope and limits.** No claim about extension of multiple maps, tournament EPPA, or absolute priority. Main proof is combinatorial; checker supplies finite corroboration only.

Self-review: passed. Independent audit: not yet performed.
