# Exact two-cluster E-optimal row sampling and a sharp correlation transition

## Finding
Let \(p,q\ge2\) and let the normalized real rows \(a_i\) of a nonsingular square system form two correlation-homogeneous groups: pairwise correlation \(c\) within each group and \(r\) between groups. Assume \(0<c<1\), \(r>0\), and \(pq r^2<ab\), where
\[
a=1+(p-1)c,\qquad b=1+(q-1)c.
\]
For iid row selection with probabilities \(\pi_i\), maximize the sharp worst-initial-error, conditional one-step squared-error reduction \(\Lambda(\pi)=\lambda_{\min}(\sum_i\pi_i a_i a_i^\top)\). The following gives a globally optimal distribution over the **entire** probability simplex.

If \(p=q\) or \(r\le c\), take uniform probabilities \(u=v=1/(p+q)\) in both classes. If the classes are unequal and \(r>c\), rename them so \(p<q\), and set
\[
t_0=\frac{b+qr}{a+pr},\qquad D=a-\frac{pr^2}{c},\qquad
 t_* =\begin{cases}
 t_0,&D\le0,\\
 \min\{t_0,(1-c)/D\},&D>0.
 \end{cases}
\]
Then per-row probabilities \(u=t_*/(pt_*+q)\) on the smaller group and \(v=1/(pt_*+q)\) on the larger group are globally optimal. The exact best constant is
\[
\Lambda_*=
\begin{cases}
(1-c)/(p+q),&r\le c,\\
(ab-pqr^2)/(pb+qa+2pqr),&p<q,\ r>c,\ t_*=t_0,\\
(1-c)/(pt_*+q),&p<q,\ r>c,\ D>0,\ t_*<t_0.
\end{cases}
\]
When \(p=q\) and \(r>c\), the optimal distribution is uniform with sharp rate \((a-pr)/(2p)\); this case is separate from the three displayed branches. At the shared boundary of the last two branches the formulas agree.

For fixed \(p\ge2\), \(0<c<1\), and \(c<r<\sqrt{ac/p}\), the optimal ratio for every sufficiently large \(q\) is exactly
\[
\frac uv=R=\frac{1-c}{a-pr^2/c}>1.
\]
Moreover the optimal-to-uniform sharp rate ratio tends to \(R\); this can be arbitrarily large as \(r\) approaches the indicated upper boundary from below (with the large-\(q\) limit taken first).

## Assumptions and scope
The real row Gram matrix is the \((p+q)\)-square block matrix with identity diagonal, constant off-diagonal entries \(c\) within either class, and constant entries \(r\) across classes. The stated inequalities make it positive definite. Thus normalized independent rows realizing it exist. Each row is selected independently with fixed probability; no finite-horizon or wall-clock-optimality claim is made. At boundary \(r=c\) both classes have the same correlation and uniform sampling remains optimal. At \(p=q\) symmetry also makes uniform optimal, even for \(r>c\).

## Proof
Write \(C\) for the row Gram matrix and \(P=\operatorname{diag}(\pi)\). Conditional projection onto row \(a_i\) gives \(\mathbb E(\|e^+\|^2\mid e)=\|e\|^2-e^\top A^\top P A e\). The nonzero eigenvalues of \(A^\top P A\) equal those of \(C^{1/2}PC^{1/2}\), which is affine in \(P\). Therefore its smallest eigenvalue is concave in the sampling probabilities. Averaging any maximizer over within-group permutations produces a group-constant global maximizer without an assumption of symmetry.

Set the two per-row probabilities to \(u,v\), with \(pu+qv=1\). The eigenvalues of \(P^{1/2}CP^{1/2}\) are \((1-c)u\) with multiplicity \(p-1\), \((1-c)v\) with multiplicity \(q-1\), and the two eigenvalues of
\[
M(u,v)=\begin{pmatrix}au&r\sqrt{pq uv}\\r\sqrt{pq uv}&bv\end{pmatrix}.
\]
Call the smaller of these last two eigenvalues \(\ell(u,v)\). This is an exact spectral decomposition, including cases \(p=q\).

For \(r\le c\), the matrix \(C-(1-c)I\) is positive semidefinite (its only nonzero two-dimensional block has determinant \(pq(c^2-r^2)\)). At uniform probabilities the smallest eigenvalue is \((1-c)/(p+q)\). Every class-constant allocation has smallest eigenvalue at most \((1-c)\min(u,v)\le(1-c)/(p+q)\). Symmetrization proves global optimality. If \(p=q\), swapping classes similarly makes uniform optimal. For \(r>c\) and \(p=q\), the coupled minimum is \((a-pr)/(2p)\).

For the remaining case \(p<q\), \(r>c\), introduce \(t=u/v\), so \(u=t/(pt+q)\), \(v=1/(pt+q)\). The coupled lower eigenvalue is
\[
\ell(t)=\frac{at+b-\sqrt{(at-b)^2+4pqr^2t}}{2(pt+q)}.
\]
Its unique maximizer on \(t>0\), obtained by differentiation, is \(t_0=(b+qr)/(a+pr)>1\), where \(\ell(t_0)=(ab-pqr^2)/(pb+qa+2pqr)\). The derivative changes from positive to negative there. For \(0<t\le1\), both \(\ell(t)\) and the smaller transverse eigenvalue \((1-c)u\) increase, so no global optimum lies below \(1\). For \(t\ge1\), the smaller transverse eigenvalue is \((1-c)v\). The determinant test for
\(M-(1-c)v I\) is proportional to \(Dt-(1-c)\). Thus if \(D\le0\), \(\ell(t)<(1-c)v\) for all \(t\); if \(D>0\), the two active branches cross exactly at \(t=(1-c)/D>1\), the coupled branch lying below before the crossing. The scalar objective is therefore maximized at \(t_*\) as stated. Strict monotonicity in these regions also gives uniqueness of the optimal **group-constant** ratio, without claiming full-simplex uniqueness.

For fixed \(p,c,r\) in the stated asymptotic range, \(D>0\), while \(t_0=(b+qr)/(a+pr)\) grows linearly in \(q\). Eventually \(t_0>(1-c)/D=R\), proving the exact crossover allocation. Its rate satisfies \(q\Lambda_*\to1-c\). For uniform sampling, the coupled Gram minimum tends to \(a-pr^2/c=D\), which is strictly less than \(1-c\), so \(q\Lambda_{\rm uniform}\to D\). Their ratio tends to \(R\), and \(R\to\infty\) as \(D\downarrow0\).

## Verification
The standalone `verify.py` independently constructs Gram matrices and performs eigenvalue computations for 4,800 admissible parameter cases, comparing the theorem with one-dimensional numerical optimization. Smaller systems are also checked against thousands of asymmetric probability competitors and exact-rational arithmetic is provided for a twelve-row illustration. The numerical tests corroborate the formula but do not replace the proof of the all-parameter statement.

For example, with \(p=2\), \(q=10\), \(c=1/4\), \(r=7/20\), one gets \(D=27/100\), \(R=25/9\), \(u=5/28\), \(v=9/140\), and \(\Lambda_*=27/560\).

## Relationship to prior work
Strohmer and Vershynin (2007) introduced the influential randomized Kaczmarz framework. Gower and Richtárik (2015), especially section 5.1, formulate optimal sampling probabilities through a general semidefinite program. The present result evaluates that E-optimal program in closed form on a two-block compound-symmetry Gram family, identifying a genuine finite-dimensional change of active eigenmode and an unbounded large-class-size sampling advantage. It is not a new generic SDP formulation. The previously available one-exceptional-row classification does not imply this theorem because both classes here have at least two rows and each contributes transverse eigenvalues. Agaskar, Wang, and Lu (2014) treat different finite-step and asymptotic MSE criteria; full-text comparison was restricted by repository access.

## Limitations
The result determines an optimal fixed iid row-selection rule and its sharp worst-case conditional one-step squared-error coefficient. It does not establish all nonsymmetric maximizers, empirical wall-clock speed, finite-time MSE optimality, or the same rule for inconsistent systems. Equivalent special cases in differently indexed optimal-design literature cannot be excluded without independent review.

## References
- T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, arXiv:math/0702226, first submitted 2007-02-08, https://arxiv.org/abs/math/0702226.
- R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, SIAM Journal on Matrix Analysis and Applications 36 (2015), 1660–1690, arXiv:1506.03296, https://pages.stat.wisc.edu/~bwu62/771/gower2015.pdf.
- A. Agaskar, C. Wang, and Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, IEEE GlobalSIP (2014), 389–393, https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b.
