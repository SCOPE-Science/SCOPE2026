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

# Exact algebraic verification

Run `python verify_dst.py` under Python 3 using only the standard library. The full expected standard output is embedded as `verification_output.txt`. For each odd modulus in the test list, the script constructs primitive roots of that order in several finite prime fields, evaluates the unnormalized sine-character kernel and all of its two-by-two determinants exactly, and checks the congruence criterion where \(p\ge5\). It also checks the prime-square closed census and the exceptional order-nine all-nonzero certificate. Modular reduction is used only with primes admitting primitive roots of the requisite order. Since any complex cyclotomic zero specializes to zero at each finite-field root, a nonzero modular determinant is a valid **exact nonvanishing certificate**. A modular zero by itself is not interpreted as a complex zero; the formal group-ring proof supplies positive vanishing claims.

The finite checks comprise orders \(5,9,25,49,121,125\). Their total numbers of tested minors and singular counts, respectively, are \((1,0)\), \((36,0)\), \((4356,81)\), \((76176,765)\), \((3132900,11100)\), and \((3575881,32131)\). The checker uses only arithmetic, with no numerical thresholds, and makes no claim about untested orders beyond the rigorous proof. Independent audit: not performed.
