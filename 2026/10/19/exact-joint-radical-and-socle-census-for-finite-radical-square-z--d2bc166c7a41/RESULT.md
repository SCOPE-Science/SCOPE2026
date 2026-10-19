# Exact joint radical-and-socle census for finite radical-square-zero loop modules

## Finding
Let \(q\) be a prime power, \(n\ge1\), and \(k\ge2\). Consider ordered tuples of matrices
\[
\mathcal Z_{n,k}(q)=\{(X_1,\ldots,X_k)\in M_n(\mathbb F_q)^k: X_iX_j=0\text{ for every }1\le i,j\le k\}.
\]
Define their joint image \(U=\sum_i\operatorname{im}X_i\) and common kernel \(K=\bigcap_i\ker X_i\), and let \(r=\dim U\) and \(t=n-\dim K\). Write \({a\brack b}_q\) for a Gaussian binomial coefficient and set
\[
F_{r,t,k}(q)=\sum_{a=0}^{r}(-1)^{r-a}q^{\binom{r-a}{2}}{r\brack a}_q\prod_{j=0}^{t-1}(q^{ka}-q^j).
\]
The empty product is \(1\). Then the number of tuples with joint image dimension \(r\) and common-kernel codimension \(t\) is exactly
\[
\boxed{N_{n,k}(r,t;q)={n\brack r}_q{n-r\brack t}_q F_{r,t,k}(q)}
\]
for \(r,t\ge0\) and \(r+t\le n\), and is zero outside this range. In particular, the total number of such tuples equals \(\sum_{r+t\le n}N_{n,k}(r,t;q)\), and
\[
N_{n,k}(r,t;q)=N_{n,k}(t,r;q).
\]
For the local algebra \(\Lambda_{k,q}=\mathbb F_q\langle x_1,\ldots,x_k\rangle/(x_ix_j:1\le i,j\le k)\), these are the labeled \(n\)-dimensional representations. Their radical \(JM\) has dimension \(r\) and their socle has dimension \(n-t\).

## Assumptions and scope
All vector spaces and matrices are over the finite field \(\mathbb F_q\). The \(k\) endomorphisms are **ordered**, and all products including squares vanish. All labeled representations are counted separately, even if they are isomorphic under simultaneous conjugation; there is no division by \(\operatorname{GL}_n(\mathbb F_q)\). The result is valid for every prime power and all specified dimensions. For the zero tuple, \((r,t)=(0,0)\) and the count is \(1\). For nonzero tuples both dimensions are positive.

## Proof
1. **Canonical flag.** The relations \(X_iX_j=0\) imply \(X_i(U)=0\) for each \(i\), so \(U\subseteq K\) and necessarily \(r+t\le n\). Conversely, for any subspaces \(U\subseteq K\subseteq V=\mathbb F_q^n\), maps \(X_i:V\to V\) with \(\operatorname{im}X_i\subseteq U\) and \(K\subseteq\ker X_i\) satisfy all product-zero relations, because \(U\subseteq K\). Such maps correspond uniquely to \(k\) maps \(f_i:W=V/K\to U\).

2. **Exactness conditions.** These maps have joint image exactly \(U\) precisely when \(\sum_i\operatorname{im}f_i=U\). Their common kernel is exactly \(K\) precisely when \(\bigcap_i\ker f_i=0\) inside \(W\). The latter condition means the vertical map \(W\to U^{\oplus k}\), \(w\mapsto(f_1(w),\ldots,f_k(w))\), is injective. The domain has dimension \(t\).

3. **Möbius count at a fixed flag.** For any subspace \(A\le U\) of dimension \(a\), the number of \(k\)-tuples \(W\to A\) with zero common kernel equals the number of injections \(W\hookrightarrow A^k\), namely \(\prod_{j=0}^{t-1}(q^{ka}-q^j)\). To require that their images also span all of \(U\), apply Möbius inversion over the lattice of subspaces \(A\le U\). The Möbius value for a codimension \(d\) inclusion is \((-1)^dq^{\binom d2}\), and there are \({r\brack a}_q\) subspaces of dimension \(a\). This gives precisely \(F_{r,t,k}(q)\). The case \(t=0\) is correctly handled by the empty product and cancellation, with only the zero tuple remaining.

4. **Count flags.** There are \({n\brack r}_q\) choices of \(U\) and, for each \(U\), exactly \({n-r\brack t}_q\) choices of \(K\) with \(U\subseteq K\) and codimension \(t\). Every tuple has a unique pair \((U,K)\). Multiplication gives the asserted formula without multiplicities.

5. **Duality.** Simultaneously transposing all \(X_i\) reverses every zero product, preserves the defining relations, and exchanges the dimension of the joint image with the codimension of the common kernel. Indeed the image of the joint transposes is the annihilator of \(K\), and their common kernel is the annihilator of \(U\). This gives the stated symmetry of the joint distribution.

These five arguments use no classification of indecomposable representations and no restriction on field characteristic.

## Verification
The included standalone `verify.py` uses finite-field Gaussian elimination and enumerates ordered matrix tuples directly, testing \(X_iX_j=0\) for every ordered pair. It computes the joint horizontal rank and the common-kernel codimension as an independent stacked-matrix rank. Direct exhaustive checks agree with the formula for \((n,k,q)=(2,2,2),(2,3,2),(3,2,2),(2,2,3)\): totals respectively \(10,22,148,33\). In the three-dimensional binary-pair case the four nonzero strata are \((r,t)=(0,0):1,(1,1):63,(1,2):42,(2,1):42\). Further arithmetic tests verify nonnegativity and transpose symmetry for \(1\le n\le6\), \(k\in\{2,3,4\}\), and \(q\in\{2,3,4,5\}\). Exhaustive tests are finite checks; the all-parameter theorem follows from the proof.

## Relationship to prior work
Kinser and Lőrincz, *Representation varieties of algebras with nodes* (arXiv:1810.10997, original 2018 version), analyze representation varieties, node splitting, and irreducible-component geometry of radical-square-zero algebras; their Proposition 3.5 gives a geometric bundle isomorphism of single-rank strata and Theorem 3.19 classifies irreducible components, but the paper does not state an exact joint finite-field cardinality for radical and socle dimensions. Bleher, Chinburg, and Huisgen-Zimmermann, *The geometry of finite dimensional algebras with vanishing radical square* (arXiv:1407.3045), analyze the same module-variety setting over algebraically closed fields and provide structural rank and top/socle information. Their component classifications are not being claimed as new. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity* (arXiv:2110.15566), counts pairs satisfying \(AB=BA=0\), and nilpotent such pairs; this is broader in individual nilpotency indices but restricted to pairs and does not give the all-products-zero joint \((r,t)\) distribution for arbitrary \(k\). Fulman and Guralnick (arXiv:2111.09433) independently derive Huang's pair enumeration via partition measures.

The present statement is the exact finite-field two-rank *arithmetic* refinement, not a new geometric component classification. The elementary flag and Möbius method makes the refinement explicit; the existence of earlier work describing the strata means that the claimed contribution is specifically the complete closed enumerator and joint distribution.

## Limitations
This counts **labeled** representations only, not simultaneous-conjugacy classes, indecomposable isomorphism classes, or module automorphism groups. It gives no closed infinite-product generating function over dimension and makes no claim to improve the geometric component or singularity theorems cited above. A differently formulated point-count or Hall-polynomial identity in unindexed literature could subsume the arithmetic refinement; no independence or external validation is claimed. The packaged exhaustive checks cover finite prime fields at small sizes and do not establish all-characteristic validity without the written proof.

## References
- Ryan Kinser and András C. Lőrincz, *Representation varieties of algebras with nodes*, arXiv:1810.10997, initial release 2018-10-25, Sections 1.2, 3.4 and Theorem 3.19. https://arxiv.org/abs/1810.10997
- Frauke M. Bleher, Ted Chinburg and Birge Huisgen-Zimmermann, *The geometry of finite dimensional algebras with vanishing radical square*, arXiv:1407.3045, 2014, Sections 3–4. https://arxiv.org/abs/1407.3045
- Yifeng Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566, 2021, Sections 1 and 3.1. https://arxiv.org/abs/2110.15566
- Jason Fulman and Robert Guralnick, *Cohen Lenstra Partitions and Mutually Annihilating Matrices over a Finite Field*, arXiv:2111.09433, 2021. https://arxiv.org/abs/2111.09433
