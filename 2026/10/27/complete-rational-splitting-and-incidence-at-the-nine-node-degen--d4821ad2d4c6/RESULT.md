# Complete rational splitting and incidence at the nine-node degeneration of a characteristic-three quartic

## Finding

Let \(k=\mathbf F_9=\mathbf F_3(\iota)\), with \(\iota^2=-1\), and put \((X,U,V,Y)=(x_0,x_1,x_2,x_3)\). Consider the projective quartic surface \(S\subset\mathbf P^3_k\) given by
\[
\begin{aligned}
F={}&(1-\iota)(X^2UV-X^2Y^2+UVY^2)\\
&-(1+\iota)(U^2V^2-XY(U^2+V^2))\\
&-(UV+XY)(X+Y)(U+V)=0.
\end{aligned}
\]
This is the singular parameter \(a=\iota\) of Example 5.3 of Veniani's characteristic-three quartic family; the conjugate parameter \(a=-\iota\) has the same assertions by Galois conjugation.

**Arithmetic and incidence classification.** All **forty geometric lines** of \(S\) are defined over \(k\). All **nine geometric singularities** are \(k\)-rational ordinary double points. Exactly six of the forty lines pass through each node. The \(k\)-rational points on at least one of the forty lines have incidence multiplicities
\[
\begin{array}{c|rrrr}
\text{number of incident lines}&1&2&4&6\\\hline
\text{number of points}&36&153&1&9.
\end{array}
\]
The unique point on four lines is smooth; all nine points on six lines are the singular nodes. There are no further intersections of two geometric lines. The line-intersection graph has forty vertices, 294 edges, and degree multiset \(12^4,14^{18},16^{18}\). Its 135 edges meeting at singular points and 159 edges meeting at smooth points are disjoint classes. Exactly four lines contain no node, eighteen contain one, and eighteen contain two.

In particular, the **reduced geometric line scheme** is the disjoint union of forty \(k\)-rational points, with zeta function
\[
Z(F_1(S)_{\mathrm{red}}/k,T)=(1-T)^{-40}.
\]
The claim does **not** assert that the nonreduced scheme \(F_1(S)\) is étale or reduced, nor does it compute the zeta function of \(S\).

## Assumptions and scope

All geometry is in projective three-space in characteristic three; the distinguished base field is \(k=\mathbf F_9\). A line is a projective one-dimensional linear subspace, or equivalently a two-dimensional vector subspace of \(k^4\) when defined over \(k\). Incidence refers to geometric intersections of lines on the singular quartic, *including* intersections at nodes. The published geometric counts of forty distinct lines and nine ordinary double points for the exceptional fiber are used as previously established inputs, not as new results [1, Example 5.3].

## Proof

First specialize the degree-four homogeneous family equation in [1, Example 5.3] at \(a=\iota\). The identities \(\iota^2=-1\) and \(\iota^3=-\iota\) imply that the coefficients of the original first and last terms vanish and the remaining terms give exactly \(F\) above.

**Exhaustive line enumeration.** A two-dimensional subspace of \(k^4\) has a unique reduced row-echelon matrix with pivot columns \(0\le i<j\le3\). Such matrices in the six pivot charts have respective cardinalities \(9^4,9^3,9^2,9^2,9,1\); hence there are precisely
\[
9^4+9^3+2\cdot9^2+9+1=7462
\]
\(k\)-rational projective lines in \(\mathbf P^3_k\). For each matrix with rows \(u,v\), substitute \(su+tv\) into \(F\) and require all five coefficients of the resulting binary quartic to vanish in \(k\). Exact enumeration of all 7462 matrices yields **forty** distinct lines, recorded explicitly as the complete echelon-matrix list in `lines_f9.json`. The independent point-evaluation check tests all ten \(k\)-rational projective points of each accepted line against \(F\). Vanishing of the five binary coefficients is equivalent to containment, without a heuristic search or an assumed bound. Since [1, Example 5.3] proves that the geometric quartic has *exactly* forty lines, these found lines exhaust the lines over \(\bar k\). The reduced geometric line scheme is therefore forty rational points, proving the displayed zeta formula.

**Singularities.** The 820 points of \(\mathbf P^3(k)\) are exhausted in normalized projective coordinates. The simultaneous vanishing of \(F\) and its four formal partial derivatives yields nine rational points. At each, take the affine chart in which its first nonzero coordinate is normalized to one; the restricted three-by-three Hessian has nonzero determinant in \(k\). Thus all nine are ordinary nodes. The independent geometric count of nine ordinary nodes in [1] proves there are no further geometric singular points. Both conjugate fibers are defined over \(\mathbf F_9\) and have isomorphic incidence by the field automorphism \(\iota\mapsto-\iota\).

**Incidence.** Normalize the ten points on each of the forty rational lines. The resulting map from a projective point to its set of incident line indices has precisely 36 values of size one, 153 of size two, one of size four, and nine of size six. The nine points of size six coincide exactly with the nine nodes. This gives \(36+2(153)+4+6(9)=400=40(9+1)\) line-point incidences. Since any two distinct projective lines intersect in at most one geometric point and these lines are all defined over \(k\), every meeting pair is detected here. The pairs at smooth points total \(153+\binom42=159\), and those at nodes total \(9\binom62=135\), for 294 edges. Counting edge degrees yields four degrees of 12, eighteen of 14, and eighteen of 16. The line-node incidence counts follow from the same exact incidence matrix. The checker recomputes every stated number.

## Verification

Run `python3 verify.py` in a directory containing `verify.py` and `lines_f9.json` (Python standard library only). A successful run prints `VERIFY_OK`, tests the canonical 40-line certificate against a complete echelon enumeration, checks exact polynomial restrictions and pointwise evaluations independently, verifies all nine rational node Hessians, and recomputes the line-node and line-line incidence counts. This finite exhaustive argument proves the claims over \(k\); the extension from 40 rational lines/nodes to all geometric lines/nodes uses the explicit total counts in [1].

## Relationship to prior work

Veniani [1, Example 5.3] gives the defining family, identifies the exceptional value \(a^2=-1\), and states **nine \(A_1\) singularities and forty geometric lines**, with several geometric line types and valencies. Neither the geometric total counts nor those line types are newly asserted here. The present refinement establishes that *every* one of the forty geometric lines and all nine nodes descend to the concrete quadratic field \(\mathbf F_9\), and provides the exact rational-point incidence, including its unique smooth four-line point and the complete graph on forty marked lines. Some aggregate graph degrees are consistent with, and may be deduced from, Veniani's published local-valency information together with rational node incidences; they are reported as a verification of the arithmetic configuration, not separately claimed as a novel abstract graph theorem.

Degtyarev [2] classifies large line configurations of **smooth** supersingular quartics, including the neighboring smooth 58-line strata, but does not give this singular fiber's finite-field descent. A targeted search of available mathematical records and primary literature found no statement forcing full \(\mathbf F_9\)-splitting of this particular 40-line configuration. This absence is evidence of a gap, not a proof of uniqueness.

## Limitations

The main completeness step relies on the established forty-line count of [1], rather than an independent computation of the geometric Hilbert-scheme degree. The scheme structure of the line Hilbert scheme is not computed. The statement concerns the specific nodal boundary, not all specializations of the family or a classification of their isomorphism classes. Earlier specialist tables or unpublished electronic configuration files might already imply the descent and incidence facts; such an equivalent source would supersede the originality claim.

## References

[1] D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, arXiv:1608.04209 (first submitted 15 August 2016), Example 5.3 and §§1, 5. Open preprint: https://arxiv.org/abs/1608.04209 ; journal version: https://doi.org/10.1007/s00229-021-01284-9 .

[2] A. Degtyarev, *Lines in supersingular quartics*, arXiv:1604.05836 (first submitted 20 April 2016), Theorem 1.2 and §8. Open preprint: https://arxiv.org/abs/1604.05836 .
