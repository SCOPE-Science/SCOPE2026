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

# Exact arithmetic and finite-state verification

Run `python3 wheel_cca_verifier.py` with Python 3 standard library. The verifier constructs, rather than loads, the 3-, 9-, 4-, and 81-state transfer matrices. It checks the small matrices' complete characteristic polynomials by the first full-dimensional Newton traces; for the 81-state matrix it checks exact rational ranks of its fifth and sixth powers (each six), an exact integer matrix-polynomial annihilation identity, and six power sums, obtaining the stated degree-six nonzero characteristic polynomial. These are finite, exact certificates for the transfer part of the proof, not floating-point guesses.

The verifier separately enumerates every labelled initial color assignment for wheel rim sizes \(3\) through \(10\), totaling \(265680\) states. For each, it directly applies five synchronous updates, checks \(F^5=F^2\), identifies the first time at which a fixed point or three-cycle is entered, and matches the six formula counts. Its last output line is `WHEEL_CCA_EXACT_VERIFY_OK`, and the full run output is supplied as `verification_output.txt`.

The structural proof in `RESULT.md` handles all wheel sizes; the finite enumeration alone cannot establish the universal time bound or the asymptotic conclusion. No independent audit, formal theorem-prover certification, or exhaustive search of all historical literature is claimed.
