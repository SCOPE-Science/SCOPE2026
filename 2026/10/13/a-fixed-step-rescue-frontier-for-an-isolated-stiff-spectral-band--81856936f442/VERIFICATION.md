---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

An independent interval-feasibility proof avoids assuming the location of the quadratic extremum. Write w(z)=z(z−1). Tolerance M at z imposes θ ∈ [1/z−M/w(z), 1/z+M/w(z)]. These closed intervals have common intersection iff the lower bound at u is at most the upper bound at v for all u<v (the reverse order imposes no positive constraint). Thus the optimum is the maximum of (1/u−1/v)/(1/w(u)+1/w(v)). Both the positive numerator and the reciprocal of the denominator increase with v, so take v=y. With a=u−1 and b=y−1 the ratio is ab(b−a)/(a(a+1)+b(b+1)). Its derivative in a has the sign of b²−2ab−a², hence its maximum on [x−1,b] is at a=max{x−1,(√2−1)b}. The active pair pins θ uniquely at their coincident interval boundaries; equivalently θ=((u−1)+(y−1))/(w(u)+w(y)), which lies strictly between 1/y and 1/u≤1/x. Substitution gives both frozen formulas, the branch join, and θ<1/2. In the interior branch the inequality M≤1 is d²≤1+2d, equivalent to y≤4+2√2. At fixed width Δ the endpoint branch is eventually active and division by y² yields Δ/2. On [0,2] both factors have magnitude at most one; the spectral theorem then gives the stated Euclidean norm result.

## originality

PASS

The distinct contribution is the explicit fixed-unstable-root minimax classification, not Euler stabilization by a correction packet, equioscillation as a general technique, or an all-band high-frequency cutoff. The strongest inspected published comparisons optimize a different quantity or have incompatible step constraints.

## value

PASS

Prescribing the large step models the already committed unstable update in explicit stabilization. The exact optimum replaces single-frequency sufficiency with robust tuning under band uncertainty, identifies the lower-edge-independent branch, and separates the sharp wide-band cutoff from narrow-band rescue at arbitrarily high frequencies. It gives a usable step and operator norm, not merely a numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
