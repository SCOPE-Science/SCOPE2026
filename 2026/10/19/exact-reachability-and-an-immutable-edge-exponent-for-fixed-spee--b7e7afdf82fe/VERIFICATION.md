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

The normalized stationary position density follows by zero aggregate flux and the orientation equation (polarization (x/R)ρ); the orientation factors then give a leading cumulative edge layer of power β+1 for the plus state and an extra power for the minus state. The pathwise deficit is the sum of the compressed initial deficit and a nonnegative weighted negative-orientation occupation time; the weight is at least s>0. The plus/no-switch event exactly provides the stated coefficient. A switched plus trajectory in the edge layer needs its first switch near T or a close pair; the Poisson intensity and second factorial moment give an O(ε) bound independent of initial position conditional on orientation. Initial minus states are already subleading. This proves the sharp relative O(ε) remainder as well as conservation, including −1<β<0. The frontier is attained as a support supremum by the no-switch trajectories, satisfies R'=v−κR<v, and therefore enforces a strict expansion bound. Under the strict bound a smooth monotone radius path can use a normalized almost-flat derivative on the interior with endpoint values zero; the controls are strictly positive and match the prescribed values. Differentiating X=R(t)Y(q(t)) with q'=v/R, and transforming the independent flips, proves equality of the whole joint law for the constructed path. As a separate algebraic check, `python /workspace/independent_checks_1_4.py 4` verifies the full even-position/odd-polarization moment recurrence for the scaled stationary shape; it is not used in place of the exact path and time-change arguments.

## originality

PASS

The distinct claim is the sharp arbitrary-protocol finite-time edge invariant and complete reachable-state criterion under the stated regular athermal fixed-speed actuators. The stationary beta density, moment equations, and scale-control idea have precedents and are not new here.

## value

PASS

The primary model explicitly motivates shortcuts between states with different edge shapes. Determining what is exactly impossible, not just how to match a few moments approximately, resolves a concrete control question. The allowed transfers are constructive and the strict time bound is sharp with no imposed common control-amplitude cap; the tail invariant also applies away from the final stationary family. No claims about thermal, impulsive, or amplitude-constrained controls are needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
