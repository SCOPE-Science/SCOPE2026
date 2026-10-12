# Finite-field symmetry strata of three-dimensional Heisenberg Poisson algebras

## Finding

Let \(k=\mathbb F_q\), for **every prime power** \(q\), and let \(P\) be a three-dimensional (not necessarily unital) Poisson algebra whose Lie algebra is the Heisenberg Lie algebra, with \([x,y]=z\) and \([x,z]=[y,z]=0\). Suppose the commutative associative product is nonzero and its linear span \(P^2\) lies in the one-dimensional Lie-derived space \([P,P]=kz\). Then the following is a **complete classification with automorphism and derivation profiles**, not merely a classification of the underlying Lie algebra.

Write \(V=kx\oplus ky\), \(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), and let the associative product of \(u,v\in V\) be \(uv=(u^{\mathsf T}Sv)z\), where \(S\) is symmetric and nonzero. Define \(T=J^{-1}S\). Thus \(T\) is a **nonzero trace-zero** \(2\times2\) matrix. Poisson isomorphism classes are in natural bijection with \(\operatorname{GL}_2(k)\)-similarity classes of these \(T\), and

\[
|\operatorname{Aut}_{\mathrm{Pois}}(P)|=q^2|C_{\operatorname{GL}_2(k)}(T)|,\qquad
\dim_k\operatorname{Der}_{\mathrm{Pois}}(P)=2+\dim_k C_{M_2(k)}(T).
\]

Here derivations preserve **both** the associative product and Lie bracket, and \(C\) denotes the matrix centralizer.

If \(q\) is odd, there are **exactly \(q\) classes**: a unique class for each \(\delta\in k\), represented by

\[
[x,y]=z,\quad x^2=z,\quad y^2=\delta z,\quad xy=xz=yz=z^2=0.
\]

For \(\delta=0\), the product-form orbit has size \(q^2-1\), the automorphism group has order \(q^3(q-1)\), and the Poisson-derivation space has dimension \(4\). For \(\delta\ne0\), the orbit has size \(q(q+1)\) and the automorphism group has order \(q^2(q-1)^2\) when \(-\delta\) is a square; the respective values are \(q(q-1)\) and \(q^2(q^2-1)\) when \(-\delta\) is a nonsquare. Every odd-characteristic class has derivation dimension \(4\). There are \((q-1)/2\) classes of each nonzero-discriminant type.

If \(q\) is even, there are **exactly \(2q-1\) classes**. For each \(\lambda\in k\) there is a Jordan class, represented by

\[
[x,y]=z,\qquad x^2=0,\quad xy=\lambda z,\quad y^2=z,
\]

and for each \(\lambda\in k^\times\) there is a distinct scalar class, represented by

\[
[x,y]=z,\qquad x^2=y^2=0,\quad xy=\lambda z.
\]

All unlisted products or brackets involving \(z\) vanish. Each Jordan class has product-form orbit size \(q^2-1\), automorphism-group order \(q^3(q-1)\), and derivation dimension \(4\). Each scalar class has orbit size \(1\), automorphism-group order \(q^3(q-1)^2(q+1)\), and derivation dimension \(6\). Precisely these \(q-1\) scalar classes exhibit the **two-dimensional extra-symmetry jump**.

For a fixed normalized Heisenberg bracket, there are \(q^3-1\) nonzero compatible central multiplication forms; the stated product-form orbit sizes sum to this number in both characteristics.

## Assumptions and scope

A Poisson algebra here means a commutative associative \(k\)-algebra with an alternating Lie bracket satisfying \([a,bc]=[a,b]c+b[a,c]\). No unit is assumed. The hypothesis \(P^2\subseteq[P,P]\) refers to the linear span of associative products, not to products in the Lie algebra. The stipulation \(P^2\ne0\) excludes the already separate zero-product Heisenberg Poisson structure. Equivalence means simultaneous transport of both operations by an invertible \(k\)-linear map, **not** change of basis fixing \(z\). The orbit sizes above count the symmetric products relative to the fixed bracket normalization \([x,y]=z\), under the quotient \(\operatorname{GL}_2(k)\) action, rather than complete \(3\times3\) labeled structures.

## Proof

**Central annihilation follows from the hypotheses.** Choose \(x,y\) with \([x,y]=z\). Since every associative product lies in \(kz\) and \([z,P]=0\), the Poisson identity applied to \([x,xy]\) gives \(xz=0\); applied to \([y,yx]\) gives \(yz=0\), also in characteristic \(2\). Applying it to \([x,yz]\) gives \(z^2=0\). Hence every multiplication is determined by an arbitrary nonzero symmetric bilinear form \(S\) on \(V=P/kz\). Conversely every such form gives a Poisson algebra: triple associative products, nested brackets, and Leibniz cross-products all vanish.

**Reduction to similarity.** The bracket is represented by \(J\) on \(V\). Writing \(S=JT\), the condition \(S^{\mathsf T}=S\) is exactly \(\operatorname{tr}T=0\), in every characteristic. A simultaneous isomorphism must induce some \(G\in\operatorname{GL}_2(k)\) and send \(z\) to \((\det G)z\); an arbitrary central shear \(V\to kz\) can be added. The identity \(G^{\mathsf T}JG=(\det G)J\) gives the transformation \(T\mapsto G^{-1}TG\). Thus isomorphism classes are precisely the conjugacy classes of nonzero traceless \(T\). Furthermore, a Poisson automorphism consists uniquely of a central shear (\(q^2\) choices) and a matrix \(G\) commuting with \(T\), proving the automorphism formula.

**Derivations.** An arbitrary simultaneous derivation is of the form \(D(v)=Av+\ell(v)z\) and \(D(z)=(\operatorname{tr}A)z\), because it preserves the derived Lie line and satisfies the Lie derivation identity. The Poisson multiplication derivation identity is

\[
A^{\mathsf T}S+SA=(\operatorname{tr}A)S.
\]

Substitute \(S=JT\) and use \(A^{\mathsf T}J+JA=(\operatorname{tr}A)J\): this identity is equivalent to \(AT=TA\). The central functional \(\ell\) is arbitrary (two dimensions), proving the derivation formula. A nonscalar \(2\times2\) matrix has a two-dimensional full-matrix centralizer \(k[T]\); a scalar matrix has a four-dimensional one.

**Odd characteristic.** If \(\operatorname{char}k\ne2\), no nonzero traceless matrix is scalar. Every such matrix is cyclic, so its similarity class is determined by its characteristic polynomial \(t^2+\delta\), \(\delta=\det T\). The companion \(T_\delta=\left(\begin{smallmatrix}0&-\delta\\1&0\end{smallmatrix}\right)\) has \(JT_\delta=\operatorname{diag}(1,\delta)\), giving the displayed representatives. The centralizer of \(T_0\) has \(q(q-1)\) units; for \(\delta\ne0\) it has \((q-1)^2\) units if the polynomial splits into distinct linear factors (\(-\delta\) square) and \(q^2-1\) if irreducible. Division of \(|\operatorname{GL}_2(q)|=q(q-1)^2(q+1)\) by those orders gives the listed orbits. There are \((q-1)/2\) nonzero squares and nonsquares.

**Even characteristic.** Every \(t^2+\delta\) equals \((t+\lambda)^2\) for a **unique** \(\lambda\in k\), since every finite field of characteristic two is perfect. A traceless matrix is either scalar \(\lambda I\) or conjugate to \(\lambda I+N\), with \(N\) a nonzero nilpotent Jordan block. Only \(\lambda=0\) in the scalar case would make \(S=0\) and is omitted. Every Jordan block has \(q(q-1)\) commuting invertibles, while each scalar has all \(|\operatorname{GL}_2(q)|\) invertibles. The corresponding \(S=JT\) yield the two displayed kinds of products. The full centralizer dimensions are respectively \(2\) and \(4\), causing the claimed Poisson-derivation jump.

## Verification

Run `python verify.py` with Python 3 and no third-party dependencies. It independently enumerates all \(2\times2\) invertible matrices and the \(q^3-1\) nonzero traceless matrices for \(q=2,3,4,5\) (the field of order four uses the explicitly implemented quotient \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\)). It constructs every conjugacy orbit, compares actual stabilizers with all centralizer formulas, and tests the equivalence of the multiplication-derivation equation and matrix commutation for every test matrix. The verified class counts are respectively \(3,3,7,5\), with the expected orbit partitions and final `VERIFY_OK`. These finite computations check boundaries and formulas but are **not** a proof for infinitely many fields; the preceding arguments supply that proof.

## Relationship to prior work

Petrov and Pypka (arXiv:2609.13784v1; first publicly available September 12, 2026) classify low-dimensional Poisson algebras structurally, including dimension three. The 2022 classification of Abdelwahab, Fernández Ouaridi and Martín González, as tabulated in the 2024 survey by Kaygorodov, Khrypchenko and Páez-Guillán (section 1.35, page 253), treats the complex three-dimensional Poisson variety and explicitly displays a central mixed-product family. Neither cited accessible statement gives the **all-finite-field product-form orbit sizes, full automorphism orders, and modular derivation-space jump** computed here. Classification of similarity classes of \(2\times2\) matrices itself is classical and not claimed as new.

The published published-finding corpus finding *Finite-field enumeration and automorphism orders for Dedekind Poisson algebras* already treats the **anisotropic odd-characteristic subfamily** of central mixed Poisson structures (the nonsplit case with \(-\delta\) nonsquare), including its automorphism order. That overlapping subcase is credited, not separately claimed as new. The new combined symmetry profile includes the singular and split classes as well as all characteristic-two classes, and identifies exactly when Poisson derivations jump from dimension four to six.

## Limitations

This theorem assumes a three-dimensional Heisenberg Lie bracket, a nonzero associative product, and \(P^2\subseteq[P,P]\); it does **not** classify every three-dimensional Poisson algebra or higher-dimensional analogues. The 2026 Petrov–Pypka preprint's complete full text was not accessible during comparison, so an equivalent characterization or automorphism computation there cannot be definitively excluded. The 2022 primary paper was similarly checked through its abstract and the cited 2024 full-text survey, not through its entire primary text. These are originality risks, not deficiencies in the self-contained proof. No independent review is claimed.

## References

1. A. V. Petrov and O. O. Pypka, *On the Structure of Low-Dimensional Poisson Algebras over Arbitrary Fields*, arXiv:2609.13784v1 (2026), https://arxiv.org/abs/2609.13784.
2. H. Abdelwahab, A. Fernández Ouaridi and C. Martín González, *Degenerations of Poisson algebras*, arXiv:2209.09150 (2022), https://arxiv.org/abs/2209.09150.
3. I. Kaygorodov, M. Khrypchenko and P. Páez-Guillán, *The geometric classification of non-associative algebras: a survey*, Communications in Mathematics 32 (2024), 185–284, §1.35, https://doi.org/10.46298/cm.14458.
4. *Finite-field enumeration and automorphism orders for Dedekind Poisson algebras*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-finite-field-dedekind-poisson-counts-and-automorphisms--1715d90ac8e4.
