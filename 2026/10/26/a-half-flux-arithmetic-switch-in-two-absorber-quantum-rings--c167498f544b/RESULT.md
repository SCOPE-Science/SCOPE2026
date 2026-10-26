# A half-flux arithmetic switch in two-absorber quantum rings

## Finding

**Theorem (flux-sensitive two-contact trapping).** Fix an integer \(N\ge3\), distinct sites \(0,s\) with \(1\le s<N\), and positive absorption strengths \(\gamma_0,\gamma_s>0\). Let \(\{|j\rangle:j\in\mathbb Z/N\mathbb Z\}\) be the one-excitation site basis and define the flux-threaded ring Hamiltonian
\[
H_\Phi=\sum_{j=0}^{N-1}\left(e^{-i\Phi/N}|j+1\rangle\langle j|+e^{i\Phi/N}|j\rangle\langle j+1|\right),
\quad K_\Phi=H_\Phi-\frac i2\bigl(\gamma_0|0\rangle\langle0|+\gamma_s|s\rangle\langle s|\bigr).
\]
Let \(S_x(\Phi)=\lim_{t\to\infty}\|e^{-itK_\Phi}|x\rangle\|^2\) denote the never-absorbed probability from site \(x\). Put \(g=\gcd(N,s)\) and \(L=N/g\). All fluxes are interpreted modulo \(2\pi\).

The dimension \(D_\Phi\) of the undamped eigenspace is
\[
D_\Phi=\begin{cases}
0,&\Phi\not\equiv0,\pi,\\
g-1,&\Phi\equiv0,\quad L\text{ even},\\
\lfloor(g-1)/2\rfloor,&\Phi\equiv0,\quad L\text{ odd},\\
0,&\Phi\equiv\pi,\quad L\text{ even},\\
\lfloor g/2\rfloor,&\Phi\equiv\pi,\quad L\text{ odd}.
\end{cases}
\]
In particular, \(N^{-1}\sum_x S_x(\Phi)=D_\Phi/N\). The eventual absorbed fraction is \(1-D_\Phi/N\) for uniformly distributed starting sites.

The complete site-resolved survival law is as follows. For generic flux, \(S_x=0\). At zero flux, if \(L\) is even, then
\[
S_x(0)=\begin{cases}0,&g\mid x,\\g/N,&g\nmid x.\end{cases}
\]
If \(L\) is odd, set \(h=g/\gcd(g,2)\); then
\[
S_x(0)=\begin{cases}0,&h\mid x,\\g/(2N),&h\nmid x.\end{cases}
\]
At half flux, \(S_x(\pi)=0\) when \(L\) is even. If \(L\) and \(g\) are both odd,
\[
S_x(\pi)=\begin{cases}0,&g\mid x,\\g/(2N),&g\nmid x.\end{cases}
\]
Finally, if \(L\) is odd and \(g\) is even,
\[
S_x(\pi)=\begin{cases}
0,&x\equiv0\pmod g,\\
g/N,&x\equiv g/2\pmod g,\\
g/(2N),&\text{otherwise}.
\end{cases}
\]
Every formula is independent of the magnitudes of the two positive loss strengths.

**Parity switching.** When \(N\) is even and \(L\) is even, changing \(\Phi=0\) to \(\Phi=\pi\) removes \(g-1\) dark modes; for even \(N\) with odd \(L\), the same change *creates exactly one* dark mode; for odd \(N\), it leaves the dark dimension and the site-resolved survival profile unchanged. Arbitrarily small generic flux perturbations away from either special flux eliminate all permanent darkness, although no uniform absorption-time bound is asserted.

For example, on a six-site ring with absorbers at sites \(0,2\), zero flux gives complete eventual absorption, whereas half flux gives survival \(1/3\) from every odd-numbered site and zero from even-numbered sites. With absorbers at \(0,3\), zero flux instead leaves survival \(1/2\) from sites not divisible by three, while half flux gives complete eventual absorption.

## Assumptions and scope

The graph is one homogeneous nearest-neighbour cycle, with one particle and a static uniform Peierls phase of total flux \(\Phi\). Absorption is modeled by the non-Hermitian no-jump generator \(K_\Phi\), with two *strictly* positive and otherwise arbitrary rates. The initial condition is a localized site state for the sitewise formulas, or a uniform classical mixture of these for the average. The limit \(t\to\infty\) is taken at fixed finite \(N\), flux, and rates. No claim is made about simultaneous weak-flux, large-size, or weak-loss limits.

## Proof

**1. Spectral reduction of loss.** Let \(V=(|0\rangle,|s\rangle)\) and \(G=\mathrm{diag}(\gamma_0,\gamma_s)\). The derivative of the norm is
\[
\frac{d}{dt}\|e^{-itK_\Phi}u\|^2=-\|G^{1/2}V^*e^{-itK_\Phi}u\|^2\le0.
\]
For an eigenvector of \(K_\Phi\) with real eigenvalue \(E\), this equality forces zero amplitude at both absorbers. Such a vector is therefore also an eigenvector of the Hermitian \(H_\Phi\). Conversely, every eigenvector of \(H_\Phi\) vanishing at both absorbers is a real-energy eigenvector of \(K_\Phi\). Those vectors also diagonalize \(K_\Phi^*\), so their span is orthogonally reducing. Contractivity excludes nontrivial Jordan blocks on the real axis: otherwise a generalized eigenvector would grow polynomially in time. On the orthogonal complement, all eigenvalues have strictly negative imaginary part, whence propagation decays exponentially for each fixed parameter choice. Consequently \(S_x(\Phi)=\langle x|P_{\rm dark}|x\rangle\), with \(P_{\rm dark}\) the orthogonal spectral projection onto simultaneous eigenvectors of \(H_\Phi\) annihilated by both contact evaluations.

**2. Flux-dependent degeneracies.** The plane waves
\[
f_k(j)=N^{-1/2}e^{2\pi ikj/N},\qquad E_k(\Phi)=2\cos\frac{2\pi k+\Phi}{N},\qquad k=0,\ldots,N-1,
\]
form a complete orthonormal eigenbasis. Distinct eigenvalues collide only when \(\Phi\equiv0\) or \(\Phi\equiv\pi\pmod{2\pi}\): from \(E_k=E_\ell\), \(k\ne\ell\), the cosine identity gives \(k+\ell+\Phi/\pi\equiv0\pmod N\). A simple eigenvector has nonzero amplitude at site zero, so none can be dark. At zero flux the degenerate pairs are \(\{k,N-k\}\), excluding possible self-paired indices. At half flux they are \(\{k,N-1-k\}\), again excluding self-paired indices.

**3. Which pairs are dark.** On a nontrivial degenerate pair \(\{k,\ell\}\), vanishing at site zero singles out the normalized difference \((f_k-f_\ell)/\sqrt2\). It also vanishes at site \(s\) if and only if
\[
e^{2\pi i(k-\ell)s/N}=1\quad\Longleftrightarrow\quad L\mid(k-\ell).
\]
At zero flux the condition is \(L\mid2k\), with \(1\le k<N/2\). For even \(L\), the solutions are \(k=mL/2\), \(m=1,\ldots,g-1\), giving \(g-1\) dark pairs. For odd \(L\), they are \(k=mL\), \(m=1,\ldots,\lfloor(g-1)/2\rfloor\), giving the stated count. At half flux the condition becomes \(L\mid(2k+1)\). No solution exists for even \(L\); for odd \(L\) the odd integers \(2k+1=mL\), with \(m<g\) odd, give \(\lfloor g/2\rfloor\) solutions. The possible self-paired mode is not dark because it has nonzero amplitude at site zero.

**4. Site-resolved survival.** Each dark pair contributes at starting site \(x\) exactly
\[
\left|\langle x|(f_k-f_\ell)/\sqrt2\rangle\right|^2
=\frac1N\left(1-\cos\frac{2\pi(k-\ell)x}{N}\right).
\]
At zero flux with even \(L\), sum over frequencies \(m=1,\ldots,g-1\) to obtain \(g/N\) for \(g\nmid x\) and zero otherwise, using a complete roots-of-unity sum. When \(L\) is odd, the frequencies reduce to representatives modulo \(h=g/\gcd(g,2)\); the half-pair cosine sum gives \(g/(2N)\) unless \(h\mid x\). At half flux with odd \(L\), the paired frequencies are precisely the odd residue representatives \(m=1,3,\ldots<g\). For odd \(g\), their cosine sum is \(-1/2\) when \(g\nmid x\), and the constant case otherwise. For even \(g\), their exponential sum is zero unless \(g/2\mid x\); in the exceptional congruence classes it equals \(+g/2\) or \(-g/2\) according to \(x\equiv0\) or \(g/2\pmod g\). These finite Fourier sums yield each displayed piecewise formula. Taking the trace of \(P_{\rm dark}\) yields \(\sum_x S_x=D_\Phi\). The even/odd switching claims are immediate from the counts and the parity of \(N=gL\). This proves all assertions.

## Verification

The accompanying standalone script `verify_cycle_two_sink.py` numerically diagonalizes the actual Hermitian magnetic-cycle matrix and computes the joint contact kernel within each distinct energy eigenspace. For every \(N=3,\ldots,12\), every separation \(1\le s<N\), and flux \(0\), \(\pi\), and an off-resonance flux \(0.461\), it verifies the full sitewise projection formula and dark dimensions, including both positive loss-rate pairs \((1.1,2.9)\) and \((0.43,3.7)\) for the non-Hermitian spectral test. All 195 parameter/phase cases passed. The script checks finite instances only; the unrestricted theorem is proved above. Run with `python verify_cycle_two_sink.py` with `numpy` installed.

## Relationship to prior work

Agliari, Mülken and Blumen (arXiv:0903.3288v1, Sections III–IV) studied quantum trapping on rings, including general multi-trap placement. Their Equation (21) explicitly gives the zero-flux Fourier trap sum; its specialization to two traps already supplies the basic zero-flux vanishing criterion used here. **That zero-flux criterion, the general spectral-projection method, and the idea that trap geometry governs quantum survival are prior work, not novelty claims.** The present result instead evaluates the interplay of *half-quantum magnetic flux* and *two absorbers*, including an all-size arithmetic direction reversal (half flux can either create or destroy trapping) and every starting-site survival value.

Lu and collaborators (arXiv:1405.6209, Sections 2–3) establish the phase/gauge and chiral-transport viewpoint; they do not evaluate two-loss-site asymptotic trapping on flux-threaded cycles. Razzoli, Paris and Bordone (arXiv:2011.13794; published 2021, Sections 3–4 and conclusion) develop spectral-subspace transport-efficiency methods for graphs with a *single* absorber, explicitly leaving multiple traps as future work. No known theorem in those inspected texts states or dominates the two-contact half-flux arithmetic switch. This is a bounded literature comparison rather than a proof of global novelty.

## Limitations

The special-flux discontinuities concern **infinite-time** survival; for fixed finite time the evolution varies continuously in flux. The result does not provide mixing times, absorption-time asymptotics, a multi-particle statement, noisy phase disorder, nonuniform hopping, or more than two absorbers. The zero-flux two-trap compatibility criterion follows from previously published Fourier formulas, while the half-flux arithmetic and local-survival evaluation is the separate contribution. Independent scientific and historical validation remains unperformed.

## References

1. E. Agliari, O. Mülken and A. Blumen, “Continuous-Time Quantum Walks and Trapping,” arXiv:0903.3288v1, publicly posted 19 March 2009. https://arxiv.org/html/0903.3288v1.
2. D. Lu et al., “Chiral Quantum Walks,” arXiv:1405.6209, first posted 23 May 2014. https://ar5iv.labs.arxiv.org/html/1405.6209.
3. L. Razzoli, M. G. A. Paris and P. Bordone, “Transport Efficiency of Continuous-Time Quantum Walks on Graphs,” arXiv:2011.13794v1, first posted 27 November 2020; *Entropy* 23 (2021), 85. https://pmc.ncbi.nlm.nih.gov/articles/PMC7826824/.
