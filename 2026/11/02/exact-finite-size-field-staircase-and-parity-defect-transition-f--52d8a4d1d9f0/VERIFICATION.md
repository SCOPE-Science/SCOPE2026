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

# Verification of the finite-size ground-state classification

The result relies on the analytic incidence-charge reduction, a proved near-regular degree-sequence lemma, exact discrete-convexity parity optimization, and direct combinatorial enumeration of near-saturation defect patterns. All are fully specified in RESULT.md. Independent assessment has not been performed.

Run `python3 verify.py` in the directory containing the two standalone files `verify.py` and `verification_output.txt`. The exact integer checker enumerates every spin configuration of \(T_4,T_5,T_6,T_7\), corresponding to \(64\), \(1024\), \(32768\), and \(2097152\) states, and compares every predicted minimizing charge profile and its complete labelled degeneracy with exact brute-force values for each tested half-integer \(h/J\) through \(2(n-2)+1\). Captured stdout is embedded in verification_output.txt. The checker prints PASS for all four sizes.

The finite census does not establish arbitrary \(n\) by itself. The general proof requires the incidence-square identity, the exchange-edge degree-balancing argument, the parity condition for simple-graph degree sums, and the matching/path classification for dilute negative spins. No kinetic, quantum, positive-temperature or experimental claim is made.
