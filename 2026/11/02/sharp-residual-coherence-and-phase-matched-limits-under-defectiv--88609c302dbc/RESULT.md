# Sharp residual coherence and phase-matched limits under defective quantum resetting

## Finding

A summable age-dependent reset hazard can cause nonstationary discrete-time quantum evolution, but not merely because some trajectories never reset. In the full-state quantum reset protocol below, *every trajectory performs only finitely many resets almost surely*, and the ensemble approaches a single unitary orbit whose entire spectrum is computable from the last-reset time. At every nonzero spectral gap, coherence retains at least a sharp proportion \(p/(2-p)\) of its original complex amplitude, where \(p\) is the probability of never resetting after a fresh start. For a gate with opposite eigenphases, every residual fraction in this permitted interval is realizable by an elementary two-step protocol.

Specifically, let \(U=\sum_{u}uP_u\) be unitary on a finite-dimensional Hilbert space and let \(\rho_0\) be any density matrix. The protocol applies \(\rho\mapsto U\rho U^\dagger\) unless a reset to \(\rho_0\) occurs, with probability \(r_n\) after \(n\) successive nonreset updates. Assume \(0\le r_n<1\) for every \(n\) and

\[
p:=\prod_{n=0}^{\infty}(1-r_n)>0.
\]

Define the defective first-reset masses and their transform by

\[
f_k:=r_{k-1}\prod_{j=0}^{k-2}(1-r_j),\quad
F(z):=\sum_{k=1}^{\infty}f_kz^k,\quad
G(z):=\frac{p}{1-F(z)},\qquad |z|\le1.
\]

Here an empty product equals one and \(\sum_{k\ge1}f_k=1-p\). There is an almost surely finite *last* reset time \(L\), with \(L=0\) if no reset ever occurs, such that \(\mathbb E[z^L]=G(z)\). Let \(\rho_t\) be the ensemble density matrix after \(t\) updates. Then

\[
\left\|U^{-t}\rho_tU^t-\sigma\right\|_1\le2\mathbb P(L>t)\longrightarrow0,
\qquad
\sigma=\mathbb E\!\left[U^{-L}\rho_0U^L\right].
\]

In any orthonormal eigenbasis of \(U\) with eigenvalues \(u_i\),

\[
\sigma_{ij}=(\rho_0)_{ij}\,G(u_j/u_i),\qquad
\boxed{\frac{p}{2-p}\le|G(z)|\le1\quad (|z|=1).}
\]

The bounds are optimal among all such protocols (for the relative phase \(z=-1\)). For that phase there is a complete sharp range:

\[
\boxed{\{G(-1)\colon\text{protocols with fixed }p\}
=\left[\frac{p}{2-p},1\right].}
\]

The strong-limit and time-averaged classifications are

\[
\boxed{\rho_t\text{ converges}\ \Longleftrightarrow\ [U,\rho_0]=0},
\qquad
\boxed{\lim_{T\to\infty}\frac1T\sum_{t=0}^{T-1}\rho_t
=\sum_{u}P_u\rho_0P_u}.
\]

The final sum runs over *distinct* eigenvalues and retains all coherences inside each degenerate eigenspace.

## Assumptions and scope

Time \(t\) is a nonnegative integer; the reset age increments by one on a unitary update and returns to zero on a reset. After each reset, a fresh sequence of independent reset decisions is used, with the same age-dependent hazards. The reset state equals the initial density matrix. There is no continuous environmental decoherence or intermediate measurement back-action other than the reset itself. For the sharp range, \(p\in(0,1]\), with the trivial \(p=1\) endpoint allowed.

The trace norm is \(\|X\|_1=\operatorname{tr}\sqrt{X^\dagger X}\). The eigenphases \(u\) lie on the complex unit circle. Summability \(\sum_n r_n<\infty\) is sufficient for \(p>0\) under \(r_n<1\); only the product positivity is needed for the theorem.

## Proof

**1. Renewal escape and last finite reset.** From a fresh reset, the probability of not resetting during the next \(n\) updates is \(S_n=\prod_{j=0}^{n-1}(1-r_j)\), with \(S_0=1\) and \(S_\infty=p\). First-reset time \(X\) has defective mass \(\Pr(X=k)=f_k=S_{k-1}r_{k-1}\) for \(k\ge1\), and \(\Pr(X=\infty)=p\). Successive post-reset waits are independent copies of \(X\). The number \(K\) of *finite* inter-reset waiting periods before the first infinite wait is geometric, \(\Pr(K=k)=p(1-p)^k\) for \(k\ge0\). Conditional on finiteness, each wait has distribution \(\Pr(X=j\mid X<\infty)=f_j/(1-p)\) (for \(p<1\)). The final reset epoch is \(L=X_1+\cdots+X_K<\infty\) almost surely (empty sum zero). Directly summing the finite convolution masses gives

\[
\mathbb E[z^L]
=\sum_{k=0}^{\infty}p\left(\sum_{j\ge1}f_jz^j\right)^k
=\frac{p}{1-F(z)}=G(z),\qquad |z|\le1.
\]

The denominator never vanishes since \(|F(z)|\le\sum_j f_j=1-p<1\).

**2. Pathwise coupling and Fourier filter.** Let \(\tau_t\le t\) denote the most recent reset epoch at or before \(t\), putting \(\tau_t=0\) if no reset has occurred. Along each history its density matrix at \(t\) equals \(U^{t-\tau_t}\rho_0U^{-(t-\tau_t)}\). On the event \(L\le t\), we have \(\tau_t=L\); on the complementary event both evolved density matrices have trace norm one. Taking expectations after conjugating by \(U^{-t}\), the triangle inequality proves

\[
\left\|U^{-t}\rho_tU^t-\mathbb E[U^{-L}\rho_0U^L]\right\|_1
\le 2\Pr(L>t)\longrightarrow0.
\]

For eigenvectors \(U|i\rangle=u_i|i\rangle\), the \((i,j)\) entry of \(U^{-L}\rho_0U^L\) is \((\rho_0)_{ij}(u_j/u_i)^L\). Taking expectation proves the spectral formula.

**3. Strict coherence floor and optimal protocol range.** For \(|z|=1\), \(|F(z)|\le1-p\), whence

\[
p\le|1-F(z)|\le2-p,
\quad \frac{p}{2-p}\le|G(z)|\le1.
\]

For \(z=-1\), the transform \(F(-1)\) is real, so \(G(-1)>0\). Fix any \(q\in[0,1-p]\) and choose

\[
r_0=q,\quad
r_1=\frac{1-p-q}{1-q},\quad
r_n=0\ (n\ge2).
\]

Then \(f_1=q\), \(f_2=1-p-q\), the escape probability equals \(p\), and

\[
G(-1)=\frac{p}{p+2q}.
\]

As \(q\) ranges from \(0\) to \(1-p\), this continuously exhausts the entire interval \([p/(2-p),1]\). Hence both universal bounds are sharp *without claiming* that the lower bound is attained for each fixed phase \(z\ne-1\). Protocols with all hazards strictly positive can approximate these endpoint schedules, so the sharp envelope survives that restriction as an infimum/supremum.

**4. Pointwise versus Cesàro limits.** The error estimate in step 2 gives \(\rho_t=U^t\sigma U^{-t}+o_{\|\cdot\|_1}(1)\). Consequently,

\[
\lim_{t\to\infty}\|\rho_{t+1}-\rho_t\|_1
=\|U\sigma U^\dagger-\sigma\|_1.
\]

This is zero exactly when \([U,\sigma]=0\). Since \(G(u_j/u_i)\ne0\) for every eigenvalue pair, \([U,\sigma]=0\) exactly when \([U,\rho_0]=0\). In that case every trajectory stays at \(\rho_0\). Otherwise the nonzero limit of consecutive differences rules out convergence. Finally, Cesàro averaging the finite-dimensional unitary orbit suppresses each phase \(u_i/u_j\ne1\) and preserves every phase equal to one, yielding \(\sum_u P_u\sigma P_u\). But \(G(1)=\mathbb E[1^L]=1\), so this equals \(\sum_u P_u\rho_0P_u\). The trace-norm \(o(1)\) error has vanishing Cesàro average as well.

**5. Exact strictly positive power-law witness and rate.** Take \(r_n=(n+2)^{-2}\) for every \(n\ge0\). The telescoping survival product, defective masses and transform are

\[
S_n=\frac{n+2}{2(n+1)},\qquad p=\frac12,\qquad
f_k=\frac{1}{2k(k+1)},\qquad
F(z)=\frac12\left[1+\frac{1-z}{z}\log(1-z)\right],
\]

where the displayed formula for \(F\) extends continuously to \(z=0\), and at \(z=1\) by the series. In particular

\[
G(-1)=\frac{1}{1+2\log2}.
\]

For \(U=\operatorname{diag}(1,-1)\) and \(\rho_0=|+\rangle\langle+|\), with \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\), the density matrix obeys

\[
\rho_t=\frac12\begin{pmatrix}
1&(-1)^t/(1+2\log2)\\
(-1)^t/(1+2\log2)&1
\end{pmatrix}+o_{\|\cdot\|_1}(1).
\]

Thus \(\lim_{t\to\infty}\|\rho_{t+1}-\rho_t\|_1=2/(1+2\log2)\), while its Cesàro mean is the maximally mixed qubit state. For a finite inter-reset wait, the exact conditional tail satisfies \(\Pr(X>m\mid X<\infty)=1/(m+1)\) for integers \(m\ge0\). If \(K=k\) and the sum of waits exceeds integer \(t\ge1\), some wait exceeds \(t/k\); the union bound therefore gives \(\Pr(L>t\mid K=k)\le k^2/t\). Because \(K\) is geometric with \(p=1/2\), \(\mathbb E[K^2]=3\). Hence

\[
\Pr(L>t)\le\frac3t,\qquad
\left\|U^{-t}\rho_tU^t-\sigma\right\|_1\le\frac6t
\quad\text{for all integers }t\ge1.
\]

## Verification

The included standalone `checker.py` implements a direct renewal-age recursion independently of the transform calculation, verifies the survival product and first-reset masses against exact telescoping formulas, checks the complex generating function against long finite series, tests the sharp extremal schedules and compares co-rotating finite-time amplitudes with the analytic limit at several unrelated eigenphases. Its finite checks passed. Run from the extracted directory using `python checker.py` with Python 3 and NumPy. None of these finite calculations is claimed as the proof of a statement for all times or dimensions; the preceding analytic arguments are the proof.

## Relationship to prior work

Wald, Yao, Platini, Hooley and Carollo [1], Secs. II and IV and Appendix C, define the same age-hazard discrete-time quantum reset process, its last-renewal relation, and the nonvanishing no-reset probability for fast-decaying hazards; their study discusses nonexistence of stationary states and numerical examples. The theorem here uses their model but determines the *exact surviving moving unitary orbit*, an all-phase nonzero coherence filter, a sharp fixed-escape probability bound with full interval attainability at phase \(\pi\), a necessary-and-sufficient ensemble convergence criterion, and a reset-independent Cesàro limit. The later published version [2] has also been compared. Carollo and Wald [3] develop non-Markovianity and last-renewal dynamical maps, not the sharp residual phase filter or its attained optimization. Michelitsch and collaborators [4] treat classical graph walks under renewal resetting; their propagator and ergodicity questions differ from unitary quantum phase coherence. Rose and collaborators [5] address constant-rate Markovian resetting; the available abstract does not establish this defective renewal theorem. The construction uses standard renewal and spectral ideas; a more general unpublished or differently worded defective-renewal theorem may subsume part of it.

## Limitations

The result assumes full identical-state resetting and a fixed finite-dimensional *unitary* gate. It does not address partial resetting, nonunitary channels, state-dependent hazards, external decoherence, or the regime \(p=0\). The bound \(p/(2-p)\) is globally sharp across phase/hazard choices, not necessarily sharp at each fixed eigenphase. For general hazards only convergence without an explicit numerical rate is claimed; the \(6/t\) estimate holds for the displayed square-decay protocol. The mathematical analysis does not constitute an experimental demonstration or independent publication-priority certification.

## References

1. S. Wald, L. H. Yao, T. Platini, C. Hooley, and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497v1, first publicly posted 15 October 2024. https://arxiv.org/html/2410.11497v1
2. Same authors, arXiv:2410.11497v3, 9 May 2025. https://arxiv.org/html/2410.11497v3
3. F. Carollo and S. Wald, *Stochastic resetting induces quantum non-Markovianity*, arXiv:2601.13367v1 (2026). https://arxiv.org/html/2601.13367v1
4. T. M. Michelitsch, G. D'Onofrio, F. Polito, and A. P. Riascos, *Random walks with stochastic resetting in complex networks: a discrete time approach*, arXiv:2409.08394v1 (2024). https://arxiv.org/html/2409.08394v1
5. D. C. Rose, H. Touchette, I. Lesanovsky, and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, Phys. Rev. E 98, 022129 (2018), DOI:10.1103/PhysRevE.98.022129. https://doi.org/10.1103/PhysRevE.98.022129
