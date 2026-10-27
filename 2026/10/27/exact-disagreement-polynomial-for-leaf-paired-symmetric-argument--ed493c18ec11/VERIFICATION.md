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

# Verification

The standalone `checker.py` enumerated all \(1099\) simple labelled graphs on one through five vertices and \(20\) additional deterministic six-vertex examples. For every example, it directly checked stable extensions in the paired-leaf symmetric attack graph, the independent-core bijection, all coefficients of the disagreement polynomial, and the leading degree and coefficient. The observed output was: `20 extra six-vertex tests; 1119 graphs checked in total`.

The mathematical identity is proved for **every** finite simple graph in `RESULT.md` by a reversible counting argument. Computation was not used to infer the infinite statement. No external theorem prover or independent reviewer was involved. The script has no nonstandard dependencies.
