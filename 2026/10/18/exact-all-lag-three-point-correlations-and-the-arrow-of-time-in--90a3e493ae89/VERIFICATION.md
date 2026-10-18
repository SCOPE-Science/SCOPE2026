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

# Reproduction and checks

The package contains the standalone Python standard-library program `verify.py`. Run `python3 verify.py` in the same directory. The program implements independently the valuation-based prediction, the paperfolding odd-part signs, and uniform residue sampling modulo \(2^{13}\), entirely with integer and rational arithmetic. It checks 703 three-site triples \((0,a,b)\) for \(-19\le a<b\le19\), \(a,b\ne0\), and 64 two-site lags. The output is:

`VERIFY_OK: 767 exact residue comparisons with rigorous error, two exact cylinders`

For a triple of distinct times, at most three 2-adic sample residues coincide with a singular argument modulo \(2^{13}\), bounding the discrepancy between the finite-residue mean and the Haar correlation by \(3/2^{13}\). The two-site discrepancy is at most \(2/2^{13}\). Thus these are rigorous finite-certificate tolerance checks, not heuristic floating-point tests.

The proof of the infinite assertion is the parity decomposition and Haar rescaling in `RESULT.md`. Finite tests cannot substitute for the proof of all lags. Historical novelty has not been independently established.
