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

# Reproducible verification

Run \(`python3 verify.py`\) using Python 3's standard library. The verifier reconstructs each polynomial \(P_n\) by differentiated Horner products, independently checks residue evaluations using prefix and suffix products, and tests each claimed prime-power shift for 44 consecutive integers. The supplied elementary Newton-difference lemma extends those finite shifts to **all** integers because each shift difference has degree at most 43.

It enumerates every residue in each of the fourteen certified local periods, computes the exact CRT product and rational density, and checks the explicit positive order both modulo \(45!\) and using an exact large-integer differentiated product. Separately, for the index 35, it checks 34 shift values and all 49 residues modulo \(7^5\), proving a root-free global congruence.

Observed result on the packaged file: \(`VERIFY_OK`\), with 616 shift-certificate points, 1,817 local residue points, all 14 root counts, the positive CRT witness and the index-35 obstruction.

The external classification of small indices and the 2025 prior-art comparison require normal reading of cited papers and are not executable consequences of this verifier. The research review is not an independent audit.
