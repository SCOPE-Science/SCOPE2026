---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For hull of coaxial balls H(t)=max_j(r_j+c_j t), the width g(t)=H(t)+H(-t), t=|u.e|, is continuous convex even/nondecreasing on [0,1]. The distribution of t has strictly increasing CDF F_d=I_{t^2}(1/2,(d-1)/2), so quantiles of g(T) reconstruct g and the axial support of K-K. For two nonnested balls (radii R>=r, separation L>R-r), g(t)=max(2R,R+r+Lt); the minimum m=2R, maximum M=R+r+L and atom q=F_d((R-r)/L) invert to L=(M-m)/(1-theta), r=R-theta L, theta=F_d^{-1}(q). Three-ball examples A=((0,2/5),(1,3/10),(2,1/10)) and B=((-1,1/5),(0,2/5),(1,3/10)) have g(t)=4/5+(|t|-1/10)_++(|t|-1/5)_+ exactly for all directions. All component balls are pairwise disjoint and exposed on open normal intervals, but the exposed spherical radius multisets differ, precluding congruence. Independent exact Fraction checks verified 401 rational directional identities and a two-ball inverse grid.

## originality

PASS

Independent statement/implication comparisons found no decisive prior coverage of the exact assessed theorem, with explicit caveats. A generic difference-body identity does not alone give inversion from the unlabeled law on this restricted coaxial subclass or two-ball component parameter identification.

## value

PASS

Random widths and unlabeled projection measurements are natural geometric tomography data. The theorem gives a complete recoverable invariant (the central difference body), precise recovery formulas for the minimal nontrivial ball family, and an explicit sharp counterexample already at three disjoint individually exposed components. The two-versus-three identifiability boundary is stronger than generic difference-body nonuniqueness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
