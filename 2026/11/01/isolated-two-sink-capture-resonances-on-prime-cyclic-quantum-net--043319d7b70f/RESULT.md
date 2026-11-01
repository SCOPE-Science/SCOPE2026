# Isolated two-sink capture resonances on prime cyclic quantum networks

## Finding

Let \(p=2m+1\ge5\) be an odd prime. A continuous-time quantum walker on the cyclic group \(\mathbb Z/p\mathbb Z\) hops with independently tunable positive nearest-neighbor and next-nearest-neighbor amplitudes \(J_1,J_2>0\), while two distinct sites \(0,d\) absorb at any positive rates. Put \(r=J_2/J_1\), and \(c_j=\cos(2\pi j/p)\). For the initially maximally mixed state, eventual capture is complete except at the precisely \(\lfloor m^2/4\rfloor\) distinct positive ratios

\[
 r_{k,l}=-\frac{1}{2(c_k+c_l)},\qquad 1\le k<l\le m,\quad k+l\ge m+1.
\]

At each ratio \(r_{k,l}\), the nondecaying subspace has dimension exactly two and the eventual capture probability is \(1-2/p\); elsewhere it is \(1\). These assertions hold for every nonzero trap separation and every pair of strictly positive absorption rates, and there are no other exceptional ratios.

The same theorem gives a site-resolved law. At \(r=r_{k,l}\), define \(F(t)=\cos(2\pi kt/p)+\cos(2\pi lt/p)\), \(A=F(d)\), with all arguments interpreted modulo \(p\). A walker initially localized at \(x\) survives indefinitely with probability

\[
 q(x)=\frac4p\left[1-\frac{F(x)^2+F(x-d)^2-A F(x)F(x-d)}{4-A^2}\right].
\]

Its eventual capture is \(1-q(x)\); away from every exceptional ratio, its capture is \(1\). The displayed denominator is strictly positive. At either absorbing vertex the survival probability is zero.

## Assumptions and scope

The one-excitation Hilbert space has orthonormal site basis \(\{|x\rangle:x\in\mathbb Z/p\mathbb Z\}\). Define the Hermitian Hamiltonian and the lossy no-jump generator by

\[
 H=\sum_{x=0}^{p-1}\sum_{a=1}^2J_a\bigl(|x\rangle\langle x+a|+|x+a\rangle\langle x|\bigr),
 \qquad K=H-\frac{i}{2}\left(\kappa_0|0\rangle\langle0|+\kappa_d|d\rangle\langle d|\right),
\]

where \(1\le d\le p-1\), \(\kappa_0,\kappa_d>0\), and \(J_a>0\). Time evolution without a recorded capture is \(T(t)=e^{-itK}\). For a normalized pure initial state \(|\psi\rangle\), define eventual capture as \(\eta_\psi=1-\lim_{t\to\infty}\|T(t)|\psi\rangle\|^2\); the mixed-state definition replaces the squared norm by \(\operatorname{tr}[T(t)\rho T(t)^*]\). There is no homogeneous recombination, dephasing, diagonal disorder, or extra sink. The result is an exact infinite-time statement; it gives no uniform finite capture-time bound near resonance.

## Proof

**1. Fourier spectrum and all possible level collisions.** Let \(\zeta=e^{2\pi i/p}\) and \(|v_a\rangle=p^{-1/2}\sum_x\zeta^{ax}|x\rangle\) for \(a\in\mathbb Z/p\mathbb Z\). Fourier diagonalization gives

\[
 H|v_a\rangle=E_a|v_a\rangle,\qquad E_a=2J_1\cos(2\pi a/p)+2J_2\cos(4\pi a/p).
\]

Thus \(E_a=E_{p-a}\), and \(E_0>E_a\) for every \(a\ne0\), because both couplings are positive. For distinct \(1\le k<l\le m\), the identity \(\cos(2\theta)=2\cos^2\theta-1\) gives

\[
 E_k-E_l=2(c_k-c_l)\bigl(J_1+2J_2(c_k+c_l)\bigr).
\]

Since the \(c_j\) are strictly decreasing for \(1\le j\le m\), their levels coincide precisely at \(r=-1/[2(c_k+c_l)]\). Furthermore,

\[
 c_k+c_l=2\cos\frac{(k+l)\pi}{p}\cos\frac{(l-k)\pi}{p}.
\]

The second cosine is positive. Since \(k+l\) is integral and \(p=2m+1\), the sum is negative exactly when \(k+l\ge m+1\), establishing the positive-resonance set.

**2. Collisions are isolated and pairwise distinct.** The real numbers \(c_1,\dots,c_m\) are linearly independent over \(\mathbb Q\) for prime \(p\). Indeed, a rational relation \(\sum_{j=1}^m a_jc_j=0\) yields the polynomial \(P(z)=\sum_j a_j(z^j+z^{p-j})\), of degree at most \(p-1\) and with zero constant coefficient, satisfying \(P(\zeta)=0\). The minimal polynomial of \(\zeta\) over \(\mathbb Q\) is \(1+z+\cdots+z^{p-1}\), so \(P\) would have to be its rational scalar multiple. Its zero constant coefficient forces \(P=0\), and disjoint monomial supports then give \(a_j=0\) for all \(j\). In particular, equality of two sums \(c_k+c_l\) forces equality of their unordered index pairs. Hence no two collision ratios coincide, and each resonance coalesces exactly two Fourier pairs into one four-dimensional eigenspace.

Counting the eligible pairs gives

\[
 \#\{(k,l):1\le k<l\le m,\ k+l\ge m+1\}=\lfloor m^2/4\rfloor.
\]

For each fixed \(1\le k\le m-1\), the possible values of \(l\) are the integers from \(\max(k+1,m+1-k)\) through \(m\). Their number is \(\min(k,m-k)\), so the total is \(\sum_{k=1}^{m-1}\min(k,m-k)=\lfloor m^2/4\rfloor\). This also covers \(m=2\).

**3. Complete characterization of nondecaying states.** For a vector \(\psi(t)\), differentiation yields

\[
 \frac{d}{dt}\|\psi(t)\|^2=-\kappa_0|\psi_0(t)|^2-\kappa_d|\psi_d(t)|^2\le0.
\]

Every eigenvector of \(K\) with real eigenvalue has zero amplitude at both sinks by taking the imaginary part of its eigenvalue identity; it is consequently an eigenvector of \(H\). Conversely any \(H\)-eigenvector vanishing at both sinks is an undamped \(K\)-eigenvector. These dark eigenspaces reduce both \(H\) and \(K\). All eigenvalues on their orthogonal complement have strictly negative imaginary parts (otherwise another real eigenvector would be dark), so finite-dimensional Jordan theory implies the complementary propagator tends to zero. Thus indefinite survival of any pure or mixed state is exactly its orthogonal projection onto the sum of the dark eigenspaces.

For a simple Fourier level \(a=0\), the single eigenvector is nonzero at both traps. For an ordinary doublet \(\operatorname{span}\{|v_a\rangle,|v_{-a}\rangle\}\), evaluation at the two traps has a \(2\times2\) determinant proportional to \(\zeta^{ad}-\zeta^{-ad}\), nonzero because \(p\) is odd prime and \(a,d\not\equiv0\pmod p\). Hence ordinary doublets have no dark state. At a resonance \((k,l)\), the four-dimensional space has trap-evaluation rank precisely two: the columns for \(v_k,v_l\) have determinant proportional to \(\zeta^{ld}-\zeta^{kd}\ne0\), while the map has only two rows. It therefore contributes exactly two dark eigenvectors. By step 2 there is only one such four-dimensional level at each resonance. The total dark dimension is consequently either \(0\) or \(2\), proving all capture probabilities for the maximally mixed state.

**4. Exact localized survival formula.** At the exceptional level let \(P_E\) denote its orthogonal spectral projector. The real symmetric kernel is \(P_E(x,y)=(2/p)F(x-y)\). The two vectors \(P_E|0\rangle\) and \(P_E|d\rangle\) span the bright part of this level, with Gram matrix

\[
 G=\frac2p\begin{pmatrix}2&A\\A&2\end{pmatrix},\qquad A=F(d).
\]

Its strict positivity follows from the rank-two argument in step 3, hence \(4-A^2>0\). Subtracting the projector onto that bright part from \(P_E\), and computing its \((x,x)\) entry with \(G^{-1}\), gives precisely the stated \(q(x)\). Since this projector has rank two, \(\sum_xq(x)=2\), consistent with the maximally mixed result. No absorption rate appears because the dark space depends only on the sinks' locations, not the magnitude of their strictly positive rates.

## Verification

The standalone `checker.py` constructs the Hermitian matrices independently, diagonalizes them numerically, evaluates two-sink null spaces by singular-value decomposition, and compares the resulting site projectors to the analytic formula for every pair of sink locations in all exceptional configurations and multiple ordinary configurations for prime sizes \(5,7,11,13,17,19,23,29\). It also compares selected large-time lossy propagators with the exact mixed-state asymptotic survival. The actual replay result is in `verification_output.txt`. These are finite numerical cross-checks, not substitutes for the proof for all primes. Independent expert validation has not been performed.

## Relationship to prior work

Parlangeli and Notarstefano (2011) prove arithmetic controllability and observability for **ordinary nearest-neighbor** paths and cycles, including complete two-vertex observation on prime cycles. This is the baseline at zero next-neighbor coupling; the level-crossing mechanism introduced by the additional coupling is absent there. Kassal and Aspuru-Guzik (2012) analyze environment-assisted transport and a single trapping vertex on a cycle, establishing the physical motivation but not the two-sink spectral-resonance law.

Candeloro and collaborators (2020) solve the Fourier dynamics of cycle walks with a quadratic-Laplacian term; their spectral method and the presence of next-neighbor hopping are existing antecedents. The corresponding closed-system Fourier eigenvalues are not claimed here as new. The inspected treatment focuses on coherent spreading and parameter estimation without the two-absorber dark-space classification, prime-index resonance census, or localized capture formula. Razzoli, Paris, and Bordone (2020/2021) prove a general single-sink spectral-subspace method for transport efficiency. That method is also credited, and does not by itself provide the present simultaneous spectral-collision and two-sink classification. The new contribution assessed here is the complete coupling-dependent two-site capture theorem, not the individual Fourier or projection tools.

## Limitations

The theorem requires prime odd circumference, two distinct perfect absorbing vertices with strictly positive loss rates, coherent single-excitation dynamics, and positive uniform hopping at distances one and two. It does not cover composite rings, negative hopping amplitudes, three or more sinks, on-site disorder, dephasing, finite-time capture rates, or generic many-body physics. A specialized unpublished or unlocated prior classification of the same two-sink model remains a historical-priority risk. A self-review is not independent validation.

## References

- G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs* (first public 2011-09-16), https://arxiv.org/abs/1109.3556 .
- I. Kassal and A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems* (first public 2012-01-25), https://arxiv.org/abs/1201.5202 .
- C. M. Chandrashekar and T. Busch, *Noise-enhanced quantum transport on a closed loop using quantum walks* (2012), https://arxiv.org/abs/1209.3144 .
- A. Candeloro, L. Razzoli, S. Cavazzoni, P. Bordone and M. G. A. Paris, *Continuous-time quantum walks in the presence of a quadratic perturbation* (first public 2020-05-13), https://arxiv.org/abs/2005.06351 .
- L. Razzoli, M. G. A. Paris and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs* (first public 2020-11-27), https://arxiv.org/abs/2011.13794 ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC7826824/ .
