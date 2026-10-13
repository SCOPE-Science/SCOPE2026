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

Run `python3 verify_bell.py` with standard-library Python >=3.9. The program enumerates all partial matchings of complete graphs on 2 through 8 vertices, constructs the exact rational transition matrix of the Bell/one-site monitoring dynamics at probabilities 1/3, 2/5, and 3/4, and checks detailed balance at every positive transition, including size-preserving reconnections. It also independently counts every crossing-edge number for every nontrivial cut and checks the proposed generating coefficients, means, and variances against brute-force weighted matching enumeration.

Actual output from the code inside the final package: `VERIFY_OK: 21 exact weighted matching chains; 3342 state instances; 70788 transition pairs; generating distributions and first two moments for every bipartition; 9 thermodynamic variance checks`.

The nine large-size tests use the exact log-weight finite-n sums at n=4000 and cut fractions 0.25, 0.4 and 0.5 for each of p=0.1, 0.4 and 0.85. They check both density and variance limits to tolerances <=0.002. These experiments do not prove all-n statements or limits. The written detailed-balance, generating-function and Laplace arguments establish the general claim; no independent audit or external certification was performed.
