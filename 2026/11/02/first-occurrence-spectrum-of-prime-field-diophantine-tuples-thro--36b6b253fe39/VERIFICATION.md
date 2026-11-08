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

Reconstructed G_p on F_p^* with adjacency iff ab+1 mod p is in the set {r^2:r mod p}, zero included. A desired tuple is exactly a clique. Read frozen verify.py and all 70 rows of SPECTRUM.csv; checked branch-and-bound correctness: each candidate pool is partitioned by choosing a vertex, greedy independent color classes give valid clique upper bound for each processed prefix, and pruning only occurs if bound <= actual best. Independent DIFFERENT exact bitset coloring and recursive clique algorithm computed omega(G_p) for ALL 70 odd primes 3..353 and reproduced every first-prime threshold and M(353)=12, with direct verification of all 66 pairs of twelve-element witness. The proof is exhaustive finite computation, not a heuristic random search or extrapolation to larger primes.

## originality

PASS

Dujella–Kazalicki 2021 covers finite-field tuple basics and small m plus modular-form counts; Kim–Yip–Yoo 2024 covers explicit constructions and general growth. Neither accessible full-text result supplies exact minimal odd primes across m=2..12 or the 70-graph maximum-clique census. First few classical thresholds not individually claimed novel; surviving contribution is complete finite initial spectrum.

## value

PASS

The least field size for a fixed Diophantine tuple cardinality is a natural threshold invariant. The eleven-value first-occurrence spectrum through 12, with transparent proof of exhaustive finite search, provides an independently reusable benchmark; no general asymptotic theorem is required to make a complete motivated finite classification valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
