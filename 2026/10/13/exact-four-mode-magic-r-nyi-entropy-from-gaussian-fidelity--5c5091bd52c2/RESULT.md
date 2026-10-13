# Exact four-mode magic Rényi entropy from Gaussian fidelity
## Finding
For every normalized positive-parity pure state \(\psi\) of four complex fermionic modes, define its fermionic Gaussian fidelity by
\[
F_{\mathrm G}(\psi)=\max_{\phi\ \mathrm{Gaussian}}\lvert\langle\phi\mid\psi\rangle\rvert^2,
\]
and let \(\nu_2(\psi)\) be the purity of the balanced two-copy fermionic convolution used to define the order-two magic Rényi entropy \(M_2(\psi)=-\ln\nu_2(\psi)\). Then
\[
\nu_2(\psi)=1-3F_{\mathrm G}(\psi)(1-F_{\mathrm G}(\psi))+\frac32F_{\mathrm G}(\psi)^2(1-F_{\mathrm G}(\psi))^2.
\]
Hence
\[
M_2(\psi)\le \ln\frac{32}{11},
\]
with equality if and only if \(F_{\mathrm G}(\psi)=1/2\). The equality states are precisely the Gaussian-unitary orbit of an equal vacuum/full-occupancy superposition, for example \((\lvert0000\rangle+\lvert1111\rangle)/\sqrt2\), up to overall phase.

For \(N=8\) Majorana modes, the universal upper bound of Hoshino--Matsuda--Ashida is \(6\ln(4/3)\). Therefore its exact finite-size slack is
\[
6\ln\frac43-\ln\frac{32}{11}=\ln\frac{1408}{729}>0.
\]
Thus the universal bound is not tight at the first nontrivial pure-state fermionic system size.

## Assumptions and scope
The state is a normalized pure state in the positive-parity sector of four complex fermionic modes. Gaussian unitaries are parity-preserving fermionic Gaussian unitaries. The convolution and its purity use the balanced two-copy convention of Hoshino--Matsuda--Ashida. The statement concerns the order-two magic Rényi entropy only; it does not classify mixed states, higher Rényi orders, or systems with more than four complex modes.

## Proof
Dias and Koenig prove that every normalized positive-parity pure state of four modes has a unique canonical decomposition
\[
\psi=e^{i\varphi}\bigl(\sqrt f\,\psi_{\mathrm G}+\sqrt{1-f}\,\theta\psi_{\mathrm G}\bigr),\qquad \frac12\le f\le1,
\]
where \(\psi_{\mathrm G}\) and \(\theta\psi_{\mathrm G}\) are orthogonal Gaussian states, and their Theorem 5.6 identifies \(f=F_{\mathrm G}(\psi)\). Their particle-hole involution \(\theta\) commutes with parity-preserving Gaussian unitaries. A Gaussian unitary can therefore send \(\psi_{\mathrm G}\) to the vacuum and \(\theta\psi_{\mathrm G}\) to the fully occupied state. A quadratic number-phase rotation removes the remaining relative phase. Since \(M_2\) and \(\nu_2\) are Gaussian-unitary invariant, it suffices to evaluate
\[
\psi_f=\sqrt f\,\lvert0000\rangle+\sqrt{1-f}\,\lvert1111\rangle.
\]

Hoshino--Matsuda--Ashida give the exact convolution purity for the \(n\)-mode vacuum/full-occupancy family. Writing \(p=f\), \(q=1-f\), and \(r=4pq\,2^{-n}\), their Eq. (S90) is
\[
\nu_2=(p^2+r)^2+(q^2+r)^2+(2^{n-1}-2)r^2+2r.
\]
At \(n=4\), put \(t=pq\), so \(r=t/4\). Since \(p^2+q^2=1-2t\) and \(p^4+q^4=1-4t+2t^2\), direct simplification gives
\[
\nu_2=1-3t+\frac32t^2,
\qquad t=f(1-f).
\]
Using \(f=F_{\mathrm G}(\psi)\) proves the displayed fidelity formula.

For \(f\in[1/2,1]\), one has \(0\le t\le1/4\). The derivative of \(1-3t+3t^2/2\) is \(-3+3t<0\) throughout this interval, so the purity is minimized exactly at \(t=1/4\), equivalently \(f=1/2\). Its minimum is
\[
1-\frac34+\frac3{32}=\frac{11}{32}.
\]
Taking \(-\ln\) gives the entropy maximum and its equality condition. Finally, Hoshino--Matsuda--Ashida's universal bound \(N\ln(4/3)-\ln(16/9)\) equals \(6\ln(4/3)\) at \(N=8\), and subtracting \(\ln(32/11)\) gives \(\ln(1408/729)>0\).

## Verification
The proof is analytic and does not depend on finite enumeration. As a corroborating calculation, `artifacts/verify.py` constructs two four-mode copies by Jordan--Wigner Majoranas, applies the balanced convolution beam splitter directly on the eight physical modes, traces out the second copy, and checks the resulting purity against \(1-3p(1-p)+3p^2(1-p)^2/2\) at several parameter values including the extremizer. Running

`python3 artifacts/verify.py`

prints `VERIFY_OK`. The numerical replay checks the normalization and convolution convention; it is not used as an infinite proof.

## Relationship to prior work
Hoshino, Matsuda, and Ashida prove the universal bound and explicitly state that finite-\(N\) tightness is open. Their supplement evaluates the vacuum/full-occupancy family and gives the cat-state value, but does not identify the global four-mode optimum or express the convolution purity as an exact function of Gaussian fidelity.

Dias and Koenig give the four-mode canonical decomposition and prove that its parameter equals fermionic Gaussian fidelity, but their work predates the magic Rényi entropy and does not compute this convolution purity. Lyu and Bu introduce fermionic convolution and non-Gaussian Rényi entropies and numerically study a four-qubit family, but do not state the global four-mode maximum or the Gaussian-fidelity formula. Oszmaniec, Gutt, and Kuś identify four modes as the first nontrivial even-parity pure-state case and develop the corresponding Gaussian geometry, again without the later convolution entropy.

The result arises by combining the exact four-mode normal form with the recent convolution formula and then optimizing the resulting single invariant. It answers the first finite-size instance of the tightness question rather than merely evaluating another special state.

## Limitations
No claim is made that \(\ln(32/11)\) is the maximum for more than four complex fermionic modes, for mixed states, or for Rényi orders other than two. The equality characterization is within the positive-parity pure sector. A very recent or differently indexed source could conceivably contain the same combination of the four-mode normal form with the 2026 convolution formula; targeted searches and inspected primary sources did not locate such a statement.

## References
1. M. Hoshino, R. Matsuda, and Y. Ashida, “Universal Bound and Phase Transition in Many-Body Fermionic Non-Gaussianity,” arXiv:2610.02075v1 (2026), Theorem 1 and Supplement Eqs. (S88)--(S91).
2. B. Dias and R. Koenig, “Classical simulation of non-Gaussian fermionic circuits,” arXiv:2307.12912 (2023), Theorems 5.4 and 5.6.
3. X. Lyu and K. Bu, “Fermionic Gaussian Testing and Non-Gaussian Measures via Convolution,” arXiv:2409.08180v2 (2024).
4. M. Oszmaniec, J. Gutt, and M. Kuś, “Classical simulation of fermionic linear optics augmented with noisy ancillas,” arXiv:1406.1577v1 (2014).
