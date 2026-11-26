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

At h=2ε/L the smoothness decrement is at least h∑ g_i²√w_i/(ε+√w_i)², where w is the new memory. A nonzero gradient component forces w_i>0, so the decrement is strict off the minimizer. Coercivity bounds x, and the memory filter then bounds v on the same orbit. Vanishing decrements and compactness force x→x_*; the stable filter with input g²→0 yields v→0. Uniform bounds in terms of the initial objective gap and initial memory prove Lyapunov stability in the full state. In the scalar quadratic with L=a and no finite zero, eventually x reverses sign and q_k=|x_{k+1}/x_k|→1. The error y_k−1 for y_k=v_k/(a²x_k²) satisfies an affine recurrence with coefficient β/q_k² eventually bounded strictly below one and forcing tending to zero. Hence y_k→1; telescoping reciprocal amplitudes, whose increments tend to 2a/ε, gives both claimed limits. The finite-hit example is exact: v_1=124/125+1/125=1, h=1, x_1=1/10−(1/5)/2=0. Zero positions remain zero and their memory decays geometrically.

## originality

PASS

The closest primary theorems for the same new-memory update are strict on either side of the threshold and do not establish global stability at equality. The exact scalar dichotomy and constants overlap with a later-indexed scalar Resultary finding; that overlap is credited and no provenance inference depends on its date. In particular it does not supply the general endpoint stability theorem for coupled strongly convex L-smooth objectives and arbitrary initial memory. No earlier matching endpoint theorem or exact limiting law was established in the sources examined.

## value

PASS

The exact step boundary is a natural missing regime: the linearized scalar spatial multiplier is −1 and strict-step geometric estimates cease to apply. The proof extends global stability to that boundary even for coupled smooth strongly convex objectives and arbitrary memory, and the scalar law quantifies the nonlinear slowdown with exact constants and a real finite-hit exception. This changes the boundary classification rather than making a numerical adjustment to a strict step-size bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
