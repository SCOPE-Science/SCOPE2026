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

PASS: From actual composition domains [a,b]∩[c−d,f−d] and [c,f]∩[a−e,b−e], equality of two nonempty product intervals is an iff endpoint criterion. Its sign-case partition is disjoint: both zero shifts give binom(n+1,2)^2−2binom(n+2,4), exactly one zero contributes four binom(n+3,5), both positive/negative give two binom(n+1,4), opposite signs impossible by inconsistent left endpoints. Each parametrization is bijective, so holds for all n≥2. Together with independent mutual-annihilation Z_n and zero-factor count 2N_n−1 it gives C_n and 3/10+3/(10n)+15/(8n²)+O(n^-3). Independent direct composition over all enumerated partial-map pairs for n≤8 checked 74,732 ordered pairs; finite tests corroborate rather than prove all n.

## originality

PASS

Best-knowledge PASS, qualified. Fikioris–Fikioris establish the consecutive-diagonal interval-translation submonoid and triple product; prior mutually annihilating count and limiting 3/10 commutation probability are expressly credited. The result assessed is the exact complementary P_n count, shift-sign classification, and finite-size corrections. The inspected original full PDF and extension do not state this enumeration. Konieczny 2020 full inverse-semigroup centralizer theory (only abstract read) could indirectly imply a stronger count; this remains a priority risk.

## value

PASS

PASS: Exact commuting-pair enumeration is a natural finite semigroup invariant; the nonzero-product sector is structurally different from the already known annihilating sector. A complete polynomial and shift-sign obstruction plus explicit 1/n corrections are meaningful classification results rather than merely a one-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
