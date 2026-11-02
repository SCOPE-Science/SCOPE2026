# Rank-one Rota–Baxter spectra of finite-field spin factors and discriminant recovery

## Finding

Let \(q\) be an odd prime power, \(n\ge4\), and \((V,B)\) a nondegenerate symmetric bilinear space of dimension \(n\) over \(k=\mathbb F_q\). Its spin-factor Jordan algebra \(J=k1\oplus V\) has multiplication
\[
(a,u)\circ(b,v)=(ab+B(u,v),av+bu).
\]
A weight-zero Rota–Baxter operator satisfies \(R(x)\circ R(y)=R(R(x)\circ y+x\circ R(y))\) for every \(x,y\in J\). Consider all **nonzero rank-one** such operators. Let \(\mathcal R_{\rm nil}\) denote those with a square-zero image line, and \(\mathcal R_{\rm idem}\) those whose image line contains a nonzero idempotent. These are intrinsic, exhaustive and disjoint classes.

Write \(\Delta\) for the determinant square class of \(B\), \(\chi\) for the quadratic character, and set
\[
\eta=\chi((-1)^{\lfloor n/2\rfloor}\Delta),\qquad c_q=q^{n-1}-1.
\]
Every such operator has the form \(R(a',v)=\ell(v)(a,u)\), with \((a,u)\ne0\), \(B(u,u)=a^2\), \(\ell\in V^*\setminus\{0\}\), and \(\ell(u)=0\), uniquely modulo inverse simultaneous rescaling of \((a,u)\) and \(\ell\). Moreover, \(R(1)=R^2=0\). The exact counts are
\[
\begin{array}{c|cc}
 &|\mathcal R_{\rm nil}|&|\mathcal R_{\rm idem}|\\\hline
n=2m&c_q\left(\dfrac{q^{n-1}-1}{q-1}+\eta q^{m-1}\right)&c_q\left(q^{n-1}-\eta q^{m-1}\right)\\[6pt]
n=2m+1&c_q\dfrac{q^{n-1}-1}{q-1}&c_q\left(q^{n-1}+\eta q^m\right).
\end{array}
\]
Their sum is
\[
|\mathcal R_1(J)|=\begin{cases}
(q^{n-1}-1)(q^n-1)/(q-1),&n\text{ even},\\
(q^{n-1}-1)\left((q^n-1)/(q-1)+\eta q^{(n-1)/2}\right),&n\text{ odd}.
\end{cases}
\]
For fixed \(q,n\), the pair of image-type counts distinguishes the two determinant square classes of forms in **every** dimension \(n\ge4\). The total distinguishes them precisely for odd \(n\): in even dimensions its dependence on \(\eta\) cancels. For instance, at \(n=4,q=5\), both form classes have total \(19{,}344\), while the square-zero-image counts are respectively \(4{,}464\) and \(3{,}224\).

The **reduced** rank-one solution variety is smooth, geometrically irreducible, of dimension \(2n-2\), and is isomorphic to the nonzero part of a rank-\((n-1)\) vector bundle over the smooth quadric
\[
\mathcal Q=\{[a:u]\in\mathbb P(k\oplus V):a^2=B(u,u)\}.
\]

## Assumptions and scope

The field has odd characteristic, \(n\ge4\), and \(B\) is nondegenerate and symmetric. The count concerns **individual** linear weight-zero operators of rank one, not conjugacy classes. Image-line type is determined by the Jordan product, without choosing coordinates. Results do not cover characteristic two, higher ranks, or the potentially nonreduced full Rota–Baxter equation scheme.

## Proof

**Rank-one reduction.** Write \(R(x)=f(x)w\) with \(f,w\ne0\), and define \(g=f\circ L_w\), \(L_w(x)=w\circ x\). Choosing \(x_0\) with \(f(x_0)=1\), the operator identity at \((x_0,x_0)\) implies \(w^2=\mu w\). Its full polarization is then \(\mu f(x)f(y)=f(x)g(y)+f(y)g(x)\). Taking \(x=x_0\), \(y\in\ker f\) shows that \(g\) vanishes on \(\ker f\), hence \(g=\alpha f\); taking \(x=y=x_0\) gives \(\alpha=\mu/2\). Conversely those two equations are sufficient.

**Spin-factor specialization.** Let \(w=(a,u)\). If \(u=0\), then \(a\ne0\), \(w^2=aw\), and \(L_w=aI\), contradicting \(f\circ L_w=(a/2)f\). Thus \(u\ne0\). Comparison of components of \(w^2=\mu w\) gives \(\mu=2a\) and \(B(u,u)=a^2\). The map \(L_w-aI\) sends \((b,v)\) to \((B(u,v),bu)\), with image exactly \(k1\oplus ku\) because \(B\) is nondegenerate. Therefore \(f\circ L_w=af\) is equivalent to \(f(1)=f(u)=0\). Put \(\ell=f|_V\). These conditions are also sufficient. The equality \(\ell(u)=0\) yields \(R^2=0\). When \(a=0\), \(w^2=0\); otherwise \(w/(2a)\) is an idempotent.

**Fibers over a quadric.** The image line \([w]\) uniquely determines the associated point of \(\mathcal Q\). Its projection \(ku\subset V\) is nonzero for every such point. The allowed covectors \(\ell\) form the annihilator of \(ku\), an \((n-1)\)-dimensional space, with exactly \(q^{n-1}-1\) nonzero elements. Choosing a representative of \([w]\) determines \(\ell\) uniquely, with inverse adjustment under rescaling. Therefore each quadric point contributes exactly \(c_q\) distinct operators. For the square-zero-image stratum, \(a=0\), so base points are isotropic lines of \(B\). For the idempotent-image stratum, \(a\ne0\), so every base point has a unique representative \((1,u)\) satisfying \(B(u,u)=1\).

**Quadratic-form arithmetic.** Diagonalize \(B\) with entries \(d_1,\dots,d_n\). For a nontrivial additive character \(\psi\), the quadratic Gauss sum \(G=\sum_{t\in k}\psi(t^2)\) satisfies \(G^2=\chi(-1)q\), and for \(s\ne0\), \(\sum_{u\in V}\psi(sB(u,u))=\chi(s)^n\chi(\Delta)G^n\). Additive-character orthogonality gives the numbers of vectors with norms \(0\) and \(1\). For \(n=2m\) these numbers are
\[
q^{n-1}+(q-1)\eta q^{m-1}\quad\text{and}\quad q^{n-1}-\eta q^{m-1};
\]
for \(n=2m+1\) they are
\[
q^{n-1}\quad\text{and}\quad q^{n-1}+\eta q^m.
\]
Subtract the zero vector from the norm-zero count, divide by \(q-1\) to count projective isotropic lines, and multiply each line or norm-one vector by \(c_q\). This proves both columns and their sum. Both form determinant classes occur over every odd finite field; \(\eta\) takes opposite signs, with nonzero coefficients in the refined counts. Thus the refined pair recovers determinant class; the unrefined total cancels the sign exactly when \(n\) is even.

**Geometry.** The projective quadric \(\mathcal Q\) of the nondegenerate form \(a^2-B(u,u)\) is smooth and geometrically irreducible of dimension \(n-1\). Let \(\mathcal L\) be its tautological line in \(J\) and \(\mathcal U\) the tautological projected line in \(V\). Then \(\mathcal H=(\mathcal O\cdot1\oplus\mathcal U)^\perp\) inside the constant dual bundle \(J^*\) has rank \(n-1\). Nonzero tensors in \(\mathcal L\otimes\mathcal H\) correspond bijectively and algebraically to nonzero rank-one solutions, removing the scalar redundancy. The complement of the zero section is smooth and geometrically irreducible of dimension \((n-1)+(n-1)=2n-2\). This is a statement about the reduced locus, not the entire equation scheme.

## Verification

The attached dependency-free `check.py` reconstructs the original Jordan multiplication, enumerates projective image lines and admissible covectors, and evaluates the Rota–Baxter equation directly on ordered basis pairs. In dimension \(4\) over \(\mathbb F_3\), it tests **all \(29{,}282\) nonzero rank-one linear operators** and finds exactly \(1{,}040\) solutions. It also exhausts dimension-\(3\) rank-one maps over \(\mathbb F_3\) solely as an already-known boundary check, and independently samples direct identities while enumerating all admissible parameters in further cases. The ten field/form/dimension configurations include the two determinant types, dimension \(5\), and genuine extension-field arithmetic over \(\mathbb F_9\). The output is in `check_output.txt`; marker `SPIN_FACTOR_RANK_ONE_RB_OK 10_CASES`. Finite computations corroborate but do not replace the proof. Run `python3 check.py`.

## Relationship to prior work

Guo, Rosenkranz and Zheng (arXiv:1402.3702, first posted 2014-02-15) classify weight-zero Rota–Baxter operators on small semigroup algebras, not on this spin-factor family. Gubarev (arXiv:1710.02377, first posted 2017-10-06) proves cube-zero bounds for operators on spin-factor Jordan algebras and completely classifies the three-dimensional algebra (Proposition 2). His Theorem 3 studies nilpotency indices in higher dimensions, not the two image-type counts or the vector-bundle locus here. The dimension-three case is excluded from the theorem. Benito, Gubarev and Pozhidaev (arXiv:1801.07037, 2018) study Rota–Baxter operators on quadratic algebras, including primarily nonzero-weight spin-factor operators, but do not state the present rank-one arithmetic. Gubarev and Panasenko (arXiv:2502.18866, 2025) classify operators on the four-dimensional Jordan algebra \(M_2(k)^{(+)}\), which has quadratic-space dimension \(3\), also excluded here. The complete rank-one count for all \(n\ge4\), its nilpotent/idempotent-image refinement, discriminant reconstruction, and punctured bundle structure were not identified in the inspected literature or searchable prior records. This does not establish exhaustive publication priority.

## Limitations

Characteristic two, higher operator ranks, and conjugacy-orbit classifications are outside scope. No full-scheme reducedness or claim of independent validation is made. The quadratic-form counting uses classical finite-field Gauss identities. An unidentified general theorem on rank-one Rota–Baxter operators of Jordan algebras could imply parts of the result; independent historical priority confirmation remains appropriate.

## References

1. L. Guo, M. Rosenkranz, S. Zheng, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, arXiv:1402.3702 (2014), https://arxiv.org/abs/1402.3702.
2. V. Yu. Gubarev, *Rota–Baxter operators of weight zero on simple Jordan algebra of Clifford type*, arXiv:1710.02377 (2017), full text https://m.mathnet.ru/php/getFT.phtml?jrnid=semr&option_lang=rus&paperid=890&what=fullt.
3. P. Benito, V. Gubarev, A. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, arXiv:1801.07037 (2018), https://arxiv.org/abs/1801.07037.
4. V. Gubarev, A. Panasenko, *Rota-Baxter operators on the simple Jordan algebra of matrices of order two*, arXiv:2502.18866 (2025), https://arxiv.org/abs/2502.18866.
