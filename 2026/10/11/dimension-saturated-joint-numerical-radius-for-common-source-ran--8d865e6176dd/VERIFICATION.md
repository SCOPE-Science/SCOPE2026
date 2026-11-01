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

Reconstructed the exact norm N²=A²+Σ_{j=1}^q s_j², obtained 4W²≥A²+s_1² by averaging squared joint evaluations at (v±y)/√2 with ||S*y||=s_1, and subtracted N²/q to get (q−1)A²/q+Σ_j(s_1²−s_j²)/q≥0. In the orthogonal-source case W=s_1/2 exactly. q>1 equality forces A=0 and rank-q equal nonzero singular values; q=1 requires the separate t-perturbation: averaged squared value t²A²+t(1−t)s_1² has strictly positive derivative A² at t=1/2 unless A=0. Coordinate partial-isometries attain the infimum over both real and complex fields. Under N=1, ε near-minimality yields the stated bounds. Independent deterministic tests use four explicit tight-frame/orthogonal witnesses, one exact q=1 strictness inequality, and 1,400 random real/complex spectral-deficit identities. These do not prove arbitrary dimensions; the analytic argument does.

## originality

PASS

Best-of-knowledge: the finite-Hilbert global index for k<m is credited to Mal, while the new restricted k>=m saturation, both-field tight-frame/orthogonal equalizers, and quantitative spectral deficit are not implied by the materially inspected primary theorems. Results mirror for the assigned finding is not independent priority. The original Drnovšek–Müller article remains a real access-limited risk, not a fabricated noncoverage finding.

## value

PASS

The restricted class is the natural common-source rank-one mechanism used in Mal’s Hilbert joint-index sharpness witness. Its exact finite ambient-dimensional saturation at k=m−1 resolves a meaningful parameter regime left by that construction. The complete equality characterization identifies orthogonal systems when k<=m−1 and redundant tight frames when k>=m−1, while a nontrivial spectral deficit controls near-minimizers and source leakage. It is independently useful even without a theorem about arbitrary operator tuples; simple standard matrix inequalities are ingredients but do not by themselves communicate the fixed-m classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
