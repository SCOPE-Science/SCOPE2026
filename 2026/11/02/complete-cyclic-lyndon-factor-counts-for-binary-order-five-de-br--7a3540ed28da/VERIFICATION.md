---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the finite census

Run `python3 checker.py`. The complete run from the embedded checker returned `VERIFY_OK` after checking all 65,536 Boolean feedback maps, obtaining 2,048 single-orbit maps and verifying 65,536 root factorizations. This requires Python 3.9+ and no external dependencies.

The first enumerator visits each Boolean function on sixteen four-bit contexts. Its necessary-and-sufficient full-cycle predicate and one-to-one anchoring at the unique all-zero five-bit block prove global completeness, not merely a test sample. The independent enumerator searches edge-simple Euler circuits in the sixteen-vertex de Bruijn graph. It reproduces the exact canonical cycle set. The two different factorization implementations, Duval's algorithm and a definition-level Lyndon-prefix search with explicit non-increasing-order validation, agree for every root.

The exact distribution counters are compared with both tables in RESULT.md. In the source run, the root counts totaled 65,536; the per-cycle maximum counts totaled 2,048; and both extremal witnesses had exactly 16 Lyndon factors. Execution is finite, deterministic and integer-only. No extrapolation to orders other than five or claims of independent validation are made.
