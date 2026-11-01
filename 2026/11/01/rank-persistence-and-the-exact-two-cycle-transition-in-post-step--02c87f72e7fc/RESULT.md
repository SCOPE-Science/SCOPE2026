# Rank persistence and the exact two-cycle transition in post-step spectral decay

## Finding
Consider the exact-polar post-step spectral-weight-decay update for a centered matrix quadratic. Except at one gradient stepsize resonance and a countable set of initial singular values, the method **preserves rank** and drives every surviving singular value to the *same positive number*, although the strictly convex nuclear-regularized objective has the zero matrix as its unique minimizer. Below the gradient resonance the matrices approach a nonzero two-cycle; above it they converge to a nonzero fixed point that is a scalar multiple of a partial isometry.

Precisely, let \(a,\lambda>0\), \(\eta>0\), \(0<\eta a<2\), and let \(W_0\in\mathbb R^{m\times n}\), with arbitrary positive integers \(m,n\). Set \(q=1-\eta a\), \(\tau=\eta\lambda\), and, for a compact SVD \(Z=U\Sigma V^{\mathsf T}\), put \(Q(Z)=UV^{\mathsf T}\) if \(Z\ne0\), with \(Q(0)=0\). With the usual zero action on the kernel, \(Q\) is the minimum-Frobenius-norm nuclear-norm subgradient. The exact-polar iteration is
\[
Z_k=qW_k,\qquad W_{k+1}=Z_k-\tau Q(Z_k).
\]
For \(q=0\), \(W_1=0\) for every input. For \(q\ne0\), write \(s=|q|\in(0,1)\) and
\[
c=\frac{\tau}{1+s},\qquad R_j=\frac{\tau(s^{-j}-1)}{1-s}\quad(j=1,2,\ldots).
\]
Every initially positive singular value equal to some \(R_j\) vanishes at iteration \(j\) and remains zero. All other initially positive singular values stay nonzero at every finite iteration and converge to \(c\), satisfying
\[
|\sigma_k-c|\le s^k|\sigma_0-c|.
\]
If \(r\) is the number, with multiplicity, of the latter nonresonant positive initial singular values, then for all sufficiently large \(k\), \(\operatorname{rank}(W_k)=r\), and
\[
\|W_k\|_{\mathrm F}\longrightarrow c\sqrt r,\qquad
\|W_k\|_*\longrightarrow cr.
\]
For \(r>0\), both stable rank and entropy-based effective rank tend to \(r\), while the regularized objective has the strictly positive asymptotic gap \(F(W_k)\to r(ac^2/2+\lambda c)\). If \(0<\eta a<1\), the even and odd matrix subsequences converge to opposite rank-\(r\) matrices whose nonzero singular values all equal \(c\). If \(1<\eta a<2\), the full matrix sequence converges to a rank-\(r\) matrix with these singular values. Explicitly,
\[
c=\begin{cases}
\displaystyle\frac{\eta\lambda}{2-\eta a},&0<\eta a<1,\\[4pt]
\displaystyle\frac{\lambda}{a},&1<\eta a<2.
\end{cases}
\]
Thus the nonzero asymptotic spectral floor tends to \(\lambda/a\) from either side of \(\eta a=1\), but is **exactly zero** at that stepsize. The full-rank initial matrices avoiding all resonance singular values form an open dense set of full Lebesgue measure: each resonance is a proper singular-value polynomial hypersurface, and the resonance radii tend to infinity. For these generic inputs the limiting effective rank is \(\min(m,n)\), not a reduced rank.

## Assumptions and scope
The objective is \(F(W)=a\|W\|_{\mathrm F}^2/2+\lambda\|W\|_*\), uniquely minimized at \(W=0\). The gradient step acts on the smooth quadratic term, and the subtraction uses the **exact** partial polar factor of the provisional matrix. Rank is the exact-arithmetic rank, not a finite-tolerance numerical rank. At zero singular values the chosen minimum-norm subgradient is zero. The result allows arbitrary rectangular dimensions, repeated initial singular values, and rank deficiency. It does not describe an approximate Newton--Schulz polar factor, adaptive optimizer, noisy gradient, or nonzero data target.

For a nonzero matrix with singular values \(\sigma_1,\ldots,\sigma_r\), effective rank means \(\exp(-\sum_j p_j\log p_j)\), where \(p_j=\sigma_j/\sum_i\sigma_i\), and stable rank means \(\|W\|_{\mathrm F}^2/\|W\|_2^2\). Both are defined only when \(W\ne0\).

## Proof
Choose the initial compact SVD \(W_0=U\operatorname{diag}(d_1,\ldots,d_{r_0})V^{\mathsf T}\). Inductively every iterate can be expressed in the **same** left and right singular bases as \(W_k=U\operatorname{diag}(x_{1,k},\ldots,x_{r_0,k})V^{\mathsf T}\), allowing signed coefficients. Exact polar-factor calculus then gives the independent scalar recursions
\[
x_{j,k+1}=q x_{j,k}-\tau\operatorname{sgn}(q x_{j,k})
\]
when \(q x_{j,k}\ne0\), and zero when it vanishes. Hence \(r_{j,k}=|x_{j,k}|\) obeys, until any zero is reached,
\[
r_{j,k+1}=h(r_{j,k}),\qquad h(r)=|sr-\tau|.
\]
The function \(h:[0,\infty)\to[0,\infty)\) is \(s\)-Lipschitz and has the unique positive fixed point \(c=\tau/(1+s)\). This yields the displayed exponential contraction bound for every orbit that avoids zero.

A positive radius maps to zero precisely when it equals \(R_1=\tau/s\). A preimage of \(y>\tau\) under \(h\) is uniquely \((y+\tau)/s\), because the other absolute-value branch takes values at most \(\tau\) on the nonnegative half-line. Since \(R_1>\tau\), induction gives the unique positive \(j\)-step preimage \(R_j\), with the asserted formula. A zero radius stays zero by the convention on \(Q(0)\). All nonresonant positive radii remain positive and converge to \(c\).

Because \(c<\tau/s\), each surviving radius eventually lies permanently below \(\tau/s\). For \(q>0\), the signed scalar recursion then changes the sign of every nonzero coefficient at each step; the positive radii converge to \(c\), giving opposite limits along even and odd subsequences. For \(q<0\), the signed recursion then preserves the sign of each nonzero coefficient, giving one limit. Zeros remain absent from the surviving block, and the number of positive singular values is eventually \(r\). The formulas for the norms and effective ranks follow directly from convergence of the surviving singular values. The piecewise expression for \(c\) is obtained by substituting \(s=|1-\eta a|\). The case \(q=0\) follows immediately from \(Z_k=0\).

For comparison, the genuine nuclear proximal-gradient update replaces the polar subtraction by singular-value soft thresholding. Its radial map is \(r\mapsto\max(sr-\tau,0)\), whose \(k\)-fold iterate is \(\max(s^k r-\tau(1-s^k)/(1-s),0)\). Every finite input therefore reaches zero in finitely many steps. This proves the asserted qualitative difference without attributing it to approximation error in computing the polar factor.

## Verification
Run `python verify.py` with Python 3, NumPy, and its standard-library `fractions` module. The script checks the exact resonance formula and scalar contraction on rational parameters, reproduces the signed polar-coordinate recursion, independently iterates dense rectangular matrices using numerical SVD polar factors, and contrasts genuine proximal soft thresholding. A local execution returned `CHECKS_OK 156222`. Numerical tests corroborate the algebra but are not used to prove convergence or rule out exceptional initial values.

As explicit examples, \(\eta a=1/2\) gives a generic two-cycle with singular-value magnitude \(\lambda/(3a)\); \(\eta a=3/2\) gives a fixed point with singular-value magnitude \(\lambda/a\); and \(\eta a=1\) sends every input to zero in one step. These examples are consequences, not replacements for the proof.

## Relationship to prior work
Andriianov, Veprikov and Beznosikov (arXiv:2610.11730, publicly submitted 2026-10-08) define the decoupled post-step spectral correction, identify the un-clipped crossing of singular values through zero, and analyze one-step order sensitivity. Their main-text Section 4 and Appendix A describe the update and compare it with exact soft thresholding, but do not state this complete repeated-iterate, exceptional-radius, and stepsize-regime classification for the centered quadratic. Ordinary constant-step subgradient methods are already known to exhibit chattering; no claim is made to invent the scalar overshoot mechanism. The distinction here is the exact **matrix rank, spectral equalization, and polar-step resonance law** for the particular proposed update.

Becker's 2026 polar-decomposition reduction computes true singular-value *soft thresholding* and is therefore not equivalent to un-clipped polar subtraction. Earlier proximal thresholding convergence theory covers the genuinely proximal map, which has a different radial recurrence. Other published exact SVT rank-staircase results concern a matrix-completion dual update, not the post-gradient polar step. Related polar-gradient exact-line-search results concern a different step normalization and do not imply the fixed-step map above.

## Limitations
These are exact-polar, fixed-stepsize, homogeneous quadratic dynamics, not claims about training neural networks, approximate matrix signs, stochastic optimizers, or the finite training horizons investigated in the motivating paper. Close to a resonance an arbitrarily small perturbation changes exact finite-time rank collapse into persistent nonzero rank; no finite-precision rank guarantee follows. The scalar mechanism is elementary, and a broad historical proof of the same specialized classification may exist despite the targeted checks. Independent mathematical verification remains outstanding.

## References
1. D. Andriianov, A. Veprikov, and A. Beznosikov, *Spectral Weight Decay: Inducing Low-Rank Structure in Neural Network Weights*, arXiv:2610.11730 (first public 2026-10-08), https://arxiv.org/abs/2610.11730. Readable manuscript text: https://www.paperpeel.com/paper/2610.11730, especially Section 4 and Appendix A.
2. S. Becker, *Singular value soft-thresholding via the polar decomposition*, arXiv:2607.22484 (2026), https://arxiv.org/abs/2607.22484.
3. P. L. Combettes and J.-C. Pesquet, *Proximal Thresholding Algorithm for Minimization over Orthonormal Bases*, SIAM Journal on Optimization 18 (2007), 1351–1376, https://doi.org/10.1137/060669498.
4. *Finite-Time Nonsmooth Convergence of Signum and Muon*, https://www.lamda.nju.edu.cn/yudz/finite-time-nonsmooth-signum-muon.html (related sign-based cycling on different objectives).
