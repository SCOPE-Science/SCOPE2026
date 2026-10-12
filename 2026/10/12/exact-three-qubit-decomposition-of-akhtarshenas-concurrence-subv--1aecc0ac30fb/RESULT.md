# Exact three-qubit decomposition of Akhtarshenas concurrence subvectors
## Finding
For every pure three-qubit state \(|\psi\rangle\), denote by \(A_{ij}\) the norm of the concurrence subvector associated with qubits \(i,j\) in Akhtarshenas's construction, by \(c_{ij}=C_W(\rho_{ij})\) the Wootters concurrence of the reduced state \(\rho_{ij}\), by \(\tau\) the Coffman-Kundu-Wootters three-tangle, and by \(Q\) the Meyer-Wallach global entanglement. Then
\[
A_{12}^2=c_{12}^2+\frac{\tau}{2},\qquad
A_{13}^2=c_{13}^2+\frac{\tau}{2},\qquad
A_{23}^2=c_{23}^2+\frac{\tau}{2}.
\]
Therefore, if \(A_{\mathrm{tot}}^2=A_{12}^2+A_{13}^2+A_{23}^2\),
\[
A_{\mathrm{tot}}^2
=c_{12}^2+c_{13}^2+c_{23}^2+\frac{3\tau}{2}
=\frac{3Q}{2}.
\]
The pair-subvector norm consequently contains a fixed share of genuine tripartite entanglement whenever \(\tau>0\); it coincides with the ordinary reduced-pair concurrence exactly when \(\tau=0\).

## Assumptions and scope
The Hilbert space is \((\mathbb C^2)^{\otimes 3}\), the global state is pure, and all reduced states use the standard partial trace. The Wootters concurrence is the usual two-qubit convex-roof concurrence. The three-tangle is normalized by the CKW identities
\[
T_1=c_{12}^2+c_{13}^2+\tau,
\quad
T_2=c_{12}^2+c_{23}^2+\tau,
\quad
T_3=c_{13}^2+c_{23}^2+\tau,
\]
where \(T_i=2(1-\operatorname{Tr}\rho_i^2)\). The Meyer-Wallach normalization is
\[
Q=\frac13(T_1+T_2+T_3).
\]
No mixed-state convex-roof extension and no claim for four or more parties is made.

## Proof
For qubits, each local \(SO(2)\) factor in Akhtarshenas's Eq. (31) has one antisymmetric generator. Expanding that equation for the pair \(i,j\), or equivalently tracing the untouched qubit first, gives
\[
A_{ij}^2=\operatorname{Tr}\!\left(\rho_{ij}\widetilde{\rho}_{ij}\right),
\]
where
\[
\widetilde{\rho}_{ij}
=(\sigma_y\otimes\sigma_y)\rho_{ij}^*(\sigma_y\otimes\sigma_y).
\]
For any normalized two-qubit state \(\omega\), the spin-flip identity gives
\[
\operatorname{Tr}(\omega\widetilde{\omega})
=1-\operatorname{Tr}(\omega_i^2)-\operatorname{Tr}(\omega_j^2)
 +\operatorname{Tr}(\omega^2).
\]
Taking \(\omega=\rho_{ij}\) and using purity of the global state,
\[
\operatorname{Tr}(\rho_{ij}^2)=\operatorname{Tr}(\rho_k^2)
\]
for the complementary qubit \(k\). Hence
\[
A_{ij}^2
=\frac12(T_i+T_j-T_k).
\]
Substituting the three CKW identities cancels the two concurrences involving the complementary qubit and leaves
\[
A_{ij}^2=c_{ij}^2+\frac{\tau}{2}.
\]
Summing the three pair identities yields
\[
A_{\mathrm{tot}}^2
=c_{12}^2+c_{13}^2+c_{23}^2+\frac{3\tau}{2}.
\]
Alternatively, summing \(A_{ij}^2=(T_i+T_j-T_k)/2\) directly gives
\[
A_{\mathrm{tot}}^2=\frac12(T_1+T_2+T_3)=\frac{3Q}{2}.
\]
This completes the proof.

## Verification
The derivation is algebraic and dimension-finite; no enumeration or numerical extrapolation is used. Three source examples provide independent boundary checks. For the GHZ state, \(c_{ij}=0\) and \(\tau=1\), so \(A_{ij}=1/\sqrt2\), exactly as reported by Akhtarshenas. For the three-qubit W state, \(\tau=0\) and \(c_{ij}=2/3\), giving \(A_{ij}=2/3\). For a Bell pair tensored with a pure third qubit, \(\tau=0\), one reduced-pair concurrence is \(1\), and the other two vanish, again matching the source examples.

A separate floating-point sanity check on randomly generated normalized three-qubit amplitudes verified
\[
\operatorname{Tr}(\rho_{ij}\widetilde{\rho}_{ij})
=1-\operatorname{Tr}\rho_i^2-\operatorname{Tr}\rho_j^2+\operatorname{Tr}\rho_k^2
\]
to machine precision for all three pairs. This numerical check is not used as proof.

## Relationship to prior work
Akhtarshenas defines the multipartite concurrence vector as a direct sum of pair-labelled subvectors and proposes the norm of each subvector as the entanglement contribution of the corresponding pair. The paper's GHZ example already shows a nonzero pair-labelled value even though every reduced pair has zero ordinary concurrence, but it does not identify the discrepancy with the three-tangle.

Amico, Fazio, Osterloh, and Vedral later note qualitatively that the multipartite concurrence-vector entries are not the ordinary reduced-pair concurrences. That review does not give the exact decomposition above. CKW supplies the one-tangle decomposition into two reduced-pair concurrences and the three-tangle. Concurrence-of-assistance literature gives the neighboring identity \(C_a^2=c^2+\tau\) for reductions of pure three-qubit states. These results make the present identity natural, but the inspected sources do not identify Akhtarshenas's pair-subvector norm with \(c^2+\tau/2\) or identify the total norm with \(3Q/2\).

A later concurrence-vector treatment by Bernal, Casas, and Moreno organizes concurrences of bipartitions via coefficient-matrix minors and cites Akhtarshenas, but it does not state the pair-subvector/three-tangle decomposition above.

## Limitations
The result is specific to pure three-qubit states. It does not show that the multipartite concurrence-vector construction is an LOCC monotone in arbitrary dimensions, does not address its proposed mixed-state extension, and does not provide an analogous decomposition for four or more qubits. The closest originality risk is that the formula can be assembled from standard spin-flip and CKW identities once the Akhtarshenas subvector is recognized as \(\operatorname{Tr}(\rho_{ij}\widetilde{\rho}_{ij})^0.5\); a targeted literature comparison found the qualitative warning but not this exact assembly.

## References
1. S. J. Akhtarshenas, “Concurrence Vectors in Arbitrary Multipartite Quantum Systems,” arXiv:quant-ph/0311166, first public 2003-11-25; J. Phys. A 38 (2005), 6777–6784, doi:10.1088/0305-4470/38/30/011.
2. V. Coffman, J. Kundu, and W. K. Wootters, “Distributed Entanglement,” arXiv:quant-ph/9907047; Phys. Rev. A 61, 052306 (2000), doi:10.1103/PhysRevA.61.052306.
3. D. A. Meyer and N. R. Wallach, “Global entanglement in multiparticle systems,” arXiv:quant-ph/0108104; J. Math. Phys. 43, 4273–4278 (2002), doi:10.1063/1.1497700.
4. L. Amico, R. Fazio, A. Osterloh, and V. Vedral, “Entanglement in many-body systems,” Rev. Mod. Phys. 80, 517–576 (2008), doi:10.1103/RevModPhys.80.517.
5. A. Bernal, J. A. Casas, and J. M. Moreno, “Entanglement and entropy in multipartite systems: a useful approach,” Quantum Inf. Process. 23 (2024), doi:10.1007/s11128-023-04246-0.
6. X.-J. Ren, Z. Wang, X. Zhou, Z.-W. Zhou, and L. He, “Three-tangle of assistance,” Phys. Rev. A 81, 042306 (2010), doi:10.1103/PhysRevA.81.042306.
