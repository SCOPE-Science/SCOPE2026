# Haar-dephased spin batteries have an exact harmonic ergotropy law and a sharp square-root limit

## Finding

**Theorem.** For each integer \(n\ge1\), put \(d=2^n\) and fix \(\omega>0\). Let \(\psi\) be a complex Haar-uniform unit vector in the \(n\)-qubit space. Completely dephase \(|\psi\rangle\langle\psi|\) in the **specified computational product basis** (one chosen eigenbasis of the battery Hamiltonian). Write the result as \(\rho_n\), with Hamiltonian
\[
H_n=\omega\sum_{j=1}^{n}|1\rangle\langle1|_j.
\]
Define its unrestricted global-unitary ergotropy
\[
W_n=\operatorname{Tr}(H_n\rho_n)-\min_{U\in\mathrm U(d)}\operatorname{Tr}(H_nU\rho_nU^\dagger).
\]
Let \(e_1\le\cdots\le e_d\) list all computational Hamming weights, with each \(k\in\{0,\ldots,n\}\) repeated \(\binom nk\) times. Let \(h_m=\sum_{j=1}^{m}j^{-1}\) for \(m\ge1\), and \(h_0=0\). Then, **for every finite \(n\)**,
\[
\boxed{\mathbb E W_n=\frac{\omega}{d}\sum_{i=1}^{d}e_i\bigl(1+h_{i-1}-h_d\bigr).}
\]
For \(\varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}\) and \(\Phi(z)=\int_{-\infty}^z\varphi(t)\,dt\), define
\[
\boxed{c_*=\frac12\int_{-\infty}^{\infty}\frac{\varphi(z)^2}{\Phi(z)}\,dz=0.451598642784\ldots.}
\]
Then
\[
\boxed{\lim_{n\to\infty}\frac{\mathbb EW_n}{\omega\sqrt n}=c_*},
\qquad
\boxed{\frac{W_n}{\omega\sqrt n}\xrightarrow{\mathrm P}c_*}.
\]
Indeed, for every \(n\ge1\) and every \(\varepsilon>0\),
\[
\Pr\left(\left|\frac{W_n-\mathbb EW_n}{\omega\sqrt n}\right|>\varepsilon\right)
\le3\exp\left(-\frac{2^n\varepsilon^2}{200\pi n}\right).
\]
Writing \(E_n=\operatorname{Tr}(H_n\rho_n)\), the extractable fraction obeys
\[
\boxed{\sqrt n\,W_n/E_n\xrightarrow{\mathrm P}2c_*\approx0.903197285569},
\]
with \(E_n>0\) almost surely. Thus the energy remains extensive while the globally extractable work after full product-basis dephasing is only of order \(\sqrt n\).

## Assumptions and scope

The ensemble is the **uniform complex Haar-pure-state ensemble** in the full \(2^n\)-dimensional Hilbert space, before dephasing. The channel removes every off-diagonal matrix element in the fixed computational product basis; it is *not* the weaker spectral pinching that preserves coherences inside the degenerate eigenspaces of \(H_n\). All unitary operations on the entire battery are allowed during work extraction. The Hamiltonian has \(n\) uncoupled identical qubits with gap \(\omega>0\), and zero ground energy. All stated limits take integer \(n\to\infty\), with fixed \(\omega\). The source motivating a chaotic-battery benchmark studies a different driven interacting system; its dynamics are **not** assumed or derived here.

## Proof

**1. Haar populations and rearrangement.** A complex Haar vector can be constructed by normalizing \(d\) independent standard complex Gaussians. Its computational populations \((p_1,\ldots,p_d)\) therefore have the uniform simplex distribution \(\operatorname{Dirichlet}(1,\ldots,1)\); each has mean \(1/d\). For populations sorted in nonincreasing order \(p_{[1]}\ge\cdots\ge p_{[d]}\), the exact passive-state rearrangement (including degenerate energy levels) gives
\[
\frac{W_n}{\omega}=\sum_{x\in\{0,1\}^n}|x|p_x-\sum_{i=1}^{d}e_ip_{[i]}.
\]
The first term has expectation \(n/2\), by symmetry.

**2. Ordered simplex mean.** For \(1\le j<d\) define \(v_j=j(p_{[j]}-p_{[j+1]})\), and put \(v_d=dp_{[d]}\). The map from the ordered simplex sector to the ordinary simplex is affine-linear with constant nonzero Jacobian. Since the Dirichlet density is constant, \((v_1,\ldots,v_d)\) is uniform on the ordinary simplex, with \(\mathbb Ev_j=1/d\). Because \(p_{[i]}=\sum_{j=i}^d v_j/j\),
\[
\mathbb E p_{[i]}=\frac1d\sum_{j=i}^{d}\frac1j=\frac{h_d-h_{i-1}}d.
\]
Substitution and \(\sum_i e_i=dn/2\) give the asserted exact formula. This argument uses the full \(d\)-dimensional distribution, not finite sampling.

**3. Sharp square-root limit.** For \(0<u\le1\) let
\[
Q_n(u)=\frac{2}{\sqrt n}\left(e_{\lceil du\rceil}-\frac n2\right),\qquad
w_n(u)=h_d-h_{\lceil du\rceil-1}.
\]
The first is the quantile function of \((2B_n-n)/\sqrt n\) for \(B_n\sim\operatorname{Binomial}(n,1/2)\). The central limit theorem and convergence of second moments to \(1\) imply \(Q_n\to\Phi^{-1}\) in \(L^2(0,1)\) (the one-dimensional Wasserstein-two quantile criterion). The harmonic estimate
\[
0\le w_n(u)\le1-\log u
\]
holds for every \(n\) and \(u\in(0,1]\): for an index \(i\), use \(\sum_{j=i}^d j^{-1}\le i^{-1}+\log(d/i)\) and \(u\le i/d\). For each fixed \(u>0\), \(w_n(u)\to-\log u\), hence dominated convergence gives \(L^2(0,1)\) convergence. The exact expectation formula consequently yields
\[
\lim_{n\to\infty}\frac{\mathbb EW_n}{\omega\sqrt n}
=-\frac12\int_0^1\Phi^{-1}(u)(-\log u)\,du.
\]
Set \(u=\Phi(z)\), and integrate by parts using \(\varphi'(z)=-z\varphi(z)\). The boundary terms vanish by Gaussian tail estimates. The result is \(\frac12\int\varphi(z)^2/\Phi(z)\,dz=c_*\). This integral is strictly positive and finite; its lower tail is integrable since \(\Phi(z)\sim\varphi(z)/|z|\) as \(z\to-\infty\).

**4. Concentration and extractable fraction.** For any density matrices \(\rho,\sigma\), the passive-energy minimum is \(\|H_n\|_\infty\)-Lipschitz in trace norm, as it is an infimum of linear expectations with that bound. Therefore ergotropy is \(2\|H_n\|_\infty\)-Lipschitz in trace norm. Complete dephasing contracts trace distance, and for unit vectors \(\psi,\xi\),
\[
\|\,|\psi\rangle\langle\psi|-|\xi\rangle\langle\xi|\,\|_1\le2\|\psi-\xi\|_2.
\]
Since \(\|H_n\|_\infty=n\omega\), the map \(\psi\mapsto W_n(\psi)\) on the real unit sphere of dimension \(2d-1\) has Euclidean Lipschitz constant at most \(4n\omega\). The sphere form of Lévy's lemma with a valid universal constant \(1/(25\pi)\) gives the displayed concentration bound \(3\exp[-2^n\varepsilon^2/(200\pi n)]\). Hence normalized work converges in probability to \(c_*\).

Likewise \(\mathbb E E_n=n\omega/2\) and the same concentration argument for the energy expectation gives \(E_n/(n\omega)\to1/2\) in probability. Combining the limits by Slutsky's theorem proves the extractable-fraction law. The pure pre-dephasing state has ergotropy exactly its energy, because a global unitary can map any pure state to the ground state; therefore complete basis dephasing changes a typical extensive work resource to a subextensive one.

## Verification

A standalone Python 3 checker at `verify.py` computes exact rational expectations by two independent formulas for \(1\le n\le8\), checks the combinatorial Hamming-energy multiplicities, evaluates the Gaussian integral by Simpson quadrature, and independently samples normalized exponential populations for \(n\in\{2,3,4,5\}\). Command: `python3 verify.py`. The completed run returned `VERIFY_OK exact=8 gaussian= 0.451598642784 samples=48000`. The checks corroborate the analytic argument but **are not a substitute for the all-size proof or convergence justification**. Example exact means in units of \(\omega\) are \(1/4\), \(11/24\), \(431/672\), and \(255747/320320\) for \(n=1,2,3,4\), respectively.

## Relationship to prior work

The 2026 chaotic Floquet-battery study motivates testing residual extractable work after a dephasing storage phase, but treats a driven interacting model rather than the complete fixed-product-basis dephasing of a uniformly Haar-random pure state analyzed here [1]. Its publicly readable abstract does not supply this exact benchmark; its full text was unavailable for a conclusive comparison.

The 2025 study of incoherent ergotropy [2] already supplies the general passive-energy rearrangement and discusses random diagonal populations; its full paper and supplement use a different Hilbert–Schmidt sampling distribution (including Dirichlet shape \(2\)), and do not state the Haar-pure Dirichlet-shape-\(1\) spin-battery harmonic law or sharp Gaussian-quantile constant. The 2024 concentration paper [3] proves generic Lipschitz/measure-concentration tools for Hilbert–Schmidt-distributed mixed states; we rely on that established technique and do **not** claim it as new. The 2020 random quantum batteries analysis [4] concerns work under random unitary driving with fixed spectra, not global-unitary optimization of a post-dephasing Haar-pure state. Classical ordered-Dirichlet and central-limit facts are also used rather than claimed as new. The proposed contribution is their precise, all-size synthesis into this physically motivated work-extraction benchmark.

## Limitations

The claim concerns one specified idealized ensemble and full product-basis dephasing, not generic finite-time noisy dynamics or dephasing that leaves degeneracy-sector coherences. The extractable work assumes unrestricted global unitaries; restrictions to local unitaries, finite-depth circuits, or work fluctuations under actual protocols can change the answer. Gaussian chaotic states need not be exactly Haar-distributed. The numerical checks cover only finite dimensions. An uninspected full text of the motivating 2026 paper and possible unindexed equivalent treatments leave a **residual originality risk**; the theorem is not represented as externally or independently audited.

## References

[1] Lakshmija N. K. and U. Divakaran, *Optimal performance in a chaotic Floquet quantum battery*, arXiv:2609.35655v1 (first public 2026-09-28), https://arxiv.org/abs/2609.35655 .

[2] C.-J. Wang and F.-Q. Dou, *Ergotropy in Quantum Batteries*, arXiv:2512.21855v1 (2025-12-26), https://arxiv.org/pdf/2512.21855 .

[3] K. V. Hovhannisyan, R. P. A. Simon and J. Anders, *Concentration of ergotropy in many-body systems*, arXiv:2412.19801v1 (2024-12-27), https://arxiv.org/pdf/2412.19801 .

[4] F. Caravelli, G. Coulter-De Wit, L. P. García-Pintos and A. Hamma, *Random Quantum Batteries*, arXiv:1908.08064 (2019 first public), https://arxiv.org/pdf/1908.08064 .
