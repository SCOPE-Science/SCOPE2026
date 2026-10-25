# A sharp three-absorber dichotomy for quantum transport on hypercubes

## Finding

For every integer \(d\ge2\), consider the unweighted \(d\)-dimensional binary hypercube \(Q_d\) with adjacency Hamiltonian \(A\). Let \(F\) be any three distinct vertices, each a continuous-time absorber with an arbitrary positive loss strength. The dimension \(R_d(F)\) of the subspace that is eventually absorbed is exactly

\[
R_d(F)=\begin{cases}2d,&\text{if two vertices of }F\text{ are antipodal},\\3d-1,&\text{otherwise}.\end{cases}
\]

The nondecaying dark subspace therefore has dimension \(2^d-R_d(F)\). From the maximally mixed one-particle initial state, the eventual absorption probability is exactly \(R_d(F)/2^d\), independently of the positive loss strengths. For a general initial density matrix \(\rho\), eventual absorption is \(\operatorname{Tr}(P_B\rho)\), where \(P_B\) projects onto the stated bright subspace.

In the three-cube, three traps with no antipodal pair give certain absorption, while three traps containing an antipodal pair absorb just \(3/4\) of a maximally mixed initial state. Among uniformly chosen unordered triples of vertices of \(Q_d\), the proportion containing an antipodal pair is exactly \(3/(2^d-1)\).

## Assumptions and scope

Vertices are bit vectors \(x\in\{0,1\}^d\), with an edge whenever their Hamming distance is one. The Hilbert space is \(\mathbb C^{2^d}\), equipped with basis vectors \(|x\rangle\). Fix three distinct vertices \(F=\{u,v,w\}\) and strictly positive constants \(\gamma_z\) for each \(z\in F\). Evolution of the unabsorbed wavefunction is governed by \(\dot\psi=(-iA-\Gamma)\psi\), with \(\Gamma=\sum_{z\in F}\gamma_z|z\rangle\langle z|\). The lost squared norm is called absorption. Time is continuous, with \(\hbar=1\). The claim is for each fixed finite \(d\ge2\); it makes no infinite-volume or uniform-in-\(d\) assertion. Two vertices are antipodal when their bit strings differ in all \(d\) coordinates.

## Proof

**Spectral bright–dark decomposition.** The Walsh characters \(\chi_S(x)=2^{-d/2}(-1)^{\sum_{k\in S}x_k}\), indexed by subsets \(S\subseteq[d]\), diagonalize \(A\): the eigenvalue at Walsh weight \(|S|=j\) is \(d-2j\), for \(0\le j\le d\). Let \(E_j\) be the orthogonal spectral projector onto weight \(j\). Define

\[
B=\sum_{j=0}^d\operatorname{span}\{E_j|z\rangle:z\in F\},\qquad D=B^\perp.
\]

Each subspace is invariant under \(A\). Every trap basis vector belongs to \(B\), hence both subspaces are invariant under \(\Gamma\). A vector is in \(D\) precisely when its component in every eigenspace is orthogonal to all three trap vectors, so it is dark to all absorbers. Conversely, an eigenvector of the dissipative generator on \(B\) with eigenvalue of zero real part would have \(\langle\psi,\Gamma\psi\rangle=0\), hence \(\Gamma\psi=0\), and would be an eigenvector of \(A\) vanishing on \(F\); it would lie in \(D\cap B=\{0\}\). Since \(-iA-\Gamma\) is dissipative and finite dimensional, all its eigenvalues on \(B\) have strictly negative real parts. Thus its semigroup decays on \(B\), and the semigroup is unitary on \(D\). The asymptotic surviving trace of an initial density matrix is \(\operatorname{Tr}(P_D\rho)\), proving the absorption statements once \(\dim B\) is known. This step uses positivity, not equality, of the rates.

**Exact shell rank.** The mutually orthogonal weight eigenspaces give

\[
\dim B=\sum_{j=0}^d r_j(F),\quad r_j(F)=\operatorname{rank}\bigl[((-1)^{S\cdot z})_{z\in F}\bigr]_{|S|=j},
\]

where \(S\cdot z\) is the mod-two dot product. Translation of all three vertices by the same bit vector only rescales the individual Walsh rows and does not change rank; therefore take \(F=\{0,a,b\}\). For \(j=0,d\), there is one row and \(r_j(F)=1\).

For an interior weight \(1\le j\le d-1\), write each row as \((1,(-1)^{S\cdot a},(-1)^{S\cdot b})\). If a pair of the three traps is antipodal, their Walsh columns are proportional on every fixed weight: for antipodes \(z,z+\mathbf1\), \((-1)^{S\cdot(z+\mathbf1)}=(-1)^j(-1)^{S\cdot z}\). The third column is not proportional to these because its displacement from either antipode is neither zero nor \(\mathbf1\). Indeed, if the parity \(S\cdot c\) were constant over all size-\(j\) subsets for an interior \(j\), swapping one selected coordinate with one unselected coordinate would force all coordinates of \(c\) equal, giving \(c=0\) or \(c=\mathbf1\). Hence \(r_j(F)=2\).

If no pair is antipodal, all three columns are linearly independent at every interior weight. To see this, every distinct sign pair \(((-1)^{S\cdot a},(-1)^{S\cdot b})\) gives one of the four rows \((1,\pm1,\pm1)\), and any three distinct such rows have determinant of magnitude four. Were the rank at most two, the realized parity pairs \((S\cdot a,S\cdot b)\in\mathbb F_2^2\) would thus number at most two, lying in an affine line with direction a one-dimensional subspace \(H\) (or in one point, for which choose any line). Fix any two coordinates \(h,k\). Since \(1\le j\le d-1\), there is a size-\(j\) subset containing \(h\) and not \(k\). Swapping \(h\) for \(k\) changes the parity pair by \((a_h,b_h)+(a_k,b_k)\), which therefore belongs to \(H\). Hence every coordinate pattern \((a_h,b_h)\) lies in one affine line of \(\mathbb F_2^2\). The three possible directions of a line force one of \(a\), \(b\), or \(a+b\) to be a constant bit vector. Since \(0,a,b\) are distinct, constant zero is impossible; constant one would make a pair of the traps antipodal, contradicting the case assumption. Consequently at least three sign pairs occur and \(r_j(F)=3\).

Summing the two endpoint ranks and the \(d-1\) interior ranks gives \(2+2(d-1)=2d\) in the antipodal case and \(2+3(d-1)=3d-1\) otherwise. For \(d=2\), every triple contains an antipodal pair, as required by the formula.

**Configuration count.** There are \(2^{d-1}\) unordered antipodal pairs. Each belongs to exactly \(2^d-2\) distinct triples. No triple contains more than one antipodal pair. Dividing their product by \(\binom{2^d}{3}\) yields \(3/(2^d-1)\).

## Verification

Run the included standalone standard-library program with `python verify_three_hypercube_traps.py`. It computes ranks independently from the Walsh eigenshells and from the finite Krylov matrix \([A^k|z\rangle]_{z\in F,\ 0\le k\le d}\), using exact modular arithmetic. It checks all triples up to translation symmetry for \(d=2,3,4,5\), plus a deterministic range in \(d=6\), and specifically distinguishes the two possible ranks in the three-cube. The executable reports `PASS 1388 exact finite rank checks (two independent formulations)`. These checks are finite and not a proof of the theorem for all \(d\); the preceding shell-rank argument supplies that proof. No external computation or unavailable supporting file is needed to reconstruct the proof.

## Relationship to prior work

Bernasconi, Godsil and Severini (2008) establish spectral quantum transport, including antipodal perfect transfer, on cubelike graphs; the antipodal symmetry used here is therefore not claimed as new. Novo, Mohseni and Omar (2013) examine one-site trapping and disorder effects, and Novo et al. (2014) give a general Krylov reduction for quantum walks with a single sink and evaluate the single-sink hypercube. In particular the single-sink \(d+1\) bright dimension and the general Krylov method are prior results, not part of the originality claim. The new assessed assertion is the complete placement dichotomy for **three distinct absorbers**, including the value \(3d-1\) for every configuration without an antipodal pair, the combined mixed-state efficiency, and the exact incidence proportion. A general observability or controllability theorem may furnish another derivation and remains a priority-search risk.

## Limitations

The result concerns unweighted hypercube adjacency dynamics, finite \(d\), and three distinct strictly positive on-site absorbers. Arbitrary edge weights, unequal coherent couplings, more than three absorbers, finite-time absorption distributions, coherent source-specific absorption values, and open-system dephasing are not classified. The relation to all possible earlier graph-observability classifications has not been exhaustively verified. No independent audit has been performed.

## References

1. A. Bernasconi, C. Godsil and S. Severini, *Quantum Networks on Cubelike Graphs*, arXiv:0808.0510, first posted 2008-08-04.
2. L. Novo, M. Mohseni and Y. Omar, *Disorder-assisted quantum transport in suboptimal decoherence regimes*, arXiv:1312.6989, first posted 2013-12-25.
3. L. Novo, S. Chakraborty, M. Mohseni, H. Neven and Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209, first posted 2014-12-22.
4. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794 (background only; original publication is later than the motivating 2008 paper).
5. F. Thiel et al., *Dark states of quantum search cause imperfect detection*, Physical Review Research 2, 043107 (2020), DOI: 10.1103/PhysRevResearch.2.043107 (related projective-detection setting; abstract inspected).
