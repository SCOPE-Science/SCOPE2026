---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Reconstructed binary carry q*2^t=n+1 and the shared prefix replacement P0 1^t versus P1 0^t; for mixed length-three patterns all internal constant-suffix triples are absent, so the change indicator depends on odd q mod 8 and truncated v2(n+1) (with sparse q=1,3 exceptions). The bundled verify.py explicitly generates local transition table from occurrence parity rather than hardcoding it, checks q equivalences and exceptional stable suffix, enumerates 64 phase classes with at most one divisible-by-16 position in 14 consecutive transitions, enumerates all permitted odd residues and exact rational density weights, then checks first 145 symbols. The finite reduction is mathematically justified by carry locality and 2-adic residue densities; a prefix alone would not prove exhaustion. Independently recomputed 131072 symbols for each of the six words, recovered full spectra and rational frequency agreement. Origin-only runs and density 0 are handled separately. The length-weighted densities equal 1.

## originality

PASS

All six length-three mixed-pattern words and the full rational run-start spectra are not equivalent to the earlier morphic/non-purely-morphic, orthogonality or all-one-run results inspected. The three origin anomalies and explicit frequencies go beyond known general block-counting context; best-of-knowledge with unindexed-automata risk.

## value

PASS

Complete natural six-case classification at first nontrivial mixed pattern length, with exact exceptional boundary runs and positive limiting frequencies; answers local combinatorics of automatic pattern-parity sequences beyond finite sampling and provides precise repeatable benchmark invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
