# A clipped spectral floor for a nullspace branch of double saddle-point preconditioning

## Finding

Consider the real symmetric double saddle-point matrix and the block-triangular preconditioner

\[
\mathcal A=\begin{pmatrix}A&0&B^{\mathsf T}\\0&E&C\\B&C^{\mathsf T}&0\end{pmatrix},\qquad
\mathcal P=\begin{pmatrix}\widehat A&0&0\\0&\widehat E&C\\0&0&-Q\end{pmatrix}.
\]

Write

\[
\widetilde A=\widehat A^{-1/2}A\widehat A^{-1/2},\quad
\overline B=Q^{-1/2}B\widehat A^{-1/2},\quad
\overline C=\widehat E^{-1/2}CQ^{-1/2},
\]

and define the positive parameters \(a=\lambda_{\min}(\widetilde A)\), \(b=\lambda_{\max}(\widetilde A)\), and \(\beta=\lambda_{\min}(\overline B\overline B^{\mathsf T})\). If a **real** eigenvalue \(\lambda\) of \(\mathcal P^{-1}\mathcal A\) admits a nonzero scaled eigenvector \((x,y,z)\) with \(z\ne0\) and \(\overline C z=0\), then

\[
0<\lambda<b,\qquad
\lambda\ge
\begin{cases}
\displaystyle\min\!\left\{a,\frac{b-\sqrt{b^2-4\beta}}2\right\},&4\beta\le b^2,\\[6pt]
a,&4\beta>b^2.
\end{cases}
\tag{1}
\]

In particular, \(\lambda\ge\min\{a,\beta/b\}\) for every admissible choice of blocks. When \(4\beta\le b^2\) and the square-root threshold does not exceed \(a\), the corresponding branch of (1) is attained by a finite-dimensional example.

The clipping in (1) is essential. There is a family with **fixed positive diagonal-block spectra** for which a real eigenvalue on this same nullspace branch remains \(\lambda=1\), yet \(\beta/b\) diverges. Consequently, the unconditional inequality \(\beta/b\le\lambda\) stated for this branch in Lemma 2.2 of Liang and Huang (2026) fails by an unbounded factor.

## Assumptions and scope

Let \(n\ge m\ge p\ge1\). The matrices \(A\in\mathbb R^{n\times n}\) and \(E\in\mathbb R^{p\times p}\) are symmetric positive definite, \(B\in\mathbb R^{m\times n}\) and \(C\in\mathbb R^{p\times m}\) have full row rank, and \(\widehat A,\widehat E,Q\) are symmetric positive definite with matching sizes. Therefore \(\mathcal P\) is invertible and \(\beta>0\). The scaled eigenvector comes from the block-diagonal similarity normalization used to obtain equations (2.2)–(2.4) of Liang and Huang. No commutativity of the blocks is assumed. The claim is restricted to **real eigenvalues with a nonzero third component annihilated by \(\overline C\)**. It makes no assertion about all eigenvalues or any randomized construction of \(Q\).

## Proof

**1. Energy identity.** In normalized coordinates the eigen-equations are

\[
\widetilde A x+\overline B^{\mathsf T}z=\lambda x,\quad
\widetilde E y+\overline C z=\lambda y+\lambda\overline C z,\quad
\overline Bx+\overline C^{\mathsf T}y=-\lambda z.
\tag{2}
\]

For real \(\lambda\) and \(\overline C z=0\), take Hermitian inner products of the first equation with \(x\) and the third with \(z\). The cross terms cancel and yield

\[
x^*\widetilde A x=\lambda(\|x\|_2^2+\|z\|_2^2).
\tag{3}
\]

The vector \(x\) cannot vanish: otherwise the first equation would imply \(\overline B^{\mathsf T}z=0\), contradicting full row rank and \(z\ne0\). Thus (3) proves \(0<\lambda<b\), the upper inequality being strict because \(z\ne0\).

**2. The legitimate resolvent branch.** If \(\lambda<a\), then \(\widetilde A-\lambda I\) is positive definite. By (2),

\[
x=-(\widetilde A-\lambda I)^{-1}\overline B^{\mathsf T}z,\qquad
\lambda\|z\|_2^2=z^*\overline B(\widetilde A-\lambda I)^{-1}\overline B^{\mathsf T}z.
\]

Since \(\widetilde A-\lambda I\preceq(b-\lambda)I\), inversion reverses the Loewner order, and consequently

\[
\lambda\ge\frac{\beta}{b-\lambda},\qquad
\lambda(b-\lambda)\ge\beta.
\tag{4}
\]

If \(4\beta>b^2\), inequality (4) is impossible because \(\lambda(b-\lambda)\le b^2/4\) for \(0<\lambda<b\); hence necessarily \(\lambda\ge a\). If \(4\beta\le b^2\), (4) forces \(\lambda\ge (b-\sqrt{b^2-4\beta})/2\) when \(\lambda<a\). Combining with the complementary branch \(\lambda\ge a\) establishes (1). The weaker bound \(\min\{a,\beta/b\}\) follows because the lower quadratic root is at least \(\beta/b\).

**3. Exact family violating an unclipped floor.** For each real \(t\ge1\), set \(s=\sqrt{3+6t^2}\) and take

\[
\begin{aligned}
&A=\operatorname{diag}(1/2,4,6,7),\quad E=\operatorname{diag}(1/2,3),\\
&B=\begin{pmatrix}t&s&0&0\\0&0&10t&0\\0&0&0&10t\end{pmatrix},\quad
C=\begin{pmatrix}0&1&0\\0&0&1\end{pmatrix},\\
&\widehat A=I_4,\quad\widehat E=I_2,\quad Q=I_3.
\end{aligned}
\tag{5}
\]

All stipulated positive-definiteness and full-row-rank assumptions hold. Moreover \(a=1/2<1<b=7\) and the two eigenvalues of \(\widetilde E\) lie on opposite sides of \(1\). Set

\[
x=(2t,-s/3,0,0)^{\mathsf T},\qquad y=0,\qquad z=(1,0,0)^{\mathsf T}.
\]

One directly obtains \(Cz=0\), \(Ax+B^{\mathsf T}z=x\), \(Ey+Cz=y+Cz=0\), and \(Bx+C^{\mathsf T}y=-z\). Therefore \(\mathcal A(x,y,z)=\mathcal P(x,y,z)\), giving the exact real eigenvalue \(\lambda=1\). This value belongs to neither \(\operatorname{sp}(\widetilde A)\) nor \(\operatorname{sp}(\widetilde E)\).

The row supports of \(B\) are disjoint, so

\[
\overline B\overline B^{\mathsf T}
=\operatorname{diag}(3+7t^2,100t^2,100t^2),\qquad
\frac{\beta}{b}=\frac{3+7t^2}{7}>1.
\]

The proposed unclipped floor fails already at \(t=1\), for which \(s=3\) and \(\beta/b=10/7\). Its discrepancy becomes arbitrarily large as \(t\to\infty\), although \(A,E,\widehat A,\widehat E,Q\) stay fixed. The further integer instance \(t=11,s=27\) gives \(\beta/b=850/7\) with the identical eigenvalue. The dependence on the relative orientation of \(\overline B^{\mathsf T}z\) and the eigenspaces of \(\widetilde A\), not merely on its norm, is what defeats an unconditional scalar quadratic reduction.

**4. Equality on the resolvent branch.** The quadratic-root alternative can be exact. Take \(n=3,m=2,p=1\), \(A=\operatorname{diag}(3,4,4)\), \(E=(1)\), \(B=\begin{psmallmatrix}0&2&0\\0&0&2\end{psmallmatrix}\), \(C=\begin{psmallmatrix}0&1\end{psmallmatrix}\), and identity approximating blocks. Here \(a=3,b=4,\beta=4\), and the lower quadratic root equals \(2<a\). The vector \(x=(0,-1,0)^{\mathsf T},y=0,z=(1,0)^{\mathsf T}\) is an exact generalized eigenvector with \(\lambda=2\), attaining (1). More generally, alignment with a \(b\)-eigenvector realizes the lower root when it lies below \(a\).

## Verification

Run `python verify.py` using Python 3 and only the standard library. The verifier uses exact rational arithmetic for the \(t=1\) and \(t=11\) generalized eigenpairs, nullspace conditions, diagonal coupling Gram matrices, excluded endpoint eigenvalues, and the rational equality instance. It prints a `VERIFY_OK` line. The continuous-parameter family and the universal inequality are established algebraically above; finite checks alone do not prove them.

## Relationship to prior work

Liang and Huang, arXiv:2609.01031v1, introduce the same block matrix and triangular preconditioner in equations (1.1) and (2.1). Their Lemma 2.2 states the nullspace-branch enclosure \(\gamma_{\min}^{B}/\gamma_{\max}^{A}\le\lambda\le\gamma_{\max}^{A}\), with parameters corresponding to \(\beta\) and \(b\). The transition from the resolvent Rayleigh quotient to a scalar quadratic in equations (2.8)–(2.9) is not justified for arbitrary \(\widetilde A\): in general, a Rayleigh quotient of \((\lambda I-\widetilde A)^{-1}\) is not the reciprocal of \(\lambda\) minus a Rayleigh quotient of \(\widetilde A\). Formula (1) replaces that step with an operator-order argument valid on the appropriate spectral branch. The construction (5) shows that the original universal lower bound is not just an imprecise estimate but false under the stated assumptions.

Balani Bakrani, Bergamaschi, Martínez, and Hajarian (2024) derive bounds for a different three-block saddle-point matrix and a different triangular Schur-complement preconditioner, with stronger normalization in their Section 4.1. Those bounds do not imply the present statement for the Liang–Huang pencil. Bergamaschi and Bergamaschi (2026) study symmetric multiple saddle-point problems under symmetric positive-definite preconditioning, not this nonsymmetric triangular branch. The energy identity and the correct resolvent inequality are standard ingredients; no novelty is claimed for those ingredients in isolation.

## Limitations

The analysis only concerns real eigenvalues admitting a nonzero third block in the kernel of the scaled \(C\) coupling. It does not prove or disprove Liang and Huang's other theorems, convergence results, or computational experiments. The counterexample uses permissible SPD approximations, but does not claim these matrices arise from the source's randomized construction. The valid clipped bound is not asserted optimal in all parameter regimes. An independent audit and an exhaustive literature search are not performed; prior equivalent counterexamples remain a residual possibility.

## References

1. S. Liang and N. Huang, *Randomized inexact block triangular preconditioners for double saddle-point systems in PDE-constrained optimization*, arXiv:2609.01031v1, first public 2026-09-01, especially equations (1.1), (2.1), (2.2)–(2.9), Lemma 2.2, and Theorem 2.1. https://arxiv.org/html/2609.01031v1
2. F. Balani Bakrani, L. Bergamaschi, Á. Martínez, and M. Hajarian, *Some preconditioning techniques for a class of double saddle point problems*, Numerical Linear Algebra with Applications **31** (2024), e2551, DOI:10.1002/nla.2551, Sections 2 and 4.1. https://onlinelibrary.wiley.com/doi/full/10.1002/nla.2551
3. L. Bergamaschi and M. Bergamaschi, *Eigenvalue Bounds for Symmetric, Multiple Saddle-Point Matrices with SPD Preconditioners*, 2026, DOI:10.3390/a19050359. https://www.preprints.org/manuscript/202602.0162
