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

The analytic proof has two independent checks.

First, with the normalized Choi state \(\rho_{\mathcal U}=|\Phi_U\rangle\langle\Phi_U|\), every unitary channel has Choi spectrum \(\{1,0,\ldots,0\}\), yet
\[
\langle\Phi_d|\rho_{\mathcal U}|\Phi_d\rangle=\frac{|\operatorname{Tr}U|^2}{d^2}.
\]
Substitution into the standard average-fidelity identity gives the claimed unitary formula.

Second, the source's eigenvalue expression was evaluated under both common conventions. A normalized unitary Choi state has \(\sum_i\lambda_i^2=1\), giving the source expression \(1/d\). An unnormalized unitary Choi matrix has one nonzero eigenvalue \(d\), giving the source expression \(1\) for every unitary. Neither equals the actual target-relative fidelity in general.

`artifacts/verify.py` checks these statements for dimensions \(2\) through \(12\), including a traceless diagonal unitary in each dimension, and prints `VERIFY_OK`. These finite computations are consistency checks only; the proof for all \(d\ge2\) is the algebra above.
