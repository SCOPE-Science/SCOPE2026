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

# Reproducibility

Run `python3 verify.py` using Python 3 standard library. The packaged checker uses exact rational Gauss–Jordan inversion and reconstructs every tested Laplacian and step matrix independently of the stated spectral formula. It completed `VERIFY_OK 29662 exact rational assertions`. It covers every unordered multipartite profile with total vertices 4 through 10, with each class size at least two and at least two classes; seven \(\theta\) choices and seven step sizes are tested. See `RESULT.md` for their explicit values.

The analytic proof separately covers every finite allowed partition and continuous \(\theta\), \(h\) range. Finite testing does not independently verify the infinite theorem, novelty, or asymptotic claim. The source-code checks are not an external or independent mathematical audit.
