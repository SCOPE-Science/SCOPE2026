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

Execute `python verify.py` after installing the standalone dependencies in `requirements.txt`. The verification uses exact SymPy identities for the 2-by-2 eigenblocks, determinant obstruction, and asymptotic formula; direct dense eigenvalue comparisons for 30 balanced multipartite graph instances; 540 feasible invariant and 150 feasible nonuniform competitors; ten cycle/hypercube transitive core cases; and exact spectral restrictions on adjacency zero modes.

Observed output from the supplied package: `VERIFY_OK {'exact_blocks': 30, 'dense_checks': 30, 'random_invariant': 540, 'random_nonuniform': 150, 'other_cores': 10} asymptotic slope=1/5`.

No finite experiment establishes the quantified theorem by itself. The core uniform inequality uses an analytic PSD interpolation, and the equality classification uses an exact adjacency quadratic-form argument. Cases of non-invariant uniqueness and exact values for nonmultipartite cores remain unproved. Independent external validation has not been performed.
