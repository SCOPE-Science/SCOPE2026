---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS. Joint ordered-pair 2-WL starts at equality/edge/nonedge and separates distance classes through 2^r after r rounds on cycles sufficiently longer than the interaction radius. For a rival union of cycles with shortest component m, s=ceil(log2 m), round s-1 diagonal profiles still match the connected C_n; at round s, a shortest-component vertex has far-color count n-m whereas a C_n vertex has n-1-2^s, differing by 1+2^s-m>0. The Pikhurko–Verbitsky exact diagonal 2-WL/counting-game bridge shifts first distinct diagonal round s to counting-quantifier depth s+1. Non-2-regular same-order rival graphs are separated by vertex-degree counting, and n=3,4,5 have depth 2. Independent implementation of canonical simultaneous 2-WL checked all 137 disjoint-cycle partitions for n=6..18 against s+1; finite enumeration supports, not establishes, the all-n proof.

## originality

PASS

PASS, best of knowledge. Existing 2-WL cycle stabilization and general WL iteration-depth bounds do not imply a lower bound against all same-order graphs or identify balanced disconnected cycles as worst rivals. Pikhurko–Verbitsky supplies the proof technology and game bridge, not the exact cycle-specific all-n characterization. A separately published finite-cycle stabilization-depth result is distinct from global definition depth. An unindexed C^3 cycle folklore theorem remains possible.

## value

PASS

PASS. Exact C^3 definability depth of C_n is a canonical finite-model-theoretic graph invariant. The precise logarithmic threshold, extremal disconnected rivals and round-index correction supply a structural and potentially reusable classification beyond a routine restatement of WL correspondence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
