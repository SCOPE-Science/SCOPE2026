# Canonical polarization and intersection numbers of six-contact line threefolds

## Finding
Let \(X\subset\mathbb P^5_{\mathbb C}\) be **any smooth hypersurface of degree \(d\ge6\)**. Let \(F=F(1,2;6)\) be the variety of incident pairs of a point and a projective line, and let \(V_6(X)\subset F\) be the scheme of pairs \((p,\ell)\) for which \(\ell\) has intersection multiplicity at least six with \(X\) at \(p\) (a contained line has infinite contact).

**Theorem.** The scheme \(V_6(X)\) is a pure, projective, three-dimensional local complete intersection, hence Gorenstein, with **ample dualizing line bundle**. Let \(H\) be the hyperplane class pulled back from \(\mathbb P^5\), and \(G\) the Plücker hyperplane class pulled back from \(\operatorname{Gr}(2,6)\). Its canonical class and top intersection are
\[
\omega_{V_6(X)}\cong\mathcal O_F((6d-32)H+10G)|_{V_6(X)},
\]
\[
\boxed{c_1(\omega_{V_6(X)})^3
=8d\left(58773d^4-813018d^3+4047651d^2-8560324d+6430320\right).}
\]
Here the cubic is the degree of the zero-cycle on the possibly nonreduced lci scheme; it is **not** asserted that \(V_6(X)\) is smooth for every \(X\).

For a **very general** smooth \(X\), the threefold \(V_6(X)\) is smooth and its projection to the Grassmannian is generically one-to-one on each three-dimensional component. Consequently, the Plücker degree of the three-dimensional image cycle of six-contact lines is
\[
\boxed{\deg_{\mathrm{Pl}}=3d(d-5)(5d^3+25d^2-100d+48).}
\]
In particular, for smooth sextics the canonical volume is \(64{,}403{,}136\), while the very-general sextic has a six-contact-line image cycle of Plücker degree \(25{,}704\).

## Assumptions and scope
All varieties and schemes are over \(\mathbb C\), and all intersection numbers use integral Chow classes. The ambient \(F\) parametrizes **pointed** lines and is nine-dimensional. The six-contact scheme is the vanishing scheme of the six coefficients of a degree-\(d\) defining equation along the length-six infinitesimal neighborhood of the marked point. We distinguish the canonical volume of this pointed scheme from the degree of the **unpointed** image in the Grassmannian. The latter statement requires a very general hypersurface.

## Proof
**1. Six-jet equations.** Let \(\pi:F\to\mathbb P^5\) denote the marked-point map. Write \(F\cong\mathbb P(T_{\mathbb P^5})\) for the bundle of tangent-direction **lines** and \(S\subset\pi^*T_{\mathbb P^5}\) for its tautological line. Put \(\eta=c_1(S^*)\). The exact relation with the Plücker class is
\[
\eta=G-2H.
\]
The bundle \(E_d\) of relative principal parts through order five of \(\mathcal O_{\mathbb P^5}(d)\) along the marked line has rank six. Its jet filtration has one-dimensional successive quotients
\(\pi^*\mathcal O(d)\otimes(S^*)^{\otimes j}\) for \(0\le j\le5\). The defining polynomial gives a section whose zero scheme is exactly \(V_6(X)\), and therefore
\[
 c_6(E_d)=\prod_{j=0}^{5}(dH+j\eta)
 =\prod_{j=0}^{5}((d-2j)H+jG). \tag{1}
\]
This formula is the standard relative principal-parts construction also used by Bertone--Weimann; **(1) by itself is not claimed as new**.

**2. Local complete intersection and canonical polarization for every smooth \(X\).** Theorem 1.2 of Beheshti--Mukhopadhyay proves that \(V_6(X)\) has dimension exactly \(3=2\cdot5-7\) for every smooth \(X\) with \(d\ge6\). Every component of the zero locus of six equations in the smooth ninefold \(F\) has dimension at least three. Therefore all its components have codimension exactly six, and its defining section is regular: the local defining equations form a regular sequence in the regular local rings of \(F\). Thus \(V_6(X)\) is pure lci and Gorenstein, and its fundamental Chow class is (1).

The projective-bundle tangent sequence gives
\[
K_F=-12H-5\eta=-2H-5G.
\]
Since \(\det E_d\) has first Chern class \(6dH+15\eta\), lci adjunction yields
\[
K_{V_6(X)}=(K_F+c_1(E_d))|_{V_6(X)}
=((6d-12)H+10\eta)|_{V_6(X)}
=((6d-32)H+10G)|_{V_6(X)}. \tag{2}
\]
Both \(H\) and \(G\) are pullbacks of ample classes from the two factors of the closed incidence embedding \(F\hookrightarrow\mathbb P^5\times\operatorname{Gr}(2,6)\). Since \(6d-32>0\) for every \(d\ge6\), the positive linear combination in (2) is ample, and so is its restriction to every closed subscheme \(V_6(X)\), independently of reducedness or singularities.

**3. Smoothness and image degree for very general \(X\).** Let \(\mathbb P^N\) parametrize degree-\(d\) hypersurfaces. At any flag, evaluation of the six restricted jets is a surjective linear map on global degree-\(d\) equations (because \(d\ge6\)). The universal vanishing incidence \(\mathcal I\subset F\times\mathbb P^N\) is a projective bundle over \(F\), hence smooth and irreducible. Its projection to \(\mathbb P^N\) is dominant, since the top Chern number \(\int_F H^3c_6(E_d)=274d^2-720d>0\), which forces the zero locus to be nonempty for every section. Generic smoothness in characteristic zero then gives smooth fibers of dimension three for a very general smooth hypersurface.

For \(d\le11\), a noncontained line cannot have distinct points with sixfold contact (their multiplicities would sum to at least twelve). For \(d\ge12\), ordered distinct pairs of marked points on a line have a ten-dimensional parameter space; imposing two length-six jets gives twelve independent linear conditions on the degree-\(d\) polynomial. The corresponding incidence does not dominate \(\mathbb P^N\), so a very general \(X\) has no such lines. Finally, the incidence of lines **contained** in a very general \(X\) has dimension at most \(7-d\) as a Fano scheme (empty if \(d\ge8\)); including a marked point raises dimension by one, still below three. Thus the Grassmannian map is generically one-to-one on every three-dimensional component. Its image cycle has Plücker degree \(\int_FG^3c_6(E_d)\).

**4. Explicit intersection evaluation.** Since \(F=\mathbb P(T_{\mathbb P^5})\) and \(c(T_{\mathbb P^5})=(1+H)^6\), the projective-bundle pushforward identity is
\[
\pi_*(\eta^{4+i})=(-1)^i\binom{5+i}{i}H^i\quad(i\ge0),
\qquad\pi_*(\eta^j)=0\quad(j<4).
\]
Using \(\int_{\mathbb P^5}H^5=1\) and (1), direct expansion yields
\[
\int_{V_6(X)}G^3=3d(d-5)(5d^3+25d^2-100d+48),
\]
\[
\int_{V_6(X)}((6d-12)H+10\eta)^3
=8d(58773d^4-813018d^3+4047651d^2-8560324d+6430320).
\]
The second identity is valid for **every** smooth \(X\), because the lci fundamental class is the top Chern class, even if the contact scheme is not reduced.

## Verification
The standalone `verify.py` uses only the Python standard library. It computes the two polynomials independently via a projective-bundle Segre-class expansion and via exact rational torus-fixed-point localization on the thirty fixed flags. It verifies the polynomial formulas for \(6\le d\le27\) and localization for \(6\le d\le14\), plus the explicit sextic and septic values. Both calculations returned `VERIFY_OK` when run from the packaged source. Finitely many checks do not replace the general proof above.

## Relationship to prior work
Beheshti--Mukhopadhyay (arXiv:2610.28558, Theorem 1.2) supplies the **all-smooth-hypersurfaces expected-dimension theorem**, but does not state the universal Gorenstein/ample-dualizing conclusion or the canonical volume. Bertone--Weimann (arXiv:2502.02075, Theorem 1.1 and Section 5) proves generic dimensions and the point-locus degree and develops exactly the principal-parts Chow class used in (1). In particular, its published degree for the six-flex **point locus** is \(274d^2-720d\), equal to our \(\int H^3c_6(E_d)\); this number is **known** and not a novelty claim. Their text does not give the top canonical intersection nor the **Grassmannian Plücker degree of the unpointed six-contact line image**. Patel--Riedl--Smith--Tseng (arXiv:2208.04393) provides the earlier tangent-line intersection method and conditional six-contact plane bound, not these polarized threefold invariants.

The new assertion is the uniform canonical positivity for **every smooth hypersurface**, together with its exact threefold canonical volume and the Plücker degree of the very-general unpointed-line image. Earlier full Chow-class results make the numerical integrations accessible; they are openly acknowledged as a significant originality limitation, not treated as negative search results.

## Limitations
The canonical-positivity statement is scheme-theoretic: it does **not** imply smoothness, normality, or irreducibility for every \(X\). The Plücker-degree statement is only for a very general hypersurface and describes the fundamental image cycle, not the possibly singular scheme structure on its image. The work concerns degree \(d\ge6\), dimension-five projective space and characteristic zero. The computation does not determine the Hodge numbers, deformation classes, or number of irreducible components. Earlier general Chow-class work may reduce the historical novelty of the numerical portion; no independent audit of priority or proof has been performed.

## References
1. R. Beheshti and S. Mukhopadhyay, *Higher-order tangent lines to smooth hypersurfaces*, arXiv:2610.28558v1 (first posted 20 October 2026), Theorem 1.2; https://arxiv.org/abs/2610.28558.
2. C. Bertone and M. Weimann, *Hyperflex loci of hypersurfaces*, arXiv:2502.02075v1 (first posted 4 February 2025), Theorem 1.1 and Sections 2, 4, 5; https://arxiv.org/abs/2502.02075.
3. A. Patel, E. Riedl, G. Smith and D. Tseng, *Lines highly tangent to a hypersurface*, arXiv:2208.04393v1 (first posted 8 August 2022), Section 4; https://arxiv.org/abs/2208.04393.
