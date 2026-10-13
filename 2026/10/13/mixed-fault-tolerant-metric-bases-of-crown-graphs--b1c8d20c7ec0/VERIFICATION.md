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
# Verification

The checker constructs \(\operatorname{Cr}_n\), computes all-pairs vertex distances by breadth-first search, and represents every mixed element as either a vertex or an edge.

For every pair of distinct mixed elements, it precomputes the exact set of landmarks that distinguish the pair. A landmark set is mixed fault-tolerant exactly when every such distinguisher set meets it in at least two vertices.

For every \(4\le n\le9\), the verifier exhaustively checks every vertex subset of size at most \(n\). It rejects all smaller sets and compares every size-\(n\) set with the deleted-matching-transversal and orientation theorem.

It also independently checks, for every omitted matched pair and every orientation of all remaining pairs, the one-hole mixed-resolving lemma used in the proof.

Recorded output:

```text
VERIFY_OK
crown_parameters_checked = [4, 5, 6, 7, 8, 9]
subset_trials_size_at_most_n = 207804
minimum_mft_bases_checked = 334
one_hole_transversal_trials = 4080
all sets smaller than n failed mixed fault tolerance
all size-n MFT bases matched the transversal/orientation theorem
all one-hole transversals matched the mixed-resolving lemma
```

The finite enumeration is corroborative only. The theorem for all \(n\ge4\) follows from the proof.
