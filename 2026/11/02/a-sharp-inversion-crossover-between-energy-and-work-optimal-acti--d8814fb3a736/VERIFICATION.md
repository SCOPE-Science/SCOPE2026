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

# Reproducibility and scope

The stand-alone file `check_design.py` contains direct symbolic differentiation checks in `sympy` and finite high-precision optimizer/derivative comparisons using `mpmath`. Execute `python check_design.py` from a directory containing the file with Python 3, `sympy`, and `mpmath` installed. The program passed 3,000 assertions, printing the crossover \(b_c=2.3993572805154676678\ldots\), the auxiliary root \(z_0=1.5434046384182084479\ldots\), and the capacity-retention fraction \(0.5802019684911432368\ldots\). It requires no dataset, private credential, network connection, or external dependencies besides those named Python packages.

The proof is in `RESULT.md`. The symbolic calculations check algebraic identities; finite numerical grids do not verify claims for all positive affinities or all gaps. Those claims are established analytically by sign and monotonicity arguments. No independent mathematical audit or publication-priority audit has been carried out.
