# Phase-dependent Brownian clocks for critically modulated elephant walks

## Finding
A periodically oscillating deviation of size \(1/\log n\) from the critical memory strength \(3/4\) produces a *phase-indexed family* of Brownian functional limits on logarithmic time. More precisely, under the assumptions below, let \(b_n\), \(K\), \(H\), and \(\phi_N\) be the deterministic quantities defined there. For any \(T>0\) and any integer sequence \(N_j\to\infty\) along which \(\phi_{N_j}\to\phi\) modulo \(2\pi\),
\[
 \left(\frac{b_{\max(1,\lfloor N_j^t\rfloor)}S_{\max(1,\lfloor N_j^t\rfloor)}}{K\sqrt{\log N_j}}\right)_{0\le t\le T}
 \Longrightarrow \bigl(W(\Lambda_\phi(t))\bigr)_{0\le t\le T}
\]
in the \(J_1\) topology of \(D([0,T])\), where \(W\) is standard Brownian motion and
\[
 \Lambda_\phi(0)=0,\qquad
 \Lambda_\phi(t)=\int_0^t \exp\{-4H(\phi+\log u)\}\,du\quad(t>0).
\]
The covariance of this limit is \(\Lambda_\phi(\min\{s,t\})\). For every \(t>0\), the clock is differentiable and strictly increasing, and its derivative recovers the oscillating memory profile:
\[
 h(\phi+\log t)=-\frac{t}{4}\frac{d}{dt}\log \Lambda_\phi'(t).
\]
All phases are attained by integer subsequences. Phase symmetries of \(h\) can identify some clocks, but if \(h(\theta)=c\sin\theta\) with \(c\ne0\), every pair of distinct phases modulo \(2\pi\) yields distinct clocks.

At ordinary physical time, the same model obeys a different consequence:
\[
 \frac{S_{N_j}}{\sqrt{N_j\log N_j}}\Longrightarrow
 \mathcal N\bigl(0,F_h(\phi)\bigr),\qquad
 F_h(\phi)=e^{4H(\phi)}\int_0^1e^{-4H(\phi+\log u)}\,du.
\]
The positive periodic function \(F_h\) uniquely satisfies the periodic first-order equation
\[
 F_h'(\phi)=1-\bigl(1-4h(\phi)\bigr)F_h(\phi).
\]
If \(h\) is not identically zero, \(F_h\) is not constant. Hence the single deterministic scale \(\sqrt{n\log n}\) has a continuum of distinct Gaussian subsequential limits and **no full-sequence weak limit**, although the repetition probabilities themselves converge to the critical value. The one-time Gaussian marginal at a specified phase is compatible with existing general scalar martingale CLTs; the distinguishing statement here is the functional phase-resolved clock law and its inversion.

## Assumptions and scope
Take a real continuously differentiable, \(2\pi\)-periodic function \(h\) with \(\int_0^{2\pi}h(v)\,dv=0\), and write \(H(x)=\int_0^x h(v)\,dv\); therefore \(H\) is periodic and bounded. Select an integer \(n_0\ge3\) large enough that \(0<3/4+h(\log\log n)/\log n<1\) for every \(n\ge n_0\). Define the deterministic repetition probabilities by
\[
 p_n=\begin{cases}3/4,&1\le n<n_0,\\3/4+\dfrac{h(\log\log n)}{\log n},&n\ge n_0.\end{cases}
\]
Start with a symmetric first increment \(X_1\in\{-1,+1\}\). Conditional on \(X_1,\ldots,X_n\), independently sample one of the \(n\) past increments uniformly; set \(X_{n+1}\) equal to it with probability \(p_n\), otherwise to its negative. Define \(S_n=\sum_{k=1}^nX_k\), \(a_n=2p_n-1\), and
\[
 b_1=1,\quad b_{n+1}=\frac{b_n}{1+a_n/n},\quad
 K=\lim_{n\to\infty}\sqrt n\,b_n e^{2H(\log\log n)}.
\]
The proof establishes that \(K\in(0,\infty)\). All logarithms are natural. Interpret \(\phi_N=\log\log N\pmod{2\pi}\) only for \(N\ge3\). The conclusions apply to any fixed finite time horizon \(T\); they do not assert convergence for arbitrary time-varying memory sequences beyond this smooth periodic class.

## Proof
**1. Deterministic martingale scale.** For the natural filtration \(\mathcal F_n\),
\[
 \mathbb E[X_{n+1}\mid\mathcal F_n]=\frac{a_nS_n}{n}.
\]
Thus \(M_n=b_nS_n\) is a martingale, and its increments have exact identities
\[
 \Delta M_{n+1}=b_{n+1}\left(X_{n+1}-\frac{a_nS_n}{n}\right),\qquad
 \mathbb E[(\Delta M_{n+1})^2\mid\mathcal F_n]=b_{n+1}^2\left(1-\frac{a_n^2S_n^2}{n^2}\right).
\]
In particular \(|\Delta M_{n+1}|\le2b_{n+1}\). From \(\log(1+z)=z+O(z^2)\) uniformly for \(|z|\le 1/2\),
\[
 \log b_n=-\frac12\sum_{k<n}\frac1k-2\sum_{n_0\le k<n}\frac{h(\log\log k)}{k\log k}+C_0+o(1).
\]
The first sum equals \(\log n\) plus a convergent constant and \(o(1)\). For \(g(x)=h(\log\log x)/(x\log x)\), \(\int_{n_0}^{\infty}|g'(x)|\,dx<\infty\) by boundedness of \(h,h'\); therefore the difference between its sum and integral converges. Substitution \(v=\log\log x\) gives
\[
 \sum_{n_0\le k<n}\frac{h(\log\log k)}{k\log k}=H(\log\log n)+C_1+o(1).
\]
Consequently \(\log b_n=-\tfrac12\log n-2H(\log\log n)+\log K+o(1)\), proving the stated finite, positive \(K\) and
\[
 b_n^2=\frac{K^2}{n}e^{-4H(\log\log n)}(1+o(1)),\qquad c\,n^{-1/2}\le b_n\le C\,n^{-1/2}
\]
for positive finite constants \(c,C\) and all \(n\).

**2. Quadratic-variation error is summable.** Orthogonality of martingale increments gives \(\mathbb E[M_n^2]\le\mathbb E[M_1^2]+\sum_{k=2}^nb_k^2=O(\log n)\). Since \(b_n^{-2}=O(n)\), \(\mathbb E[S_n^2]=O(n\log n)\). Therefore
\[
 \sum_{n\ge2}\mathbb E\left[b_{n+1}^2a_n^2\frac{S_n^2}{n^2}\right]
 \le C\sum_{n\ge2}\frac{\log n}{n^2}<\infty.
\]
The nonnegative random sum of these terms is finite almost surely. In particular, the compensator of the bracket discrepancy from the deterministic sum is \(O(1)\) almost surely, uniformly in the terminal time. This is substantially stronger than the \(o(\log N)\) control needed below.

**3. Entire deterministic clock.** Set \(f(v)=e^{-4H(v)}\), a positive bounded periodic continuous function. With \(\phi_N=\log\log N\pmod{2\pi}\), for each \(t\in[0,T]\), the deterministic bracket has the approximation
\[
 \frac1{K^2\log N}\sum_{k=2}^{\max(1,\lfloor N^t\rfloor)}b_k^2
 =\int_0^t f(\phi_N+\log u)\,du+o(1).
\]
The error is uniform in \(t\in[0,T]\). To see this, discard finitely many indices and bound the remaining relative \(o(1)\) error in the asymptotic formula for \(b_k^2\); the sum contributes at most \(O(\log N)\). Replace the remaining \(1/k\) sum by its logarithmic integral (a bounded accumulated discretization error follows from the derivative bound for \(f(\log\log x)/x\)). The change of variables \(u=\log x/\log N\) produces the displayed integral. The interval near \(u=0\) has integral bounded by \(\|f\|_\infty\delta\), giving uniformity at the origin. If \(\phi_{N_j}\to\phi\), periodicity, continuity and dominated convergence yield uniform convergence of those cumulative integrals to \(\Lambda_\phi\); uniformity also follows from their common Lipschitz bound \(\|f\|_\infty\).

**4. Martingale functional limit.** For the triangular process \(K^{-1}(\log N_j)^{-1/2}M_{\max(1,\lfloor N_j^t\rfloor)}\), the predictable quadratic variation converges in probability uniformly to \(\Lambda_\phi(t)\) by steps 2–3. All normalized jumps are bounded by \(2\sup_nb_n/(K\sqrt{\log N_j})\to0\), so the martingale Lindeberg condition holds for every positive threshold. The martingale functional central limit theorem (predictable-bracket formulation) gives weak convergence in \(D([0,T])\) to the continuous Gaussian martingale \(W\circ\Lambda_\phi\), with covariance \(\Lambda_\phi(s\wedge t)\). The value at \(t=0\) tends to zero. Brownian scaling is fixed by the normalized bracket and requires no independence of the original increments.

**5. Entire phase set, physical-time marginals, and inverse law.** Each phase is attained: choose integers \(N_j\) nearest to \(\exp(\exp(2\pi j+\phi))\), whose \(\log\log\) phases converge to \(\phi\). At \(t=1\), step 1 and the martingale limit imply the physical-time variance \(F_h(\phi)=e^{4H(\phi)}\Lambda_\phi(1)\). With \(v=-\log u\),
\[
 \Lambda_\phi(1)=\int_0^\infty e^{-v}f(\phi-v)\,dv.
\]
Differentiating under the integral and integrating by parts shows \(U'(\phi)+U(\phi)=f(\phi)\) for \(U(\phi)=\Lambda_\phi(1)\). Hence \(F_h'=4hF_h+e^{4H}(f-U)=1-(1-4h)F_h\). Were \(F_h\) constant, this identity would force \(h\) constant; its zero mean then forces \(h\equiv0\). For nonzero \(h\), the continuous periodic \(F_h\) has a nontrivial interval of values. Distinct variance values give distinct centered Gaussian distributions; a full weak limit at scale \(\sqrt{n\log n}\) would contradict those differing subsequences.

Finally \(\Lambda_\phi'(t)=f(\phi+\log t)\) and differentiating its logarithm yields the inverse formula in the finding. If \(h(\theta)=c\sin\theta\ne0\), two phases with identical clocks would imply \(\sin(\theta+\phi_1)=\sin(\theta+\phi_2)\) for all real \(\theta\), forcing \(\phi_1\equiv\phi_2\pmod{2\pi}\).

## Verification
The standalone file `verify.py` checks exact finite-history conditional means and variances using rational arithmetic, and numerically tests the phase-clock derivative, periodic variance ODE, inverse reconstruction, first-order small-amplitude expansion, and convergence of finite products to their predicted oscillatory asymptotics. Run `python verify.py` with Python 3, NumPy, and SciPy. The program reports 378 exact rational identities and 244 numerical clock identities, plus three larger finite-product comparisons. These finite checks do not prove the functional central limit theorem; the proof rests on the deterministic product asymptotic, summable random bracket error, and martingale functional CLT.

## Relationship to prior work
Fan and Qi (2026, arXiv:2610.16065v1) introduce the time-dependent repetition model and establish scalar martingale central limit theorems and strong laws. Their general scalar CLT, together with a separately evaluated normalization, already yields Gaussian convergence at a chosen final-time subsequence; we do not claim a new general scalar CLT. Baur and Bertoin (2016, arXiv:1608.01305), and Tokumitsu (2026, arXiv:2603.13690), establish functional elephant-walk limits for **constant** repetition probabilities. In particular their critical limit is the \(h\equiv0\) specialization of the present functional result. The distinct contribution here is a time-inhomogeneous critical window in which the *entire logarithmic-time covariance clock oscillates with phase*, together with an explicit inversion of its derivative and nonconvergence under a fixed physical-time normalization. James, James and Qi (2008) give scalar limit theorems for a related time-varying correlated Bernoulli model. None of these compared theorem statements yields the displayed time-varying functional clock directly. General martingale FCLTs are the method of proof, not claimed as new.

## Limitations
The memory perturbation must have the specified smooth zero-mean periodic form; no assertion is made for arbitrary time dependence. The law of \(\sqrt{n\log n}\)-scaled positions has phase-dependent subsequential Gaussian limits, not a full limit, when \(h\not\equiv0\). Clock phase equivalences can occur if \(h\) has a smaller fundamental period. The proof establishes weak functional convergence, not a strong invariance coupling or independently certified result. Comparisons with indexed/accessible literature are not exhaustive, and an equivalent characterization under a different correlated-Bernoulli/urn vocabulary remains a residual originality risk.

## References
1. X. Fan and Y. Qi, *A Generalized Elephant Random Walk with Time-Dependent Memory*, arXiv:2610.16065v1 (first public 2026-10-12), https://arxiv.org/abs/2610.16065.
2. G. Tokumitsu, *Stable functional CLTs for scaled elephant random walks*, arXiv:2603.13690v1 (2026), https://arxiv.org/html/2603.13690v1.
3. E. Baur and J. Bertoin, *Elephant random walks and their connection to Pólya-type urns*, arXiv:1608.01305 (2016), https://arxiv.org/abs/1608.01305.
4. B. James, K. James, and Y. Qi, *Limit theorems for correlated Bernoulli random variables*, Statistics & Probability Letters 78 (2008), 2339–2345, https://doi.org/10.1016/j.spl.2008.01.104.
