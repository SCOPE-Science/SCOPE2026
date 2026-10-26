# Scientific review: central-defect Ising trimer

## Correctness

**PASS.** The asserted all-real boundary follows from an exact characteristic factorization into a reflection-odd two-dimensional block and a reflection-even six-dimensional block. The latter yields a cubic in squared energy. Its discriminant, sign evaluations, and Descartes sign count give exactly two positive discriminant roots at every positive field; a zero-crossing argument establishes positivity of all squared energies up to the smaller root, and exclusion of real-spectrum reentry afterward. The global minimum follows from the exact resultant of the discriminant and its field derivative, combined with exact low/high-field asymptotics. The included independent symbolic script reconstructs the original eight-dimensional Pauli Hamiltonian, verifies the polynomial identities, and evaluates the minimum. Numerical values are not an infinite-parameter proof; the sign/resultant argument is.

## Originality

**PASS, subject to ordinary literature uncertainty.** Muldoon and Joglekar, arXiv:2304.10064 (2023), introduce precisely this non-Hermitian Ising perturbation and obtain the zero-field threshold and numerical transverse-field phase portraits, but their accessible full text does not supply the three-spin transverse-field discriminant, complete all-real boundary, or unique optimized-field result. Starkov–Fistul–Eremin, arXiv:2302.14672, treat staggered imaginary longitudinal fields rather than a central Jordan raising perturbation. Barnett–Joglekar, arXiv:2302.13204, analyze detuned one-particle tridiagonal chains rather than this interacting Pauli Hamiltonian. Searches of relevant published mathematical records and the accessible collection of related claims did not identify an equivalent or stronger covering result. A result in unindexed literature is possible; the absence of a search hit is not proof of global novelty.

## Mathematical value

**PASS.** The three-spin system is the smallest open Ising chain with a genuinely interior defect. Unlike an arbitrary finite-size spectrum, its exact critical curve resolves whether a transverse field can destabilize or restabilize the *entire* spectrum. The sharp global field optimization and positive all-field stability floor distinguish it from larger-chain numerical phase diagrams and provide an exact finite-size benchmark for localized non-Hermitian control. The proof needs a nontrivial polynomial sign classification and elimination; it is not a mere renaming of the known zero-field threshold. No thermodynamic or longer-chain inference is asserted.

## Closest literature and limitations

Primary comparison: Muldoon and Joglekar, 2023, arXiv:2304.10064, Sections II–IV. Nearby but different mechanisms: Starkov et al., 2023, arXiv:2302.14672, and Barnett–Joglekar, 2023, arXiv:2302.13204. Residual novelty risk: an unindexed equivalent evaluation of the same three-spin Hamiltonian. Scope limits: exact three-spin open chain, one central \(\sigma^+\) perturbation, real nonnegative parameters, full-spectrum reality rather than dynamical behavior or positive-metric construction.

Self-review: passed. Independent audit: not yet performed.
