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

# Reproducibility

Run `python verify_three_hyperflex.py` (Python 3.11+ and SymPy). The script enumerates every one of the \(32767\) nonzero binary ternary quartic forms; detects each rational hyperflex using the tangent gradient and exact line restriction; proves by an assertion that exactly \(28\) forms have three rational hyperflexes, covering each noncollinear triple once; and checks the displayed representative by Gröbner-basis unit ideals in the three affine charts over \(\mathbf F_2\). It independently enumerates all \(168\) invertible linear coordinate substitutions, obtaining the precise extremal orbit and a six-element stabilizer.

`three_hyperflex_certificate.json` is the generated list of all \(28\) triples and their coefficient masks. The verifier uses the monomial order `[(a,b,4-a-b) for a in range(5) for b in range(5-a)]`. Bit mask \(15150\) is the representative. `three_hyperflex_verification.txt` contains the actual execution output. All tests were successfully run on the packaged script before ledger delivery.

The analytic argument in `RESULT.md`, not the enumeration alone, proves the universal assertion for smooth quartics and their geometric nonsingularity. Full historical priority against unindexed tables is not certified. No independent external audit has been performed.
