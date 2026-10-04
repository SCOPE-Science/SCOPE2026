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

The symbolic proof establishes the theorem for every integer \(k\ge4\). The executable check is deliberately finite and serves only as a stress test.

`verify.py` constructs the proper Boolean poset \(P_k\) and each rank-representative puncture \(Q_{k,A}\) for \(4\le k\le8\). For every tested pair it verifies the exact point count \(2^k-3\), computes strict upper and lower sets directly, and tests the beat-point definition rather than relying on Hasse-degree heuristics. At the atom and coatom ranks it verifies the stated retraction, image, order preservation, idempotence, and pointwise comparison with the identity. At all internal ranks it confirms that there are no beat points.

The script also counts every chain by dynamic programming and obtains Euler characteristic \(1\) and maximal chain length \(k-1\) for every tested puncture. These two chain statistics are consistent with the symbolic identification of the order complex as a \((k-2)\)-ball, but they are not substituted for that proof.

The universal limitations are explicit: finite enumeration cannot prove the theorem for untested \(k\), and Euler characteristic alone cannot prove contractibility. Those steps are supplied by the written antistar and core arguments.
