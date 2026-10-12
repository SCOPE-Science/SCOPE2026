# Persistent quantum memory keeps constant simplex-decoding success across the full nontrivial BSC range
## Finding
For the binary simplex-code sensing protocol in arXiv:2610.03659v1, let \(k\) be even, \(n=2^k-1\), use one persistent-memory register pair \(B=1\), take \(S=k\) sensor qubits and \(k\) memory qubits, and set
\[
Q=2k,\qquad \theta=\frac{2\pi}{k2^{k/2}}.
\]
For every fixed binary-symmetric-channel flip probability \(p\in[0,1/2)\), the published QQ decoder has
\[
P_{\mathrm{QQ}}(k,p)=q(p)+O_p(2^{-k}),\qquad q(p)=e^{-\pi^2p(1-p)}\cos^2(\pi p)>0.
\]
Every QC receiver with the same \(Q\) and \(\theta\), even allowing arbitrary entanglement and joint measurements within each time slot but retaining only classical memory between slots, satisfies
\[
P_{\mathrm{QC}}(k,p)\le \frac{1+\frac{2\pi^2}{\ln 2}(1-2p)^2+o(1)}{k}\longrightarrow0.
\]
Therefore a single persistent quantum-memory pair yields a constant-versus-vanishing exact-message-success separation for every fixed \(p<1/2\), while the total interaction strength is weak:
\[
Q\theta=4\pi 2^{-k/2}\longrightarrow0.
\]
At \(p=1/2\), the QQ success is exactly \(2^{-k}\); the constant-success separation therefore closes at the fully random endpoint. If \(\varepsilon=1/2-p\downarrow0\), then
\[
q(p)=\pi^2e^{-\pi^2/4}\varepsilon^2+O(\varepsilon^4).
\]

## Assumptions and scope
The message is uniform, the transmitted code is the binary simplex \([2^k-1,k,2^{k-1}]\) code with even \(k\), channel bit flips are independent with fixed probability \(p\in[0,1/2]\), and the receiver model is exactly the CC/QC/QQ model of arXiv:2610.03659v1. The QQ statement uses the source's \(B=1\) decoder and its required interaction condition \(S\theta/2=\pi 2^{-k/2}\), specialized to \(S=k\). The comparison concerns exact-message success, not block error tending to zero.

## Proof
The source's Proposition 10 gives, with
\[
\alpha=\frac{\pi}{2^{k/2}},\qquad w=1-p+pe^{2i\alpha},
\]
that
\[
P_{\mathrm{QQ}}=2^{-k}+(1-2^{-k})|w|^{2^{k-1}}\left(\frac12+\frac12\cos\!\left(2^{k/2}\arg w\right)\right).
\]
First,
\[
|w|^2=1-4p(1-p)\sin^2\alpha.
\]
Writing \(m=2^{k/2}\) gives \(\alpha=\pi/m\), hence
\[
\frac{m^2}2\log|w|
=\frac{m^2}4\log\!\left(1-4p(1-p)\sin^2(\pi/m)\right)
=-\pi^2p(1-p)+O_p(m^{-2}).
\]
Therefore
\[
|w|^{2^{k-1}}=e^{-\pi^2p(1-p)}\left(1+O_p(2^{-k})\right).
\]
Also
\[
\arg w=\operatorname{Im}\log\!\left(1+p(e^{2i\alpha}-1)\right)=2p\alpha+O_p(\alpha^3),
\]
so
\[
2^{k/2}\arg w=2\pi p+O_p(2^{-k}).
\]
Substitution into Proposition 10 proves
\[
P_{\mathrm{QQ}}(k,p)=e^{-\pi^2p(1-p)}\cos^2(\pi p)+O_p(2^{-k}).
\]
For \(p<1/2\), the cosine factor is strictly positive. At \(p=1/2\), \(w=e^{i\alpha}\cos\alpha\) and \(2^{k/2}\arg w=\pi\), so the parenthetical factor in Proposition 10 vanishes exactly and \(P_{\mathrm{QQ}}=2^{-k}\).

For the QC comparison, \(Q=2k\) and \(\theta=2\pi/(k2^{k/2})\) give
\[
\Phi=Q\theta=4\pi 2^{-k/2}.
\]
The source defines
\[
C_{\mathrm{QC}}(\Phi,p)=1-h_2\!\left(\frac{1-(1-2p)\sin(\Phi/2)}2\right)
\]
and records the small-\(\Phi\) expansion
\[
C_{\mathrm{QC}}(\Phi,p)=\frac{(1-2p)^2\Phi^2}{8\ln2}+O_p(\Phi^4).
\]
Since \(n=2^k-1\),
\[
nC_{\mathrm{QC}}(\Phi,p)=\frac{2\pi^2}{\ln2}(1-2p)^2+o(1).
\]
The second branch of Proposition 3 is therefore
\[
P_{\mathrm{QC}}(k,p)\le\frac{1+nC_{\mathrm{QC}}(\Phi,p)}k
=\frac{1+\frac{2\pi^2}{\ln2}(1-2p)^2+o(1)}k\to0.
\]
Finally, for \(p=1/2-\varepsilon\),
\[
p(1-p)=\frac14-\varepsilon^2,\qquad \cos(\pi p)=\sin(\pi\varepsilon),
\]
which yields
\[
q(p)=\pi^2e^{-\pi^2/4}\varepsilon^2+O(\varepsilon^4).
\]

## Verification
The algebraic steps above use the exact Proposition 10 formula and the source's analytic QC information bound. A standalone verifier evaluates the exact finite-\(k\) expression, checks the identity for \(|w|^2\), checks the \(p=1/2\) endpoint, and numerically confirms convergence to \(q(p)\) and the QC scaling for representative fixed \(p\). These finite checks corroborate but do not replace the analytic asymptotic proof.

## Relationship to prior work
Blue, Chin, Oros, and Chuang prove reliable QQ decoding, meaning failure probability tending to zero, for fixed \(p<1/16\) using a growing number \(B=\omega(1)\) of memory-sensor register pairs. They separately derive Proposition 10, an exact \(B=1\) success formula, and use it for finite-size plots at small error rates. The result above extracts the asymptotic content of that exact formula and combines it with their QC converse to identify a different regime: nonvanishing exact-message success with a single register pair for every fixed \(p<1/2\). The conclusion is weaker than reliable decoding but covers the entire nontrivial BSC interval.

Blume-Kohout, Croke, and Zwolak's quantum-data-gathering framework shows that sequential coherent memory can implement collective discrimination when the relevant state family occupies a suitably low-rank subspace. It does not analyze the simplex weak-phase sensing model, binary-symmetric transmission noise, or the explicit limiting success curve above.

## Limitations
The result does not prove \(P_{\mathrm{QQ}}\to1\) for \(p\ge1/16\), does not optimize the QQ decoder, and does not give a converse against more general receivers with persistent quantum memory. The constant \(q(p)\) becomes very small as \(p\uparrow1/2\), vanishing quadratically. The originality comparison cannot exclude differently phrased or not-yet-indexed contemporaneous work.

## References
1. J. Blue, Z. E. Chin, V. S. Oros, and I. L. Chuang, “Quantum Codeword Sensing,” arXiv:2610.03659v1 (first public 2026-10-02). In particular Proposition 3, Theorems 7–8, and Proposition 10.
2. R. Blume-Kohout, S. Croke, and M. Zwolak, “Quantum data gathering,” Scientific Reports 3, 1800 (2013), DOI:10.1038/srep01800.
3. MSC2020, 81P45: Quantum information, communication, networks (quantum-theoretic aspects).
