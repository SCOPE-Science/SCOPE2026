---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-02.md",
      "INDEPENDENT_AUDIT_2026-10-02.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

From the frozen coefficient vectors I reran the full committed replay.py in an isolated checkout. All five quartic F4 maps and explicit inverses compose to identity in both orders after a common cofactor; F4/F16 base counts are 6/6 for four symmetric maps and 5/7 for the de Jonquieres map. The exact monomial-stabilizer orbit census yields five symmetric orbits of sizes 3,9,18,27,27 among 84 off-coordinate triples; the de Jonquieres quadruple census yields three orbits of 80,240,960. The four chosen symmetric representatives lie in distinct orbits, and homaloidal type separates the fifth. This proves the claimed at-least-five lower bound, not a complete quartic classification.

## originality

PASS

Best-of-knowledge comparison against Resultary and relevant full-text finite-field Cremona works found broad parity/group-structure and degree-three classification, not the five degree-four F4 normal forms with inverse certificates and nonconjugacy lower bound. Failure to locate an exact table is not treated as proof of novelty; the closest implications are explicitly separated below.

## value

PASS

The first nonprime tiny field and two quartic homaloidal types form a natural finite-field birational benchmark. Exact inverse and orbit certificates make the lower bound usable; it is not an arbitrary parameter slice or a claim of a full census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
