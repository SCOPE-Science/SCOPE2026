# Frobenius orbits and the cubic-extension hexagon of exceptional curves on a degree-one del Pezzo surface

## Finding

Let \(S/\mathbb F_5\) be the smooth degree-one del Pezzo surface
\[
 y^2=x^3+uv^2(3u-v)x+\frac14uv\bigl(4v^4-23uv^3-18u^2v^2+u^3v-4u^4\bigr)
 \subset\mathbb P_{\mathbb F_5}(1,1,2,3),
\]
where the displayed rational coefficients are reduced modulo \(5\). Among its \(240\) geometric exceptional \((-1)\)-curves, the geometric Frobenius permutation has exactly **two orbits of length \(3\)** and **twenty-six orbits of length \(9\)**. In particular, for each integer \(n\ge1\), the number \(N(n)\) of individual geometrically irreducible exceptional curves defined over \(\mathbb F_{5^n}\) is
\[
 N(n)=\begin{cases}0&3\nmid n,\\6&3\mid n\text{ and }9\nmid n,\\240&9\mid n.\end{cases}
\]

The six curves already defined over \(\mathbb F_{125}\) have pairwise intersection numbers distributed as \(0\) for six unordered pairs, \(2\) for six pairs, and \(3\) for three pairs. Their **disjointness graph is the six-cycle \(C_6\)**. Thus \(\mathbb F_{125}\) is the least extension of \(\mathbb F_5\) admitting an exceptional curve, and \(\mathbb F_{5^9}\) is the least splitting field of all \(240\) curves.

## Assumptions and scope

The defining equation is the reduction modulo \(5\) of the explicit surface in Cheltsov–Loginov–Orlov–Prokhorov [1, Theorem 1.5]. In [1, Lemma 4.1], its underlying genus-one fibration comes from the pencil of plane cubics
\[
 f_0=yz^2-x^3,\qquad f_1=xz^2+y^3+y^2z-z^3,
\]
whose reduced base scheme has affine coordinates \(y=x^3\) and
\[
 h(x)=x^9+x^6+x-1=0.
\]
The polynomial is irreducible over \(\mathbb F_5\), and every geometric member of the pencil is irreducible. These facts may also be checked using the attached exact certificate script for polynomial irreducibility; the geometric-fiber condition is the independently stated result of [1, Lemma 4.1]. The surface \(S\) is smooth and anticanonically ample by [1, Theorem 1.5]. No hypothesis about arbitrary del Pezzo surfaces or finite fields other than this specific \(S/\mathbb F_5\) is asserted.

A *geometric exceptional curve* means an irreducible curve on \(S_{\overline{\mathbb F}_5}\) of self-intersection \(-1\), necessarily smooth rational. A curve is *defined over \(\mathbb F_{5^n}\)* when the corresponding geometric subscheme descends to that field. Distinct exceptional divisor classes have unique exceptional-curve representatives on a smooth del Pezzo surface; hence descent is equivalent to Frobenius invariance of the class.

## Proof

**1. Galois action on the cubic pencil.** Since \(h\) has degree \(9\) and is irreducible over \(\mathbb F_5\), its nine distinct geometric roots form one Frobenius orbit. Let \(Y\) be the blow-up of the nine distinct base points of the pencil. On \(Y_{\overline{\mathbb F}_5}\), write \(H\) for the pullback of a line and \(E_0,\ldots,E_8\) for the nine exceptional curves in cyclic Frobenius order. These are sections of its genus-one fibration. The fiber class is
\[
 F=3H-\sum_{i=0}^{8} E_i.
\]
Frobenius fixes \(H\) and cyclically permutes the \(E_i\). The geometric intersection pairing is \(H^2=1\), \(E_i^2=-1\), \(H\cdot E_i=0\), and \(E_i\cdot E_j=0\) for \(i\ne j\).

**2. The integral root lattice and its equivariance.** The negative-definite rank-eight integral lattice
\[
 L=F^{\perp}/\mathbb ZF\subset\operatorname{NS}(Y_{\overline{\mathbb F}_5})/\mathbb ZF
\]
is the negative \(E_8\) root lattice. The nine geometric exceptional sections identify the genus-one fibration with its Jacobian elliptic fibration after choosing any one as origin. Its Jacobian is the blow-up of \(S\) at the anticanonical base point, as in [1, Sections 2–4]. Thus there is an integral intersection-preserving identification
\[
 L\simeq K_S^{\perp}\subset\operatorname{Pic}(S_{\overline{\mathbb F}_5}).
\]
The identification is Frobenius equivariant: changing the chosen origin changes the elliptic-surface identification by fiberwise translation. Translation acts trivially on \(F^{\perp}/\mathbb ZF\), since this quotient restricts isomorphically to degree-zero divisor classes on the geometric generic fiber when the fibers are irreducible [1, Lemmas 2.3 and 3.6], and translations act trivially on \(\operatorname{Pic}^0\) of an elliptic curve. The geometric identifications preserve the intersection form. This upgrades the Galois-module comparison in [1, Lemma 3.9] to the particular **integral root permutation** needed here; rational-character information alone does not count fixed roots.

**3. Complete root enumeration.** Every class of \(L\) has a unique representative \(r=dH-\sum m_iE_i\) with \(d\in\{0,1,2\}\). Such a representative is a root precisely when
\[
 \sum_{i=0}^{8}m_i=3d,\qquad\sum_{i=0}^{8}m_i^2=d^2+2.
\]
For \(d=0\), the only solutions consist of one \(+1\), one \(-1\), and seven zeros, giving \(9\cdot8=72\) roots. For \(d=1\), exactly three entries are \(+1\), giving \(\binom93=84\) roots. For \(d=2\), exactly six are \(+1\), giving \(\binom96=84\). Hence there are \(72+84+84=240\) roots, with no omitted classes. For a degree-one del Pezzo surface the correspondence \(r\longleftrightarrow C_r\) satisfying \([C_r]=r-K_S\) bijects the \(240\) roots with the \(240\) geometric exceptional curves [2, Section 1; 3, Section 1].

**4. Orbit census.** The nine-cycle permuting \(m_0,\ldots,m_8\) has no fixed root; its third power has three coordinate cycles, each of length \(3\). No \(d=0\) root is fixed by its third power. Among the \(84\) three-subsets, exactly three (the three coordinate cycles) are fixed by the third power; these form one orbit of length \(3\) under the nine-cycle. Among the \(84\) six-subsets, the three complements likewise form one length-\(3\) orbit. The other \(234\) roots have orbit length \(9\). The number of these is \(234/9=26\) orbits, proving the census and the formula for \(N(n)\).

**5. The six-curve intersection pattern.** Label the three cycles of the third Frobenius power by \(B_0,B_1,B_2\), each a three-element subset of \(\{0,\ldots,8\}\). The six fixed roots have representatives
\[
 r_i=H-\sum_{j\in B_i} E_j,\qquad
 s_i=2H-\sum_{j\notin B_i} E_j\qquad(i=0,1,2).
\]
For any two roots \(r,s\), their exceptional curves satisfy \(C_r\cdot C_s=1+r\cdot s\). Hence, for distinct \(i,j\),
\[
 C_{r_i}\cdot C_{r_j}=2,\quad C_{s_i}\cdot C_{s_j}=2,\quad
 C_{r_i}\cdot C_{s_i}=3,\quad C_{r_i}\cdot C_{s_j}=0.
\]
There are six disjoint cross-pairs, and their degree-two regular bipartite graph on six vertices is connected, hence is \(C_6\). This proves the intersection and disjointness assertions. All statements concern global intersection numbers; no claim about transversality or distinct local intersection points is made.

## Verification

The standalone `verify_exceptional_curves.py` uses exact integer arithmetic over \(\mathbb F_5\) to apply the polynomial irreducibility criterion to \(h\), enumerates all \(240\) roots in the above three congruence classes, computes every orbit under cyclic coordinate permutation, and checks the intersection numbers and connectivity of the six-vertex disjointness graph. The recorded outcome is `orbit histogram: {3: 2, 9: 26}`, `F_{5^3}-defined curves: 6`, `pairwise intersection histogram: {0: 6, 2: 6, 3: 3}`, and `C6`, with all assertions passing. The root enumeration and orbit logic are finite and exhaustive; the geometric identification rests on the proved argument and cited elliptic-surface lemmas, not on these finite checks alone.

## Relationship to prior work

Cheltsov–Loginov–Orlov–Prokhorov [1] give this surface, its degree-nine unirational parametrization, arithmetic Picard rank one, a degree-nine irreducible pencil base locus, and a Galois-module comparison for Picard groups. They do **not** state a complete \(240\)-curve Frobenius orbit and pairwise-incidence profile; the integral root-action identification and exact orbit/intersection census are the additional calculation here. General geometric descriptions of the \(240\) curves and Galois permutation groups appear in [2,3]. Fang [3] studies the *generic* del Pezzo surface, whereas \(S\) is a particular finite-field surface with small cyclic Frobenius image. Desjardins–Fu–Isham–Winter [4] classify concurrent-curve configurations rather than Frobenius-fixed exceptional subsets of this explicit surface. Blache–Hallouin [5] develop arithmetic types and zeta functions and provide concrete tables for degrees \(3\)–\(6\), not this degree-one curve-orbit profile.

## Limitations

The result is about the displayed smooth surface over \(\mathbb F_5\) and extensions \(\mathbb F_{5^n}\). It does not enumerate equations for individual exceptional curves, their intersection points, or possible birational contractions over all extensions. General Weyl-group conjugacy tables may permit the numerical orbit histogram to be reconstructed indirectly, and an unlocated independent enumeration could overlap this classification. The derived six-curve intersection pattern relies on interpreting Galois action through the integral root lattice, not merely through a rational Picard representation. Independent review has not been performed.

## References

[1] I. Cheltsov, K. Loginov, D. Orlov, Y. Prokhorov, *Unirational del Pezzo surfaces of degree one*, arXiv:2608.15435v1 (first posted 2026-08-15), especially Theorem 1.5 and Lemmas 2.3, 3.6, 3.9, 4.1. https://arxiv.org/abs/2608.15435

[2] R. Blache, E. Hallouin, *Classification of singular del Pezzo surfaces over finite fields*, arXiv:2301.13582v1, Section 1. https://arxiv.org/html/2301.13582v1

[3] X. Fang, *Galois group of exceptional curves on the generic del Pezzo surface*, arXiv:2604.01497v1, Section 1. https://arxiv.org/abs/2604.01497

[4] J. Desjardins, Y. Fu, K. Isham, R. Winter, *Generalized Eckardt points on del Pezzo surfaces of degree 1*, arXiv:2401.08800v2, Sections 1–3. https://arxiv.org/abs/2401.08800

[5] R. Blache, E. Hallouin, *Classification of singular del Pezzo surfaces over finite fields*, arXiv:2301.13582v1, introduction and arithmetic-types discussion. https://arxiv.org/html/2301.13582v1
