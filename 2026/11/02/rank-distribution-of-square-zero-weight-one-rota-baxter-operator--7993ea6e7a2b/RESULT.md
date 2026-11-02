# Rank distribution of square-zero weight-one Rota–Baxter operators on finite Heisenberg Lie algebras

## Finding

Let \(q\) be any prime power, \(n\ge1\), and let \(H=V\oplus\mathbb F_q z\) be the \((2n+1)\)-dimensional Heisenberg Lie algebra, with \([v,w]=\omega(v,w)z\) for a nondegenerate alternating form \(\omega\) on \(V\). Define \(\mathcal S_{n,q}\) to be the set of linear maps \(R:H\to H\) that are simultaneously **weight-one Rota–Baxter operators and square-zero maps**, \(R^2=0\). Their complete rank enumerator is
\[
\boxed{\displaystyle
P_{n,q}(t)=\sum_{R\in\mathcal S_{n,q}}t^{\operatorname{rank}R}
=\sum_{r=0}^{n} I_{n,r}\,S_{n,r}
\left(q^r t^r+(q^{2n-r}-q^r)t^{r+1}\right),}
\]
where
\[
I_{n,r}=\prod_{i=0}^{r-1}\frac{q^{2(n-i)}-1}{q^{r-i}-1},\qquad
S_{n,r}=\prod_{i=0}^{r-1}(q^{2n-r}-q^i).
\]
Empty products equal one. In particular, \(\#\mathcal S_{n,q}=P_{n,q}(1)=\sum_{r=0}^{n}I_{n,r}S_{n,r}q^{2n-r}\). All these statements hold in every characteristic, including characteristic two.

The **induced horizontal rank** \(\rho(R)=\operatorname{rank}(R\bmod\mathbb F_qz)\) also has a sharp arithmetic concentration law. Choose \(R\) uniformly from \(\mathcal S_{n,q}\), keep \(n\) fixed, and let \(q\) tend to infinity through prime powers. Set \(r_0=(4n+2)/5\). If \(n\not\equiv2\pmod5\), then \(\rho(R)\) tends in probability to \(\lfloor r_0\rfloor\). If \(n\equiv2\pmod5\), then the two ranks \(r_0-1\) and \(r_0\) each receive limiting probability \(1/2\), and all other ranks have limiting probability zero. Thus the rank transition occurs precisely at generator multiplicities \(n\equiv2\pmod5\).

For example, the exact full rank enumerator for the five-dimensional Heisenberg algebra over \(\mathbb F_2\) is
\[
P_{2,2}(t)=1+225t+990t^2.
\]

## Assumptions and scope

The Lie algebra is finite dimensional over \(\mathbb F_q\) with center \(\mathbb F_qz\), and the weight-one convention is
\[
[R(x),R(y)]=R\bigl([R(x),y]+[x,R(y)]+[x,y]\bigr),\qquad\forall x,y\in H.
\]
The restriction \(R^2=0\) means square-zero as a **linear map**, not that its Lie image is automatically zero. Rank is ordinary linear-map rank; \(\rho(R)\) is the rank of the map induced by \(R\) on \(H/\mathbb F_qz\). The center-preservation property needed to define it is proved below. The result concerns labeled operators, not equivalence classes under automorphisms. Nothing is assumed about the characteristic.

## Proof

**Step 1: Every weight-one operator preserves the center.** Write \(R(z)=u+cz\), \(R(v)=Av+\phi(v)z\), where \(u\in V\), \(c\in\mathbb F_q\), \(A\in\operatorname{End}(V)\), and \(\phi\in V^*\). The Rota–Baxter equation with \(x=z\), \(y=v\) gives
\[
\omega(u,Av)z=\omega(u,v)(u+cz).
\]
If \(u\ne0\), nondegeneracy lets us choose \(v\) with \(\omega(u,v)\ne0\), giving a contradiction in the noncentral component. Thus \(u=0\). For \(v,w\in V\), the same identity reduces exactly to
\[
\omega(Av,Aw)=c\bigl(\omega(Av,w)+\omega(v,Aw)+\omega(v,w)\bigr).
\]
In terms of any symplectic Gram matrix \(J\), this is \(A^{\mathsf T}JA=c(A^{\mathsf T}J+JA+J)\). The linear functional \(\phi\) is unrestricted by the Rota–Baxter identity.

**Step 2: Incorporate square-zero.** The equation \(R^2(z)=0\) says \(c^2=0\), hence \(c=0\) over a field. Thus the horizontal identity becomes \(A^{\mathsf T}JA=0\): the image \(U=\operatorname{im}A\) is totally isotropic. Furthermore,
\[
R^2(v)=A^2v+\phi(Av)z.
\]
Consequently, \(R^2=0\) is equivalent to \(A^2=0\) and \(\phi|_U=0\), in addition to \(U\) being isotropic. Conversely, every choice with these properties satisfies both defining identities: the bracket of images vanishes since \(U\) is isotropic, and the entire argument of \(R\) in the weight-one equation is a multiple of \(z\), which \(R\) kills. Hence the complete normal form is
\[
R(z)=0,\qquad R(v)=Av+\phi(v)z,\qquad
U=\operatorname{im}A\text{ isotropic},\quad U\subseteq\ker A,\quad\phi(U)=0.
\]
No division by \(2\) was used, so this works in characteristic two.

**Step 3: Count a prescribed horizontal rank.** Put \(r=\dim U\). Since \(U\) is totally isotropic, \(0\le r\le n\). The number of isotropic \(r\)-subspaces of a symplectic \(2n\)-space is
\[
I_{n,r}=\prod_{i=0}^{r-1}\frac{q^{2(n-i)}-1}{q^{r-i}-1}.
\]
For completeness, after an independent isotropic \(i\)-frame spanning \(W\), the next vector must lie in \(W^\perp\setminus W\), giving \(q^{2n-i}-q^i\) choices. Divide the number of frames \(\prod_{i=0}^{r-1}(q^{2n-i}-q^i)\) by \(|\operatorname{GL}_r(q)|=\prod_{i=0}^{r-1}(q^r-q^i)\), yielding the displayed formula. For each fixed \(U\), the square-zero condition \(U\subseteq\ker A\) means that \(A\) is exactly a surjective map \(V/U\twoheadrightarrow U\). Since \(\dim(V/U)=2n-r\), their number is
\[
S_{n,r}=\prod_{i=0}^{r-1}(q^{2n-r}-q^i).
\]
The functional \(\phi\) must vanish on \(U\), and there are exactly \(q^{2n-r}\) such functionals. This proves the count by horizontal rank and the total obtained by setting \(t=1\).

**Step 4: Refine to the actual rank of \(R\).** For fixed \(A\) of horizontal rank \(r\), write \(K=\ker A\). Because \(U\subseteq K\), the requirement \(\phi(U)=0\) still allows all functionals in \(U^\perp\subseteq V^*\) (here \(\perp\) denotes annihilator, not the symplectic orthogonal). The image of \(R\) has dimension \(r\) if and only if \(\phi\) vanishes on \(K\), because otherwise some vector in \(K\) maps to a nonzero multiple of \(z\) and adds an independent central direction. There are precisely \(q^{\dim(V/K)}=q^r\) functionals annihilating \(K\); the other \(q^{2n-r}-q^r\) give rank \(r+1\). Multiply by \(I_{n,r}S_{n,r}\) and sum to establish the displayed polynomial \(P_{n,q}(t)\). Note that \(r=n\) forces \(K=U\), so the coefficient of \(t^{n+1}\) vanishes, as required for a square-zero map on a \((2n+1)\)-space.

**Step 5: Derive the rank-concentration transition.** For fixed \(n\), the rank-\(r\) horizontal stratum has size \(I_{n,r}S_{n,r}q^{2n-r}\) with leading coefficient one as a polynomial/rational polynomial in \(q\). Its leading degree is
\[
F_n(r)=2n+\frac{r(8n-5r-1)}2.
\]
For \(1\le r\le n\), direct subtraction gives \(F_n(r)-F_n(r-1)=4n+2-5r\). Hence there is a unique dominant rank \(\lfloor(4n+2)/5\rfloor\) unless \((4n+2)/5\) is an integer, precisely when \(n\equiv2\pmod5\). In that case the two adjacent ranks \(r_0-1,r_0\) have equal strictly maximal degree and leading coefficient one. Their limiting probabilities are therefore each \(1/2\); every other stratum is lower order. This proves the stated limit law.

## Verification

The included standalone `verify.py` is executable with Python 3 and no dependencies. It independently constructs arithmetic in \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), enumerates **all** linear maps of the three-dimensional Heisenberg algebra, tests both the Rota–Baxter equation on all basis pairs and \(R^2=0\) directly, and Gaussian-eliminates to obtain ranks. The observed polynomials are \(1+9t\), \(1+32t\), and \(1+75t\). In dimension five over \(\mathbb F_2\), it enumerates all \(2^{16}\) horizontal matrices and all relevant central coefficients, independently verifying \(1+225t+990t^2\). The finite tests are not claimed to prove the infinite family; Steps 1–5 do.

## Relationship to prior work

The three-dimensional Heisenberg weight-one classification is known, through Ji–Hua [1] and Rathee [2]. Ji–Hua use an opposite sign convention for the weight; Rathee [2, Remark 4.4] explains conversion. These papers supply relevant operator classification, but Theorem 3.2 of [1] and Theorems 4.1/4.3 of [2] do not enumerate square-zero operators by rank on **every** higher-dimensional finite Heisenberg algebra or establish the modular-five asymptotic split. Related general investigations of nilpotency in Rota–Baxter algebras [3] concern unital associative algebras and do not imply the Lie-algebra rank formula.

The counting of isotropic subspaces and ordinary surjective matrices is standard and is used here without a novelty claim. The asserted result is the combined, characteristic-independent square-zero rank distribution and its nontrivial two-rank concentration condition, including the difference between horizontal and full rank.

## Limitations

The theorem is restricted to square-zero weight-one linear Rota–Baxter operators, not all operators of this weight and not other nilpotency indices. It gives rank counts, not conjugacy classes or descriptions of induced post-Lie isomorphism classes. The asymptotic keeps \(n\) fixed while \(q\to\infty\); it is not a large-\(n\) statement. Earlier equivalent computations of square-zero symplectic-image maps are a possible priority risk; the absence of a matching search result is not proof of global novelty. A 2016 primary paper about five-dimensional Heisenberg **Lie superalgebras** [4] was identified bibliographically but not read in full. Independent mathematical audit has not been performed.

## References

[1] G. Ji and X. Hua, *Rota-Baxter operators of 3-dimensional Heisenberg Lie algebra*, Korean Journal of Mathematics **26** (2018), 53–60, DOI 10.11568/kjm.2018.26.1.53, first public date March 30, 2018. Full text: https://kkms.org/index.php/kjm/article/download/594/393/2347.

[2] N. Rathee, *Rota–Baxter operators and skew left brace structures over Heisenberg Group*, arXiv:2402.15428 (February 23, 2024), Sections 4–5. Full text: https://ar5iv.labs.arxiv.org/html/2402.15428.

[3] V. Gubarev, *Rota–Baxter Operators on Unital Algebras*, Moscow Mathematical Journal **21** (2021), 325–364; the published abstract discusses nilpotent operators and the Rota–Baxter index on unital associative algebras.

[4] S. Q. Lv and W. D. Liu, *Rota-Baxter Operators on Heisenberg Lie Superalgebras of Dimension Five*, Journal of Mathematics in Practice and Theory **46**(20) (2016), 248–258; bibliographic reference in [1], full text unavailable in this review.
