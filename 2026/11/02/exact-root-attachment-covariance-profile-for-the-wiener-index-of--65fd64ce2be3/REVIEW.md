# Scientific review

## Correctness — PASS

The exact local formula follows from the conditional Wiener-growth recurrence, the independence of earlier and later parent choices from a fixed arrival indicator, and the explicit expectations of the Wiener index and total root path length. The factor \(n(n+1)/(j(j+1))\) is a telescoping product, and the strict sign follows from the increasing harmonic ratio \(\frac{j+1}{j-1}H_{j-1}\) starting at \(3\). Both the finite-sum identity and limiting coefficient are derived directly in `RESULT.md`. Exhaustive independent computation for all \(5913\) recursive trees through size \(8\) corroborates all \(28\) local cases; rational sum identities were checked through size \(150\). Finite checking is not offered as a proof for all sizes.

## Originality — PASS (qualified)

Neininger's full author manuscript (2001) treats the Wiener index jointly with **internal/root path length**, not the root outdegree; its exact expectation is prior art and is used here. Grübel and Michailow (2014), inspected through the introduction and Sections 3.1 and 3.3–3.4, establish path-length/Wiener limit results but do not state the root-attachment influence or its exact sign threshold. A published result on root attachments and **total root path length** is mathematically distinct: that statistic sums root distances, whereas Wiener index sums distances over all pairs. Neither mixed covariance determines the other. Searches by the present statistics, harmonic-square formulas, and equivalent attachment/degree wording did not identify a stronger prior covering statement. This is a best-knowledge priority assessment, not proof of uniqueness. Residual risks include older tree-index literature and potential unstated corollaries of general joint enumerations.

## Mathematical value — PASS

Root degree measures local attachment concentration; the Wiener index measures global pairwise-distance spread. The theorem determines the entire arrival-resolved dependence profile rather than only a mean or one numerical value. The exact neutrality of arrivals \(2\) and \(3\), the strict negativity at every subsequent arrival for all final sizes, and the nonzero quadratic limiting constant give a structural and all-size answer. The result is not just a substitution into a published path-length covariance because Wiener distances include pairwise subtree interactions.

## Scientific limits and sources

The claim concerns the uniform increasing-label recursive-tree model; zero covariance does not assert independence, and finite tests do not establish infinite-size validity. Priority risk remains after comparison with Neininger's author PDF (https://www.math.uni-frankfurt.de/~neiningr/w-ind.pdf), Grübel–Michailow's full arXiv text (https://arxiv.org/abs/1406.7614), and the abstract of Munsonius' tail-bound paper (doi:10.1239/jap/1339878805). No external independent mathematical validation has been conducted.

Self-review: passed. Independent audit: not yet performed.
