# Independent mathematical audit — SCOPE-20260919-7421eebe6032

Final disposition: **PASS**.

## Correctness
**PASS** — The Walsh basis diagonalizes the normalized resolvent, so the Schatten sum is exactly the sum of \((1+t\lambda_F)^{-p}\). The Mellin-product formula follows by Tonelli. Finite Schatten membership forces the singleton series to converge; exponential domination then gives the square-summable coordinate biases required by Kakutani for every positive time, hence absolute continuity of the product measures and of the resolvent mixture. The subexponential/superexponential phase follows from counting the \(2^{N-1}\) subsets with maximum index \(N\). For geometric weights those levels have size comparable to \(a^{-N}\), giving the critical exponent, endpoint weak-Schatten law, and the Abel-limit zeta residue. The dyadic Hurwitz-zeta specialization is consistent.

## Originality
**PASS** — Acuaviva's accessible primary material identifies the new complemented-space construction but does not advertise Schatten analysis. The older Schachermayer paper was inspected in full where relevant: it constructs a singular direct product convolution with multiplicative Walsh eigenvalues that is in \(S_p\) for \(p>2\), which is genuinely different from the reciprocal-additive resolvent spectrum here. published-record database and web searches found no prior phase diagram, no theorem that finite Schatten membership forces absolute continuity for these resolvents, and no geometric-weight zeta residue. Full text of the very recent Acuaviva source could not be independently retrieved in this run, so hidden overlap remains a stated risk.

### Equivalent formulations
The closest historical construction is not equivalent and in fact demonstrates the distinction claimed by the package.

### Broader coverage
No inspected broader theorem mechanically supplies the full assigned phase diagram.

### Exact database or table
This is theorem-level spectral asymptotics; there is no relevant finite table beyond exact-result search.

### Claim versus prior implication
No decisive prior implication was found.

## Value
**PASS** — The theorem identifies a sharp operator-ideal boundary inside a current Banach-space construction, distinguishes it from the classical singular Schatten convolution example, realizes every critical weak-Schatten exponent, and gives explicit zeta data. These are motivated structural consequences of the resolvent spectrum rather than an arbitrary parameter exercise.

## Source inspections
- **On complemented subspaces of L1[0,1]** (https://arxiv.org/abs/2609.17283): primary abstract and bibliographic record; verified full text was not accessible during this audit Assessment: ABSTRACT_ONLY_WITH_RESIDUAL_OVERLAP_RISK. Evidence: The accessible primary statement concerns the complemented-subspace construction and does not state a Schatten phase diagram.
- **Some remarks on integral operators and equimeasurable sets** (https://www.mat.univie.ac.at/~schachermayer/pubs/preprnts/30.pdf): full relevant Section 3, including the biased product measure, Kakutani dichotomy, Walsh diagonalization, and trace-class estimate Assessment: CLOSEST_CLASSICAL_CONSTRUCTION_NOT_COVERING. Evidence: The operator is direct convolution by a biased product measure with multiplicative Walsh eigenvalues and can be singular while belonging to \(S_p\) for \(p>2\).

## Residual risks
- The full 2026 Acuaviva preprint could not be independently retrieved, so hidden overlap in its body remains possible.
- Older literature on diagonal semigroups and Cantor-group spectral triples may contain equivalent asymptotic language not found in the searches.
