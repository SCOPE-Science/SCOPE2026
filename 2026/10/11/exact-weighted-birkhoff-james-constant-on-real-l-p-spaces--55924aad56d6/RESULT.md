# Exact weighted Birkhoff–James constant on real \(L^p\) spaces
## Finding
Let \((\Omega,\Sigma,\mu)\) be a measure space containing disjoint measurable sets \(A,B\) with
\[
0<\mu(A),\mu(B)<\infty.
\]
For \(1\le p\le\infty\) and \(0\le\lambda\le1\), write
\[
J^\perp_\lambda(L^p(\mu))
=
\sup_{\substack{x,y\in S_{L^p(\mu)}\\ x\perp_B y}}
\min\left\{
\|\lambda x+(1-\lambda)y\|_p,\,
\|\lambda x-(1-\lambda)y\|_p
\right\}.
\]
Then
\[
J^\perp_\lambda(L^p(\mu))
=
\begin{cases}
\bigl(\lambda^p+(1-\lambda)^p\bigr)^{1/p},
&1\le p\le2,\\[3pt]
\left(\frac{1+|2\lambda-1|^p}{2}\right)^{1/p},
&2\le p<\infty,\\[6pt]
1,&p=\infty.
\end{cases}
\]
The two finite-\(p\) formulas coincide at \(p=2\). The same formulas are the unrestricted weighted James suprema on these \(L^p\) spaces, so imposing Birkhoff--James orthogonality does not decrease the optimum.

For \(1\le p\le2\), normalized disjoint indicators attain the optimum. For \(2\le p<\infty\), a balanced two-piece Hanner pair attains it. The transition at \(p=2\) is therefore not only a change in the sharp formula but also a change in the natural extremal geometry.

## Assumptions and scope
The space is real. The measure space need only contain two disjoint measurable sets of finite positive measure. This hypothesis covers \(L^p[0,1]\), any non-atomic \(\sigma\)-finite \(L^p\) space of dimension at least two, and sequence spaces with at least two atoms, but the claim is stated as a measure-space theorem rather than as a sequence-space formula.

Birkhoff--James orthogonality means
\[
x\perp_B y
\quad\Longleftrightarrow\quad
\|x\|_p\le\|x+t y\|_p
\quad\text{for every }t\in\mathbb R.
\]
No uniqueness of maximizing pairs is asserted.

## Proof
Put \(m=1-\lambda\).

For \(1<p\le2\), let \(q=p/(p-1)\). Clarkson's inequality gives, for arbitrary unit vectors \(x,y\in L^p(\mu)\),
\[
\|\lambda x+m y\|_p^q+\|\lambda x-m y\|_p^q
\le
2\bigl(\lambda^p+m^p\bigr)^{q/p}.
\]
Hence
\[
\min\left\{
\|\lambda x+m y\|_p,\,
\|\lambda x-m y\|_p
\right\}
\le
\bigl(\lambda^p+m^p\bigr)^{1/p}.
\]
This upper bound is valid before imposing orthogonality. Choose
\[
e=\mu(A)^{-1/p}\mathbf 1_A,
\qquad
f=\mu(B)^{-1/p}\mathbf 1_B.
\]
Then \(e,f\) are disjoint unit vectors and
\[
\|e+t f\|_p^p=1+|t|^p\ge1,
\]
so \(e\perp_B f\). Moreover,
\[
\|\lambda e\pm m f\|_p^p=\lambda^p+m^p.
\]
Thus the upper bound is attained. At \(p=1\), the triangle inequality gives the upper bound \(1\), and the same disjoint pair has both weighted norms equal to \(\lambda+m=1\). This proves the first branch.

Now let \(2\le p<\infty\). Hanner's inequality gives, for arbitrary unit vectors \(x,y\),
\[
\|\lambda x+m y\|_p^p+\|\lambda x-m y\|_p^p
\le
(\lambda+m)^p+|\lambda-m|^p
=
1+|2\lambda-1|^p.
\]
Therefore
\[
\min\left\{
\|\lambda x+m y\|_p,\,
\|\lambda x-m y\|_p
\right\}
\le
\left(\frac{1+|2\lambda-1|^p}{2}\right)^{1/p}.
\]
Using the same disjoint unit vectors \(e,f\), define
\[
x=2^{-1/p}(e+f),
\qquad
y=2^{-1/p}(e-f).
\]
Both are unit vectors. Since \(1<p<\infty\), the \(L^p\) norm is smooth and the standard Birkhoff--James criterion gives
\[
x\perp_B y
\quad\Longleftrightarrow\quad
\int_\Omega |x|^{p-2}x\,y\,d\mu=0.
\]
The two disjoint pieces contribute equal quantities with opposite signs, so the integral vanishes. Finally,
\[
\lambda x+m y
=
2^{-1/p}\bigl(e+(2\lambda-1)f\bigr),
\]
and
\[
\lambda x-m y
=
2^{-1/p}\bigl((2\lambda-1)e+f\bigr).
\]
Both norms therefore have \(p\)-th power
\[
\frac{1+|2\lambda-1|^p}{2},
\]
which attains the Hanner upper bound.

For \(p=\infty\), the triangle inequality gives
\[
\|\lambda x\pm m y\|_\infty\le1
\]
for all unit \(x,y\). Let \(e=\mathbf 1_A\), \(f=\mathbf 1_B\), and set
\[
x=e+f,\qquad y=e-f.
\]
Then
\[
\|x+t y\|_\infty
=
\max\{|1+t|,|1-t|\}\ge1,
\]
so \(x\perp_B y\), while
\[
\|\lambda x\pm m y\|_\infty=1.
\]
Thus \(J^\perp_\lambda(L^\infty(\mu))=1\).

Every upper bound above was proved without the orthogonality restriction, while every sharp witness is Birkhoff--James orthogonal. Hence the weighted Birkhoff constant equals the unrestricted weighted James supremum throughout the stated class.

## Verification
The proof is symbolic. The only nontrivial external inequalities used are the classical Clarkson inequality on \(L^p\) for \(1<p\le2\) and Hanner's sharp inequality on \(L^p\) for \(2\le p<\infty\). The endpoint cases \(p=1\) and \(p=\infty\) are checked directly.

The Birkhoff--James witnesses are also checked directly: disjoint indicators give \(\|e+t f\|_p\ge1\), the balanced finite-\(p\) pair satisfies the smooth \(L^p\) orthogonality integral exactly, and the \(L^\infty\) pair satisfies the defining minimization inequality for every real \(t\). No finite experiment or numerical sample is used to establish any quantified statement.

## Relationship to prior work
Qi, Yin, Liu, and Li introduced \(J^\perp_\lambda\) in 2026. The accessible primary metadata and abstract establish the definition and scope of the new invariant. A detailed accessible review of that preprint reports, among its concrete examples, the lower bound
\[
J^\perp_\lambda(\ell_p^n)
\ge
\bigl(\lambda^p+(1-\lambda)^p\bigr)^{1/p},
\]
rather than an exact all-\(p\) \(L^p\) formula.

Classical Clarkson and Hanner inequalities supply the sharp unrestricted upper bounds. A published semantic-index result for the unrestricted generalized James constant on real \(\ell_p\) already gives the corresponding two-branch sequence-space formula. That sequence-space result is therefore treated as covering the \(\ell_p\) special case; the present finding is the measure-space \(L^p(\mu)\) theorem together with the explicit observation that its sharp unrestricted witnesses can always be chosen Birkhoff--James orthogonal.

Older James-type-constant literature was also compared. Yang and Wang compute several concrete sequence-space examples for Takahashi's different James-type constant; those statements do not imply the present weighted Birkhoff formula on general \(L^p(\mu)\).

## Limitations
The theorem requires two disjoint measurable sets of finite positive measure. It does not classify all maximizing pairs, and it does not address Banach lattices that merely resemble \(L^p\) spaces without satisfying the exact Clarkson/Hanner geometry.

The full text of arXiv:2606.01068v1 was not available through the accessible primary channels during the comparison. Its abstract and metadata were inspected, and a detailed secondary review was used to identify the paper's stated \(\ell_p^n\) lower bound. Consequently there remains a residual originality risk that the inaccessible body of the preprint contains an exact \(L^p\) statement not exposed by the accessible materials.

## References
1. J. Qi, Z. Yin, Q. Liu, and Y. Li, *A weighted Birkhoff orthogonal James-type constant*, arXiv:2606.01068v1, 2026.
2. J. A. Clarkson, *Uniformly convex spaces*, Transactions of the American Mathematical Society 40 (1936), 396--414.
3. O. Hanner, *On the uniform convexity of \(L^p\) and \(\ell^p\)*, Arkiv för Matematik 3 (1956), 239--244, DOI:10.1007/BF02589410.
4. C. Yang and Y. Wang, *Some properties of James type constant*, Applied Mathematics Letters 25 (2012), 538--544, DOI:10.1016/j.aml.2011.09.054.
