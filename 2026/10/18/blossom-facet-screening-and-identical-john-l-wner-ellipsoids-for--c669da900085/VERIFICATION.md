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

For even N>=6, the unsigned incidence matrix has BB^T=(N-2)I+J, hence rank N. The uniform c satisfies all genuine inequalities strictly, so both bodies are full dimensional in H_N. With P the tangent projector, P_ee=(N-3)/(N-1), and the coordinate-plane distance is r. For an odd cut of t=s(N-s) edges, B a has sum 2t and squared norm Nt; subtracting its normal component using (BB^T)^(-1) gives ||P a||²=2t(t-N+1)/((N-1)(N-2)). The slack is (t-N+1)/(N-1), so the squared distance divided by r² is (N-2)(N-3)(1-(N-1)/t)/2, at least (N-2)(N-4)/3>1. All coordinate feet are positive in every other coordinate and satisfy all odd cuts strictly. The normalized negative projected coordinate vectors with weights P_ee have zero mean and second moment I on ker B, certifying John optimality for both bodies. For F_N, every coordinate is in [0,1] and their sum is N/2; equality in the bound sum x_e²<=N/2 occurs exactly at perfect matchings. Matching inclusion probabilities for one edge, two incident edges, and two disjoint edges give centered covariance (N-2)P/((N-1)(N-3))=(R²/d)P, yielding the global Löwner certificate for both. Two disjoint half-weight triangles and a matching on the rest give an explicit fractional point violating an odd cut even at N=6. The ratio, dimension-asymptotic and intrinsic volume formulas follow. Replay is the projection and contact computation in RESULT.md §§1–6; the companion verify.py was inspected, not run, and only tests N=6,8,10.

## originality

PASS

The fractional ellipsoids, and the exact circumradius and perfect-matching contact pattern in the even complete-graph setting, have material prior coverage. The supported distinct result is that the integral perfect-matching polytope retains the fractional John ball with strictly positive clearance to every nontrivial odd cut, yielding joint John–Löwner equality for a proper relaxation. This is not a claim of priority for either fractional radius or the outer contact pattern alone.

## value

PASS

Nontrivial odd cuts are essential to integrality and yet all miss the fractional inball by a quantitative uniform margin. Together with the exact enclosing contacts this shows that both canonical ellipsoids miss the strict integrality difference for a natural infinite family. This structural comparison is useful beyond recomputing the old fractional radii or merely recognizing a symmetric ball.

The dated certificate retains the supplied scientific assessment, sources and limitations.
