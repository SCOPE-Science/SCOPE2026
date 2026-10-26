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

# Reproducibility and evidentiary limits

Run `python3 verify.py` with standard Python 3; no external packages or datasets are required. This program inverts the truncated odd-divisor-sum parity series over \(\mathbb F_2\) directly, independently factors integers, and checks the \(3\pmod8\) reciprocal membership description for every \(n\le20000\). It compares the first twenty values against the published OEIS A192717 prefix and checks membership counts in compatible reduced residue classes for seven moduli. Successful output begins `VERIFY_OK`.

These finite calculations establish no asymptotic and do not independently verify the Bombieri–Vinogradov theorem. The proof of the distribution claim is contained in RESULT.md and requires the classical published \(\max_{y\le X}\) Bombieri–Vinogradov bound. Distinguish this theorem's proof from the finite software tests. No independent mathematical audit or validation has been performed.
