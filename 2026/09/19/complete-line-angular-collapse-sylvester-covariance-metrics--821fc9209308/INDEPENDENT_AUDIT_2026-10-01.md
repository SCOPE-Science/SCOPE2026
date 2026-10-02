---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For every smooth positive symmetric homogeneous kernel metric on the SPD cone, metric and geodesic completeness hold exactly at homogeneity degree \(2\). For the Sylvester-power family this gives completeness exactly on \(p+q=2\), equivalently the dilation- and inversion-invariant line; after constant normalization, the complete non-mean region \(|p-q|>2\) has explicit isospectral quarter-turn length asymptotic to \(\pi\kappa^{(2-|p-q|)/4}\), hence angular collapse at infinity.

## Correctness — PASS

Necessity follows from the exact scalar-ray length integral: for homogeneity \(r<2\) the zero boundary is at finite length and for \(r>2\) infinite scale is at finite length. For \(r=2\), the diagonal metric terms control Euclidean displacement of the ordered log-spectrum, confining every metric-Cauchy sequence to a fixed spectral annulus; continuity and positivity of the kernel then give two-sided uniform equivalence with the Frobenius norm and metric completeness, hence geodesic completeness by Hopf--Rinow. Direct substitution independently verifies the dilation/inversion pullbacks, the mean-kernel monotonicity threshold \(|p-q|=2\), and the two-dimensional rotation-speed formula. The actual verifier source was inspected and its algebra agrees with these identities; the saved output was not used as proof.

**Sources.** current RESULT.md and verification script at the archived record; Li--Mishra--Jawanpuria--Mostajeran, arXiv:2609.17089; Thanwerdas--Pennec, arXiv:2109.05768 / Linear Algebra Appl. 661 (2023)

**Residual risks.** No correctness defect was found.

## Originality — PASS

The motivating covariance-metric paper studies local Hessian conditioning and does not state this global completeness/angular phase diagram. The closest established completeness theorem located is for mean-kernel metrics and says homogeneity power \(2\) is necessary and sufficient in that subclass. The audited theorem removes the mean hypothesis and then reaches the non-mean \(|p-q|>2\) part of this new family. published-result corpus searches for homogeneous-kernel completeness, the complete line, inversion symmetry, and angular collapse returned the current record but no earlier equivalent finding.

### Equivalent formulations

The audited general homogeneous-kernel lemma is stronger than the mean-kernel theorem and is not an alias of the source paper's conditioning result.

### Broader coverage

That prior coverage does not imply the non-mean complete region or its angular-collapse threshold.

### Exact database or table

The claim is theorem-level rather than a finite database value; the semantic database was used as a coverage check.

### Claim versus prior implication

Neither checked prior implication yields the all-positive-homogeneous-kernel completeness theorem or the explicit non-mean isospectral degeneration.

**Checked sources.** arXiv:2609.17089; arXiv:2109.05768; Hiai--Petz 2009; published-result corpus search

**Residual risks.** Older matrix-geometry literature using different terminology for homogeneous kernels remains a residual risk, but the directly relevant 2023 synthesis did not state the audited extension.

## Value — PASS

Completeness is a basic global invariant of a newly proposed optimization metric family, and the result supplies a sharp line together with a distinct angular-degeneration boundary inside that line. The non-mean extension is structurally meaningful and can constrain geometric metric tuning without pretending to prove algorithmic convergence.

**Sources.** Li et al. 2026 metric-family motivation; mean-kernel completeness literature

**Residual risks.** The angular-collapse construction is diagnostic rather than a geodesic-distance or optimization-performance theorem.

## Limitations

- The angular formula is the length of an explicit isospectral path and therefore an upper bound on geodesic distance, not an exact distance formula.
- The global statements concern smooth positive kernel metrics on the full SPD cone and do not imply optimization convergence.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
