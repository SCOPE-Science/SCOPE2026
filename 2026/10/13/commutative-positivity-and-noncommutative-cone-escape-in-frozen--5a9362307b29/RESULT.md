# Commutative positivity and noncommutative cone escape in frozen-Sylvester square-root refinement

## Finding

Fix an exact symmetric positive-definite square-root target \(X\) and put \(A=X^2\). For any symmetric positive-definite seed \(Z\), define the **frozen-Sylvester iteration** by \(Y_0=Z\) and
\[
Y_{k+1}=Y_k+\mathcal L_Z^{-1}(A-Y_k^2),\qquad
\mathcal L_Z(H)=ZH+HZ.
\]
All matrices here are real symmetric, all Sylvester equations are solved exactly, and the same \(Z\) is used throughout. The following two statements hold.

**Commuting sufficiency (every dimension).** For every \(n\ge1\) and every symmetric positive-definite pair \(X,Z\in\mathbb R^{n\times n}\) satisfying \(XZ=ZX\) and \(2Z-X\succ0\), every \(Y_k\) is positive definite and \(Y_k\to X\).

**Strict noncommutative obstruction (dimension two).** The same strict matrix inequality \(2Z-X\succ0\), even though it makes \(X\) a locally linearly attracting fixed point of the full matrix iteration, does **not** ensure positive-definite iterates when \(XZ\ne ZX\). In fact, take
\[
X=\begin{pmatrix}4&0\\0&1/4\end{pmatrix},\qquad
Z=\begin{pmatrix}25/8&1/2\\1/2&1/2\end{pmatrix}.
\]
Then \(Z\succ0\), \(2Z-X\succ0\), \(Y_1\succ0\), but \(\det(Y_2)<0\). All inequalities are strict, so the phenomenon persists on an open neighborhood of these data. This gives an exact-arithmetic distinction between local linear attraction and preservation of the positive-definite cone.

## Assumptions and scope

The iteration is the fixed-Jacobian, or chord, specialization of the Sylvester refinement equation used in Gao, Kressner, and Shao's matrix square-root method. The target \(X\) is the principal square root of \(A=X^2\); the seed \(Z\) is an arbitrary real symmetric positive-definite matrix. The conclusions concern mathematical iterates, not a specific lower-precision eigensolver's actual output. The strict condition \(2Z-X\succ0\) is a **local stability condition**, not a claimed sufficient condition for global convergence in the noncommuting case. No near-solution or small-roundoff assumption is imposed on the example.

## Proof

**1. Local attraction under the strict order condition.** On symmetric matrices with Frobenius pairing, \(\mathcal L_M\) is a self-adjoint positive-definite operator whenever \(M\succ0\), since
\[
\langle H,\mathcal L_MH\rangle_{\mathrm F}=2\operatorname{tr}(H^\mathsf T MH)>0\quad(H\ne0).
\]
The derivative of the iteration map at its fixed point \(X\) is
\[
\mathcal T'(X)=I-\mathcal L_Z^{-1}\mathcal L_X.
\]
As \(0\prec\mathcal L_X\prec2\mathcal L_Z\) in the operator quadratic-form order when \(X\succ0\) and \(2Z-X\succ0\), every eigenvalue of \(\mathcal L_Z^{-1}\mathcal L_X\) is strictly between \(0\) and \(2\). The derivative therefore has spectral radius strictly below one. By the finite-dimensional fixed-point linearization theorem, \(X\) is locally linearly attracting, without needing \(XZ=ZX\).

**2. Commuting sufficiency.** If \(X\) and \(Z\) commute, simultaneously diagonalize them. Each diagonal entry follows
\[
y_{k+1}=y_k+\frac{x^2-y_k^2}{2z},\qquad y_0=z,\quad x,z>0,\quad x<2z.
\]
Set \(r=1+x/z\in(1,3)\) and \(u_k=(y_k+x)/(2(z+x))\). Direct substitution gives the logistic recurrence
\[
u_{k+1}=r u_k(1-u_k),\qquad u_0=\tfrac12,
\qquad u_*=\frac{r-1}{r}=\frac{x}{z+x}.
\]
For \(1<r\le2\), the interval \([u_*,1/2]\) is invariant, and \(u_{k+1}-u_k=-ru_k(u_k-u_*)\), so the orbit decreases monotonically to \(u_*\). For \(2<r<3\), the interval \([1/2,u_*]\) is invariant under the second iterate: \(g(u)=ru(1-u)\) maps it into \([u_*,r/4]\), and \(g([u_*,r/4])\subset[1/2,u_*]\); the latter follows from \(g(r/4)\ge1/2\) for \(2\le r\le3\). Moreover
\[
g(g(u))-u=-u(ru-r+1)\bigl[r^2u^2-r(r+1)u+r+1\bigr].
\]
The quadratic bracket is strictly positive for \(1<r<3\), as its discriminant is \(r^2(r+1)(r-3)<0\). Hence the even subsequence grows monotonically to \(u_*\) and the odd subsequence also tends to \(u_*\). Throughout, \(u_k\ge\min(1/2,u_*)>u_*/2\), so \(y_k=2(z+x)u_k-x>0\), and \(y_k\to x\). Apply this to every simultaneous eigenmode.

**3. Exact rational cone-exit witness.** The displayed \(X,Z\) satisfy
\[
2Z-X=\begin{pmatrix}9/4&1\\1&3/4\end{pmatrix},
\qquad\det(2Z-X)=11/16>0,
\qquad\det Z=21/16>0.
\]
The leading entries are positive, giving \(Z\succ0\) and \(2Z-X\succ0\). Also \(XZ\ne ZX\). Solving both symmetric \(2\times2\) Sylvester equations exactly yields
\[
Y_1=\begin{pmatrix}
40841/9744&-110/609\\
-110/609&7241/9744
\end{pmatrix},\qquad
\det(Y_1)=\frac{13934861}{4521216}>0.
\]
Thus \(Y_1\succ0\). The next correction yields
\[
Y_2=\begin{pmatrix}
1928079971/498464064&119583745/498464064\\
119583745/498464064&-398298121/1993856256
\end{pmatrix},
\]
with
\[
\det(Y_2)=-\frac{89099634797531}{107317319122944}<0.
\]
The second iterate has eigenvalues of opposite signs. Strict positive-definiteness/negative-determinant inequalities, together with smooth dependence of \(\mathcal L_Z^{-1}\) on \(Z\succ0\), give robustness under sufficiently small perturbations of \((X,Z)\).

## Verification

Run \(\texttt{python3 verify.py}\) with Python's standard library. The checker reconstructs both corrections through exact rational elimination, verifies the Sylvester identities, rechecks all displayed rational matrices and determinants, and verifies strict order and noncommutativity. The printed success marker is \(\texttt{VERIFY_OK}\). The all-dimensions commuting conclusion and local stability are proved above, not inferred from finite testing.

## Relationship to prior work

Gao, Kressner, and Shao (arXiv:2607.12430, Sections 2.1 and 3.1) give the fixed-Sylvester refinement equation and a sufficient norm-smallness condition for local convergence. Those results do not assert global cone invariance from \(2Z-X\succ0\). The present finding separates a globally sufficient condition in the commuting class from a strictly locally stable, noncommuting cone-exit example. The logistic-map reduction and positive-definite operator comparison are standard ingredients; neither is claimed to be new in isolation. Li and Shen (2014) analyze Newton/Samanskii variants based on a different transformed square-root equation, and Higham (1986) analyzes classic matrix-square-root Newton variants; the inspected portions do not state this specific dichotomy. See REVIEW.md and AUDIT.json for the detailed scientific comparisons and remaining literature risk.

## Limitations

This example is outside the source paper's small-initial-error guarantee and is not a counterexample to that theorem, to the correctness of its implementation, or to eventual convergence of this particular orbit. It concerns exact arithmetic and the unmodified frozen-Jacobian mapping; it does not describe floating-point eigensolver output, guarantee failure of a rounded implementation, or establish how often positivity is lost in applications. It proves neither a global convergence failure in the noncommuting case nor a sharp threshold for all noncommuting seeds. An equivalent statement may exist in older chord-method or matrix-iteration literature.

## References

1. B. Gao, D. Kressner, and M. Shao, *A mixed precision algorithm for the matrix square root*, arXiv:2607.12430 (first preprint 2026-07-14), https://arxiv.org/abs/2607.12430 ; accessible full text https://academ.us/article/2607.12430/ . An earlier public conference contribution by the same authors was delivered 2026-05-18: https://indico.math.vt.edu/event/2/contributions/61/ .
2. C.-M. Li and S.-Q. Shen, *Newton's Method for the Matrix Nonsingular Square Root*, Journal of Applied Mathematics (2014), article 267042, https://doi.org/10.1155/2014/267042 .
3. N. J. Higham, *Newton's Method for the Matrix Square Root*, Mathematics of Computation 46 (1986), 537–549, https://doi.org/10.2307/2007992 .
4. J. M. Ortega and W. C. Rheinboldt, *Iterative Solution of Nonlinear Equations in Several Variables*, SIAM, 2000, Chapter 7, https://doi.org/10.1137/1.9780898719468.ch7 .
