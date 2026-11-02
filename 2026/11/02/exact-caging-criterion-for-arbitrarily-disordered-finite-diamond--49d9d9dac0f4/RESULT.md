# Exact caging criterion for arbitrarily disordered finite diamond chains

## Finding

A diamond chain has \(N\ge2\) hub sites \(A_1,\ldots,A_N\) and, for each \(1\le j<N\), two arm sites \(U_j,L_j\) linked **only** to the adjacent hubs \(A_j,A_{j+1}\). Give every vertex a real on-site energy, and every hub-arm edge a nonzero complex hopping amplitude. The matrix \(H\) is Hermitian; the edges among hubs and the edges among arm sites are absent. Let
\[
v_j=\begin{pmatrix}H_{U_j,A_j}\\H_{L_j,A_j}\end{pmatrix},\qquad
w_j=\begin{pmatrix}H_{U_j,A_{j+1}}\\H_{L_j,A_{j+1}}\end{pmatrix},
\qquad D_j=\operatorname{diag}(u_j,\ell_j).
\]
There is no periodicity assumption on \(H\), its couplings, or its on-site energies.

**Theorem (necessary and sufficient exact caging).** For every such finite chain, the following are equivalent:

1. For all distinct hubs \(j,k\) and every \(t\in\mathbb R\),
   \[
   \langle A_k|e^{-itH}|A_j\rangle=0.
   \]
2. For every \(1\le j<N\),
   \[
   \boxed{\;w_j^\dagger v_j=0,\qquad u_j=\ell_j.\;}
   \]
3. The Hilbert space splits into mutually orthogonal, \(H\)-invariant subspaces \(\mathcal C_j\) of dimensions \(2,3,\ldots,3,2\), each containing exactly the corresponding hub basis vector \(\lvert A_j\rangle\), with the explicit construction below.

Because all four edge amplitudes on a diamond are nonzero, the condition \(w_j^\dagger v_j=0\) is the exact cancellation
\[
\overline{w_{j,U}}v_{j,U}=-\overline{w_{j,L}}v_{j,L},
\]
which combines a relative phase of \(\pi\) and equal absolute two-hop products. Thus flux tuning alone is insufficient if the two path magnitudes differ.

For any initial basis state, the evolution has finite, uniformly bounded spatial support, independent of \(N\). If its initial site is a hub, it remains in one hub-centered cage; if it is an arm, it remains in at most two adjacent cages. The result holds for unbounded nonzero edge magnitudes and phase patterns **subject to the one complex cancellation constraint per diamond**, and arbitrary real hub energies and common arm energies varying independently between diamonds. In general the eigenvalues of different cages are unequal, so exact caging need not mean a degenerate flat-band spectrum.

## Assumptions and scope

The system is a finite *open* chain, with exactly \(3N-2\) vertices, no direct hub-hub or arm-arm edges, Hermitian time-independent hopping, and four *nonzero* hub-arm amplitudes per diamond. Arbitrary complex phases are permitted (subject to Hermiticity). The two arm energies may differ until the equivalence criterion is imposed. On-site terms at the hubs are unrestricted real numbers. Natural units set \(\hbar=1\).

The full-Hilbert-space decomposition in the theorem refers to the particular explicit cages defined below, not to every possible invariant decomposition of \(H\). A global overall phase or gauge transformation does not change the condition.

## Proof

**Necessity from two moments.** For adjacent hubs \(A_j,A_{j+1}\), no direct edge exists. The only two-step paths travel through \(U_j,L_j\), so
\[
(H^2)_{A_{j+1},A_j}=w_j^\dagger v_j.
\]
If their transition amplitude vanishes at all real times, analyticity of the matrix exponential implies that every derivative at zero vanishes, including the above moment. Every three-step walk between those hubs either spends one step on a hub diagonal, or one step on the same intervening arm diagonal; hence
\[
(H^3)_{A_{j+1},A_j}=(h_j+h_{j+1})w_j^\dagger v_j+w_j^\dagger D_jv_j,
\]
where \(h_j=H_{A_j,A_j}\). With the second moment zero, the third moment becomes
\[
0=w_j^\dagger D_jv_j
=(u_j-\ell_j)\overline{w_{j,U}}v_{j,U}.
\]
The last edge product is nonzero by hypothesis, forcing \(u_j=\ell_j\). This proves necessity **on each link**; cancellations among different diamonds cannot evade the adjacent-hub moment constraints.

**Sufficiency and explicit block decomposition.** Suppose the two conditions hold. In the two-dimensional arm space at link \(j\), define
\[
\lvert V_j\rangle=\frac{v_j}{\|v_j\|},\qquad
\lvert W_j\rangle=\frac{w_j}{\|w_j\|}.
\]
These vectors are orthonormal because \(w_j^\dagger v_j=0\). Since \(D_j=\epsilon_j I_2\), each is an eigenvector of the arm on-site term with energy \(\epsilon_j=u_j=\ell_j\). Moreover \(\lvert V_j\rangle\) couples only to hub \(A_j\), and \(\lvert W_j\rangle\) couples only to \(A_{j+1}\). Set
\[
\mathcal C_j=\operatorname{span}\{\lvert A_j\rangle,
\lvert W_{j-1}\rangle\ (j>1),
\lvert V_j\rangle\ (j<N)\}.
\]
The cages are mutually orthogonal, their dimensions sum to \(3N-2\), and \(H\mathcal C_j\subseteq\mathcal C_j\). In the displayed order the restriction to an interior cage is
\[
H\big|_{\mathcal C_j}=\begin{pmatrix}
h_j&\|w_{j-1}\|&\|v_j\|\\
\|w_{j-1}\|&\epsilon_{j-1}&0\\
\|v_j\|&0&\epsilon_j
\end{pmatrix},
\]
with the missing row and column omitted at the endpoints. Consequently
\[
H\cong\bigoplus_{j=1}^{N}H\big|_{\mathcal C_j},\qquad
 e^{-itH}\cong\bigoplus_{j=1}^{N}e^{-itH|_{\mathcal C_j}}
\]
for every real \(t\), which implies all off-diagonal hub transition amplitudes vanish. It also gives a compactly supported orthonormal eigenbasis: diagonalize these independent blocks. Every initial arm state is a linear combination of one \(\lvert V_j\rangle\) and one \(\lvert W_j\rangle\), hence occupies at most two neighboring cages. The conditions are sufficient and give (iii), while (iii) immediately implies (i).

**Sharp leakage orders.** Define \(p_j=w_j^\dagger v_j\). The matrix-exponential Taylor series gives
\[
\langle A_{j+1}|e^{-itH}|A_j\rangle
=-\frac{p_jt^2}{2}+\frac{it^3}{6}
\big((h_j+h_{j+1})p_j+w_j^\dagger D_jv_j\big)+O(t^4).
\]
If \(p_j\ne0\), leakage already occurs at order \(t^2\). If \(p_j=0\) and \(u_j\ne\ell_j\), it first occurs at order \(t^3\), with coefficient \(i(u_j-\ell_j)\overline{w_{j,U}}v_{j,U}/6\ne0\). Consequently the corresponding **transition probability** starts at order \(t^4\), respectively \(t^6\), with positive leading coefficients \(\lvert p_j\rvert^2/4\), respectively \(\lvert (u_j-\ell_j)\overline{w_{j,U}}v_{j,U}\rvert^2/36\). Thus both requirements are individually necessary and have distinct short-time signatures in amplitude and probability.

**Nonuniform example.** On a three-hub chain choose \(v_1=(1,2)^T\), \(w_1=(2,-1)^T\), \(v_2=(1,3)^T\), and \(w_2=(3,-1)^T\), with hub energies \((0,2,5)\) and paired arm energies \((7,7)\), \((-2,-2)\). All bond amplitudes are nonzero and nonconstant, yet both inner products vanish. The seven-state Hamiltonian splits into blocks of sizes \(2,3,2\) and every hub-to-other-hub amplitude vanishes identically at all times.

## Verification

The included standalone file `diamond_cage_checker.py` reconstructs random finite Hermitian matrices with nonuniform complex four-edge couplings and nonuniform real on-site terms. It verifies local orthogonality, unitary block decomposition, spectra, exact matrix moments, and near-zero hub transfers computed by matrix exponentials; it also perturbs a single arm energy and separately one hopping amplitude to confirm the first nonvanishing moments. Run `python diamond_cage_checker.py` with NumPy and SciPy. It passed **2,970** numerical assertions for hub counts \(N=2,\ldots,12\), nine disorder realizations per count. The largest structural/spectral discrepancy was \(2.52\times10^{-14}\). Finite calculations are checks, not substitutes for the preceding analytic proof.

## Relationship to prior work

Vidal, Mosseri and Douçot introduced magnetic-flux cages and bounded wavepacket support for geometrically symmetric rhombic structures [1]. Flach and collaborators developed local unitary detangling of compact flat-band states and their response to local correlated potentials [2]. Longhi treated photonic AB caging for periodic rhombic chains [3]. Bodyfelt and collaborators examined correlated perturbations in flat-band lattices [4]. More recent works by Gligorić and collaborators [5] and Ahmed and collaborators [6,7] investigated diamond-chain disorder. In particular [6,7] already demonstrate exact decoupling of **the fixed-hopping model** under symmetric arm potential disorder; that covered subcase is not claimed as new here.

The distinct claim here is a necessary-and-sufficient all-time hub-caging test for **arbitrary link-by-link nonzero complex hopping strengths and phases**, combined with arbitrary hub and equal-pair arm potentials; a complete independent-cage decomposition and the sharp distinction between second- and third-order leakage. It does not claim invention of Aharonov-Bohm caging or of local detangling. An equivalent result in a broader local-unitary or flat-band construction framework may exist; historical priority is not independently certified.

## Limitations

The characterization requires the open two-arm-per-link geometry, no bypass hopping, nonzero four-edge couplings, a Hermitian static single-particle Hamiltonian, and perfect phase/energy matching. It does not cover periodic boundary conditions, extra edges, vanishing couplings, non-Hermitian gain/loss, many-body interactions, dynamical disorder, or approximate persistence under finite perturbations. The short-time amplitude hierarchy does not by itself quantify late-time leakage. No claim is made about an extensive degenerate flat band in nonperiodic systems.

## References

[1] J. Vidal, R. Mosseri, B. Douçot, *Aharonov-Bohm cages in two-dimensional structures* (1998), https://arxiv.org/abs/cond-mat/9806068 (public 1998-06-05).

[2] S. Flach et al., *Detangling flat bands into Fano lattices* (2014), https://arxiv.org/abs/1311.5689 ; https://doi.org/10.1209/0295-5075/105/30001 .

[3] S. Longhi, *Aharonov-Bohm photonic cages in waveguide and coupled resonator lattices by synthetic magnetic fields* (2014), https://arxiv.org/abs/1407.3486 .

[4] J. D. Bodyfelt et al., *Flat Bands Under Correlated Perturbations* (2014), https://arxiv.org/abs/1407.8345 .

[5] G. Gligorić, D. Leykam, A. Maluckov, *Influence of different disorder types on Aharonov-Bohm caging in the diamond chain* (2019 preprint; 2020 journal), https://arxiv.org/abs/1909.07055 .

[6] A. Ahmed et al., *Flat-band-based multifractality in the all-band-flat diamond chain* (2022), https://arxiv.org/abs/2205.02859 .

[7] A. Ahmed, N. Roy, A. Sharma, *Interplay of many-body interactions and quasiperiodic disorder in the all-bands-flat diamond chain* (2023), https://arxiv.org/abs/2303.17633 .
