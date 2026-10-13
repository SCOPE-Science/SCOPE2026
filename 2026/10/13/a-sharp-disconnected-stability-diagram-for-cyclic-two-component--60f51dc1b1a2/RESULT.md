# A sharp disconnected stability diagram for cyclic two-component heavy-ball descent

## Finding
Consider two scalar strongly convex component losses \(f_a(x)=a x^2/2\) and \(f_b(x)=b x^2/2\), where \(a,b>0\), and their common minimizer \(x_*=0\). A deterministic incremental heavy-ball scheme takes one component gradient per step in the order \(a,b,a,b,\ldots\):
\[
x_{k+1}=x_k-\eta c_k x_k+\beta(x_k-x_{k-1}),\qquad c_{2j}=a,\quad c_{2j+1}=b,
\]
for fixed \(\eta>0\), \(0\le\beta<1\), and arbitrary real \(x_{-1},x_0\). Put
\[
C=\frac{(1+\beta)(a+b)}{ab},\qquad
\Delta=(1+\beta)^2(a-b)^2-4ab(1-\beta)^2.
\]
**Sharp classification.** Every initialization converges to zero exactly for the following stepsizes:

1. When \(\Delta<0\), the entire interval \(0<\eta<C\).
2. When \(\Delta=0\), the interval \(0<\eta<C\) with its center \(\eta=C/2\) deleted.
3. When \(\Delta>0\), the two disjoint intervals
\[
0<\eta<\eta_-\quad\text{or}\quad\eta_+<\eta<C,\qquad
\eta_\pm=\frac{(1+\beta)(a+b)\pm\sqrt\Delta}{2ab}.
\]
All excluded nonnegative stepsizes admit nonconvergent initial states; boundaries are excluded. Thus a larger stepsize can restore convergence after a smaller one has lost it. Writing \(\kappa=\max(a,b)/\min(a,b)\) and \(r=(1-\beta)/(1+\beta)\), the disconnected regime is characterized exactly by
\[
\kappa>\left(r+\sqrt{1+r^2}\right)^2.
\]
At equality there is a single marginally unstable isolated parameter. The cutoff equals \(3+2\sqrt2\) for zero momentum and tends to one as \(\beta\uparrow1\).

**Rate-optimal resonances within the stable region.** For *all* positive curvatures and every fixed admissible momentum, the two explicit stepsizes \(\eta=(1+\beta)/a\) and \(\eta=(1+\beta)/b\) are stable and attain the smallest possible spectral radius \(\rho(P)=\beta\) among all stepsizes. When \(\beta=0\), each of these choices even gives finite-step termination. Thus the large-stepsize island contains an exact phase-cancellation tuning independently of curvature contrast.

For an exact positive-momentum witness take \((a,b,\beta)=(9,1,1/2)\). At \(\eta=1/2\), the two-step transfer has characteristic roots \((-4\pm\sqrt{15})/2\), one outside the unit disk. At the *larger* stepsize \(\eta=3/2\), its two-step matrix is
\[
P=\begin{pmatrix}-1/2&0\\-12&-1/2\end{pmatrix},
\]
so every trajectory converges, despite a first component transition whose coefficient on the current iterate is \(-12\).

## Assumptions and scope
Both components are quadratic, one-dimensional, share the same minimizer, and have strictly positive curvatures. The component order is strictly periodic with period two, and the momentum is the fixed heavy-ball difference term shown above (not velocity momentum with a different parameter convention). All initialization pairs are allowed; “converges” means the actual sequence \(x_k\to0\), including both parity subsequences. The step-size parameter is positive, and \(\beta\in[0,1)\). The two-step stability boundaries are treated as failures of *universal* convergence; some exceptional states may still converge there.

## Proof
Define \(U=1+\beta\), \(R=1-\beta\), and
\[
B_c=\begin{pmatrix}U-\eta c&-\beta\\1&0\end{pmatrix},\qquad
\binom{x_{k+1}}{x_k}=B_{c_k}\binom{x_k}{x_{k-1}}.
\]
The even-phase state after an entire component cycle is transformed by \(P=B_bB_a\), where direct multiplication yields
\[
\det P=\beta^2,\qquad
\operatorname{tr}P=(U-\eta a)(U-\eta b)-2\beta.
\]
Every initialization converges if and only if both eigenvalues of \(P\) have modulus strictly less than one. Indeed this is equivalent to \(P^j\to0\); its odd-step partner is \(B_aP^j\) (up to the phase labeling), which then also tends to zero. If \(P\) has an eigenvalue with modulus at least one, a real eigenvector or the real invariant plane of a complex conjugate pair yields at least one real initial state with no convergence.

For a real quadratic \(z^2-tz+d\), both roots lie in the open unit disk if and only if \(1-d>0\), \(1-t+d>0\), and \(1+t+d>0\) (the strict second-degree Schur/Jury criterion). Since \(\beta\in[0,1)\), the first condition holds automatically. Here the other two inequalities simplify *exactly* to
\[
1-\operatorname{tr}P+\det P
=\eta ab(C-\eta)>0,
\]
\[
1+\operatorname{tr}P+\det P
=ab\left(\eta-\frac C2\right)^2-\frac\Delta{4ab}>0.
\]
The first condition is exactly \(0<\eta<C\). If \(\Delta<0\), the second is strict for every \(\eta\). If \(\Delta=0\), it fails only at the midpoint. For \(\Delta>0\), its forbidden closed interval has endpoints \(\eta_\pm=C/2\pm\sqrt\Delta/(2ab)\); because \(a,b>0\) and \(R>0\), \(\sqrt\Delta<U(a+b)\), so \(0<\eta_-<\eta_+<C\). This proves the complete classification, including all strict endpoint assertions.

To obtain the curvature-ratio threshold, assume without loss that \(a\ge b\), divide \(\Delta>0\) by \(U^2ab\), and rearrange to \((\kappa-1)^2>4\kappa r^2\). With \(w=\sqrt\kappa\ge1\), this is \(w-1/w>2r\), which is equivalent to \(w>r+\sqrt{1+r^2}\). Equality gives the singleton deletion. Direct substitution in the witness gives \(P=\left(\begin{smallmatrix}-1/2&0\\-12&-1/2\end{smallmatrix}\right)\) at \(\eta=3/2\), and trace \(-4\), determinant \(1/4\) at \(\eta=1/2\). The stated eigenvalues follow. Also \(\rho(P)\ge\sqrt{|\det P|}=\beta\) for every parameter, because the moduli of the eigenvalues multiply to \(\beta^2\). At \(\eta=U/a\) or \(\eta=U/b\), one factor in \((U-\eta a)(U-\eta b)\) vanishes, so \(\operatorname{tr}P=-2\beta\), while \(\det P=\beta^2\); both characteristic roots are then \(-\beta\). This achieves the global minimum \(\rho(P)=\beta<1\). If \(\beta=0\), the resulting \(2\times2\) matrix is nilpotent and hence gives exact finite termination after at most two component cycles. All proofs are finite-dimensional exact algebra; no numerical inference is required.

## Verification
Run `python3 verify.py` using Python's standard library. It reconstructs each one-step and two-step matrix with exact rational arithmetic, checks the trace, determinant, both Schur factorizations, and the interval condition for 5000 distinct rational parameter tuples. It also confirms both exact witness matrices and their classification. The program's `VERIFY_OK` output is a finite consistency check only; the all-parameter theorem follows from the algebraic proof above.

## Relationship to prior work
The heavy-ball formulation and full-gradient convergence theory are established in E. Ghadimi, H. R. Feyzmahdavian and M. Johansson, *Global convergence of the Heavy-ball method for convex optimization*, original arXiv submission 23 December 2014. The submitted work analyzes a full-gradient update, not alternating component curvatures. P. Tseng's *An incremental gradient(-projection) method with momentum term and adaptive stepsize rule* (1998) already studies incremental momentum; its displayed algorithm uses an adaptive stepsize safeguard, and the accessible material does not identify this exact fixed-stepsize, period-two stability phase diagram. The finite-sum perspective and sequential/randomized processing precede the present calculation, including A. Defazio, F. Bach and S. Lacoste-Julien, *SAGA: A Fast Incremental Gradient Method With Support for Non-Strongly Convex Composite Objectives* (2014), whose stored-gradient algorithm is distinct. J. Qiu and A. Milzarek, *Random Reshuffling with Momentum for Nonconvex Problems* (2024), consider stochastic reshuffling and asymptotic/complexity guarantees, not this deterministic fixed-order sharp all-initialization boundary in the accessible material. The Schur criterion and Floquet matrix reduction themselves are standard and not claimed as original. The contribution here is the complete explicit order-two incremental-optimization boundary and its disconnected/isolated-point phase classification.

## Limitations
The result concerns only scalar, centered, two-component strongly convex quadratics and deterministic alternating order. It does not establish comparable disconnected regions in higher dimensions, nonquadratic objectives, independently resampled component orders, or differing component minimizers. Isolated instability points are universal convergence failures, not assertions that every state diverges. The return of stability at high stepsizes can be accompanied by large intermediate amplification and is not a robustness or finite-precision recommendation. Prior equivalent expressions might exist in older incremental-momentum, switched-recursion, or Floquet literature; novelty requires external scholarly validation.

## References
1. E. Ghadimi, H. R. Feyzmahdavian, M. Johansson, *Global convergence of the Heavy-ball method for convex optimization*, arXiv:1412.7457v1 (23 December 2014), https://arxiv.org/abs/1412.7457.
2. P. Tseng, *An Incremental Gradient(-Projection) Method with Momentum Term and Adaptive Stepsize Rule*, SIAM Journal on Optimization 8 (1998), 506–531, DOI 10.1137/S1052623495294797.
3. A. Defazio, F. Bach, S. Lacoste-Julien, *SAGA: A Fast Incremental Gradient Method With Support for Non-Strongly Convex Composite Objectives*, NeurIPS 2014, arXiv:1407.0202.
4. J. Qiu, A. Milzarek, *Random Reshuffling with Momentum for Nonconvex Problems: Iteration Complexity and Last Iterate Convergence*, arXiv:2404.18452 (2024).
