---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

A non-surjective idempotent must fix a unique contiguous image arc. The omitted complementary path maps to a lazy walk in that arc, proving E_(n,l+1)=n(B_l^(n-l))_(0,l). Tridiagonal cofactor/resolvent gives n[z^(n-2l)]D_(l+1)^(-1). The Perron eigenvalue 1+2cos(pi/(l+2)) and its positive endpoint projection yield phase Phi(x)=x log 3+pi²/(3x²) at l=x n^(1/3); the unique saddle gives the c and kappa constants, with outer tails bounded by lambda_l^N. Step-sum closure yields |W_n|=n(T_n+2). Independent complete step-sequence enumeration for 3<=n<=8 verified every rank and monoid count, including (n,E_n,|W_n|)=(6,157,858) and (8,1025,8872). Asymptotic arguments, not small counts, support the n->infinity result.

## originality

PASS

Best-of-knowledge differentiated same-object formulations and stronger-coverage implications; no confirmed statement-level coverage found. This is a qualified priority decision, not evidence of exhaustive absence.

## value

PASS

The idempotents/retractions of a natural graph-endomorphism monoid are classified by image size, with an explicit random-rank scale and stretched-exponential density. This answers a motivated semigroup counting question; distinguishing weak from strict edge-preserving maps changes the underlying path family and exponential base.

The dated certificate retains the supplied scientific assessment, sources and limitations.
