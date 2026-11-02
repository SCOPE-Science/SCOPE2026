# Flux-selective arithmetic dark states with two detectors on a quantum ring

## Finding

For a uniform magnetic tight-binding quantum walk on a finite ring, monitoring two sites produces an exact greatest-common-divisor classification of the entire dark subspace and the eventual nondetection probability from every localized initial state. Its dependence on the enclosed flux is nonmonotone: half a flux quantum can either create or eliminate exact dark modes. For continuous absorption or nonresonant projective sampling, complete eventual detection at **every** magnetic flux is guaranteed precisely when the detector spacing is coprime to the ring size.

Here is the exact theorem. Let \(N\geq3\) be the number of ring sites and let \(d\in\{1,\ldots,N-1\}\) be the second monitored site, the first being site \(0\). Let \(T|j\rangle=|j+1\pmod N\rangle\), and let
\[
H_\phi=-J\big(e^{-i\phi/N}T+e^{i\phi/N}T^\dagger\big),\quad J>0,\quad \phi\in[0,2\pi).
\]
Take \(P=|0\rangle\langle0|+|d\rangle\langle d|\). Define \(\mathcal D_\phi\) as the maximal \(H_\phi\)-invariant subspace in \(\ker P\), \(D_\phi=\dim\mathcal D_\phi\), and \(W_j(\phi)=\|\Pi_{\mathcal D_\phi}|j\rangle\|^2\) for each \(j\in\{0,\ldots,N-1\}\). Then, with \(g_0=\gcd(N,2d)\) and \(s_0=\gcd(N,2)\), at zero flux,
\[
D_0=\frac{g_0-s_0}{2},\qquad
W_j(0)=\begin{cases}0,&g_0\mid 2j,\\[2pt]g_0/(2N),&g_0\nmid 2j.\end{cases}
\]
At half a flux quantum, \(\phi=\pi\), put \(g_1=\gcd(N,d)\) and \(M=N/g_1\). If \(M\) is even, \(D_\pi=0\) and \(W_j(\pi)=0\) for all \(j\). If \(M\) is odd and \(N\) is odd,
\[
D_\pi=\frac{g_1-1}{2},\qquad
W_j(\pi)=\begin{cases}0,&g_1\mid j,\\[2pt]g_1/(2N),&g_1\nmid j.\end{cases}
\]
If \(M\) is odd and \(N\) is even (in which case \(g_1\) is even),
\[
D_\pi=\frac{g_1}{2},\qquad
W_j(\pi)=\begin{cases}
0,&j\equiv0\pmod{g_1},\\[2pt]
g_1/N,&j\equiv g_1/2\pmod{g_1},\\[2pt]
g_1/(2N),&\text{otherwise}.
\end{cases}
\]
For every other flux, \(D_\phi=0\) and \(W_j(\phi)=0\) for every site. Consequently, \(D_\phi=0\) for **all** fluxes if and only if \(\gcd(N,d)=1\); this is exactly the all-flux complete-detection criterion for continuous absorption and nonresonant projective monitoring.

These weights have two operational interpretations. For every absorption strength \(\kappa>0\),
\[
\lim_{t\to\infty}\Big\|e^{t(-iH_\phi-\kappa P/2)}|j\rangle\Big\|^2=W_j(\phi).
\]
For projective two-site monitoring every \(\tau>0\), with \(Q=(I-P)e^{-iH_\phi\tau}\), the same weight is
\[
\lim_{m\to\infty}\|Q^m|j\rangle\|^2=W_j(\phi),
\]
provided no two **distinct** energy eigenvalues differ by an integer multiple of \(2\pi/\tau\). This excludes a countable set of stroboscopic sampling resonances and makes no claim at those exceptional periods.

For a minimal flux-switching example, take \(N=6\). With second detector at \(d=2\), zero flux has no dark states, while half flux creates one and gives \(W_1(\pi)=1/3\). With detector at \(d=3\), zero flux instead has two dark states and gives \(W_1(0)=1/2\), while half flux eliminates every dark state.

## Assumptions and scope

The walk is a coherent, uniform, nearest-neighbor one-particle tight-binding model on a finite cycle, with a static gauge flux. The two monitor sites are simultaneous and distinct. The continuous detector is a positive uniform absorbing potential at those sites; the discrete detector uses a projective yes/no measurement onto their joint subspace at a single fixed sampling interval. All statements cover every permitted ring length, spacing, site and flux, except that the stroboscopic survival identity excludes the explicitly stated sampling resonances. Detection rates may affect transients, but not the limiting continuous survival probability.

## Proof

**Energy pairing.** Plane waves \(|k\rangle=N^{-1/2}\sum_{j=0}^{N-1}e^{2\pi i kj/N}|j\rangle\), for \(k\) modulo \(N\), diagonalize \(H_\phi\), with energies \(E_k=-2J\cos((2\pi k+\phi)/N)\). For distinct indices, equality of the cosines requires their angles to be negatives modulo \(2\pi\). Thus energy degeneracies are possible only when \(\phi=0\) or \(\phi=\pi\) modulo \(2\pi\). At \(\phi=q\pi\) with \(q\in\{0,1\}\), the paired index is \(\ell\equiv-q-k\pmod N\).

**Dark vectors.** Every plane wave has nonzero amplitude at site \(0\); hence no nondegenerate energy sector contains a dark vector. In a two-dimensional degenerate sector, orthogonality to site \(0\) forces the unique candidate \((|k\rangle-|\ell\rangle)/\sqrt2\). Orthogonality to site \(d\) is then equivalent to
\[
N\mid d(k-\ell),\quad\text{or}\quad N\mid d(2k+q).
\]
The set \(\Omega_q=\{k\pmod N:N\mid d(2k+q)\}\) is invariant under pairing. Every non-fixed pair in this set contributes exactly one orthonormal dark vector; a fixed index contributes none.

**Dimension and arithmetic.** For \(q=0\), the number of solutions to \(N\mid2dk\) is \(g_0\), with \(s_0\) fixed points of \(2k\equiv0\pmod N\), giving \(D_0=(g_0-s_0)/2\). For \(q=1\), writing \(g_1=\gcd(N,d)\) and \(M=N/g_1\), the condition is \(M\mid(2k+1)\). It has no solutions when \(M\) is even; otherwise it has exactly \(g_1\) solutions. There is one fixed point of \(2k+1\equiv0\pmod N\) for odd \(N\), and none for even \(N\). This yields all three half-flux dimension formulas.

**Weights.** Squaring localized overlaps with the pairwise normalized dark vectors gives the general finite character formula
\[
W_j(q\pi)=\frac1{2N}\sum_{k\in\Omega_q}\bigg[1-\cos\bigg(\frac{2\pi(2k+q)j}{N}\bigg)\bigg].
\]
At zero flux, \(\Omega_0\) is a cyclic subgroup of size \(g_0\). Its character sum is \(g_0\) when \(g_0\mid2j\), and zero otherwise. At half flux with odd \(M\), the allowed odd numbers \(2k+1\) form one coset modulo \(N\). For odd \(N\), the character sum is \(g_1\) exactly when \(g_1\mid j\), otherwise zero. For even \(N\), it equals \(g_1\), \(-g_1\), or \(0\), according as \(j\equiv0\), \(g_1/2\), or neither modulo \(g_1\). Substitution proves every stated survival weight.

**Detection dynamics.** Write \(G=-iH_\phi-\kappa P/2\). For its evolution, \(d\|\psi_t\|^2/dt=-\kappa\|P\psi_t\|^2\). Hence an eigenvector on the imaginary axis must be annihilated by \(P\) and be an eigenvector of \(H_\phi\); conversely every such vector remains undamped. The resulting dark space is reducing for both Hermitian matrices, and all eigenvalues on its invariant orthogonal complement have strictly negative real parts; therefore that complement decays, establishing continuous survival. Similarly, \(Q=(I-P)U\) is a contraction. A unit-modulus eigenvector of \(Q\) must obey \(P U\psi=0\) and \(U\psi=\lambda\psi\). When distinct energy levels do not alias at the sampling period, the unit-modulus subspace is exactly \(\mathcal D_\phi\). All remaining eigenvalues are strictly inside the unit disk, proving the stroboscopic limit.

**Coprime design criterion.** If \(\gcd(N,d)=1\), then \(g_0=s_0\) and \(g_1=1\); all dark dimensions vanish. Conversely, if \(g=\gcd(N,d)>1\) and \(N\) is odd, then \(D_0=(g-1)/2>0\). If \(N\) is even and \(g_0>2\), then \(D_0>0\). In the remaining even case, \(g_0=2\) forces \(g=2\) and \(N/2\) odd, so \(D_\pi=1\). Therefore a noncoprime separation always admits dark states at one of the two special fluxes.

## Verification

The included standalone script `quantum_ring_dark_check.py` reconstructs spectral dark vectors directly from paired Fourier waves and independently checks dimensions and individual site weights over all \(3\le N\le36\), every distinct detector spacing, both exceptional fluxes, and every localized initial site. It also independently propagates absorbing and projective finite matrices on representative examples, including both directions of flux switching and a generic-flux control. Execute `python quantum_ring_dark_check.py` with Python 3, NumPy and SciPy installed. The recorded output from this actual package source was `PASS 32975 exact-arithmetic/Fourier, absorbing and projective evolution checks`. This finite testing corroborates but does not replace the all-size proof above.

## Relationship to prior work

Wang, Ren, Yin, Ziegler, Barkai and Tornow [1] analyze an experimentally monitored **three-site** flux-threaded triangle, contrasting a one-site detector with full position tracking. They demonstrate dark states, phase-dependent detection and sampling resonances. The present result addresses the intermediate **two-simultaneous-site** protocol on arbitrary cycles and derives an exact spacing-dependent arithmetic classification. Thiel, Mualem, Meidan, Barkai and Kessler [2] establish the general finite-dimensional dark/bright spectral-projection principle and discuss **single-target** detection on magnetic rings. The proof uses that known spectral mechanism; its claim is not to invent dark-space projection but to evaluate the two-target projection in closed form, including flux-switchable localized weights and the coprime all-flux design criterion. Thiel, Mualem, Kessler and Barkai [3] separately develop symmetry bounds for single-target detection. These are relevant frameworks rather than claims of an absent general theory.

## Limitations

The classification concerns exact infinite-time/no-click limits, not finite-time detection rates or optimal measurement times. At exceptional stroboscopic sampling periods, distinct energy eigenvalues can alias and additional dark states may appear. Weak/nonprojective monitoring that is not represented by the specified absorbing potential, nonuniform hopping, noise, disorder, time-varying magnetic flux and interacting many-particle walks are outside scope. Although no direct two-detector flux-parity formula was identified in the examined primary literature and mathematical records, an unexamined multi-target observability theorem could provide an alternative derivation; independent priority review remains necessary.

## References

1. Q. Wang, S. Ren, R. Yin, K. Ziegler, E. Barkai, S. Tornow, *First Hitting Times on a Quantum Computer: Topological Effects and Dark States*, arXiv:2402.15843v1 (first public 2024-02-24). https://arxiv.org/html/2402.15843v1
2. F. Thiel, I. Mualem, D. Meidan, E. Barkai, D. A. Kessler, *Quantum total detection probability from repeated measurements I. The bright and dark states*, arXiv:1906.08112 (2019). https://arxiv.org/abs/1906.08112
3. F. Thiel, I. Mualem, D. A. Kessler, E. Barkai, *Quantum total detection probability from repeated measurements II. Exploiting symmetry*, arXiv:1909.02114 (2019). https://arxiv.org/abs/1909.02114
