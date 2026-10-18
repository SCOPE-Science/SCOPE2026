# Scientific review: pentagon stable-set toric fivefold

## Correctness
PASS. The polytope's eleven-inequality description is verified by exhaustive exact vertex solving and facet-rank checks. Its complete face lattice and normal cones are enumerated without random sampling, and each simplicial cone's integral index is tested. The ten maximal nonsmooth triangles are found exactly; their two-component-orbit formulas and plane orbit closures are independently checked. For the two symmetry representatives, the primitive ray relations, saturated lattice spans and unimodular triples prove the generic transverse conifold description. `CHECK.py` was executed from the package and returned `VERIFY_OK`. The proof uses standard toric orbit, smoothness, and divisor-class theorems, rather than treating the verification output alone as a proof of geometric assertions.

## Originality
PASS, qualified. The March 2016 source by Matsuda, Ohsugi, and Shibata has been inspected in its accessible full-text form, including the sections on ring-graph Gröbner bases, normality, and toric-ideal generators. It does not give the exact singular-component, conifold, or intersection classification for the pentagon stable-set normal fan. Engström and Norén's available abstract and bibliographic materials address graph-homomorphism toric ideals, not this local normal-fan theorem. Current semantic mathematical-index queries for this precise polytope, singular components, and aliases yielded nearby toric and graph-polytope results but no implication-equivalent classification. The highest residual risk is an unindexed face-by-face toric calculation under different terminology. This is evidence-based qualified originality, not a uniqueness guarantee.

## Mathematical value
PASS. The five-cycle is the minimal odd hole and a distinguished first nonperfect graph. Its stable-set polytope supplies a natural nontrivial toric fivefold. The complete singular stratification exhibits ten irreducible projective planes, two symmetry classes, uniform generic conifold singularities, and a nontrivial intersection pattern of five triple lines and five five-component fixed points. These exact local invariants are not consequences of the cited global normality or Gröbner-basis statements, and provide a concrete model for singularity and resolution questions on stable-set toric varieties. The result is restricted to this natural smallest case; no all-odd-cycle theorem is claimed.

## Closest literature and limits
- Matsuda–Ohsugi–Shibata, arXiv:1603.01850 (full-text sections inspected): global stable-set ring/ideal properties and ring-graph results; no corresponding singular fan list found.
- Engström–Norén, arXiv:1002.4679 (abstract and metadata inspected, not a full-text exclusion): graph-homomorphism ideals and Gröbner-basis context.
- Standard toric-geometry smoothness/class-group criteria are established background, not new assertions.

The possible existence of an unindexed equivalent explicit toric computation remains an originality limitation. The findings describe the reduced singular locus and generic transverse types; they do not classify intersection-point analytic germs or the singular scheme.

Self-review: passed. Independent audit: not yet performed.
