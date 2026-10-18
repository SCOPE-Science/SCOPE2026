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

# Verification of exact coefficient zero masks

Analytically checked all rank-one coefficient cases: four nonzero coordinates; a vanishing pair on one half; exactly one coefficient in a half; and the normalization for two nonempty zero fibers. The determinant relation \(UV=WX\) and the order \(L\) of \(\chi^2\) are essential. Projective multiplicities count functions modulo nonzero complex scalar only.

Run `python3 verify.py` with a standard Python 3 interpreter; no third-party packages are required. The packaged checker uses exact modular exponent arithmetic for the fiber witnesses, followed by exact Gaussian-integer matrix-coefficient tests for \(D_8\).

Observed final line: `CHECK_OK characters 80 pair_witnesses 3192 gaussian_rank_one_vectors 2304`.

The code covers twelve finite abelian kernels and a finite coefficient alphabet in one dihedral group; it is not a proof of any untested case. The infinite family is handled by the explicit algebraic argument in RESULT.md. Independent audit: not performed.
