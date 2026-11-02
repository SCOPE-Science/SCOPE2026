# Arithmetic bright-site criterion and Ramanujan capture law for quantum spider networks

## Finding
Consider a finite spider network with a single absorbing hub and any number of unequal path arms. The eventual first-absorption probability of **every** initially occupied vertex is given by a finite divisor sum with integer Ramanujan coefficients. More sharply, all vertices that are captured with probability one admit an exact greatest-common-divisor/least-common-multiple classification.

Write the number of vertices on arm \(i\) as \(\ell_i\), and put \(L_i=\ell_i+1\). For each positive integer \(q\), define
\[
I_q=\{i:q\mid L_i\},\qquad c_q=|I_q|,\qquad W_q=\sum_{j\in I_q}\frac1{L_j}.
\]
Let \(\varphi(q)\) be Euler's totient, and let the Ramanujan sum be
\[
C_q(t)=\sum_{\substack{1\le a<q\\\gcd(a,q)=1}}\cos(2\pi at/q)
=\sum_{d\mid\gcd(q,t)}d\,\mu(q/d),
\]
where \(\mu\) is the Möbius function. For an excitation initially at distance \(t\) along arm \(i\), the exact asymptotic survival probability is
\[
\boxed{\displaystyle
S(i,t)=\frac1{L_i}\sum_{\substack{q\mid L_i\\q\ge2,\ c_q\ge2}}
\bigl(\varphi(q)-C_q(t)\bigr)
\left(1-\frac1{L_iW_q}\right).}
\]
Its eventual first-capture probability is \(1-S(i,t)\); the hub itself is captured with probability one. These answers are independent of the positive hopping and absorption rates.

Define
\[
\boxed{\displaystyle G_i=\operatorname{lcm}_{j\ne i}\gcd(L_i,L_j).}
\]
Then the site \((i,t)\) is captured with probability **exactly one** if and only if \(G_i\mid t\). Thus the number of perfectly capturable vertices, including the hub, is exactly
\[
\boxed{\displaystyle B=1+\sum_{i=1}^m\left(\frac{L_i}{G_i}-1\right).}
\]
In particular, all initial vertices are eventually captured with probability one if and only if the shifted arm lengths \(L_1,\ldots,L_m\) are pairwise coprime.

The full dark-space dimension and the capture probability for the maximally mixed single-excitation state are, respectively,
\[
\boxed{\displaystyle
D=\sum_{q=2}^{\max_iL_i}\varphi(q)\max(c_q-1,0),\qquad
P_{\mathrm{mix}}=1-\frac{D}{1+\sum_i\ell_i}.}
\]
These are exact for any finite number of arms and any positive integer arm lengths.

## Assumptions and scope
Fix an integer \(m\ge3\) and integers \(\ell_1,\ldots,\ell_m\ge1\). The graph \(S(\ell_1,\ldots,\ell_m)\) has one hub \(o\), arm vertices \((i,t)\) for \(1\le i\le m\) and \(1\le t\le\ell_i\), and precisely the edges \(o\leftrightarrow(i,1)\) and \((i,t)\leftrightarrow(i,t+1)\). Let \(A\) be its real adjacency matrix. The single-excitation tight-binding Hamiltonian has uniform real positive hopping \(J A\), and the hub is an irreversible loss site of rate \(\kappa>0\). No additional onsite potentials, other reservoirs or dephasing are present.

For a unit initial state \(\psi\), the no-jump state at time \(T\ge0\) is \(\exp[-i(JA-i\kappa|o\rangle\langle o|/2)T]\psi\). Its squared norm is the probability that no first loss event has yet occurred. Define \(S(\psi)\) as the limit of this probability as \(T\to\infty\). The theorem concerns basis-state inputs \(|i,t\rangle\), the hub input, and the uniform mixed one-excitation input \(I/N\), where \(N=1+\sum_i\ell_i\).

## Proof
**1. The surviving subspace.** Let \(H_{\mathrm{eff}}=JA-i\kappa|o\rangle\langle o|/2\). Its maximal nondecaying invariant subspace is the span \(\mathcal D\) of adjacency eigenvectors orthogonal to \(|o\rangle\). Indeed, \(\mathcal D\) is reducing for both \(A\) and the hub projector; all states in \(\mathcal D\) evolve unitarily. On its orthogonal complement, every eigenvalue of \(H_{\mathrm{eff}}\) has strictly negative imaginary part. To see this, an eigenvector with real eigenvalue must satisfy the imaginary part identity \(-\kappa|\psi(o)|^2/2=0\), and is therefore a hub-orthogonal eigenvector of \(A\), contradicting membership in the complement. Jordan blocks in the strictly decaying sector also vanish exponentially with a polynomial prefactor. Consequently \(S(\psi)=\|P_{\mathcal D}\psi\|^2\).

**2. Common path modes.** An eigenvector in \(\mathcal D\) has hub amplitude zero. Deleting the hub leaves disjoint paths of orders \(\ell_i=L_i-1\). The normalized modes on arm \(i\) are
\[
u_{i,a}(t)=\sqrt{2/L_i}\sin(\pi at/L_i),\quad
1\le a<L_i,
\]
with eigenvalue \(2\cos(\pi a/L_i)\). Reduced fractions \(a/L_i=b/q\), with \(1\le b<q\) and \(\gcd(b,q)=1\), label these eigenvalues uniquely; such an eigenvalue occurs on arm \(i\) exactly when \(q\mid L_i\). For each fixed reduced \(b/q\), the hub eigenvalue equation imposes a single linear constraint on the \(c_q\) available arm amplitudes. Its coefficients are all nonzero, so the corresponding dark eigenspace has dimension \(c_q-1\) when \(c_q\ge2\), and zero otherwise. There are \(\varphi(q)\) distinct reduced numerators. Summing proves the formula for \(D\), and tracing the projector proves the mixed-state capture formula.

**3. Site-resolved projection.** At eigenvalue \(2\cos(\pi b/q)\), the hub coupling of the normalized arm mode is \(\sqrt{2/L_i}\sin(\pi b/q)\). Therefore, in the arm coefficient space indexed by \(I_q\), the rank-one hub-visible direction has squared coordinate weights proportional to \(1/L_i\). The diagonal of its orthogonal-complement projector on coordinate \(i\) is exactly \(1-(L_iW_q)^{-1}\). At site \((i,t)\), the mode intensity is \((2/L_i)\sin^2(\pi bt/q)\). Summing over reduced numerators and using
\[
\sum_{\substack{1\le b<q\\\gcd(b,q)=1}}2\sin^2(\pi bt/q)
=\varphi(q)-C_q(t)
\]
proves the displayed divisor sum for \(S(i,t)\).

**4. Exact bright-site criterion.** Every summand of \(S(i,t)\) is nonnegative. When \(c_q\ge2\), the projector factor is strictly positive. Moreover, \(\varphi(q)-C_q(t)\) is zero exactly when \(q\mid t\): it is a sum of nonnegative \(2\sin^2(\pi bt/q)\), and already \(b=1\) detects nondivisibility. Hence \(S(i,t)=0\) precisely when every divisor \(q\ge2\) of a common shifted length \(\gcd(L_i,L_j)\) divides \(t\). This is equivalent to \(G_i\mid t\). Since \(G_i\mid L_i\), exactly \(L_i/G_i-1\) integers \(t\) in \(1,\ldots,L_i-1\) satisfy this divisibility, proving \(B\). Finally, \(D=0\) holds precisely when no integer \(q\ge2\) divides two shifted arm lengths, equivalently to pairwise coprimality.

## Verification
The companion program `verify_spider.py` independently constructs the graph adjacency matrix, diagonalizes it numerically, forms each eigenspace projector, subtracts its hub-visible component, and compares all vertex diagonal projections with the divisor-sum formula. It also checks the dark-space trace and the exact bright-site congruence criterion. Running `python3 verify_spider.py` with NumPy verifies 715 finite spider graphs and 7,973 site projections; the maximal absolute difference is below \(2.3\times10^{-15}\). When SciPy is available it additionally compares four positive-loss non-Hermitian evolutions at time \(T=12000\) with the asserted infinite-time limits; the maximum difference in this sample is below \(1.2\times10^{-12}\).

For example, arms of lengths \((1,3,5)\) have shifted lengths \((2,4,6)\), exactly two dark modes, and ten vertices. The maximally mixed capture probability is \(4/5\). All three arms have \(G_i=2\): the hub and precisely the even-distance sites on the second and third arms are perfectly capturable, although the odd-distance sites survive with probabilities \(5/11\), \(4/11\) and \(3/11\) on their respective arms. These finite calculations support but do not substitute for the proof for all arm lengths.

## Relationship to prior work
Anishchenko, Blumen and Mülken (2011), arXiv:1111.7065, analyze coherent spreading on ordinary star and complete graphs and perturbations by additional bonds. Their ordinary star is the special case in which every arm has one vertex, without a hub absorber or heterogeneous arm-length arithmetic. The standard bright/dark spectral projector principle is independently developed for repeated quantum detection by Thiel, Mualem, Meidan, Barkai and Kessler (2019/2020), arXiv:1906.08112. The spectral projection method itself is not claimed as new here, and their measurement protocol differs from continuous irreversible loss. The new statement is the all-arm-length exact Ramanujan evaluation and the position-by-position gcd/lcm classification, which require identifying and combining all coincident path spectra.

Yalouz and Pouthier (2018), DOI:10.1103/PhysRevE.97.022304, treat hub trapping on a symmetric two-generation extended star. The available description confirms direct topical relevance and an exact symmetric-model analysis; the complete paper could not be accessed for a decisive historical-priority comparison. No priority claim is made for the general dark/bright decomposition, equal-arm special cases, or the existence of symmetric-star trapping.

## Limitations
The results are for finite graphs, one irreversible hub trap, ordinary symmetric adjacency hopping with a common nonzero coupling, and one-excitation dynamics. They do not determine capture-time distributions, optimize loss rates, classify unequal edge couplings or onsite energies, or cover multiple absorbing vertices. They are not an infinite-volume absorption theorem, and no independent literature-priority or scientific audit is claimed. The closely related 2018 extended-star paper remains a material historical-coverage risk because its complete text was not available.

## References
1. A. Anishchenko, A. Blumen, O. Mülken, *Enhancing the spreading of quantum walks on star graphs by additional bonds*, arXiv:1111.7065 (first posted 2011-11-30), https://arxiv.org/abs/1111.7065.
2. S. Yalouz and V. Pouthier, *Continuous-time quantum walk on an extended star graph: Trapping and superradiance transition*, Physical Review E **97**, 022304 (2018), https://doi.org/10.1103/PhysRevE.97.022304.
3. F. Thiel, I. Mualem, D. Meidan, E. Barkai and D. A. Kessler, *Dark states of quantum search cause imperfect detection*, arXiv:1906.08112 (first posted 2019-06-19), https://arxiv.org/abs/1906.08112.
4. T. P. Le, L. Donati, S. Severini and F. Caruso, *How to suppress dark states in quantum networks and bio-engineered structures*, arXiv:1707.07482 (2017), https://arxiv.org/abs/1707.07482.
