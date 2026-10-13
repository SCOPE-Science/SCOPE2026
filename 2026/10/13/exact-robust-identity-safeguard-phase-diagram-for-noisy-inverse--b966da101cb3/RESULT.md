# Exact robust identity-safeguard phase diagram for noisy inverse preconditioning

## Finding

Let \(0<\mu<L\) and \(0<\delta<1/L\). Consider a real symmetric positive-definite coefficient matrix \(A\in\mathbb R^{n\times n}\), \(n\ge2\), with **attained** extreme eigenvalues \(\lambda_{\min}(A)=\mu\) and \(\lambda_{\max}(A)=L\). A symmetric, mode-aligned inverse error \(E\) satisfies \(AE=EA\) and \(\|E\|_2\le\delta\). For a reliable digital identity safeguard \(\omega\ge0\), apply the right-preconditioner
\[
M_{\omega}=A^{-1}+E+\omega I,
\qquad B_{\omega}=AM_{\omega}.
\]
For a nonzero initial residual \(r\), the exactly line-searched first right-preconditioned GMRES residual has relative norm
\[
\min_{\alpha\in\mathbb R}\frac{\|r-\alpha B_{\omega}r\|_2}{\|r\|_2}.
\]
Define \(\mathcal R_n(\omega)\) to be its supremum over all such \(A,E,r\). Then
\[
\mathcal R_n(\omega)=\frac{K_n(\omega)-1}{K_n(\omega)+1},
\]
where the **exact attained worst condition ratios** are
\[
K_2(\omega)=\max\left\{
\frac{1+L(\omega+\delta)}{1+\mu(\omega-\delta)},
\frac{1+\mu(\omega+\delta)}{1+L(\omega-\delta)}
\right\}
\]
and, in **every** dimension \(n\ge3\),
\[
K_n(\omega)=
\begin{cases}
\displaystyle\frac{1+L(\omega+\delta)}{1+L(\omega-\delta)}, & 0\le\omega\le\delta,\\[6pt]
\displaystyle\frac{1+L(\omega+\delta)}{1+\mu(\omega-\delta)}, & \omega\ge\delta.
\end{cases}
\]
The two branches agree at \(\omega=\delta\). Let
\[
\delta_c=\frac{L-\mu}{2\mu L},\qquad
\omega_2=\frac{\sqrt{1+(\mu+L)^2\delta^2}-1}{\mu+L}.
\]
There is a **sharp three-phase minimax classification**:

1. If \(0<\delta<\delta_c\), then \(\mathcal R_2\) has the unique minimizer \(\omega_2\), while **each** \(\mathcal R_n\), \(n\ge3\), has the unique minimizer \(\omega=\delta\). The optimal rates are strictly less than the unpreconditioned benchmark \((L-\mu)/(L+\mu)\). For \(n\ge3\), the exact optimal rate is \(L\delta/(1+L\delta)\). In contrast, \(\omega_2\sim (\mu+L)\delta^2/2\) as \(\delta\downarrow0\), giving a quadratic versus linear dimension transition in the best safeguard.
2. If \(\delta=\delta_c<1/L\), the minimizer sets are respectively \([\omega_2,\infty)\) for \(n=2\), and \([\delta,\infty)\) for \(n\ge3\). Both optimal rates equal the unpreconditioned benchmark.
3. If \(\delta_c<\delta<1/L\), both \(\mathcal R_2\) and \(\mathcal R_n\), \(n\ge3\), strictly decrease with \(\omega\), attaining **no** finite minimum; their infima are the unpreconditioned benchmark, approached only as \(\omega\to\infty\).

The second and third regimes are feasible only when \(L/\mu<3\), because the admissible error bound requires \(\delta<1/L\). All asserted spectral and one-step worst cases are attained for every finite \(\omega\), using endpoint perturbations. The no-finite-minimizer assertion concerns only optimization over \(\omega\), not attainment of the inner supremum.

## Assumptions and scope

The coefficient matrix is fixed per one-step problem, real, symmetric and positive definite, with **exact** extreme eigenvalues \(\mu<L\). The perturbation is deterministic, symmetric, commutes with the matrix, and has a prescribed spectral-norm bound \(\delta<1/L\). No independence or stochastic hardware error model is assumed. The safeguards are nonnegative reals and the identity action is exact. The supremum permits separate choices of matrices, errors, and nonzero initial residual for each safeguard parameter. One-step residual minimization is in the ordinary Euclidean norm, with exact scalar line search. Multiple outer iterations, noncommuting errors, quantization, clipping, and time-varying analog actions are excluded.

## Proof

**Step 1: positivity and the exact residual factor.** Since \(E\) and \(A\) are simultaneously orthogonally diagonalizable, their shared spectral modes have eigenvalues \(a\in[\mu,L]\) and \(e\in[-\delta,\delta]\). The right-preconditioned matrix \(B_{\omega}=I+\omega A+AE\) is symmetric positive definite: each mode is \(1+a(\omega+e)\ge1-L\delta>0\). For any SPD matrix with extreme eigenvalues \(0<u\le v\), exact scalar minimization gives
\[
\min_{\alpha}\frac{\|r-\alpha Br\|_2^2}{\|r\|_2^2}
=1-\frac{(r^{\mathsf T}Br)^2}{(r^{\mathsf T}B^2r)(r^{\mathsf T}r)}.
\]
The sharp Kantorovich bound gives the maximum \(((v-u)/(v+u))^2\). This is an equality even when the two endpoint eigenvalues have multiplicity one: take the squared normalized projections of \(r\) onto the \(u\)- and \(v\)-eigenspaces to be \(v/(u+v)\) and \(u/(u+v)\), respectively. Thus the one-step adversarial residual ratio is exactly \((v-u)/(v+u)\), increasing in the condition ratio \(v/u\).

**Step 2: the two-dimensional interval extremum.** In dimension two, the required attained endpoint eigenvalues are exactly \(\mu,L\). The two eigenvalues of \(B_{\omega}\) range independently over
\[
[1+\mu(\omega-\delta),\,1+\mu(\omega+\delta)]
\quad\text{and}\quad
[1+L(\omega-\delta),\,1+L(\omega+\delta)].
\]
The largest ratio of the greater to the smaller of two positive numbers in these intervals occurs at the opposing interval endpoints. This yields the displayed two terms in \(K_2\). Each is attained by the diagonal \(A=\operatorname{diag}(\mu,L)\) and a diagonal \(E\) with entries in \(\{-\delta,\delta\}\), hence is a genuine worst case, not just a bound.

**Step 3: the multimode interval extremum.** For every eigenmode \(a\in[\mu,L]\), the corresponding eigenvalue lies in \([1+a(\omega-\delta),\,1+a(\omega+\delta)]\). The largest possible value is always \(1+L(\omega+\delta)\). If \(\omega\le\delta\), the smallest possible value is \(1+L(\omega-\delta)\), attainable independently of the largest value by **two distinct** \(L\)-eigenvectors. Take \(A=\operatorname{diag}(\mu,L,L)\) and assign errors \(0,-\delta,+\delta\) to these respective eigenvectors. If \(\omega\ge\delta\), the minimum is \(1+\mu(\omega-\delta)\), attained with \(A=\operatorname{diag}(\mu,L,L)\) and errors \(-\delta,+\delta,0\). Padding these matrices proves the same equality for every \(n\ge3\). Their full spectra remain in the required interval, and their extreme eigenvalues remain exactly \(\mu,L\).

**Step 4: exact optimization.** Write
\[
R_+(\omega)=\frac{1+L(\omega+\delta)}{1+\mu(\omega-\delta)},\quad
R_-(\omega)=\frac{1+\mu(\omega+\delta)}{1+L(\omega-\delta)}.
\]
The derivative of \(R_-\) is strictly negative. The derivative of \(R_+\) has the sign of \(L-\mu-2\mu L\delta\), hence changes from positive through zero to negative at \(\delta=\delta_c\). The two ratios cross at the **unique nonnegative** solution of
\[
(\mu+L)\omega^2+2\omega-(\mu+L)\delta^2=0,
\]
namely \(\omega_2\), with \(0<\omega_2<\delta\); \(R_-\) dominates below this point, and \(R_+\) dominates above it. This proves all three two-dimensional minimax regimes. For \(n\ge3\), the initial branch has strictly negative derivative on \([0,\delta]\) and the second branch has the sign of \(L-\mu-2\mu L\delta\), giving the stated minimizers and strict decrease in the last regime. At \(\omega=\delta\), the multimode condition ratio is \(1+2L\delta\), yielding \(L\delta/(1+L\delta)\). At the equality threshold the rising/flat branch ratio equals \(L/\mu\); above threshold it approaches \(L/\mu\) strictly from above. Finally the expansion \(\sqrt{1+t^2}-1\sim t^2/2\) establishes the small-noise comparison. This completes the proof.

## Verification

Run `python verify.py` with Python 3 and its standard library. The program enumerates all sign-extreme commuting errors in \(2100\) exact-rational examples for dimensions two and three, reconstructs \(2100\) exact-rational one-step GMRES endpoint witnesses, verifies nine rational critical-threshold equalities, and checks the two distinct finite-optimum formulas on grids totaling \(20002\) points. Expected output begins `VERIFY_OK`. These checks are finite corroboration; Steps 1–4 above establish the unrestricted theorem.

For a rational illustration, take \(\mu=1\), \(L=2\), \(\delta=1/5\). The error lies strictly below \(\delta_c=1/4\). The two-mode optimum is \(\omega_2=(\sqrt{34}/5-1)/3\), while all dimensions at least three have exact optimum \(\omega=1/5\) and guaranteed contraction \(2/7\); using no preconditioner instead yields worst contraction \(1/3\).

## Relationship to prior work

Shah, Li, Gokmen, Kalantzis, Horesh, and Xi introduce an analog approximate inverse application augmented by a reliable identity term in their equation (3.20), and analyze practical analog-aware damping and flexible GMRES. The present theorem studies their **identity-safeguard design motif** only in a highly structured exact-inverse-plus-commuting-error model, which is not their general hardware model; it gives a closed-form worst-case design diagram rather than another empirical parameter comparison. Feinberg et al. (2021) study analog inversion with circuit compensation but not this deterministic exact one-step optimization. Kalantzis, Gupta, Horesh, Nowicki, Squillante, and Wu (2021) analyze noisy approximate-inverse Richardson iterations, including additive write error and convergence in a stochastic sense, not an optimal reliable-identity offset for one GMRES step. The classical one-step Kantorovich extremum, not claimed as new, is an ingredient; neither the resulting switch in the worst spectral mode nor the dimension-dependent best offset follows from a generic constant-\(\kappa\) estimate alone. Related analyses of noncommuting and time-varying preconditioner errors remain outside this finding.

## Limitations

This result is **not** a universal noise tolerance for analog hardware or an optimal method for full flexible GMRES; symmetry, simultaneous diagonalizability, fixed error, perfect baseline inverse, an exact identity action, a spectral-norm uncertainty ball, and a one-step objective are essential. In particular, arbitrary off-diagonal write error may make \(AM_{\omega}\) nonnormal, defeating the interval argument. The model is a mathematically tractable aligned-error baseline rather than a measured distribution of device errors. Classical perturbation theory may contain an equivalent alternative derivation of these formulas; the literature comparison is necessarily finite, and independent novelty review is outstanding.

## References

1. S. Shah, R. P. Li, T. Gokmen, V. Kalantzis, L. Horesh, and Y. Xi, *Hybrid Digital-Analog Approximate Inverse Preconditioning for Krylov Methods*, arXiv:2606.17227v1, first submitted June 15, 2026. In particular §3.4, equation (3.20). https://arxiv.org/abs/2606.17227
2. B. Feinberg et al., *An Analog Preconditioner for Solving Linear Systems*, Proceedings of IEEE HPCA (2021), DOI:10.1109/HPCA51647.2021.00069.
3. V. Kalantzis et al., *Solving Sparse Linear Systems with Approximate Inverse Preconditioners on Analog Devices*, arXiv:2107.06973, 2021; DOI:10.1109/HPEC49654.2021.9622816.
4. Y. Saad, *A Flexible Inner-Outer Preconditioned GMRES Algorithm*, SIAM Journal on Scientific Computing (1993), DOI:10.1137/0914028. Flexible methods are relevant to varying preconditioners, not used to prove the one-step identity here.
5. Classical Kantorovich inequality and its equality cases for positive-definite matrices (standard spectral extremal tool).
