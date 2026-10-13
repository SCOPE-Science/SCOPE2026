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
# Verification details

Run `python3 checker.py` with a standard Python 3 interpreter. The program exhaustively enumerates coefficient matrices of all ordinary derivations on the free class-two Lie algebra over \(\mathbb F_2\) in generator ranks \(2\) and \(3\), and over \(\mathbb F_3\) and \(\mathbb F_5\) in generator rank \(2\). It constructs the full operators directly from their action on generators and brackets, independently composes them to test \(D^2=D\), computes their ranks, and compares with the symbolic Gaussian formulas. It also checks integer polynomial coefficients for several larger parameters, but does not exhaustively enumerate those larger operator spaces.

Recorded exhaustive rank-count dictionaries:

- \((n,q)=(2,2)\): `{0: 1, 2: 16}`.
- \((n,q)=(3,2)\): `{0: 1, 3: 1408, 4: 448}`.
- \((n,q)=(2,3)\): `{0: 1, 2: 36}`.
- \((n,q)=(2,5)\): `{0: 1, 2: 150}`.

The program finishes by printing `VERIFY_OK` only if every assertion passes. In the largest exhaustive test, all \(2^{9}\) linear-generator matrices and \(2^{9}\) central-generator maps (a total of \(262144\) candidate pairs) were tested. These cases support but do not prove the infinite-field theorem; the proof in `RESULT.md` handles all fields and all \(n\ge3\).
