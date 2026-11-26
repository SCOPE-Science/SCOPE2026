---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For Q=u v^T with u=(-1,1)^T and v=(a,-b)^T, v^Tu=-s. Every affine combination C of the two given generators therefore satisfies C^2=-sC, and the left and right exponent matrices L,R satisfy LR=-sR. With r=exp(-hs/2), their product is I+(1-r)(L+rR)/s, in the specified order. The off-diagonal sum is 1-r², so their nonnegativity is necessary and sufficient for the column-conservative product to be stochastic and implies strictly positive diagonals. The coefficient of Q1 is positive; that of Q2 changes sign exactly at r=7-4√3. The opposite one-way pair attains the failure beyond this boundary, and perturbing its zero rates gives strictly positive-rate counterexamples at each fixed supercritical step. The same one-way pair has a negative entry in each factor for every positive step. At equality the Q2 coefficient vanishes; above it division by the positive Q1 coefficient gives precisely both stated rate inequalities. No conclusion about realization by the other stages is needed.

## originality

PASS

On inspected evidence, the distinct result is the sharp interval and full rate test for the product, including cases where both factors are signed, not the two-exponential construction or the sufficient test that both exponent matrices are generators.

## value

PASS

The published method's negative coefficient makes stage-wise positivity an incomplete test. A sharp scaled time horizon with an exact test beyond it and cancellation even for two signed factors answers a natural endpoint question in the minimal nontrivial Markov dimension. The common-relaxation hypothesis is substantive; the result is not sold as a bound for arbitrary generators or for the full nonlinear scheme.

The dated certificate retains the supplied scientific assessment, sources and limitations.
