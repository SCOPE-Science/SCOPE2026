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

# Finite proof replay

Execute `python3 VERIFY.py` in the directory containing the included source. No third-party libraries or external files are required. The program constructs the entire set of 2048 canonical binary order-five de Bruijn cycles by two independent exact exhaustive schemes: depth-first traversal of every unused directed edge, and all 65536 local incoming/outgoing edge pairings. It asserts equality of those two sets, checks each five-bit factor appears exactly once, and computes aperiodic peak sidelobes over every possible cut and positive shift.

The second metric implementation computes Hamming mismatches rather than signed autocorrelations. Its 11-bin histogram must equal that from signed products. Additional assertions verify the exact frequency table, the number of optimal cuts for 32 minima, the cyclic/aperiodic normalization identity, and the reversal/complement symmetry-orbit counts. The program prints the exact mean and variance and explicit extremal representatives. A successful run begins with `PHASE_APERIODIC_PSL_DB5_PASS`.

The check is exhaustive for binary order five only. No higher-order claim is made. No independent audit is claimed.
