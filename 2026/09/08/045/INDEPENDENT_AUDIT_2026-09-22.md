# Independent three-axis audit — record 2026/09/08/045

Review date (UTC): 2026-09-24  
Reviewer: separate AI audit under the SCOPE historical-record campaign

## Source identity

- Source path: `2026/09/08/045`
- Audited source tree: `822da9ad8c2780f17a4fb2feb3965400cfcde0d3`
- `RESULT.md` blob: `8766d0bdeefecfced669fa8a0c27443c2e3a5ece`
- Historical audit evidence was not used as a correctness proof.
- No repair to `RESULT.md` is required.

## Claim audited

Within the class of unlabelled trees, all trees of order at most 11 have distinct
generalized spectra, while among the 551 trees of order 12 there is exactly one
nontrivial generalized-cospectral class, a pair. Thus order 12 is the first
order at which two non-isomorphic trees share both adjacency and complement
spectra. The record also gives the exact witness pair and adjacency-cospectral
resolution counts.

## Correctness — PASS

I independently generated the non-isomorphic free trees with NetworkX's
`nonisomorphic_trees` for n=2,...,12 (adding the unique n=1 tree), obtaining
counts 1,1,1,2,3,6,11,23,47,106,235,551, hence 987 through order 12.

For every generated tree I computed, in exact SymPy integer arithmetic, the
adjacency characteristic polynomial and the characteristic polynomial of
`J-I-A`. Grouping by the ordered pair of these polynomials gave:
- n=8: 23 singleton generalized classes;
- n=9: 47 singleton classes;
- n=10: 106 singleton classes;
- n=11: 235 singleton classes;
- n=12: 550 classes, distributed as 549 singletons and one class of size 2.

The independent enumeration's internal ordering differs from the record's, but
the displayed record witnesses were checked directly: they are non-isomorphic
and have identical adjacency and complement characteristic polynomials. The
shared ascending coefficient vectors recompute to
`(0,0,-6,0,39,0,-66,0,42,0,-11,0,1)` and
`(5,36,-25,-346,-334,438,798,172,-336,-246,-55,0,1)`.

Separately grouping only by adjacency characteristic polynomial reproduces the
record's numbers of trees lying in non-singleton adjacency classes:
2, 10, 8, 60, 119 for n=8,...,12. At n=12 the adjacency class-size
distribution is 432 singletons, 49 pairs, 7 triples; generalized grouping is
549 singletons and one pair. Therefore the stated resolution counts and the
minimal order 12 conclusion are exact consequences of exhaustive finite
classification within trees.

## Originality — PASS, qualified to the literature checked

The literature search used the standard DGS terminology, generalized
cospectrality, complement-cospectrality, trees, and small-order census terms.

Wei Wang, *A simple arithmetic criterion for graphs being determined by their
generalized spectra* (arXiv:1410.2164), proves a sufficient arithmetic
walk-matrix criterion for DGS; it is not an exhaustive classification of free
trees by order.

Ji, Wang and Zhang, *Generalized spectral characterization of signed trees*
(arXiv:2310.00846), Theorem 1.2 gives a sufficient discriminant criterion for
signed trees with irreducible characteristic polynomial. Its Example 1
discusses a 14-vertex adjacency-cospectral tree pair for which the sufficient
criterion prevents generalized cospectrality; it does not give the 12-vertex
generalized-cospectral pair or an n<=12 census.

I also checked the recent Zhu preprint *Main-Factor Allocation and Coronal
Realizability for Generalized Cospectral Mates of Trees*, arXiv:2608.24137v2.
Its introduction and main results develop component bounds, tree-forcing
criteria and DGS-but-not-DS double-star families. The full text describes those
structural criteria and does not report an exhaustive free-tree census or an
order-12 first generalized-cospectral tree pair.

Searches for `first generalized-cospectral pair of trees`, `generalized
cospectral trees 12`, and the witness polynomial did not identify a prior
publication of this finite census. To the best of the sources inspected, the
specific minimal-order census and explicit unique pair are not covered by the
known sufficient-criterion and structural literature. This is a qualified
priority statement, not a guarantee against an unindexed computation.

## Scientific value — PASS

This finite computation answers a natural threshold question in the DGS
program: at what smallest tree order does generalized spectral data cease to
separate all trees? The exact answer n=12, together with the unique witness
pair and the complete class distributions through that threshold, provides a
compact benchmark for generalized-spectral algorithms and a concrete
exception against which sufficient DGS criteria can be tested. This survives
after subtracting the cited general criteria, which do not determine this
minimal finite threshold.

The scope is intentionally narrow: DGS here is only within trees, not against
all graphs, and no claim is made for orders at least 13.

## Final disposition

- Correctness: **PASS**
- Originality: **PASS**, qualified to the literature checked
- Scientific value: **PASS**
- Disposition: **passed**

This is a computational/literature audit, not Lean verification or human
expert attestation.
