# Complete continuity locus and sharp boundary jumps of the Pan–Liu–Lu–Draayer multipartite entropy measure
## Finding
For every integer \(N\ge3\), write
\[
A(\psi)=\frac{1}{N}\sum_{i=1}^N S(\rho_i),
\]
where \(S\) is the base-two von Neumann entropy of the one-qubit reduced state \(\rho_i\). Pan, Liu, Lu, and Draayer define their Eq. (9) measure \(\eta_N\) to equal \(A(\psi)\) when every nontrivial bipartition has nonzero partial entropy, and to equal zero otherwise.

On the pure-state space, \(\eta_N\) is continuous exactly at genuinely multipartite-entangled states and fully separable states. It is discontinuous at every partially entangled state, meaning every pure state that is product across at least one nontrivial bipartition but is not fully separable. If \(|\phi\rangle\) is such a state, then along every sequence of genuine states \(|\psi_m\rangle\to|\phi\rangle\),
\[
\eta_N(\psi_m)\longrightarrow A(\phi)>0,
\]
while \(\eta_N(\phi)=0\). The genuine-side jump therefore equals \(A(\phi)\).

The largest possible jump is
\[
\max_{\phi\text{ partially entangled}}A(\phi)=
\begin{cases}
\frac{2}{3},&N=3,\\
1,&N\ge4.
\end{cases}
\]
Hence Eq. (9) has full-scale unit discontinuities from \(N=4\) onward.

## Assumptions and scope
The domain is the normalized pure-state space of \(N\) qubits, modulo global phase, with its usual finite-dimensional topology (equivalently the topology induced by trace distance of the associated rank-one density matrices). A state is called genuine when it is nonproduct across every nontrivial bipartition; it is partially entangled here when it is product across at least one bipartition but not fully separable. These are the pure-state notions used by the source's factorization criterion.

The statement concerns the literal piecewise definition in Eq. (9). It does not claim a discontinuity for later continuous genuine-multipartite measures, and it does not by itself prove or disprove any separate LOCC-monotonicity assertion.

## Proof
Let \(\mathcal B\) be the union, over all nontrivial bipartitions \(A|A^c\), of the pure states that factor across that cut, and let \(\mathcal G\) be its complement. For a fixed cut, product states are exactly those whose coefficient-matrix flattening has rank one. They are therefore the common zero set of its \(2\times2\) minors, hence a closed proper algebraic subset with empty interior. There are finitely many cuts, so \(\mathcal B\) is closed with empty interior and \(\mathcal G\) is open and dense.

The function \(A\) is continuous because partial trace is continuous in finite dimension and von Neumann entropy is continuous on the compact qubit state space. The source definition can therefore be written exactly as
\[
\eta_N(\psi)=
\begin{cases}
A(\psi),&\psi\in\mathcal G,\\
0,&\psi\in\mathcal B.
\end{cases}
\]
At a genuine state, openness of \(\mathcal G\) makes \(\eta_N=A\) on a neighborhood, hence \(\eta_N\) is continuous there.

For a fully separable pure state \(\phi\), every one-qubit reduction is pure, so \(A(\phi)=0\). For any nearby pure state \(\psi\), one always has \(0\le\eta_N(\psi)\le A(\psi)\). Continuity of \(A\) gives \(A(\psi)\to0\), hence \(\eta_N(\psi)\to0=\eta_N(\phi)\). Thus \(\eta_N\) is continuous at every fully separable state.

Conversely, if \(\phi\in\mathcal B\) is not fully separable, then \(A(\phi)>0\). Indeed, \(A(\phi)=0\) would make every one-qubit reduced state pure; successively factoring off those pure one-qubit marginals would force \(|\phi\rangle\) to be fully separable. Since \(\mathcal G\) is dense, choose \(\psi_m\in\mathcal G\) with \(\psi_m\to\phi\). Then \(\eta_N(\psi_m)=A(\psi_m)\to A(\phi)>0\), whereas \(\eta_N(\phi)=0\). This proves both discontinuity and the exact genuine-side jump.

For \(N=3\), a partially entangled pure state factors as one pure qubit times a two-qubit pure state. If the latter has single-qubit entropy \(s\le1\), then its two one-qubit entropies are both \(s\), while the isolated qubit contributes zero, so \(A=2s/3\le2/3\). A Bell pair tensored with a pure qubit attains \(2/3\).

For \(N\ge4\), the universal entropy bound gives \(A\le1\). The biseparable state
\[
|\Phi_N\rangle=|\mathrm{Bell}\rangle_{12}\otimes|\mathrm{GHZ}_{N-2}\rangle_{3\ldots N}
\]
has every one-qubit reduced state maximally mixed, so \(A(\Phi_N)=1\) while \(\eta_N(\Phi_N)=0\). Thus the maximum jump is exactly one.

For a concrete three-qubit approach already contained in the source's three-term family, put
\[
|\psi_\varepsilon\rangle=\sqrt{\frac{1-\varepsilon}{2}}|000\rangle+\sqrt{\frac{1-\varepsilon}{2}}|110\rangle+\sqrt{\varepsilon}|101\rangle,
\qquad 0<\varepsilon<1.
\]
The source's Eq. (13) shows this is genuine when all three coefficients are nonzero. Its one-qubit entropies give
\[
\eta_3(\psi_\varepsilon)=\frac{h_2(\varepsilon)+2h_2((1-\varepsilon)/2)}{3}\longrightarrow\frac{2}{3},
\]
whereas the limit is a Bell pair tensored with \(|0\rangle\) and therefore has \(\eta_3=0\).

## Verification
The proof uses only finite-dimensional topology, Schmidt-rank algebra, and one-qubit entropy bounds. The critical source premise was checked in the full text: Eq. (9) explicitly assigns the average one-particle entropy only when every listed partial entropy is nonzero and assigns zero otherwise; the surrounding text identifies a zero partial entropy with failure of genuine multipartite entanglement. The source's Eq. (13) also supplies the reduced spectra for the explicit three-term family used above.

The density step is not an experiment: each fixed-cut product set is a proper algebraic zero set, so its finite union has empty interior. The maximal-jump bounds are exact: \(2/3\) follows from the Schmidt equality of the two qubits in a pure two-qubit factor, while the \(N\ge4\) witness has all one-qubit entropies exactly one.

## Relationship to prior work
Pan–Liu–Lu–Draayer introduce the piecewise measure and discuss separability, local-unitary invariance, and LOCC behavior, but the inspected full text does not state its continuity locus or quantify its boundary jumps. Their own three-term example supplies a particularly transparent path to the \(2/3\) discontinuity.

Cao–Liu–Bai later compare multipartite pure-state entanglement measures; its indexed record is directly relevant to the same measure family and is classified primarily under MSC 81P15. No accessible full text was located in the present check, so that paper remains a residual literature risk rather than evidence of noncoverage. Recent GME literature explicitly treats continuity as a desirable property and constructs continuous alternatives, but the inspected abstract/review material does not give the classification or sharp jump formula proved here.

## Limitations
This result is about continuity of the literal pure-state functional in Eq. (9). It does not analyze mixed-state extensions, does not assert that discontinuity alone violates an LOCC axiom, and does not compare numerical state orderings away from the biseparable boundary. The originality assessment remains subject to the possibility of an unindexed note or inaccessible full text that observed the same discontinuity.

## References
1. F. Pan, D. Liu, G. Lu, J. P. Draayer, “A simple entanglement measure for multipartite pure states,” arXiv:quant-ph/0405133; DOI:10.1023/B:IJTP.0000048612.08077.8e. First arXiv public date: 2004-05-22.
2. W. Cao, D. Liu, H. Bai, “A comparison of the entanglement measures for multipartite pure states,” International Journal of Theoretical Physics (2007), zbMATH record 1107.81302; indexed primary MSC 81P15.
3. K.-K. Wang, Z.-W. Wei, S.-M. Fei, “Genuine Multipartite Entanglement Measure Based on \(\alpha\)-concurrence,” arXiv:2505.05998 (2025), whose abstract explicitly records continuity for its different GME construction.
