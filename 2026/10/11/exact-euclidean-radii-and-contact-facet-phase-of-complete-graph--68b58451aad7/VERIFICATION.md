---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The theorem is proved analytically in `RESULT.md`; the accompanying finite checker is corroborative only.

Source-dependent checks:
- The first public arXiv version is dated 2024-07-11.
- The published article lists MSC 52B05 first, followed by 52B12 and 52B20.
- Proposition 3 in the inspected full text gives the irredundant matching-polytope inequalities: nonnegativity, essential-vertex degree inequalities, and induced 2-connected factor-critical odd-set inequalities.

Mathematical checks:
- Group averaging preserves an inball radius and reduces an optimal center to a constant edge vector.
- The degree-facet balance value is \(1/(n-1+\sqrt{n-1})\).
- The odd-set balance value at size \(s\) is \(1/(s+\sqrt{2s/(s-1)})\), and the denominator increases with \(s\).
- The comparison leaves blossom control only for \(n=3,5,7\), a tie at \(n=4\), and degree control for \(n=6\) and every \(n\ge8\).
- The active shrunken facet and the coordinate lower bounds force uniqueness of the incenter.
- For a constant circumcenter coordinate \(q\), a matching of size \(j\) has squared distance \(j(1-2q)+\binom n2 q^2\); minimization at the maximum matching size gives the displayed center and radius.

`verify.py` enumerates all matchings of \(K_n\) for \(2\le n\le8\), evaluates every relevant facet orbit at the proposed incenter, checks the tangent phase, and checks the circumradius against every matching vertex.
