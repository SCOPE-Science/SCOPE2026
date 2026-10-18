# Joint fixed-point and image-size census of abelian endomorphisms of finite Heisenberg groups

## Finding

Let \(p\) be an odd prime and \(n\ge 1\). Every group endomorphism of the finite Heisenberg group \(H_n(p)\) with abelian image is classified by its projected rank \(r\), its fixed-point dimension \(s\), and the logarithmic size \(k\) of its image. The number of such endomorphisms in each stratum is exactly
\[
M_{n,p}(r,s,k)=\alpha_{n,r}(p)X_{n,r,s}(p)
\begin{cases}
p^r,&k=r,\\
p^{2n}-p^r,&k=r+1,\\
0,&\text{otherwise},
\end{cases}
\]
where \(0\le s\le r\le n\),
\[
\alpha_{n,r}(p)=\prod_{j=0}^{r-1}\frac{p^{2n-2j}-1}{p^{r-j}-1},
\quad
X_{n,r,s}(p)=\sum_{t=s}^{r}(-1)^{t-s}
 p^{\binom{t-s}{2}}{t\brack s}_p{r\brack t}_p
 p^{t(2n-t)}\prod_{j=0}^{r-t-1}(p^{2n-t}-p^j).
\]
The Gaussian binomial coefficient \({a\brack b}_p\) counts \(b\)-dimensional subspaces of \(\mathbb F_p^a\); empty products equal one. For each such endomorphism, its fixed-point subgroup has exactly \(p^s\) elements and its image exactly \(p^k\) elements. No other strata occur.

In particular, the exact number with only the identity fixed and with abelian image is
\[
F_{n,p}=p^{2n}\sum_{r=0}^{n}\alpha_{n,r}(p)X_{n,r,0}(p).
\]
For \(n=1\), this simplifies to \(F_{1,p}=p^5-2p^3\). For \(n=2,p=3\), it gives \(F_{2,3}=12{,}078{,}801\). These are **labelled endomorphism counts**, not counts up to automorphism or counts of inequivalent Yang--Baxter solutions.

## Assumptions and scope

Fix \(p\) odd, \(n\ge1\), \(N=2n\), and an \(N\)-dimensional nondegenerate symplectic \(\mathbb F_p\)-space \((V,\omega)\). Define \(G=H_n(p)=V\times\mathbb F_p\) with group multiplication
\[
(v,z)(w,t)=(v+w,z+t+\tfrac12\omega(v,w)).
\]
The center and derived subgroup coincide with \(\{(0,z):z\in\mathbb F_p\}\). An endomorphism is *abelian-image* when the subgroup it maps onto is abelian. Write \(r=\operatorname{rank}A\), \(s=\dim\ker(I-A)\), and \(|\operatorname{im}\psi|=p^k\) for the associated projected linear map \(A\), which is uniquely defined below. The characteristic-two case and groups of higher prime-power exponent are **outside** this theorem.

## Proof

**1. Parametrization.** An endomorphism \(\psi:G\to G\) with abelian image kills \([G,G]\), so it factors through \(G/[G,G]\cong V\). Since \(V\) is an elementary abelian \(p\)-group, necessarily
\[
\psi(v,z)=(Av,\ell(v))
\]
for \(\mathbb F_p\)-linear maps \(A:V\to V\) and \(\ell:V\to\mathbb F_p\). The images of two vectors commute precisely when \(\omega(Av,Aw)=0\). Thus \(\psi\) is a homomorphism with abelian image if and only if \(L=\operatorname{im}A\) is totally isotropic. Conversely, every pair \((A,\ell)\) satisfying this condition defines such an endomorphism: the group-law cross-term vanishes on \(L\). This correspondence is injective and exhaustive.

**2. Isotropic image spaces.** The number of totally isotropic \(r\)-spaces \(L\subseteq V\) is \(\alpha_{n,r}(p)\). Indeed, ordered isotropic independent vectors can be selected in
\[
\prod_{i=0}^{r-1}(p^{2n-i}-p^i)
\]
ways, because the next vector lies in the orthogonal complement of the current isotropic span but not in that span. Divide by \(|\operatorname{GL}_r(\mathbb F_p)|=\prod_{i=0}^{r-1}(p^r-p^i)\). Cancelling powers of \(p\) yields the displayed product \(\alpha_{n,r}(p)\). Necessarily \(r\le n\).

**3. Surjective maps and fixed spaces.** Fix one isotropic \(r\)-space \(L\). A map \(A:V\twoheadrightarrow L\) has all its fixed vectors in \(L\). For any \(t\)-space \(T\le L\), let \(B_{n,r,t}(p)\) count surjective maps that restrict to the identity on \(T\). Such maps induce a surjection \(V/T\twoheadrightarrow L/T\), with
\[
\prod_{j=0}^{r-t-1}(p^{2n-t}-p^j)
\]
choices. Each induced map admits exactly \(p^{t(2n-t)}\) lifts with \(A|_T=I\): the arbitrary \(T\)-components of the images of a complement basis yield these choices. Hence
\[
B_{n,r,t}(p)=p^{t(2n-t)}\prod_{j=0}^{r-t-1}(p^{2n-t}-p^j).
\]
Let \(X_{n,r,s}(p)\) be the number of such surjections whose fixed space is exactly \(s\)-dimensional. Counting the pairs \((A,T)\) where \(T\le\operatorname{Fix}(A)\) has dimension \(t\), gives the triangular system
\[
{r\brack t}_p B_{n,r,t}(p)=\sum_{s=t}^{r}{s\brack t}_p X_{n,r,s}(p).
\]
Möbius inversion in the lattice of \(\mathbb F_p\)-subspaces, whose interval Möbius function at dimension gap \(u\) is \((-1)^u p^{\binom u2}\), gives precisely the expression for \(X_{n,r,s}(p)\) displayed in the Finding. The inversion therefore counts actual maps, not merely a formal signed sum. As a check, \(\sum_{s=0}^{r}X_{n,r,s}(p)=\prod_{j=0}^{r-1}(p^{2n}-p^j)\), the total number of surjections \(V\to L\).

**4. Central coefficients and image order.** For fixed \(A\) of rank \(r\), its group-image size is \(p^r\) exactly when \(\ell\) vanishes on \(\ker A\), equivalently when \(\ell\) factors through \(A\). Exactly \(p^r\) linear functionals have this property. The remaining \(p^{2n}-p^r\) have joint map \((A,\ell)\) of rank \(r+1\), hence image order \(p^{r+1}\). Meanwhile \((v,z)\) is fixed precisely when \(Av=v\) and \(z=\ell(v)\). There are thus \(p^s\) fixed points regardless of the choice of \(\ell\). Multiplying the independent choices of \(L\), \(A\), and \(\ell\) proves the complete formula. Summing the \(s=0\) strata proves the formula for \(F_{n,p}\).

For \(n=1\), \(\alpha_{1,1}(p)=p+1\) and \(X_{1,1,0}(p)=p^2-p-1\); together with the zero-rank contribution this yields \(F_{1,p}=p^2(1+(p+1)(p^2-p-1))=p^5-2p^3\). For \(n=2,p=3\), the image-rank multiplicities \(\alpha_{2,0}=1\), \(\alpha_{2,1}=40\), \(\alpha_{2,2}=40\) and fixed-point-free counts \(X_{2,0,0}=1\), \(X_{2,1,0}=53\), \(X_{2,2,0}=3675\) give \(81(1+40\cdot53+40\cdot3675)=12{,}078{,}801\).

## Verification

The included `check_heisenberg_abelian_endos.py` uses only Python's standard library. It independently enumerates all isotropic-image \(2\times2\) matrices over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), determining fixed-space dimensions by row reduction. For a fixed isotropic line and plane in dimension four, it enumerates all surjective matrices over \(\mathbb F_3\) and \(\mathbb F_5\) and compares their complete fixed-space distributions with \(X_{n,r,s}(p)\). It separately enumerates all isotropic planes in \(\mathbb F_3^4\) and checks a nonzero example directly against the Heisenberg multiplication law for all element pairs in the order-27 group. Execute `python3 check_heisenberg_abelian_endos.py`; the last line is `ALL_FPF_AB_IMAGE_COUNTS_PASSED`. Finite checks are supplementary; the unrestricted assertion follows from the preceding proof.

## Relationship to prior work

Kumar and Pradhan [1] establish the symplectic/isotropic-image parametrization and enumerate abelian-image endomorphisms by image rank (their Theorems 5.2--5.3). Those established results include the isotropic-space factor \(\alpha_{n,r}(p)\) and the **unrefined** count of surjections. The contribution here is the **joint fixed-point-size and total image-size distribution** (including an explicit subspace-lattice inversion and its fixed-point-free specialization), not the earlier unrefined result.

Koch, Stordy, and Truman [2] motivate fixed-point-free abelian endomorphisms by constructing Yang--Baxter/brace structures from them; no count of inequivalent braces or solutions is asserted here. Nejabati Zenouz [3] studies skew braces and Hopf--Galois structures of Heisenberg type, particularly small rank; that classification is different from an all-rank labelled endomorphism census. The related published result [4] concerns **fixed-point-free automorphisms** of a three-dimensional Heisenberg **Lie algebra**; in the nonabelian Heisenberg **group**, no automorphism can have abelian image. Its formula therefore does not imply this joint enumeration.

## Limitations

The formula counts labelled maps, not equivalence classes under conjugation, nor independently certified Yang--Baxter or Hopf--Galois structures. It requires odd characteristic and exponent \(p\). Known 2019 work covers unrefined abelian-image endomorphism counts and is not claimed as novel. Although source comparisons support a distinct finer distribution, an equivalent fixed-point stratification might appear in older semidirect-product, symplectic enumeration, or brace literature. The finite checks do not establish historical priority or replace the all-rank proof. Independent mathematical audit has not been performed.

## References

[1] S. Kumar and R. Pradhan, *On the Endomorphism Semigroups of Extra-special p-groups and Automorphism Orbits*, arXiv:1908.00331 (first posted 2019-08-01), https://arxiv.org/abs/1908.00331, especially Theorems 5.2--5.3.

[2] A. Koch, L. Stordy, and P. Truman, *Abelian fixed point free endomorphisms and the Yang--Baxter equation*, arXiv:2006.13196 (2020), https://arxiv.org/abs/2006.13196.

[3] K. Nejabati Zenouz, *Skew braces and Hopf--Galois structures of Heisenberg type*, arXiv:1804.01360 (2018), https://arxiv.org/abs/1804.01360.

[4] *Exact fixed-point-free automorphism count for the three-dimensional Heisenberg Lie algebra*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-fixed-point-free-automorphism-count-for-the-three-dimensio--17f0de4cb789.
