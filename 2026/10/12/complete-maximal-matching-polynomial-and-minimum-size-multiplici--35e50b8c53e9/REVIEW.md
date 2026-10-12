# Self-review of cycle-prism maximal matchings

## Correctness: PASS

The 25-state construction imposes exactly the matching and maximality conditions on each cyclic column, with each selected edge weighted once. Its trace enumerates labeled matchings without quotienting by cyclic automorphisms. The explicit characteristic determinant is verified by integer-polynomial Newton identities in the supplied, executable standalone verifier. Substituting \(t=s/y^2\), \(z=y^3\), and extracting its lowest three \(y\)-coefficients proves the asserted minimum size and all residue-class multiplicities for every \(n\ge3\). Independent direct enumeration checks all coefficients on labeled prisms of orders 3 through 12, but those finite checks are not used as an infinite proof. Boundary conventions explicitly exclude formal prism orders one and two.

## Originality: PASS (residual priority risk)

The complete, original-language primary text of Došlić--Zubac was compared in its definition and ladder sections: it defines the polynomial and treats an **open** ladder, not the claimed cycle-prism graded distribution. Hertz et al. also study the open ladder. OEIS A284703 **already gives the exact ungraded prism totals** and an order-eight recurrence, with the same scalar denominator obtained by setting \(z=1\) in the new determinant; that narrower claim is credited rather than presented as new. The full graded two-variable polynomial and the residue-class number of smallest maximal matchings are neither contained in, nor logically recovered from, these scalar totals or open-ladder results. Searches for circular/closed ladder, maximal independent edge set, saturated dimer, edge domination, maximal matching polynomial, and the exact minimum-layer patterns did not surface an equivalent theorem; absence from search alone does not prove priority. Relevant public mathematical result records returned generic maximal-matching inequalities, not the all-order prism enumeration. Remaining risk: an equivalent bivariate formula under another name, or unpublished work, could exist.

## Value: PASS

The prism is a natural finite periodic two-row lattice for saturated dimer adsorption. Its complete size distribution refines the already-known ungraded total into the probability-relevant cardinality strata, and the exact three-case multiplicity for smallest saturated matchings identifies the worst-case occupancy patterns. This is a complete all-order invariant and a structurally derived extremal classification, not an arbitrary finite sample or the routine restatement of the published ungraded recurrence.

## Closest literature and limits

Došlić--Zubac (2015 online), Proposition 5.2: open-ladder ungraded counting and general maximal-matching polynomial. OEIS A284703 (2017): exact **ungraded cyclic-prism** recurrence. Hertz et al. (2022), Section 5.4: average size on **open** ladders. The matchings are labeled and the graph family requires \(n\ge3\); mathematical independence and exhaustive historical priority have not been certified.

Self-review: passed. Independent audit: not yet performed.
