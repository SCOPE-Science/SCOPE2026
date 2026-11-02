---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The trace quadratic form Q(x)=Tr(ax^(p^h+1)+bx^2) has polar radical cut out by a x^(p^h)+a^(p^(2n-h))x^(p^(2n-h))+2bx=0 for n>=h; applying Frobenius yields an order-two semilinear recurrence over fixed field F_(p^d), d=gcd(h,2n), with invertible companion matrix. The fixed-vector lemma (minimal K-dependence of k-independent semilinear solutions) bounds radical dimension r<=2d over F_p, and each nonzero scalar quadratic Gauss sum has modulus p^(n+r/2). Triangle inequality gives the uniform bound; Hasse extremal deviation (p-1)p^(n+h) implies d=h. For n<h the Hasse value exceeds point-count constraints; n=h,b!=0 cannot have full polar radical because nontrivial Frobenius and identity maps are independent. Independent direct F9 trace and point count for nine (a,b) nonzero pairs corroborates boundary; the proof is symbolic for arbitrary p,n,h.

## originality

PASS

Fixed-field divisibility h|2n is not stated in the accessed most relevant Cartesian-specialized results. The 2014 quadratic-form framework and 2024 Chen Dickson-matrix classification could subsume it through a nontrivial specialization; this remains substantive priority risk, with primary text comparison distinguishing their hypotheses and explicit implications.

## value

PASS

A coefficient-uniform necessary arithmetic obstruction for a naturally sparse two-term Artin–Schreier family, filtering entire extension-degree families not excluded by the general lower degree n>=h+1 bound. It is a structural semilinear rank theorem and useful arithmetic search cutoff, not mere computation and not an existence classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
