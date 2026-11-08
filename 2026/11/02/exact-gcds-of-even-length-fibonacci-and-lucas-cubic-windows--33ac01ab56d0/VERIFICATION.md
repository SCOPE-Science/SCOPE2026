---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The theorem for every integer m>=1 and two sequences is proved from 5F_r^3=F_(3r)-3(-1)^r F_r and L_r^3=L_(3r)+3(-1)^rL_r, endpoint pairing at half-length, and reversible fourth-order T_a(t),U_a(t) normalized recurrences. Directly evaluated four initial terms imply gcd_t T_a(t)=gcd(a+6,30) and gcd_t U_a(t)=gcd(3a+6,11a+12), whose Bezout combination divides 30. Parities and Lucas norm identities isolate p=2,3,5; hence for odd m both Fibonacci and Lucas 2m-window gcd equal L_m/2^[3|m], while for even m they are 3^[4|m]F_m/2^[3|m] (Fibonacci) and five times that (Lucas). Independently recomputed both sequence families for m<=60 using 15 shifts each, including length6 gcd=2 for each. The all-m result is algebraic, not obtained by extrapolating that finite range.

## originality

PASS

The Fibonacci half of the finding is contained in the distinct same-assignment all-k Fibonacci theorem, so do NOT claim its independent originality here; the additional full Lucas-cubic branch with its factor-five transition is the surviving distinct all-even-length claim. Earlier arxiv:2204.12626 §6.1 poses (rather than proves) even cubic gcd expressions for both sequences, with wrong small boundary; arxiv:2104.12262 and 2301.05758 are first/square powers. The comparative Lucas theorem is not a direct implication of first-power or Fibonacci-only formulas. Residual unindexed resolution possible.

## value

PASS

The Lucas sequence is the canonical companion to Fibonacci in the published infinite-window GCD problem. A complete exact Lucas-cube classification at every even width, including an unexpected factor five for even half-width, answers a motivated natural invariant, beyond reusing the Fibonacci-only theorem. The result also corrects a printed cubic conjecture at length six. It is a substantive paired recurrence classification, while clearly distinguishing the Fibonacci branch that overlaps a separate same-batch result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
