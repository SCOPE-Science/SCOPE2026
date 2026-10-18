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

# Verification record

Run the standalone `check.py` with Python 3. It generates paperfolding bits directly from their odd-part definition; independently, it enumerates conditional \((c,\omega)\) sets by the exact interleaving recurrence. For all lengths \(2^k\) with \(1\le k\le9\), complete sets from a direct sliding-window scan of the first \(131072\) symbols equal the recurrence sets. For \(2\le k\le11\), checks also verify the exact total \(2^{k+1}+k+1\), the two outer tiers' starting-parity disjointness and cardinality, and the central arithmetic progression. The successful terminal marker is `PAPERFOLDING_DYADIC_2_BINOMIAL_ALL_CHECKS_PASSED`.

The finite sliding prefix cannot establish completeness for infinitely many starting positions, or infinitely many powers of two. Completeness and the unconditional theorem are proved instead by the onto two-way interleaving and simultaneous induction in `RESULT.md`. The code uses exact integers and Python sets; no external packages or data files are required. Independent audit has not been performed.
