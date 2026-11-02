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

# Verification record

The analytic proof in `RESULT.md` addresses the complete infinite parameter range and all positive nondecreasing functions. Its two decisive inequalities are \(x+u<2\lambda-2\leq4\) and \(1/x+1/u\geq4/(x+u)>1\). The exact monotonicity contradiction rules out nonfixed positive period-two points. The constructive direction provides a nonempty interval of midpoint choices for each \(\lambda>3\) and strict limiting inequalities for the affine intercept and slope.

Run `python3 verify.py` alongside `RESULT.md`; it uses only Python's standard `fractions` library. Execution in the supplied environment completed with output `PASS: exact two-cycle witness and three independent rational constructions`. The computation verifies the rational orbit at \(\lambda=4\), its reciprocal predator multipliers, and three further exact rational realizations, but no finite program execution proves the universal assertions.

The theorem does not assert global attraction, absence of periods greater than two, or stability of the constructed two-cycles. Independent mathematical audit has not been performed.
