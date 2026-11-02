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

# Verification record

The included `verify.py` can be run using Python 3 with NumPy. `verification_output.txt` is the output of an actual run of that included script. It reported `PASS 11507 deterministic finite and asymptotic sanity assertions`.

The script checks the direct graph-Laplacian spectrum for every binary creation history from three through ten vertices, separately checks the terminal-creation-run formula and all suffix-event indicators, and performs exact rational enumeration for four positive integer Beta-urn parameter pairs through nine vertices. Exact posterior beta-binomial counts, rare-event probabilities, conditional gap tails and the complete-graph atom are tested. Large finite \(n\) checks compare exact formulas to the proposed limiting constants at multiple macroscopic thresholds.

The infinite Gamma posterior, Cox point process, negative-binomial law and conditional gap distribution are justified by the analytical proof in `RESULT.md`. Finite enumeration cannot establish their infinite validity. There is no independent audit in this package, and no stronger form of numerical certification is claimed.
