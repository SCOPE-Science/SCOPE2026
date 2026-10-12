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

# Checks performed

The standalone `verify.py` uses exact Python integer modular recurrences. Run with `python3 verify.py`; expected output appears in `verification_output.txt`. The check covers 17 distinct recurrence coefficients congruent to four modulo six, four values of the exponent of three for each coefficient, and 153 exact tripling/companion identities. For each combined modulus, it verifies ranks and periods independently from the recurrence-state cycle. The first explicit witness is \(a=4\) with moduli \(8,3,24\) and exact (rank,period) pairs \((4,4),(3,6),(12,12)\).

# Interpretation and limits

The verifier tests only finitely many instances and **does not** establish the infinite assertion. The matrix identity, explicit four-term computation, and triple-index divisibility induction in `RESULT.md` supply the unrestricted proof. No independent scientific audit has been performed.
