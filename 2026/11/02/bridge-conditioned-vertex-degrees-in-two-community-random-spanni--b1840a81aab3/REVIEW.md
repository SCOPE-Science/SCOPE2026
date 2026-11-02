# Scientific review: bridge-conditioned degrees in two-community random spanning trees

## Correctness (C): PASS

The exact bivariate generating polynomial follows from a weighted Matrix–Tree Laplacian minor whose two invariant zero-sum subspaces and two-dimensional block-constant space are exhibited in the result. Cross-differentiation of the logarithm gives the covariance and its unique sign-switch threshold. Coefficient comparison at the first two cross-edge counts, followed by the all-cross-edge endpoint, proves that the conditional mean cannot be monotone for any unequal community sizes. The balanced conditional mean follows by transitive symmetry. Every weight and size boundary is stated. A standalone independent Prüfer enumeration and Laplacian determinant checker passed 250 exact assertions, including positive integer conductances and graphs up to seven vertices. The analytic proof, not those finite checks, handles every finite size.

## Originality (O): PASS, qualified

The 2024 work of Fita Sanmartín, Schnörr and Hamprecht already proves a general product-conductance spanning-tree model, a node-degree enumerator and formulas for degree moments/covariances; these are not new here. Rapoport (2023) gives general uniform-spanning-tree local-degree joint statistics and edge-event methods. Those papers were inspected in their available full HTML sections describing definitions, main claims and covariance arguments. Searches for two-block cross-edge/marked-degree bivariate polynomials, conditional bridge-count regression and conductance-reversal thresholds found no implication-equivalent explicit result. Existing general Matrix–Tree/transfer-current theory can be specialized to recover some formulas, so future inspection of older two-type Cayley-tree enumerations is a specific historical-priority risk. No novelty guarantee beyond these comparisons is made.

## Value (V): PASS

The two observables have a direct structural interpretation: a local hub degree and the count of links joining two network communities. Their conditional association has an unexpected all-order qualitative obstruction: the regression first moves opposite to its total endpoint displacement for every unequal pair of community sizes, even though the global covariance can switch sign with the conductance ratio. The exact joint polynomial makes the effect reproducible and permits complete finite-size distributions, rather than an isolated small counterexample. The balanced exception differentiates covariance zero from independence.

## Limits

The proof is confined to complete two-block networks with positive constant within/between edge conductances; no claim of a general multi-community or heterogeneous-weight theorem. Only nonmonotonicity, not a count of turning points, is established. Independent external audit and definitive priority assessment have not occurred.

Self-review: passed. Independent audit: not yet performed.
