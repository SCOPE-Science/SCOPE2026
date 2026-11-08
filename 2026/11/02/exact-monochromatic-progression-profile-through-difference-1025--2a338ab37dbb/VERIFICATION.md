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

The base-four parity digit formula t_{Bm+r}=t_m xor t_r for B a fourth power is proved by substitution. For B>1031*d, each progression of length <=1032 crosses at most one high-digit boundary. The choices m=0 (same low colors) and m=1 (opposite colors) make the separate before/after low-bit-constant criterion necessary and sufficient over EVERY starting position. Intersecting exact masks over all B residues proves existence and its first failure for each d; no cap is attained. Independently reimplemented a different residue bit-mask enumerator for all 1,025 d, including witness-start reconstruction; generated the exact same 11,605-byte AP_PROFILE.csv (Git blob SHA 5b536a833af2f8442256e68ff1b250d60f0bba82). The resulting unique maxima/second values are (65,66,64), (255,260,258), (1025,1026,1024). These are exhaustive finite-difference proofs, not infinite-difference conclusions.

## originality

PASS

Aedo–Grimm–Nagai–Staynova formulate the same generalized Morse-like fixed point and conjecture the optimal progression lengths at substitution scales; published propositions show specific long progressions, not comparison against all smaller differences through 1025. The later automatic-group paper concerns general growth bounds. The identical 1,025-row table was not identified in targeted published-findings searches, but unpublished/collateral computation is possible.

## value

PASS

Cutoffs 4^3+1=65, 4^4+1=257 and 4^5+1=1025 are dictated by Conjecture 30, not arbitrary range slices. An exact all-differences profile and uniqueness of maximizing shifts resolves three concrete finite conjecture scales and yields exact witnesses useful for future patterns.

The dated certificate retains the supplied scientific assessment, sources and limitations.
