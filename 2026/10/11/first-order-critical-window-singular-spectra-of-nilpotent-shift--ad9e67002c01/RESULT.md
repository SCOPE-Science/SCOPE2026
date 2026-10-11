# First-order critical-window singular spectra of nilpotent-shift resolvents

## Finding
Let \(J_n:\mathbb C^n\to\mathbb C^n\) be the upper nilpotent shift, \((J_nx)_i=x_{i+1}\) for \(i<n\), with last coordinate zero. For real \(s\), put \(r_n=1+s/n>0\) and \(R_n(s)=(I-r_nJ_n)^{-1}\). Write \(S_{n,j}(s)\) for the \(j\)-th largest singular value. The parameter \(s\) is fixed as \(n\to\infty\), and \(j\ge1\) is fixed.

Define a real function on its separate spectral branches by
\[
\Phi(w)=\begin{cases}\sqrt w\cot\sqrt w,&w>0,\quad \sqrt w\notin\pi\mathbb Z,\\1,&w=0,\\\sqrt{-w}\coth\sqrt{-w},&w<0.\end{cases}
\]
For every real \(s\), let \(w_1(s)\) be the unique solution of \(\Phi(w)=s\) with \(w<\pi^2\), and let \(w_j(s)\), for \(j\ge2\), be the unique solution in \(((j-1)^2\pi^2,j^2\pi^2)\). In the first branch, \(w_1(s)>0\) for \(s<1\), \(w_1(1)=0\), and \(w_1(s)<0\) for \(s>1\). Set \(D_j(s)=s^2+w_j(s)>0\).

**Theorem (all fixed ranks; locally uniform in the parameter).** For every fixed positive integer \(j\) and every compact \(K\subset\mathbb R\), as \(n\to\infty\) with \(n\ge j\) and \(r_n>0\), uniformly for \(s\in K\),
\[
\boxed{S_{n,j}(s)=\frac{n}{\sqrt{D_j(s)}}+\frac{s-1}{4\sqrt{D_j(s)}\,\Phi'(w_j(s))}+O_{j,K}(n^{-1}).}
\]
Here the ordinary derivative satisfies \(\Phi'(w)<0\) on every branch, including \(\Phi'(0)=-1/3\). Therefore the finite, explicit constant-order correction is positive for \(s<1\), zero for \(s=1\), and negative for \(s>1\), **simultaneously at every fixed rank**.

At the common cancellation point \(s=1\), all fixed singular values converge with one additional order:
\[
S_{n,j}(1)=\frac{n}{\sqrt{1+w_j(1)}}+O_j(n^{-1}).
\]
The leading singular value has the stronger **exact finite-dimensional identity**
\[
\boxed{\|R_n(1)\|_{2\to2}=S_{n,1}(1)=n\qquad(n\ge2).}
\]
For the unweighted edge \(s=0\), the formula recovers the exact spectrum \(S_{n,j}(0)=[2\sin((2j-1)\pi/(4n+2))]^{-1}\), hence \(S_{n,j}(0)=2n/((2j-1)\pi)+1/((2j-1)\pi)+O_j(n^{-1})\).

## Assumptions and scope
All vector spaces are real or complex Euclidean spaces, with the same singular values for these real matrices. The asymptotic concerns **fixed rank** \(j\) only; it does not assert a uniform estimate in \(j\) growing with \(n\), nor in unbounded \(s\). Negative \(s\) is allowed provided \(1+s/n>0\), automatic eventually. The upper rather than lower shift merely fixes an orientation. All eigenvalues and singular values are arranged by multiplicity and size; for \(r_n>0\) the finite singular values are simple.

## Proof
**1. The continuum spectral branches and their indexing.** The inverse \(R_n(s)\) has exact entries \((R_n(s))_{ik}=r_n^{k-i}\) for \(k\ge i\), and zero otherwise. Associate \(\mathbb C^n\) isometrically with step functions in \(L^2(0,1)\) by mapping the coordinate \(i\) to the value \(\sqrt n\,x_i\) on its \(i\)-th interval. The embedded operator \(R_n(s)/n\), extended by zero on the orthogonal complement, has step kernel equal to the above matrix entries. Uniformly for \(s\) in compact sets, these kernels converge in \(L^2((0,1)^2)\) to
\[
K_s(x,y)=\mathbf1_{\{x<y\}}e^{s(y-x)}.
\]
Thus the embedded operators converge in Hilbert–Schmidt (and hence operator) norm, and each fixed singular value converges to that of \(T_sf(x)=\int_x^1e^{s(y-x)}f(y)\,dy\). This compact operator is the inverse of \(L_s=-d/dx-s\) with terminal Dirichlet condition \(f(1)=0\). The eigenvalue problem for \(L_s^*L_s\) is \(-f''+s^2f=\lambda f\), subject to \(f(1)=0\) and \(f'(0)+sf(0)=0\). Writing \(\lambda=s^2+w\), a nonzero solution gives exactly \(\Phi(w)=s\). For \(w<0\), write \(w=-u^2\) and obtain \(s=u\coth u\); in that case \(s^2+w=u^2\operatorname{csch}^2u>0\). For \(w>0\) the branch functions decrease from \(+\infty\) to \(-\infty\) between successive poles. On the first branch, \(\Phi\) decreases from \(+\infty\) at \(w=-\infty\) through \(1\) at \(0\) to \(-\infty\) as \(w\uparrow\pi^2\). Its derivative is strictly negative: for \(w=t^2>0\), \(\Phi'(w)=[\sin t\cos t-t]/(2t\sin^2t)<0\); the hyperbolic analogue gives the same sign, while \(\Phi'(0)=-1/3\). The corresponding one-dimensional Robin–Dirichlet Sturm–Liouville operator has simple increasing eigenvalues \(s^2+w_j(s)\). Compact singular-value convergence fixes the index \(j\) in the subsequent discrete calculation.

**2. Exact finite characteristic equation.** Write \(B_n=I-r_nJ_n\). The symmetric tridiagonal matrix \(B_n^*B_n\) has diagonal entries \(1,1+r_n^2,\ldots,1+r_n^2\) and off-diagonal entries \(-r_n\). A vector with components \(y_i=\sin((n+1-i)\theta)\) solves its interior and last-coordinate equations with eigenvalue \(\lambda=1+r_n^2-2r_n\cos\theta\). The first-coordinate equation is exactly
\[
\sin((n+1)\theta)=r_n\sin(n\theta).
\]
The formulas have their analytic hyperbolic continuation for imaginary \(\theta\); at \(\theta=0\), the limiting vector is \(y_i=n+1-i\), and the limiting boundary equation is \(n+1=r_nn\). All eigenvalues of this irreducible symmetric tridiagonal matrix are simple. Combined with step-kernel convergence and the simplicity of the continuum spectrum, the root associated with each fixed \(j\) has \(n\theta_{n,j}\to\sqrt{w_j(s)}\), with the principal imaginary square root when needed, locally uniformly in \(s\).

**3. First-order root expansion.** Set \(z_{n,j}=n^2\theta_{n,j}^2\) and \(w=w_j(s)\). Dividing the characteristic equation by the analytic sine factors yields the exact analytic equation near each continuum root,
\[
s=\Phi(z_{n,j})\frac{\sin(\sqrt{z_{n,j}}/n)}{\sqrt{z_{n,j}}/n}+n\left[\cos(\sqrt{z_{n,j}}/n)-1\right].
\]
The quotient is defined as one at zero and by its entire power series on negative inputs. Taylor expansion, uniformly for bounded \(z\), gives \(s=\Phi(z_{n,j})-z_{n,j}/(2n)+O(n^{-2})\). Since \(\Phi'(w)\ne0\), the implicit-function theorem yields
\[
z_{n,j}=w+\frac{w}{2\Phi'(w)}\frac1n+O_{j,K}(n^{-2}).
\]
This remains valid at \(w=0\). Consequently,
\[
n^2\lambda_{n,j}=s^2+w+\frac{sw+w/(2\Phi'(w))}{n}+O_{j,K}(n^{-2}),
\]
where \(\lambda_{n,j}\) is the \(j\)-th **smallest** eigenvalue of \(B_n^*B_n\). Using \(\Phi'(w)=[s(1-s)-w]/(2w)\) for \(w\ne0\), with continuity at zero, reduces the coefficient to \((1-s)(s^2+w)/(2\Phi'(w))\). Taking \(\lambda_{n,j}^{-1/2}\) gives the asserted \(S_{n,j}\) formula. The compactness of \(K\), the strict simplicity of continuum roots, and the analytic expansions make the remainders locally uniform. Because \(\Phi'<0\), the coefficient's sign is the opposite of the sign of \(s-1\).

**4. Exact critical identity and strict finite threshold.** At \(s=1\), \(r_n=(n+1)/n\). The positive vector \(y_i=n+1-i\) satisfies \(B_n^*B_ny=n^{-2}y\) by direct substitution. More precisely, with \(\lambda=n^{-2}\) and arbitrary complex \(x\), its positive-ground-state identity is
\[
\langle x,(B_n^*B_n-\lambda I)x\rangle=\sum_{i=1}^{n-1}r_n y_i y_{i+1}\left|\frac{x_i}{y_i}-\frac{x_{i+1}}{y_{i+1}}\right|^2\ge0.
\]
This proves the smallest eigenvalue is exactly \(n^{-2}\), and hence the largest singular value of its inverse is exactly \(n\). For each fixed \(n\ge2\), \(R_n(r)\) has nonnegative entries and is entrywise strictly increasing in \(r>0\) above the diagonal. Perron–Frobenius applied to the positive matrix \(R_n(r)^*R_n(r)\) shows that \(\|R_n(r)\|_{2\to2}\) is strictly increasing with \(r>0\); therefore the unique positive parameter giving norm \(n\) is \(r=(n+1)/n\).

## Verification
The supplementary `verify.py` replays the exact rational eigenvector identity for each \(2\le n\le50\), and independently computes finite tridiagonal eigenvalues for three leading ranks, five values of \(s\), and three dimensions per parameter. It compares them against the derived \(n\)-term and constant term, reporting `JORDAN_CRITICAL_WINDOW_CHECK_OK` on success. The finite numerical checks **do not prove** the all-dimensional asymptotic, its uniformity, nor literature priority; those rely on the preceding analytic argument.

## Relationship to prior work
Widom's 1989 paper treats second-order aggregate singular-value distributions for Toeplitz matrices under fixed bounded-symbol hypotheses, not the present dimension-dependent symbol with a pole approaching the unit circle or individual fixed-rank \(O(1)\) coefficients. Bourget, Alvarez Loya and McMillen's 2016 spectral-asymptotics survey likewise treats limiting distributions and determinant regimes of Toeplitz/Kac–Murdock–Szegő matrices. Ransford's 2022 Volterra-resolvent exposition reports the known singular-value calculus for linear functions of the Volterra operator; that continuum calculation is relevant to, and is **not** claimed as a novelty of, the leading \(n\)-scaled limit. Higham's 2024 work on bidiagonal matrices includes inverse formulas and spectral perturbation bounds (notably Theorems 2.4–2.5), but does not state the explicit critical-window fixed-rank expansion, its simultaneous cancellation, or the exact finite critical norm. The present contribution is the **joint explicit first correction, its rank-uniform sign transition for each fixed index, and critical exact finite threshold**, not the underlying tridiagonal recurrence or continuum Robin spectrum.

## Limitations
The \(O(n^{-1})\) remainder is proved only at fixed singular-value index and for bounded \(s\); no bulk eigenvalue or growing-rank statement is made. The finite equality and finite threshold concern the upper Euclidean nilpotent shift and positive real weights. A historical equivalent, especially in local-to-unity autoregressive covariance, bidiagonal SVD, or Sturm–Liouville boundary-discretization literature, cannot be excluded by a finite literature search. Independent mathematical and bibliographic validation has not been performed.

## References
1. H. Widom, *On the Singular Values of Toeplitz Matrices*, Z. Anal. Anwend. 8 (1989), 221–229, DOI 10.4171/ZAA/350 (published 30 June 1989).
2. A. Bourget, A. Alvarez Loya and T. McMillen, *Spectral Asymptotics for Kac–Murdock–Szegő Matrices*, arXiv:1610.00084 (first arXiv posting 1 October 2016).
3. T. Ransford, *The Norm of the Resolvent of the Volterra Operator*, arXiv:2206.09937 (2022).
4. N. J. Higham, *The Power of Bidiagonal Matrices*, Electronic Journal of Linear Algebra 40 (2024), 453–474, DOI 10.13001/ela.2024.8297.
