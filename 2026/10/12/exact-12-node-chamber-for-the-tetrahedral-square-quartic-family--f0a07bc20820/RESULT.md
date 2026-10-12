# Exact 12-node chamber for the tetrahedral square-quartic family in characteristic two
## Finding
Let \(k\) be algebraically closed of characteristic \(2\). Fix four linearly independent linear forms and use them as coordinates \(x_1,\ldots,x_4\). For
\[
q=\sum_{i=1}^4 a_i x_i^2+\sum_{1\le i<j\le4} b_{ij}x_ix_j
\]
set
\[
X_q=V(x_1x_2x_3x_4+q^2)\subset\mathbb P^3_k.
\]
Then \(X_q\) has exactly twelve singular points if and only if
\[
\prod_{i=1}^4 a_i\prod_{1\le i<j\le4}b_{ij}\ne0.
\]
Whenever this holds, every singularity is an \(A_1\)-node. Moreover the scheme-theoretic singular locus is
\[
\operatorname{Sing}(X_q)=V(x_2x_3x_4,x_1x_3x_4,x_1x_2x_4,x_1x_2x_3,q^2),
\]
and is a disjoint union of twelve curvilinear schemes of length \(2\), so its total length is \(24\).

Thus, after the four marked planes are put in coordinate position, the exact twelve-node locus in the affine ten-dimensional coefficient space of \(q\) is the coefficient torus cut out by the nonvanishing of all four square coefficients and all six mixed coefficients.

## Assumptions and scope
The statement concerns the marked normal form \(x_1x_2x_3x_4+q^2\) in characteristic \(2\), with the four linear forms assumed independent. It is not a projective classification of all quartic surfaces with twelve nodes, and it does not assert that the ten coefficient hyperplanes remain intrinsic after forgetting the marked tetrahedron. The field is algebraically closed so every binary quadratic splits.

Catanese and Schütt introduced this family in Example 19 of arXiv:2206.03295v1 and stated that it has twelve nodes generally. The result here identifies the exact coefficient chamber for that generic statement and determines the entire Jacobian scheme there.

## Proof
Put
\[
F=x_1x_2x_3x_4+q^2.
\]
Because the characteristic is \(2\), every first derivative of \(q^2\) vanishes. Hence
\[
\frac{\partial F}{\partial x_1}=x_2x_3x_4,\quad
\frac{\partial F}{\partial x_2}=x_1x_3x_4,\quad
\frac{\partial F}{\partial x_3}=x_1x_2x_4,\quad
\frac{\partial F}{\partial x_4}=x_1x_2x_3.
\]
Let
\[
J=(x_2x_3x_4,x_1x_3x_4,x_1x_2x_4,x_1x_2x_3).
\]
The reduced subscheme \(V(J)\) is the union \(E\) of the six coordinate lines, namely the edges of the coordinate tetrahedron. Since \(x_1x_2x_3x_4\in J\), the Jacobian singular scheme is
\[
V(F,J)=V(J,q^2).
\]
This proves the displayed scheme formula.

Consider an edge \(L_{ij}=\{x_i=x_j=0\}\), and let \(\{k,l\}\) be the complementary pair. On this edge,
\[
q|_{L_{ij}}=a_kx_k^2+b_{kl}x_kx_l+a_lx_l^2.
\]
For a binary quadratic \(A s^2+Bst+C t^2\) over an algebraically closed field of characteristic \(2\), the two roots in \(\mathbb P^1\) are distinct exactly when \(B\ne0\), while neither root is an endpoint exactly when \(A C\ne0\). Therefore each of the six edges contributes two distinct nonvertex singular points exactly when its complementary mixed coefficient and the two corresponding square coefficients are nonzero. Simultaneously for all six edges this is precisely
\[
\prod_i a_i\prod_{i<j}b_{ij}\ne0.
\]
Under this condition no point is shared by two edges, so there are exactly \(6\cdot2=12\) singular points.

Conversely, every singular point lies on \(E\), and each edge supports at most two points of \(V(q)\). Twelve distinct singular points therefore force every edge to contribute two distinct nonvertex roots. A vanishing \(b_{kl}\) makes the corresponding binary quadratic a square and collapses its two roots; a vanishing \(a_i\) makes the vertex with only \(x_i\) nonzero a root shared by the three incident edges. Either event prevents twelve distinct support points. Thus all ten coefficients must be nonzero.

It remains to identify the local singularity and the singular-scheme length. At a singular point in the interior of an edge, two complementary coordinates are units. If \(u,v\) are transverse coordinates to that edge, then the product term is a unit times \(uv\). Since the edge root of \(q\) is simple, \(dq\) is nonzero in the edge direction, so \(w=q\) is a local parameter. After multiplying one transverse coordinate by the unit, the completed local equation is
\[
uv+w^2=0.
\]
This is the characteristic-two \(A_1\)-node used in the deformation discussion of Catanese--Schütt. Locally the Jacobian singular scheme has ideal \((u,v,w^2)\), with basis \(1,w\), hence length \(2\). The twelve supports are disjoint, giving total length \(24\).

## Verification
The accompanying checker uses only exact arithmetic. It verifies in a polynomial dictionary over \(\mathbb F_2\) that differentiating \(x_1x_2x_3x_4+q^2\) kills the square term and produces exactly the four cubic generators above. It then uses the witness
\[
q_0=\sum_i x_i^2+\sum_{i<j}x_ix_j
\]
over \(\mathbb F_4\). Every edge restriction is \(s^2+st+t^2\), whose two roots are the two nontrivial elements satisfying \(r^2+r+1=0\). The checker enumerates the resulting twelve distinct projective points, verifies the quartic and all four partial derivatives vanish at each, verifies no tetrahedron vertex lies on \(q_0=0\), and confirms the local length count \(12\cdot2=24\).

The exact theorem is proved symbolically above; the finite-field computation is a reproducibility witness, not a substitute for the universal argument.

## Relationship to prior work
Catanese--Schütt, arXiv:2206.03295v1, Example 19, introduces \(l_1l_2l_3l_4+q^2=0\) and states that the quartic has twelve nodes generally. The same paper identifies \(z^2+uv\) as the local node equation in characteristic \(2\). It does not give the coefficient-wise if-and-only-if criterion above or the length-\(24\) Jacobian scheme for the marked tetrahedral family.

Catanese, arXiv:2106.09988v3, studies a substantially smaller \(\mathfrak S_4\)-invariant family and classifies singular orbits there. That symmetric specialization neither contains arbitrary \(q\) nor implies the exact ten-coordinate chamber for the general marked family.

Searches for equivalent formulations using tetrahedral quartics, twelve nodes, characteristic two, the equation \(l_1l_2l_3l_4+q^2\), edge restrictions, Jacobian schemes, and length \(24\) did not locate a source stating this complete criterion. This is evidence of noncoverage, not a claim that no equivalent statement exists anywhere.

## Limitations
The coefficient criterion depends on retaining the marked tetrahedron. The theorem is characteristic-two specific because it uses \(d(q^2)=0\). It does not classify degenerations on the ten boundary hyperplanes beyond proving that they cannot have twelve distinct singular points, and it does not classify projective equivalences among points of the coefficient torus. An equivalent calculation may exist in classical or unindexed literature under different terminology.

## References
1. F. Catanese and M. Schütt, *Singularities of normal quartic surfaces III (char=2, non-supersingular)*, arXiv:2206.03295v1, especially Example 19 and Remark 21; published in *Tunisian Journal of Mathematics* 5 (2023), 457--478, DOI 10.2140/tunis.2023.5.457.
2. F. Catanese, *Singularities of normal quartic surfaces I (char=2)*, arXiv:2106.09988v3, especially the analysis of the \(\mathfrak S_4\)-invariant quartic family.
