---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Rescaling by the axes identifies the normalized law with a signed Dirichlet vector with d unit parameters and slack alpha+1. Each coordinate magnitude T is Beta(1,m), with second moment 2/((m+1)(m+2)); sign symmetry diagonalizes the Gram matrix. The resulting row 1+c sum_i x_i y_i/a_i² uses c=(m+1)(m+2)/2>1. The row mass is convex, and distinct vertex rows have opposite signs on positive-measure interior sets close to the negative of a vertex, so equality is possible only at a vertex. At a vertex the excess over 1 equals E(cT−1)_+ = c integral_[1/c,1] (1−t)^m dt, giving the formula. The sign row and negative-set indicator yield the two claimed extremal values by unit row mass, and self-adjointness gives L1 duality. Full support and affine continuity justify vertex values for essential suprema. For excess F and b=1−2/((m+1)(m+2)), differentiation and log b>−(1−b)/b give (log F)'>(m²+5m+2)/(m(m+2)(m+3))>0. Expansion b^m=1−2/m+8/m²+O(m^-3) gives the stated norm; E(sum |Y_i|/a_i)=d/(m+1) proves weak concentration at fixed d. This includes d=1 and all m>d−1 in fixed d. Replay: RESULT.md lines 25–58. VERIFICATION.md and verify.py describe 204 finite exact/symbolic/high-precision checks; the supplied script was inspected but not executed.

## originality

PASS

The October 18 unweighted solid result gives exactly the same norm at m=d and the October 25 surface result gives the excluded boundary limit m=d−1. The weighted result deserves no independent credit for those cases, coordinate rescaling, or the old integer scalar values. The inspected simplex results concern different laws. The supported distinct claim is the signed slack-weighted family for all real alpha>−1, including its sharp monotonicity in real m, unique norming evaluations, and concentration-versus-amplification behavior. No inspected result gives that family.

## value

PASS

The radial slack exponent changes observation concentration without changing the affine space, and the exact formula quantifies the resulting stability and worst negative excursion throughout that natural family. In particular weak concentration at one site can coexist with linearly diverging amplification; the real-parameter law and strict vertex geometry add useful information beyond recomputing the unweighted constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
