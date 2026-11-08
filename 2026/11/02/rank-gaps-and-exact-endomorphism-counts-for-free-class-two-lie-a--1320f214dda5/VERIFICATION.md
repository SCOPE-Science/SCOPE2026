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

For L_d=F_q^d⊕∧²F_q^d (d≥3), bracket alternating even in characteristic two, every endomorphism has block [[A,0],[B,∧²A]], A and B arbitrary. If a=rank A, b=binom(a,2), U=ker A and S=∧²(im A), then im φ∩∧²V=S+B(U), so rank φ=a+b+j with j=rank(U→∧²V/S). Given a, C=binom(d,2), choose M_{d,a}(q) maps A and q^{Ca+b(d−a)} lifts B times rank-j rectangular count R_{C−b,d−a,j}(q); yields exact polynomial. Since C−b=(d−a)(d+a−1)/2≥d−a, j covers 0..d−a and rank support is union [binom(a+1,2), d+binom(a,2)], with adjacent gap max(0,2a−d) and sharp maximal singular rank N−d+1. Matrix corank T_d converges to P(T=t)=q^−t²P∞/P_t² and a random map of ker A into growing quotient is injective whp at fixed t; hence (N−rankφ)/d→T. Independently computed full d=3,q=2 histogram {0:1,1:441,2:8526,3:54264,4:112896,6:86016} and finite d=3,q=3 and d=4,q=2 distributions with exact total q^{d(d+C)}. Finite enumerations alone do not prove d→∞ or all q.

## originality

PASS

Best-of-knowledge full finite-field rank polynomial, exact forbidden intervals and normalized endomorphism corank law are not a special case of inspected characteristic-zero automorphism theory. Explicitly credits universal extension, free Lie exterior-square model and standard finite-field matrix rank formulas.

## value

PASS

The entire image-rank spectrum and sharp holes are structural invariants of a natural endomorphism monoid, and the asymptotic square-matrix-corank limit explains how missing generator rank causes order-d loss in the larger Lie algebra. This is a substantive all-dimension/fixed-field classification, beyond testing an isolated finite sample or the known automorphism criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
