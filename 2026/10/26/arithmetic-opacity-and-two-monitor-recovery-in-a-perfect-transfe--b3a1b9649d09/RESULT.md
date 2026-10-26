# Arithmetic opacity and two-monitor recovery in a perfect-transfer spin chain

## Finding
Let \(N\ge3\) be an integer and consider the one-excitation Hamiltonian \(H_N\) on sites \(0,1,\ldots,N\), with zero diagonal and symmetric adjacent hopping
\[
\langle j+1|H_N|j\rangle=\sqrt{(j+1)(N-j)},\qquad 0\le j<N.
\]
This is the analytic perfect-transfer chain. Put a local absorbing channel of positive rate \(\gamma\) at site \(3\), with no-click Hamiltonian \(G_0=H_N-i\gamma |3\rangle\langle3|/2\). Write \(D_N\) for its nondecaying subspace.

The dimension \(d_N=\dim D_N\) has the exact arithmetic classification
\[
d_N=\begin{cases}
3,&N\text{ even and }3N-2\text{ a perfect square},\\
1,&N\text{ even and }3N-2\text{ not a perfect square},\\
2,&N\text{ odd and }3N-2\text{ a perfect square},\\
0,&N\text{ odd and }3N-2\text{ not a perfect square}.
\end{cases}
\]
In the order given, the surviving endpoint probability is \(2^{-N}\sum_{k\in Z_N}\binom Nk\), where
\[
Z_N=\left\{k\in\{0,\ldots,N\}:(N-2k)((N-2k)^2-3N+2)=0\right\}.
\]
When \(N\to\infty\) through the three nonempty classes of sizes (generic even, exceptional even, exceptional odd), the endpoint survivor probability multiplied by \(\sqrt N\) tends, respectively, to
\[
\sqrt{2/\pi},\qquad (1+2e^{-3/2})\sqrt{2/\pi},\qquad 2e^{-3/2}\sqrt{2/\pi}.
\]
The square-discriminant cases are infinite: for instance \(3N-2=s^2\) with odd \(s\ge5\) not divisible by \(3\) yields odd exceptional sizes, and with even \(s\ge4\) not divisible by \(3\) yields even exceptional sizes. All sizes give a globally averaged stationary survival fraction \(d_N/(N+1)\) when initial basis positions are uniformly averaged.

A second absorbing channel of rate \(\eta>0\) at site \(2\), giving \(G_\eta=G_0-i\eta|2\rangle\langle2|/2\), removes all nondecaying states: every initial state is eventually absorbed for every \(N\ge3\) and all \(\gamma,\eta>0\). Moreover, each dark eigenmode of index \(k\in Z_N\), initially at real eigenvalue \(E_k=N-2k\), has an analytic continuation with loss exponent
\[
-2\operatorname{Im} E_k(\eta)=\eta\,p_{2,k}+O_{N,\gamma}(\eta^2),\qquad
p_{2,k}=\frac{\binom Nk}{2^N\binom N2}\left(\frac{(N-2k)^2-N}{2}\right)^2>0.
\]
Thus the formerly exactly trapped modes have lifetimes of order \(1/\eta\), with explicit mode-dependent coefficients. For the central dark mode (even \(N\)), \(p_{2,k}=\frac{N}{2(N-1)}2^{-N}\binom N{N/2}\). For each side dark mode, \(p_{2,k}=\frac{2(N-1)}N 2^{-N}\binom Nk\).

## Assumptions and scope
All couplings are real positive in the site basis, \(N\ge3\), and only one excitation is present. Time evolution is non-unitary no-click dynamics \(\psi_t=e^{-itG}\psi_0\). Survival means \(\|\psi_t\|_2^2\); eventual absorption probability is \(1-\lim_{t\to\infty}\|\psi_t\|_2^2\). No replacement evolution after a detector click is considered. The two local absorbing strengths are strictly positive when both are present. All asymptotics keep the single-site rate \(\gamma>0\) fixed; the square-size limits take \(N\to\infty\) within specified arithmetic subsequences.

## Proof
**Spectral structure.** The standard spin-\(N/2\) realization diagonalizes \(H_N\), giving simple eigenvalues \(E_k=N-2k\), \(0\le k\le N\). A normalized eigenbasis \(u_k\) satisfies
\[
\langle j|u_k\rangle=\left(\frac{\binom Nk}{2^N\binom Nj}\right)^{1/2} K_j(k),\quad
K_j(k)=\sum_{h=0}^j(-1)^h\binom kh\binom{N-k}{j-h},
\]
with binomial coefficients zero outside their range. In particular,
\[
K_2(k)=\frac{(N-2k)^2-N}{2},\qquad
K_3(k)=\frac{(N-2k)((N-2k)^2-3N+2)}6.
\]
These follow by expanding the generating identity \(\sum_{j=0}^NK_j(k)z^j=(1-z)^k(1+z)^{N-k}\).

**Characterization of eternal survival.** For \(G_0\),
\[
\frac{d}{dt}\|\psi_t\|^2=-\gamma|\langle3|\psi_t\rangle|^2\le0.
\]
An eigenvector with real eigenvalue must lie in the detector kernel; conversely any \(H_N\) eigenvector with zero site-\(3\) amplitude is unchanged by the loss and is nondecaying. The finite-dimensional contraction semigroup has no nontrivial Jordan blocks on the real axis (otherwise polynomial growth would contradict contractivity), and its remaining spectral components decay exponentially. Since the \(H_N\) spectrum is simple, the eternal subspace is exactly \(\operatorname{span}\{u_k:K_3(k)=0\}\). The square root \(s=\sqrt{3N-2}\), when integer, always has the parity of \(N\): for even \(N\) the square condition forces \(s\) even; for odd \(N\), \(s\) is odd. Consequently the two side roots \((N\pm s)/2\) are integral. For \(N\ge3\), \(0<s\le N\) since \((N-1)(N-2)\ge0\). The central root \(N/2\) exists precisely for even \(N\), and cannot coincide with the side roots. This proves the dimension classification.

**Endpoint survival and asymptotics.** Orthogonal projection onto the dark subspace gives \(\lim_{t\to\infty}\|e^{-itG_0}|0\rangle\|^2=\sum_{k\in Z_N}|\langle0|u_k\rangle|^2=2^{-N}\sum_{k\in Z_N}\binom Nk\). The global uniform average is \(\operatorname{Tr}P_{D_N}/(N+1)=d_N/(N+1)\). For integer \(k=N/2+x\sqrt N/2+O(1)\), Stirling's formula gives \(2^{-N}\binom Nk=\sqrt{2/(\pi N)}e^{-x^2/2}(1+o(1))\), uniformly for bounded \(x\). The center has \(x=0\); the side modes have \(x^2=(3N-2)/N\to3\), proving all three limits. Odd and even exceptional subsequences are infinite: choosing integers \(s\not\equiv0\pmod3\) of the desired parity ensures \((s^2+2)/3\) is an integer of the same parity as \(s\).

**Two-monitor recovery and weak-loss law.** If a real eigenvalue existed for \(G_\eta\), the norm derivative would force \(\langle2|u\rangle=\langle3|u\rangle=0\); the state would be an \(H_N\) eigenvector. But \(K_2(k)\) and \(K_3(k)\) have no common root: at their central root \(K_2=-N/2\ne0\), and at either side root \(K_2=N-1\ne0\). Thus every eigenvalue has strictly negative imaginary part. Since the matrix is finite, its evolution decays exponentially even with nontrivial Jordan blocks. At \(\eta=0\), each real dark eigenvalue is simple: it is simple in \(H_N\), the complementary dissipative block has no real eigenvalues, and the eigenspace decouples orthogonally. Analytic eigenvalue perturbation gives \(E_k'(0)=-i|\langle2|u_k\rangle|^2/2\) because \(u_k\) is simultaneously a right and left eigenvector of \(G_0\), yielding the stated first-order loss coefficient and its two evaluations.

## Verification
The standalone script `verify.py` tests the Krawtchouk arithmetic classification for sizes \(3\) through \(70\), compares independently diagonalized weighted-chain eigenvectors and endpoint survival for sizes up to \(22\), and checks small-\(\eta\) complex spectral slopes at sizes \(4,6,9,17,22,34\). The exact all-size assertions follow from the proof, not from these finite computations.

## Relationship to prior work
Christandl, Datta, Ekert and Landahl's original engineered spin chain supplies the Hamiltonian and perfect-transfer spectral context. Le, Donati, Severini and Caruso study the general relationship between quantum transport, dark eigenspaces and loss suppression. Both sources motivate and establish the general framework; neither is claimed here as a new method. The new evaluated assertion is the site-\(3\) arithmetic opacity classification, its three endpoint-survival constants, and adjacent site-\(2\) recovery with explicit loss-opening rates. The general dark-subspace principle and known Krawtchouk polynomial identities are acknowledged rather than claimed as new. They make this evaluated classification accessible, and a source containing the equivalent specialization would supersede it.

## Limitations
This is a finite, one-excitation, specifically weighted path model, not a generic spin network. The asymptotic limits are restricted to arithmetic subsequences and should not be interpreted as a limit over all sizes. The weak-secondary-loss expansion holds for each fixed \(N,\gamma\), without uniformity as \(N\to\infty\). The model does not address many-body excitation sectors, dephasing or arbitrary detector placements. The first-order decay law is not a statement that the entire survival curve is a single exponential.

## References
1. M. Christandl, N. Datta, A. Ekert, A. J. Landahl, *Perfect state transfer in quantum spin networks*, arXiv:quant-ph/0309131 (first public 17 September 2003), https://arxiv.org/abs/quant-ph/0309131.
2. T. P. Le, L. Donati, S. Severini, F. Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482 (first public 24 July 2017), https://arxiv.org/abs/1707.07482.
