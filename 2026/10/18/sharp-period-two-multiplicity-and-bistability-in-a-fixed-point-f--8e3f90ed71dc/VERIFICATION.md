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

# Verification evidence and limits

Run `python3 verify_period2.py` using only the Python standard library. The program uses exact `fractions.Fraction` arithmetic to reconstruct the quartic at \((a,b,c)=(1/5,1/10,17/200)\), verifies the four rational sign tests, and isolates one root in each disjoint sign-changing interval by 95 exact bisection rounds. It checks that all reconstructed states fall in their required pieces, that two periods are attracting and one repelling, and that \(H'(t)=b(1-m(t))\) at every rational midpoint. An observed passing run printed `EXACT_RATIONAL_THREE_PERIOD_TWO_ORBITS_AND_TWO_SINKS_OK` and approximately \(0.64775,1.22504,0.41844\) for the multipliers.

The **infinite and parameter-wide** bound is established analytically: branch monotonicity forces alternating two-cycles, \(H''\) has at most one sign change on \([0,1]\), and Rolle's theorem bounds the number of roots. Finite precision or finite bisection does not prove the upper bound. The symbolic rational identities and exact signs independently support the explicit sharpness example.

The literature comparison is limited to identified sources; it is not an independent external originality certificate.
