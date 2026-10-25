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

# Reproduction

Run the standalone Python 3 standard-library script with `python3 verify_partition.py` in a directory containing that file. The exact program output is included as `verification_output.txt`, ending in `VERIFY_OK`.

The script enumerates all partition-transfer graph cliques for \(1\le n\le16\), including \(8{,}932\) faces, using direct Ferrers symmetric-difference adjacency. It separately enumerates removable/addable Young corner choices in \(153\) parameter pairs up to \(n=18\), computes the proposed product coefficients up to \(n=65\), compares published face and homology tables, and tests first-occurrence thresholds for clique sizes \(2\) through \(10\). The Euler-Betti series test serves solely as a consistency check and is not claimed new. The script is deterministic and has no network or nonstandard dependencies.

# Scientific limits

Finite enumeration tests the implementation and sampled instances only; it does not certify every integer \(n\) or every \(r\). General validity follows from the proof's exact incidence uniqueness and formal partition-series manipulations, dependent on the published star/top classification. No independent audit has been performed.
