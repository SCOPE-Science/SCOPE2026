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

# Verification and reproducibility

The proof uses the exact Haar Parseval identity on each dyadic interval, a two-orientation subtree recursion, and an induction on binary Hamming weight. These are full mathematical arguments for every length \(N=2^m\), not assumptions extrapolated from a numerical test.

Execute `python3 checks/haar_phase_fibers.py` from the artifact root using Python 3's standard library. This enumerates every binary input for lengths 2, 4, 8, and 16 (including all 65,536 inputs at length 16), verifies exact fiber cardinalities and weight maxima, identifies singleton and maximum-fiber classes, and checks local Parseval by rational arithmetic for lengths up to 8. Results do not by themselves prove the infinite family.

Independent mathematical audit and independent replication have not been performed. Bibliographic priority remains provisional in the wider literature.
