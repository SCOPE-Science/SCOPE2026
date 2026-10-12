# A biseparable three-qubit state exposes nonconvexity of the mixed \(R_2\) construction

## Finding

For the mixed-state construction of Ichikawa, Huber, Krammer, and Hiesmayr (arXiv:0911.4245), specialize to three qubits and \(m=2\), so \(R_2(\rho)=[\xi_{A|BC}(\rho)\xi_{B|AC}(\rho)\xi_{C|AB}(\rho)]^{1/3}\), with each \(\xi\) defined by the separate convex roof in their Eq. (15). Define \(|\psi_{AB}\rangle=(|000\rangle+|110\rangle)/\sqrt2\), \(|\psi_{AC}\rangle=(|000\rangle+|101\rangle)/\sqrt2\), \(|\psi_{BC}\rangle=(|000\rangle+|011\rangle)/\sqrt2\), and \(\rho_\star=(|\psi_{AB}\rangle\langle\psi_{AB}|+|\psi_{AC}\rangle\langle\psi_{AC}|+|\psi_{BC}\rangle\langle\psi_{BC}|)/3\). Each pure component is product across one bipartition and hence has \(R_2=0\). Yet \(\rho_\star\) is permutation symmetric and its partial transpose across any one-qubit cut has spectrum \(\{1/3-\sqrt2/6,\,1/3+\sqrt2/6,\,-\sqrt2/6,\,\sqrt2/6,\,0,\,0,\,1/6,\,1/6\}\). Thus it is entangled across every fixed bipartition. Because each fixed-partition convex roof \(\xi_{X|YZ}\) is nonnegative and vanishes exactly on states separable across that cut, all three factors are strictly positive and \(R_2(\rho_\star)>0\). Therefore the mixed-state \(R_2\) is not convex: \(R_2(\rho_\star)>\frac13[R_2(\psi_{AB})+R_2(\psi_{AC})+R_2(\psi_{BC})]=0\). In particular, \(\rho_\star\) is biseparable by its displayed ensemble but receives positive \(R_2\), so this partitionwise-geometric mixed extension does not vanish on all biseparable mixed states in the standard convex-hull sense.

## Assumptions and scope

The construction is exactly the mixed-state \(R_m\) family defined in arXiv:0911.4245, specialized to three qubits and \(m=2\). There are three two-block partitions,
\[
\Gamma_A=A|BC,\qquad \Gamma_B=B|AC,\qquad \Gamma_C=C|AB,
\]
so the source definition becomes
\[
R_2(\rho)=\left(\xi_{\Gamma_A}(\rho)\,\xi_{\Gamma_B}(\rho)\,\xi_{\Gamma_C}(\rho)\right)^{1/3}.
\]
For each fixed partition \(\Gamma\), the source first defines a nonnegative pure-state quantity \(\xi_\Gamma(\psi)\) and then takes its convex roof,
\[
\xi_\Gamma(\rho)=\inf_{\rho=\sum_jp_j|\phi_j\rangle\langle\phi_j|}\sum_jp_j\xi_\Gamma(\phi_j).
\]
The claim concerns convexity and the zero set of the resulting \(R_2\). It does not claim that \(R_2\) fails average LOCC monotonicity, nor does it evaluate the positive number \(R_2(\rho_\star)\) exactly.

A mixed state is called biseparable here in the standard convex-hull sense: it is a convex combination of pure states that may be separable across different bipartitions. The state \(\rho_\star\) is biseparable by construction even though it is entangled across each fixed bipartition.

## Proof

Set
\[
|\psi_{AB}\rangle=\frac{|000\rangle+|110\rangle}{\sqrt2},\qquad
|\psi_{AC}\rangle=\frac{|000\rangle+|101\rangle}{\sqrt2},\qquad
|\psi_{BC}\rangle=\frac{|000\rangle+|011\rangle}{\sqrt2}.
\]
The first state is a Bell pair on \(AB\) tensored with \(|0\rangle_C\), hence is product across \(C|AB\). Therefore \(\xi_{\Gamma_C}(\psi_{AB})=0\), and the geometric product defining \(R_2\) gives \(R_2(\psi_{AB})=0\). Cyclic permutation gives
\[
R_2(\psi_{AB})=R_2(\psi_{AC})=R_2(\psi_{BC})=0.
\]
Now let
\[
\rho_\star=\frac13\left(
|\psi_{AB}\rangle\langle\psi_{AB}|+
|\psi_{AC}\rangle\langle\psi_{AC}|+
|\psi_{BC}\rangle\langle\psi_{BC}|
\right).
\]
In the computational basis \(|000\rangle,\ldots,|111\rangle\),
\[
\rho_\star=
\begin{pmatrix}
1/2&0&0&1/6&0&1/6&1/6&0\\
0&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0\\
1/6&0&0&1/6&0&0&0&0\\
0&0&0&0&0&0&0&0\\
1/6&0&0&0&0&1/6&0&0\\
1/6&0&0&0&0&0&1/6&0\\
0&0&0&0&0&0&0&0
\end{pmatrix}.
\]
The state is invariant under all permutations of the three qubits. Partial transposition on \(A\) produces, on the subspace spanned by \(|001\rangle,|010\rangle,|100\rangle\), the block
\[
\frac16\begin{pmatrix}0&0&1\\0&0&1\\1&1&0\end{pmatrix},
\]
whose eigenvalues are \(0\) and \(\pm\sqrt2/6\). The remaining eigenvalues are \(1/3\pm\sqrt2/6\), \(1/6\), \(1/6\), and \(0\). Hence
\[
\operatorname{spec}(\rho_\star^{T_A})=
\left\{\frac13-\frac{\sqrt2}6,\frac13+\frac{\sqrt2}6,-\frac{\sqrt2}6,
\frac{\sqrt2}6,0,0,\frac16,\frac16\right\}.
\]
The negative eigenvalue proves entanglement across \(A|BC\). Permutation symmetry gives the same conclusion across \(B|AC\) and \(C|AB\).

It remains to justify strict positivity of each fixed-cut convex roof. For a fixed bipartition \(\Gamma\), the source pure-state quantity \(\xi_\Gamma(\psi)\) is continuous, nonnegative, and zero exactly for pure states product across that cut. In finite dimension, its convex-roof infimum is attained: by Carathéodory one may restrict to ensembles of bounded cardinality, and the corresponding compact ensemble space has a continuous objective. If \(\xi_\Gamma(\rho)=0\), every positive-weight state in an optimal ensemble must have zero pure-state value, so \(\rho\) is separable across \(\Gamma\). Conversely a cut-separable decomposition gives zero. Thus
\[
\xi_\Gamma(\rho)=0\quad\Longleftrightarrow\quad \rho\text{ is separable across }\Gamma.
\]
Since \(\rho_\star\) is entangled across all three cuts, all three factors in \(R_2(\rho_\star)\) are strictly positive. Therefore
\[
R_2(\rho_\star)>0
=\frac13\left(R_2(\psi_{AB})+R_2(\psi_{AC})+R_2(\psi_{BC})\right),
\]
which is a strict violation of convexity. The same displayed ensemble simultaneously proves that \(\rho_\star\) is biseparable in the standard mixed-state sense.

## Verification

The bundled standard-library script `verify_r2_nonconvex.py` reconstructs the three projectors with exact rational arithmetic, forms \(\rho_\star\), verifies trace one and full qubit-permutation symmetry, performs each of the three partial transposes, and checks an exact eigenvector over \(\mathbb Q(\sqrt2)\) with eigenvalue \(-\sqrt2/6\). It also checks that each ensemble component factors across its stated bipartition. Running the embedded script returns `VERIFY_OK`.

The script certifies the explicit density matrix and NPT witnesses. Strict positivity of the convex roofs is proved analytically from the zero set and attainment of finite-dimensional convex roofs; no finite numerical experiment is used as a substitute for that argument.

## Relationship to prior work

Ichikawa, Huber, Krammer, and Hiesmayr define \(R_m\) for pure states as a geometric mean over partition measures and, for mixed states, first convex-roof each fixed-partition quantity \(\xi_\Gamma\) separately and then take their geometric mean. Their paper derives computable lower bounds and illustrates intermediate separability, but the inspected definition and examples do not analyze convexity of the final geometric combination or mixtures whose components are separable across different cuts.

The earlier Love et al. global-entanglement construction uses the same order of operations for its mixed extension: each fixed-cut factor is convex-roofed and the geometric mean is then formed. The present three-qubit example therefore isolates a general structural issue with this order of operations, without claiming anything about the correctness of the individual fixed-cut convex roofs.

Later geometric-mean GME work uses the opposite order for mixed states: form the geometric mean on pure states and then take one convex roof of the whole pure-state quantity. That construction automatically vanishes on convex mixtures of biseparable pure states and is therefore not implication-equivalent to the 2009 partitionwise-roof construction considered here.

## Limitations

The theorem is an explicit three-qubit counterexample to convexity of the mixed \(R_2\) definition and to vanishing on the convex hull of biseparable pure states. It does not compute \(R_2(\rho_\star)\) numerically, classify all states on which the construction is nonconvex, or assert failure of average LOCC monotonicity. A residual literature risk remains that an obscure or poorly indexed note may have observed the same three-state obstruction; targeted semantic, exact-phrase, citation-chain, and source-title searches located no such statement.

## References

1. T. Ichikawa, M. Huber, P. Krammer, and B. C. Hiesmayr, *Mixed State Entanglement Measures for Intermediate Separability*, arXiv:0911.4245v1 (22 November 2009), DOI 10.1142/S0219749910006526.
2. P. J. Love, A. Maassen van den Brink, A. Yu. Smirnov, M. H. S. Amin, M. Grajcar, E. Il'ichev, A. Izmalkov, and A. M. Zagoskin, *A characterization of global entanglement*, arXiv:quant-ph/0602143.
3. Y. Li and J. Shang, *Geometric mean of bipartite concurrences as a genuine multipartite entanglement measure*, arXiv:2112.10509, Phys. Rev. Research 4, 023059 (2022).
4. C. Palazuelos and J. I. de Vicente, *Genuine multipartite entanglement of quantum states in the multiple-copy scenario*, arXiv:2201.08694, Quantum 6, 735 (2022).
