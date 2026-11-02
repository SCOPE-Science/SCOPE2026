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

# Finite checks and proof boundary

Run `python3 verify_triple.py` with only the Python standard library. It verifies the finite-field multiplication rules, constructs full three-block parity-check matrices for odd \(r\in\{3,5,7,9\}\), checks that the \(2^r-2\) columns are all nonzero and distinct, that the row rank is \(r+1\), and that each basis word \(\iota_3(e_i)\) has zero syndrome. By linearity, these basis checks show full threefold-diagonal inclusion for those constructed instances. For \(r=3\), it also checks every possible six-column, rank-three distinct-nonzero syndrome set has nonzero column sum. A successful run prints `VERIFY_OK` and the tested parameter rows; no external data are needed.

The unbounded proof is in `RESULT.md`: the omitted-vector all-one obstruction and explicit general \(\mathbb F_4\) line selection do not depend on numerical enumeration. Finite outputs are not an exhaustive test of all larger parity-check matrices, all possible binary codes, or literature novelty. The equality-case partial-line-spread argument follows from forced three-column sums and unique nonzero binary columns. No independent audit has occurred.
