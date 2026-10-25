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
# Reproduction and checks

The source code `verify.py` enumerates all one- and two-dimensional subspaces of a three-dimensional vector space over each of \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_{11}\), adds the zero and full spaces, and tests the exact bilinear multiplication on every subspace basis. All nonzero values of \(\lambda\) are included, for 22 parameter-field pairs. The checker separately constructs the seven-or-fewer displayed generators and verifies set equality between all actual and predicted subalgebras. Run `python verify.py` with a Python 3 interpreter.

The full test reported `VERIFY_OK`. It includes both characteristic-dependent special values wherever present, including the collision \(4=1\) in characteristic three. These exhaustive finite-field tests are not a proof over arbitrary fields: the symbolic case analysis given in `RESULT.md` is the proof. Independent audit has not been performed.
