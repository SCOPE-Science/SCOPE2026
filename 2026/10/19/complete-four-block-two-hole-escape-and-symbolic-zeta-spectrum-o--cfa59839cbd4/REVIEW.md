# Self-review

## Correctness — PASS

The finite-time survival probability is exactly \(2^{-(n+3)}\mathbf1^{\mathsf T}A_B^n\mathbf1\), with \(A_B\) the eight-state de Bruijn adjacency matrix after deleting two four-digit transitions. Its exponential rate is \(\log(2/r_B)\); the symbolic zeta is \(1/\det(I-zA_B)\). All \(120\) possible holes are exhausted by exact integer characteristic polynomials and rational Sturm root isolation. The verifier passed all \(120\) classifications and \(960\) independent integer finite-time comparisons. Spectral theory, not experiments, proves the infinite-time limit. Symbolic periodic itineraries are distinguished from ambiguous binary endpoint orbits.

## Originality — PASS, subject to priority uncertainty

The closest primary works are Ramsey (arXiv:1902.03352, 2019) and Cheriyath–Agarwal (arXiv:1905.11767, first 2019; revised 2022). Both supply general correlation-polynomial methods; they do not state the full binary four-block \(120\)-pair classification, its \(16\) escape classes/26 symbolic zetas, or its two and eight exact extremizer lists. General formulas can compute any given case, so overlap with unlocated specialized tables remains a meaningful limitation. Nearby results on other hole geometries or random/negative-doubling maps do not imply this complete table.

## Mathematical value — PASS

Two equal-size Markov holes have different escape rates depending on symbolic overlap. The binary four-block census provides a natural exact test case where large-alphabet comparison theorems do not apply directly; it determines all outcomes and reveals that the maximum survival exponent can hide different periodic-itinerary zeta functions. The result does not claim a general all-length classification.

## Limitations and references

Scope is exactly two simultaneous length-four binary cylinders, with fair Bernoulli/Lebesgue measure. Exact symbolic zeta counts may differ from geometric doubling-map periodic-point counts at dyadic boundary identifications. Literature: https://arxiv.org/html/1902.03352v1 and https://arxiv.org/html/1905.11767v5. Priority outside inspected material is not certified.

Self-review: passed. Independent audit: not yet performed.
