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

# Verification

Run `python3 verify.py` from this directory using Python 3. The script calculates least-prime factorizations through \(250000\), independently lists every positive divisor in \((1,\sqrt n]\), and compares the resulting Schreier predicate with the square-adjusted divisor-count criterion. It also verifies inclusion of all instances of the maximal prime-factor layers described by the theorem. All asserted exact identities passed. It prints sample counts for eight fixed least primes and slow-converging leading-asymptotic estimates; **these finite ratios are not evidence that a limit exists**.

The infinite asymptotic proof is analytical: it invokes Landau's established fixed-prime-factor count and a finite classification of exponent types. It assumes the prime number theorem through Landau, not an unproved prime-distribution conjecture. No independently performed audit or machine proof is claimed.
