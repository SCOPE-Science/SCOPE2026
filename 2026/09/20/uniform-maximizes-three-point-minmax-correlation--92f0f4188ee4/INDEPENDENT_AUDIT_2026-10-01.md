# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-92f0f4188ee4`

## Correctness — PASS

The direct moment identities on the affine-normalized support \(\{-1,0,1\}\) give \(\operatorname{Cov}(M,L)=G^2/4\) and the displayed rational squared-correlation function. Exact differentiation and resultant elimination rule out nonsymmetric stationary points in the strict interior; the symmetry line has its unique maximum at \(q=2/3\), and the two simplex-edge families have squared correlation at most \(1/9\). The boundary limits are therefore below \(64/361\). The inspected symbolic verifier independently reconstructs the moments, resultant, edge formulas, uniform value, and the published benchmark; it is corroboration rather than the proof.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_three_point_minmax.py
- Papadatos arXiv:2205.14360
- López-Blázquez–Salamanca-Miño 2021

### Correctness risks

- The theorem is only for sample size two, the min/max pair, and three equally spaced atoms.

## Originality — PASS

Papadatos proves a global discrete Terrell bound and characterizes equality by discrete rectangular laws, but that \(1/2\) theorem does not determine the sharp maximum inside the fixed three-point support simplex. The audited optimization gives the strictly smaller exact constant \(8/19\), unique uniform weight, and complete positive attainable range. Fresh Resultary and web searches found no theorem already solving this fixed-support probability-vector optimization.

### equivalent_formulations

Searches:
- Resultary: three point probability weights min max correlation uniform Papadatos N=3 n=2
- Papadatos arXiv:2205.14360
- López-Blázquez–Salamanca-Miño 2021 fixed discrete-parent correlation

Evidence:
- Papadatos's theorem is over all discrete laws and yields the coarser universal bound \(1/2\).
- The audited theorem optimizes over weights on a fixed three-point lattice and attains \(8/19\), so the parameter problem is different.

Reasoning:
The fixed-support weight optimization, the unrestricted discrete-parent problem, and the fixed-weight formula were compared as distinct formulations.

### broader_coverage

Searches:
- Papadatos 2022/2023 discrete Terrell theorem
- Terrell 1983 continuous theorem
- López-Blázquez–Salamanca-Miño 1999/2021

Evidence:
- The broader parent-distribution theorems do not imply the fixed-support sharp constant because their extremizers range over different supports.

Reasoning:
A universal upper bound of \(1/2\) cannot imply the stronger \(8/19\) bound on this constrained simplex.

### exact_database_or_table

Searches:
- current Resultary order-statistic correlation findings
- fixed three-atom probability-vector searches

Evidence:
- No exact table/database result for the three-atom simplex maximum was located.

Reasoning:
The claim is a continuous optimization theorem, not a finite table lookup.

### claim_vs_prior_implication

Searches:
- claim-versus-Papadatos implication comparison

Evidence:
- Uniform weights on three equally spaced atoms are a discrete rectangular law, but Papadatos only shows they can attain the universal discrete optimum when support size is allowed to vary; it does not show that nonuniform weights on that fixed support are bounded by \(8/19\).

Reasoning:
The audited elimination and boundary analysis provide additional information not mechanically implied by the prior characterization.

### source_inspections

- **A discrete analogue of Terrell's characterization of rectangular distributions** — https://arxiv.org/abs/2205.14360. Trigger: Closest primary theorem on min/max correlation for discrete samples of size two. Material read: Accessible arXiv abstract and public full-text copy scope; the fixed-support probability-vector optimization was checked against the theorem statement and discussion. Method: Primary-source scope and implication comparison. Assessment: NOT COVERING the sharp fixed-three-point constant. Evidence: The paper proves the universal discrete \(1/2\) bound with discrete-rectangular equality, not the \(8/19\) fixed-support optimization.
- **Assigned exact symbolic verifier** — artifacts/verify_three_point_minmax.py. Trigger: Nontrivial resultant and boundary computations. Material read: Complete source. Method: Line-by-line symbolic check. Assessment: Correct corroboration. Evidence: It reproduces the rational formula, derivative resultant, symmetry maximum, boundary maxima, and benchmark values.

### checked_sources

- https://arxiv.org/abs/2205.14360
- https://doi.org/10.1007/s00180-021-01103-5
- current Resultary exact search
- assigned RESULT.md and verifier

### residual_risks

- A differently indexed solution of the fixed-support probability-vector problem may exist, especially in computational order-statistics literature.

## Scientific value — PASS

The theorem settles the first nontrivial fixed-support weight-optimization case of a natural order-statistic correlation question, with a sharp constant, unique extremizer, boundary control, and full attainable range. That is a motivated exact extremal fact rather than a routine substitution.

### Value sources

- Papadatos fixed-support direction
- assigned global simplex optimization

### Value risks

- No extension to larger supports or other order-statistic pairs is established.

## Limitations

- Three equally spaced atoms only.
- Sample size two and the min/max pair only.
- No claim for arbitrary support locations or larger support sizes.
- Originality is best-of-knowledge.

## Disposition

**PASSED**
