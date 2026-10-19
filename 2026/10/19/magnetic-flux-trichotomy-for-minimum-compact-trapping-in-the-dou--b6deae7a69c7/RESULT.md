# Magnetic-flux trichotomy for minimum compact trapping in the doubly decorated square lattice

## Finding
For the precisely specified Hermitian tight-binding operator below, fix either sign \(s\in\{-1,+1\}\). The smallest site support of a nonzero **finitely supported** eigenstate with energy \(s t\) has size
\[
N_{\min}(\phi)=\begin{cases}
8,&e^{i\phi}=1,\\
12,&e^{i\phi}=-1,\\
14,&e^{i\phi}\notin\{1,-1\}.
\end{cases}
\]
The result is valid without restricting flux to a rational multiple of \(2\pi\), and it holds for both flat-band energies separately. Each constructed support is shared by states at both energies; nontrivial linear superpositions therefore remain confined to that support while beating at angular frequency \(2t\).

## Assumptions and scope
Start with the infinite square graph \(\mathbb Z^2\). Orient each edge positively along a coordinate direction. Replace every oriented edge \(u\to v\) by three bonds \(u-a_e-b_e-v\), placing two new physical sites in the edge interior. The Hamiltonian has zero onsite entries and the following nonzero matrix entries, together with their complex conjugate transposes:
\[
H_{u,a_e}=t,\qquad H_{a_e,b_e}=t,\qquad H_{v,b_e}=t e^{i\theta_e},\qquad t>0.
\]
For a horizontal edge, \(\theta_e=0\). For a vertical edge with initial vertex \((x,y)\), put \(\theta_e=x\phi\). The magnetic holonomy around each positive elementary square is \(e^{i\phi}\). Here "occupied" means a nonzero complex amplitude at a *physical site*, not a nonzero original edge or a support-containing unit cell. All eigenstates under consideration are finitely supported, and no boundary or finite-torus twist is imposed.

## Proof
**1. Hub exclusion at either flat-band energy.** Partition sites into original vertices (hubs) and edge-interior dimers, and write the Hamiltonian as \(H=\bigl(\begin{smallmatrix}0&T\\T^*&D\end{smallmatrix}\bigr)\). Each block of \(D\) equals \(t\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)\), so its eigenvalues are \(\pm t\). The four internal neighbors of a hub are all distinct, giving \(TT^*=4t^2I\). If \(H(h,z)=\lambda(h,z)\), where \(\lambda=s t\), project the second block equation \((\lambda-D)z=T^*h\) onto the \(\lambda\)-eigenspace of \(D\); its right-hand side has zero such component. Hence
\[
z=\frac{1}{2\lambda}T^*h+z_\lambda,\qquad Dz_\lambda=\lambda z_\lambda,\qquad z_\lambda\perp T^*h.
\]
Take the inner product of the first block equation \(Tz=\lambda h\) with \(h\):
\[
\lambda\lVert h\rVert^2=\frac{1}{2\lambda}\lVert T^*h\rVert^2=2\lambda\lVert h\rVert^2.
\]
Since \(\lambda\ne0\), \(h=0\). On each edge interior, the two amplitudes must therefore be \((x_e,sx_e)\). Thus every occupied original edge contributes *exactly two* occupied physical sites.

**2. Magnetic incidence constraints.** The remaining equations are
\[
\sum_{e:\,\mathrm{tail}(e)=v}x_e+\sum_{e:\,\mathrm{head}(e)=v}s e^{i\theta_e}x_e=0\qquad(v\in\mathbb Z^2).
\]
Call the resulting matrix \(C_s\). At any original vertex incident to exactly one edge with nonzero \(x_e\), the equation cannot hold. Consequently, the finite graph formed by nonzero edges has minimum degree at least two at every nonisolated vertex. On the square grid, every nonempty such graph with at most six edges is a simple cycle: its only possible lengths are four (one elementary square) and six (a rectangle bounding two squares). Indeed, the grid has girth four, and the union of two distinct cycles requires at least seven edges (two adjacent four-cycles sharing one edge attain seven). In any simple cycle, the incidence equations determine each consecutive edge amplitude up to a scalar. Consistency upon returning to the starting vertex requires the oriented product of magnetic gains around the cycle to equal one; the even cycle length eliminates the sign \(s\). Accordingly, a four-cycle is possible exactly when \(e^{i\phi}=1\); a six-cycle is possible exactly when \(e^{2i\phi}=1\). This proves lower bounds of four, six and seven occupied *original* edges in the three cases.

**3. Sharp support witnesses.** For zero flux, use the four edges of a single elementary square with oriented edge coefficients \((+1,-1,-1,+1)\) on its bottom, top, left and right sides for \(s=-1\). For half flux, take the six boundary edges of two horizontally adjacent squares. For an arbitrary other flux, use all seven edges of those two squares, including their shared vertical edge. Write their bottom horizontal edges as \(a,b\), top horizontal edges as \(c,d\), and vertical edges from left to right as \(e,f,g\), all in positive coordinate orientation. Put \(\omega=e^{i\phi}\). The coefficients for \(s=-1\) are
\[
(a,b,c,d,e,f,g)=(-\omega,1,\omega,-\omega^2,\omega,-(1+\omega),1).
\]
Substitution in the six hub equations verifies \(C_{-1}x=0\) exactly. All seven coefficients are nonzero whenever \(\omega\notin\{1,-1\}\); at \(\omega=-1\), only the shared-edge coefficient vanishes and the six boundary edges give the half-flux witness. The zero-flux square witness was given above.

To transfer each witness to \(s=+1\), multiply the edge coefficient \(x_e\) by \((-1)^{u_1+u_2}\), where \(u\) is the *tail* of the original edge. Because adjacent original vertices have opposite checkerboard parity, this converts every row of \(C_{-1}x=0\) into the corresponding row of \(C_{+1}x'=0\), up to a nonzero row sign. Thus support sizes agree for the two energies. Doubling the occupied-edge counts proves the displayed formula.

**4. Oscillating confined states.** For any one of these physical supports choose nonzero eigenvectors \(\psi_+\) and \(\psi_-\) at energies \(+t\) and \(-t\), respectively, using the same edge set as above. Writing evolution time as \(\tau\), the evolving state is \(\psi(\tau)=e^{-it\tau}\psi_++e^{it\tau}\psi_-\). Its union of occupied sites is contained in the same finite support, with relative angular frequency \(2t\).

## Verification
The accompanying script `verification/lieb5_flux_checker.py` constructs the complete finite open Hamiltonian on a \(5\times4\) hub window, embeds each witness, and tests both signs for \(\phi=0,\pi,\pi/2,2\pi/3,\sqrt2\). In all ten cases the eigenvector residual is below \(10^{-12}\) and the count of occupied physical sites equals the claimed \(8\), \(12\), or \(14\). The script also exhaustively enumerates graph edge sets of size at most six in a \(4\times4\) hub window and confirms the possible minimum-degree-two types. These finite checks are not asserted to prove the infinite-lattice statement: the analytical grid geometry and hub-exclusion proof do that. To reproduce, run `python verification/lieb5_flux_checker.py` with Python and NumPy installed.

## Relationship to prior work
Hanafi et al. established and experimentally realized oscillating compact localized states from the two distinct flat bands of the unthreaded decorated Lieb-5 lattice; in particular, their eight-site octagonal state is the zero-flux member here. Zhang et al. earlier analyzed multiple flat bands and confinement in face-centered photonic square lattices. Centała and Kłos investigated compact localized states in magnonic Lieb lattices. Those inspected physical statements do not specify the present all-flux, all-parameter **minimum support** trichotomy. Classical gain-graph/frame-matroid circuit theory already characterizes balanced cycles, unbalanced thetas, and handcuffs as elementary dependencies; it provides important stronger *general graph-combinatorial context* for the incidence part of this argument. The present statement instead gives the physical hub-exclusion reduction at the two nonzero flat-band energies, the exact square-lattice flux and support thresholds, and shared-support beating. Its priority relative to other applications of gain-graph theory remains a genuine scope risk.

## Limitations
This is a mathematical result for the ideal equal-modulus nearest-neighbor Hermitian tight-binding model. Different interior bond strengths, onsite shifts, long-range couplings, or physical waveguide imperfections may change it. The minimum is over *stationary finitely supported eigenvectors at a fixed flat-band energy*, not arbitrary transiently confined states or all states in the full spectrum. The shared-support superposition assertion gives a construction, not an independent optimality theorem for every time-dependent trapping protocol. The statement concerns an infinite lattice; a finite torus with nontrivial flux quantization may have additional boundary constraints. Classical frame-matroid circuit results overlap substantially with the graph-theoretic portion, and independent verification of scientific priority is outstanding.

## References
1. H. Hanafi, P. Menz, A. McWilliam, J. Imbrock, and C. Denz, *Localized dynamics arising from multiple flat bands in a decorated photonic Lieb lattice*, arXiv:2207.01480v1 (posted 2022-07-04), APL Photonics **7**, 111301 (2022), DOI 10.1063/5.0109840.
2. Y. Zhang et al., *New face-centered photonic square lattices with flat bands*, arXiv:1605.04389v1 (2016), Annals of Physics **382**, 160–169 (2017).
3. G. Centała and J. W. Kłos, *Compact localized states in magnonic Lieb lattices*, Scientific Reports **13**, 12676 (2023), DOI 10.1038/s41598-023-39816-w.
4. T. Zaslavsky, *Frame matroids and biased graphs*, European Journal of Combinatorics **15**, 303–307 (1994), DOI 10.1006/eujc.1994.1034.
5. S. Xia et al., *Unconventional Flatband Line States in Photonic Lieb Lattices*, arXiv:1810.12618v1 (2018).
