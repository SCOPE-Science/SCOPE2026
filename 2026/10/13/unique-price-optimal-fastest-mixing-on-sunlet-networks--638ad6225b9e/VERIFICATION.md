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

# Verification of the sunlet conductance optimum

Execute `python3 verify_sunlet.py` from the same directory as this file. The program uses only Python's standard library and reconstructs the weighted Laplacian of the sunlet graph from individual edge values. It verifies the symbolic optimum against complete symmetric-matrix spectra via a Jacobi eigensolver and tests positive nonsymmetric feasible allocations.

Observed execution:

`VERIFY_OK 168 exact rational identities; 36 optimized full Laplacian eigenspectra; 1080 nonsymmetric feasible comparisons; max absolute gap error 2.776e-16`

The exact tests use \(n\in\{3,4,6\}\), for which the first nonzero cycle eigenvalue is rational, and \(t\) chosen so that \(\sqrt{\mu_n t}\) is integral. The numerical tests cover \(n\in\{3,4,5,6,8,11\}\), six positive prices, and 30 reproducible random nonsymmetric allocations at each pair.

These finitely many tests do not establish optimality or uniqueness for arbitrary parameters. The complete analytical proof and equality analysis appear in RESULT.md. No external certification has been performed.
