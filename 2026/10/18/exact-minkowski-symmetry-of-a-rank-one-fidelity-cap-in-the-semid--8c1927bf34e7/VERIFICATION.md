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

Writing s=d-1, any feasible center can be averaged over the stabilizer of P to Z_q=(1-q)P+q(I-P)/s. The cap constraint at X=P forces (1+alpha)q≤delta. All extreme points of the cap are pure: on any support of rank at least two the self-adjoint perturbation space has dimension at least three, so a nonzero perturbation preserving both traces remains feasible in both signs for small amplitude. For a pure state at transverse weight t, positivity of reflection is equivalent to alpha/(1+alpha) times [(1-t)/(1-q)+s t/q] being at most one. At q*=delta/(1+alpha*)<s/(s+1) the worst state has t=delta, and equality is exactly the defining quadratic. The reflection is trace-one and satisfies the linear cap constraint. For alpha>alpha*, all possible averaged centers would have 0<q<q*; the function G(q) at t=delta is strictly decreasing up to q*, since its minimizer is at least min(delta,s/(s+1)). Therefore G(q)>G(q*) while (1+alpha)/alpha decreases, excluding a better factor. Implicit differentiation gives strict monotonicity using f(1/d)=-1/d². The two endpoint limits and the special width follow by substitution/continuity; delta=0 is excluded, and all reflection factors would be feasible for its singleton.

## originality

PASS

The distinct result is the all-dimensional rank-one PSD-cap symmetry law and attaining center, including PSD bodies that are not balls. The index and the half-ball special case are classical; a later indexed ball-truncation law is exactly equivalent to both d=2 matrix slices and should not be counted as a distinct mathematical phenomenon in those slices.

## value

PASS

The cap is the natural trace-one PSD section imposing a fidelity lower bound to a fixed pure state. The calculation gives an exact optimal reflection factor and a usable center, distinguishes singular narrow caps from their collapsed point, and gives a dimension- and width-dependent input to a general rounding estimate. The higher-size result goes beyond the ball case without claiming optimality for that rounding estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
