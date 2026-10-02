# Independent audit — 2026-10-01

## Final claim

For every simple three-path theta graph \(\Theta(a,b,c)\), the ordinary two-distance chromatic number is exactly 4, 5 or 6 according to the stated complete list of length patterns.

## Correctness — PASS

The 12-state four-color path transfer is exact: each step forbids precisely the previous two colors, and the reachable-state counts saturate at all 12 ordered unequal states by path length 7. The endpoint closed neighborhoods are \(K_4\)'s in the square, so the case split reduces to finite endpoint-state compatibility. The exceptional \(\Theta(2,2,3)\) has six vertices and diameter two, hence square \(K_6\); the remaining obstructions have explicit five-color witnesses or use five-color state saturation, which independently reaches all 20 ordered unequal states at length 5. I independently computed exact square chromatic numbers for all 77 triples with \(1\le a\le b\le c\le7\), \(b\ge2\), with no mismatch. The repository verifier extends this to all 210 triples through length 10. The finite replay supports, but does not replace, the general transfer proof.

Checked sources:
- V. Suvagiya, Two-distance and list-two-distance coloring of cacti, arXiv:2609.20204 (2026)
- K.-W. Lih, W.-F. Wang, X. Zhu, Coloring the square of a K4-minor free graph, Discrete Mathematics 269 (2003)
- T. J. Hetherington, D. R. Woodall, List-colouring the square of a K4-minor-free graph, Discrete Mathematics 308 (2008)
- Assigned theta-square verifier and an independent exact coloring replay for all 77 triples with lengths at most 7
- Resultary semantic searches for theta/generalized-theta square coloring and K2,3 subdivisions

Residual risks:
- The theorem is for ordinary square coloring, not list square coloring, and exactly three internally disjoint paths.

## Originality — PASS

Best-of-knowledge originality passes for the complete three-parameter classification. Suvagiya's recent theorem is for cacti, while theta graphs are the first 2-connected non-cactus series-parallel blocks. The 2003 and 2008 papers provide sharp general \(K_4\)-minor-free square/list-square bounds, but accessible abstracts do not supply the exact length-by-length theta classification. Because the most plausible older primary full text could not be obtained after a lawful retrieval attempt, that access risk is stated explicitly; no whole-document noncoverage conclusion is drawn from snippets.

### Equivalent formulations

Searches:
- Resultary query: theta graph square coloring exact chromatic number three paths
- Resultary query: K4 minor free graph square coloring theta subdivision K2,3 chromatic

Evidence:
- The assigned record was the only exact theta-square classification hit; no earlier published SCOPE record with the same invariant and family appeared.

Reasoning: Equivalent descriptions include two-distance coloring of a three-path theta, square coloring of a subdivision of \(K_{2,3}\), and endpoint-state transfer classification. None was found as a prior exact classification.

### Broader coverage

Searches:
- Suvagiya arXiv:2609.20204 abstract
- Lih--Wang--Zhu 2003 abstract
- Hetherington--Woodall 2008 abstract

Evidence:
- Suvagiya treats cacti; the older papers treat all \(K_4\)-minor-free graphs only through general sharp upper bounds.

Reasoning: A general upper bound such as \(\chi(G^2)\le6\) for subcubic \(K_4\)-minor-free graphs does not imply which theta length triples have chromatic number 4, 5, or 6.

### Exact database or table

Searches:
- Resultary exact theta-square searches
- Independent exact enumeration through length 7 and repository enumeration through length 10

Evidence:
- No prior parameter table was located; the audited finite tables agree with the theorem on the checked ranges.

Reasoning: The computation is evidence for correctness, not novelty; search absence is not treated as proof.

### Claim versus prior implication

Searches:
- Lih--Wang--Zhu 2003 general bound
- Hetherington--Woodall 2008 list bound
- Suvagiya cactus classification

Evidence:
- The older results bound all relevant graphs but do not, in accessible material, determine the exact theta spectrum; the cactus theorem excludes theta blocks by hypothesis.

Reasoning: The complete obstruction families and transfer characterization are not mechanical corollaries of those upper bounds. The inaccessible 2003 full text remains a genuine but non-decisive risk.

### Source inspections

- **Coloring the square of a K4-minor free graph** (https://doi.org/10.1016/S0012-365X(03)00059-1): trigger — Broader graph class and sharp subcubic square-coloring bound; material read — Abstract and bibliographic material; full text was not available during this audit after lawful access attempts; method — Primary-source abstract inspection; full-text access unavailable; assessment — Highly relevant residual risk. Accessible material supports only the general sharp bound, not the full theta classification.; evidence — The abstract states the general bound and that sharpness examples exist.
- **Two-distance and list-two-distance coloring of cacti: the subcubic case and the C5 obstruction** (https://arxiv.org/abs/2609.20204): trigger — Immediate motivating exact classification in the neighboring cactus class; material read — Primary abstract and bibliographic record; method — Primary-source abstract inspection; assessment — Not covering: theta graphs with three internally disjoint paths are non-cactus 2-connected blocks.; evidence — The source classification is expressly for cacti.

Checked sources:
- V. Suvagiya, Two-distance and list-two-distance coloring of cacti, arXiv:2609.20204 (2026)
- K.-W. Lih, W.-F. Wang, X. Zhu, Coloring the square of a K4-minor free graph, Discrete Mathematics 269 (2003)
- T. J. Hetherington, D. R. Woodall, List-colouring the square of a K4-minor-free graph, Discrete Mathematics 308 (2008)
- Assigned theta-square verifier and an independent exact coloring replay for all 77 triples with lengths at most 7
- Resultary semantic searches for theta/generalized-theta square coloring and K2,3 subdivisions

Residual risks:
- The full 2003 Lih--Wang--Zhu paper was not available during this audit after lawful access attempts. Its abstract says sharpness examples are given, so isolated theta examples may occur there.
- The full 2008 Hetherington--Woodall paper was not inspected; its general list-square bound is broader in graph class but does not, from accessible material, supply the exact theta length classification.

## Scientific value — PASS

Three-path theta graphs are the minimal 2-connected step beyond cacti inside series-parallel graphs. An exact 4/5/6 phase diagram, including infinite obstruction families and a reusable finite-state transfer method, is a natural classification likely to be useful in extending two-distance coloring beyond cactus blocks.

Checked sources:
- V. Suvagiya, Two-distance and list-two-distance coloring of cacti, arXiv:2609.20204 (2026)
- K.-W. Lih, W.-F. Wang, X. Zhu, Coloring the square of a K4-minor free graph, Discrete Mathematics 269 (2003)
- T. J. Hetherington, D. R. Woodall, List-colouring the square of a K4-minor-free graph, Discrete Mathematics 308 (2008)
- Assigned theta-square verifier and an independent exact coloring replay for all 77 triples with lengths at most 7
- Resultary semantic searches for theta/generalized-theta square coloring and K2,3 subdivisions

Residual risks:
- The full 2003 Lih--Wang--Zhu paper was not available during this audit after lawful access attempts. Its abstract says sharpness examples are given, so isolated theta examples may occur there.
- The full 2008 Hetherington--Woodall paper was not inspected; its general list-square bound is broader in graph class but does not, from accessible material, supply the exact theta length classification.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
