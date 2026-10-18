---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible scientific verification

From the directory containing these files, execute:

```sh
python3 check_incidence.py
python3 check_quadratic.py
```

Both scripts use only Python 3 standard-library facilities. Their deterministic successful outputs are included as `check_incidence.out` and `check_quadratic.out`. The first script independently constructs totally isotropic projective lines in four-dimensional prime-field alternating spaces, forms their incidence duals by transposition, and checks complete center-count spectra and joint one-dimensional refinement histograms for the labelled pairs and linewise sets. All tests for primes \(3,5,7\) passed, with first cross-graph mismatch of refinement histogram at round \(4\) for the opposite-pair case. The second script enumerates every nonsingular symmetric binary form for prime fields \(3,5,7,11,13\) and checks its projective zero count and discriminant, with all tests passing.

For \(q=3\), opposite-pair center multiplicities are \(\{1:16,4:2\}\) versus \(\{0:6,2:12\}\). Two marked collinear points yield eleven stable colour classes in both geometries, while marking all four points of their common line yields fourteen. Finite checks provide **corroboration only**. They do not establish an unbounded-prime-power result; the proofs in RESULT.md establish the stated range. There is no formal proof-assistant verification and no independent scientific audit.
