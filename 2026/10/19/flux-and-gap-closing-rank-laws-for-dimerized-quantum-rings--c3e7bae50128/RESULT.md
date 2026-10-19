# Flux and gap-closing rank laws for dimerized quantum rings

## Finding
For every integer \(m\ge2\), positive hopping magnitudes \(a,b>0\), and real flux \(\phi\), a periodic two-sublattice (Su–Schrieffer–Heeger) ring has exactly the following long-time quantum average-mixing rank:

\[
\operatorname{rank}\widehat M_{m,a,b,\phi}=
\begin{cases}
1,&\phi\not\equiv0,\pi\pmod{2\pi},\\
m,&\phi\equiv0,\ m\text{ odd},\\
m-1+\mathbf1_{\{a=b\}},&\phi\equiv0,\ m\text{ even},\\
m+\mathbf1_{\{a=b\}},&\phi\equiv\pi,\ m\text{ odd},\\
m+1,&\phi\equiv\pi,\ m\text{ even}.
\end{cases}
\]

In particular, generic non-time-reversal-invariant flux yields the completely uniform matrix \(\widehat M=\mathbf1\mathbf1^{\mathsf T}/(2m)\), even if \(a\ne b\). At the two time-reversal-invariant fluxes, arithmetic momentum pairing restores positive-semidefinite Fourier modes; band-gap closing at \(a=b\) adds one additional sublattice-staggered mode precisely when the discrete Bloch momentum \(\pi\) occurs.

## Assumptions and scope
Let \(\{|A_j\rangle,|B_j\rangle:j\in\mathbb Z/m\mathbb Z\}\) be the orthonormal vertex basis and define the Hermitian, zero-diagonal Hamiltonian
\[
H_{m,a,b,\phi}=\sum_{j=0}^{m-1}\bigl(a|A_j\rangle\langle B_j|+b e^{i\phi/m}|A_{j+1}\rangle\langle B_j|+\mathrm{h.c.}\bigr).
\]
The two bonds meeting each site are distinct for \(m\ge2\). The flux \(\phi\) is defined modulo \(2\pi\) up to diagonal unitary gauge, and \(a,b\) are strictly positive. No site energies, extra hoppings, dissipation or discrete-time coin are assumed. The matrix under study has entries
\[
\widehat M_{uv}=\lim_{T\to\infty}\frac1T\int_0^T|\langle u|e^{-itH_{m,a,b,\phi}}|v\rangle|^2\,dt.
\]
The result concerns the rank of this \(2m\times2m\) matrix, not instantaneous mixing or a finite observation window. For a complex Hermitian Hamiltonian, if \(H=\sum_E E P_E\) is its decomposition over **distinct** eigenvalues, then \(\widehat M=\sum_E P_E\circ\overline{P_E}\), a real symmetric positive-semidefinite matrix.

## Proof
**1. Bloch spectrum.** Put \(\omega=e^{2\pi i/m}\) and \(\theta_j=(\phi+2\pi j)/m\). The cell Fourier basis with factor \(\omega^{-jx}\) reduces \(H\) to the matrices
\[
h_j=\begin{pmatrix}0&z_j\\\overline{z_j}&0\end{pmatrix},\qquad z_j=a+b e^{i\theta_j},\qquad r_j=|z_j|.
\]
When \(r_j>0\), the eigenvalues are \(\pm r_j\), and normalized eigenvectors are
\[
\psi_{\sigma,j}(A_x)=\frac{\omega^{-jx}}{\sqrt{2m}},\qquad
\psi_{\sigma,j}(B_x)=\frac{\sigma\overline{q_j}\,\omega^{-jx}}{\sqrt{2m}},\quad q_j=z_j/r_j,\quad \sigma\in\{-1,1\}.
\]
They have constant vertex intensity \(1/(2m)\). Two distinct positive \(r_j\) coincide exactly if \(\cos\theta_j=\cos\theta_k\). For \(j\ne k\), this requires \(\theta_j\equiv-\theta_k\pmod{2\pi}\), hence \(\phi\equiv0\) or \(\pi\pmod{2\pi}\). Vanishing \(z_j\) requires \(a=b\) and \(\theta_j\equiv\pi\). Therefore away from the two exceptional fluxes all \(2m\) energies are distinct and every eigenprojector contributes the uniform matrix \(\mathbf1\mathbf1^{\mathsf T}/(4m^2)\). Their sum is \(\mathbf1\mathbf1^{\mathsf T}/(2m)\), of rank one.

**2. Positive collision blocks.** Reduce \(\phi\) to \(0\) or \(\pi\), and initially suppose every \(r_j>0\). The involution pairing coincident positive energies is \(j\mapsto-j\) at zero flux and \(j\mapsto-1-j\) at flux \(\pi\). Each nonfixed pair \(\{j,k\}\) has two separate doubled levels \(\pm r_j\). Relative to treating all Bloch eigenstates as simple, its correction to \(\widehat M\), indexed by cells \(x,y\) and sublattices \(s,t\), is
\[
\Delta_{(s,x),(t,y)}=\frac1{m^2}\operatorname{Re}\!\left(\omega^{-(j-k)(x-y)}v_s\overline{v_t}\right),\qquad
v=(1,\overline{q_j}q_k).
\]
This follows by expanding the absolute square of the sum of the two rank-one spectral projectors at each sign: cross terms \(P_j\circ\overline{P_k}+P_k\circ\overline{P_j}\) survive precisely because the energies coincide. In the discrete cell Fourier decomposition, \(\Delta\) contributes a positive rank-one matrix proportional to \(vv^*\) at cell frequency \(\ell=j-k\), and its conjugate at frequency \(-\ell\). At a self-conjugate frequency \(\ell=-\ell\) modulo \(m\), the single block contains their sum, proportional to \(vv^*+\overline v v^{\mathsf T}\). The initial uniform contribution occupies only frequency zero and has rank one.

**3. Frequency arithmetic, odd \(m\).** At zero flux each pair has \(j+k\equiv0\pmod m\), so \(\ell\equiv2j\pmod m\); at flux \(\pi\), each pair has \(j+k\equiv-1\pmod m\), so \(\ell\equiv2j+1\pmod m\). Since multiplication by two is invertible modulo odd \(m\), exactly one ordered pairing contributes at each nonzero frequency. It contributes rank one, including its conjugate frequency viewed separately. Thus the total rank is \(1+(m-1)=m\) whenever no Bloch level vanishes.

**4. Frequency arithmetic, even \(m\).** For \(\phi=0\) only nonzero even frequencies occur, while for \(\phi=\pi\) only odd frequencies occur. There are respectively \(m/2-1\) and \(m/2\) such frequencies. Every activated nonzero Fourier block has rank two. Indeed, away from a self-conjugate frequency, the two distinct unordered collision pairs contributing to the same frequency are represented by Bloch angles \(\theta\) and \(\theta+\pi\), with complex amplitudes \(z=a+b e^{i\theta}\) and \(z'=a-b e^{i\theta}\). Their rank-one sublattice vectors would be parallel only if their squared phase ratios agreed, forcing \(z/z'\) to be real. But
\[
\operatorname{Im}(z\overline{z'})=2ab\sin\theta\ne0.
\]
The possible \(\sin\theta=0\) cases are fixed Bloch points and yield frequency zero, not the nonzero blocks in question. At a self-conjugate frequency \(\ell=m/2\), there is one unordered pair, with angles \(\pi/2\) and \(3\pi/2\). Its sublattice vector \(v=(1,\overline q^{\,2})\) has a non-real second coordinate, because \(z=a\pm ib\) with \(a,b>0\). Hence \(v\) and \(\overline v\) are linearly independent and the block again has rank two. Summing the frequency-zero rank one gives \(m-1\) at zero flux and \(m+1\) at flux \(\pi\), before accounting for possible band closing.

**5. Zero-energy boundary.** A vanishing \(z_j\) is possible only if \(a=b\) and the allowed Bloch set includes \(\theta_j=\pi\). This is precisely \(\phi=0\) with even \(m\), or \(\phi=\pi\) with odd \(m\). There the zero-energy eigenspace consists of the two separate Fourier vectors on the \(A\)- and \(B\)-sublattices. Its rank-two projector is not the sum of two projectors at distinct energies. Relative to the nondegenerate uniform baseline, its Schur square contributes the extra matrix
\[
\frac1{2m^2}ss^{\mathsf T},\qquad s(A_j)=1,\quad s(B_j)=-1.
\]
This is a positive rank-one contribution entirely in the cell-frequency-zero sublattice-antisymmetric direction, orthogonal to the all-ones direction. All other collision blocks are at nonzero frequencies and remain unchanged. The rank therefore rises by exactly one in the two stated boundary cases. Combining steps 1–5 proves the classification for every admitted parameter.

## Verification
A standalone finite-dimensional checker, `verify.py`, constructs the Hermitian Hamiltonian directly and independently computes its spectral projectors with `numpy.linalg.eigh`; it then reconstructs all Bloch eigenvectors from the analytic two-band formula and compares the two average-mixing matrices entrywise. It additionally tests the rank law, nonnegative spectrum, row sums, and generic-flux uniformity. The replay covered \(m=2,\ldots,11\), five positive hopping pairs and five flux choices, giving 250 profiles and 50,500 matrix entries, with maximum entrywise discrepancy \(7.772\times10^{-16}\). Its output was `VERIFY_OK spectral_profiles= 250 matrix_entries= 50500 orders=2..11 max_entry_discrepancy= 7.772e-16`. The finite tests are corroboration, not an infinite proof; the unrestricted conclusion follows from the Fourier and collision-block argument above. Execute `python verify.py` with NumPy installed.

## Relationship to prior work
The infinite-time spectral-projector formula and its quantum-walk interpretation are standard, and are treated in Coutinho et al., *Irrational quantum walks* (arXiv:2208.08971), especially its introduction and Section 2. The undimerized-cycle average-mixing behavior is part of earlier work by Adamczak et al. (arXiv:0708.2096) and the ordinary cycle literature. Roy, Ganguly and Maiti (2023) consider flux-threaded dimerized SSH rings with additional Aubry–André–Harper site modulation, using the tight-binding Hamiltonian to study spectral bands, persistent currents and inverse participation ratios. Their paper supplies a near-identical physical ring construction but does not calculate the full long-time average-mixing matrix or the five-regime rank law here. Levine et al. (2026) prove that simple-spectrum cyclic circulants have uniform average mixing (their Section 5, Theorem 5). The simple-spectrum part here follows the same flat-projector mechanism; the two-sublattice Hamiltonian is generally not a one-site circulant when \(a\ne b\). That result does not cover the parity-sensitive degeneracies or the gap-closing rank jumps. The displayed classification concerns the **joint** effects of parity, exceptional flux, and the gap-closing surface, which are not supplied by the general spectral formula alone. The result is not claimed to classify disorder-modulated rings or arbitrary magnetic cycles.

## Limitations
The theorem requires a clean, exactly periodic, two-site unit cell, equal site energies, only nearest-neighbor hoppings and strictly positive \(a,b\). The rank is an infinite-time Cesàro invariant; observation at finite time near \(0\) or \(\pi\) flux can show very long crossovers not quantified here. Spectral and physical connections to earlier work are documented, but no exhaustive priority search can exclude an unlocated stronger Floquet/Bloch or quantum-mixing theorem. Independent expert verification has not been performed.

## References
1. G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier and R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first public 2022-08-18), https://arxiv.org/html/2208.08971v1.
2. W. Adamczak et al., *Non-uniform mixing of quantum walk on cycles*, arXiv:0708.2096 (2007), https://arxiv.org/abs/0708.2096.
3. S. Roy, S. Ganguly and S. K. Maiti, *Interplay between hopping dimerization and quasi-periodicity on flux-driven circular current in an incommensurate Su–Schrieffer–Heeger ring*, Scientific Reports 13 (2023), article 4093, https://www.nature.com/articles/s41598-023-31354-9.
4. X.-P. Xu, *Continuous-time quantum walks on one-dimensional regular networks*, Physical Review E 77 (2008), 061127, https://doi.org/10.1103/PhysRevE.77.061127.
5. L. Levine et al., *Uniform Mixing in Chiral Quantum Walks*, arXiv:2605.04414v2 (2026), Section 5, https://arxiv.org/html/2605.04414v2.
