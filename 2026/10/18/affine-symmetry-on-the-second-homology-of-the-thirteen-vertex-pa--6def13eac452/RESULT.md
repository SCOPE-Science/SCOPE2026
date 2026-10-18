# Affine symmetry on the second homology of the thirteen-vertex Paley neighborhood complex

## Finding
Let \(P_{13}\) be the Paley graph on \(\mathbb F_{13}\), with \(u\sim v\) if and only if \(u-v\) is a nonzero quadratic residue. Let \(K=\mathcal N(P_{13})\) be the ordinary **open** Lovász neighborhood complex. Let
\[
A=\mathbb F_{13}\rtimes (\mathbb F_{13}^{\times})^2
\]
act on its vertices by \(x\mapsto ax+b\), with \(a\in\{1,3,4,9,10,12\}\) and \(b\in\mathbb F_{13}\). The complete rational homology representation is
\[
\boxed{\widetilde H_2(K;\mathbb Q)\cong \mathbb Q\oplus 2\bigl(\mathbb Q[\mathbb F_{13}]/\mathbb Q\mathbf 1\bigr)}.
\]
Here the quotient is the twelve-dimensional augmentation representation of the affine permutation action, and \(2(-)\) denotes two direct summands. Its character at \(g\in A\) is
\[
\operatorname{tr}(g\mid\widetilde H_2(K;\mathbb Q))=2|\operatorname{Fix}_{\mathbb F_{13}}(g)|-1.
\]
Thus the values are \(25\) at the identity, \(-1\) at each nonidentity translation, and \(1\) at every element with nontrivial multiplier. The invariant subspace is one-dimensional. The already published **nonequivariant** homotopy classification \(K\simeq\bigvee^{25}S^2\) is not claimed as new.

## Assumptions and scope
The graph is the six-regular Paley graph of order thirteen, also denoted \(QR(13)\) or the circulant graph \(C_{13}(1,3,4)\), not a Paley tournament. The neighborhoods are open: \(N(v)=v+Q\) for \(Q=\{1,3,4,9,10,12\}\). The complex consists precisely of subsets of the thirteen neighborhoods. The group \(A\) has order \(78\) and is specified as a subgroup of the full graph automorphism group; no representation claim is made for any larger group or other Paley order. Rational representations are meant as \(\mathbb Q[A]\)-modules.

## Proof
**Homotopy input, independently checked.** Each face is a subset of some six-element neighborhood \(v+Q\). Exhaustively taking these subsets yields \(598\) nonempty simplices and face counts \((f_0,f_1,f_2,f_3,f_4,f_5)=(13,78,221,195,78,13)\). In particular the one-skeleton is the complete graph on thirteen vertices. Of the \(286\) possible triples, exactly \(65\) are nonfaces. For each of these, an explicit exhaustive search finds a fourth vertex \(w\) such that all three triangles \(abw,bcw,caw\) are faces. Thus every missing triangular loop bounds a simplicial cone, and each present triangular loop bounds its triangle. Since loops in the complete one-skeleton are products of triangle loops, \(K\) is simply connected.

The standalone checker then performs exactly \(218\) valid elementary simplicial collapses, each removing a maximal simplex together with a nonempty codimension-one face contained in no other maximal simplex. Its remaining subcomplex has face counts \((13,68,81)\) in dimensions zero, one, two, and no higher cells. Euler characteristic is \(26\), so simple connectivity and the fact that integral second homology is a subgroup of a free cellular chain group give \(\widetilde H_2\cong\mathbb Z^{25}\), with no other reduced homology. By Hurewicz, a basis of integral \(H_2\) is represented by based maps of two-spheres; the induced map from \(\bigvee^{25}S^2\) is a homology isomorphism between simply connected CW complexes. Whitehead's homology theorem makes it a homotopy equivalence. This reproduces, but does not seek priority over, the existing nonequivariant classification.

**Equivariant character.** The affine maps preserve \(Q\), hence act simplicially on \(K\). For any simplicial automorphism \(g\), the reduced Hopf trace identity gives
\[
\operatorname{tr}(g\mid\widetilde H_2(K;\mathbb Q))=
-1+\sum_{\varnothing\ne F\in K,\;gF=F}(-1)^{|F|-1}\operatorname{sgn}(g|_F).
\]
The sign is that of the induced permutation of the ordered vertices of the invariant face. For a nonidentity translation, every nonempty orbit has thirteen vertices, while each face has at most six; therefore the sum is empty and the trace is \(-1\). For a nontranslation \(g(x)=ax+b\) with \(a\ne1\), conjugation by a translation makes it multiplication by \(a\). Enumerating the invariant unions of multiplication orbits, with orientation signs, yields the following signed augmented contributions by dimensions \((-1,0,1,2,3,4,5)\): multiplier order \(2\): \((-1,1,6,-3,-3,0,1)\); order \(3\): \((-1,1,0,2,0,0,-1)\); order \(6\): \((-1,1,0,0,0,0,1)\). Each sums to \(1\). The identity trace equals the established Betti number \(25\). These are all elements of \(A\), since its multiplicative factor is cyclic of order six.

Finally, the thirteen-point affine permutation module \(\mathbb Q[\mathbb F_{13}]\) has character \(g\mapsto|\operatorname{Fix}_{\mathbb F_{13}}(g)|\). The proposed module \(\mathbb Q\oplus2(\mathbb Q[\mathbb F_{13}]/\mathbb Q\mathbf1)\) has character \(2|\operatorname{Fix}(g)|-1\), agreeing on every group element. Rational characters determine finite-group representations in characteristic zero, establishing the asserted isomorphism. Since \(A\) acts transitively on thirteen points, the permutation augmentation has no invariants and the displayed direct summand \(\mathbb Q\) is the unique invariant line.

## Verification
Run `python3 verification/paley13_affine.py` using Python 3 and the standard library only. The checker builds all thirteen maximal neighborhoods, enumerates the complete face set, certifies a cone filling for all \(65\) missing triangles, tests every one of the \(218\) elementary collapses against the current maximal faces, verifies the terminal two-dimensional face counts, and computes signed Lefschetz traces for every one of the \(78\) affine transformations. The program prints a success line only after all exact assertions pass. The computations are finite and exhaustive for this explicit thirteen-vertex complex; they do not prove any claim about other graph orders.

## Relationship to prior work
Two previously published calculations explicitly establish the **same** nonequivariant homotopy type \(\bigvee^{25}S^2\), and their full statements and proofs have been compared. This result does **not** republish that homotopy classification. Their statements do not determine how graph automorphisms act on homology; a 25-dimensional vector space alone permits many inequivalent \(A\)-representations. The present character on all 78 elements and the complete rational module decomposition are the independent contribution.

Shukla's theorem on neighborhood complexes of maximum-degree-three graphs and four-regular circulants does not include this six-regular graph. Matsushita's fundamental-group description does not determine degree-two equivariant homology. Namiq's 2026 classification of two-linear neighborhood-complex rings discusses strongly regular graphs with positive common-neighbor parameters, but supplies neither the Paley homology representation nor this affine character.

## Limitations
The result is an exact finite equivariant calculation, not an all-Paley family theorem. It determines rational, not integral, \(A\)-module extensions or the representation of any larger group. The 25-sphere nonequivariant classification is covered by previous published results; its verification here is solely a correctness check for the new character. Novelty against unindexed equivariant work is not guaranteed; no independent review has been performed.

## References
1. *The thirteen-vertex Paley neighborhood complex is a wedge of twenty-five two-spheres*, published 2026-10-11, published-finding corpus scientific record `0bd4f768ad7e` (nonequivariant homotopy classification).
2. *The neighborhood complex of the order-13 Paley graph is a wedge of 25 two-spheres*, published 2026-10-11, published-finding corpus scientific record `3f8cbbf12bfc` (nonequivariant classification).
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, 2018-02-13.
4. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, 2012-10-10.
5. M. R. Namiq, *A Complete Classification of 2-Linear Neighborhood Complexes*, arXiv:2606.03573, 2026-06-02, especially Remark 4.10.
6. L. Lovász, *Kneser's conjecture, chromatic number, and homotopy*, J. Combin. Theory Ser. A 25 (1978), 319–324.
