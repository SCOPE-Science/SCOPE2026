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

# Reproducibility checks and limits

Running `python3 verify.py` (Python standard library only) reconstructs the binary four-neighbor transition matrices directly from their vertex adjacencies. Binary Gaussian elimination checks the rank of each iterate for 39 tested rectangular tori with a dyadic first circumference and at most 200 sites, through two steps after the predicted final nilpotent depth. It also iterates every one of the 69,632 labelled configurations for the \(4\times3\) and \(4\times4\) tori until recurrence, thereby independently measuring the first-periodic-entry time; 2,500 further initial configurations on five other tori were tested for maximal entry time.

Actual recorded stdout is in `verify_output.txt`, including `TORUS_4NEIGHBOR_GF2_VERIFY_OK`. The computed shell populations include \((256,768,3072)\) for \(4\times3\) and \((1,255,65280)\) for \(4\times4\), indexed by entry times starting at zero. All ranks and microscopic results agreed with the formulas. Only the algebraic proof, not these finite computations, establishes the result for every admissible dimension.

Historical novelty has not been independently certified; one relevant 2004 full text remained inaccessible. No checks for primitive periods within the invertible component were performed or claimed.
