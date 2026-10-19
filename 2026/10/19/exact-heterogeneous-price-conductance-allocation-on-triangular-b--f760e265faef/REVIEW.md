# Scientific review of priced triangular-bouquet resistance allocation

## Correctness — PASS

The theorem specifies all variable conductances, prices, budget and connectivity conventions. The effective-resistance identities for each weighted triangle and the articulation-point decomposition yield equation (1), independently confirmed through full weighted-Laplacian inverses. Trace-inverse strict convexity on connected Laplacians, together with injectivity of edge coordinates, justifies unrestricted uniqueness and the consequent spoke symmetry. Equation (2) determines a unique petal-ratio minimum, including the boundary. Cauchy–Schwarz then proves the global expenditure allocation and the stated exact value. The complete argument applies for every integer \(m\ge2\), each \(t_i>0\), and \(B>0\). The standalone verification script passed 549 symbolic, exact-rational, and numerical assertions; its finite tests are supplemental, not an infinite proof.

## Originality — PASS, with identified risks

The closest general treatment is Ghosh–Boyd–Saberi (2006/2008), whose full text develops the weighted-Laplacian convex framework and solves trees, wheels and barbells, but does not give heterogeneous triangular-bouquet mixed-phase conductances or their square-root budget coupling. Sardar–Xu (online 2024; journal 2025) evaluates resistance of unit-weight windmills; the accessible abstract explicitly assumes a one-ohm resistor on every edge. Its complete article was not available for inspection. Bhoite and coauthors (2026) investigate a distinct mixed-integer edge-augmentation model and numerical optimization rather than this closed-form unrestricted fixed-support theorem.

The high-price *deletion threshold alone* also follows from general tree-with-optional-chord optimality conditions and is therefore not claimed independently as original. The non-implicated contribution is the complete unique optimizer in every mixed-price regime, the exact radical value for arbitrary independent prices, and the cross-petal expenditure law. Bibliographic searches did not locate a dominating closed-form result, but unindexed specialization remains possible.

## Value — PASS

A triangular bouquet is the simplest multi-cycle network with an articulation hub, so its independently priced petals model heterogeneous small redundant clusters in a common infrastructure. For all \(m\) petals the theorem resolves the entire optimal weight-allocation problem, not just a first-order deletion test. Its particularly useful conclusions are that each cycle's retention decision is independent of other prices and budget, while the *amount* of budget allocated to that petal is globally coupled by an exact square-root rule. This makes a natural complete family of design choices analytically tractable, including all equality-price boundaries and all \(2^m\) support configurations.

## Scope of this review

No claim is made for arbitrary cactus graphs, unequal prices for the two spokes of an individual triangle, or independently established novelty. Any equivalent specialized theorem in sources not available for full inspection would affect the originality assessment. All numerical assertions concern only checked finite inputs.

Self-review: passed. Independent audit: not yet performed.
