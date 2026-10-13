# Complete rank census of idempotent derivations of full matrix algebras

## Finding

Let \(q\) be any prime power, \(n\geq2\), and \(R=M_n(\mathbb F_q)\). A derivation here means an \(\mathbb F_q\)-linear map \(D:R\to R\) satisfying \(D(XY)=D(X)Y+XD(Y)\); idempotence means **composition** \(D^2=D\), not that a matrix representing \(D\) lies in \(R\). Define the complete rank enumerator
\[
P_{n,q}(z)=\sum_{D\in\operatorname{Der}_{\mathbb F_q}(R),\ D^2=D}z^{\operatorname{rank}_{\mathbb F_q}D}.
\]
Put \(G_k(q)=\prod_{i=0}^{k-1}(q^k-q^i)\), with \(G_0(q)=1\), and write \({n\brack r}_q=\prod_{i=0}^{r-1}(q^{n-i}-1)/(q^{r-i}-1)\). If \(q\) is odd, \(P_{n,q}(z)=1\). If \(q\) is even, then
\[
\boxed{P_{n,q}(z)=1+\sum_{1\le r<n/2}{n\brack r}_q q^{r(n-r)}z^{2r(n-r)}
+\boldsymbol 1_{2\mid n}\,\frac{{n\brack n/2}_q q^{n^2/4}+G_n(q)/G_{n/2}(q^2)}{2}z^{n^2/2}.}
\]
The indicator term is absent when \(n\) is odd. Thus the formula is integral, including for even \(q\), since each numerator counts matrices divided by a fixed-point-free involution.

There is also an explicit classification by conjugation of nonzero derivations. In characteristic two, each is \(D=\operatorname{ad}(A)\), where \(\operatorname{ad}(A)(X)=AX-XA\), and exactly one of the following occurs:

* **Split:** \(D=\operatorname{ad}(E)\) with \(E^2=E\) and \(0<r=\operatorname{rank}E<n\). Replacing \(E\) by \(E+I\) gives precisely the same derivation; a representative has diagonal blocks \(I_r,0\), and \(\operatorname{rank}D=2r(n-r)\).
* **Nonsplit:** necessarily \(n=2m\). One may choose \(A\) satisfying \(A^2+A=cI\), with \(t^2+t+c\) irreducible over \(\mathbb F_q\). The associated \(\mathbb F_{q^2}\)-vector-space structure on \(\mathbb F_q^n\) has dimension \(m\); \(\operatorname{rank}D=n^2/2\). All such derivations form one conjugacy orbit, disjoint from the split orbits. Its exact size is \(G_n(q)/(2G_m(q^2))\).

For example, \(P_{2,2}(z)=1+4z^2\), \(P_{3,2}(z)=1+28z^4\), and \(P_{4,2}(z)=1+120z^6+336z^8\). The nonsplit orbit contributes \(56\) of the \(336\) rank-eight derivations in the last case.

## Assumptions and scope

No algebraic-closedness assumption is imposed. Fields are finite for enumeration, and the inner-generator and characteristic classification work over arbitrary fields, with the nonsplit branch interpreted as the quadratic field extension when available. The formulas count distinct linear derivations, **not** matrices representing them: scalar shifts \(A\mapsto A+aI\) leave \(\operatorname{ad}(A)\) unchanged. The conjugation action is induced by algebra automorphisms \(X\mapsto UXU^{-1}\), \(U\in\mathrm{GL}_n(\mathbb F_q)\).

## Proof

**1. Every derivation is inner.** Write \(E_{ij}\) for matrix units. Given \(D\), set \(A=\sum_{k=1}^{n}D(E_{k1})E_{1k}\). Since \(E_{ij}=E_{i1}E_{1j}\), the Leibniz identity gives \(D(E_{ij})=D(E_{i1})E_{1j}+E_{i1}D(E_{1j})\). Now \(AE_{ij}=D(E_{i1})E_{1j}\). Differentiating \(E_{1j}E_{k1}=\delta_{jk}E_{11}\), multiplying on the left by \(E_{i1}\) and on the right by \(E_{1k}\), then summing over \(k\), gives
\[
E_{ij}A=E_{i1}D(E_{11})E_{1j}-E_{i1}D(E_{1j})=-E_{i1}D(E_{1j}),
\]
because \(E_{11}D(E_{11})E_{11}=0\) follows from differentiating \(E_{11}^2=E_{11}\). Consequently \([A,E_{ij}]=D(E_{ij})\) for every matrix unit. A matrix commuting with all matrix units is scalar, so two generators define the same derivation exactly when their difference is scalar.

**2. Odd characteristic is rigid.** Extend scalars to an algebraic closure. Since \(D^2=D\), \(D\) is diagonalizable, with all eigenvalues in \(\{0,1\}\). If \(\lambda,\mu\) are eigenvalues of its generator \(A\), then both \(\lambda-\mu\) and \(\mu-\lambda\) occur among the eigenvalues of \(\operatorname{ad}(A)\). Indeed, triangularize \(A\) and use its action on the matrix-unit filtration (or its Kronecker-difference representation). In odd characteristic the only common value of \(\{0,1\}\) and \(\{0,-1\}\) is zero, so all eigenvalues of \(A\) coincide. Consequently \(A=\lambda I+N\) with \(N\) nilpotent after scalar extension. The commuting left and right multiplications by \(N\) are nilpotent, hence \(\operatorname{ad}(N)=L_N-R_N\) is nilpotent. A nilpotent idempotent is zero, so \(D=0\). Scalar extension does not affect this conclusion.

**3. Characteristic two reduces to a separable quadratic.** Here
\[
\operatorname{ad}(A)^2(X)=A^2X-2AXA+XA^2=\operatorname{ad}(A^2)(X).
\]
Thus \(D^2=D\) if and only if \(A^2+A=cI\) for a scalar \(c\). Shifting \(A\) by \(aI\) replaces \(c\) by \(c+a^2+a\). Let \(\operatorname{AS}(\mathbb F_q)=\{a^2+a:a\in\mathbb F_q\}\). It has index two since \(a^2+a=0\) precisely when \(a\in\{0,1\}\).

If \(c\in\operatorname{AS}(\mathbb F_q)\), choose \(a\) with \(a^2+a=c\), and set \(E=A+aI\). Then \(E^2=E\). Every such \(E\) is similar to \(\operatorname{diag}(I_r,0)\). The cases \(r=0,n\) give the zero derivation. If two idempotents give the same derivation, their difference is \(aI\), and idempotence forces \(a^2+a=0\); they are either equal or complementary \(E+I\). Therefore each nonzero split derivation corresponds to **exactly two** complementary projections. On the block decomposition \(\mathbb F_q^n=\operatorname{im}E\oplus\ker E\), its fixed-point space is precisely the off-diagonal block matrices, of dimension \(2r(n-r)\), whereas its kernel is the block-diagonal algebra.

If \(c\notin\operatorname{AS}(\mathbb F_q)\), the separable quadratic \(t^2+t+c\) is irreducible. Hence \(\mathbb F_q^n\) becomes a module over the field \(K'=\mathbb F_q[t]/(t^2+t+c)\cong\mathbb F_{q^2}\); this forces \(n=2m\), and all resulting \(A\)'s for fixed \(c\) are conjugate. The centralizer of \(A\) in \(M_n(\mathbb F_q)\) is \(M_m(K')\), of \(\mathbb F_q\)-dimension \(2m^2=n^2/2\). Thus \(\operatorname{ad}(A)\) has rank \(n^2/2\). More intrinsically, choosing a root \(\theta\in K'\), the decomposition
\[
\operatorname{End}_{\mathbb F_q}(K'^m)=\operatorname{End}_{K'}(K'^m)\oplus\{B\circ\sigma:B\in\operatorname{End}_{K'}(K'^m)\},
\]
where \(\sigma(v)=v^q\) componentwise, is the kernel-image decomposition of \(\operatorname{ad}(A)\), since \(\theta^q=\theta+1\). This proves the claimed nonsplit geometric structure.

**4. Counting split classes.** For each \(r\), the image of a rank-\(r\) projection can be any of \({n\brack r}_q\) subspaces, and the complementary kernel can be selected in \(q^{r(n-r)}\) ways. Hence \(Q_r={n\brack r}_q q^{r(n-r)}\) rank-\(r\) projections exist. Complementation identifies each projection with one of rank \(n-r\), without fixed points for nontrivial projections. When \(r<n/2\), a split derivation has precisely one representative of rank \(r\). When \(n=2r\), precisely two rank-\(r\) representatives correspond to each split derivation; its count is \(Q_r/2\).

**5. Counting the nonsplit class.** Every scalar shift preserves \(D\) and changes \(c\) within its Artin–Schreier coset. Any two nonsplit quadratic parameters differ by \(a^2+a\) and therefore are equivalent after scalar shift. Fix one nonsplit parameter \(c\). The full \(\operatorname{GL}_n(\mathbb F_q)\)-orbit of its generators has cardinality \(G_n(q)/G_m(q^2)\). Exactly two members \(A\) and \(A+I\) in that orbit define each derivation *with the same parameter* \(c\); hence the number of nonsplit derivations is \(G_n(q)/(2G_m(q^2))\). A split generator cannot become nonsplit by scalar shift because its Artin–Schreier coset is invariant. Combining the disjoint counts by rank gives the displayed polynomial. The matrix-unit argument, orbit counts, and Artin–Schreier dichotomy prove necessity and sufficiency with no enumeration assumptions beyond finiteness of the field.

## Verification

Run the supplied standard-library script `verify.py` with Python 3. It exhaustively enumerates normalized inner generators and directly checks \(D(D(E_{ij}))=D(E_{ij})\) for all matrix units. The predicted polynomials agree for \((n,q)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)\). The full \(n=4\), \(q=2\) enumeration gives \(1+120z^6+336z^8\). These finite checks are corroboration only; the unrestricted proof is above. The script implements \(\mathbb F_4\) using the irreducible polynomial \(t^2+t+1\).

## Relationship to prior work

Ashraf, Ansari and Akhter [1] investigate generalized Jordan derivations of unital rings with idempotents and discuss matrix-ring applications. Their main setting explicitly assumes two-torsion-freeness and gives no enumeration of composition-idempotent derivations in characteristic two. Bai, Gao and Li [2] analyze Lie algebras admitting idempotent derivations **over the complex numbers** and obtain an image-abelian decomposition; their argument uses division by two. It therefore does not cover the characteristic-two full matrix Lie-commutator behavior or its Artin–Schreier split/nonsplit branch. The classical facts that derivations of full matrix rings are inner, that idempotent matrices are classified by rank, and that conjugacy classes of irreducible quadratic operators have finite-field centralizers are **prior mathematical ingredients**, not claims of novelty. The contribution is the single complete composition-idempotent derivation rank census and nonsplit orbit description over every finite field.

## Limitations

The theorem concerns associative derivations of the full matrix algebra, not arbitrary Lie derivations of its underlying commutator Lie algebra, and not additive non-linear maps. The classification is for finite fields (with some arbitrary-field structural steps), not a classification of Galois forms over all imperfect fields. The source search cannot exclude every equivalently formulated result, especially one encoded in the standard theory of algebraic adjoint representations. The verifier is finite and is not an independent audit or a proof of the infinite family.

## References

[1] M. Ashraf, M. A. Ansari and M. S. Akhter, *Multiplicative generalized Jordan n-derivations of unital rings with idempotents*, arXiv:2210.08776v1, first posted 17 October 2022. https://arxiv.org/abs/2210.08776

[2] R. Bai, Y. Gao and Z. Li, *Lie algebras with idempotent derivations*, Mathematica Aeterna **5** (2015), 159–162. https://www.longdom.org/articles-pdfs/lie-algebras-with-idempotent-derivations.pdf
