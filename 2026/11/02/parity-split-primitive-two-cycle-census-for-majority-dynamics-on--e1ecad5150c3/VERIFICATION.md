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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 and only its standard library. Its recorded output is included as `verification_output.txt`.

The verifier uses two mathematically distinct routes: direct synchronous updates of every labelled wheel configuration for each \(3\le n\le16\), and separate cyclic-run binomial counts for the two-cycle formula. It also performs direct enumeration of permissible cyclic words for lengths two through twelve and symbolic polynomial multiplication of the three-state transfer matrix for lengths two through ten. It compares exact counts of fixed configurations, constant-hub primitive two-cycle orbits, and switching-hub primitive two-cycle orbits. The total finite simulation size is \(262{,}128\) configurations. Every test passed and the recorded terminal marker is `WHEEL_MAJORITY_ORBITS_VERIFY_OK`.

The infinite-family theorem rests on the mathematical proof in `RESULT.md`, particularly the necessity and sufficiency of the hub-switching conditions, the one/two-cycle decomposition under step-two adjacency, and the weighted cyclic-word transfer. Finite tests cannot prove the full quantified statement; they are reproducible discrepancy checks. The independent audit status remains unperformed.
