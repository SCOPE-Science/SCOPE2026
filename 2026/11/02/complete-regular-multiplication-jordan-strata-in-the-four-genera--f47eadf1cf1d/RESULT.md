# Complete regular-multiplication Jordan strata in the four-generator exterior algebra

## Finding
Let \(V\) be a four-dimensional vector space over any field \(k\), and \(E=\bigwedge_k V\), with \(\dim_k E=16\). Write an element uniquely as
\[
x=a+v+w+z+t,\qquad a\in k,\quad v\in\bigwedge^1 V,\quad w\in\bigwedge^2 V,\quad z\in\bigwedge^3 V,\quad t\in\bigwedge^4 V.
\]
Let \(L_x:E\to E\) be left multiplication. Its only eigenvalue is \(a\), and its Jordan blocks have size at most three. The following tables give the **complete** Jordan partition \(\lambda(x)\) of \(L_x-aI\) over every field, including nonalgebraically closed fields. Let \(\rho(w)\in\{0,2,4\}\) be the rank of the alternating bilinear form encoded by the two-form \(w\) (equivalently, the rank of the skew coefficient matrix). Conditions involving \(v\wedge w\) do not depend on the choice of basis.

In characteristic other than two:

| Defining condition on the positive-degree part | \(\lambda(x)\) | \(\operatorname{rank}L_{x-a}\) | \(\operatorname{rank}(L_{x-a})^2\) | Dimension of stratum | Number over \(\mathbb F_q\) |
|---|---|---:|---:|---:|---:|
| \(v\ne0,\ v\wedge w\ne0\) | \((3^2,2^4,1^2)\) | 8 | 2 | 15 | \((q^4-1)(q^6-q^3)q^5\) |
| \(v\ne0,\ v\wedge w=0\) | \((2^8)\) | 8 | 0 | 12 | \((q^4-1)q^8\) |
| \(v=0,\ \rho(w)=4\) | \((3,2^4,1^5)\) | 6 | 1 | 11 | \(R_4(q)q^5\) |
| \(v=0,\ \rho(w)=2\) | \((2^4,1^8)\) | 4 | 0 | 10 | \(R_2(q)q^5\) |
| \(v=w=0,\ z\ne0\) | \((2^2,1^{12})\) | 2 | 0 | 5 | \((q^4-1)q\) |
| \(v=w=z=0,\ t\ne0\) | \((2,1^{14})\) | 1 | 0 | 1 | \(q-1\) |
| \(v=w=z=t=0\) | \((1^{16})\) | 0 | 0 | 0 | \(1\) |

In characteristic two:

| Defining condition | \(\lambda(x)\) | \(\operatorname{rank}L_{x-a}\) | Dimension | Number over \(\mathbb F_q\) |
|---|---|---:|---:|---:|
| \(v\ne0\) | \((2^8)\) | 8 | 15 | \((q^4-1)q^{11}\) |
| \(v=0,\ \rho(w)=4\) | \((2^6,1^4)\) | 6 | 11 | \(R_4(q)q^5\) |
| \(v=0,\ \rho(w)=2\) | \((2^4,1^8)\) | 4 | 10 | \(R_2(q)q^5\) |
| \(v=w=0,\ z\ne0\) | \((2^2,1^{12})\) | 2 | 5 | \((q^4-1)q\) |
| \(v=w=z=0,\ t\ne0\) | \((2,1^{14})\) | 1 | 1 | \(q-1\) |
| \(v=w=z=t=0\) | \((1^{16})\) | 0 | 0 | \(1\) |

Here
\[
R_2(q)=(q-1)(q^2+1)(q^2+q+1),\qquad R_4(q)=q^2(q-1)(q^3-1).
\]
Every listed stratum is a nonempty, smooth, geometrically irreducible locally closed subvariety of the fifteen-dimensional augmentation space. Its motivic class is the finite-field polynomial in its row, with \(q\) replaced by \(\mathbb L=[\mathbb A^1]\). All row counts sum to \(q^{15}\). For the full sixteen-dimensional algebra, the scalar parameter \(a\) contributes a factor \(q\) to each count, and every stratum acquires one extra affine dimension. For every field, these tables exhaust the possibilities; no additional Jordan types occur over field extensions.

## Assumptions and scope
The multiplication is the genuine exterior product: \(u\wedge u=0\) for each generator, with signed permutation of distinct generators. In characteristic two the exterior algebra is the commutative square-zero-generator algebra. The alternating rank \(\rho(w)\) is defined from its coefficient matrix in all characteristics; in characteristic two it must **not** be inferred from \(w^2\), which vanishes identically. The field may have arbitrary characteristic and need not be perfect, finite, or algebraically closed. A Jordan partition \((3^2,2^4,1^2)\) denotes two blocks of size three, four blocks of size two and two blocks of size one.

## Proof
**1. Nilpotency and rank reconstruction.** Let \(n=x-a\). The cube vanishes: in the expansion of \(n^3\), the only products of total exterior degree at most four are \(v^3\) and the three arrangements of \(v^2w\); all vanish because \(v\wedge v=0\) and \(w\) has even degree. Every other triple product has exterior degree at least five. Thus \(n^3=0\) in all characteristics. Consequently \(L_n^3=0\). A nilpotent operator on a sixteen-dimensional space with \(r_1=\operatorname{rank}L_n\) and \(r_2=\operatorname{rank}L_n^2\) has exactly \(r_2\) blocks of size three, \(r_1-2r_2\) blocks of size two and \(16-2r_1+r_2\) blocks of size one.

**2. Nonzero degree-one part.** Suppose \(v\ne0\). Choose a complement \(V=kv\oplus U\), where \(\dim U=3\), and write \(A=\bigwedge U\), \(E=A\oplus vA\), and
\[
n=vu+b+d,\quad u\in A^\times\text{ with scalar term }1,\quad b\in\bigwedge^2U,\quad d\in\bigwedge^3U.
\]
The operator \(L_n\) has block matrix, relative to this decomposition,
\[
\begin{pmatrix}L_{b+d}&0\\ L_u&L_{b-d}\end{pmatrix}.
\]
Since \(u\) is a unit and \((b+d)u^{-1}(b-d)=0\) (each outside factor has degree at least two in the three-generator exterior algebra), elementary block operations show that its rank is exactly eight. Further, if \(u=1+\alpha+\beta+\gamma\) by degrees, then
\[
n^2=2vb(1+\alpha).
\]
Indeed the square of \(vu\) and \(b+d\) vanishes, and all omitted products have exterior degree above four. If \(\operatorname{char}k=2\), then \(n^2=0\); otherwise it is zero precisely when \(b=0\), equivalent to \(v\wedge w=0\). In the nonzero case, left multiplication by the degree-three element \(vb(1+\alpha)\) has rank two: it sends \(1\) to a nonzero degree-three-plus-four element and sends \(V\) onto the one-dimensional top exterior degree. This proves both nonzero-\(v\) rows in odd characteristic and the merged row in characteristic two.

**3. Vanishing degree-one part.** If \(v=0\), write \(n=w+z+t\). When \(w\ne0\), the image of \(L_n\) has independent contributions from: the image of \(1\) (dimension one); the images of \(V\), with rank \(\rho(w)\) in degree three (one may add a degree-four correction without changing rank); and the image of \(\bigwedge^2 V\) in top degree (dimension one). Thus
\[
\operatorname{rank}L_n=2+\rho(w).
\]
The square is \(n^2=w^2\), which is \(2\operatorname{Pf}(w)\Omega\) in a chosen oriented basis, where \(\Omega\) spans \(\bigwedge^4V\). Over odd characteristic its multiplication rank is one precisely when \(\rho(w)=4\); in characteristic two it is always zero. When \(w=0,z\ne0\), the image is the span of \(n\) and the top degree (rank two). When \(w=z=0,t\ne0\), the image is the top degree (rank one); when \(n=0\), the rank is zero. Substituting in the block formulas of Step 1 establishes all partitions.

**4. Geometry and finite-field counts.** For fixed nonzero \(v\), the linear map \(\bigwedge^2V\to\bigwedge^3V\), \(w\mapsto v\wedge w\), has rank three and kernel dimension three. Thus the locus \(v\wedge w=0\) is a rank-three vector bundle over \(\mathbb A^4\setminus\{0\}\), while the nonvanishing locus is its rank-three nonzero quotient bundle. Their classes, including free \(z,t\) coordinates, are \((\mathbb L^4-1)\mathbb L^8\) and \((\mathbb L^4-1)(\mathbb L^6-\mathbb L^3)\mathbb L^5\), respectively. Both are smooth and geometrically irreducible.

In \(\bigwedge^2V\cong\mathbb A^6\), nonzero decomposable forms have alternating rank two and form the punctured affine Plücker cone over \(\mathrm{Gr}(2,4)\). The projective Grassmannian has a Schubert cell decomposition with class \((\mathbb L^2+1)(\mathbb L^2+\mathbb L+1)\), so this rank-two stratum has class \((\mathbb L-1)(\mathbb L^2+1)(\mathbb L^2+\mathbb L+1)\). The complementary rank-four open has class \(\mathbb L^6-1-R_2(\mathbb L)=\mathbb L^2(\mathbb L-1)(\mathbb L^3-1)\). These form smooth geometrically irreducible strata over any field, including characteristic two (the Plücker relation remains valid). Each has five free \(z,t\) coordinates. Finally, the remaining graded cases are complements of origins in affine spaces or a point. All geometric dimensions and motivic classes follow; the counting realization \(\mathbb L\mapsto q\) yields the finite-field census. Their disjoint union exhausts the augmentation space, and the row sum is \(q^{15}\).

## Verification
The standalone file `exterior4_verify.py` constructs the exterior multiplication table from bit-mask antisymmetry and, independently of the proof, computes \(16\times16\) left multiplication matrices, their ranks and squared ranks by Gaussian elimination over explicit finite fields. Exhaustive verification covers **all 32,768 augmentation elements over \(\mathbb F_2\)**, the complete \(2\)-form slice for \(\mathbb F_3\) and \(\mathbb F_4\), and 557 stratified operators each over \(\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_9\). Genuine degree-two extension fields are used for \(\mathbb F_4\) and \(\mathbb F_9\). The independent output is recorded in `exterior4_verify.log`, and ends with `EXTERIOR4_REGULAR_JORDAN_SPECTRUM_OK`. These tests are finite checks; the preceding argument supplies the arbitrary-field proof.

## Relationship to prior work
Domokos and Zubor [1] investigate dimensions and structure of commutative subalgebras of Grassmann algebras and explain square-zero phenomena for odd homogeneous elements; their paper explicitly assigns primary MSC `15A75`. This is distinct from the full Jordan partition, geometric stratum, and finite-field distribution of **left-regular multiplication by every element**. Márki, Meyer, Szigeti and van Wyk [2] construct matrix representations and derive Cayley–Hamilton identities for finitely generated Grassmann algebras. Their regular-representation discussion does not furnish these rank strata or point counts. Generic rank-to-Jordan identities and Plücker geometry are standard ingredients, not claimed as new. Related arithmetic results for Jordan lifts over dual-number rings and Rota–Baxter operators on a smaller exterior algebra concern different objects and do not imply these tables. The complete publication-priority search is not certified; an unlocated stronger result could still cover some or all of the statement.

## Limitations
The closed classification concerns **four** generators. It does not classify five or more generators, arbitrary operators on the same space, conjugacy classes of algebra elements, scheme-theoretic structures of rank-stratification closures, or Jordan forms over more general base rings. The finite-field tests are supportive and not a substitute for proof. Independent mathematical review has not been performed; historical priority is provisional.

## References
[1] M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916, first posted 2014-03-12; https://arxiv.org/abs/1403.2916.

[2] L. Márki, J. Meyer, J. Szigeti, and L. van Wyk, *Matrix representations of finitely generated Grassmann algebras and some consequences*, arXiv:1307.0292, first posted 2013-07-01; https://arxiv.org/abs/1307.0292.
