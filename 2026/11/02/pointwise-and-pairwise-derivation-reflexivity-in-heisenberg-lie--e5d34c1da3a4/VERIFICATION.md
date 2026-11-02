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

`python3 verify.py` was run against the packaged standalone source, with the marker `HEISENBERG_LINEAR_LOCAL_2LOCAL_OK`.

The script solves ordinary derivation equations directly from Lie structure constants, constructs the derivation subspace by row reduction, and checks single- and paired-vector agreement against the resulting spans. It exhausts all 512 linear endomorphisms and all vector pairs for the three-dimensional Lie algebra over the two-element field. It also checks 80 reproducibly sampled endomorphisms over the three-element field, and tests 18 random plus 10 conformally symplectic maps over the five-dimensional Lie algebra over the two-element field against all 1024 vector pairs. This is finite corroboration, not proof for arbitrary ranks or fields; the universal arguments appear in `RESULT.md`.

The study does not determine nonlinear two-local derivations, arbitrary two-step nilpotent centers, or publication priority. No external independent audit was performed.
