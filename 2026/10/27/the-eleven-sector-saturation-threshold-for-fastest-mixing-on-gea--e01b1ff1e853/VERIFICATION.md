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

The proof uses a dihedral average, exact Fourier blocks, a monotone lower-bound eigenvalue, and strict rational cutoff inequalities. The critical inequalities at eleven and ten sectors are reproduced exactly using Python `fractions.Fraction`; trigonometric comparison at eleven additionally uses \(\pi^2<10\). The infinite tail follows from a cubic polynomial's monotonicity and is not inferred from numerical tests.

Running `python verify.py` after installing `requirements.txt` yielded:

`VERIFY_OK: 5 exact rational threshold inequalities; 14 spectral/dense comparisons; 490 dense eigenvalues; 1024 orbit-feasible tests; 96 nonuniform tests; n=10 strict improvement; high-n asymptotics`

The dense eigenvalue comparisons and randomly generated feasible matrices only corroborate the analytically proved result. They do not establish universal optimality. Non-invariant optimizer uniqueness and complete solutions for smaller gear graphs are outside the claim. Independent audit remains unperformed.
