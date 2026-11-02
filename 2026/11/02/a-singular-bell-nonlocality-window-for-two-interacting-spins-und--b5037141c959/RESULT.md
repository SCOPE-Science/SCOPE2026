# A singular Bell-nonlocality window for two interacting spins under Poisson resetting

## Finding
For the global Poisson-reset transverse-Ising two-spin model, the stationary state's maximal Clauser–Horne–Shimony–Holt (CHSH) value has a **nontrivial strong-interaction/weak-reset scaling window**. In dimensionless units, take interaction \(a>0\), resetting rate \(R>0\), and let \(\mathcal B(a,R)\) be the largest CHSH expectation over local dichotomic projective measurements. For each fixed \(q>0\),
\[
\lim_{a\to\infty}\mathcal B\left(a,\frac q{2a}\right)=2\sqrt{1+\left(\frac q{1+q^2}\right)^2}.
\]
This profile is strictly above the classical bound \(2\), and its unique maximum is \(\sqrt5\), attained at \(q=1\). For each \(a\ge2\), the finite choice \(R=1/(2a)\) itself strictly violates CHSH. In contrast, the strong-interaction limit at any fixed positive reset rate has CHSH value tending to \(2\); and the zero-reset stationary limit at each fixed finite interaction has value strictly below \(2\). The scaling law is an exact limit for this particular model, not a claimed global upper bound on CHSH for arbitrary finite parameters.

## Assumptions and scope
Work in units \(\hbar=\Omega=1\). Two spins with Pauli matrices \(\sigma_x,\sigma_y,\sigma_z\) have Hamiltonian
\[
H=-a\,\sigma_z\otimes\sigma_z+\frac12(\sigma_x\otimes I+I\otimes\sigma_x),\qquad a=J/\Omega>0.
\]
At rate \(R=r/\Omega>0\), a Poisson event resets the full pure state to \(|\downarrow\downarrow\rangle\). The stationary ensemble density operator is
\[
\rho_{a,R}=R\int_0^\infty e^{-Rt}e^{-iHt}|\downarrow\downarrow\rangle\langle\downarrow\downarrow|e^{iHt}\,dt.
\]
Set \(T_{ij}=\mathrm{tr}(\rho_{a,R}\,\sigma_i\otimes\sigma_j)\) in order \(i,j=x,y,z\). If \(s_1\ge s_2\ge s_3\) are the singular values of the real \(3\times3\) correlation matrix \(T\), the two-qubit Horodecki criterion gives \(\mathcal B=2\sqrt{s_1^2+s_2^2}\).

## Proof
Let \(D=(1+R^2)^2+4a^2R^2\) and \(E=4a^2+R^2+4\). The stationary resolvent equation
\[
R(\rho_{a,R}-|\downarrow\downarrow\rangle\langle\downarrow\downarrow|)+i[H,\rho_{a,R}]=0
\]
is a finite linear system. Use the orthonormal Bell-sector basis
\[
A=\frac{|\uparrow\uparrow\rangle-|\downarrow\downarrow\rangle}{\sqrt2},\quad
E_0=\frac{|\uparrow\uparrow\rangle+|\downarrow\downarrow\rangle}{\sqrt2},\quad
S=\frac{|\uparrow\downarrow\rangle+|\downarrow\uparrow\rangle}{\sqrt2}.
\]
The unused antisymmetric \((|\uparrow\downarrow\rangle-|\downarrow\uparrow\rangle)/\sqrt2\) sector is never populated. In the ordered basis \((A,E_0,S)\),
\[
H=\begin{pmatrix}-a&0&0\\0&-a&1\\0&1&a\end{pmatrix},\qquad
\rho_0=\frac12\begin{pmatrix}1&-1&0\\-1&1&0\\0&0&0\end{pmatrix}.
\]
Solving the resolvent equation and tracing the Pauli products gives the **exact** symmetric correlation matrix
\[
T(a,R)=\begin{pmatrix}
0&-2aR/D&2aR^2/D\\
-2aR/D&2/E&-R/E\\
2aR^2/D&-R/E&(4a^2+R^2+2)/E
\end{pmatrix}.
\]
This is independently verifiable from the energy-basis Laplace integral; a standalone exact checker is supplied.

Put \(R=q/(2a)\) with fixed \(q>0\). Then \(D\to1+q^2\), \(E\to\infty\), \(2aR=q\), and \(R\to0\), so
\[
T(a,q/(2a))\longrightarrow T_q=\begin{pmatrix}
0&-q/(1+q^2)&0\\
-q/(1+q^2)&0&0\\
0&0&1
\end{pmatrix}.
\]
Its singular values are \(1,q/(1+q^2),q/(1+q^2)\). The Horodecki formula gives the asserted profile. Since \(q/(1+q^2)\) rises strictly on \((0,1)\) and falls strictly on \((1,\infty)\), the limiting maximum is uniquely \(\sqrt5\) at \(q=1\).

For finite \(a\), use the min-max variational characterization of the largest two eigenvalues of \(T^{\mathsf T}T\):
\[
\frac{\mathcal B(a,R)^2}{4}\ge\|T e_x\|^2+\|Te_z\|^2\ge T_{xy}^2+T_{zz}^2.
\]
At \(R=1/(2a)\), put \(y=a^2\). Direct rational simplification yields
\[
T_{zz}^2+T_{xy}^2-1=
\frac{16y(4y+1)^2 P(y)}{(16y^2+16y+1)^2(32y^2+8y+1)^2},
\]
where
\[
P(y)=256y^5-640y^4-688y^3-160y^2-20y-1.
\]
For \(y\ge4\), bound the five negative terms in \(P\) by \(160y^5,43y^5,3y^5,y^5,y^5\), respectively. Their sum is at most \(208y^5<256y^5\), proving strict Bell violation for all \(a\ge2\). For example, at \(a=2,R=1/4\), \(T_{zz}=289/321\) and \(T_{xy}=-256/545\), and the sum of their squares is greater than one.

Finally, at fixed \(R>0\), \(a\to\infty\) gives \(T\to\mathrm{diag}(0,0,1)\), whence \(\mathcal B\to2\). At fixed \(a>0\), \(R\downarrow0\) gives \(T\to\mathrm{diag}(0,1/[2(a^2+1)],(2a^2+1)/[2(a^2+1)])\). Here the sum of the two largest squared singular values equals
\[
\frac{(2a^2+1)^2+1}{4(a^2+1)^2}<1,
\]
so its CHSH value is strictly less than \(2\). This establishes the noncommuting operational regimes.

## Verification
The supplied `verify.py` independently constructs the stationary generator in the symmetric Bell subspace, tests the exact state equation and the full Pauli correlation matrix, symbolically verifies the scaling limit and finite-rate rational identity, and compares direct energy-basis Laplace transforms at explicit parameters. Only finite rational checks and the independently derived algebra support the theorem; the infinite-parameter statements follow from the explicit formulas and elementary limiting arguments in the proof.

## Relationship to prior work
Kulkarni and Majumdar (2023) introduced and solved the *same* continuously Poisson-reset two-spin model and computed stationary entropy, fidelity, and concurrence. Their general density operator and an entropy crossover depending on \(aR\) are established prior results, **not** claimed as new. Horodecki, Horodecki, and Horodecki (1995) established the general two-qubit CHSH spectral criterion, also not new. The finding is the explicit model-specific Bell-correlation matrix, its sharp singular nonlocality profile with unique scaling maximum, and a positive finite-coupling nonlocality guarantee. A distinct later study of reset-driven Ising environments examines concurrence and discord for two central spins but does not establish this stationary CHSH theorem.

## Limitations
The theorem concerns ideal stationary ensemble averages, projective local CHSH optimization, identical global resets, ferromagnetic coupling, and the specified pure reset state. It does not assert the **global** maximum of \(\mathcal B\) over all finite \(a,R\), a sharp finite-parameter boundary between local and nonlocal regimes, finite-sample detection power, or robustness to imperfect resetting. General prior density-matrix formulas permit these observables to be calculated, leaving some publication-priority risk for implicit reductions.

## References
1. M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485v1 (first public 2023-07-14), https://arxiv.org/abs/2307.07485 .
2. R. Horodecki, P. Horodecki, and M. Horodecki, *Violating Bell inequality by mixed spin-1/2 states: necessary and sufficient condition*, Physics Letters A 200, 340–344 (1995), https://doi.org/10.1016/0375-9601(95)00214-N .
3. *Quantum Correlation Dynamics Subjected to Quantum Reset-Driven Environment*, arXiv:2602.09348v1, https://arxiv.org/html/2602.09348v1 (different environmental-reset model).
