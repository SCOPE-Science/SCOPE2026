# Sharp dimension-dependent diagonal scaling of one-hub equicorrelation systems

## Finding
For every integer \(m\ge3\), consider the real symmetric matrix
\[
A=\begin{pmatrix}
1&a\mathbf1_m^\top\\
a\mathbf1_m&(1-b)I_m+b\mathbf1_m\mathbf1_m^\top
\end{pmatrix}.
\]
Assume \(a>0\), \(-1/(m-1)<b<1\), and \(m a^2<c:=1+(m-1)b\). This is a positive-definite correlation matrix. Put \(e=1-b\). Among **every** positive diagonal matrix \(D\), without a common-leaf or other symmetry restriction, the spectral condition number \(\kappa_2(DAD)\) is minimized uniquely up to multiplying \(D\) by a positive constant. Its representative with all leaf scales equal to one is
\[
D_*=\operatorname{diag}(\sqrt{x_*},1,\ldots,1),\qquad
x_*=\begin{cases}
c,&a^2c\ge m b^2,\\[2pt]
\dfrac{b(1-b)}{b-a^2},&a^2c<m b^2.
\end{cases}
\]
The second denominator never vanishes in its stipulated regime and yields \(x_*>0\). The sharp minimum is
\[
\kappa_*=
\begin{cases}
\dfrac{\sqrt c+\sqrt m\,a}{\sqrt c-\sqrt m\,a},&a^2c\ge m b^2,\\[5pt]
\max\!\left\{\dfrac{x_*+mb}{e},\dfrac{e}{x_*+mb}\right\},&a^2c<m b^2.
\end{cases}
\]
The ordinary Jacobi scaling, which leaves the displayed unit diagonal unchanged, is globally condition-number optimal **if and only if** \(b=0\) or \(a^2=b^2\).

For fixed \(0<a^2<b<1\), define
\[
m_c=\frac{a^2(1-b)}{b(b-a^2)}.
\]
Then the balanced branch \(x_*=1+(m-1)b\) holds for integer \(m\le m_c\), and the hub scale **saturates** at \(x_*=b(1-b)/(b-a^2)\) for integer \(m\ge m_c\); the two formulae agree at equality. For example, \(a=1/5\), \(b=1/10\) gives \(m_c=6\), and the optimal hub scale remains \(3/2\) for all \(m\ge6\).

## Assumptions and scope
Here \(\mathbf1_m\) is the all-ones vector, \(\kappa_2(M)=\lambda_{\max}(M)/\lambda_{\min}(M)\) for a symmetric positive-definite matrix, and a *positive diagonal scaling* means a diagonal \(D\) with strictly positive diagonal entries. The value is unchanged under a global positive scaling of \(D\); no other equivalence is imposed. Only the real SPD, unit-diagonal, one-hub equicorrelation family and the spectral condition number are claimed. The case \(a=0\) is excluded because its disconnected hub can produce different optimizer behavior. The endpoints \(b=-1/(m-1)\), \(b=1\), or \(ma^2=c\) are singular or outside the SPD domain. The claim makes no assertion about nonsymmetric or non-SPD matrices.

## Proof
**Step 1: reducing the unrestricted problem to a symmetric scaling.** For any positive diagonal \(D\), let \(\ell=\lambda_{\min}(DAD)>0\), \(k=\kappa_2(DAD)\), and \(W=\ell D^{-2}\). Then
\[
W\preceq A\preceq kW.
\]
Conversely, if a positive diagonal \(W\) obeys these inequalities, \(D=W^{-1/2}\) satisfies \(\kappa_2(DAD)\le k\). The permutation group acting on the \(m\) leaves preserves \(A\); averaging the diagonal \(W\) over this finite group preserves both semidefinite inequalities and makes its leaf coordinates equal. Thus for every attainable \(k\) there is a scaling with identical leaf factors attaining a condition number no larger than \(k\). Existence of a scalar optimum will be explicit below, and establishes that an unrestricted optimum is achieved within the symmetric family.

**Step 2: complete eigenvalue reduction.** Normalize the common leaf scale to one, set \(D_x=\operatorname{diag}(\sqrt x,1,\ldots,1)\), \(x>0\), and use the orthogonal decomposition into the leaf-sum-zero subspace and the plane spanned by the hub and the normalized leaf sum. The former has eigenvalue \(e=1-b\), multiplicity \(m-1\). The latter has the \(2\times2\) SPD matrix
\[
T(x)=\begin{pmatrix}x&\sqrt{mx}\,a\\\sqrt{mx}\,a&c\end{pmatrix},\quad
\lambda_\pm(x)=\frac{x+c\pm\sqrt{(x-c)^2+4ma^2x}}2.
\]
Hence \(\lambda_+(x)>\lambda_-(x)>0\), their product is \(x(c-ma^2)\), and their sum is \(x+c\). Each \(\lambda_\pm(x)\) is strictly increasing in \(x\): differentiating \(T(x)\) as a positive diagonal congruence and applying the simple-eigenvalue derivative formula gives
\[
\lambda_\pm'(x)=\frac{\lambda_\pm(x)}x\,|u_{\pm,1}(x)|^2>0,
\]
where the normalized eigenvectors have nonzero first component since \(a>0\).

**Step 3: the two-phase minimum.** The spectral ratio \(r(x)=\lambda_+(x)/\lambda_-(x)\) has a unique minimum at \(x=c\). Indeed, since the product is \(x(c-ma^2)\), the ratio is a strictly increasing function of \((x+c)/\sqrt{x}=\sqrt x+c/\sqrt x\), whose unique minimum is at \(x=c\). At that point the two plane eigenvalues are \(c\pm a\sqrt{mc}\).

If \(b>0\), then \(c>e\) and \(\lambda_+(x)>e\) for every \(x>0\). The bottom eigenvalue is \(\min\{e,\lambda_-(x)\}\). At \(x=c\), the inequality \(\lambda_-(c)\le e\) is equivalent to \(a^2c\ge mb^2\), in which case minimizing \(r(x)\) proves that \(x_*=c\) is the unique global optimum. Otherwise the increasing \(\lambda_-(x)\) crosses \(e\) at exactly one \(x_0<c\). To its left the condition number is \(r(x)\), strictly decreasing there; to its right it is \(\lambda_+(x)/e\), strictly increasing. Thus \(x_*=x_0\).

If \(b<0\), then \(c<e\) and \(\lambda_-(x)<e\) for every \(x>0\). The top eigenvalue is \(\max\{e,\lambda_+(x)\}\). The same inequality \(a^2c\ge mb^2\) is equivalent to \(\lambda_+(c)\ge e\) and implies \(x_*=c\). Otherwise the strictly increasing \(\lambda_+(x)\) crosses \(e\) at a unique \(x_0>c\); the condition number is \(e/\lambda_-(x)\), strictly decreasing before the crossing, and \(r(x)\), strictly increasing after it. Thus \(x_*=x_0\). If \(b=0\), then \(e=c=1\) lies strictly between \(\lambda_-(x)\) and \(\lambda_+(x)\), and the unique minimum of \(r(x)\) gives \(x_*=c=1\).

In either crossing regime, setting \(\det(T(x_0)-eI)=0\) gives
\[
(x_0-e)(c-e)-ma^2x_0=0,
\qquad x_0(b-a^2)=b(1-b),
\]
and hence the asserted weak-branch scale. Here the other plane eigenvalue is \(x_0+c-e=x_0+mb>0\), yielding the weak-branch condition-number formula. At \(x=c\), the plane eigenvalues yield the strong-branch formula. These arguments also prove uniqueness among symmetric scalings.

**Step 4: rigidity against arbitrary independent diagonal entries.** Let \(k=\kappa_*\). For an arbitrary unrestricted optimal scaling \(D\), form the feasible \(W=\lambda_{\min}(DAD)D^{-2}\) from Step 1. Let \(\overline W\) be its average over leaf permutations. Then \(\overline W\preceq A\preceq k\overline W\). Symmetric optimizer uniqueness from Step 3 determines the ratio of the hub and leaf entries of \(\overline W\); furthermore the two tight inequalities for a condition ratio exactly \(k\) fix their common normalization. Therefore \(\overline W=W_0\), where \(W_0=\lambda_{\min}(D_*AD_*)D_*^{-2}\). Writing \(\Delta=W-W_0\), we have \(\Delta_{00}=0\) and \(\sum_{i=1}^m\Delta_{ii}=0\).

When \(b\ge0\), the largest eigenvalue of \(D_*AD_*\) is the uniform-leaf plane eigenvalue \(\lambda_+\), strictly above \(e\). Choose its generalized eigenvector \(q\) with \((kW_0-A)q=0\); all of its leaf components coincide and are nonzero because \(a>0\). Since \(kW-A\succeq0\) and \(q^\top(kW-A)q=kq^\top\Delta q=0\), positivity forces \((kW-A)q=0\). Subtracting the first kernel identity gives \(\Delta q=0\). Because the common leaf component is nonzero, every \(\Delta_{ii}=0\).

When \(b<0\), instead use the uniform-leaf plane minimum eigenvector, for which \((A-W_0)q=0\), and the identical argument with \(A-W\succeq0\) yields \(\Delta q=0\). Hence in both cases \(W=W_0\), proving uniqueness of \(D\) up to a positive scalar **without assuming symmetry of the competing scaling**.

**Step 5: Jacobi criterion and dimension transition.** Since \(A\) has unit diagonal, Jacobi scaling is the identity, corresponding to \(x=1\). In the strong branch \(x_*=c=1\) forces \(b=0\). In the weak branch \(b(1-b)/(b-a^2)=1\) is equivalent to \(a^2=b^2\), which indeed lies in the weak branch whenever the SPD assumptions hold and \(b\ne0\). This proves the criterion. For \(0<a^2<b<1\), the comparison \(a^2[1+(m-1)b]\ge mb^2\) rearranges to \(m\le a^2(1-b)/[b(b-a^2)]\). This proves the exact dimension cutoff and eventual scale saturation.

## Verification
Run `python3 VERIFY.py` with Python 3 standard library. The included checker verifies exact rational determinant and branch identities, independent numerical Jacobi eigenvalue decompositions, perturbations of hub and independent leaf scales, and the explicit integer-dimension crossover. In the prepared package it returned `PASS: 2666 finite exact/numerical assertions; 176 admissible parameter triples`. These checks do not substitute for Steps 1–5, which apply to every stated parameter and integer dimension.

## Relationship to prior work
Takapoui and Javadi (2016) motivate diagonal preconditioning through equilibration and numerical matrix conditioning. Diamond and Boyd (2016) rigorously relate equilibration to a bound on the condition number, not the exact optimum of this structured SPD family. Kolotilina's original 2004 / translated 2006 theorem explicitly settles generic quasireal Hermitian \(3\times3\) diagonal scaling, and **already covers the special case \(m=2\)**; that case is therefore excluded from the present claim. General matrix-condition and block-scaling methods of Shapiro, Kolotilina, Braatz–Morari, and Qu–Gao–Hinder–Ye–Zhou provide related optimization frameworks, not an explicitly inspected version of this full \(m\ge3\) two-phase formula and unrestricted rigidity. This is a qualified comparison, not an assertion that a failed database search proves novelty.

## Limitations
The result is for positive diagonal *congruence* scaling of this SPD family, not arbitrary nonsymmetric left–right equilibration, block preconditioning, indefinite matrices, or acceleration of a specific iterative solver. Only the spectral two-norm condition number is optimized. The closed form is not claimed novel in dimension three. The full texts of some potentially relevant older general block-scaling works, notably Shapiro (1985) and Kolotilina (2002), could not be examined; they are remaining historical-coverage risks. No independent mathematical audit has been performed.

## References
1. A. Takapoui and H. Javadi, *Preconditioning via Diagonal Scaling*, arXiv:1610.03871v1 (public October 12, 2016), https://arxiv.org/abs/1610.03871.
2. S. Diamond and S. Boyd, *Stochastic Matrix-Free Equilibration*, arXiv:1602.06621v1 (public February 22, 2016), https://arxiv.org/abs/1602.06621.
3. L. Yu. Kolotilina, *Solution of the Problem of Optimal Diagonal Scaling for Quasireal Hermitian Positive-Definite 3×3 Matrices*, Russian original (2004), English translation *Journal of Mathematical Sciences* (2006), https://doi.org/10.1007/s10958-005-0488-1.
4. A. Shapiro, *Optimal Block Diagonal l₂-Scaling of Matrices*, *SIAM Journal on Numerical Analysis* (1985), https://doi.org/10.1137/0722005.
5. L. Yu. Kolotilina, *Optimally Conditioned Block Matrices*, *Linear Algebra and its Applications* (2002), https://doi.org/10.1016/S0024-3795(01)00412-8.
6. R. D. Braatz and M. Morari, *Minimizing Euclidean Condition Number*, *SIAM Journal on Control and Optimization* (1994), https://doi.org/10.1137/S0363012992238680.
7. Z. Qu, W. Gao, O. Hinder, Y. Ye and Z. Zhou, *Optimal Diagonal Preconditioning*, arXiv:2209.00809 (2022), https://arxiv.org/abs/2209.00809.
