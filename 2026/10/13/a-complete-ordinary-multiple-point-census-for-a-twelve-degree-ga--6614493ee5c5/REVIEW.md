# Self-review

## Correctness — PASS
The two order-twelve groups, their trivial intersection and regular action on the twelve rational source points are checked by exact projective matrix arithmetic. Their invariant trace functions give the printed degree-twelve forms, and finite Galois correspondence proves the plane parametrization is birational. The standalone checker enumerates all 122 source points over \(\mathbb F_{121}\), finds 25 fibers of size two, six of size three, two of size four, and checks every tangent determinant. Those transverse branches contribute the entire plane arithmetic-genus defect \(55\); hence no unenumerated geometric singularity can remain. The method is a proof using an exhaustive finite calculation and genus saturation, not a numerical extrapolation.

## Originality — PASS
Fukasawa–Waki [1] supply the group-pair existence construction, and do not state a singularity basket for this explicitly defined trace-coordinate model. The earlier Fukasawa–Waki examples [2] use other group pairs. Fukasawa–Higashine [3] treat birational embedding criteria, not local singularity distribution. Fukasawa–Speziali [4] require a semidirect-product group, whereas the present two groups generate all 1320 elements of \(\operatorname{PGL}_2(\mathbb F_{11})\). Literature and indexed mathematical-record searches under coefficient, group, degree and singularity-basket descriptions did not find equivalent coverage. This does not establish global priority; implicit or unindexed calculations remain a residual risk.

## Value — PASS
A degree-twelve rational curve with two prescribed outer Galois groups is a nontrivial, naturally motivated example of the known positive-characteristic construction. Its complete local singularity distribution, field of definition and rational-point count make explicit geometry not supplied by the existence theorem. The combination of ordinary points of multiplicities two, three and four and saturation of the genus bound is structurally informative; it is not a cosmetic restatement of group existence.

## Comparison and limitations
The assertion concerns a specific trace-coordinate embedding rather than the universal singularity type of every embedding with the same groups. A different choice of quotient coordinates can change the plane model. General existence and semidirect-product classifications do not imply the precise \(25+6+2\) basket. The checker uses standard-library exact arithmetic; an external mathematical audit has not been performed.

References: [1] arXiv:2103.02218v1; [2] arXiv:1704.01269v1; [3] arXiv:1809.01777v1; [4] arXiv:1801.03198v3.

Self-review: passed. Independent audit: not yet performed.
