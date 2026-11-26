---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Fubini gives the frozen row kernel with the subtraction (1-t)^α/α before the overall 1/Γ(α). The input sign of a row realizes its L¹ mass, and the L¹-continuous rows on [0,1] give an attained maximum. On x≤b=α^(1/(1−α)) the ratio of the positive and subtractive terms increases in t and starts at ≥1, so the mass differentiates to x^(α−1)−2(1−x)^α/α. The function x^(1−α)(1−x)^α increases up to 1−α then decreases, and its value at b exceeds α/2, yielding exactly one upward crossing on the first branch. Beyond b, put y=1−t* at the extra zero and z=1−x: y'=(1−α)/(1−αz/y) lies strictly between 0 and 1. The derivative of the row mass there is −(1−z)^(α−1)+2(y^α−z^α)/α; differentiation in z gives a negative result from y>z and y'<1. Hence that branch is convex and its maximum is at b or 1. Direct endpoint integration and α^α≤1−α+α²≤(1+α)/2 for α≥1/2 show the terminal row does not exceed the initial one, proving the unique interior maximum. The maximizing row is nonzero a.e.; equality in the complex triangle inequality and |f|≤1 forces exactly its sign times one global phase. The Abel quadratic and norm radical check out; at α=1 the row mass is [x²+(1−x)²]/2. With ε=1−α, the small root lies below ε and satisfies x≤α2^(−1/ε); substituting into the logarithmic equation gives log x=(log α−log 2)/ε+o(1). Substituting stationarity into the mass difference and Taylor-expanding gives 2εx/α²+O(x²), with uniform remainder and x²=o(εx), confirming the leading gain. Independent replay: python3 /workspace/branches/independent_reproduction.py fractional; singularity-removed quadrature and a logarithmic fixed-point calculation reproduce the Abel norm 0.89568534008928865309 and sampled rows, with gain/asymptotic ratio 1.0018466485563 at ε=0.002. These are finite checks only; the uploaded checker was inspected, not executed.

## originality

PASS

The closest inspected results optimize different operators, spaces, or parameter limits. The standard reduction to the absolute row integral is not new; the supported distinct claim is the sharp value and optimizer for the output-mean-centered fractional operator, including the explicit Abel case and the exponentially small improvement over the initial row.

## value

PASS

This gives the best uniform oscillation bound relative to the output mean and identifies all inputs realizing it, for a natural fractional Volterra family. It shows an interior optimizer despite the integer-order endpoint maximizers, and quantifies an exponentially small gain that sampling and ordinary expansions at order one do not resolve. This is more than a routine kernel norm bound or evaluation at one arbitrary point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
