# Independent audit — 2026-09-29

Record: `2026/09/11/059`  
Audited tree: `682c9825267b579334810350f51e29d86d0b43a5`  
Disposition: **repaired**

## Correctness

I independently brute-forced all 30 labeled connected acyclic directed
3-edge multigraphs, all compositions of four incoming and four outgoing legs,
and all positive bounded-edge weights up to 8. The canonical S3 quotient stabilizes
at 105 underlying decorated classes already by weight 4, with no new class through
weight 8. Recomputing linear-extension counts and full automorphism orders gives
23,352 marked isomorphism classes. Weighting those markings by
`prod [w]_q^2` reproduces exactly

`6q^-5 + 96q^-4 + 798q^-3 + 4416q^-2 + 17274q^-1 + 42432 + ... + 6q^5`

and `G(1)=87612`. Independently expanding Bousseau's Theorem 5.12 specialization
reproduces `N1=87612`, `N2=-94913`, `N3=3306499/60`,
`N4=-8097139/360`, `N5=308342441/43200`.

The published polynomial and lambda-series are correct. The published count
"105 isomorphism classes of marked diagrams" is not: 105 is the number of
underlying unmarked decorated classes, whose marking counts sum to 23,352.
The staged repair corrects RESULT, METADATA, and SLOGAN accordingly.

## Originality

The general correspondence is Bousseau's theorem. The potentially original
content is the explicit finite `(3,4)` ledger and coefficient specialization;
search non-detection is not treated as proof of priority.

## Scientific value

The corrected ledger is a useful exact benchmark for implementations of refined
genus-one floor-diagram counts and for checking the higher-genus lambda-series
normalization.

Sources: https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/059 ; https://arxiv.org/abs/1904.10311 ; https://doi.org/10.1007/s00029-021-00667-w
