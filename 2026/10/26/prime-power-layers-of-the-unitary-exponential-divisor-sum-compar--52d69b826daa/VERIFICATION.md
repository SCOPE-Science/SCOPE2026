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

PASS: Verified the local divisor-sum difference equals 1+p^a-q*Delta_a(p), so integrality converts strict inequality to q*Delta<=p^a. For fixed a, Delta=p^d(1+O_a(p^-1)), leading cutoff p^b and prime split T=X^(1/(a+b)). PNT and partial summation give the small-p contribution T^(b+1)/(b(b+1)log^2 T) and large-p T^(b+1)/(b(a-1)log^2 T); the p>T^(1+epsilon) tail is lower order, and diagonal p=q is negligible. Converting log T gives K_a and no a-uniformity. Independent enumeration of p,q up to X=100000 verified exact criterion with counts for a=2,3,4,5 equal 233,87,28,52. These finite counts are not a proof of the limit.

## originality

PASS

PASS (best of knowledge, not priority certification): Compared claims and logical implications with the located primary texts and published records. The specific claim is not stated as covered in the materials actually read; any implicit-specialization or inaccessible-full-text risk is separately documented. Neither matching mathematical terminology nor unsuccessful search alone was treated as conclusive originality evidence.

## value

PASS

PASS: Trudgian motivated the ambient unitary versus exponential divisor-sum density problem. Fixed two-prime exponent layers are the smallest non-squarefree domains in which the local factors compete. The asymptotic, sharp constant and exponent dependence on the divisor lattice of a give natural conditional arithmetic information, not just a finite table or textbook substitution. This does not solve the ambient density problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
