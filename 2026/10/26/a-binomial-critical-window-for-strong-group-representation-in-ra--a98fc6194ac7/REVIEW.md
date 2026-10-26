# Scientific review

## Correctness — PASS
The candidate-based one-cohesive score definition was verified against Definitions 2--8 of arXiv:2609.29332v1, including the distinction between a common elected representative (SJR) and coverage by possibly different elected representatives (SSJR). Independent approval columns make the number of cohesive candidates exactly binomial. The union bound quantifies a simultaneously valid witness event over all unelected candidates and committees; on that event every committee's two scores equal its fraction of selected cohesive candidates. This proves the score law, feasibility sandwich, and the triangular-array normal critical window with the correct lattice boundary. The limiting expected score and feasibility fraction at \(m=8,k=3\) are exact rational evaluations. Exact exhaustive arithmetic checks cover five small domains, without using finite enumeration as a substitute for the general proof.

## Originality — PASS (qualified)
The originating paper establishes worst-case complexity and reports empirical SJR/SSJR feasibility but no independent-Bernoulli probability or optimal-score limit in its examined main text and appendices. The closest probabilistic theorem, Han et al. (arXiv:2510.18718), is about average justified representation and cannot imply the distinct one-cohesive full-coverage laws. Comparisons by claim implication, candidate-coverage aliases, and accessible mathematical-results records did not identify direct coverage. A negative search is not proof of historical priority; undiscovered equivalent random-set-cover calculations remain a residual risk.

## Value — PASS
The finite-sample simultaneous reduction and its critical-window law answer how often recently formalized strong group-diversity guarantees are even feasible, what their best normalized score can achieve when not feasible, and when selecting cohesive candidates is exactly optimal. This gives an analytically calibrated null model for empirical SJR/SSJR performance, explains why the two axioms become asymptotically indistinguishable under independent approvals while differing sharply on structured datasets, and identifies the nontrivial boundary \(p=1/k\) alongside the singular unanimous endpoint. This is more than checking a local inequality or computing an arbitrary small instance.

## Closest literature and remaining limitations
Chingoma et al. (2026), arXiv:2609.29332v1, §§2--4, 8.1 and appendices; Han et al. (2025), arXiv:2510.18718v1, §§1--2. The quantitative error may be loose for small electorates. Fully correlated voter/candidate approvals, stronger all-\(\ell\) axioms, and the near-unanimity double-scaling regime are outside the theorem. The empty-cohesion score uses an explicit vacuity convention not defined by the source quotient. Priority is subject to further independent checking.

Self-review: passed. Independent audit: not yet performed.
