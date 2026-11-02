---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For every analytic Schwarz function omega fixing zero, w=omega(z), s=|w|<=r, the exact differentiation identity 1+zf''/f'=phi(w)+z omega'(z)*(1+1/[2(1+w)]) holds. Coefficient recurrence (n+1)a_{n+1}=(3/2-n)a_n+a_{n-1}, with alternating sign from n=5, yields Re phi(w)>=phi(-s) through s<=17/50 using the positive polynomial 3/2-7s/2-11s^3/8. Schwarz–Pick applied to omega(z)/z gives |z omega'|<=s+(r^2-s^2)/(1-r^2); the lower envelope K_r(s)=phi(-s)-m_r(s)(1+1/[2(1-s)]) decreases with s on 0<=s<=r<=17/50 and equals H(r) at s=r. Canonical omega(z)=z at z=-r attains equality. H decreases and has rigorous sign-changing rational brackets at 1/3 and 17/50, hence one sharp root R, with H<0 just above it. Complex target has Re phi>0 by boundary argument sin theta+theta/4<pi/2, guaranteeing normalized starlike/univalent functions. At r=0 radial order is 1. All quantifiers and r<=R boundary hold; no extrapolation of radial equality above R.

## originality

PASS

Best-of-knowledge: fresh Resultary + independent literature searches, exact same-target 2026 primary full texts, a general Ma–Minda radius full text, and the strongest same-target published interpolation full proof did not imply the sharp full-circle Re(1+zf''/f') profile or its exact convexity radius. Exact Resultary match is the currently assessed result itself, not older independent priority. The formerly inaccessible June same-class preprint was actually read in full accessible arXiv HTML. Unindexed older radius results remain possible; non-detection is not a novelty proof.

## value

PASS

The sharp classical convexity radius of a defined and studied Ma–Minda starlike family is a natural geometric invariant: it is the largest centered subdisk on which every normalized image is convex. The theorem determines a full sharp radial order, a unique exact boundary root, and one extremizer for all r<=R. The target-specific alternating coefficient inequality and Schwarz–Pick optimization are substantive, not a textbook substitution or arbitrary narrow parameter slice. It provides a benchmark to distinguish apple-class starlikeness from local classical convexity; it does not extend to r>R or unrelated targets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
