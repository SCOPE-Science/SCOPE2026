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

## Reproduction

Run `python3 verify.py`. The expected final line is `VERIFY_OK 19 exhaustive finite-field cases`. The verifier uses only Python standard-library modules.

It constructs the multiplication table of each finite radical-square-zero quiver algebra from vertex and arrow bases, then enumerates every ordered tuple in each of 19 small configurations. It determines the actual generated subalgebra by repeatedly adjoining left and right products and computing vector-space rank over the relevant field. The computations include characteristics two and three, the quadratic extension field of order four, loops, parallel arrows, two-cycles, and a directed three-vertex path. None of these tests assumes the structural generation criterion in the proof. The exact counts match the closed product formula.

## Scope of verification

Exhaustive enumeration in these finite configurations is not a proof of the formula for arbitrary quivers, fields, or tuple lengths. Those cases are covered by the diagonal-interpolation, idempotent-lifting, conjugation, and independent-rank argument in `RESULT.md`. The birthday-window limit follows analytically from the exact finite formula and logarithmic estimates, not from an extrapolation of numerical tests.

The source inspections and originality comparison are reported separately in `AUDIT.json` and `REVIEW.md`. Independent mathematical audit has not been performed.
