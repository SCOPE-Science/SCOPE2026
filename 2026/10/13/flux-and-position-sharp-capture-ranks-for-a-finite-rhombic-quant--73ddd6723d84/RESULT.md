# Flux- and position-sharp capture ranks for a finite rhombic quantum chain

## Finding

For every integer \(N\ge2\) and upper-rim detector position \(1\le j\le N\), the rank of the detector-visible subspace in the uniformly magnetized finite open diamond (rhombic) chain is exactly

\[
R_{N,j}(\phi)=
\begin{cases}
2N+3,&\phi\not\equiv0,\pi\pmod{2\pi},\\
2N-2\gcd(j,N+1)+3,&\phi\equiv0\pmod{2\pi},\\
5,&\phi\equiv\pi\pmod{2\pi},\quad j\in\{1,N\},\\
3,&\phi\equiv\pi\pmod{2\pi},\quad1<j<N.
\end{cases}
\]

If the initial condition is the maximally mixed one-particle density operator, the exact eventual probability of absorption at the selected upper-rim vertex is

\[
P_{N,j}(\phi)=\frac{R_{N,j}(\phi)}{3N+1}.
\]

The formula is independent of the strictly positive absorption rate. It provides three distinct phenomena in a single natural family: the generic-flux bright dimension is independent of detector placement; at zero flux it depends on a greatest common divisor of the detector position and the number of hub vertices; at half flux Aharonov–Bohm caging reduces the bright dimension to three for an interior rim trap or five for an end rim trap.

## Assumptions and scope

The Hilbert space is \(\mathbb C^{3N+1}\) with orthonormal basis \(\{|a_0\rangle,\ldots,|a_N\rangle,|u_1\rangle,|d_1\rangle,\ldots,|u_N\rangle,|d_N\rangle\}\). Every cell \(j\) has upper/lower rim vertices \(u_j,d_j\) joined to both hubs \(a_{j-1}\) and \(a_j\). All hopping magnitudes are one. In the bipartite order (hubs, rim sites), define

\[
H_\phi=\begin{pmatrix}0&B_\phi^*\\B_\phi&0\end{pmatrix},
\qquad
\begin{aligned}
(B_\phi)_{u_j,a_{j-1}}&=1,&(B_\phi)_{u_j,a_j}&=e^{i\phi},\\
(B_\phi)_{d_j,a_{j-1}}&=1,&(B_\phi)_{d_j,a_j}&=1,
\end{aligned}
\]

and every other entry zero. The gauge-invariant plaquette flux is \(\phi\) modulo \(2\pi\). Here \(\phi\) is real and no onsite disorder is present. For the detector \(s=u_j\), put \(P_s=|s\rangle\langle s|\) and \(K=H_\phi-i\gamma P_s\), with \(\gamma>0\). Conditional propagation is \(e^{-iKt}\) for \(t\ge0\); the probability of not yet being absorbed from an initial density matrix \(\rho\) is \(\operatorname{Tr}(e^{-iKt}\rho e^{iK^*t})\). Define the detector-visible subspace

\[
\mathcal B=\operatorname{span}\{H_\phi^k|s\rangle:0\le k\le3N\},
\]

and its orthogonal projection \(\Pi_{\mathcal B}\). The stated conclusions are exact for all finite \(N\ge2\) and positive detector rates; no claim of rate-uniform finite-time convergence is made.

## Proof

**1. Absorption is controlled by the visible spectral support.** Since \(H_\phi\) is Hermitian, \(\mathcal B\) and \(\mathcal B^\perp\) reduce \(H_\phi\). The detector projection vanishes on \(\mathcal B^\perp\), so the conditional dynamics is unitary there. On \(\mathcal B\), \(K\) has no eigenvalue with zero imaginary part: if \(Kv=\lambda v\) and \(\operatorname{Im}\lambda=0\), then taking imaginary parts of \(\langle v,Kv\rangle\) gives \(\langle s|v\rangle=0\); hence \(H_\phi v=\lambda v\), and \(\langle s|H_\phi^k v\rangle=\lambda^k\langle s|v\rangle=0\) for all \(k\), contrary to nonzero \(v\in\mathcal B\). Consequently every eigenvalue of the restriction of \(K\) to \(\mathcal B\) has strictly negative imaginary part and the conditional propagator decays exponentially on that finite-dimensional space (allowing polynomial Jordan factors). Therefore

\[
\lim_{t\to\infty}\operatorname{Tr}(e^{-iKt}\rho e^{iK^*t})
=\operatorname{Tr}((I-\Pi_{\mathcal B})\rho),
\]

and the capture probability equals \(\operatorname{Tr}(\Pi_{\mathcal B}\rho)\). In particular, for \(\rho=I/(3N+1)\), it is \(\dim\mathcal B/(3N+1)\). This spectral-support principle is classical; the work below is the explicit evaluation for the finite magnetic rhombic family.

**2. The hub Gram matrix.** Write \(T_\phi=B_\phi^*B_\phi\). In the basis \(a_0,\ldots,a_N\), \(T_\phi\) is Hermitian tridiagonal: its endpoint diagonal entries are \(2\), all its interior diagonal entries are \(4\), and its superdiagonal entries are \(1+e^{i\phi}\), with conjugate subdiagonal entries. For any positive eigenvalue \(\mu\) of \(T_\phi\), each corresponding unit hub eigenvector \(x\) supplies eigenvectors of \(H_\phi\) at \(\pm\sqrt\mu\) with rim components proportional to \(B_\phi x\). The upper-detector overlap in that spectral pair is nonzero exactly when

\[
(B_\phi x)_{u_j}=x_{j-1}+e^{i\phi}x_j\ne0.
\]

An individual spectral eigenvalue contributes precisely one dimension to \(\mathcal B\) whenever the detector has nonzero projection onto its eigenspace, irrespective of its multiplicity. The zero-energy eigenspace likewise contributes either one or zero visible dimensions.

**3. Exactly one visible zero energy for every flux.** For \(\phi\not\equiv0\pmod{2\pi}\), \(B_\phi\) has full column rank: the two row equations in any cell of \(B_\phi x=0\) give \(x_{j-1}+x_j=x_{j-1}+e^{i\phi}x_j=0\), hence both adjacent components vanish, and all hubs vanish. When \(\phi=0\), the nullspace of \(B_0\) is one-dimensional, generated by the alternating hub vector, which has no rim component. In both cases the detector \(|u_j\rangle\) has nonzero projection onto \(\ker H_\phi\). Indeed, if its rim coordinate vector were in \(\operatorname{im}B_\phi\), there would be \(x\) with \(B_\phi x=e_{u_j}\). At \(\phi=0\), both rows of each cell of \(B_0x\) agree, immediately contradicting a single nonzero upper coordinate. At \(\phi\ne0\), the two zero equations in every non-target cell force both adjacent hub components to vanish. Together these zero cells cover every hub except possibly the left endpoint when \(j=1\) or the right endpoint when \(j=N\); the target lower-row condition \(x_{j-1}+x_j=0\) then forces the remaining endpoint to vanish as well. The target upper coordinate cannot be nonzero, a contradiction. Thus the zero-energy projection of \(|u_j\rangle\) is nonzero. This gives exactly one zero-energy dimension in \(\mathcal B\) for all fluxes.

**4. Generic flux.** Suppose \(\phi\not\equiv0,\pi\pmod{2\pi}\). The nonzero offdiagonal entries make \(T_\phi\) an irreducible Hermitian Jacobi matrix; it has exactly \(N+1\) simple positive eigenvalues, since \(B_\phi\) is injective. Gauge an eigenvector as \(x_\ell=e^{-i\ell\phi/2}y_\ell\); then the \(y_\ell\) can be chosen real because the gauged tridiagonal matrix is real symmetric. Adjacent components of a nonzero Jacobi eigenvector cannot both vanish (a zero pair propagates in both directions by the recurrence). But

\[
(B_\phi x)_{u_j}=e^{-i(j-1)\phi/2}
\big(y_{j-1}+e^{i\phi/2}y_j\big).
\]

For \(\phi\not\equiv0\pmod{2\pi}\), the expression in parentheses can vanish for real \(y_{j-1},y_j\) only if both vanish, since \(\sin(\phi/2)\ne0\). This is impossible. Every one of the \(N+1\) positive singular-value modes is detector-visible at both signs. With the one visible zero energy, the result is \(2(N+1)+1=2N+3\).

**5. Zero flux and the gcd law.** For \(\phi=0\), the hub matrix is the twice-weighted signless path Laplacian. Its eigenvalues are simple, given by \(\mu_k=4-4\cos(k\pi/(N+1))\) for \(k=0,\ldots,N\). The zero mode has hub profile \(x_\ell=(-1)^\ell\) and no rim overlap. For each \(1\le k\le N\), a real eigenvector has components

\[
x_\ell=(-1)^\ell\cos\!\left(\frac{(\ell+1/2)k\pi}{N+1}\right).
\]

Using the cosine difference identity, the detector overlap on the corresponding positive singular-energy pair is, up to a nonzero scalar,

\[
(B_0x)_{u_j}=(-1)^{j-1}2
\sin\!\left(\frac{jk\pi}{N+1}\right)
\sin\!\left(\frac{k\pi}{2(N+1)}\right).
\]

For \(1\le k\le N\), the last sine is nonzero. The overlap therefore vanishes exactly when \(N+1\mid jk\). Among \(k=1,\ldots,N\), precisely \(\gcd(j,N+1)-1\) satisfy this divisibility. Hence the number of visible strictly positive singular-energy pairs is \(N-\gcd(j,N+1)+1\). Including both signs and one visible zero gives \(2N-2\gcd(j,N+1)+3\).

**6. Half flux and caging.** If \(\phi=\pi\) modulo \(2\pi\), then \(1+e^{i\phi}=0\) and \(T_\pi\) is diagonal, with value \(2\) at hubs \(a_0,a_N\) and value \(4\) at hubs \(a_1,\ldots,a_{N-1}\). The detector upper row couples exactly the two adjacent hub basis vectors \(a_{j-1}\) and \(a_j\), with nonzero coefficients of opposite signs. If \(j=1\) or \(j=N\), those two hubs belong to different eigenvalues of \(T_\pi\), so the detector sees both pairs \(\pm\sqrt2\) and \(\pm2\). Otherwise they belong to the same eigenvalue \(4\), so the detector sees only the pair \(\pm2\). Adding the unique visible zero gives \(5\) at the ends, \(3\) in the interior. This exhausts the spectrum and completes the proof. \(\square\)

## Verification

The reproducible file `verify.py` constructs the Hamiltonian from the explicit matrix elements and independently checks both the Krylov dimension and the detector-visible eigenspace count for every site and all tested chain lengths \(2\le N\le8\), at phases \(0\), \(\pi/7\), \(\pi/2\), and \(\pi\). The same file independently exponentiates the lossy finite-dimensional Hamiltonian at three illustrative cases and compares the long-time mixed-state survival with the predicted dark-space fraction. It requires the versions of NumPy and SciPy specified in `requirements.txt`. The tested computations are corroboration only: the exact all-length/all-flux theorem follows from the analytic steps above.

## Relationship to prior work

Aharonov–Bohm caging at half flux is a classical phenomenon of destructive interference; see Vidal, Mosseri and Douçot (1998), and the later rhombic photonic-lattice demonstration by Mukherjee and collaborators (2018). The latter explicitly identifies the bulk spectral energies \(0,\pm2\) and the open-boundary end energies \(\pm\sqrt2\) in the caging limit. These spectral facts are not claimed as new here. Novo and collaborators (2015) established the general relation between quantum trapping efficiency and the trap-visible invariant/Krylov subspace, also not claimed as new. The present classification evaluates that invariant for every finite open rhombic chain, every upper-rim detector position, and every magnetic flux, including the exact zero-flux gcd law and the flux-dependent rank discontinuities. These results are not stated in the inspected primary texts. This is a literature comparison, not an assertion that no equivalent specialized or broader result can exist elsewhere.

## Limitations

The theorem treats single-particle ideal coherent hopping with fixed uniform plaquette flux and one strictly absorbing upper-rim vertex. It does not address multiple detectors, finite-time optimal detection rates, disorder, higher-body interactions, or nonuniform flux. Although the infinite-time absorption probability is discontinuous at special fluxes, finite-time dynamics is continuous in flux at any fixed time: the convergence rate is not uniform as flux approaches a degeneracy. Numerical checks cover finitely many lengths and do not independently establish the all-length proof. Independent literature-priority review remains outstanding.

## References

1. J. Vidal, R. Mosseri and B. Douçot, “Aharonov–Bohm cages in two-dimensional structures,” *Physical Review Letters* **81**, 5888 (1998). First public preprint 1998-06-05, arXiv:cond-mat/9806068; https://arxiv.org/abs/cond-mat/9806068.
2. L. Novo, S. Chakraborty, M. Mohseni, H. Neven and Y. Omar, “Systematic dimensionality reduction for quantum walks: optimal spatial search and transport on non-regular graphs,” *Scientific Reports* **5**, 13304 (2015). arXiv:1412.7209; https://www.nature.com/articles/srep13304.
3. S. Mukherjee and collaborators, “Experimental observation of Aharonov–Bohm cages in photonic lattices,” *Physical Review Letters* **121**, 075502 (2018). arXiv:1805.03564; https://ar5iv.labs.arxiv.org/html/1805.03564.
4. L. Jin, “Flat band induced by the interplay of synthetic magnetic flux and non-Hermiticity,” *Physical Review A* **99**, 033810 (2019), doi:10.1103/PhysRevA.99.033810. A different, parity–time-symmetric non-Hermitian lattice is studied.
