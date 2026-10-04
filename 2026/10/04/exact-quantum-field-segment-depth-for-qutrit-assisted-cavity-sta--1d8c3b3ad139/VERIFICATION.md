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

# Verification

The mathematical proof is the excitation-support induction in `RESULT.md`. It uses the exact source-model identities that \(H_C\) preserves cavity photon number and \(H_Q\) conserves \(\mathcal N=N_{\mathrm{cav}}+|m\rangle\langle m|+2|e\rangle\langle e|\). Since the ancilla part contributes at most two excitations, one quantum-field segment can increase the largest occupied cavity Fock index by at most two, independent of pulse values or superposition phases.

`verify.py` gives a finite consistency replay of these support rules. It closes abstract basis supports under arbitrary classical-field ancilla changes and arbitrary quantum-field mixing within fixed total-excitation sectors. For \(0\le k\le20\) it checks that the largest cavity photon number permitted by the abstract closure model is exactly \(2k\), and for \(0\le N\le40\) it checks the minimal integer depth \(\lceil N/2\rceil\). Its successful output is `VERIFY_OK`.

The finite replay is not used as an infinite proof. The all-\(N\) statement follows from induction and the exact conservation laws. The verification does not model noise, simultaneous \(H_C+H_Q\) driving, higher-order multiphoton terms, or a higher-dimensional ancilla.
