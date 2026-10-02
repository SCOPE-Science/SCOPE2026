# Independent mathematical audit — SCOPE-20260919-6dd1f9692951

Final disposition: **PASS**.

## Correctness
**PASS** — Tang's full paper was inspected through Section 4.2. Fourier inversion shows that for a Hamming-distance-one pair all modes with j_c=0 cancel, and maximizing the real pole order forces every unchanged coordinate index to zero. For l_c=2 the unique dominant pole has order 1-2/m and positive Selberg-Delange constant, giving an eventual fixed sign. For l_c>=3 the dominant conjugate pair has nonzero amplitude and frequency sin(2pi/l_c)/m, giving infinitely many sign changes. In the explicit M=5, l=(3,2,1,1) example the surviving pole orders are 1/2 and 1/8 plus/minus i sqrt(3)/8, so the x/sqrt(log x) binary bias dominates.

## Originality
**PASS** — Tang's complete fourteen-page v1 explicitly conjectures in Section 4.2 that when some l_i>=3 the sign changes infinitely often for every distinct pair. The audited counterexample exploits cancellation of all modes on the unchanged high-modulus coordinate and contradicts that literal conjecture. Resultary searches found related all-binary strict-bias work but no earlier mixed-modulus correction or one-coordinate dichotomy. Porritt's scalar omega-mod-q races supply methodology, not this vector mixed-modulus statement.

### Equivalent formulations
The leading-mode formulation directly matches the source's Selberg-Delange framework.

### Broader coverage
No inspected broader theorem implies the mixed one-coordinate correction.

### Exact database or table
Negative search is supporting only; the primary source's explicit contrary conjecture establishes the novelty target.

### Claim versus prior implication
The final claim is not implied by the source; it disproves a source conjecture using its framework.

## Value
**PASS** — The result gives a rigorous counterexample to a concrete new universal conjecture and replaces the failed heuristic with a clean one-coordinate classification explaining exactly which modulus controls the leading race. This is a motivated structural correction with an explicit infinite family, not an arbitrary computation.

## Source inspections
- **Distribution of squarefree integers with double congruence conditions** (https://arxiv.org/abs/2609.16716): complete 14-page v1 via authorized full-text retrieval, including Sections 3, 4.1 and 4.2 Assessment: PRIMARY_SOURCE_CONJECTURE_REFUTED_BY_ASSIGNED_RESULT. Evidence: Page 13 states the conjecture that the sign changes infinitely often for all distinct a,a' in the regime treated in Section 4.2 where some l_i>=3.

## Residual risks
- Unindexed simultaneous corrections to the very recent Tang preprint remain possible.
- The theorem classifies only Hamming-distance-one comparisons; multiple changed coordinates can have leading-mode cancellation.
