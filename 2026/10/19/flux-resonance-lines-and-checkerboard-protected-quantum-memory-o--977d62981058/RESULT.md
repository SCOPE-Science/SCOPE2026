# Flux-resonance lines and checkerboard-protected quantum memory on square tori

## Finding

For even integers \(m,n\ge4\), set \(g=\gcd(m,n)\), \(N=mn\), and write \(f_x,f_y\in[0,1)\) for the two Aharonov--Bohm boundary twists measured in flux quanta. A nearest-neighbor continuous-time quantum walk on \(C_m\square C_n\) is independently dephased at every even-checkerboard vertex, with any strictly positive rates; no odd-checkerboard vertex is directly monitored. Define
\[
I_{\pm}=\mathbf 1\!\left\{nf_x\pm mf_y\in g\mathbb Z\right\},\qquad
k=\frac g2(I_++I_-)-\mathbf 1\!\{f_x=f_y=0\}.
\]
Then \(k\ge0\) is **exactly** the number of decoherence-free one-particle states, all supported on odd vertices. If \(D\) is their orthogonal projector, every initial density matrix has the limit
\[
\lim_{t\to\infty}\rho(t)
=D\rho(0)D+\frac{1-\operatorname{Tr}(D\rho(0))}{N-k}(I_N-D).
\]
There are no nonstationary persistent oscillations. In particular, off the two sets of flux-resonance lines, \(k=0\) and complete mixing occurs.

For a square \(m=n=L\) (even \(L\ge4\)) the complete classification simplifies: \(k=0\) away from \(f_x=f_y\) and \(f_x+f_y=1\); \(k=L/2\) on either line apart from their crossing; \(k=L-1\) at \((f_x,f_y)=(0,0)\); and \(k=L\) at \((f_x,f_y)=(1/2,1/2)\). The first diagonal includes the origin, with its separately stated value. Thus generic twists erase all initial-state memory, whereas resonant twists protect a subspace whose dimension grows linearly in the circumference. The half-flux crossing has one extra state compared with zero flux.

For a walker initially localized at an odd site, its exact long-time return probability is
\[
R_{m,n}=p^2+\frac{(1-p)^2}{N-k},\qquad p=\frac{2k}{N}.
\]
For square tori along even \(L\to\infty\), the limiting rescaled return \(L^2 R_{L,L}\) takes exactly the three values \(1\) (generic twists), \(2\) (a single resonance line), or \(5\) (either double-resonant point). The order of limits is time first, lattice size second.

## Assumptions and scope

Let vertices be \((x,y)\in\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\). The Hamiltonian has constant hopping magnitude one and flat connection
\[
H_{(x,y),(x+1,y)}=e^{2\pi i f_x/m},\qquad
H_{(x,y),(x,y+1)}=e^{2\pi i f_y/n},
\]
with the conjugates on reverse bonds, all other entries zero, and periodic indices. The total holonomies around the two noncontractible loops are \(e^{2\pi if_x}\) and \(e^{2\pi if_y}\). For even \(m,n\), the checkerboard sets \(E=\{(x,y):x+y\text{ even}\}\) and \(O=V\setminus E\) are well defined and both have \(N/2\) vertices.

Let \(P_e=|e\rangle\langle e|\). For arbitrary \(\gamma_e>0\), evolution means the finite-dimensional trace-preserving Lindblad equation
\[
\dot\rho=-i[H,\rho]-\tfrac12\sum_{e\in E}\gamma_e[P_e,[P_e,\rho]].
\]
This is site-selective **pure dephasing**, not absorption, a sink, or collective sublattice measurement. The assertion holds for all density matrices, all even sizes at least four, and all twists in the stated fundamental square. No relaxation-rate bound uniform in size or flux is asserted.

## Proof

**1. Peripheral spectrum and the commutant.** For every matrix \(X\), Hilbert--Schmidt dissipation gives
\[
\operatorname{Re}\langle X,\mathcal LX\rangle
=-\frac12\sum_{e\in E}\gamma_e\|[P_e,X]\|_2^2.
\]
Thus an eigenmatrix of \(\mathcal L\) with purely imaginary eigenvalue commutes with every \(P_e\). Relative to \(\mathbb C^E\oplus\mathbb C^O\), such a matrix is block diagonal, and its even block is diagonal. Since \(H\) is bipartite, its commutator with a block-diagonal matrix is off-block-diagonal. Therefore the eigenvalue equation forces that eigenvalue to be zero and \([H,X]=0\). There are no other peripheral eigenvalues.

Write \(H=\begin{pmatrix}0&B\\B^*&0\end{pmatrix}\) (even vertices first) and \(X=\operatorname{diag}(\operatorname{diag}(a_e),C)\). Commutation with \(H^2\) implies \((a_e-a_{e'})(BB^*)_{e,e'}=0\). Between any even sites separated by one of the diagonal steps \((1,1)\) or \((1,-1)\), \((BB^*)_{e,e'}\ne0\): the two common two-step paths have identical magnetic phase because the connection has zero plaquette flux, and reinforce rather than cancel. Diagonal steps generate the entire even-checkerboard sublattice, since for coordinates of equal parity, \((x,y)=[(x+y)/2](1,1)+[(x-y)/2](1,-1)\). Hence all \(a_e=c\).

Now \(BC=cB\) and \(CB^*=cB^*\); consequently \(C=cI\) on \(\operatorname{im}B^*\), leaves that space and its orthogonal complement invariant, and is arbitrary on \(\ker B\). Let \(D\) be the projector onto \(\ker B\) inside the odd subspace, extended by zero on the even subspace. The common commutant and hence the fixed-operator space is
\[
\{c(I-D)+DXD:c\in\mathbb C,\ X\in M_N(\mathbb C)\}.
\]
Since this space is also the kernel of the adjoint Lindblad generator, the asymptotic spectral projection is the Hilbert--Schmidt orthogonal projection onto it. The completely positive trace-preserving semigroup is bounded, precluding nontrivial zero-eigenvalue Jordan blocks; with no other imaginary eigenvalues, it converges. The projection formula is precisely the displayed density-matrix limit.

**2. Arithmetic zero-mode count.** The Bloch waves \(e^{2\pi i(kx/m+\ell y/n)}\), with \(0\le k<m\), \(0\le\ell<n\), diagonalize \(H\), with real eigenvalues
\[
\varepsilon_{k,\ell}=2\cos\frac{2\pi(k+f_x)}m+2\cos\frac{2\pi(\ell+f_y)}n.
\]
A zero eigenvalue occurs iff
\[
\frac{k+f_x}m\equiv\frac12+\frac{\ell+f_y}n\pmod1
\quad\text{or}\quad
\frac{k+f_x}m\equiv\frac12-\frac{\ell+f_y}n\pmod1.
\]
Each branch is a congruence with integer part \(nk\mp m\ell\) modulo \(mn\). Because \(g\mid mn/2\) for even \(m,n\), the branch has solutions precisely if \(nf_x\mp mf_y\in g\mathbb Z\), and then exactly \(g\) solutions. The branches intersect only if \(\cos[2\pi(\ell+f_y)/n]=\pm1\), which forces \(f_y=0\); the first equation then forces \(f_x=0\). At the untwisted point they intersect in exactly two Bloch modes, with momenta \((k,\ell)=(m/2,0),(0,n/2)\). Thus the complete zero-eigenvalue multiplicity of \(H\) is
\[
\nu_0=g(I_++I_-)-2\mathbf1\{f_x=f_y=0\}.
\]
The two checkerboard sectors have equal dimension; the nonzero eigenvalues of the two blocks of the bipartite Hamiltonian come in opposite pairs, and \(\ker H=\ker B\oplus\ker B^*\) with \(\dim\ker B=\dim\ker B^*\). Consequently \(k=\nu_0/2\), proving the arithmetic classification.

**3. Local return and the square phase diagram.** Because the flat-connection Hamiltonian and the even-checkerboard monitoring pattern are invariant under translations preserving checkerboard parity, the diagonal entries of \(D\) are constant over odd sites. Their sum is \(k\), so for each odd site \(v\), \(p=\langle v,Dv\rangle=2k/N\). Inserting \(\rho(0)=|v\rangle\langle v|\) into the limiting-state formula gives \(R_{m,n}=p^2+(1-p)^2/(N-k)\). For \(m=n=L\), the two arithmetic conditions become \(f_x=f_y\) and \(f_x+f_y\in\{0,1\}\), respectively. Within \([0,1)^2\), the latter is the antidiagonal \(f_x+f_y=1\) together with \((0,0)\). This proves the four cases for \(k\). Substituting \(k=0,L/2,L-1,L\), then letting \(L\) tend to infinity through even integers, gives respectively \(L^2R\to1,2,5,5\), as stated.

## Verification

The standalone `verify.py` constructs the complex Hermitian hopping matrix independently of the Fourier count, and compares its nullity with the arithmetic formula. It also computes the odd-sublattice block kernel, checks connectivity of the weighted length-two even graph, builds the dark projector, verifies its stationarity and the return formula, and checks dephasing commutators. The recorded run passed 36 independent combinations of sizes and twist pairs, plus ten stationary-state calculations. The script requires NumPy; `requirements.txt` records the dependency. These finite checks are reproducibility aids; the all-size, all-flux and all-initial-state statements rest on the above exact proof.

## Relationship to prior work

The general theory of finite-dimensional Lindblad stationary states and noiseless subsystems is established in Baumgartner--Narnhofer (2008). Strauch (2008) analyzed site-decohered continuous-time hypercube walks under different, all-site noise and hitting-probability questions. Campos Venuti--Zanardi (2011) related dark subspaces to transport in hybrid open networks. Kassal--Aspuru-Guzik (2012) studied environment-assisted transport with all-site dephasing, loss, and traps in ordered chains and circles. These provide physical context and general machinery, not the two-holonomy arithmetic count or the exact three-level torus return law above. The untwisted \(4\times4\) grid is isomorphic to the four-cube, so its three-dimensional odd dark kernel is not presented as independently new; the rectangular and flux-dependent classification is the subject here.

## Limitations

The result concerns a **flat** magnetic connection (Aharonov--Bohm flux through torus handles), not a uniform magnetic field through each plaquette. It requires unit-magnitude nearest-neighbor couplings, both circumferences even and at least four, independent positive dephasing on every even site and nowhere else, and no onsite potentials or losses. Small perturbations away from an exact resonance generally destroy protected zero modes, but this theorem does not estimate the ensuing relaxation times. No independent audit has been performed.

## References

1. B. Baumgartner and H. Narnhofer, *Analysis of quantum semigroups with GKS--Lindblad generators II. General*, arXiv:0806.3164 (first posted 2008-06-19), https://arxiv.org/abs/0806.3164.
2. F. W. Strauch, *Reexamination of decoherence in quantum walks on the hypercube*, arXiv:0808.3403 (first posted 2008-08-25), https://arxiv.org/abs/0808.3403.
3. L. Campos Venuti and P. Zanardi, *Excitation transfer through open quantum networks: a few basic mechanisms*, arXiv:1101.4808 (first posted 2011-01-25), https://arxiv.org/abs/1101.4808.
4. I. Kassal and A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems*, arXiv:1201.5202 (first posted 2012-01-25), https://arxiv.org/abs/1201.5202.
