---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Write Q(q)=∏_{j>=1}(1+q^j). Distinct-part marking gives q^(-k) ∑_n(A_k(n)-A_(k+1)(n))q^n=(1-q)∏_{j not in {k,k+1}}(1+q^j) as formal series. Binary-expansion factorization (1-q)∏_i(1+q^(2^i))=1 reduces generic adjacent nonpowers-of-2 to manifestly nonnegative restricted distinct-part product. If k or k+1 is m=2^s>=8, the remaining quotient has denominator (1+q^m). Numerator includes 1+q^(3m), quotient exactly 1-q^m+q^(2m). With h=m/8, the five distinct available nonpower-of-2 factors indexed T+=(3,5,6,7,10)h, except (m,b)=(8,7) where T-=(3,5,6,10,14)h, yield P±(q^h). Both finite integer polynomials (1-z^8+z^16)∏_(a in T±)(1+z^a) have all nonnegative coefficients, independently reconstructed (48 and 55 coefficients, minimum 0, sum32); remaining formal factors are nonnegative, proving every A_k(n)-A_(k+1)(n)>=0 for k>=5. Finite independent DP additionally checked 21,895 comparisons to n=150 but is not the all-n proof. Telescoping over residues yields all-n D_r,t>=D_s,t for t>=6,5<=r<s<=t.

## originality

PASS

Best-of-knowledge PASS for a uniform all-n ALL-MODULI part-frequency inequality on residues >=5. Craig (2022) proved fixed-modulus eventual inequalities in general and all n>8 only when modulus <=10, and listed numerical potential exceptional (r,s,n) involving residues <=4; it did not give this all-moduli partial theorem in the inspected abstract and source notes. Sellers–Sills–Mullen (2004) supply Guy’s classical no-powers-of-two distinct-part bijection, which explains the generic binary factorization but does not handle adjacent pairs straddling 2^s via the two finite positivity polynomials. The exact two-certificate argument is additional, not a renaming of the classical identity. Craig full primary text unavailable via OA/arXiv and Oxford VPN disconnected; possible implicit theorem remains risk.

## value

PASS

This proves a natural infinite-domain slice of Craig’s open all-modulus distinct-part frequency ordering problem, with no bound on n or modulus, and eliminates every power-of-two exception above 8 by two universal finite positivity certificates. It reduces the missing adjacent inequalities to k=1..4 while yielding a concrete positive partition interpretation for all generic k. This is a motivated substantial combinatorial threshold and not merely a small-degree verification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
