# Scientific review: super-domination polynomial of heterogeneous pendant coronas

## Correctness — PASS
The witness definition is equivalent to the local classification: an omitted root must retain all its private leaves; each root supports at most one omitted private leaf; and an omitted leaf is permitted only where no adjacent root is omitted. An omitted root is then witnessed by one of its selected leaves, whereas a permissible omitted leaf is witnessed by its selected root. These mutually inverse constructions establish the exact weighted polynomial for every finite simple base and positive pendant multiplicities. The constant-term and two-omission coefficient arguments follow directly from this bijection. The supplied independent brute-force enumerator passed all 1,150 tested cases (2,435,884 candidate subsets). The infinite statement is proved, not extrapolated from these checks.

## Originality — PASS, with a specific residual risk
Theorem 18 of Klein–Rodríguez-Velázquez–Yi (arXiv:1705.00928) gives the minimum super-domination number of ordinary coronas, not the full polynomial; recovering the scalar minimum here does not claim novelty. Ghanbari–Jäger–Lehtilä (arXiv:2209.01795) study neighborhood coronas and selected minimum-set enumerations, not this ordinary pendant-corona distribution. Kaidash's 2023 conference contribution (Vologda proceedings, pp. 31–33) introduces the polynomial and describes complete graph, star, complete-bipartite, and universal-vertex formulas, which do not cover the stated transformation. Searches for aliases, corona products, private-neighbor enumerators, and related result records did not identify the claimed complete weighted formula. Kaidash's later chapter (DOI 10.1007/978-3-031-73365-9_6) names unspecified graph families in its abstract; no full-text comparison was possible, so unrecognized implicit coverage is a nonzero residual risk.

## Value — PASS
The full distribution for *every* base graph and heterogeneous pendant bundle provides information absent from the known scalar corona formula. The closed multiplicity of minimum sets detects a factorization by connected components, and a high-degree coefficient measures the base graph's weighted edge count, specializing to actual edge reconstruction for uniform bundles. These are natural all-cardinality and structural invariants, not selected small examples or a normalization adjustment.

## Limits and source comparisons
No claim is made for non-pendant attachments, zero-sized bundles, polynomial-time general computation, universal priority, or independent verification. The 2017 scalar result and the 2023 introduction of the polynomial are credited; the later inaccessible chapter is a substantive but nondecisive originality risk. Literature and existing published research records can establish coverage, but a negative search never proves absolute novelty.

Self-review: passed. Independent audit: not yet performed.
