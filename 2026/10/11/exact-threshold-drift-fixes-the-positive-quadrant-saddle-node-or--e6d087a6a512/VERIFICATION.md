---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For the stated physical-time two-patch ODE, set A=1+D1, q=1-D2/A and m=aq with 0<a<q. Independent expansion gives d[(D1/A)x1+x2]/dt=x2^2(q-a-x2)/(x2+a) and the off-diagonal positive couplings make x2 eventually positive for every nonzero nonnegative initial state. A hypothetical approach to zero would make the strictly positive weighted coordinate eventually nondecreasing, contradicting its vanishing. The Jacobian J=[[-A,D2],[D1,-D1D2/A]] has eigenvalues 0, -(A+D1D2/A), right nullvector v=(D2/A,1) and left w=(D1/A,1). The second equation has quadratic coefficient (q-a)/a along v; left/right projection gives κ=((q-a)/a)/(1+D1D2/A²)=A²(q-a)/(a(A²+D1D2))>0 when x2=u+O(u²). Thus the positive center side is repelling in forward physical time. Valid only m=aq, 0<a<q; no statement for positive E3 collision or a≥q.

## originality

PASS

Best-of-knowledge distinct exact weighted drift and normalized positive center coefficient correct the forward-time interpretation of the primary source. The source itself already says first-quadrant instability in Corollary 2.1: the qualitative exclusion alone is NOT claimed new. Distinct content is the exact model-specific identity, rigorous no-approach mechanism, and explicit orientation coefficient explaining the internal terminology conflict. No implication from the source’s saddle-node classification alone produces that identity.

## value

PASS

The invariant removes a genuine forward/backward-time stability ambiguity at the precise extinction/persistence threshold; κ determines the physical-side parabolic drift and the U identity gives a global exclusion argument for every nonzero nonnegative trajectory near the origin. The exact coefficient is a useful correction for interpreting threshold slow dynamics, not merely a relabelled saddle-node.

The dated certificate retains the supplied scientific assessment, sources and limitations.
