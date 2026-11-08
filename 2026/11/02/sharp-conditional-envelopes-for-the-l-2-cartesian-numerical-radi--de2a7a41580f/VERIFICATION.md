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

For bounded nonzero T on a complex Hilbert space, min over phases of ||Re(e^{-iθ}T)|| equals the distance d(T) to phase multiples of self-adjoint operators. The centrally symmetrized closed numerical range K has support h equal to these norms, circumradius R and inradius uR=d. The convex-body containments conv(u disk, ±v) ⊂ K ⊂ disk∩{|Re(z conj w)|<=u} yield L(u) <= Q^2/R^2 <= U(u), with L=u^2+[(1-2u^2) arccos u+u sqrt(1-u^2)]/pi and U=1-[arccos u-u sqrt(1-u^2)]/pi. Support uniqueness forces equality bodies; Minkowski interpolation preserves u,R and normal diagonal spectrum realizes every intermediate value. L’(u)=4u asin(u)/pi and the small-u expansion prove the optimal global 4/(3pi) cubic coefficient. Independently evaluated the analytic width and squared-support integrals for six u values with 400000 phase samples and matched <=3e-7; Hilbert-space quantification rests on geometric proof.

## originality

PASS

Qualified PASS: the original 2026 L2-Cartesian operator radius article proves only unconditional comparison. Prior published quantitative stability theorem uses the exact same d(T) and establishes cubic exponent and smaller nonoptimal coefficient 1/(2pi), expressly leaving best coefficient unknown. The entire sharp L(u),U(u) interval, both extremal bodies and best 4/(3pi) coefficient are additional, not a notation change. A prior convex-geometry support integral extremal theorem with other terminology remains possible.

## value

PASS

A complete sharp conditional range for the new operator numerical radius, including realizations, two geometric rigidity classes and optimal stability constant, is a natural general operator-theoretic classification with interpretation via inradius/circumradius of the symmetrized numerical range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
