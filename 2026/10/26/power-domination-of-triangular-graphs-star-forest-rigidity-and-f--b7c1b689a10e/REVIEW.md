# Scientific review: power domination of triangular graphs

## Correctness — PASS

The proof defines vertices of \(\operatorname{Tri}(n)=L(K_n)\) as original edges and identifies the exact unobserved set after the domination step with the edges of \(K_U\), where \(U\) is the set of isolated endpoints of the selected edges. At \(|U|\ge3\), an observed edge has either zero or at least two unobserved neighbors and therefore cannot force. At \(|U|=2\), there is exactly one unobserved edge and an observed adjacent edge forces it; at \(|U|\le1\), domination is already complete. The iff criterion is therefore fully proved for every integer \(n\ge3\).

Inclusion–exclusion over original isolated vertices proves all coefficients of the power-domination polynomial. The degree-one endpoint test upon deleting a selected edge proves the exhaustive minimal-set classification into matchings and star forests. Labeled matching and two-edge-path enumeration proves both parities of the minimum coefficient, and the exponential formula counts every minimal set. The maximal-obstruction characterization is checked by considering all possible isolated-vertex counts.

The standalone direct-definition verifier covered 2,131,016 vertex subsets for \(3\le n\le7\), and separate exact coefficient arithmetic covered \(3\le n\le14\). The infinite-domain proof is not inferred from that enumeration.

## Originality — PASS, with residual bibliographic uncertainty

The directly relevant foundational paper, Brimkov–Patel–Suriyanarayana–Teich (arXiv:1805.10984v1), defines power-domination polynomials and enumerates several graph families, including numerical data for graphs with fewer than ten vertices. Its relevant full-text sections do not furnish the general polynomial or star-forest characterization for \(L(K_n)\); the small \(n=3,4\) instances are not claimed separately.

Lu–Mao–Wang (arXiv:1808.02613v1) establish a four-regular claw-free power-domination bound. Since \(L(K_n)\) has degree \(2(n-2)\), it covers only the \(n=4\) special case, not the entire family or its minimal-set distribution. Anitha–Rajasingh's 2019 "triangle graph" is instead a hexagon-based planar lattice network, confirmed from the authors' definitions and figure. The more recent power-domination reconfiguration work addresses general minimum-set reconfiguration and does not give these formulas. Targeted searches of the relevant published research collection did not identify a statement dominating the full theorem.

Not every obscure or unindexed paper can be ruled out, and generic matching or edge-cover formulas do not themselves certify bibliographic priority.

## Value — PASS

This is a complete classification of *all* feasible power-monitoring placements of a natural, highly symmetric infinite graph family—not merely the ordinary minimum number. The one-step-or-stalled dichotomy is a structural boundary; the star-forest decomposition classifies *all* inclusion-minimal sensor placements and provides a full size generating function. The sharp gap \(\overline\gamma_P-\gamma_P\) is unbounded, and maximal failing placements are exactly counted. These give concrete tools for robustness, choice among minimal placements, and finite enumerations that are not implied by knowing the domination number or a generic graph-polynomial definition.

## Limits

The result does not treat arbitrary line graphs or higher Johnson graphs. The \(n=3,4\) polynomial instances may occur in existing small-graph tables, and independent bibliographic and mathematical assessments remain outstanding.

Self-review: passed. Independent audit: not yet performed.
