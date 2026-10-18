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

# Reproducibility and proof obligations

Run `python3 verify.py` with Python 3 standard library, no network and no input files. Observed output:

`VERIFY_OK composite_steps=103350 prime_progression_steps=7224 seeds=3445+301`

For each integer \(10\le k\le4000\) with composite \(k+2\), the code reconstructs the least-prime-divisor seed, checks trace \(H\ge2\) and the unique claimed equality, and checks thirty steps of exact recurrence, conic invariant, strict positivity, reciprocal divisibility and gcd equal to one. It separately checks twenty-four steps for each of the 301 parameters \(k=41+21t\), \(0\le t\le300\). It tests the exact polynomial closed form at the parabolic boundary.

The proof of universal solvability is independent of these finite checks: it follows from the conic identity, Vieta map and inequalities established in `RESULT.md`. The density count invokes the standard prime number theorem for arithmetic progressions, which is not proved by the verifier. Neither finite tests nor self-review constitute independent scientific auditing.
