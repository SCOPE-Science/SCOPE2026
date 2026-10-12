# Correlation-blind short-time purity laws for fluctuating quantum networks
## Finding
Consider the rapid-switching model in which the one-excitation Hilbert space has basis \(|1\rangle,\ldots,|N\rangle\), every possible edge \(e=\{i,j\}\) has exchange operator
\[
V_e=|i\rangle\langle j|+|j\rangle\langle i|,
\]
and the Bernoulli edge-indicator covariance is \(C\). Retain the order-\(\Delta t\) effective generator derived in arXiv:2610.03194v1,
\[
\mathcal L^{(1)}(\rho)=-i[\bar H,\rho]-\frac{J^2\Delta t}{2}\sum_{e,f}C_{ef}[V_e,[V_f,\rho]].
\]
For a pure initial state \(|\psi\rangle\), define
\[
(K_\psi)_{ef}=\frac12\langle\psi|\{V_e,V_f\}|\psi\rangle-\langle V_e\rangle_\psi\langle V_f\rangle_\psi.
\]
Then its initial purity-loss rate under \(\mathcal L^{(1)}\) is
\[
R_\psi\equiv-\left.\frac{d}{dt}\operatorname{Tr}(\rho_t^2)\right|_{t=0}
=2J^2\Delta t\,\operatorname{Tr}(C K_\psi).
\]
This immediately yields two correlation-blind laws.

For every localized vertex state \(|v\rangle\),
\[
R_v=2J^2\Delta t\sum_{e\ni v}C_{ee}
=2J^2\Delta t\sum_{e\ni v}p_e(1-p_e).
\]
Thus the complete collection of localized initial purity slopes is independent of every off-diagonal covariance \(C_{ef}\) with \(e\ne f\).

For a Haar-uniform pure state in the \(N\)-dimensional one-excitation manifold,
\[
\mathbb E_\psi R_\psi
=\frac{4J^2\Delta t}{N+1}\operatorname{Tr}C
=\frac{4J^2\Delta t}{N+1}\sum_e p_e(1-p_e).
\]
Hence the Haar-averaged initial purity slope is also completely blind to covariance eigenvectors and to all edge-edge correlations. If every edge has the same marginal \(p_e=\xi\), then
\[
R_v=2J^2\Delta t(N-1)\xi(1-\xi)
\]
for every vertex and
\[
\mathbb E_\psi R_\psi
=\frac{2J^2\Delta t\,N(N-1)}{N+1}\xi(1-\xi).
\]

## Assumptions and scope
The statement concerns the leading rapid-switching effective generator displayed above, not the exact discrete random-unitary dynamics at finite switching interval. The edge set is the complete set of unordered pairs used by the source model, although the two formulas remain valid after restricting to any fixed allowed edge set and replacing incident-edge sums accordingly. The edge indicators may be arbitrarily correlated so long as their covariance matrix is physically realizable. The localized formula applies to computational-basis one-excitation states; the second formula averages over Haar-random pure states in that same one-excitation Hilbert space.

The conclusion is an identifiability boundary for initial purity slopes. It does not imply that fidelity, sector-resolved coherence, the full Lindblad generator, or finite-time purity is correlation-blind. In particular, the source explicitly shows that covariance eigenvectors can change fidelity and coherence, and it proves equal finite-time purity only for its special global/community pair.

## Proof
For a pure state \(\rho=|\psi\rangle\langle\psi|\), the Hamiltonian commutator does not contribute to \(\frac{d}{dt}\operatorname{Tr}(\rho^2)\). Using symmetry of \(C\) and cyclicity of trace,
\[
2\operatorname{Tr}\!\left[\rho\left(-\frac{J^2\Delta t}{2}\sum_{e,f}C_{ef}[V_e,[V_f,\rho]]\right)\right]
=-2J^2\Delta t\sum_{e,f}C_{ef}(K_\psi)_{ef}.
\]
Negating this derivative gives the stated formula for \(R_\psi\).

For \(|\psi\rangle=|v\rangle\), every \(\langle V_e\rangle_v\) vanishes. Also
\[
V_{ij}^2=|i\rangle\langle i|+|j\rangle\langle j|,
\]
so \(\langle v|V_e^2|v\rangle=1\) exactly when \(e\) is incident to \(v\). If \(e\ne f\), the diagonal matrix element \(\langle v|\{V_e,V_f\}|v\rangle\) vanishes. Therefore \(K_v\) is diagonal with a \(1\) precisely on incident edges, which proves the localized law.

For Haar-uniform \(|\psi\rangle\in\mathbb C^N\), the standard second-moment identity gives, for traceless Hermitian \(A,B\),
\[
\mathbb E_\psi[\langle A\rangle_\psi\langle B\rangle_\psi]
=\frac{\operatorname{Tr}(AB)}{N(N+1)},
\qquad
\mathbb E_\psi\!\left[\frac12\langle\{A,B\}\rangle_\psi\right]
=\frac{\operatorname{Tr}(AB)}{N}.
\]
Hence
\[
\mathbb E_\psi(K_\psi)_{ef}=\frac{\operatorname{Tr}(V_eV_f)}{N+1}.
\]
The exchange operators are Hilbert--Schmidt orthogonal:
\[
\operatorname{Tr}(V_eV_f)=2\delta_{ef}.
\]
Thus \(\mathbb E_\psi K_\psi=\frac{2}{N+1}I\), and substituting into the general rate formula proves the Haar law. Finally, Bernoulli indicators satisfy \(C_{ee}=p_e(1-p_e)\); for homogeneous marginals there are \(N-1\) incident edges at a vertex and \(N(N-1)/2\) total edges, giving the displayed closed forms.

## Verification
A standalone exact-arithmetic checker verifies the Hilbert--Schmidt Gram matrix \(\operatorname{Tr}(V_eV_f)=2\delta_{ef}\), the localized covariance matrices \(K_v\), and the homogeneous simplifications for \(2\le N\le 8\). These finite checks corroborate the algebraic proof; they are not used as evidence for the all-\(N\) quantifiers.

The critical nonstandard premise is the source's rapid-switching effective generator. The source derives it by averaging independently redrawn graph Hamiltonians and identifies the edge-indicator covariance as the coefficient matrix of the double-commutator dissipator. All further steps above are direct finite-dimensional trace identities.

## Relationship to prior work
Nourmandipour and Mancini (arXiv:2610.03194v1) derive the covariance-controlled Lindbladian and emphasize that covariance eigenvectors encode dissipative geometry. They exhibit a global and a community ensemble with identical marginals and covariance spectra whose fidelity and sector coherence differ, while their total purity happens to coincide. The present result is different: it proves, for arbitrary physically realizable edge covariance, that two broad classes of *initial-slope* purity measurements erase all off-diagonal covariance information. It therefore explains a robust short-time reason that purity can fail to reveal fluctuation geometry without extending the source's special finite-time equality to general ensembles.

Zanardi and Lidar, Phys. Rev. A 70, 012315 (2004), develop general channel-purity and Haar-averaging machinery. That general framework is prior art for the Haar technique and is not claimed as new here. Yang, Xu, and del Campo, Phys. Rev. Research 6, 023229 (2024), study short-time purity/decoherence rates averaged over Gaussian and Ginibre random Lindblad operators; their random-matrix ensembles do not contain the edge-covariance geometry or the localized-vertex no-go law above. Farooq and Mancini, arXiv:1404.0508v1, study information spreading in random quantum networks with randomly added edges, but not the covariance-resolved rapid-switching generator or the present correlation-blind slope identities.

## Limitations
The result is restricted to the one-excitation exchange model and the order-\(\Delta t\) effective generator. Higher orders in the switching interval can depend on moments beyond the covariance and are not controlled here. The Haar formula is an ensemble average, not a concentration theorem. The localized formula says nothing about coherent superpositions, for which off-diagonal covariance can already enter the initial purity slope through \(K_\psi\). No claim is made that purity is generally unable to distinguish topology correlations at later times; the source itself shows a special exact equal-purity pair, not a universal theorem.

The novelty comparison is necessarily subject to indexing lag because the anchor is very recent. General channel-purity identities and random-Lindblad decoherence-rate formulas are older and explicitly credited; the claimed contribution is the topology-specific correlation-blind laws and their identifiability interpretation.

## References
1. A. Nourmandipour and S. Mancini, *Emergent Dissipation from Fluctuating Quantum-Network Topology*, arXiv:2610.03194v1 (2026).
2. P. Zanardi and D. A. Lidar, *Purity and state fidelity of quantum channels*, Phys. Rev. A 70, 012315 (2004), doi:10.1103/PhysRevA.70.012315.
3. Y. Yang, Z. Xu, and A. del Campo, *Decoherence rate in random Lindblad dynamics*, Phys. Rev. Research 6, 023229 (2024), arXiv:2402.04705v3, doi:10.1103/PhysRevResearch.6.023229.
4. U. Farooq and S. Mancini, *Information Dissipation in Random Quantum Networks*, arXiv:1404.0508v1 (2014), doi:10.1142/S1230161214500048.
