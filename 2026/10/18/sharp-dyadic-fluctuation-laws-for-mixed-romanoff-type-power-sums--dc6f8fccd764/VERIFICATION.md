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
# Verification and reproducibility

The argument in `RESULT.md` proves every integer \(r\ge2\) and every integer cutoff \(N\ge2\). It uses uniqueness of binary expansions, an exact collision count, the binomial theorem on root blocks, and a dyadic partition for empirical distribution discrepancy. No finite experiment is substituted for an infinite argument.

Run `python3 check_representations.py`. The program uses only Python's standard library and integer arithmetic. It checks the finite exact count, collision multiplicities, and two-representation count for all 294 pairs \((r,N)\) with \(2\le r\le7\) and \(2\le N\le50\). Expected output begins `PASS exact enumeration for 294 (r,N) cases`. These checks do not independently establish the limiting law or its error bound; those are analytic theorems proven in `RESULT.md`.

There is no independent external audit or certification of the mathematical conclusions. The accompanying review is a self-review, not independent verification.
