---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The cited Kaneko--Stoll theorem was independently checked in accessible primary full text: for output binary weight three and \(\max\{\ell,m\}\ge3\), it gives \(ab<2^{-13+4\ell m}\), which specializes to \(ab<2048\) for weights two and three. Every odd weight-two factor is \(1+2^u\), every odd weight-three factor is \(1+2^v+2^w\) with \(1\le v<w\), and the strict product bound leaves 119 exponent triples. An independent direct integer enumeration reproduced exactly \((3,7,21)\) and \((5,7,35)\) and no others.

## originality

PASS

The exact two-solution classification is not present in the primary Kaneko--Stoll paper and is not implied without resolving the remaining finite search. The prior theorem supplies the global cutoff; the audited result completes the first asymmetric fixed-weight case and targeted exact searches found no earlier table. This is original best-of-knowledge despite using a published bound as a premise.

## value

PASS

The primary source explicitly presents existence for fixed binary-weight triples as a natural unresolved classification problem. The audited case is the first asymmetric triple immediately beyond the exceptional infinite weight-two/weight-two family; closing it exactly is therefore a motivated finite classification, not an arbitrary parameter slice. The 119-case census is exhaustive because a nontrivial published theorem supplies the global cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
