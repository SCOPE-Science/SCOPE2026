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

# Reproducible verification and scope

Execute `python3 verify.py` from the directory containing this file. The verifier uses only the Python standard library, constructs all equivalence relations on six or fewer labeled vertices, and performs independent modal partition refinement for all selected colorings. It directly constructs Boolean modal subalgebras in 180 small cases and independently checks the finite generating-count coefficient and Bell factorial moments. Monte Carlo illustrations of Stam-distributed uniform partitions and independent colors are additional sanity checks, not analytical certificates.

Observed run:

```text
EXHAUSTIVE_OK valuation_frame_pairs 1065872 enumeration_cases 18 direct_term_closures 180
MONTE_CARLO n=400 q=2048 samples=600 p_obs=0.6267 p_theory=0.6450 pairs_obs=0.4467 pairs_theory=0.4384
MONTE_CARLO n=1000 q=8192 samples=600 p_obs=0.7250 p_theory=0.7259 pairs_obs=0.3217 pairs_theory=0.3204
MONTE_CARLO n=3000 q=16384 samples=600 p_obs=0.5400 p_theory=0.5677 pairs_obs=0.6100 pairs_theory=0.5662
VERIFY_OK
```

The general asymptotic result rests on Bell ratio concentration, the dependency-graph Poisson approximation and a separate palette collision bound. The verifier does not prove these unbounded-size statements or establish research priority. The stochastic discrepancies shown are expected finite-sample fluctuations and finite-parameter effects.
