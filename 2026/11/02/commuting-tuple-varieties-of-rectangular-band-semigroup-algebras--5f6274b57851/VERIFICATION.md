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

# Reproducibility

Run `python checker.py` with Python 3 and no third-party dependencies. The script multiplies coefficient vectors directly using the basis rule \(e_{ij}e_{h\ell}=e_{i\ell}\). It exhaustively enumerates 11 parameter sets, including \(\mathbb F_4\), checks commuting pair/triple totals, and verifies centralizer dimensions and the three-family decomposition for all directly enumerated commuting pairs. The recorded output is stored in `verification_output.txt`.

The mathematical proof independently establishes the formula for all integer side sizes \(a,b\ge2\), all tuple lengths \(m\ge0\) and all finite fields, and establishes the component decomposition over every algebraically closed field for \(m\ge2\). Finite computations do not test arbitrary parameters or establish geometric irreducibility. The reduced-variety qualifier is essential; no scheme-theoretic radicality or formal external validation is asserted.
