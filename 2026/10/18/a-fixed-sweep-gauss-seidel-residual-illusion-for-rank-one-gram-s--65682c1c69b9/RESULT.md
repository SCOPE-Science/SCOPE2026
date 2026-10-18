# A fixed-sweep Gauss–Seidel residual illusion for rank-one Gram systems

## Finding
For every real \(a>0\) and positive integer \(s\) **fixed independently of dimension** \(n\), define
\[
 W_n=I_n+a\mathbf1_n\mathbf1_n^{\mathsf T},\qquad
 W_nx^*=\mathbf1_n.
\]
Let \(x^{(s,n)}\) be the result of precisely \(s\) **forward, unrelaxed Gauss–Seidel sweeps starting from zero**, using the usual row order. Write \(q=(1+a)^{-1}\), \(c=a/(1+a)\) and
\[
 \psi_i^{(s)}=q^ic^{s-1}\binom{i+s-2}{s-1},\quad i\ge1,\qquad
 \gamma_s(a)=a\sum_{i=1}^{\infty}(\psi_i^{(s)})^2.
\]
Then \(0<\gamma_s(a)<\infty\), and the following **simultaneous sharp limits** hold:
\[
 n\left(\frac{\|\mathbf1_n-W_nx^{(s,n)}\|_2}{\|\mathbf1_n\|_2}\right)^2
 \longrightarrow\frac{\gamma_s(a)}{a},
\]
\[
 \frac{\|x^{(s,n)}-x^*\|_{W_n}^2}{\|x^*\|_{W_n}^2}
 \longrightarrow\gamma_s(a).
\]
In particular, a relative *Gram-residual* tolerance fixed independently of \(n\) eventually accepts every fixed positive number of sweeps although its relative squared energy error stays bounded away from zero. The first two constants are
\[
 \gamma_1(a)=\frac{1}{a+2},\qquad
 \gamma_2(a)=\frac{(1+a)^2+1}{(a+2)^3}.
\]
This is not merely a bound for an abstract coefficient system. Define the physical least-squares/Galerkin data in \(\mathbb R^{n+1}\) by
\[
 Q_n=[e_i+\sqrt a\,e_0]_{i=1}^n,\qquad r=e_0/\sqrt a,
\]
where \(e_0,\ldots,e_n\) are standard orthonormal vectors. Then \(Q_n^{\mathsf T}Q_n=W_n\) and \(Q_n^{\mathsf T}r=\mathbf1_n\), and
\[
 \frac{\|r-Q_nx^{(s,n)}\|_2^2}{\|r\|_2^2}\longrightarrow\gamma_s(a)>0,
 \qquad
 \frac{\min_x\|r-Q_nx\|_2^2}{\|r\|_2^2}=\frac1{1+an}\longrightarrow0.
\]
All columns of \(Q_n\) have the same norm and, after scaling by \((1+a)^{-1/2}\), its Gram matrix has **unit diagonal** and fixed off-diagonal coherence \(a/(1+a)\). The phenomenon survives this normalization.

## Assumptions and scope
Everything is exact real arithmetic. The parameter \(a>0\), number of sweeps \(s\ge1\), and row order are fixed; the only limit is \(n\to\infty\). The SPD Gram matrix has eigenvalues \(1\) (multiplicity \(n-1\)) and \(1+an\) (multiplicity one). The coefficient residual is measured in the Euclidean norm and normalized by \(\|\mathbf1_n\|_2\). The energy norm is \(\|v\|_{W_n}^2=v^{\mathsf T}W_nv\). The physical residual is a norm in \(\mathbb R^{n+1}\) rather than the coefficient-space residual.

## Proof
**1. Exact finite-row recurrence.** Put \(S_i^{(s,n)}=\sum_{j=1}^{i}x_j^{(s,n)}\), \(S_0^{(s,n)}=0\), and \(d_n^{(s)}=1-aS_n^{(s,n)}\). The Gauss–Seidel row equation is
\[
 (1+a)x_i^{(s,n)}=1-aS_{i-1}^{(s,n)}
     -a\bigl(S_n^{(s-1,n)}-S_i^{(s-1,n)}\bigr).
\]
Summing/rearranging gives
\[
 S_i^{(s,n)}=qS_{i-1}^{(s,n)}+q d_n^{(s-1)}
      +cS_i^{(s-1,n)}.
\]
For the zero initial iterate, \(x_i^{(1,n)}=q^i\), exactly for every \(1\le i\le n\), and \(d_n^{(1)}=q^n\).

**2. Infinite profile and a justified dimension limit.** For each fixed \(s\), let \(U_i^{(s)}=\sum_{j=1}^{i}\psi_j^{(s)}\). The generating-function identity
\[
 \sum_{i\ge1}\psi_i^{(s)}z^i
 =\frac{qz\,c^{s-1}}{(1-qz)^s}
\]
shows that \(\sum_{i\ge1}\psi_i^{(s)}=1/a\), that \(\psi_i^{(s)}>0\), and that for \(s\ge2\)
\[
 U_i^{(s)}=qU_{i-1}^{(s)}+cU_i^{(s-1)}.
\]
The missing tail \(1/a-U_n^{(s)}\) is \(O_{a,s}(n^{s-1}q^n)\). To verify the finite-to-infinite passage, set \(E_{s,n}=\max_{0\le i\le n}|S_i^{(s,n)}-U_i^{(s)}|\). From the two recurrences,
\[
 E_{s,n}\le E_{s-1,n}+\frac{q}{c}|d_n^{(s-1)}|,
 \qquad
 |d_n^{(s-1)}|\le a E_{s-1,n}+a\bigl(1/a-U_n^{(s-1)}\bigr).
\]
The initial discrepancy is \(E_{1,n}=0\). By induction, \(E_{s,n}=O_{a,s}(n^{s-2}q^n)\) for \(s\ge2\) (a looser polynomial degree also suffices), and \(d_n^{(s)}=O_{a,s}(n^{s-1}q^n)\). Thus \(x_i^{(s,n)}=S_i^{(s,n)}-S_{i-1}^{(s,n)}\) converges in the squared-summable sense to \(\psi_i^{(s)}\), extending the finite vectors by zero: a uniform exponentially small discrepancy on the first \(n\) coordinates, together with the exponentially small infinite tail, gives
\[
 \sum_{i=1}^{n}(x_i^{(s,n)})^2\longrightarrow
 \sum_{i=1}^{\infty}(\psi_i^{(s)})^2.
\]

**3. Gram residual.** The \(i\)-th residual is exactly \(d_n^{(s)}-x_i^{(s,n)}\). Therefore
\[
 \|\mathbf1-W_nx^{(s,n)}\|_2^2
   =\sum_i(d_n^{(s)}-x_i^{(s,n)})^2
   \longrightarrow\sum_{i\ge1}(\psi_i^{(s)})^2
   =\gamma_s(a)/a.
\]
Because \(\|\mathbf1_n\|_2^2=n\), this proves the normalized residual limit.

**4. Physical residual and energy error.** The explicit embedding yields the identity
\[
 \frac{\|r-Q_nx\|_2^2}{\|r\|_2^2}
 =\bigl(1-a\mathbf1_n^{\mathsf T}x\bigr)^2+a\|x\|_2^2.
\]
Its value at \(x^{(s,n)}\) tends to \(\gamma_s(a)\). Direct inversion gives \(x^*=\mathbf1_n/(1+an)\) and the optimal normalized physical residual \((1+an)^{-1}\). By the orthogonal-projection Pythagorean identity,
\[
 \|r-Q_n x\|_2^2-\|r-Q_n x^*\|_2^2
 =\|x-x^*\|_{W_n}^2,
\]
while \(\|x^*\|_{W_n}^2=n/(1+an)\). Dividing proves the energy limit.

**5. Leading constants.** At one sweep \(\psi_i^{(1)}=q^i\); summing the geometric squares gives \(\gamma_1(a)=1/(a+2)\). At two sweeps \(\psi_i^{(2)}=i c q^i\); the standard geometric second-moment identity gives \(\gamma_2(a)=((1+a)^2+1)/(a+2)^3\). Every \(\gamma_s(a)>0\) because its first summand is positive. This completes the proof.

## Verification
The self-contained `verify.py` performs 42 exact rational one-sweep checks for small dimensions, checks the first two constants, and compares 15 independent fixed-sweep parameter combinations at dimension 8192 with the derived asymptotic limits. It prints `ALL_CHECKS_PASSED` when successful. Reproduce with `python3 verify.py`. Those computations check finite cases only; the dimension limits follow from the recurrence and tail estimates above.

## Relationship to prior work
Recent analyses of Chebyshev-basis \(s\)-step preconditioned conjugate gradient recommend a forward Gauss–Seidel Gram solve, and describe relative Gram-residual stopping as a practical indicator rather than a universal theorem. An earlier work analyzes inexact forward Gauss–Seidel and coarse solvers. The new precise fixed-sweep phenomenon is a structural boundary for how such *inner residual criteria* can be interpreted when basis dimension changes: residual reduction by itself need not certify a good projected physical correction. General textbook residual-versus-solution condition-number warnings are not claimed as new.

## Limitations
The matrices are a deliberately coherent SPD Gram family, not demonstrated to be Gram matrices of a particular Chebyshev Krylov run. The result does not predict failures of published numerical tests or of the full iterative algorithms. It does not concern a number of sweeps increasing with dimension, finite-precision effects, or general matrices. The result is a self-contained mathematical counterexample, not a certification of novelty against every historical Gauss–Seidel paper.

## References
1. P. D’Ambra, M. Bernaschi, M. Carrozzo, and collaborators, *Scalable s-step Preconditioned Conjugate Gradient with Chebyshev Basis and Gauss-Seidel Gram Solve*, arXiv:2603.09790, first publicly available 2026-03-10, https://arxiv.org/abs/2603.09790 (full HTML version examined).
2. A. Thomas and P. D’Ambra, *Inexact Gauss Seidel and Coarse Solvers for AMG and s-step CG*, arXiv:2512.09642, first publicly available 2025-12-10, https://arxiv.org/abs/2512.09642 (full HTML examined).
