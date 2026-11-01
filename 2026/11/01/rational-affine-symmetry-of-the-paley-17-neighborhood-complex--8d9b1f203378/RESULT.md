# Rational affine symmetry of the Paley-\(17\) neighborhood complex

## Finding
Let \(P_{17}\) be the graph on \(\mathbb F_{17}\) with an edge between \(u\) and \(v\) exactly when \(u-v\) is a nonzero square. Let \(X=\mathcal N(P_{17})\) be its **ordinary open-neighborhood complex**: a nonempty vertex set is a simplex exactly when all its vertices have a common neighbor. Let
\[
G=\mathbb F_{17}\rtimes \langle2\rangle,
\qquad \langle2\rangle=\{1,2,4,8,16,15,13,9\}\cong C_8,
\]
act on vertices by \(v\mapsto av+b\). Let \(U\subset\mathbb Q^{\mathbb F_{17}}\) be the sixteen-dimensional augmentation module for this natural affine permutation action. Let \(\eta\) be the one-dimensional rational representation in which all translations act trivially and the multiplier \(2\) acts as \(-1\). Let \(J\) be the two-dimensional rational representation with trivial translation action in which \(2\) acts by multiplication by \(i\) on \(\mathbb Q(i)\), i.e. by the matrix \(\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\).

Then the **complete rational graded \(G\)-homology representation** is
\[
\boxed{\widetilde H_3(X;\mathbb Q)\cong_{\mathbb Q[G]}U^{\oplus2}\oplus\eta\oplus J,}
\qquad
\boxed{\widetilde H_k(X;\mathbb Q)=0\quad(k\ne3).}
\]
Equivalently, the degree-three character is \(35\) at the identity, \(1\) at every nonidentity translation, \(3\) at each affine element with multiplier \(-1\), and \(-1\) at every affine element whose multiplier has order \(4\) or \(8\). In particular, the translation-fixed degree-three subspace is three-dimensional, whereas the subspace fixed by all of \(G\) is zero.

## Assumptions and scope
All homology is simplicial homology of the geometric realization, with rational coefficients, except for the explicitly labeled auxiliary mod-two calculation. The group \(G\) is the specified natural 136-element affine subgroup of graph automorphisms; the result does not need a claim that it exhausts every graph automorphism. The quadratic-residue set is
\[
Q=\{1,2,4,8,9,13,15,16\}\subset\mathbb F_{17}.
\]
The seventeen maximal simplices of \(X\) are the distinct eight-vertex sets \(v+Q\), for \(v\in\mathbb F_{17}\). The complex is not the clique, independence, closed-neighborhood, or Vietoris–Rips complex. We orient every simplex by increasing representatives \(0,\ldots,16\).

## Proof
**The rational homology is concentrated in degree three.** Exhaustively take all nonempty subsets of the seventeen sets \(v+Q\), deduplicating each subset. Their face counts in dimensions zero through seven are
\[
(17,136,612,1122,952,476,136,17).
\]
For each dimension \(k\ge1\), form the ordinary signed simplicial boundary \(\partial_k\) in the increasing orientation and reduce its entries modulo two. Exact column elimination gives the ranks
\[
(\operatorname{rank}_{\mathbb F_2}\partial_1,\ldots,
 \operatorname{rank}_{\mathbb F_2}\partial_7)
 =(16,120,492,595,357,119,17).
\]
With the reduced augmentation in degree zero, the resulting reduced mod-two Betti vector in degrees zero through seven is \((0,0,0,35,0,0,0,0)\). For integer boundary matrices, a nonzero minor modulo two is nonzero over \(\mathbb Q\), so the rational boundary ranks are at least their mod-two ranks. It follows directly from the chain-group dimensions that each rational Betti number is no greater than its corresponding mod-two Betti number; therefore all reduced rational homology outside degree three vanishes. The face vector has ordinary Euler characteristic \(-34\) and reduced Euler characteristic \(-35\). Consequently \(\dim_{\mathbb Q}\widetilde H_3(X;\mathbb Q)=35\). This argument does not assume an integral torsion classification.

**The affine Lefschetz character.** Every affine map \(g(v)=av+b\), with \(a\in Q\), preserves the family of neighborhoods because \(aQ=Q\). For an oriented simplex \(\sigma=(v_0<\cdots<v_k)\) fixed setwise by \(g\), its contribution to \(\operatorname{tr}(g\mid C_k(X;\mathbb Q))\) is the sign of the permutation \((g(v_0),\ldots,g(v_k))\); a non-fixed simplex contributes zero. Thus its cellular Lefschetz number is the alternating sum of these signed fixed-simplex counts.

For \(b=0\) and \(a=2^j\), the signed chain traces in dimensions zero through seven are exactly as follows. Each entry can be verified by testing whether a subset of \(v+Q\) is stable under multiplication by \(a\) and, if so, evaluating the inversion parity of its induced permutation.

| \(j\) | \(a\) | signed traces in degrees \(0,\ldots,7\) | Lefschetz number |
| --- | --- | --- | ---: |
| \(0\) | \(1\) | \((17,136,612,1122,952,476,136,17)\) | \(-34\) |
| \(1,3,5,7\) | \(2,8,15,9\) | \((1,0,0,0,0,0,0,-1)\) | \(2\) |
| \(2,6\) | \(4,13\) | \((1,0,0,-2,0,0,0,1)\) | \(2\) |
| \(4\) | \(16\) | \((1,-8,-4,10,0,-4,0,1)\) | \(-2\) |

A nonzero translation acts on the seventeen vertices as a 17-cycle, so it fixes no nonempty simplex of cardinality at most eight; its Lefschetz number is zero. Every affine map with \(a\ne1\) is conjugate by a translation to multiplication by \(a\): its unique vertex fixed point is \(b/(1-a)\). Therefore this table determines the Lefschetz number of **all 136 group elements**. Since the only nonzero rational homology groups are ordinary \(H_0\cong\mathbb Q\) and \(H_3\cong\mathbb Q^{35}\), the Lefschetz theorem gives \(\operatorname{tr}(g\mid H_3)=1-L(g)\), yielding the asserted character.

**Identifying the rational module.** The character of \(U\), the augmentation summand of the permutation module on the seventeen points, is \(\#\operatorname{Fix}_{\mathbb F_{17}}(g)-1\). Thus it equals \(16\) at the identity, \(-1\) on nonzero translations, and zero for \(a\ne1\). Both \(\eta\) and \(J\) kill translations. For multiplier \(2^j\), the character of \(\eta\oplus J\) is
\[
(-1)^j+2\cos(\pi j/2),
\]
which is \(3\) when \(j=0,4\) and \(-1\) at every other exponent. Hence the character of \(U^{\oplus2}\oplus\eta\oplus J\) agrees with the computed homology character on every element of \(G\). Maschke semisimplicity and character uniqueness over characteristic zero imply the claimed \(\mathbb Q[G]\)-module isomorphism. The invariant-subspace dimensions follow because \(U^G=0\), \(U^{\mathbb F_{17}}=0\), and neither \(\eta\) nor \(J\) has a \(C_8\)-fixed vector.

## Verification
The standalone file `verify_character.py` uses only Python standard-library functions. It independently reconstructs all 3,468 nonempty faces, computes the exact mod-two boundary ranks using sparse bit-vector elimination, computes signed fixed-face traces for each of the 136 affine maps, and checks equality with the explicit direct-sum character. Its recorded complete output is `VERIFY_OUTPUT.txt`, ending in `VERIFY_OK`. Execute `python3 verify_character.py` in the extracted directory. The infinite logical step is only ordinary finite-dimensional semisimple representation theory; no inference from a bounded computation to an unbounded family is made.

## Relationship to prior work
Kahle's 2005 treatment supplies the open-neighborhood construction and general graph-topological motivation, but gives random-graph asymptotic statements, not this deterministic affine homology representation. Matsushita's 2012 preprint analyzes fundamental groups of neighborhood complexes rather than this rational degree-three character. A subsequently published exact calculation of the same \(P_{17}\) neighborhood complex determines its nonequivariant integral homotopy type \(M(\mathbb Z/3,2)\vee\bigvee^{35}S^3\); the homotopy type and 35-dimensional Betti number are **not** claimed as new. That published result's complete scientific statement and proof were inspected and contain no asserted affine homology representation. The present result is not implied by knowing the homotopy type, since a group action on a fixed homotopy type need not be uniquely determined. The decomposition also concerns a different complex and action from the Paley flag complex and the Paley-13 neighborhood complex. Targeted searches found no published covering equivariant calculation, subject to the residual literature risk below.

## Limitations
This is a finite, exact statement only for the 17-vertex Paley graph and the specified affine group, with rational coefficients. It does not determine the integral lattice action on free homology or the group action on the \(\mathbb Z/3\) torsion class. It does not classify the homology of other Paley neighborhood complexes. The algorithmic checks are exhaustive for 17 vertices, not a proof about an infinite family. The literature comparison cannot eliminate unindexed equivalent work; independent mathematical validation is not claimed.

## References
1. M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077, first public 2005-12-04, https://arxiv.org/abs/math/0512077 .
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first public 2012-10-10, https://arxiv.org/abs/1210.2803 .
3. *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, published mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-neighborhood-complex-of-the-paley-graph-of--3bbd3a54ace8 .
4. T. K. Lim and C. E. Praeger, *On generalised Paley graphs and their automorphism groups*, arXiv:math/0605252 (2006), https://arxiv.org/abs/math/0605252 .
