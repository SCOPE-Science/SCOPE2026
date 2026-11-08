---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

At scale m=b^k the 1-islands S_k are separated by runs of length g*b^r where g=(b-2)m, r=nu_2(j); adjacent gaps cannot both be minimal. The first-to-third island separation exceeds a 2p window, p=(b-1)m. A nonzero square of period p therefore pairs two islands at the minimum gap and must start x in [-g,0]; its literal root is exactly 0^a S_k 0^(g-a). Every a is attained at an internal minimum-gap pair. The unique longest circular zero run in S_k 0^g makes it primitive. This proves exactly g+1 distinct nonzero roots for all b>=3,k>=0; the zero square is deliberately excluded. The source standalone checker was read, and independent direct substitution/digit/square enumeration verified 16 bounded (b,k) cases, not the infinite claim.

## originality

PASS

The closest same-word Bell–Shallit result counts cyclic conjugacy classes of finite factors (Lie complexity), not which conjugates have contiguous square occurrences; an entire conjugacy class of factors does not imply all its squares occur. Generalized Cantor palindromic and k-Abelian papers study other invariants. Search of published findings and primary literature found no equivalent root-set classification, with unindexed repetition theory retained as risk.

## value

PASS

For the canonical Cantor/Sierpinski morphic family, square-root multiplicity at the intrinsic period (b-1)b^k measures the precise fraction of conjugate words realizing immediate repeats. A complete all-b,k classification and primitive-root guarantee are natural combinatorics-on-words invariants, not a recoding of known factor-class counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
