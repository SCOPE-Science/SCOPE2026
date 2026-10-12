# Endomorphism rank spectra and an automorphism-density transition in alternating two-step algebras

## Finding
Let \(m\ge 1\) and let \(K\) be any field. The endomorphism monoid of the explicitly defined nonunital associative algebra \(H_m(K)\) admits a complete block description. Over every finite field it has the following **complete linear-rank enumerator**:
\[
\mathcal R_{m,q}(T)=q^{2m}G_m(q)T^{2m+1}
 +\sum_{r=0}^{m}N_{m,r}(q)\bigl(q^rT^r+(q^{2m}-q^r)T^{r+1}\bigr),
\]
where
\[
I_{m,r}(q)={m\brack r}_q\prod_{i=0}^{r-1}(q^{m-i}+1),\qquad
N_{m,r}(q)=I_{m,r}(q)\prod_{i=0}^{r-1}(q^{2m}-q^i),
\]
and
\[
G_m(q)=(q-1)q^{m^2}\prod_{i=1}^{m}(q^{2i}-1).
\]
Here the Gaussian coefficient counts \(r\)-spaces of \(\mathbb F_q^m\), and empty products are one. A rank gap occurs for \(m\ge2\): the only possible ranks are \(0,1,\ldots,m+1,2m+1\). For fixed \(m\), the fraction of algebra endomorphisms that are automorphisms tends to \(1\), \(1/2\), or \(0\) as \(q\to\infty\), according as \(m=1\), \(m=2\), or \(m\ge3\).

## Assumptions and scope
Let \(V\) have dimension \(2m\) over \(K\), equipped with a fixed nondegenerate alternating bilinear form \(\omega\). Let \(z\) be a new basis vector and define the \(K\)-vector space \(H_m(K)=V\oplus Kz\) with multiplication
\[
(v+az)(w+bz)=\omega(v,w)z
\qquad(v,w\in V,\ a,b\in K).
\]
Every product of three elements is zero, hence this is associative, nilpotent, and nonunital. Its square \(H_m(K)^2=Kz\), its two-sided annihilator is \(Kz\), and both facts hold also in characteristic \(2\). An endomorphism is a \(K\)-linear map preserving this multiplication, without a unitality requirement. The rank of a map is its rank on the full \((2m+1)\)-dimensional vector space. The theorem applies to every prime-power field order \(q\), including even characteristic.

## Proof
**1. Endomorphism normal form.** Every algebra endomorphism \(F\) preserves \(H_m(K)^2=Kz\), so \(F(z)=cz\) for a unique \(c\in K\). Decomposing \(F|_V\) along the direct sum gives unique \(A\in\operatorname{End}_K(V)\) and \(f\in V^*\) such that
\[
F(v+tz)=Av+(f(v)+ct)z.
\]
For \(v,w\in V\), the equation \(F(vw)=F(v)F(w)\) is exactly
\[\omega(Av,Aw)=c\omega(v,w).\]
All other products involve \(z\) and are zero on both sides. Thus this equation is necessary and sufficient, with no omitted compatibility conditions on \(f\).

**2. Two disjoint kinds of maps.** If \(c\ne0\), nondegeneracy of \(\omega\) forces \(A\) to be invertible: if \(Av=0\), then \(0=c\omega(v,w)\) for all \(w\), so \(v=0\). Thus \(A\) is a symplectic similitude with multiplier \(c\), and every \(f\) is allowed; the resulting endomorphism is invertible of full rank \(2m+1\). Conversely each such similitude and \(f\) gives an automorphism. The similitude multiplier map is surjective on \(K^\times\): for a symplectic basis, scaling one member in every hyperbolic pair by \(c\) yields multiplier \(c\). Over \(\mathbb F_q\), a symplectic-basis count gives
\[
|\operatorname{Sp}_{2m}(q)|=q^{m^2}\prod_{i=1}^{m}(q^{2i}-1),
\]
so the conformal group has order \(G_m(q)\) above and there are exactly \(q^{2m}G_m(q)\) algebra automorphisms (all have maximal rank).

If \(c=0\), the equation says that \(\operatorname{im}A\) is totally isotropic; hence \(r=\operatorname{rank}A\) lies in \(0\le r\le m\). The image of \(F\) is the graph of \(f\) over \(\operatorname{im}A\), possibly enlarged by the central direction \(Kz\). The central direction lies in this image exactly when \(f|_{\ker A}\ne0\). Therefore \(\operatorname{rank}F=r\) if \(f|_{\ker A}=0\), and \(\operatorname{rank}F=r+1\) otherwise. As \(\dim\ker A=2m-r\), the first condition holds for precisely \(q^r\) functionals \(f\) (those factoring through \(A\)), and the second for \(q^{2m}-q^r\).

**3. Count the isotropic images and maps onto them.** For \(0\le r\le m\), the number of totally isotropic \(r\)-spaces in symplectic \(\mathbb F_q^{2m}\) is
\[
I_{m,r}(q)={m\brack r}_q\prod_{i=0}^{r-1}(q^{m-i}+1).
\]
For completeness, build an ordered isotropic basis recursively. After choosing an isotropic \(j\)-space, the next vector must lie in its perpendicular \((2m-j)\)-space but outside the chosen \(j\)-space, hence there are \(q^{2m-j}-q^j\) choices. Divide the product of these choices by the number \(\prod_{j=0}^{r-1}(q^r-q^j)\) of ordered bases of an \(r\)-space; cancellation yields the displayed expression. For any fixed \(r\)-space \(W\), the number of surjections \(V\twoheadrightarrow W\) equals \(\prod_{i=0}^{r-1}(q^{2m}-q^i)\), by counting independent coordinate functionals. Thus \(N_{m,r}(q)\) is precisely the number of rank-\(r\) maps \(A\) with isotropic image. Multiplying by the respective functional counts and adding the disjoint invertible stratum proves \(\mathcal R_{m,q}(T)\).

**4. Rank gap.** For each \(r=0,\ldots,m\), \(N_{m,r}(q)>0\); for \(r<m\), \(q^{2m}-q^r>0\). The ranks from the singular stratum are exactly \(0,1,\ldots,m+1\), with no higher ranks. Every nonsingular map has rank \(2m+1\). For \(m\ge2\), these disjoint rank bands leave a gap \(m+2,\ldots,2m\); the interval is empty for \(m=1\).

**5. Density transition.** The summand \(q^{2m}N_{m,r}(q)\) is the total number of endomorphisms in singular rank-\(r\) matrix stratum. Its leading degree in \(q\) is
\[
s_r=2m+4mr-\frac{3r^2-r}{2}.
\]
The difference \(s_{r+1}-s_r=4m-3r-1\) is positive for \(0\le r<m\). Hence the largest singular degree is \(s_m=(5m^2+5m)/2\), attained only at \(r=m\) and with leading coefficient one. The automorphism-count polynomial \(q^{2m}G_m(q)\) has degree \(2m^2+3m+1\), also with leading coefficient one. Their singular-minus-automorphism degree difference is
\[
\frac{(m-2)(m+1)}2.
\]
Comparison of leading degrees and coefficients yields automorphism densities tending to \(1\) when \(m=1\), \(1/2\) when \(m=2\), and \(0\) when \(m\ge3\), as prime powers \(q\to\infty\).

## Verification
The included standalone Python program `checker.py` uses exact finite-field arithmetic and direct testing of the multiplication table; no external packages are required. It exhaustively enumerates all \((2m+1)\)-square linear matrices for \((m,q)=(1,2),(1,3),(1,4)\), tests whether each matrix is an algebra endomorphism, and compares its rank to the theorem. For \((m,q)=(2,2)\), it independently enumerates all \(2^{16}\) possible degree-one blocks \(A\), tests the multiplication constraint, and enumerates all \(2^4\) central functionals. All checks returned `VERIFY_OK`. In particular:
\[
\mathcal R_{1,2}(T)=1+21T+18T^2+24T^3,\quad
\mathcal R_{2,2}(T)=1+465T+15750T^2+37800T^3+11520T^5.
\]
These computations are finite checks, not a substitute for the proof for general \(m\) and \(q\). Run the extracted file with `python3 checker.py`.

## Relationship to prior work
Ignatyev–Kaygorodov–Popov [1] investigate algebraic varieties and geometric degenerations of two-step nilpotent algebras, including associative cases, but do not give the endomorphism-monoid rank census in the present theorem. The paper is the eligible, dated background source for this family. Facchini–Heidari Zadeh [2, Theorem 1.2] relate augmentations of unital algebras to composition-idempotent endomorphisms having a one-dimensional image, rather than classifying all endomorphisms of the nonunital alternating algebra here. Finite symplectic monoids [3,4] supply a plausible parallel for the matrix equation \(\omega(A-,A-)=c\omega\), but their representation-monoid and Borel/poset statements do not supply the central-functional rank lift or this algebra's endomorphism-density transition. The ideal-growth study [5] counts ideals in class-two nilpotent rings, not these algebra endomorphisms. Standard counts of symplectic groups and isotropic subspaces are used as known counting ingredients, not claimed as new.

## Limitations
This theorem concerns **linear \(K\)-algebra endomorphisms**, not arbitrary group/ring-semigroup maps and not a classification of conjugacy classes. It does not assert that classical counts of isotropic subspaces or symplectic similitudes are new. There remains a genuine bibliographic risk that a broader pre-existing classification of Heisenberg-type Lie endomorphism monoids, alternating-form contraction semigroups, or symplectic monoids implies the stated distribution in a different formulation. The directly inspected statements below have not resolved that risk. No independent audit or originality certification is claimed.

## References
[1] M. Ignatyev, I. Kaygorodov, Y. Popov, *The geometric classification of 2-step nilpotent algebras and applications*, arXiv:2103.01036 (first submitted 2021-03-01), https://arxiv.org/abs/2103.01036.

[2] A. Facchini, L. Heidari Zadeh, *Algebras with a bilinear form, and Idempotent endomorphisms*, arXiv:2210.08230 (first submitted 2022-10-15), https://arxiv.org/abs/2210.08230.

[3] *Orders of finite reductive monoids*, arXiv:0812.3105, https://arxiv.org/abs/0812.3105.

[4] *On the Borel Submonoid of a Symplectic Monoid*, arXiv:2006.00929, https://arxiv.org/abs/2006.00929.

[5] C. Bauer, C. Schein, *Ideal growth in amalgamated powers of nilpotent rings of class two and zeta functions of quiver representations*, arXiv:2202.10865 (first submitted 2022-02-22), https://arxiv.org/abs/2202.10865.
