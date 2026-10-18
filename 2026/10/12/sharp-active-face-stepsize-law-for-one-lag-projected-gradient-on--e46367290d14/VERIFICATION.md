---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Coordinatewise scalar recursion y_{k+1}=max(0,y_k−s(y_{k−1}−a)) separates the diagonal problem. For a>=0 and 0<s<1, independently symbolically verified exact Lyapunov decrement E(u−sv,u)−E(u,v)=−s(1−s)u²/(1+s)−s(1−s)v² with E(u,v)=u²−2suv/(1+s)+sv². The projection correction is nonpositive for u>=−a, yielding geometric decay. For a>0,s>=1, eventual interior convergence would obey characteristic roots lambda²−lambda+s=0 with modulus sqrt(s)>=1; only stationary initial pairs can converge, and the exact positive 6-cycle at s=1 witnesses sharpness. For a=0, monotone nonnegative recurrence tends to zero for every s, with y3=y4=0 for s>=1. For a<0, per-step decrease >=s|a| until zero gives the explicit finite cutoff. The proof covers any finite diagonal dimension and arbitrary feasible initial pair, not coupled Hessians.

## originality

PASS

Liu–Wright and collaborators study asynchronous stochastic coordinate descent and proximal updates with stale gradients and general sufficient stepsize/delay conditions. Their indexed primary methods use random coordinate selection/inconsistent updates, not this deterministic simultaneous fixed-lag projected scalar recurrence, and do not provide the if-and-only-if interior-face threshold with unbounded allowed steps on active constraints. No directly matching paper surfaced in Resultary or targeted delayed projection searches. A differently titled deterministic fixed-point recurrence classification could exist; neither stochastic theorem nor a generic spectral bound implies the active-face trichotomy.

## value

PASS

This exact phase diagram isolates an algorithmically consequential distinction between interior and active minimizers: stability ceiling s<1 is necessary only for strictly interior coordinates, while active faces permit arbitrarily large steps and often finite termination. Sharpness and explicit critical six-cycle make the classification a reusable boundary case for delayed projected methods, not a routine unconstrained eigenvalue calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
