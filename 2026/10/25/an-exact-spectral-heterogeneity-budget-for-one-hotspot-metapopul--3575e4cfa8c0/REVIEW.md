# Self-review

**Finding under assessment:** an exact, spectral-energy invasion threshold for the one-hotspot SIR-network model under arbitrary symmetric stochastic travel, plus an exact fixed-hub-column pair with opposing invasion classifications.

## Correctness — PASS

The infection matrix follows from the equal-population symmetric-flux SIR model. The decomposition into a background matrix square plus a positive rank-one hotspot term is exact. Since the background reproduction parameter is below one, a positive-definite rank-one congruence gives an if-and-only-if invasion test, including strict and boundary cases. Spectral decomposition makes the scalar heterogeneity budget exact and basis independent. The full analytic proof covers all finite patch numbers and all nonnegative symmetric stochastic fluxes. In the five-patch pair, every matrix entry and all matrix inverses are rational; the reproducible verifier checks the full constructed fluxes, exact budgets, exact determinant signs, and uniform-hub consistency identities. No inference from finite enumeration is used in the general theorem.

## Originality — PASS, with priority risks

Das and Stolerman (arXiv:2308.01998, 2023; DOI:10.1137/23M1579522, 2024) give the SIR-network threshold problem and analyze classes with equal flux into the hotspot. Their four conjectures, star variants and previous fully connected results do not address the fixed **nonuniform** hub column examined here. The 2019 equitable-quotient theorem is a decisive broader source for the uniform-hub quotient reduction, so this reduction is excluded from the novel claim; its accessible abstract and limitations are recorded. Classical rank-one spectral tests are also acknowledged as tools. The accepted novelty is the complete **non-equitable** spectral risk budget, including the two precise five-patch systems with identical hotspot column and opposite outcomes. Related layered-mobility papers have different mechanisms. Searches of primary literature and relevant prior results did not show this model-specific statement or pair. The complete 2019 full text and an exhaustive later-priority survey remain outstanding scientific risks, not proof of uniqueness.

## Value — PASS

The classification distinguishes two epidemiologically natural mechanisms that hotspot-traffic summaries conflate: individual journeys involving the hotspot and mixing among the remaining neighborhoods. It proves that even the entire hotspot column and its variance can fail to predict invasion, while the weighted spectral energy gives a necessary-and-sufficient all-size test. This closes a motivated parameter-interpretation gap in the source SIR-network model, rather than a textbook substitute for a known instance. The elementary linear algebra used in the proof is not claimed novel.

## Scope and limitations

Only local disease-free invasion is addressed. Assumptions include equal populations, symmetric row-stochastic mobility, common recovery, strictly subcritical background transmission, and exactly one elevated infection rate. The result does not establish whole-epidemic size, persistence, or heterogeneous/directed travel claims. Publication priority and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
