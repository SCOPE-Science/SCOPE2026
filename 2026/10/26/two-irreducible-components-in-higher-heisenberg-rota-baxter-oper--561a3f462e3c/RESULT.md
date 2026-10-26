# Two irreducible components in higher Heisenberg Rota--Baxter operator varieties

## Finding
Let \(k\) be a field and \(H_n(k)=V\oplus kz\) the Heisenberg Lie algebra with \(\dim V=2n\), \(n\geq1\), and bracket \([v,w]=\omega(v,w)z\) for a nondegenerate alternating form \(\omega\). Write a linear endomorphism uniquely as
\[
R(v+tz)=Av+tu+(\ell(v)+ct)z,
\]
where \(A\in\operatorname{End}(V)\), \(u\in V\), \(\ell\in V^*\), \(c\in k\). It satisfies the weight-zero Rota--Baxter identity
\[
[R(x),R(y)]=R([R(x),y]+[x,R(y)])\quad(x,y\in H_n(k))
\]
if and only if \(u=0\) and
\[
\boxed{(A-cI)^T J(A-cI)=c^2J},
\]
where \(J\) represents \(\omega\) in a symplectic basis. Thus \(\ell\) is arbitrary; for \(c\ne0\) one has \(A=c(I+S)\) with \(S\in\operatorname{Sp}_{2n}(k)\), whereas for \(c=0\) the image of \(A\) is totally isotropic.

Let \(\mathcal R_n\) be the **reduced affine algebraic set** of these operators over an algebraically closed field, not a claim about the possibly nonreduced scheme cut out by all coefficient equations. If \(n=1\), then \(\mathcal R_1\) is irreducible of dimension \(6\). For **each \(n\ge2\)**, it has **exactly two distinct irreducible components**: the closure of its \(c\ne0\) locus, of dimension
\[
D_{\mathrm{gen}}=2n^2+3n+1,
\]
and the entire \(c=0\) locus, of dimension
\[
D_{\mathrm{special}}=\frac{5n(n+1)}2.
\]
The dimensions agree for \(n=2\); the special component is strictly larger for every \(n\ge3\), by \((n-2)(n+1)/2\).

Over every finite field \(\mathbb F_q\), the exact number of weight-zero Rota--Baxter operators is
\[
\boxed{\#\mathcal R_n(\mathbb F_q)=q^{2n}\left[(q-1)q^{n^2}\prod_{j=1}^n(q^{2j}-1)+\sum_{r=0}^n I_{n,r}(q)\prod_{j=0}^{r-1}(q^{2n}-q^j)\right]},
\]
where empty products are \(1\) and
\[
I_{n,r}(q)=\prod_{j=0}^{r-1}\frac{q^{2n-j}-q^j}{q^r-q^j}
\]
is the number of totally isotropic \(r\)-planes. In particular, the counts for \(n=1\) and \(n=2\) are, respectively, \(q^6\) and \(q^{11}(2q^4+q-2)\).

## Assumptions and scope
The structural characterization holds for every field, including characteristic two. Irreducible-component statements concern reduced algebraic sets over algebraically closed fields, in all characteristics. Exact counts concern all prime powers \(q\). The result does not classify operators modulo automorphism conjugacy, scheme-theoretic multiplicities, or Rota--Baxter operators of nonzero weight.

## Proof
**Step 1: the central generator is preserved.** Substitute \(x=z\), \(y=v\in V\) into the Rota--Baxter identity. The left side is central. Its right side has \(V\)-component \(\omega(u,v)u\). If \(u\ne0\), nondegeneracy supplies \(v\) with \(\omega(u,v)\ne0\), a contradiction. Thus \(u=0\).

**Step 2: symplectic reduction.** For \(v,w\in V\), the defining identity now reads
\[
\omega(Av,Aw)=c\bigl(\omega(Av,w)+\omega(v,Aw)\bigr).
\]
Adding \(c^2\omega(v,w)\) to the two sides after expanding \(\omega((A-cI)v,(A-cI)w)\) gives exactly \((A-cI)^TJ(A-cI)=c^2J\). Conversely, this equation and \(u=0\) verify the identity for every pair, since terms involving \(z\) vanish. When \(c\ne0\), dividing by \(c^2\) gives \(S=(A-cI)/c\in\operatorname{Sp}_{2n}\). When \(c=0\), \(\omega(Av,Aw)=0\) means \(\operatorname{im}A\) is totally isotropic.

**Step 3: components.** The open \(c\ne0\) locus is isomorphic to \(\mathbb G_m\times\operatorname{Sp}_{2n}\times\mathbb A^{2n}\), irreducible of dimension \(1+n(2n+1)+2n\). The closed \(c=0\) locus is the image in \(\operatorname{End}(V)\) of the total space of the vector bundle \(\operatorname{Hom}(V,\mathcal L)\) over \(\operatorname{LG}(n,V)\), where \(\mathcal L\) is the universal Lagrangian subbundle. Every isotropic image lies in some Lagrangian, so this image is the entire special locus; irreducibility follows, and the rank-\(n\) part is dense with a uniquely determined Lagrangian. Therefore its dimension is \(2n^2+n(n+1)/2+2n\).

For \(c\ne0\), the displayed symplectic identity also implies the *dual polynomial identity*
\[
(A-cI)J^{-1}(A-cI)^T=c^2J^{-1}.
\]
This identity persists on the closure of the open locus. For \(n\ge2\), choose a symplectic basis \(e_1,\ldots,e_n,f_1,\ldots,f_n\), and let \(A(e_1)=e_1\), \(A(f_1)=e_2\), with \(A\) zero on all other basis vectors. Its image \(\langle e_1,e_2\rangle\) is isotropic, but its two nonzero rows pair nontrivially under \(J^{-1}\). Hence \(AJ^{-1}A^T\ne0\): this \(c=0\) point is not in the closure of the open locus. The entire variety is the union of that irreducible closure and the irreducible special locus, neither contained in the other, so these are exactly the two irreducible components.

For \(n=1\), every nonzero singular \(2\times2\) matrix has rank one and can be written \(U\operatorname{diag}(1,0)W\) with \(U,W\in\operatorname{SL}_2(k)\). It is the limit, as \(t\to0\), of \(B_t=U\operatorname{diag}(1,t^2)W\), where \(c_t=t\) and \(A_t=B_t+tI\) satisfy the nonzero-\(c\) condition. The zero matrix is the limit obtained from \(B_t=tI\). Thus the whole special locus is in the closure of the open locus when \(n=1\), proving irreducibility and dimension \(6\).

**Step 4: finite-field count.** There are \(q^{2n}\) choices of \(\ell\). For each \(c\ne0\), the symplectic group contributes \(q^{n^2}\prod_{j=1}^n(q^{2j}-1)\) choices of \(A\). For \(c=0\), stratify \(A\) by image dimension \(r\le n\). Construct an ordered isotropic basis one vector at a time to obtain \(I_{n,r}(q)\), then choose a surjection \(V\twoheadrightarrow\mathbb F_q^r\), giving \(\prod_{j=0}^{r-1}(q^{2n}-q^j)\) maps onto that chosen image. Summing proves the formula. Elementary simplification gives \(q^6\) for \(n=1\) and \(q^{11}(2q^4+q-2)\) for \(n=2\).

## Verification
Run `python3 verify.py` using Python's standard library. The script tests the original Rota--Baxter identity directly on **all** \(3\times3\) linear maps over \(\mathbb F_2\) and \(\mathbb F_3\), then tests **all** \(4\times4\) matrices over \(\mathbb F_2\) in both central-scalar fibers, including the shifted-symplectic equivalence. It obtains \(64\) and \(729\) operators for \(n=1\), and the \(n=2,q=2\) split \(3376+720\), multiplied by \(16\) arbitrary central functionals to give \(65536\). It separately verifies the special-fiber witness has nonisotropic row space. These finite checks supplement, but do not replace, the all-dimensional proof.

## Relationship to prior work
Gao--Liu--Bai--Jing (2014, arXiv:1407.3159) developed weight-zero Rota--Baxter classification for Witt/Virasoro Lie algebras, motivating the operator perspective, but those are not finite Heisenberg algebras. Ji--Hua (2018, Theorem 3.1) explicitly classify the **three-dimensional** Heisenberg case; therefore the \(n=1\) classification is not claimed as new. Rathee (2024, Section 4) treats **weight-one** operators in that same three-dimensional setting. These results do not entail the higher-dimensional two-component geometry, dimension crossover, or all-rank finite-field formula. Symplectic-monoid language partially describes the closure of the nonzero-scalar branch; the exceptional special branch contains matrices violating the dual symplectic identity, so identifying it with that closure would miss an entire component. The standard isotropic-image count is acknowledged as a building block, not itself a novelty claim.

## Limitations
The assertions address the reduced variety, not its scheme structure or intersection multiplicities. The component descriptions do not resolve orbit stratifications. A bounded comparison of accessible literature, including earlier symplectic-matrix theory, does not establish absolute first-publication priority. Results on distinct Heisenberg superalgebras may use related techniques but were not established to imply the theorem.

## References
1. X. Gao, M. Liu, C. Bai, N. Jing, *Rota-Baxter operators on Witt and Virasoro algebras*, arXiv:1407.3159 (first posted 2014-07-11), Sections 1--3. https://arxiv.org/abs/1407.3159
2. G. Ji, X. Hua, *Rota-Baxter operators of 3-dimensional Heisenberg Lie algebra*, Korean Journal of Mathematics 26 (2018), 53--60, Theorem 3.1. https://doi.org/10.11568/kjm.2018.26.1.53
3. N. Rathee, *Rota-Baxter operators and skew left brace structures over Heisenberg Group*, arXiv:2402.15428 (first posted 2024-02-23), Section 4. https://arxiv.org/abs/2402.15428
