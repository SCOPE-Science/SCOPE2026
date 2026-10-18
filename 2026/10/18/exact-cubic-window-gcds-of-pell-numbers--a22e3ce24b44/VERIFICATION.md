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

# Exact arithmetic and mathematical checks

`python3 verify.py` uses only the Python 3 standard library. The included `verification_output.txt` gives the run outcome and case counts. The executable recomputes all \(480\) proposed window GCDs independently from Pell cubes, checks \(7200\) additional shifted windows, checks \(504\) antidifference identities and \(498\) cubic fourth-order recurrence identities, and checks \(2400\) Pell matrix identities plus \(2400\) integral-polynomial/congruence instances.

The proof's unrestricted parts are the exact matrix identity, the global odd-prime obstruction from Cassini's identity, the integer-polynomial identity \(7S_n=t\Phi_n\), and exact local valuations. Finite arithmetic does not establish the infinite statement on its own. No external independent validation has been performed.
