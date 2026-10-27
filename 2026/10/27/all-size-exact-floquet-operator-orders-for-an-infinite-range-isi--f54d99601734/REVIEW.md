# Scientific review

**Correctness — PASS.** On the full Hilbert space, the even proof reduces the Ising gate exactly to one global Pauli rotation and computes its fourth power. The odd proof reduces the Ising gate to a quadratic Boolean phase, proves an all-dimension Walsh-cube identity from a nondegenerate quotient Gauss sum, then determines the precise projective order via a binary symplectic action. The Pauli phases and small-size matrix consequences were checked independently; `check.py` checks the Walsh cube in exact integer arithmetic for four odd sizes. The analytical proof, not enumeration, bears the infinite quantifier.

**Originality — PASS with residual risk.** The 2023 primary source proves explicit sizes \(5\) through \(11\) and offers numerical evidence for higher sizes, whereas the claimed identities cover every \(N\ge2\). A 2024 companion studies a distinct coupling; a later 2024 follow-up explicitly describes finite-size analytic and larger-size numerical evidence. The 2026 arithmetic method is for finite matrices and investigates a nearest-neighbor open chain, not this complete graph. Searches for aliases and global-Pauli and Clifford forms yielded no stronger exact all-size implication. Residual possibility: an unindexed Clifford-circuit treatment or an inaccessible follow-up appendix independently contains the same identities.

**Mathematical value — PASS.** A sharp exact all-size period theorem resolves the model's stated numerical extrapolation problem and determines whether ordinary recurrence occurs after twelve or twenty-four kicks in the odd case. The halfway global Pauli identities determine the entire operator return for arbitrary input states and are not consequences of abstract Clifford finiteness without a nontrivial family-specific calculation.

**Scope.** No statement of physical integrability beyond exact recurrence, no generic-coupling result, and no claim concerning shorter periods for special individual states. The related 2024 arbitrary-input follow-up could only be assessed via its publicly accessible abstract.

Self-review: passed. Independent audit: not yet performed.
