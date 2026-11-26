# Independent mathematical audit

## correctness

PASS

For a path using j+1 A and j B vertices, contraction gives reduced Laplacian with bI and aI on the diagonal and all minus ones off diagonal; dividing its determinant by a^(b-1)b^(a-1) gives inclusion probability [ab-(a-j-1)(b-j)]/(a^j b^(j+1)), including empty blocks. The alternating label count times this probability equals the difference of successive survival products, because paths with fixed endpoints are disjoint events. The support of J_A ends at b and that of J_B at b-1 when a>b. On common support the mass ratio is a product of accumulated tail-factor ratios and (C_j+b)/(C_j+a), C_j=j(a+b-j-1). Each new tail factor in an adjacent comparison exceeds one by an explicitly positive numerator difference a-b, and C_{j+1}-C_j=a+b-2j-2>0 there. At b=2 strictness comes from the extra A mass; a=b is symmetry. The corrected strict tail inequalities at integers 2 through b follow independently by termwise comparison of the positive products, with zero B tail at b. A fresh exhaustive finite check retained the connected 6-edge subsets of the 12 edges of K_4,3 and measured the two fixed-pair distances by graph traversal: among 432 trees, A counts at 2,4,6 were 288,132,12; B counts were 324,108,0. This exact replay prescription checks the example only. The frozen verify.py and VERIFICATION.md were inspected, not executed; the algebra above covers all sizes.

## originality

PASS

For the repaired claim only: the one-part laws are credited as exact existing results. The comparison across different hosts in the strongest indexed neighbor does not give the within-host strict likelihood-ratio order, and the broader containment results give probabilities, not the sign of their cross-class likelihood-ratio minors. The new comparison rests on a separate sign argument. This assessment is limited to inspected evidence.

## value

PASS

Distinguishing the two natural anchor classes in a single unbalanced UST host by monotone likelihood ratios is a sharper, size-uniform structural result than comparing means or tails. In particular the higher-to-lower distance odds remain ordered after conditioning on the same distance window. The result is elementary but answers a natural comparison question not decided by the existing different-host theorem. The standalone law is not counted toward value as a new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
