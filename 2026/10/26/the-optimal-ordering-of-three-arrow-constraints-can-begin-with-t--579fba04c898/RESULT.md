# The optimal ordering of three arrow constraints can begin with the most correlated pair

## Finding

For every \(0<t<1\), put \(s=\sqrt{1-t^2}\), and form the three unit constraint rows
\[
r_1=(1,0,0),\qquad r_2=(t,s,0),\qquad r_3=(t,0,s).
\]
For the nonsingular symmetric arrow-shaped saddle-point matrix
\[
\mathcal A=\begin{pmatrix}I_3&R^{\mathsf T}\\R&0_3\end{pmatrix},
\qquad R=\begin{pmatrix}r_1\\r_2\\r_3\end{pmatrix},
\]
consider the **exact sequential Schur-complement block-diagonal preconditioner** with the three scalar constraint blocks ordered according to a permutation \(\pi\). Let \(\varrho_\pi\) denote the spectral radius of the symmetrically preconditioned \(6\times6\) matrix. Then all six permutations have a strict three-class ordering:
\[
\boxed{\varrho_{(1,2,3)}=\varrho_{(1,3,2)}
<\varrho_{(2,1,3)}=\varrho_{(3,1,2)}
<\varrho_{(2,3,1)}=\varrho_{(3,2,1)}.}
\]
Thus the **only optimal permutations start with \(r_1\)**. In contrast, the uniquely least-correlated unordered first pair is \(\{r_2,r_3\}\), since \(r_2r_3^{\mathsf T}=t^2<t=r_1r_2^{\mathsf T}=r_1r_3^{\mathsf T}\). Choosing that pair first yields the worst spectral radius, not the best.

The result is quantitative and sharp along this entire parameter family. If \(\mu_\pi\) denotes the largest squared singular value of the normalized constraint matrix, then
\[
\lim_{t\uparrow1}\frac{\mu_{(2,3,1)}}{\mu_{(1,2,3)}}=\frac54,
\qquad
\boxed{\lim_{t\uparrow1}\frac{\varrho_{(2,3,1)}}{\varrho_{(1,2,3)}}=\frac{\sqrt5}{2}.}
\]
Three scalar constraints are minimal for such an ordering dependence within the stated unit-row, zero-constraint-diagonal model: with two independent unit constraint rows, interchanging them leaves the entire preconditioned eigenvalue multiset unchanged.

## Assumptions and scope

All matrices and inner products are real and all claims concern exact arithmetic. For each \(\pi\in S_3\), let \(R_\pi\) be the rows of \(R\) in that order and let \(G_\pi=R_\pi R_\pi^{\mathsf T}\). Set
\[
S_{\pi,1}=1,\qquad
S_{\pi,2}=1-(G_\pi)_{12}^2,\qquad
S_{\pi,3}=\frac{\det G_\pi}{S_{\pi,2}},
\]
\[
P_\pi=\operatorname{diag}(I_3,S_{\pi,1},S_{\pi,2},S_{\pi,3}),
\qquad
Q_\pi=P_\pi^{-1/2}
\begin{pmatrix}I_3&R_\pi^{\mathsf T}\\R_\pi&0_3\end{pmatrix}
P_\pi^{-1/2}.
\]
Because \(\det R=s^2>0\), the three Schur pivots are positive. These are **scalar blocks of the full sequential Schur complement** (the Cholesky pivots of \(G_\pi\)), not the single dense Schur complement and not the incomplete block-diagonal approximation \(\operatorname{diag}(1,1,1)\). The objective \(\varrho_\pi=\max\{|\lambda|:\lambda\in\sigma(Q_\pi)\}\) is the preconditioned spectral radius; neither a MINRES iteration count nor a finite-precision guarantee is asserted.

## Proof

**1. Connection to singular values.** Let \(D_\pi=\operatorname{diag}(S_{\pi,1},S_{\pi,2},S_{\pi,3})\) and \(W_\pi=D_\pi^{-1/2}R_\pi\). Then
\[
Q_\pi=\begin{pmatrix}I_3&W_\pi^{\mathsf T}\\W_\pi&0_3\end{pmatrix}.
\]
For each singular value \(\sigma>0\) of \(W_\pi\), the associated symmetric two-dimensional restriction has eigenvalues
\[
\lambda_\pm(\sigma)=\frac{1\pm\sqrt{1+4\sigma^2}}2.
\]
Therefore, with \(H_\pi=W_\pi W_\pi^{\mathsf T}\) and \(\mu_\pi=\lambda_{\max}(H_\pi)\),
\[
\varrho_\pi=\frac{1+\sqrt{1+4\mu_\pi}}2.
\]
This expression increases strictly with \(\mu_\pi\). It suffices to classify the three-by-three positive-definite matrices \(H_\pi\).

**2. Characteristic coefficients.** Write \(y=t^2\in(0,1)\), \(d=1-y\) and \(\Delta=\det G_\pi=d^2\). Since
\[
H_\pi=D_\pi^{-1/2}G_\pi D_\pi^{-1/2},
\qquad \det H_\pi=\frac{\Delta}{S_{\pi,1}S_{\pi,2}S_{\pi,3}}=1,
\]
its characteristic polynomial is
\[
\chi_\pi(z)=z^3-T_\pi z^2+U_\pi z-1,
\quad T_\pi=\operatorname{tr}H_\pi,
\quad U_\pi=\operatorname{tr}(H_\pi^{-1}).
\]
The last identity uses \(\det H_\pi=1\). The trace and inverse trace can be computed without square roots:
\[
T_\pi=\sum_{i=1}^3\frac{(G_\pi)_{ii}}{S_{\pi,i}},\qquad
U_\pi=\sum_{i=1}^3 S_{\pi,i}(G_\pi^{-1})_{ii}.
\]
Every permutation is equivalent under interchange of the labels \(2\) and \(3\) to one of three orders, denoted \(A=(1,2,3)\), \(B=(2,1,3)\), and \(C=(2,3,1)\). Direct substitution of the Gram products \(t,t,t^2\) gives
\[
\begin{array}{c|cc}
\text{class}&T_\pi&U_\pi\\ \hline
A&T&T\\
B&T&T-\dfrac{y^2}{d}\\
C&T+\dfrac{y^2}{d(1+y)}&T-\dfrac{y^2}{d}
\end{array}
\qquad T=1+\frac2d.
\]
Consequently the three polynomials satisfy the **strict sign differences**
\[
\chi_B(z)=\chi_A(z)-\frac{y^2}{d}z,
\qquad
\chi_C(z)=\chi_B(z)-\frac{y^2}{d(1+y)}z^2
\qquad(z>0).
\]
If \(a\) is the largest positive root of \(\chi_A\), then \(\chi_B(a)<0\). A monic cubic tends to \(+\infty\) as \(z\to+\infty\), so \(\chi_B\) has a real root strictly above \(a\); hence \(\mu_B>\mu_A\). Repeating at the largest root of \(\chi_B\) gives \(\mu_C>\mu_B\). Since every \(H_\pi\) is positive definite, these largest roots are precisely its largest eigenvalues. Strict monotonicity of \(\varrho_\pi\) proves the ordering claim for every \(0<t<1\).

**3. Exact endpoint ratio.** The first polynomial factors as
\[
\chi_A(z)=(z-1)\left(z^2-\frac2d z+1\right),
\quad \mu_A=\frac{1+t\sqrt{2-t^2}}{1-t^2},
\]
so \(d\mu_A\to2\) as \(t\uparrow1\). For class \(C\),
\[
dT_C\longrightarrow\frac52,
\qquad d^2U_C\longrightarrow0,
\qquad d^3\longrightarrow0.
\]
The eigenvalues of \(dH_C\) are nonnegative; their sum tends to \(5/2\) and the sum of their pairwise products tends to zero. Thus exactly one eigenvalue has a nonzero limit, and \(d\mu_C\to5/2\). It follows that \(\mu_C/\mu_A\to5/4\). Applying the expression for \(\varrho\) from Step 1 and using \(\mu_A,\mu_C\to\infty\) proves the limiting ratio \(\sqrt5/2\).

**4. Minimality of three constraints.** For two independent unit rows \(u,v\in\mathbb R^n\) with \(a=u v^{\mathsf T}\) and \(|a|<1\), the scalar Schur pivots in either order are \(1\) and \(1-a^2\). The normalized two-row Gram matrix always has trace \(1+1/(1-a^2)\) and determinant \(1\), independently of which row comes first. Therefore its two eigenvalues are unchanged under reversal. By Step 1 the nontrivial preconditioned eigenvalues are unchanged; if \(n>2\), the additional top-block null-direction eigenvalues are \(1\), also independent of the order. This establishes minimality in the stated model.

## Verification

The accompanying `check.py` verifies the characteristic-polynomial coefficient table **exactly**, using rational arithmetic on seven Pythagorean choices of \(t\) and all six row permutations (42 exact checks). Independent numerical recomputation of all six eigenvalues of the symmetrically preconditioned arrow matrix is compared against the singular-value formula for 36 further cases. Each selected parameter exhibits the three strict spectral classes; the sampled near-singular limiting ratio is consistent with \(5/4\). The infinite-parameter assertions are proved in the preceding section, not inferred from samples. Run `python check.py` with Python 3 and NumPy installed.

## Relationship to prior work

Bergamaschi and Bergamaschi (2026, arXiv:2610.17940v1) define forward sequential Schur blocks for multiple arrow-shaped saddle-point matrices and analyze bounds and rational spectral equations for block-diagonally preconditioned matrices. In particular, their Sections 2–5 give the Schur definitions and the general preconditioned spectral framework used as background here. They also observe that the full sequential Schur-block choice can have unfavorable eigenvalues compared with incomplete blocks. **Neither this construction nor the general singular-value reduction is claimed as new.** The result above instead solves a distinct cross-permutation optimization question for a continuous three-constraint family, classifies all six orders sharply, and proves that the least-correlated-first-pair rule can select the worst one.

Wang, Zhang and Chen (2024, arXiv:2407.19217v2) study row permutations and an approximate block triangular preconditioner for a Neumann boundary-control system; their system, preconditioner and spectral objective differ from the exact sequential scalar Schur blocks examined here. Earlier general saddle-point preconditioning works by Golub, Greif and Varah (2006) and Notay (2014) supply broader block-preconditioner theory, but the accessible materials examined did not exhibit this particular three-order comparison. The novel scope is therefore the stated strict ordering and asymptotic penalty, not a claim of new general block preconditioning principles.

## Limitations

This theorem concerns a specified six-dimensional symmetric indefinite family with three scalar constraints, unit constraint rows, zero constraint-diagonal blocks, and exact sequential Schur complements. It optimizes **spectral radius**, not the full MINRES residual bound, iteration count, implementation cost, numerical stability, or an optimal permutation for arbitrary block matrices. The asymptotic constant concerns the limit along this family, not a universal approximation bound for any ordering heuristic. Additional classical or specialized treatments of elimination ordering could contain equivalent reductions; the assessed priority is subject to such bibliographic uncertainty.

## References

1. L. Bergamaschi and M. Bergamaschi, *Block diagonal preconditioners for arrow-shaped multiple saddle-point linear systems*, arXiv:2610.17940v1, first posted 2026-10-13, https://arxiv.org/abs/2610.17940 (especially Sections 2–5).
2. C. Wang, X. Zhang and X. Chen, *Permuted preconditioning for extended saddle point problem arising from Neumann boundary control*, arXiv:2407.19217v2, https://arxiv.org/abs/2407.19217 (especially Sections 3–4).
3. G. H. Golub, C. Greif and J. M. Varah, *An Algebraic Analysis of a Block Diagonal Preconditioner for Saddle Point Systems*, SIAM J. Matrix Anal. Appl. 27 (2006), 779–792, https://doi.org/10.1137/04060679X.
4. Y. Notay, *A New Analysis of Block Preconditioners for Saddle Point Problems*, SIAM J. Matrix Anal. Appl., https://doi.org/10.1137/130911962.
