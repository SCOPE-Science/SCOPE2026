# Scientific review

## Correctness — PASS
The active facets of a rooted-tree order polytope are explicitly listed using Stanley's inequalities. The primitive normal map is the reduced coboundary map of the connected active-facet graph, so its cokernel is integral \(H^1\), free with the asserted cycle rank. The frontier decomposition yields the formula even at the empty and full filters. Root-exclusion gives the polynomial recurrence; unary terminal chains give the smooth-point product. The binary-tree asymptotic follows from a proved inequality. The standard-library checker independently constructs facets and unimodular spanning minors for all 17,471 filters in the finite test census. All infinite assertions are proved symbolically, not inferred from these tests.

## Originality — PASS, with qualifications
Stanley (1986) supplies the facets and fixed-point vertices; Wagner (1996, Theorem 2.3) supplies a general smoothness criterion; Lakshmibai–Mukherjee (2007) give a singular-locus theorem; Friedl (2015, Theorem 8 and Lemma 12) supplies global divisor groups and local Cartier tests. None of their inspected relevant theorem statements gives the uniform pointwise rooted-tree rank distribution \(R_T(q)\), the leaf-tail count, or the complete-binary asymptotic. A general cohomological presentation is close to Friedl's graph methods, so the originality assessment rests on the explicit family classification and enumeration, not on standard toric facts. An equivalent unindexed derivation remains a risk.

## Value — PASS
The exact local class-group ranks across every fixed point, including their integral torsion behavior, separate smooth and non-\(\mathbb Q\)-factorial strata in a natural poset-toric family. The recursive polynomial records the **complete distribution**, while the leaf-tail product and binary-tree decay characterize geometric variation that total vertex counts and global divisor-class groups do not measure. This is a structural family computation, not a claim of a new general divisor theory.

## Limitations and closest sources
The theorem does not address non-fixed point class groups or local analytic equations. The main risk is derivability from Wagner's tree-fiber criterion together with Friedl's local Cartier framework; the newly assessed content is the explicit tree-indexed arithmetic and enumeration. Primary sources examined: Stanley (1986), Wagner (1996), Lakshmibai–Mukherjee (2007), Friedl (2015).

Self-review: passed. Independent audit: not yet performed.
