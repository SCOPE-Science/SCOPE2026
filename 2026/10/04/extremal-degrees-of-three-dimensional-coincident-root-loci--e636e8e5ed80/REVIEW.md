# Review of Extremal degrees of three-dimensional coincident root loci


## Correctness
PASS. The object and quantifiers are explicit: all unordered three-part positive partitions of every integer \(d\ge3\). Fehér--Némethi--Rimányi record Hilbert's formula \(\deg\Delta_\lambda=3!\prod j^{{e_j}}/\prod e_j!\) and the fact that the dimension is the number of parts. The proof splits repeated and distinct triples, uses AM--GM only as an upper bound for repeated triples, and then applies strictly improving integer transfers to force the unique distinct maximizer. The minimum proof checks each multiplicity type separately. Small degrees \(3,4,5,6\) are handled directly. The exact checker independently enumerates all partitions through \(d=500\).

## Originality
PASS with residual literature risk. The closest primary source, arXiv:math/0311312, gives the degree of each individual coincident root locus and its intersection-theoretic meaning, but the inspected introduction and degree discussion do not state an extremal comparison across fixed three-part partitions; searches within the paper for “maximum” and “maximal” returned no match. arXiv:1911.01958 recalls the loci and their degree formula in service of dual and real-rank-boundary questions, not the ordinary-degree extremizers. Science-only semantic searches for maximum/minimum degree, multiple-root-locus aliases, three-part partitions, and nearest-distinct multiplicities returned no close matching finding. Because the optimization is elementary once Hilbert's formula is known, unindexed historical mention remains a genuine residual risk.

## Value
PASS. Projective degree is the exact intersection count of the stratum with a generic complementary-dimensional linear family, so extremizing it ranks the most and least prevalent three-root multiplicity patterns in generic linear families of binary forms. The maximum exhibits a non-obvious symmetry penalty: equal multiplicities lose a factorial factor, so the dominant stratum is instead the closest admissible distinct triple. The result is a complete infinite classification with sharp uniqueness and small-degree exceptions, not a numerical table.

## Closest literature and limitations
The 2003 Fehér--Némethi--Rimányi preprint is the direct source of the pointwise Hilbert degree formula and dimension statement. Brambilla--Staglianò provide later multiple-root-locus and duality context. The result does not extend automatically to four or more parts because multiplicity factorials can compete with product balancing in new ways.

Same-model review: passed. Independent audit: not yet performed.
