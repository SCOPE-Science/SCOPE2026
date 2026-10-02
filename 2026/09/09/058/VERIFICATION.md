---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
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

The raw witness partition has u0 connected in the background to v1 and all four x/y copies while v0 is isolated; no choice of the five incident w-edges can reach v0, so the signed conditional difference is exactly -1 in every one of 32 states. The symmetrized witness similarly fixes the two signed terms at -1/2 each and is exactly -1. Independent enumeration reproduced 877 raw partitions with 233 grid-negative and 4140 symmetrized partitions with 1107 grid-negative. The counts remain explicitly labeled grid-screening, while the two constant witnesses are exact.

## originality

PASS

Searches found the general bunkbed counterexample and Denart’s cactus/biconnected-component results, but no prior statement of this exact degree-2 conditional-partition no-go lemma or the symmetrized constant -1 witness.

## value

PASS

A concrete exact obstruction to the most natural degree-2 induction step is a motivated boundary result for the unresolved series-parallel direction. The symmetrized -1 witness shows that even exploiting layer-swap symmetry does not rescue partitionwise domination, forcing any successful proof to use realizability or correlations rather than a pointwise inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
