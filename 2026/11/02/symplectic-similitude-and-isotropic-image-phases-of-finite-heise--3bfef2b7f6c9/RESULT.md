# Symplectic-similitude and isotropic-image phases of finite Heisenberg Rota–Baxter operators

## Finding
Fix an odd prime \(p\), an integer \(n\geq1\), a \(2n\)-dimensional symplectic vector space \((V,\omega)\) over \(\mathbb F_p\), and the exponent-\(p\) Heisenberg group \(H=V\times\mathbb F_p\) with
\[
(v,z)(w,t)=(v+w,z+t+\tfrac12\omega(v,w)).
\]
A weight-one **group** Rota–Baxter operator is a map \(B:H\to H\) satisfying
\[
B(g)B(h)=B(gB(g)hB(g)^{-1}) \quad\text{for all }g,h\in H.
\]
Consider the natural **center-affine, quotient-linear family** of all maps
\[
B_{T,\mu,F}(v,z)=(Tv,\mu z+F(v)),
\]
where \(T:V\to V\) is linear, \(\mu\in\mathbb F_p\), and \(F:V\to\mathbb F_p\) is initially an arbitrary function. No classification of all group Rota–Baxter operators is claimed.

**Theorem.** Such a map is a Rota–Baxter operator **if and only if** there is a unique linear form \(\ell\in V^*\) such that
\[
F(v)=\frac\mu2\omega(v,Tv)+\ell(v),
\qquad
\omega((T-\mu I)v,(T-\mu I)w)=\mu(\mu+1)\omega(v,w)
\]
for all \(v,w\in V\).

Define
\[
L_{n,r}(p)={n\brack r}_p\prod_{j=0}^{r-1}(p^{n-j}+1),\quad
M_n(p)=\sum_{r=0}^n L_{n,r}(p)\prod_{i=0}^{r-1}(p^{2n}-p^i),
\]
with empty products equal to one, where \({n\brack r}_p\) is the number of \(r\)-subspaces of \(\mathbb F_p^n\). Also put
\[
S_n(p)=p^{n^2}\prod_{j=1}^n(p^{2j}-1).
\]
The **exact number of operators in this family** is
\[
\boxed{p^{2n}\big((p-2)S_n(p)+2M_n(p)\big).}
\]
For each fixed \(\mu\notin\{0,-1\}\), there are \(p^{2n}S_n(p)\) such operators; their map \(T-\mu I\) is invertible. For each \(\mu\in\{0,-1\}\), there are \(p^{2n}M_n(p)\) operators and the rank of \(T-\mu I\) is at most \(n\). More precisely, the number in either exceptional phase with rank exactly \(r\), for \(0\le r\le n\), is
\[
\boxed{p^{2n}L_{n,r}(p)\prod_{i=0}^{r-1}(p^{2n}-p^i).}
\]
Thus the quotient-linear part has a strict full-rank versus isotropic-image transition as the central scalar crosses \(0\) or \(-1\).

## Assumptions and scope
Throughout \(p\) is an **odd prime** (not an arbitrary prime power), \(n\) is any positive integer, and \(\tfrac12\) is the inverse of two in \(\mathbb F_p\). The model is the exponent-\(p\) extraspecial group of order \(p^{2n+1}\). The maps under classification are required to have quotient component \(T\) linear and central dependence of the displayed affine form; within that family \(F\) is unrestricted a priori. No claim is made that every Rota–Baxter operator on \(H\) belongs to this family. The lower-dimensional case \(n=1\) is an included consistency and normalization check, **not** claimed to be a new classification of the Heisenberg group of order \(p^3\).

## Proof
**1. Reduction to an additive functional equation.** In the group model,
\[
(a,s)(w,t)(a,s)^{-1}=(w,t+\omega(a,w)).
\]
For \(g=(v,z)\) and \(h=(w,t)\), the quotient coordinates of the Rota–Baxter identity agree because \(T\) is linear. Its central coordinates agree precisely when
\[
F(v+w)-F(v)-F(w)
=\tfrac12\omega(Tv,Tw)-\tfrac\mu2\omega(v,w)-\mu\omega(Tv,w). \tag{1}
\]
Here the terms containing \(z,t\) cancel. Because the left side is symmetric in \(v,w\), subtracting its version with \(v,w\) interchanged gives
\[
\omega(Tv,Tw)=\mu\big(\omega(v,w)+\omega(Tv,w)+\omega(v,Tw)\big). \tag{2}
\]
Writing \(S=T-\mu I\) and expanding its symplectic pairing, (2) is equivalent to
\[
\omega(Sv,Sw)=\mu(\mu+1)\omega(v,w). \tag{3}
\]

**2. Recovering all central functions.** Under (2), the right-hand side of (1) becomes
\[
\tfrac\mu2\big(\omega(v,Tw)+\omega(w,Tv)\big).
\]
The function \(Q(v)=\tfrac\mu2\omega(v,Tv)\) has this exact polarization. Consequently \(F-Q\) is additive on the additive group of \(V\), so it is necessarily \(\mathbb F_p\)-linear. Conversely, every \(F=Q+\ell\), with (3), satisfies (1) and hence the original group identity. Uniqueness of \(\ell\) is immediate. There are precisely \(p^{2n}\) choices of \(\ell\) for each admissible pair \((T,\mu)\); no function solutions were discarded.

**3. The nondegenerate phases.** If \(\mu\notin\{0,-1\}\), then \(c=\mu(\mu+1)\ne0\) and (3) says that \(S\) lies in the symplectic similitude group with multiplier \(c\). Such \(S\) is invertible by nondegeneracy of \(\omega\). In a symplectic basis, the diagonal map fixing the first Lagrangian and multiplying the complementary Lagrangian by \(c\) has multiplier \(c\). Thus the multiplier map from \(\operatorname{GSp}_{2n}(p)\) is surjective, each nonzero multiplier fiber is a coset of \(\operatorname{Sp}_{2n}(p)\), and its cardinality is the familiar \(S_n(p)\) displayed above.

**4. Exceptional phases and every rank coefficient.** If \(\mu\in\{0,-1\}\), (3) becomes \(\omega(Sv,Sw)=0\) for all \(v,w\). This says exactly that \(W=\operatorname{im}S\) is totally isotropic, hence \(0\le\operatorname{rank}S\le n\). There are
\[
L_{n,r}(p)={n\brack r}_p\prod_{j=0}^{r-1}(p^{n-j}+1)
\]
choices of an \(r\)-dimensional totally isotropic subspace \(W\) of a \(2n\)-dimensional symplectic space. For completeness, this count follows by counting ordered independent isotropic \(r\)-tuples: after choosing an isotropic \(i\)-space \(U\), the next vector can be any element of \(U^\perp\setminus U\), giving \(p^{2n-i}-p^i\) possibilities. Divide the product of these quantities for \(i=0,\dots,r-1\) by the number \(\prod_{i=0}^{r-1}(p^r-p^i)\) of ordered bases of a fixed \(W\). Elementary cancellation gives the displayed Gaussian-binomial product. For fixed \(W\), a linear map \(S:V\twoheadrightarrow W\) is specified by \(r\) independent linear functionals in \(V^*\), giving exactly \(\prod_{i=0}^{r-1}(p^{2n}-p^i)\) choices. Every \(S\) has exactly one image \(W\), so there is no overlap. Sum over \(r\), over the two exceptional \(\mu\)'s, and over \(\ell\in V^*\) to get the theorem. \(\square\)

## Verification
The self-contained standard-library script `verify.py` reconstructs the group multiplication from the symplectic form and checks the Rota–Baxter equation **from its definition**, independently of equations (1)–(3). It exhausts all \(3^4\) quotient matrices and all three scalars in dimension two, testing every pair of elements of the \(27\)-element group. It separately checks all \(5^4\) quotient matrices in dimension two by the independent matrix pairing test, and tests admissible plus inadmissible matrices in dimension four by sampled group identities. Its observed per-scalar counts are \((33,24,33)\) for \(p=3,n=1\) and \((145,120,120,120,145)\) for \(p=5,n=1\), before the \(p^{2n}\) linear-functional factor. The corresponding complete family sizes are \(810\) and \(16{,}250\). Dimension-four checks also passed; these sampled tests cannot prove the unrestricted infinite-dimensional formula. Execute with `python3 verify.py`; successful output ends with `VERIFY_OK`. The all-\(n\) result follows from the proof, not from finite computations.

## Relationship to prior work
Savelyev, *Rota—Baxter operators on extraspecial groups* (first publicly submitted 2026-08-28, arXiv:2608.28291), proves center preservation for general extraspecial groups and completely classifies operators on two extraspecial groups of order \(p^3\). The present theorem does **not** claim that center-preservation principle or the \(n=1\) classification as new; it solves an explicit natural center-affine/quotient-linear family uniformly in every higher symplectic rank and gives its all-rank counting polynomial. Rathee (arXiv:2402.15428) studies the three-dimensional Heisenberg Lie algebra and induced group/brace structures. Guo–Lang–Sheng (arXiv:2009.03492) supplies the group Rota–Baxter framework. Neither the inspected texts nor targeted mathematical searches supplied the present higher-rank count or its singular-versus-similitude phase formula. This is a best-knowledge priority assessment, not a proof that no equivalent earlier theorem exists; general Lie-algebra integration and classical symplectic-matrix results may provide routes to portions of the computation.

## Limitations
Only the explicitly defined linear-quotient, central-affine family is classified, over an **odd prime field**. It may be a proper subset of all group Rota–Baxter operators. The formula does not count isomorphism classes or conjugacy orbits of such operators, nor does it address extraspecial groups of exponent \(p^2\), characteristic two, or nonprime scalar fields. The symplectic group order and isotropic-subspace count are standard ingredients, not asserted to be new. Independent expert verification and a comprehensive historical-priority audit remain outstanding.

## References
1. A. Savelyev, *Rota—Baxter operators on extraspecial groups*, arXiv:2608.28291 (first version 2026-08-28), https://arxiv.org/abs/2608.28291.
2. N. Rathee, *Rota–Baxter operators and skew left brace structures over Heisenberg group*, arXiv:2402.15428 (2024), https://arxiv.org/abs/2402.15428.
3. L. Guo, H. Lang and Y. Sheng, *Integration and geometrization of Rota–Baxter Lie algebras*, arXiv:2009.03492 (2020), https://arxiv.org/abs/2009.03492.
4. J. Jiang, Y. Sheng and C. Zhu, *Lie theory and cohomology of relative Rota–Baxter operators*, Journal of the London Mathematical Society 109 (2024), https://doi.org/10.1112/jlms.12863.
