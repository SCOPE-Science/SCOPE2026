# Flux-gated dark-mode arithmetic and perfect antipodal trapping on lossy quantum rings

## Finding

A finite, uniformly coupled quantum ring equipped with strictly positive site-local losses has an exact flux-dependent dimension of its nondecaying single-excitation subspace. The dimension is a simple greatest-common-divisor expression, and the flux switch can make a diametrically opposite excitation either completely susceptible or completely immune to a local trap.

**Theorem.** Let \(N\ge3\), \(J>0\), and let \(S\ne\varnothing\) be a set of sites in \(\mathbb Z/N\mathbb Z\). On the single-excitation space \(\mathcal H_1=\operatorname{span}\{|j\rangle:j\in\mathbb Z/N\mathbb Z\}\), define

\[
H_\phi=J\sum_{j=0}^{N-1}\big(e^{i\phi/N}|j\rangle\langle j+1|+e^{-i\phi/N}|j+1\rangle\langle j|\big).
\]

For each \(s\in S\), let the amplitude-damping jump be \(L_s=\sqrt{\gamma_s}|\Omega\rangle\langle s|\), with \(\gamma_s>0\) and a zero-excitation vacuum \(|\Omega\rangle\). Let \(\mathcal D_\phi\subseteq\mathcal H_1\) denote the *maximal invariant single-excitation dark subspace*: vectors that evolve unitarily under \(H_\phi\) and are annihilated by every \(L_s\) at every subsequent time. The total gauge flux \(\phi\) is understood modulo \(2\pi\).

Choose \(s_0\in S\) and put

\[
G=\gcd\big(N,\{s-s_0:s\in S\}\big),\qquad M=N/G,
\qquad u=\gcd(2,N),\quad t=\gcd(2,M).
\]

The integer \(G\) is independent of representatives and of the selected anchor. For every \(\phi\not\equiv0,\pi\pmod {2\pi}\),

\[\boxed{\dim\mathcal D_\phi=0.}\]

For \(\phi\equiv\ell\pi\pmod{2\pi}\) with \(\ell\in\{0,1\}\),

\[
\boxed{\dim\mathcal D_{\ell\pi}=\frac{G\,t\,\mathbf1_{t\mid\ell}-u\,\mathbf1_{u\mid\ell}}{2}.}
\]

In particular, for even \(N\), the half-flux change is *discrete*: if \(M\) is odd, \(\dim\mathcal D_\pi=\dim\mathcal D_0+1\); if \(M\) is even, \(\dim\mathcal D_\pi=0\). For odd \(N\), the dimensions at zero and half flux coincide, although the dark eigenvectors can differ.

**Perfect antipodal switch.** Suppose \(N\) is even and \(S=\{0\}\). If the initial excitation is \(|N/2\rangle\), its probability of remaining in the one-excitation sector at time \(T\) satisfies

\[
\boxed{\lim_{T\to\infty}\Pr(\text{excitation survives through }T)=
\begin{cases}1,&\phi\equiv\pi\pmod{2\pi},\\0,&\phi\not\equiv\pi\pmod{2\pi}.
\end{cases}}
\]

At half flux the survival probability equals one **for every** \(T\ge0\), not merely asymptotically. This statement holds for all \(J>0\) and all local loss rates \(\gamma_0>0\). At zero flux, an excitation at any site other than the sink and its antipode has eventual survival probability \(1/2\); the analogous statement holds at half flux except that the antipode has probability one. Off the two resonance fluxes, the eventual survival probability of every normalized one-excitation initial state is zero.

As explicit multiple-sink witnesses, for \(N=6\) and \(S=\{0,2\}\), the dark dimensions are \(0\) at zero flux and \(1\) at half flux. For \(N=6\) and \(S=\{0,3\}\), they are \(2\) and \(0\), respectively. These observations concern amplitudes in the single-excitation sector; the vacuum is trivially stationary but is not counted.

## Assumptions and scope

The ring has one mobile excitation; nearest-neighbor hopping amplitudes are homogeneous, reciprocal and have the uniform Peierls phase producing gauge-invariant total flux \(\phi\). Sites belong to \(\mathbb Z/N\mathbb Z\), with edges interpreted modulo \(N\). The losses are Markovian, independent, and strictly positive on the sites in the nonempty set \(S\); there are no other dissipative channels, onsite potentials, nonreciprocal couplings or many-excitation interactions. Vacuum gain, coherent pumping and conditional measurements are absent. A loss ends the one-particle survival event. Uniform phase distribution is a gauge choice; only the total flux has physical content. The theorem is *not* a claim that all many-body states of an XX ring are dark.

## Proof

### 1. Spectral pairing and the sink-node condition

For \(k\in\{0,1,\dots,N-1\}\), the Fourier eigenvector \(|k\rangle_F=N^{-1/2}\sum_{j=0}^{N-1}e^{2\pi i k j/N}|j\rangle\) has energy

\[
E_k=2J\cos\frac{2\pi k+\phi}{N}.
\]

A single Fourier eigenvector has nonzero amplitude of modulus \(N^{-1/2}\) at every sink. Therefore a dark eigenvector must live inside a degenerate eigenspace. An equality \(E_k=E_m\) for distinct momentum indices requires

\[
k+m+\phi/\pi\in N\mathbb Z.
\]

Because \(k,m\) are integers, this is possible only when \(\phi/\pi\in\mathbb Z\). Modulo one flux period these are the two cases \(\phi=0,\pi\). All off-resonant eigenspaces are one-dimensional and hence contain no nonzero dark vectors.

For resonance \(\phi=\ell\pi\), each degenerate pair is \(k\leftrightarrow m=-k-\ell\pmod N\). For a distinct pair, the space of combinations vanishing at the anchor \(s_0\) is one-dimensional. A convenient representative has site amplitude proportional to

\[
\psi_j=e^{2\pi i k j/N}-e^{2\pi i(k-m)s_0/N}e^{2\pi i m j/N}.
\]

It vanishes at every \(s\in S\) if and only if

\[
N\mid (k-m)(s-s_0)\quad\text{for every }s\in S.
\]

Since \(k-m\equiv2k+\ell\pmod N\), the elementary gcd identity turns these simultaneous conditions into

\[
M\mid 2k+\ell,\qquad M=N/G.
\]

The congruence has exactly \(G\gcd(2,M)\) solutions modulo \(N\) when \(\gcd(2,M)\mid\ell\), and none otherwise. Fixed points of the involution \(k\mapsto-k-\ell\), defined by \(N\mid2k+\ell\), number \(\gcd(2,N)\) if that divisor divides \(\ell\), otherwise zero. A fixed point is a simple Fourier eigenmode and cannot vanish at any sink. Removing the fixed points and dividing by two gives precisely the displayed formula. Orthogonality of distinct Fourier spectral pairs makes these one-dimensional dark eigenspaces independent, proving maximality and the dimension theorem.

For even \(N\) and odd \(M\), \(G\) is even: at zero flux the formula becomes \((G-2)/2\), and at half flux it becomes \(G/2\). For even \(N\) and even \(M\), the half-flux congruence has no solution; the zero-flux dimension is \(G-1\). For odd \(N\), both cases give \((G-1)/2\). All stated parity corollaries follow.

### 2. Dark projection and complete absorption outside it

Restrict the unconditional Lindblad dynamics to the one-excitation block. Its unnormalized density satisfies \(\rho_1(T)=e^{AT}\rho_1(0)e^{A^\dagger T}\), where

\[
A=-iH_\phi-\frac12\Gamma,\qquad \Gamma=\sum_{s\in S}\gamma_s|s\rangle\langle s|.
\]

For any eigenpair \(Av=\lambda v\), taking the real part of \(\langle v,Av\rangle\) gives

\[
\Re\lambda=-\frac{\langle v,\Gamma v\rangle}{2\langle v,v\rangle}\le0.
\]

Equality holds exactly when \(v_s=0\) at every sink. In that case \(Av=-iH_\phi v\), so \(v\) is a dark eigenvector of \(H_\phi\). Conversely, each dark eigenvector has purely imaginary eigenvalue. Since \(H_\phi\) is self-adjoint, its dark spectral subspace \(\mathcal D_\phi\) is reducing for \(H_\phi\), and \(\Gamma\) vanishes on it and has no matrix elements connecting it to its orthogonal complement. Every eigenvalue of the complementary finite-dimensional generator \(A\) has strictly negative real part; hence its semigroup converges to zero even in the possible presence of decaying Jordan blocks. Consequently, with \(P_\phi\) the orthogonal dark projector, for every normalized initial vector \(\psi\in\mathcal H_1\),

\[
\lim_{T\to\infty}\|e^{AT}\psi\|^2=\|P_\phi\psi\|^2.
\]

This also proves the independence of the limiting survival from all positive \(\gamma_s\). In the off-resonant case \(P_\phi=0\), completing the absorption argument.

### 3. The diametric one-site trap

Take \(S=\{0\}\) and even \(N\). The antisymmetric, normalized vector in a distinct Fourier pair is \((|k\rangle_F-|m\rangle_F)/\sqrt2\), where \(m=-k-\ell\pmod N\). Its squared site amplitude is

\[
|\langle j|d_{k,m}\rangle|^2=\frac1N\Big(1-\cos\frac{2\pi(k-m)j}{N}\Big).
\]

At the antipode \(j=N/2\), the parity relation gives \((-1)^m=(-1)^{k+\ell}\). For zero flux \(\ell=0\), every dark vector has zero amplitude there. For half flux \(\ell=1\), every complementary *bright* Fourier sum has zero amplitude there, all Fourier modes occur in distinct pairs, and so \(|N/2\rangle\in\mathcal D_\pi\). Thus at \(\phi=\pi\) this state evolves entirely within a jump-free space, giving survival exactly one at all times. At zero flux the dark projection is zero, giving eventual survival zero. Outside \(\phi=0,\pi\), the first step gives no dark modes, completing the binary switch.

For a site different from the sink and its antipode, evaluate the dark-projection diagonal by Fourier orthogonality. For \(\ell\in\{0,1\}\), the number of non-fixed pairs is \((N-2)/2\) at zero flux and \(N/2\) at half flux. The full sum of squared antisymmetric amplitudes yields exactly \(1/2\), while the sink has zero projection by construction. These additional statements can also be verified directly by summing the associated geometric series; the claimed values are not inferred from the finite numerical examples.

## Verification

The included source file `verify_flux_sink.py` is an independent finite-dimensional checker requiring Python, NumPy and SciPy. Execute `python verify_flux_sink.py` in a directory containing the extracted file. The actual run returned `PASS 3183 finite checks`. It separately constructs the hopping Hamiltonian and Fourier dark vectors, checks gcd-dimension predictions, orthonormality, sink nodes and eigenvector equations for many sink sets and sizes, tests generic flux spectral simplicity, checks antipodal projection probabilities up through size 26, and uses matrix exponentials to cross-check finite-time protection and long-time absorption on smaller rings. Finite testing supplements but does not replace the preceding proof for all \(N\), fluxes, sink sets and positive loss rates.

## Relationship to prior work

Çakmak, Sümer, Campbell and Karpat (2026) characterize decoherence-free states and synchronization for a dissipative *open XX chain*, with a path-length gcd formula. That recent public model motivates examining topology and gauge flux, but its open-chain conditions do not imply the cyclic Peierls-phase formula here.

Krapivsky, Luck and Mallick (2013/2014) explicitly derive nondecaying modes and survival probabilities for *zero-flux* tight-binding rings with one or multiple traps. Their zero-flux trap-position gcd and antipodal absorption mechanisms are **prior results** and are not claimed as novel. The present assessed claim is confined to the flux-resolved family, especially half-flux mode creation/destruction with arbitrary trap sets and the binary lossless-antipodal control; this comparison is important because the zero-flux restriction of the formula is already substantially covered.

Le, Donati, Severini and Caruso (2018) give general graph-theoretic dark-subspace criteria for quantum transport, with detailed dark-state suppression; these provide broader conceptual tools but no located explicit flux-dependent arbitrary-sink cyclic arithmetic in the inspected material. Luppi (2026) studies magnetic-flux control of single-vertex *measurement back-action* in chiral continuous-time walks, including a four-cycle half-flux effect. Its accessible abstract makes the flux-interference mechanism a known precursor, not an originality claim; full text was not accessible for a definitive stronger comparison. The exact general loss/subspace classification may also be implicit in some existing spectral and controllability results. No priority beyond the checked sources is certified.

## Limitations

This is a one-excitation, homogeneous, uniformly phased ring. The outcome need not persist with onsite disorder, hopping disorder, extra dissipators, multiple excitations, or imperfectly tuned flux. The claim is about strict nondecaying modes and asymptotic survival at fixed parameters, not a uniform-in-flux finite-time convergence rate: as flux approaches a resonant value, decay times can become large, and the infinite-time limit need not commute with the flux limit. The generic-flux result does not assert finite-time zero survival. The existing zero-flux ring results are excluded from any priority claim. Broader spectral literature and an inaccessible 2026 flux-walk full text are residual originality risks. Independent validation and priority certification have not been performed.

## References

1. B. Çakmak, K. Sümer, S. Campbell and G. Karpat, *Synchronization in a dissipative quantum many-body system*, arXiv:2604.18707 (first publicly submitted 20 April 2026), https://arxiv.org/abs/2604.18707.
2. P. L. Krapivsky, J. M. Luck and K. Mallick, *Survival of classical and quantum particles in the presence of traps*, arXiv:1311.6298 (2013), *Journal of Statistical Physics* **154** (2014), 1430–1460, https://arxiv.org/abs/1311.6298.
3. T. P. Le, L. Donati, S. Severini and F. Caruso, *How to suppress dark states in quantum networks and bio-engineered structures*, *Journal of Physics A* **51** (2018), 365306, https://doi.org/10.1088/1751-8121/aad3e6.
4. P. Luppi, *Flux control of measurement back-action and Leggett-Garg correlations in chiral quantum walks*, arXiv:2608.12519 (2026), https://arxiv.org/abs/2608.12519.
