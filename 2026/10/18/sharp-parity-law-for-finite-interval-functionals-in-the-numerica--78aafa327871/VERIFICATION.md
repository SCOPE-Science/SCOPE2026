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

Gauge the phases of the unilateral shift recursively along the coordinate chain. Absolute values of a trial vector suffice for the numerical radius of the resulting nonnegative shift. The two parity classes on the k+1 interval vertices are both nonempty; normalizing each to squared mass 1/2 gives the same edge product 1/(2 sqrt(mn)) and thus the upper dual bound for every starting index and arbitrary bounded ambient weights. For odd k the alternating weights give disjoint norm-one two-vertex blocks. For even k=2q the stated adjacent-weight sums at even and odd vertices are 2 sqrt(q/(q+1)) and 2 sqrt((q+1)/q), including both endpoints. They give a strictly positive eigenvector with eigenvalue one; conjugation by its diagonal makes the block row-stochastic and hence its spectral radius one. The edge sum is 2 sqrt(q(q+1)). Equality on the interval forces a common phase and equality in the top-eigenvalue Rayleigh quotient; stepping through the vertex equations from the left endpoint uniquely fixes each edge. This includes k=1 and only asserts uniqueness for weights vanishing outside the interval. The even-length improvement follows by comparing k(k+2) with (k+1)^2. These exact equations establish all lengths; the frozen numerical script is supplementary, not rerun or treated as an independent certificate.

## originality

PASS

The numerical-radius norm, the weighted-path spectral reduction and the uniform block bound are prior. The supported distinct claim is attainment of the sharp all-length dual parity law, including the strict even improvement, and the exact unique supported equality profiles. A general feasibility or spectral characterization is not a proof of attainability and equality here. No exhaustiveness or historical priority is asserted.

## value

PASS

Consecutive finite averages are the natural nonasymptotic counterpart of the established asymptotic averaging question in this norm. The exact constants and equality profiles resolve the entire family, including a strict improvement at every even length and the structural difference between zero-weight gaps and a connected positive optimizer. It is not a numerical recomputation at one length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
