# Review of the exact subdivision independent-domination spectrum

## Correctness — PASS

There is a bijection from maximal independent vertex sets of a complete edge subdivision to original-vertex subsets with no isolated vertices in the induced graph, allowing the empty subset separately. Both implications are explicitly checked: subdivided edge vertices are forced precisely when both original endpoints are omitted, and omitted original vertices are dominated precisely when they have an omitted original neighbor. The exponent weights follow without extra choices. In bicliques these induced graphs are complete bicliques with both shores occupied, proving the full polynomial and exact shifted multiplication-table support. Finite direct tests confirm the identities in 10 bicliques and 31 general graphs. The number-theoretic sparsity bound is an application of Ford's cited established result; no finite extrapolation is used as proof.

## Originality — PASS with residual uncertainty

The independent domination polynomial is prior terminology due to Jahari and Alikhani (arXiv:1808.07369), but their inspected graph-product results concern joins and lexicographic products, not full edge subdivisions. Babikir and coauthors (DOI 10.1007/s00373-020-02269-3) study the minimum number of edges whose subdivision raises the scalar independent-domination number, not the complete maximal-independent-set distribution after subdividing every edge. A preceding ordinary-domination result for full subdivisions already establishes the minimum degree and count for bicliques; those scalar facts are explicitly treated as prior, not as original contributions. The complete independent-domination polynomial and its multiplication-table cardinality spectrum are stronger information and are not implied by merely knowing the unfiltered ordinary-domination polynomial. Ford's multiplication-table asymptotic is also known and is credited. Targeted searches identified no equivalent all-degree formula, though literature omission remains possible.

## Value — PASS

This classification supplies an exact polynomial for all biclique shore sizes, a general graph-subdivision transform, and an unexpected precise bridge from cardinalities of maximal independent vertex sets to the distinct products in integer multiplication tables. It proves the existence of arbitrarily long forbidden cardinality intervals and the asymptotic sparsity of attainable cardinalities in the balanced family, which are substantive structural refinements beyond minimum-set counts.

## Closest literature and limitations

The relevant primary references are Jahari–Alikhani (2018), Babikir–Dettlaff–Henning–Lemańska (2021), and Ford (2008). A prior complete ordinary-domination enumeration of full subdivisions already counts minimum sets, and a different prior enumeration concerns maximal induced matchings in subdivided bicliques: neither gives this independent-domination polynomial. Publication priority has not been independently confirmed against every potentially unindexed source. The executable tests cover only stated finite graph orders; the general proof is self-contained except for Ford's quoted asymptotic.

Self-review: passed. Independent audit: not yet performed.
