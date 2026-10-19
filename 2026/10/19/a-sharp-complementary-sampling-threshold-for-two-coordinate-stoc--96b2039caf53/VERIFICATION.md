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

Analytic verification consists of explicit \(2\times2\) matrices \(T_{11},T_{22},T_{12},T_{21}\), their two paired-Gram averages, and conditioning on the current state. All nonstandard calculations are exposed in the proof. Check \(J^{\mathsf T}=-J\), \(J^2=-I\), the balanced pair probabilities sum to one, and each stage marginal is uniformly distributed.

Reproduction: place `check_pair.py` beside this file and execute `python3 check_pair.py`. The script uses only the Python standard library `fractions` and `itertools`; it checks **4,864** exact rational parameter pairs for both the Gram identity and mean matrix and prints exact factors at selected boundaries. The script is a finite arithmetic cross-check, not a proof over all real parameter values. No external audit has been performed.

At \(r=1/2\), \(\eta=1/2\), compare exact factors: expected squared norm \(5/4\), squared mean norm \(13/16\). At \(r=1\), \(\eta=1/2\), the expected squared norm factor is \(1\), demonstrating the correct strict endpoint. At \(\eta=0\), all maps are identity. The proof covers arbitrary deterministic initialization and the zero initialization (trivially stationary).
