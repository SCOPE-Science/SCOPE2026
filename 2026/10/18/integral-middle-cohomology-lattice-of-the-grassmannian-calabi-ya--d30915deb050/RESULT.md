# Integral middle-cohomology lattice of the Grassmannian Calabi–Yau fourfold

## Finding
Let \(X\) be any smooth transverse intersection of eight Plücker hyperplanes with \(\operatorname{Gr}(2,8)\) over \(\mathbb C\). Let \(L=H^4(X;\mathbb Z)\) with the integral cup-product pairing. Then \(L\) is a torsion-free, odd, unimodular lattice of rank \(632\) and signature \((438,194)\). In particular,
\[
 L\cong I_{438,194}=\mathbb Z^{438}\oplus\mathbb Z^{194}(-1).
\]

Let \(a\) and \(b\) be the restrictions of the codimension-two Schubert classes \(\sigma_2\) and \(\sigma_{1,1}\) in that order, and put \(A=\mathbb Za+\mathbb Zb\). The embedding \(A\hookrightarrow L\) is primitive, with matrix
\[
 G_A=\begin{pmatrix}62&28\\28&14\end{pmatrix}.
\]
Its orthogonal complement \(K=A^\perp\subset L\) is an **even** integral lattice of signature \((436,194)\), rank \(630\), and discriminant group
\[
 K^*/K\cong\mathbb Z/2\mathbb Z\oplus\mathbb Z/42\mathbb Z.
\]
More precisely, identify the finite underlying group with \(\mathbb Z^2/G_A\mathbb Z^2\) by gluing. The finite quadratic form of \(K\), a complete discriminant-form specification, is
\[
 q_K([u,v])\equiv u+5v-\frac{14u^2-56uv+62v^2}{84}\pmod{2\mathbb Z}.
\]
Together with its signature, this determines the isometry class of \(K\) uniquely by the indefinite-even-lattice uniqueness criterion, since its rank is \(630\) and its discriminant length is \(2\). The second Chern class is the primitive characteristic vector \(c_2(X)=a+5b\); in particular, half this class is not integral.

## Assumptions and scope
All groups are ordinary singular (co)homology with integral coefficients, not quantum or intersection cohomology. \(X\) has complex dimension four. The Schubert classes come from the tautological rank-two bundle of the Grassmannian. A transverse smooth complete intersection is sufficient; no special equation for the hyperplanes is needed. The notation \(\mathbb Z^{194}(-1)\) means the diagonal negative standard form. The discriminant quadratic form is understood modulo even integers and the displayed coordinate group is a presentation, not a canonical choice of generators. This theorem does not assert that \(A\) contains every algebraic codimension-two cycle.

## Proof
**(1) Integral topology and the primitive Schubert lattice.** The Grassmannian \(G=\operatorname{Gr}(2,8)\) has a CW decomposition into even real cells. The integral Lefschetz hyperplane theorem, applied successively to eight smooth hyperplane sections, gives \(H_i(X;\mathbb Z)\cong H_i(G;\mathbb Z)\) for \(i<4\) and a surjection \(H_4(X;\mathbb Z)\twoheadrightarrow H_4(G;\mathbb Z)\). Thus \(H_3(X;\mathbb Z)=0\), \(H_2(X;\mathbb Z)=\mathbb Z\), and the dual map \(H^4(G;\mathbb Z)\hookrightarrow H^4(X;\mathbb Z)\) embeds the free Schubert rank-two lattice **primitively**. By universal coefficients, \(H^4(X;\mathbb Z)\) has no torsion (its torsion would be \(\operatorname{Ext}(H_3(X),\mathbb Z)\)). Poincaré duality therefore makes its middle pairing unimodular.

**(2) Characteristic classes and exact intersection data.** Let \(x,y\) be formal Chern roots of \(S^*\), where \(S\) is the tautological rank-two bundle on \(G\). Write \(h=x+y\), \(a=x^2+xy+y^2\), \(b=xy\). On \(G\),
\[
 \operatorname{ch}(TG)=(e^x+e^y)(8-e^{-x}-e^{-y}),
\]
and the normal bundle of \(X\) in \(G\) is \(\mathcal O_G(1)^{\oplus8}|_X\). Consequently \(c_1(X)=0\) and \(c_2(X)=a+5b=h^2+4b\). Schubert integration is given by
\[
 \int_G f(x,y)=[x^7y^6](x-y)f(x,y)
\]
for symmetric homogeneous polynomials of degree twelve. Since \([X]=h^8\), exact coefficient extraction gives \(\int_Xa^2=62\), \(\int_Xab=28\), \(\int_Xb^2=14\), \(\int_Xc_2^2=692\) and \(\int_Xc_4=636\). Here \(c_4= x^4+12x^3y+34x^2y^2+12xy^3+y^4\) under restriction. The first three pairings give \(G_A\), with determinant \(84\) and Smith invariant factors \((2,42)\). These Chern and vertical-intersection numbers agree with the earlier published table of Gerhardus and Jockers; their numerical evaluation is **not** claimed as novel.

**(3) Rank, signature, and odd unimodular lattice.** Weak Lefschetz and Poincaré duality force the Betti numbers outside the middle to be \((1,0,1,0,\cdot,0,1,0,1)\). Hence the Euler number \(636\) gives \(\operatorname{rank}L=636-4=632\). As \(c_1=0\), the Pontryagin classes satisfy \(p_1=-2c_2\) and \(p_2=c_2^2+2c_4\). Hirzebruch's signature theorem gives
\[
 \operatorname{sign}(L)=\frac{3\int_Xc_2^2+14\int_Xc_4}{45}=244.
\]
The real positive/negative indices are therefore \(438\) and \(194\). An even unimodular lattice has signature divisible by eight, whereas \(244\equiv4\pmod8\). Thus \(L\) is odd. The classification of indefinite odd unimodular lattices yields \(L\cong I_{438,194}\).

**(4) The even primitive orthogonal complement.** The rank-two lattice \(A\) is positive definite because its diagonal entries and determinant are positive. Thus \(K=A^\perp\) has signature \((436,194)\). For any smooth complex fourfold with \(c_1=0\), the degree-four Wu class is \(v_4=w_4+w_2^2=c_2\bmod2\). Therefore for every \(z\in L\), \(z^2\equiv z\cdot c_2(X)\pmod2\). Since \(c_2(X)=a+5b\in A\), every \(z\in K\) has even square. This proves that \(K\) is even. As the embedding of \(A\) is primitive in the unimodular \(L\), standard discriminant gluing gives a canonical anti-isometry of finite **bilinear** discriminant groups; its order is \(84\), and the Smith form gives the asserted abelian group.

To compute the quadratic refinement, represent a class \([u,v]\in A^*/A\) by \(\lambda\in A^*\) satisfying \(\lambda\cdot a=u\), \(\lambda\cdot b=v\). By primitive unimodular gluing, choose \(z\in L\) whose orthogonal projection to \(A\otimes\mathbb Q\) equals \(\lambda\); let \(\kappa\) be its projection to \(K\otimes\mathbb Q\). Then \(\kappa^2=z^2-\lambda^2\) and, by the Wu congruence, \(z^2\equiv z\cdot c_2=\lambda\cdot c_2=u+5v\pmod2\). Since
\[
 \lambda^2=(u,v)G_A^{-1}(u,v)^T=(14u^2-56uv+62v^2)/84,
\]
this yields exactly the stated \(q_K\). Its value is independent of representative modulo \(2\mathbb Z\) because \(c_2\) is characteristic. The lattice \(K\) has rank \(630\), signature with both signs nonzero, and discriminant length \(2\); Nikulin's uniqueness theorem for indefinite even lattices applies. Finally \(a+5b\) is primitive in \(A\) and \(A\) is primitive in \(L\), so \(c_2(X)\) is primitive in \(L\).

## Verification
The included `checker.py` runs using Python 3's standard library alone. It independently evaluates the degree-twelve Schubert coefficient functional, normal-bundle Chern character, pairing matrix, Chern numbers, signature, Smith invariants, and congruences. It also checks the finite quadratic formula on all \(84\) cosets and evaluates its Gauss sum numerically as \(i\sqrt{84}\), compatible with the complement's signature \(242\pmod8\). The script does **not** replace the integral Lefschetz theorem, Poincaré duality, Wu's formula, the gluing argument, or the cited uniqueness theorem; those steps are supplied above.

## Relationship to prior work
Bolognesi–Ciliberto–Verra (2026) study these smooth Grassmannian Calabi–Yau linear sections and the associated rational Pfaffian varieties. Gerhardus–Jockers (2016, Appendix A.6, pp. 48–49) already explicitly tabulate the Euler/Chern data and the \(2\times2\) Schubert intersection matrix, so **those inputs are prior work**. Braun–Watari (2014) motivate distinguishing vertical and orthogonal fourfold cohomology but do not give this integral Grassmannian lattice. The new assertion is the primitive integral embedding, complete odd middle-form isometry type, even rank-\(630\) orthogonal complement with explicit finite quadratic form, and primitivity of the Chern characteristic vector; none is listed as a theorem in the inspected relevant primary material. Nikulin's theorem supplies the standard uniqueness implication once the finite quadratic form is established.

## Limitations
No claim is made that the entire group \(H^{2,2}(X)\cap H^4(X;\mathbb Z)\) equals the ambient rank-two Schubert sublattice, nor that a specific geometric basis for all \(630\) complementary cycles has been constructed. The isometry class of the even complement is specified abstractly by its signature and discriminant quadratic form. The finding reuses known Chern and Schubert-pairing numbers and standard lattice theorems; it is not an independent calculation of quantum periods, Gromov–Witten invariants, or a new Torelli theorem. An unindexed prior specialization of general lattice-topology results could coincide with the conclusion; no exhaustive publication audit is claimed.

## References
1. M. Bolognesi, C. Ciliberto, A. Verra, *On Calabi–Yau varieties that are linear sections of Grassmannians of lines*, arXiv:2610.11925v1 (first public version 2026-10-08), https://arxiv.org/html/2610.11925v1.
2. A. Gerhardus, H. Jockers, *Quantum periods of Calabi–Yau fourfolds*, arXiv:1604.05325 (2016), especially Appendix A.6, pp. 48–49, https://arxiv.org/pdf/1604.05325.
3. A. P. Braun, T. Watari, *The vertical, the horizontal and the rest: anatomy of the middle cohomology of Calabi–Yau fourfolds and F-theory applications*, arXiv:1408.6167v3 (2014), https://arxiv.org/html/1408.6167v3.
4. V. V. Nikulin, *Integral symmetric bilinear forms and some of their applications*, Math. USSR Izv. 14 (1980), 103–167, Theorem 1.14.2, https://doi.org/10.1070/IM1980v014n01ABEH001060.
