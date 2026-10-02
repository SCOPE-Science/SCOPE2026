# Independent mathematical audit — SCOPE-20260913-061

Audit date: 2026-10-01 (UTC) UTC

Disposition: **passed**

## Final claim assessed

For every integer \(3\leq \ell\leq 6\) and \(k\geq1\), the cone over the extended Shi arrangement of type \(B_\ell\) is not hereditarily free: an explicit rank-three restriction has characteristic polynomial \((t-1)(t^2-9kt+S(k))\), with negative quadratic discriminant for every \(k\geq1\); every central restriction of rank at most two is free.

## Correctness: PASS

The restriction was reconstructed directly. On the rank-three flat the deconed normal families have sizes \(2k,3k,2k,2k\), so the central restriction has \(9k+1\) hyperplanes. The intersection calculation gives the coefficient \(S(k)=41k^2/2\) for even \(k\) and \(S(k)=(41k^2+1)/2\) for odd \(k\). Hence the quadratic discriminant is \(-k^2\) or \(-(k^2+2)\), respectively, and Terao factorization excludes freeness. Extra coordinates for \(\ell>3\) restrict only to already present normals or the hyperplane at infinity. An independent exact-rational enumeration for \(k=1,\ldots,8\) reproduced \(S(k)=21,82,185,328,513,738,1005,1312\) and multiplicity at most four. The analytic parity count, not the finite run, carries the theorem for all \(k\).

## Originality: PASS

Best-of-knowledge comparison found the established hereditary-freeness theorem for extended Shi arrangements of type A, but not the type-B uniform rank-three obstruction proved here. Ambient freeness results for Shi-Catalan cones do not imply hereditary freeness of restrictions.

### Originality comparisons

**equivalent_formulations.** Equivalent formulations would exhibit a nonfree rank-three restriction or classify hereditary freeness for the same type-B family. No distinct source inspected states or implies that result.

Searches: Resultary: extended Shi type B hereditary freeness restriction rank 3 characteristic polynomial nonfree; web: "extended Shi" "type B" hereditarily free

Evidence: Resultary returned this SCOPE record as the exact semantic match and no distinct theorem with the same type-B restriction statement.; The web search surfaced type-B ambient-freeness/basis literature and the type-A hereditary paper, not a type-B hereditary classification.

**broader_coverage.** The type-A restriction theorem and ambient type-B freeness do not dominate the type-B hereditary claim because coordinate and sum hyperplanes change the restriction lattice.

Searches: Nakashima-Tsujie arXiv:2111.03585 full text; extended Shi type B freeness literature

Evidence: Nakashima-Tsujie explicitly formulate and solve hereditary freeness for type A; their family is built from braid-type difference hyperplanes.; Type-B literature found in search concerns freeness/bases of the ambient Shi arrangement, not all restrictions.

**exact_database_or_table.** The result is an infinite closed-form theorem rather than a finite database lookup.

Searches: Resultary exact/semantic search for the characteristic-polynomial family; web search for the displayed type-B witness polynomial

Evidence: No independent table or database row containing this infinite witness family was found.

**claim_vs_prior_implication.** No inspected prior implication reaches the explicit type-B rank-three restriction or its negative discriminant.

Searches: arXiv:2111.03585 Sections 1 and 4; Abe-Terao Shi-Catalan ambient freeness references

Evidence: The type-A theorem states a different root-system family and does not contain the type-B sum/coordinate restrictions.; Freeness of the ambient cone does not imply freeness of every restriction; hereditary freeness is the stronger property under study.

### Primary source inspections

- **Freeness for restriction arrangements of the extended Shi and Catalan arrangements** (https://arxiv.org/abs/2111.03585): NOT_COVERING the type-B theorem. Material read: full arXiv HTML introduction, definitions, restriction theorem setup and stated type-A hereditary classification. Evidence: The paper explicitly treats extended Shi/Catalan arrangements of type A and states the type-A hereditary criterion; the type-B coordinate/sum family is not its theorem.


Checked sources: https://arxiv.org/abs/2111.03585; https://arxiv.org/abs/1012.5884; Resultary semantic search; web type-B hereditary-freeness search


Residual originality risks: The originality conclusion is best-of-knowledge; older arrangement literature under a different type-B notation remains a residual alias risk.

## Scientific value: PASS

The claim answers the natural type-B analogue of a published hereditary-freeness question and gives a uniform rank-three obstruction with a closed characteristic polynomial, rather than an arbitrary finite sample. It also locates the first possible failure rank because all rank-at-most-two central arrangements are free.

## Limitations

Uniform non-hereditary freeness is proved only for ranks three through six as stated; the result is not a complete flat-by-flat restriction census and does not re-prove ambient freeness.
