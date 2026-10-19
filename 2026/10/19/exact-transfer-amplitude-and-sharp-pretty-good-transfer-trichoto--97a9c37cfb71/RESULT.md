# Exact transfer amplitude and sharp pretty-good-transfer trichotomy on butterfly quantum-walk networks

## Finding

For every integer \(m\geq 0\), consider the butterfly graph \(B_m=P_2\square K_{1,m}\): two central body vertices joined by an edge, with \(m\) further three-edge paths between the same body vertices, each through its own pair of wing vertices. Perform a discrete-time, flip-flop coined quantum walk, using a Grover coin at every wing vertex and the negative Grover coin at both body vertices. Initialize in the equal-amplitude outward-arc state at one body vertex and measure overlap with the analogous outward-arc state at the other body vertex.

Define \(\theta_m=\arccos\!\left(\frac{m-1}{2(m+1)}\right)\), and let \(a_m(t)\) be this normalized transfer amplitude after \(t\geq0\) walk steps. Then, for every integer \(n\geq0\),
\[
 a_m(2n)=0,\qquad
 a_m(2n+1)=-\frac{m+1}{3m+1}+\frac{2m}{3m+1}\cos\!\big((2n+1)\theta_m\big).
\]
The fidelity is \(F_m(t)=|a_m(t)|^2\). Consequently:

1. For \(m=0\), perfect state transfer occurs at every positive odd time.
2. For \(m=1\), the fidelity is exactly \(1/4\) at every odd time and zero at every even time; there is no pretty-good transfer.
3. For every integer \(m\geq2\), the transfer is *pretty good but never perfect*: \(\sup_{t\geq0}F_m(t)=1\), while \(F_m(t)<1\) at every finite time.

For each integer \(m\geq2\), the long-time mean fidelity exists and is
\[
 \lim_{T\to\infty}\frac1T\sum_{t=1}^{T}F_m(t)
 =\frac{3m^2+2m+1}{2(3m+1)^2}.
\]
For completeness, the Cesàro means at \(m=0\) and \(m=1\) are \(1/2\) and \(1/8\), respectively.

For \(m=3\) and \(t=31\), the exact fidelity is
\[
 F_3(31)=\frac{18441912835338519241}{18446744073709551616}
 =0.9997380980431165\ldots<1.
\]
This distinguishes the visually near-unity numerical body-to-body transfer reported at that time from mathematically exact perfect transfer.

## Assumptions and scope

The vertices are \((j,b)\), where \(j\in\{0,1,\ldots,m\}\) and \(b\in\{0,1\}\); edges join \((j,0)\) to \((j,1)\) for all \(j\), and \((0,b)\) to \((j,b)\) for \(j\geq1\), \(b\in\{0,1\}\). Thus \(B_m=P_2\square K_{1,m}\). Let \(\mathcal H\) be the Hilbert space with orthonormal basis all directed edges \(|u\to v\rangle\). At a vertex of degree \(d\), write \(|s_v\rangle=d^{-1/2}\sum_{w\sim v}|v\to w\rangle\) and \(G_v=2|s_v\rangle\langle s_v|-I\) on that vertex's outgoing arcs. The coin \(C\) is \(-G_v\) at \(s=(0,0)\) and \(r=(0,1)\), and \(G_v\) elsewhere. The shift \(S|u\to v\rangle=|v\to u\rangle\) gives \(U=SC\).

The source and target states are \(\psi_s=|s_s\rangle\) and \(\phi_r=|s_r\rangle\), so \(a_m(t)=\langle\phi_r,U^t\psi_s\rangle\). These are normalized arc superpositions, not vertex-only states or sums of probabilities on the target's outgoing arcs. All dynamics are noiseless and unitary; no claim concerns the noisy quantum channels considered elsewhere in the motivating study.

The alternative *incoming*-arc target \(\widetilde\phi_r=S\phi_r\) obeys the exact convention-translation identity
\[
 \langle\widetilde\phi_r,U^{t+1}\psi_s\rangle
 =-\langle\phi_r,U^t\psi_s\rangle
 \quad (t\geq0),
\]
so this convention simply shifts successful transfer times by one step. No continuum-time limit is assumed.

## Proof

**Parity.** The graph is bipartite, with the body vertices in opposite bipartition classes. Every application of \(U=SC\) reverses the class of the outgoing arc tail. Source and target outgoing arcs therefore have orthogonal support at all even times, proving \(a_m(2n)=0\).

**Symmetry reduction.** For \(m\geq1\), the permutation-invariant subspace of the \(m\) indistinguishable wings has the following orthonormal ordered basis: \(a\) is the body-arc \(s\to r\); \(b\) is \(r\to s\); \(c\) is the normalized sum of arcs \(s\to(j,0)\); \(d\) is the normalized sum \((j,0)\to s\); \(e\) is the normalized sum \(r\to(j,1)\); \(f\) is the normalized sum \((j,1)\to r\); \(g\) is the normalized sum \((j,0)\to(j,1)\); and \(h\) is the normalized sum \((j,1)\to(j,0)\), where each wing sum runs over \(1\leq j\leq m\) with factor \(m^{-1/2}\).

Write \(\alpha=(m-1)/(m+1)\) and \(\beta=-2\sqrt m/(m+1)\). Direct application of the signed body coins, ordinary degree-two wing Grover coins, and arc reversal shows that the invariant matrix of \(U\), with columns denoting input vectors, is
\[
 M_m=\begin{pmatrix}
 0&\alpha&0&0&\beta&0&0&0\\
 \alpha&0&\beta&0&0&0&0&0\\
 0&0&0&0&0&0&1&0\\
 \beta&0&-\alpha&0&0&0&0&0\\
 0&0&0&0&0&0&0&1\\
 0&\beta&0&0&-\alpha&0&0&0\\
 0&0&0&0&0&1&0&0\\
 0&0&0&1&0&0&0&0
 \end{pmatrix}.
\]
In the same coordinates the normalized source and target are
\[
 p_m=\frac{(1,0,\sqrt m,0,0,0,0,0)^\mathsf T}{\sqrt{m+1}},
 \qquad q_m=\frac{(0,1,0,0,\sqrt m,0,0,0)^\mathsf T}{\sqrt{m+1}}.
\]
Consequently \(a_m(t)=q_m^\mathsf{T}M_m^t p_m\) exactly. Factoring the characteristic polynomial by elementary row operations gives
\[
 \det(zI-M_m)=(z^2-1)^2
 \left(z^2-\frac{m-1}{m+1}z+1\right)
 \left(z^2+\frac{m-1}{m+1}z+1\right).
\]
The roots have unit modulus, as also follows from unitarity. Since the nontrivial roots are \(e^{\pm i\theta_m}\) and \(-e^{\pm i\theta_m}\), the distinct possible eigenvalues of \(M_m^2\) are \(1,e^{2i\theta_m},e^{-2i\theta_m}\). The unitary matrix is diagonalizable, so the odd-time amplitudes \(b_n=q_m^\mathsf{T}M_m^{2n+1}p_m\) satisfy a third-order recurrence with characteristic roots \(1,e^{\pm2i\theta_m}\), counting multiplicity only once.

For clarity, direct multiplication of the displayed matrix gives the first three odd amplitudes,
\[
 b_0=-\frac1{m+1},\qquad
 b_1=-\frac{m^3+3m^2-m+1}{(m+1)^3},\qquad
 b_2=\frac{3m^4+4m^3-18m^2-4m-1}{(m+1)^5}.
\]
The sequence \(-\frac{m+1}{3m+1}+\frac{2m}{3m+1}\cos((2n+1)\theta_m)\) satisfies the same recurrence and agrees at \(n=0,1,2\) by the double-angle and triple-angle identities. It must therefore equal \(b_n\) for every \(n\geq0\). When \(m=0\), the graph is simply one edge, both coins are \(-I\), and \(U=-S\), giving \(a_0(2n+1)=-1\) directly; the same closed formula reduces to that value.

**Exact versus pretty-good transfer.** For \(m=1\), \(\theta_1=\pi/2\); every odd cosine vanishes and \(F_1(2n+1)=1/4\). For \(m\geq2\), \(2\cos\theta_m=(m-1)/(m+1)\) is a rational noninteger strictly between zero and one. If \(\theta_m/\pi\) were rational, \(e^{i\theta_m}\) would be a root of unity; the sum \(2\cos\theta_m=e^{i\theta_m}+e^{-i\theta_m}\) would thus be a rational algebraic integer, hence an integer, a contradiction. Therefore \(\theta_m/\pi\) is irrational. The odd multiples \((2n+1)\theta_m\), \(n\geq0\), are dense modulo \(2\pi\), so their cosines approach \(-1\) along a subsequence.

The amplitude is an affine increasing function of this cosine for \(m>0\). Its extreme possible values are \(-1\) and \((m-1)/(3m+1)\), the latter strictly less than one for \(m\geq2\). Thus its modulus can reach one only when the cosine is \(-1\), which would contradict irrationality of \(\theta_m/\pi\). Nevertheless the cosine approaches \(-1\) arbitrarily closely, proving \(\sup_t F_m(t)=1\) without finite-time attainment. This is the standard vector-norm notion of pretty-good state transfer, since the source and target are normalized and \[\min_{|\omega|=1}\|U^t\psi_s-\omega\phi_r\|^2=2-2|a_m(t)|.\] Thus fidelity arbitrarily near one is equivalent to arbitrarily small transfer error up to a global phase.

**Time averages.** The irrational rotation in the preceding paragraph is equidistributed, so \(\cos((2n+1)\theta_m)\) has time averages zero and \(\cos^2((2n+1)\theta_m)\) has time average \(1/2\) for \(m\geq2\). Squaring the odd-time amplitude and including the zero even-time terms yields
\[
 \frac12\left(\frac{(m+1)^2}{(3m+1)^2}+\frac{2m^2}{(3m+1)^2}\right)
 =\frac{3m^2+2m+1}{2(3m+1)^2}.
\]
For \(m=0,1\), the elementary periodic amplitudes give \(1/2,1/8\). The incoming-target convention identity follows directly from \(\langle S\phi_r,SCx\rangle=\langle\phi_r,Cx\rangle=-\langle\phi_r,x\rangle\), because the marked target's uniform outgoing vector is a \(-1\) eigenvector of \(C\).

## Verification

The accompanying `verify.py` constructs the **complete, unsymmetrized directed-edge graph** (not the displayed eight-dimensional reduction), implements the Grover and negative-Grover coins using exact rational arithmetic, and compares the predicted overlap with exact evolution for each \(m\in\{0,1,\ldots,15\}\) through 55 consecutive times. All 880 exact state updates agree; the one-step incoming/outgoing convention relation also agrees exactly. Independent high-precision trigonometric checks reproduce the algebraic Chebyshev formula and the reported \(m=3\), \(t=31\) fraction. Run `python verify.py` with Python 3 and no external dependencies; `python symbolic_verify.py` optionally checks the invariant matrix factorization and first three moments using SymPy. These finite checks corroborate, but do not replace, the symbolic matrix proof or the infinite irrational-rotation argument.

## Relationship to prior work

Rani, Banerjee, Swami and Dutta introduce the marked-coin butterfly network and show finite-time body-to-body fidelity plots for a few small wing counts, including near-unity transfer on \(B_3\) at the numerical time \(31\). Their numerical observations and the graph construction are prior results. The theorem above gives an all-wing-count analytic amplitude, a sharp distinction between exact and pretty-good transfer, and an exact long-time average. In particular the visually near-unit value at \(t=31\) is strictly below one.

Štefaňák and Skoupý study a different Grover-search-transfer configuration with marked leaves on a star. Chan and Zhan develop pretty-good transfer methods for reflection-coin walks. Xu and Zhan develop more general reflection-coin subspace transfer criteria, but define the transferred coin states at a vertex to lie in the \(+1\) eigenspace of its coin; our starting and target uniform outgoing states are instead in the \(-1\) eigenspaces of the two marked body coins. Bhakta and Bhattacharjya treat unmarked Grover walks on abelian Cayley graphs, which are regular, unlike \(B_m\) for \(m\geq2\). Thus the cited transfer statements do not themselves establish the present all-wing-count amplitude or finite-time obstruction. General spectral machinery may still provide alternative ways to derive special cases.

## Limitations

This is an exactly specified noiseless, discrete-time two-marked-coin protocol. It does not imply perfect transfer at any finite time on networks with at least two wings; it does not address robustness to decoherence, time to attain a prescribed tolerance, localized vertex detection, or arbitrary initial coin states. The Cesàro formula stated for \(m\geq2\) does not extend unaltered to the rational-angle exceptional case \(m=1\). The novelty assessment is relative to the accessible cited works and claim-directed searches; a more general existing spectral theorem could imply some part of this calculation. No independent external audit has been performed.

## References

1. M. Rani, S. Banerjee, N. Swami and S. Dutta, *Quantum state transfer on a scalable network under unital and non-unital noise*, arXiv:2604.11620v1 (first publicly posted 2026-04-13), https://arxiv.org/abs/2604.11620.
2. M. Štefaňák and S. Skoupý, *Perfect state transfer by means of discrete-time quantum walk search algorithms on highly symmetric graphs*, arXiv:1608.00498, https://arxiv.org/abs/1608.00498.
3. A. Chan and H. Zhan, *Pretty good state transfer in discrete-time quantum walks*, arXiv:2105.03762, https://arxiv.org/abs/2105.03762.
4. Y. Xu and H. Zhan, *Subspace State Transfer in Coined Quantum Walks*, arXiv:2511.06750, https://arxiv.org/abs/2511.06750.
5. K. Bhakta and B. Bhattacharjya, *Pretty good state transfer in Grover walks on abelian Cayley graphs*, arXiv:2508.09711, https://arxiv.org/abs/2508.09711.
