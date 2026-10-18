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

`python3 verify.py` uses the Python standard library to compare exact rational probability laws from the complete labeled-star process and the reduced two-count Markov chain for every pair of part sizes from 1 through 5 (25 cases). It then compares finite-size empirical vacancy densities at \(N=2000,5000,10000\) with the analytical formula for \(\delta=2/5\), using 250 fixed-seed replicates per size; it tests the integer perfect-cover witness. At packaging, the program was run successfully from the candidate file path, reporting `PASS 30 exact distribution and limiting-law checks`.

Finite enumerations and simulations cannot prove the infinite-volume theorem. The proof uses exact transition probabilities, bounded-step martingale concentration on interior compact sets, and a deterministic bound for the terminal boundary layer. Independent audit has not been performed.
