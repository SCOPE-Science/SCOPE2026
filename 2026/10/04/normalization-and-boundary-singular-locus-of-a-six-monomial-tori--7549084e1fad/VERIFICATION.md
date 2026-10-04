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

The included `artifacts/verify.py` uses only the Python standard library. It checks the exact exponent configuration, normalized square area \(50\), full-lattice generation, the two exponent identities defining the inverse on the dense torus, all four facet supports and their lattice length \(5\), and the common bidegree \((5,5)\) of the homogenized sections.

Run `python3 artifacts/verify.py`. The expected and observed successful terminal line is `VERIFY_OK`.

The script certifies the finite combinatorial identities used by the proof. The implications “proper plus quasi-finite implies finite,” “finite birational from a normal variety gives the normalization,” and “regular implies normal” are standard algebraic-geometric facts used in the written proof rather than delegated to computation. No local analytic singularity classification is asserted.
