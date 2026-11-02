# Scientific review

## Correctness — PASS

The labelled token graph has exactly three vertex types: the distinguished pair, the \(2n\) cross pairs, and the \(\binom n2\) within-large-part pairs. The proof explicitly reconstructs every adjacency. The three column states and the selected-within-part edge set give necessary **and sufficient** domination conditions. The hub-selected count is a product calculation; the hub-omitted count is an incidence-degree inclusion-exclusion with distinct formulas when the forced clique has at least two vertices and when it has at most one. All summations are finite for each integer \(n\ge2\); no normalized probability is involved.

For minima, the hub-selected lower bound is \(n+\frac{(t-1)(t-2)}2\) and equality has \(t=1\) or \(2\). The hub-omitted proof uses \(|D|=n-t+u+e\), the forced clique, and the degree requirement to prove \(|D|\ge n\), then exhausts the four possibilities \(t=0,1,2,3\). It counts \(4,15,24,0\) hub-free optima as \(n=2,3,4,\ge5\). Exact direct-adjacency enumeration of all \(2{,}131{,}008\) subsets for \(n=2,3,4,5\) matches every coefficient and the hub/no-hub split; the standalone verifier also checks the symbolic formula for \(n=6\) through \(11\). These finite checks support but do not replace the proof for arbitrary \(n\). No correctness caveat is disguised as a claim of certification.

## Originality — PASS, with priority qualifications

The two October 2026 preprints by Chinman et al. and Acosta Troncoso et al. prove the ordinary domination number \(n\) for \(F_2(K_{2,n})\); this fact is explicitly credited. The latter's Lemma 2.2 also gives a powerful general characterization of all dominating sets of \(F_2(K_{m,n})\). That structural result substantially anticipates the feasibility conditions, but neither inspected preprint states an ordinary domination polynomial, the minimum-set multiplicity formula, or the hub-exclusion cutoff. The novel asserted content is the explicit complete enumerator, its sharp optimum-layer count, and threshold, not the base feasibility lemma or minimum cardinality. The 2019 double-vertex-graph paper and the 2025 star/complete-graph token paper cover other statements. A previous total-domination polynomial of the same token-graph family and an independent-domination enumerator do not count the same objects. Search comparisons against exact aliases and published research records found no equivalent formula; this is evidence of non-identification, not proof of unique historical priority. A broader earlier enumeration could still imply the claim.

## Mathematical value — PASS

The recently determined domination number leaves the multiplicity and cardinality distribution of all dominating sets unresolved. The proposed formula determines the full polynomial of a natural infinite family and the precise sizes of its two structurally distinct classes; it is not a check on a single small instance. The sharp \(n=5\) cutoff, beyond which every optimal solution must include the distinguished pair, and the closed count \(n(n+3)2^{n-3}\) give interpretable information about the family of minimum certificates. The need to account for forced within-part cliques and incident-edge constraints motivates the inclusion-exclusion construction. These are exact natural invariants and a qualitative structural transition, not a renaming of the domination number.

## Closest literature and limitations

Chinman et al., arXiv:2610.28936v1 (2026-10-20), Theorem 1.1; Acosta Troncoso et al., arXiv:2610.31557v1 (2026-10-22), Theorem 1.1 and Lemma 2.2; Prabhu and Manjula (2019), *Domination in Double Vertex Graphs*; and Fabila-Monroy and Gómez-Galicia, arXiv:2509.16448v1 (2025), were inspected to the extent documented in the structured audit. A related exact total-domination enumerator on \(F_2(K_{m,n})\) concerns open neighbourhoods and does not count ordinary dominating sets. The statement does not concern \(m>2\), larger token size, arbitrary minimal-set counts, or symmetry orbits. Comprehensive historical-priority evaluation and an independent mathematical audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
