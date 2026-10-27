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

# Reproduction and limitations

Run `python3 verify.py` using standard Python 3, without external packages. The script (i) directly expands the square of the six-monomial quartic to reconstruct the three diagonal Hasse--Witt entries and checks parity-forced off-diagonal vanishing, (ii) exhaustively enumerates all normalized sextuples over \(\mathbb F_3\) and \(\mathbb F_9\), (iii) tests the geometric smoothness conditions, and (iv) compares each of four rank counts with its explicit polynomial prediction. It prints `VERIFY_OK` after all assertions pass.

Observed deterministic counts: \(\mathbb F_3: (4,12,0,0)\); \(\mathbb F_9: (64,1344,8064,19584)\). The counts are ordered by \(3\)-rank from zero through three. The separate proof in RESULT.md establishes the formula for every \(q=3^m\); enumerating these two fields cannot establish the infinite quantifier. The finite-field implementation uses \(\mathbb F_9=\mathbb F_3[u]/(u^2+1)\), a field because \(u^2+1\) is irreducible over \(\mathbb F_3\).

The result counts coefficient-marked curves, modulo common nonzero scalar, not moduli isomorphism classes. An independent audit has not been performed.
