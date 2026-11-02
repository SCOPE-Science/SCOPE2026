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

The proof's source-component hitting-time identity is reconstructed from the continuous-time Dirichlet equations. Each of the four averaged leaf-pair hitting-time expressions is verified independently against exact absorbing-chain linear systems in `verify.py`.

Run `python3 verify.py` from the directory containing that file with Python 3 and the NumPy and SymPy packages. Its deterministic random seeds make its examples reproducible. A completed run printed:

`PASS: 12 exact rational CTMC systems, 720 randomized full-edge comparisons and dual certificates, 48 phase-boundary continuity tests`

The comparison loop samples 12 nonuniform full-edge allocations in each of 720 cases, giving 8,640 checks. These samples are corroborative; the universal lower-bound certificate and equality cases in the proof establish all parameter ranges and unrestricted uniqueness. This verifies no claim about other graph families, nonuniform leaf prices or arbitrary continuous-time generators.

Self-review: passed. Independent audit: not yet performed.
