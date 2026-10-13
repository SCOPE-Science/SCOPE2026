# Sharp first-step normal-residual separation between LSQR and LSMR

## Finding
Consider a full-column-rank real least-squares problem
\[
\min_x\|Ax-b\|_2
\]
and start both LSQR and LSMR from
\[
x_0=0.
\]
Let
\[
g=A^{\mathsf T}b\ne0,
\qquad
B=A^{\mathsf T}A,
\]
and define
\[
s_0=g^{\mathsf T}g,
\qquad
s_1=g^{\mathsf T}Bg,
\qquad
s_2=g^{\mathsf T}B^2g.
\]

The first LSQR and LSMR iterates both lie on the line spanned by \(g\), but they optimize different residuals. They are exactly
\[
x_Q=\frac{s_0}{s_1}g,
\qquad
x_M=\frac{s_1}{s_2}g.
\]
If their first normal residuals are nonzero, then
\[
\boxed{
\frac{\|A^{\mathsf T}(b-Ax_Q)\|_2}
{\|A^{\mathsf T}(b-Ax_M)\|_2}
=
\frac{\sqrt{s_0s_2}}{s_1}.
}
\]

Writing
\[
\kappa=\kappa_2(A),
\]
the exact sharp condition-number envelope is
\[
\boxed{
1\le
\frac{\|A^{\mathsf T}(b-Ax_Q)\|_2}
{\|A^{\mathsf T}(b-Ax_M)\|_2}
\le
\frac{\kappa^2+1}{2\kappa}.
}
\]
The upper bound is attained in two dimensions.

A sharp family is
\[
A=\operatorname{diag}(1,\kappa),
\qquad
b=(\kappa,1/\kappa)^{\mathsf T}.
\]
For this family,
\[
\frac{\|A^{\mathsf T}r_Q\|_2}{\|A^{\mathsf T}b\|_2}
=
\frac{\kappa^2-1}{2\kappa},
\]
while
\[
\frac{\|A^{\mathsf T}r_M\|_2}{\|A^{\mathsf T}b\|_2}
=
\frac{\kappa^2-1}{\kappa^2+1}.
\]
Hence LSMR contracts the normal residual on this equality family for every finite \(\kappa\), whereas LSQR's normal residual grows after the first step exactly when
\[
\kappa>1+\sqrt2.
\]

At \(\kappa=3\), LSQR amplifies the normal residual by \(4/3\), LSMR contracts it by \(4/5\), and the first LSQR normal residual is exactly \(5/3\) times the first LSMR normal residual.

## Assumptions and scope
The theorem is in exact arithmetic. The matrix \(A\) is real and has full column rank, and both methods start from the zero vector without damping or preconditioning.

The comparison is only for the first Krylov step. It does not assert that the ratio between LSQR and LSMR normal residuals obeys the same factor at later iterations.

The monitored quantity is the normal residual
\[
\|A^{\mathsf T}(b-Ax)\|_2,
\]
which is the first-order stationarity measure for least squares. LSQR is designed to minimize the primal residual \(\|b-Ax\|_2\), while LSMR is designed to minimize the normal residual over the same Krylov space.

If \(g\) is a right singular vector of \(A\), both methods solve the one-dimensional normal-equation component exactly on the first step, so both normal residuals are zero. The inequality form remains valid; the displayed ratio is stated only when the denominator is nonzero.

## Proof
The first Krylov space for both methods is
\[
\operatorname{span}\{g\},
\qquad
g=A^{\mathsf T}b.
\]
Write a trial iterate as
\[
x=tg.
\]
Its primal residual is
\[
r(t)=b-tAg.
\]
LSQR minimizes
\[
\|r(t)\|_2^2.
\]
Differentiating gives
\[
(Ag)^{\mathsf T}(b-tAg)=0.
\]
Since
\[
(Ag)^{\mathsf T}b=g^{\mathsf T}g=s_0
\]
and
\[
\|Ag\|_2^2=g^{\mathsf T}Bg=s_1,
\]
one obtains
\[
t_Q=\frac{s_0}{s_1}.
\]
Thus
\[
x_Q=\frac{s_0}{s_1}g.
\]

LSMR instead minimizes the normal residual
\[
\|A^{\mathsf T}r(t)\|_2
=
\|g-tBg\|_2.
\]
Differentiating its squared norm gives
\[
(Bg)^{\mathsf T}(g-tBg)=0,
\]
so
\[
t_M=\frac{s_1}{s_2}
\]
and
\[
x_M=\frac{s_1}{s_2}g.
\]

Let
\[
q_Q=A^{\mathsf T}r_Q,
\qquad
q_M=A^{\mathsf T}r_M.
\]
Direct expansion yields
\[
\|q_Q\|_2^2
=
\frac{s_0(s_0s_2-s_1^2)}{s_1^2}
\]
and
\[
\|q_M\|_2^2
=
\frac{s_0s_2-s_1^2}{s_2}.
\]
When
\[
s_0s_2-s_1^2>0,
\]
the common factor cancels and gives the exact identity
\[
\frac{\|q_Q\|_2}{\|q_M\|_2}
=
\frac{\sqrt{s_0s_2}}{s_1}.
\]
Cauchy--Schwarz gives the lower bound one.

For the sharp upper bound, diagonalize the SPD matrix
\[
B=A^{\mathsf T}A.
\]
Let its eigenvalues lie in
\[
[m,M],
\qquad
m=\sigma_{\min}(A)^2,
\qquad
M=\sigma_{\max}(A)^2.
\]
After normalizing the squared spectral coordinates of \(g\) to probabilities, write
\[
\mu_1=\frac{s_1}{s_0},
\qquad
\mu_2=\frac{s_2}{s_0}.
\]
For every \(\lambda\in[m,M]\),
\[
\lambda^2
\le
(m+M)\lambda-mM.
\]
Averaging gives
\[
\mu_2\le(m+M)\mu_1-mM.
\]
Therefore
\[
\frac{s_0s_2}{s_1^2}
=
\frac{\mu_2}{\mu_1^2}
\le
\frac{(m+M)\mu_1-mM}{\mu_1^2}.
\]
The scalar right-hand side is maximized at
\[
\mu_1=\frac{2mM}{m+M},
\]
where its value is
\[
\frac{(m+M)^2}{4mM}.
\]
Taking square roots and using
\[
\frac{M}{m}=\kappa^2
\]
gives
\[
\frac{\|q_Q\|_2}{\|q_M\|_2}
\le
\frac{\kappa^2+1}{2\kappa}.
\]

Equality requires spectral support only at \(m\) and \(M\), with squared weight
\[
\frac{M}{m+M}
\]
on the \(m\)-eigenspace and
\[
\frac{m}{m+M}
\]
on the \(M\)-eigenspace. This is realized by
\[
A=\operatorname{diag}(1,\kappa),
\qquad
g=(\kappa,1)^{\mathsf T},
\]
which corresponds to
\[
b=(\kappa,1/\kappa)^{\mathsf T}.
\]
Substitution gives the displayed equality formulas.

## Verification
The embedded `verify.py` checks the symbolic first-step formulas with exact rational arithmetic for several rational condition numbers.

For the concrete witness
\[
A=\operatorname{diag}(1,3),
\qquad
b=(3,1/3)^{\mathsf T},
\]
it verifies
\[
t_Q=5/9,
\qquad
t_M=1/5,
\]
and the exact normal-residual factors
\[
\frac{\|A^{\mathsf T}r_Q\|_2}{\|A^{\mathsf T}b\|_2}=\frac43,
\qquad
\frac{\|A^{\mathsf T}r_M\|_2}{\|A^{\mathsf T}b\|_2}=\frac45.
\]
It also verifies the exact cross-method ratio
\[
\frac{\|A^{\mathsf T}r_Q\|_2}{\|A^{\mathsf T}r_M\|_2}=\frac53.
\]

The universal inequality is proved analytically. Finite replay is corroborative only.

## Relationship to prior work
Paige and Saunders introduced LSQR as a Golub--Kahan method for sparse equations and least squares. In exact arithmetic, LSQR minimizes the primal residual over its Krylov subspace and is analytically equivalent to conjugate gradients on the normal equations. Those facts are prior work.

Fong and Saunders introduced LSMR and showed that it is analytically equivalent to MINRES on the normal equations. Their full paper explicitly contrasts the two stopping diagnostics: LSQR has monotone primal residuals, while LSMR has monotone normal residuals, making LSMR attractive for early termination. Those facts are also prior work.

The result here quantifies the first point of that comparison exactly. The same one-dimensional Krylov space produces two different scalar minimizers, and their resulting normal residuals differ by the root-mean-square to mean ratio of the normal-equation spectrum under the starting spectral measure. Optimizing that ratio gives the sharp factor
\[
\frac{\kappa^2+1}{2\kappa}.
\]

A later paper on minimizing least-squares backward error studies iterates lying between LSQR and LSMR and therefore is a particularly relevant broader comparison. Its accessible abstract does not state the first-step normal-residual factor above. The possibility that a related bound appears in its full development is retained as a literature risk.

Targeted searches combining LSQR, LSMR, first iteration, normal residual, condition number, and Kantorovich-type comparisons did not locate the exact identity or sharp factor stated here.

## Limitations
The result is first-step only. Later LSQR and LSMR iterates solve higher-dimensional subproblems, and the scalar moment reduction used here no longer applies directly.

The theorem assumes full column rank. Rank-deficient problems can be treated on the nonzero singular subspace, but that extension is not claimed here.

No preconditioning, damping, regularization, or finite-precision loss of orthogonality is analyzed.

The upper bound is a Kantorovich-type spectral moment inequality, so older CG-versus-MINRES or moment-inequality literature may contain an equivalent first-step comparison under different terminology. This is the principal residual originality risk.

The exact public day of the original 1982 LSQR print issue was not available in the inspected record. The machine-readable source date therefore uses the earliest day-resolved public source among the cited numerical least-squares literature rather than inventing a day for the original print issue.

## References
1. C. C. Paige and M. A. Saunders, “LSQR: An Algorithm for Sparse Linear Equations and Sparse Least Squares,” ACM Transactions on Mathematical Software 8 (1982), 43–71.
2. S. J. Benbow, “Solving Generalized Least-Squares Problems with LSQR,” SIAM Journal on Matrix Analysis and Applications 21 (1999), 166–177. DOI 10.1137/S0895479897321830; online record dated 2006-07-31.
3. D. C.-L. Fong and M. Saunders, “LSMR: An Iterative Algorithm for Sparse Least-Squares Problems,” arXiv:1006.0758; SIAM Journal on Scientific Computing 33 (2011), 2950–2971. DOI 10.1137/10079687X.
4. E. Hallman and M. Gu, “LSMB: Minimizing the Backward Error for Least-Squares Problems,” SIAM Journal on Matrix Analysis and Applications 39 (2018), 1295–1317. DOI 10.1137/17M1157106.
