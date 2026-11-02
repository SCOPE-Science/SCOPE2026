# Half-filling exceptional-point cascade and exact no-jump survival on lossy Johnson graphs

## Finding

For each pair of integers \(k\ge2\), \(n\ge2k\), consider \(k\) hard-core bosons hopping uniformly between the \(n\) sites of a complete graph, with a monitored loss channel on one distinguished site. In the fixed-particle-number sector the no-jump Hamiltonian is
\[
H_{n,k}(J,\gamma)=J A(J(n,k))-i\gamma P_\star,
\qquad J>0,\quad\gamma>0,
\]
where \(P_\star\) projects onto occupation configurations containing the monitored site. The corresponding first-jump rate is \(2\gamma\) times the monitored-site occupation.

Put \(h_j=\binom{n-1}{j}-\binom{n-1}{j-1}\), with \(\binom{n-1}{-1}=0\), and for \(0\le j<k\) define
\[
 a_j=(k-1-j)(n-k-j)-j,\quad
 c_j=(k-j)(n-k-1-j)-j,\quad
 b_j=\sqrt{(k-j)(n-k-j)}.
\]
The **complete complex spectrum, including Jordan structure**, is that of the orthogonal direct sum of \(h_j\) identical two-dimensional blocks
\[
 M_j=\begin{pmatrix}Ja_j-i\gamma&Jb_j\\Jb_j&Jc_j\end{pmatrix}
 \qquad(0\le j<k)
\]
and \(h_k\) one-dimensional blocks with real eigenvalue \(-Jk\). Here \(h_k\ge0\), and this last block family is absent precisely at half filling \(n=2k\). Thus the eigenvalues of each two-dimensional block are
\[
 E_{j,\pm}=\frac{J(a_j+c_j)-i\gamma}{2}
 \pm\frac12\sqrt{J^2(n-2j)^2-\gamma^2+2iJ\gamma(n-2k)}.
\]

**Exceptional-point classification.** For positive real loss \(\gamma\), the Hamiltonian is defective if and only if \(n=2k\) and
\[
 \gamma\in\{2J,4J,\ldots,2kJ\}.
\]
At \(\gamma=2J(k-j)\), exactly \(h_j\) size-two Jordan blocks occur, all at energy \(J(a_j+c_j)/2-i\gamma/2\); there are no larger Jordan blocks. Away from half filling the positive-loss family has no exceptional point, despite having \(h_k\) exact dark eigenvectors.

The full finite-time first-jump survival probability from the maximally mixed state \(I/\binom nk\) also has a closed form. Write
\[
\delta_j=\frac{-J(n-2k)-i\gamma}{2},\qquad
\omega_j^2=\delta_j^2+J^2b_j^2,
\]
and interpret \(\sin(\omega_j t)/\omega_j=t\) when \(\omega_j=0\). Then, for all \(t\ge0\),
\[
\boxed{\displaystyle
 S_{n,k}(t)=\frac{h_k+\sum_{j=0}^{k-1}h_j F_j(t)}{\binom nk},\qquad
 F_j(t)=2e^{-\gamma t}\left(
 |\cos(\omega_jt)|^2+(|\delta_j|^2+J^2b_j^2)
 \left|\frac{\sin(\omega_jt)}{\omega_j}\right|^2
 \right).}
\]
At the exceptional point of block \(j\), its contribution specializes to
\[
 F_j(t)=e^{-2J(k-j)t}\bigl(2+4J^2(k-j)^2t^2\bigr).
\]
The infinite-time limit recovers the previously established dark-space fraction \(h_k/\binom nk=1-2k/n\); that dark-space count and its capture corollary are prior work, not part of the asserted addition.

## Assumptions and scope

All graphs are unweighted Johnson graphs \(J(n,k)\), whose vertices are \(k\)-subsets of \(\{0,1,\ldots,n-1\}\), adjacent when their symmetric difference has size two. The sign convention is adjacency hopping \(+J A\), with \(J>0\), and loss \(-i\gamma P_\star\), with \(\gamma>0\). The monitored site is any fixed physical site; permutation symmetry makes its choice immaterial. A first loss jump exits the chosen particle-number sector. The survival formula concerns the unconditioned maximally mixed initial density matrix within that sector, with no other dephasing, disorder or interaction besides hard-core exclusion. Its normalization is the physical no-first-jump probability, not the norm of a single specially chosen vector.

## Proof

**1. Boolean-level factorization.** Let \(N=n-1\), let \(V_r\) denote the complex vector space on the \(r\)-subsets of the \(N\) unmarked sites, and define the up and down incidence maps \(U_r:V_r\to V_{r+1}\) and \(D_{r+1}=U_r^*\). Direct counting gives
\[
D_{r+1}U_r-U_{r-1}D_r=(N-2r)I,
\qquad A(J(N,r))=U_{r-1}D_r-rI.
\]
For \(r<N/2\), the first identity and positivity of \(U_{r-1}D_r\) show \(U_r\) injective. The harmonic space \(\mathcal H_j=\ker D_j\), with \(\mathcal H_0=V_0\), therefore has dimension \(h_j\) for \(j\le k-1\), and the orthogonal harmonic strings \(U_{r-1}\cdots U_j\mathcal H_j\) exhaust \(V_r\) for \(r\le k-1\). The intertwining relation
\[
 A(J(N,r+1))U_r=U_r A(J(N,r))+(N-2r-1)U_r
\]
shows that the \(j\)-string in level \(r\) has eigenvalue \((r-j)(N-r-j)-j\).

**2. Invariant two-level sectors.** Split the Johnson configurations according to whether the monitored site is occupied. The two spaces are \(V_{k-1}\) and \(V_k\), and their joint adjacency operator has the block form
\[
 A(J(n,k))=
 \begin{pmatrix} A(J(N,k-1))&D_k\\U_{k-1}&A(J(N,k))\end{pmatrix}.
\]
For a normalized vector in the \(j\)-string of \(V_{k-1}\),
\[
 \|U_{k-1}v\|^2
 =\langle v,D_kU_{k-1}v\rangle
 =(k-j)(n-k-j)\|v\|^2=b_j^2\|v\|^2.
\]
The image vector normalized by \(b_j\) belongs to the \(j\)-string of \(V_k\). In these paired bases the restrictions of adjacency, and of the loss projector, are exactly the stated blocks \(M_j\). The orthogonal complement of \(\operatorname{im}U_{k-1}\) in \(V_k\) is \(\ker D_k\), with dimension \(h_k\). On this complement \(A(J(N,k))=U_{k-1}D_k-kI=-kI\), while \(P_\star=0\). This proves the full decomposition, including the dark block count. No unverified asymptotic or numerical rank extrapolation is used.

**3. Exceptional points.** The square of the block discriminant is
\[
 \Delta_j=J^2(n-2j)^2-\gamma^2+2iJ\gamma(n-2k).
\]
For \(n>2k\), its imaginary part is strictly positive, so every two-dimensional block has distinct eigenvalues. If \(n=2k\), it vanishes exactly at \(\gamma=J(n-2j)=2J(k-j)\). Since \(b_j>0\), the coalesced block is non-scalar and has a single eigenvector, hence one size-two Jordan block per copy. Different \(j\)'s have different positive critical losses, and all other blocks remain diagonalizable. Direct sums cannot generate a larger Jordan block. This proves the complete defective-spectrum classification.

**4. Exact time dependence.** Subtract the scalar \(\mu_j=[J(a_j+c_j)-i\gamma]/2\) from \(M_j\). The remainder \(W_j\) is traceless and satisfies \(W_j^2=\omega_j^2I\). Therefore
\[
 e^{-iM_jt}=e^{-i\mu_jt}
 \left(\cos(\omega_jt)I-i\frac{\sin(\omega_jt)}{\omega_j}W_j\right).
\]
Taking the squared Frobenius norm removes the cross term because \(\operatorname{tr}W_j=0\) and gives exactly \(F_j(t)\). Summing these norms with harmonic multiplicities, plus the unit-norm dark blocks, and dividing by \(\binom nk\) proves \(S_{n,k}(t)\). For every bright block, an eigenvector cannot have zero amplitude on the lossy coordinate because \(b_j>0\). The imaginary part of every bright eigenvalue is therefore negative, and the bright contribution tends to zero, including at Jordan points. At a Jordan point \(\omega_j=0\), the exponential series produces the displayed quadratic-polynomial factor. This completes the proof.

## Verification

The standalone `verify.py` reconstructs all Johnson adjacency and occupation-loss matrices directly from subsets; it compares the predicted complex eigenvalues to independent dense diagonalizations; it compares the closed survival formula with matrix exponentials; it checks six symbolic characteristic-polynomial factorizations; and it checks exact Jordan nullities and algebraic multiplicities at five exceptional points. Successful replay reports `VERIFY_OK checks=121`. These finite calculations corroborate, but are not substitutes for, the all-parameter incidence proof above. Example: for \(n=6\), \(k=3\), the exceptional rates are \(2J,4J,6J\), with respective numbers \(5,4,1\) of size-two Jordan blocks; for \(n=7\), \(k=3\), there are five dark dimensions and no exceptional point for any positive loss.

## Relationship to prior work

The continuous-time Johnson-graph walk and its search-oriented marked-*vertex* Hamiltonian are treated by Wong (2016), but marking one graph vertex is not the occupation-*star* loss projector studied here, and the former is Hermitian. The general dark-state/loss framework is established by Le, Donati, Severini and Caruso (2017 preprint), without this finite-particle-number Jordan classification. Tschernig et al. (2022) establish multi-photon branching exceptional points in lossy linear-optical mode networks, but their unrestricted bosonic Fock spaces and waveguide geometries are distinct from the hard-core complete-graph occupation problem. A prior exact result for the same hard-core model already fixes the infinite-time capture probability and dark-space dimension; this work does not claim them again. Its added result is the complete positive-loss non-Hermitian spectral/Jordan classification and the all-time maximally mixed first-jump survival function.

## Limitations

Uniform hopping and a uniform single-site occupation loss are essential to the stated two-dimensional reduction and exceptional-point locations. No robustness to interactions beyond hard-core exclusion, bond disorder, additional sinks, dephasing, other particle statistics, or arbitrary initial-state ensembles is claimed. These are exceptional points of the effective no-jump Hamiltonian, not automatically exceptional points of the full particle-number-changing Lindblad superoperator. Earlier specialist literature not identified by the documented searches may affect historical priority.

## References

- T. G. Wong, *Quantum Walk Search on Johnson Graphs*, arXiv:1601.04212 (initial public posting 2016-01-16), https://arxiv.org/abs/1601.04212.
- T. P. Le, L. Donati, S. Severini and F. Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482 (initial posting 2017-07-24), https://arxiv.org/abs/1707.07482.
- K. Tschernig et al., *Branching High-Order Exceptional Points in Non-Hermitian Optical Systems*, Laser & Photonics Reviews 16, 2100707 (2022), https://doi.org/10.1002/lpor.202100707.
- A. Cerjan and S. Fan, *Eigenvalue Dynamics in the Presence of Nonuniform Gain and Loss*, Physical Review A 94, 033857 (2016), https://doi.org/10.1103/PhysRevA.94.033857.
