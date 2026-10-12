# Average teleportation fidelity is not a Choi-spectrum invariant
## Finding
For a \(d\)-dimensional CPTP map \(\mathcal E\), let
\[
|\Phi_d\rangle=d^{-1/2}\sum_{j=0}^{d-1}|jj\rangle,
\qquad
\rho_{\mathcal E}=(\mathrm{id}\otimes\mathcal E)(|\Phi_d\rangle\langle\Phi_d|).
\]
The usual Haar-average fidelity to the identity channel is
\[
F_{\mathrm{avg}}(\mathcal E,\mathrm{id})
=\frac{d\langle\Phi_d|\rho_{\mathcal E}|\Phi_d\rangle+1}{d+1}.
\]
Consequently, average fidelity is not a function of the eigenvalues of the Choi matrix alone. For a unitary channel \(\mathcal U(\rho)=U\rho U^\dagger\), the normalized Choi state is pure for every \(U\), so all unitary channels have the same Choi spectrum \(\{1,0,\ldots,0\}\), but
\[
F_{\mathrm{avg}}(\mathcal U,\mathrm{id})
=\frac{|\operatorname{Tr}U|^2+d}{d(d+1)}.
\]
A traceless unitary exists for every \(d\ge2\), for example \(U=\operatorname{diag}(1,\omega,\ldots,\omega^{d-1})\) with \(\omega=e^{2\pi i/d}\), and gives \(F_{\mathrm{avg}}=1/(d+1)\); the identity gives \(F_{\mathrm{avg}}=1\).

Appendix B.4 of *Engineering Traversable Wormholes on a Quantum Computer* states instead
\[
F=\frac{d+\sum_i\lambda_i^2}{d(d+1)},
\]
where \(\lambda_i\) are said to be the eigenvalues of the Choi matrix. No standard Choi normalization salvages this expression as average input-output fidelity. If the Choi matrix is normalized to trace one, every unitary channel has \(\sum_i\lambda_i^2=1\), so the displayed expression gives \(1/d\), even for the identity. If the Choi matrix has trace \(d\), every unitary channel has spectrum \(\{d,0,\ldots,0\}\), so the expression gives \(1\) for every unitary, including traceless unitaries whose true average fidelity is \(1/(d+1)\).

Thus Choi purity \(\sum_i\lambda_i^2\) cannot replace target-relative entanglement fidelity in the source's teleportation-fidelity calculation.

## Assumptions and scope
The system dimension satisfies \(d\ge2\). The channel \(\mathcal E\) is completely positive and trace preserving. Fidelity is the Haar average of \(\langle\psi|\mathcal E(|\psi\rangle\langle\psi|)|\psi\rangle\), i.e. fidelity relative to the identity target. For another unitary target \(V\), the same statement applies to \(V^\dagger\circ\mathcal E\) and the corresponding target Choi vector. The finding does not claim that the Choi spectrum is irrelevant to channel purity, rank, or other diagnostics, and it does not address nonunitary targets.

## Proof
Nielsen's average-fidelity identity gives
\[
F_{\mathrm{avg}}(\mathcal E,\mathrm{id})=\frac{dF_e(\mathcal E)+1}{d+1},
\qquad
F_e(\mathcal E)=\langle\Phi_d|\rho_{\mathcal E}|\Phi_d\rangle.
\]
For \(\mathcal U(\rho)=U\rho U^\dagger\),
\[
\rho_{\mathcal U}=|\Phi_U\rangle\langle\Phi_U|,
\qquad
|\Phi_U\rangle=(I\otimes U)|\Phi_d\rangle,
\]
so \(\rho_{\mathcal U}\) is rank one and has spectrum \(\{1,0,\ldots,0\}\), independent of \(U\). Moreover,
\[
\langle\Phi_d|\Phi_U\rangle=\frac{\operatorname{Tr}U}{d},
\]
hence
\[
F_e(\mathcal U)=\frac{|\operatorname{Tr}U|^2}{d^2}
\]
and the unitary formula in the finding follows.

Choosing \(U=I\) gives average fidelity \(1\). Choosing the diagonal unitary whose entries are all \(d\)-th roots of unity gives trace zero and average fidelity \(1/(d+1)\), while leaving the Choi spectrum unchanged. Therefore no eigenvalue-only Choi formula can reproduce average fidelity. Substitution into the Appendix B.4 expression yields the two convention-dependent contradictions stated above.

## Verification
The proof is analytic and all-dimensional. The accompanying script `artifacts/verify.py` checks the identity and traceless-unitary cases for dimensions \(2\) through \(12\), under both normalized and unnormalized Choi conventions. These finite checks corroborate the algebra; they are not used as a proof of the quantified statement.

The anchor manuscript also states the correct relation \(F_{\mathrm{avg}}=(dF_e+1)/(d+1)\) in its main text and again in its process-tomography pseudocode. This internal comparison confirms that the Appendix B.4 eigenvalue formula is not merely an alternative definition of the same fidelity.

## Relationship to prior work
The identity \(F_{\mathrm{avg}}=(dF_e+1)/(d+1)\) is classical and is not claimed as new; Nielsen's 2002 note gives a proof and credits the underlying relation to Horodecki, Horodecki, and Horodecki. Modern quantum-software documentation likewise computes average gate fidelity from target-relative process fidelity, not from the Choi eigenvalue spectrum alone.

The new contribution here is the source-specific diagnosis: the 2026 wormhole-simulation review's Appendix B.4 formula cannot represent its stated average input-output fidelity under either common Choi normalization, and coherent unitary errors give a complete all-dimensional obstruction. Targeted semantic searches located no published correction of this Appendix B.4 statement.

## Limitations
The source is a preprint/review rather than a peer-reviewed theorem paper. Its main text and pseudocode already contain the correct entanglement-fidelity relation, so the error is localized to Appendix B.4; no claim is made that every numerical table in the manuscript used the incorrect expression. Literature search cannot prove absolute novelty of a correction, and no author erratum was located in the inspected public records.

## References
1. S. Bhattacharjee et al., *Engineering Traversable Wormholes on a Quantum Computer*, DOI 10.2139/ssrn.6308559, public author-uploaded manuscript dated February 2026.
2. M. A. Nielsen, *A simple formula for the average gate fidelity of a quantum dynamical operation*, arXiv:quant-ph/0205035, Physics Letters A 303 (2002), 249--252.
3. M. Horodecki, P. Horodecki, and R. Horodecki, *General teleportation channel, singlet fraction, and quasidistillation*, Physical Review A 60 (1999), 1888--1898.
