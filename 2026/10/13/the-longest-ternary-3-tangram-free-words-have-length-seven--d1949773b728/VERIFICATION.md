---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The 3-cut tangram property is equivalent to containing an image of one of the four minimal doubled-variable patterns S3={AA,ABACBC,ABCACB,ABCBAC}; cf. Ochem–Pierron 2025 §2. Independently expanded all nonerasing ternary substitutions of these patterns through length8, searched all 3^n labeled words for n<=8, and recovered counts 3,6,12,18,30,24,18,0. The 18 length7 survivors split into three symbol-permutation/reversal orbits of six with representatives 0102010,0102101,0121012. The original verifier also uses direct cut and independent incremental suffix enumeration; no accepted length8 word implies no longer accepted word, since any longer contains an initial length8 factor. All conclusions finite and exhaustive.

## originality

PASS

Crucial more recent primary literature: Ochem–Pierron 2025 Theorem 2 ALREADY establishes t(3)=t(4)=4, contrary to the older source-package motivation saying t(3) remained undetermined. Their six-page paper lists S3 but does not give the sharp finite ternary cutoff n8, 18 maximizers or three symmetry classes. Dębski et al. 2024/25 only show sufficiently long ternary words hit cut<=3 and all length8 ternary words have a tangram of unspecified cut. Hence the standalone exact cutoff and census survive as potentially original narrow result, not an open infinite-alphabet problem.

## value

PASS

The minimum unavoidable length and complete extremal family for the first nontrivial tangram cut threshold are motivated finite pattern-avoidance invariants. Despite later t(3)=4 being known, the precise maximal ternary length and orbit profile are not mechanical deductions of the existence/nonexistence of infinite ternary avoiding words. Scope is explicitly finite, not the already-solved infinite t(3) issue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
