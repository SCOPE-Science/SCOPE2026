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

At the specified marked trapezoid the closure Jacobian in the last two angles has determinant sin(pi/3), so the chart is smooth and locally covers all nearby shapes with the given marking. The chain remains simple near the reference, and the only turn whose sign can change is delta. Differentiating closure gives last-angle increments delta-alpha and alpha. The five varying diagonal distances have aggregate first variation h*delta, with h=sqrt(3)/2 and S(0)=9+2sqrt(3). An interior direction between edge normals cannot minimize the positive width, since the support pair is fixed and the width has second derivative minus itself. The two oblique edge-normal families have reference width 2h and drop out. For the other three, direct support projection gives width increments (delta+|delta-alpha|)/2, (delta+|alpha|)/2, and delta/2+max(0,-alpha,alpha-delta). Their minimum is max(delta,alpha,delta-alpha)/2 at first order, including chamber boundaries. Taylor errors remain uniformly quadratic under the finite minima and maxima. Division gives the claimed first variation; comparing the loss with delta+|alpha| in the three chambers gives equality of the linear bound only at alpha=delta>0. That ray stays in the strictly convex domain and proves sharpness. This proves a local result, not the unrestricted global inequality.

## originality

PASS

The nearest verified result has the same objective, reference geometry and extremal value, but only on a reflection-symmetric family. The accepted contribution is the first-order law in both independent shape directions, including the switching of supporting widths, and the sharp coordinate-dependent local loss; neither the common value nor the trapezoidal candidate is credited as new. On the statements inspected, no covering result was established.

## value

PASS

For the distance/width extremal problem, the symmetric calculation leaves open asymmetric directions of improvement at the proposed optimizer. The result rules out all such nearby directions, identifies the three competing support families and gives the worst local loss in the declared coordinates. That is useful local information about the conjecture without pretending to prove the global bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
