# Self-review

## Correctness — PASS

The exact Bloch generator is obtained from the stated Lindblad equation with the Pauli normalization fixed. Its two axis reductions recover a known cosine identity and a scalar classical decay, respectively. The second-order short-time expansion gives a negative strict defect for nonzero coherent hopping. For nonzero hopping and detuning, the Hermitian parts of the shifted and unshifted Bloch generators put every eigenvalue strictly between the classical decay abscissa and zero, while the nonzero exponential-polynomial output forces an unbounded ratio to the classical output distance along a sequence of late times. The rational Laplace transform, implicit root and simple-pole residue give the stated coefficients. These arguments cover every real pair of coefficients and every positive noise rate, with the perturbative expansion taken at fixed positive rate and nonzero hopping. The supplied exact-arithmetic checker tests algebraic identities and a rigorously bounded witness; finite tests are not substituted for the analytical argument.

## Originality — PASS, qualified best-knowledge

The exact two-state commuting cosine formula and the global mixing inequality for central Hamiltonians are in He, Hutsalyuk, Mussardo and Stampiggi, *Quantum Stochastic Walks on the Permutation Group* (2026), arXiv:2609.13387, Section 5. They explicitly identify commutation as essential for their argument and do not give the present off-axis iff condition, ratio reversal, and small-detuning amplitude–rate law in the examined full text. The detuning Hamiltonian lies outside the two-state permutation-group-algebra family, so the new theorem is a boundary under an extra on-site energy rather than a correction of their theorem. Bressanini, Benedetti and Paris (2022), DOI:10.1007/s11128-022-03647-x, examine graph decoherence through a different fidelity-based quantum/classical dynamical distance and different site-jump/dephasing operators. General stochastic-walk formulations and controlled bit-flip qubit results provide ingredients, not the specific all-time observable comparison in the examined material. General optical Bloch perturbation literature could contain implicit coverage, and the comparative search cannot certify exhaustive novelty.

## Value — PASS

The sharp condition distinguishes Hamiltonian perturbations that preserve the all-times quantum-assisted two-state mixing guarantee from those that defeat it at sufficiently late times. The small-detuning eigenvalue and residue quantify how a weak off-axis term activates a long-lived but initially low-weight mode. This is a motivated robustness boundary for a specifically recent open-system mixing theorem, not merely an arbitrary finite numerical instance. It does not establish improvements in fixed-tolerance hitting times or general multi-state walks.

## Limitations and priority risks

The claim concerns a single qubit, a single unitary bit-flip Poisson jump, one constant detuned Hamiltonian, one computational measurement basis, and a fixed classical comparator. General Bloch spectral perturbation results might subsume elements of the proof, and independent publication-priority and mathematical audits have not been performed. The related 2025 qubit-control literature was inspected in relevant excerpts rather than exhaustively.

Self-review: passed. Independent audit: not yet performed.
