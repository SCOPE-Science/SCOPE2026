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

# Reproduction and limitations

Run `python3 check_thue_morse.py` from the directory containing the files. The checker uses only Python's standard library, constructs the balanced two-point autocorrelations with exact `fractions.Fraction` arithmetic through index 65536, and separately uses the two integral matrices to reconstruct the dyadically normalized adjacent pairs. It compares both constructions at every test index, checks parities, the zero classification and the exact dyadic window counts. The observed marker is `THUE_MORSE_DYADIC_ZERO_CERTIFICATE_OK 65535`.

The finite checker cannot prove the infinite claim. The universal argument is the induction on two parity-preserving integer matrices in `RESULT.md`; it requires the classical autocorrelation recurrence and the normalization \(\eta(0)=1\). The Fourier-multiplier nullspace claim follows from Plancherel. Historical literature overlap remains a bounded risk, especially the inaccessible 1990 article. Independent audit and validation are not performed.
