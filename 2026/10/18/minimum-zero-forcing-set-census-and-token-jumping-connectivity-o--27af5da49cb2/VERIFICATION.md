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

# Reproducible checks

The self-contained Python 3 script `verify_cycle_powers.py` uses only the standard library. It constructs each adjacency matrix directly from cyclic distance and evaluates each initial set by iterated unique-white-neighbor recoloring. For every \(3\le n\le15\), \(1\le k<n\), it enumerates every vertex subset having the alleged optimum size and compares that entire family to the theorem's parametrization. It also checks the minimum-degree lower bound and connectivity of the resulting one-vertex-exchange graph. For five large graph-power parameters it checks the proposed families and connectivity without exhaustive subsets.

Recorded invocation: `python3 verify_cycle_powers.py`.

Expected output: `VERIFICATION_OK exhaustive_parameter_pairs=104 candidate_subsets=33331 enlarged_cases=25`.

The exhaustive enumeration only covers those 104 finite parameter pairs. The other 25 pairs are nonexhaustive. The unrestricted-parameter conclusion is proved mathematically in `RESULT.md`; no independent audit has been performed.
