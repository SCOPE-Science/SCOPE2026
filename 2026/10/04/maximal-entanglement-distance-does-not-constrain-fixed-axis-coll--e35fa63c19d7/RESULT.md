# Maximal entanglement distance does not constrain fixed-axis collective QFI
## Finding
For pure qubit states, maximal Entanglement Distance does not by itself constrain the quantum Fisher information for a prescribed common phase generator. With \(J_z=\tfrac12\sum_{i=1}^N Z_i\), every even \(N\ge2\) has states with the same maximal value \(E_{\mathrm D}=N\) but endpoint QFI values \(F_Q=0\) and \(F_Q=N^2\): a tensor product of singlets gives the first and an \(N\)-qubit GHZ state gives the second. Already for \(N=2\), the maximally entangled family \((I\otimes R_y(\theta))|\Phi^+\rangle\) has \(E_{\mathrm D}=2\) for all \(\theta\) while \(F_Q[J_z]=2(1+\cos\theta)\), so the full allowed interval \([0,4]\) occurs at one fixed maximal Entanglement Distance. Thus the trace-over-local-directions QFI/Entanglement-Distance identity should not be read as a generator-specific certificate of Heisenberg scaling for a prescribed collective sensing Hamiltonian.

## Assumptions and scope
Consider pure states of \\(N\\) qubits. Entanglement Distance is normalized as in Capra, de Simone and Franzosi,
\\[
E_{{\\mathrm D}}(|\\psi\\rangle)=2\\sum_{{i=1}}^N\\left(1-\\operatorname{{Tr}}\\rho_i^2\\right),
\\]
where \\(\\rho_i\\) is the one-qubit reduced state. The sensing generator is fixed to the common-axis collective observable
\\[
J_z=\\frac12\\sum_{{i=1}}^N Z_i.
\\]
For a pure probe state, the single-parameter quantum Fisher information is \\(F_Q[|\\psi\\rangle,J_z]=4\\operatorname{{Var}}_\\psi(J_z)\\). The all-even-\\(N\\) endpoint statement below assumes \\(N\\ge2\\) is even. The two-qubit interval statement is exact for \\(0\\le\\theta\\le\\pi\\).

The claim concerns a *prescribed collective generator*. It does not dispute the source paper's trace identity obtained by summing local-generator variances, nor its equivalence between Entanglement Distance and summed one-body linear entropies.

## Proof
For a pure qubit state, \\(E_{{\\mathrm D}}=N\\) exactly when every one-qubit marginal is maximally mixed, because each summand obeys \\(2(1-\\operatorname{{Tr}}\\rho_i^2)\\le1\\), with equality precisely at \\(\\rho_i=I/2\\).

First take \\(N=2\\) and
\\[
|\\psi_\\theta\\rangle=(I\\otimes R_y(\\theta))|\\Phi^+\\rangle,
\\qquad
|\\Phi^+\\rangle=\\frac{|00\\rangle+|11\\rangle}{\\sqrt2}.
\\]
Local unitaries preserve the spectra of the one-qubit marginals, so both marginals remain \\(I/2\\), hence \\(E_{{\\mathrm D}}(|\\psi_\\theta\\rangle)=2\\) for every \\(\\theta\\). Also \\(\\langle J_z\\rangle=0\\), while
\\[
J_z^2=\\frac{I+Z\\otimes Z}{2}.
\\]
Using \\(R_y(\\theta)^\\dagger ZR_y(\\theta)=\\cos\\theta\\,Z-\\sin\\theta\\,X\\) and the Bell-state correlations \\(\\langle\\Phi^+|Z\\otimes Z|\\Phi^+\\rangle=1\\) and \\(\\langle\\Phi^+|Z\\otimes X|\\Phi^+\\rangle=0\\), one obtains
\\[
\\langle Z\\otimes Z\\rangle_{{\\psi_\\theta}}=\\cos\\theta,
\\qquad
F_Q[|\\psi_\\theta\\rangle,J_z]=4\\langle J_z^2\\rangle=2(1+\\cos\\theta).
\\]
As \\(\\theta\\) runs from \\(0\\) to \\(\\pi\\), this continuously covers \\([0,4]\\), the entire pure-state QFI range for this two-qubit generator.

Now let \\(N\\) be even. For the state \\(|\\Psi^-\\rangle^{\\otimes N/2}\\), every one-qubit marginal is \\(I/2\\), so \\(E_{{\\mathrm D}}=N\\). Each singlet is annihilated by the pair generator \\(Z_a+Z_b\\), hence \\(J_z|\\Psi^-\\rangle^{\\otimes N/2}=0\\) and therefore \\(F_Q=0\\).

For the GHZ state
\\[
|\\mathrm{{GHZ}}_N\\rangle=\\frac{|0\\rangle^{\\otimes N}+|1\\rangle^{\\otimes N}}{\\sqrt2},
\\]
every one-qubit marginal is again \\(I/2\\), so \\(E_{{\\mathrm D}}=N\\). The two components are \\(J_z\\)-eigenvectors with eigenvalues \\(N/2\\) and \\(-N/2\\). Thus \\(\\langle J_z\\rangle=0\\), \\(\\operatorname{{Var}}(J_z)=N^2/4\\), and \\(F_Q=N^2\\).

Consequently, the scalar Entanglement Distance can be maximal while fixed-axis collective QFI ranges from zero to the Heisenberg endpoint. The structural reason is that Entanglement Distance is determined by the one-body marginals, whereas \\(\\operatorname{{Var}}(J_z)\\) also contains the intersite covariance terms \\(\\langle Z_iZ_j\\rangle-\\langle Z_i\\rangle\\langle Z_j\\rangle\\).

## Verification
The proof above is algebraic. The accompanying `verify.py` independently constructs the two-qubit family and the even-\\(N\\) endpoint examples, checks normalization and one-qubit purities, and evaluates \\(4\\operatorname{{Var}}(J_z)\\) numerically for representative parameters. Those finite calculations are supplementary checks; they are not used as a proof of the continuous or all-even-\\(N\\) statements.

## Relationship to prior work
Capra, de Simone and Franzosi (arXiv:2609.11720v1, first public 2026-09-10) identify Entanglement Distance with summed one-body linear entropy and with a trace over local Fubini--Study/QFI directions. Their statement is a summed, direction-agnostic identity. The present result isolates a sharp boundary of that interpretation for a *fixed common sensing generator*: at one maximal Entanglement Distance, the full two-qubit fixed-\\(J_z\\) QFI interval occurs, and for every even \\(N\\) both \\(0\\) and \\(N^2\\) occur.

Tóth and Apellaniz, *Quantum metrology from a quantum information science perspective*, J. Phys. A 47 (2014) 424006, DOI 10.1088/1751-8113/47/42/424006, reviews the pure-state identity \\(F_Q=4\\operatorname{{Var}}\\) and the broader fact that entanglement alone does not fix usefulness for a particular linear interferometer. Boixo and Monras, *Operational Interpretation for Global Multipartite Entanglement*, Phys. Rev. Lett. 100 (2008) 100503, DOI 10.1103/PhysRevLett.100.100503, gives a different operational connection between Meyer--Wallach entanglement and estimation of low-noise local depolarization strength. These broader precedents prevent interpreting the present statement as the general observation that entanglement need not help every metrological task; the specific contribution is the exact fixed-generator range and endpoint obstruction tied to the recent Entanglement-Distance/QFI trace interpretation.

Database and literature searches for aliases such as maximal Meyer--Wallach entanglement, identical maximally mixed one-body marginals, Bell/GHZ comparisons, and fixed collective-generator QFI did not reveal this exact interval statement or its all-even-\\(N\\) endpoint formulation.

## Limitations
The theorem is restricted to pure qubit states and to the prescribed common generator \\(J_z\\); it does not characterize arbitrary mixed states, arbitrary local generators, or multiparameter estimation. It does not invalidate the exact Entanglement-Distance/Fubini--Study trace identity. It instead shows that the trace quantity loses generator-specific covariance information.

The primary arXiv abstract and detailed section-level text containing the Entanglement-Distance and trace/QFI formulas were inspected, but the primary PDF was not available through the accessible source path during this check. This leaves a residual literature-comparison risk that a nuance or closely related caveat in the full manuscript was not visible in the inspected material. No searched source supplied the exact theorem above.

## References
1. L. Capra, L. de Simone, R. Franzosi, *A Geometric Theory of Quantum Entanglement*, arXiv:2609.11720v1 (2026).
2. G. Tóth, I. Apellaniz, *Quantum metrology from a quantum information science perspective*, J. Phys. A 47 (2014) 424006, DOI 10.1088/1751-8113/47/42/424006.
3. S. Boixo, A. Monras, *Operational Interpretation for Global Multipartite Entanglement*, Phys. Rev. Lett. 100 (2008) 100503, DOI 10.1103/PhysRevLett.100.100503.
