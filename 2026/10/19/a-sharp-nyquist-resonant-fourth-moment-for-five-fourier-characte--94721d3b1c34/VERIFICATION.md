---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Parseval gives precisely the alias of coefficients 0 and 8 of F², equivalently the merge of autocorrelations ±4. The reflected RMS step improves each nonnegative correlation, strictly improving some nonzero lag for unequal reflected magnitudes. The independent envelope calculation optimizes first in t=u² and then factors the derivative of the resulting rational function in v into a negative positive factor times v⁴+4v³−7v−2; the unique positive root is the global maximum, including the boundary checks. Positive magnitudes force affine phases by equality in the lag-one triangle inequality; the merged lag-four term forces phase increment in (π/4)Z, giving exactly eight classes. The exact formula is correct; the printed K approximation is off in the last displayed digit (K=3.527901483813719443…); the quoted floating-point quadrature is diagnostic, not an exact check.

## originality

PASS

Known majorization and reflection methods provide reductions, and an indexed exact three-character result already covers the x=0 boundary. The closest phase-locking result found is for four characters on the six-cycle, not five on the eight-cycle. Continuous-circle trigonometric-polynomial maximization has a different functional because it does not identify degrees 0 and 8. The supported distinct result is the exceptional finite norm and its eight equality classes, not those general methods or boundary cases.

## value

PASS

Eight samples with five consecutive Fourier modes are the critical size where the two endpoint degrees of the squared polynomial first alias. This is a natural finite threshold, not an arbitrary numerical slice. The sharp sampled norm and complete equality set determine how the alias changes the actual optimizing magnitude profile and replaces continuous modulation by a finite family; they provide an exact test case for cyclic restriction and sampling estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
