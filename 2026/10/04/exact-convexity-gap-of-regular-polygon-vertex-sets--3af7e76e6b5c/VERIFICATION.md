---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

Using cyclic vertex separation k (1<=k<=floor(n/2)), the exact minimax center distance equals chord length d_{ceil(k/2)} because cyclic index triangle inequality gives the lower bound and the shorter-arc midpoint vertex attains it. Thus leipodistance g_k=4R*sin(ceil(k/2)*pi/n)-2R*sin(k*pi/n). Every even k is dominated by preceding odd k, and for odd k=2m+1 the derivative of F(u)=4R*sin(u)-2R*sin(2u-pi/n) is 4R*(cos(u)-cos(2u-pi/n))>=0 throughout the admissible interval. The largest allowed odd k maximizes; substitution gives all four residue-class formulas and Taylor expansions, with limiting circle gap 2(sqrt(2)-1)R. Independently enumerated all vertex-pair/vertex-center minimaxes for n=3..50 and matched the exact formula numerically; the proof is all-n and finite enumeration was only a check.

## originality

PASS

The defining Geller–Misiurewicz source computes the gap of a full Euclidean circle and a Hausdorff continuity bound, not the exact finite regular-vertex gaps or their mod-four sampling oscillation. Those prior claims cannot imply the exact maximizer or coefficients. No covering prior theorem was located in accessible inspected material; current corpus search unavailability and alias risks are recorded.

## value

PASS

Regular polygon vertex sets are the canonical finite equispaced approximations of the circle, the defining benchmark for this recent metric midpoint-defect invariant. Exact finite values, extremizing separations and four distinct convergence modes supply a meaningful complete natural classification and reveal an arithmetic sampling effect not provided by Hausdorff stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
