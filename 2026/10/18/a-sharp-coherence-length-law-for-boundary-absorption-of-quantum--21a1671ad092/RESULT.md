# A sharp coherence-length law for boundary absorption of quantum walkers

## Finding
For the continuous-time, one-excitation quantum walk on the positive integer half-line with a single Lindblad sink at site one, consider a *normalized coherent packet supported on exactly a window of at most \(K\) adjacent sites*, translated to an initial distance \(n\). Let \(\mathcal A_{n,K}(\eta)\) be its eventual sink-absorption probability at dimensionless loss \(\eta=\kappa/\Omega>0\), and optimize over all such packets and all positive \(\eta\). Then, for each fixed integer \(K\ge1\),

\[
\Lambda_K\ \le\ \sup_{\eta>0,\,\|c\|_2=1}\mathcal A_{n,K}(\eta,c)\ \le\ \Lambda_K+\frac{K}{2\pi n(n-1)}\quad(n\ge2),
\]
where \(\Lambda_K\) is the largest eigenvalue of the explicit \(K\)-by-\(K\) Hermitian Toeplitz matrix
\[
(T_K)_{j\ell}=\frac1\pi\int_0^\pi\frac{\sin k}{1+\sin k}\,e^{i(\ell-j)k}\,dk,\qquad 0\le j,\ell<K.
\]
The far-field optimal loss strength is *uniquely* matched, \(\eta=1\), for every nonzero packet. The optimal far-field absorption satisfies the sharp preparation-length law
\[
\boxed{\displaystyle\Lambda_K=1-\frac{\pi^2}{4(K+1)^2}+O(K^{-3})}\quad(K\longrightarrow\infty).
\]
The coefficient and power are certified by two explicit finite-\(K\) bounds. With \(\lambda_K=4\sin^2(\pi/[2(K+1)])\),
\[
\frac{\lambda_K}{4}\le 1-\Lambda_K\le
\frac{\lambda_K}{4}+\frac18\left(\lambda_K^2+\frac4{K+1}\sin^2\frac\pi{K+1}\right).
\]
In particular, \(\Lambda_1=1-2/\pi\) and \(\Lambda_2=2/\pi\), whereas \(0<\Lambda_K<1\) for every finite \(K\). For \(K=2\), the optimal far-field packet is the equally weighted left-moving phase combination \((|n\rangle-i|n+1\rangle)/\sqrt2\), and reversing its phase gives absorption \(2-6/\pi\) at matched loss. An explicitly specified phase-chirped sine-envelope packet reaches the stated sharp large-\(K\) scaling. The contrast between finite-length non-unit absorption and asymptotically near-perfect absorption is an exact coherence-locality effect, not a finite-time or noisy-measurement claim.

## Assumptions and scope
Let \(\mathcal H=\ell^2(\{1,2,\ldots\})\), \(\Omega>0\), and \(\kappa>0\). The unabsorbed walker has Hamiltonian
\[
H_+=\Omega I-\frac\Omega2\sum_{s\ge1}(|s\rangle\langle s+1|+|s+1\rangle\langle s|),
\]
with bounded selfadjoint realization on \(\mathcal H\). Its coupling to an orthogonal absorbing vacuum uses the jump \(\sqrt\kappa\,|\emptyset\rangle\langle1|\); hence the no-jump generator is \(H_{\mathrm{eff}}=H_+-i\kappa|1\rangle\langle1|/2\). For integers \(n\ge2\), \(K\ge1\), initial states are
\[
|\psi_{n,c}\rangle=\sum_{j=0}^{K-1}c_j|n+j\rangle,\qquad\sum_j|c_j|^2=1.
\]
Here \(\eta=\kappa/\Omega\) and eventual absorption means the limit of the integrated exact Lindblad sink flux, not occupation of site one at a fixed time. Complex amplitudes and their relative phases are controllable; the individual coefficients need not all be nonzero. No unbounded-bandwidth, finite-time, dephasing, many-particle, or non-Markovian extension is asserted.

## Proof
**1. Exact absorption decomposition.** The boundary Green function for this model is the established resolvent identity
\[
\langle1|(z-H_{\mathrm{eff}})^{-1}|s\rangle=-\frac2\Omega\frac{q(z)^s}{1-i\eta q(z)},
\quad z/\Omega=1-\tfrac12(q+q^{-1}),
\]
with \(|q(z)|<1\) in the upper half-plane. Thus, for \(P_c(z)=\sum_{j=0}^{K-1}c_jz^j\), the Green function of the packet has numerator \(q^nP_c(q)\). Parseval applied to the causal boundary amplitude gives exactly
\[
\begin{split}
\mathcal A_{n,K}(\eta,c)&=\mathcal B_\eta(c)+\mathcal E_{n,\eta}(c),\\
\mathcal B_\eta(c)&=\frac{2\eta}{\pi}\int_0^\pi\frac{\sin k\,|P_c(e^{ik})|^2}{1+\eta^2+2\eta\sin k}\,dk,\\
\mathcal E_{n,\eta}(c)&=\frac\eta\pi\int_0^1\frac{q^{2n-2}(1-q^2)}{1+\eta^2q^2}\left(|P_c(q)|^2+|P_c(-q)|^2\right)dq.
\end{split}
\]
The in-band factor uses \(q=e^{ik}\), \(0<k<\pi\), while the two exterior energy branches have \(q\in(-1,0)\cup(0,1)\). The outside terms are positive. By Cauchy--Schwarz, \(|P_c(\pm q)|^2\le\sum_{j=0}^{K-1}q^{2j}\le K\). Also \(2\eta/(1+\eta^2q^2)\le1/q\). Consequently, uniformly over all \(\eta>0\) and normalized \(c\),
\[
0\le\mathcal E_{n,\eta}(c)\le\frac K\pi\int_0^1q^{2n-3}(1-q^2)dq=\frac{K}{2\pi n(n-1)}.
\]

**2. Exact reduction of the optimization.** At every \(0<k<\pi\),
\[
\frac{2\eta\sin k}{1+\eta^2+2\eta\sin k}
=\frac{2\sin k}{\eta+\eta^{-1}+2\sin k}
\le\frac{\sin k}{1+\sin k},
\]
with equality only when \(\eta=1\). Every nonzero polynomial \(P_c\) is nonzero on a set of positive measure, so the rate optimum in the far-field band term is unique. At \(\eta=1\), \(\mathcal B_1(c)=c^*T_Kc\). The spectral theorem yields \(\sup_{\eta,c}\mathcal B_\eta(c)=\Lambda_K\). Since the exterior term is nonnegative and bounded as above, the asserted finite-distance sandwich follows, proving the interchange of distance limit and optimization without assuming a uniform asymptotic expansion.

**3. The exact short-packet boundary.** For \(K=1\),
\(T_1=1-2/\pi\). For \(K=2\), the off-diagonal integral is purely imaginary, since the cosine contribution cancels under \(k\mapsto\pi-k\); explicitly
\[
T_2=\begin{pmatrix}1-2/\pi&i(4/\pi-1)\\-i(4/\pi-1)&1-2/\pi\end{pmatrix}.
\]
The integrals use \(\int_0^\pi(1+\sin k)^{-1}dk=2\). Its eigenvalues are \(2/\pi\) and \(2-6/\pi\), with corresponding normalized eigenvectors \((1,-i)/\sqrt2\) and \((1,i)/\sqrt2\). This yields the claimed sharp phase contrast.

**4. Finite support forces an exact Dirichlet gap.** Write \(P=P_c\), and on \([ -\pi,\pi]\) set
\[
\sigma(k)=\begin{cases}2\sin k/(1+\sin k),&0\le k\le\pi,\\0,&-\pi<k<0,\end{cases}
\qquad x(k)=|e^{ik}-i|^2=2(1-\sin k).
\]
Then \(\mathcal B_1(c)=(2\pi)^{-1}\int_{-\pi}^{\pi}\sigma(k)|P(e^{ik})|^2dk\), and elementary algebra gives *globally*
\[
\frac{x(k)}4\le1-\sigma(k)\le\frac{x(k)}4+\frac{x(k)^2}8.
\]
Indeed, for \(k\ge0\), \(x\in[0,2]\) and \(1-\sigma=x/(4-x)\), so the upper surplus is \(x^2/[4(4-x)]\le x^2/8\). For \(k<0\), \(x\in[2,4]\) and \(1-\sigma=1\), lying between the same two bounds.

By Parseval and a diagonal phase change \(c_j=(-i)^ju_j\), the quadratic form for multiplication by \(x\) is \(\sum_{j=0}^K|u_j-u_{j-1}|^2\), with \(u_{-1}=u_K=0\). The smallest eigenvalue of this Dirichlet path Laplacian is \(\lambda_K=4\sin^2(\pi/[2(K+1)])\). Therefore every normalized \(c\) obeys \(1-\mathcal B_1(c)\ge\lambda_K/4\), giving the *lower* bound on the optimal deficit.

For the reverse bound choose the normalized Dirichlet ground profile
\[
c_j=(-i)^j\sqrt{\frac2{K+1}}\sin\left(\frac{\pi(j+1)}{K+1}\right),\quad 0\le j<K.
\]
The \(x\)-energy equals \(\lambda_K\); the \(x^2\)-energy is exactly \(\lambda_K^2+4\sin^2(\pi/(K+1))/(K+1)\), because the interior second differences equal the Dirichlet eigenvalue times the ground profile and two endpoint corrections contribute its first- and last-site squares. Substitution in the upper pointwise inequality proves the *upper* bound on the optimal deficit. Expanding both elementary bounds yields the common leading term \(\pi^2/[4(K+1)^2]\), with an \(O(K^{-3})\) remainder. In particular \(0<\Lambda_K<1\) at every finite \(K\), but \(\Lambda_K\uparrow1\) along the nondecreasing sequence of admissible packet classes. This completes the proof.

## Verification
The accompanying executable checker independently builds the Toeplitz matrices by high-order Gauss--Legendre quadrature; verifies the closed \(K=1,2\) values; tests both rigorous finite-\(K\) inequalities for \(K=1,2,3,4,5,8,12,20,32,64\); verifies that \(\eta=1\) pointwise maximizes the band response for randomly chosen normalized complex packets; and compares the exact integral formula at finite distance against direct sparse propagation of the non-Hermitian Hamiltonian for three independent initial states. The proof above, not these finite checks, establishes the infinite and arbitrary-parameter claims. Code dependencies are specified separately.

## Relationship to prior work
Francisco Riberi, *Boundary-localized non-Hermitian modes in an absorbing quantum walk*, arXiv:2605.08056, first public version May 8, 2026, derives the Lindblad model, its full boundary Green function, single-site absorption probability, and weak--strong loss duality. The Green function and Parseval reduction used here are prior work. That source evaluates localized initial states, not the optimal probability under an arbitrary bounded coherent preparation window or its sharp length law. Earlier finite-path two-sink analyses also describe different geometry and objectives.

Amorim, Cerutti, de Sá Neto and de Oliveira, *Absorption-based qubit estimation in discrete-time quantum walks*, arXiv:2512.02186, treat coin-state inference for discrete-time, coined absorbing walks, rather than the continuous-time, coinless half-line sink and finite preparation length studied here. Bach and collaborators' classical discrete-time Hadamard-walk \(2/\pi\) absorption constant is a different physical model; the numerical coincidence with the \(K=2\) value here is not claimed as a general novelty. Classical extremal Hermitian Toeplitz theory (Parter and later treatments) can be relevant to the order-two eigenvalue deficit; the proof here derives the exact coefficient for the present nonsmooth sink symbol with explicit finite-length and finite-distance bounds. The asserted contribution is the *physical coherence-length optimum and its exact quantitative locality penalties*, not a new general Toeplitz theorem.

## Limitations
The results optimize eventual absorption after taking the initial packet far from the boundary, with a uniform finite-distance error. They do not optimize finite-time absorption, prove noisy experimental feasibility, cover interacting walkers or multiple sinks, or establish uniform error in \(K\) without the explicit stated \(K/[n(n-1)]\) term. The exact Toeplitz formulas and the asymptotic extremal constant may be related to general spectral results; independent novelty evaluation has not been performed.

## References
1. F. Riberi, *Boundary-localized non-Hermitian modes in an absorbing quantum walk*, arXiv:2605.08056, https://arxiv.org/abs/2605.08056 (first public version 2026-05-08; consulted v4 PDF, Sections 2--4 and Appendix D).
2. E. P. M. Amorim, L. R. Cerutti, O. P. de Sá Neto and M. C. de Oliveira, *Absorption-based qubit estimation in discrete-time quantum walks*, arXiv:2512.02186, https://arxiv.org/abs/2512.02186 (consulted v2 PDF, Sections I--III).
3. A. Böttcher and S. M. Grudsky, *Spectral Properties of Banded Toeplitz Matrices*, SIAM (2005), Chapter 10 on extreme eigenvalues, https://doi.org/10.1137/1.9780898717853.ch10 (general background; not a direct source for the physical theorem).
4. A. Ambainis, E. Bach, A. Nayak, A. Vishwanath and J. Watrous, *One-dimensional quantum walks*, STOC-era work (2001), https://authors.library.caltech.edu/records/a5b20-agg57 (different discrete-time Hadamard absorption model).
