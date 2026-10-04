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

The claim was verified directly against the quantifiers and norm assumptions of Conjectures 2.21--2.28 in arXiv:2201.00125v1.

For each statement, the source gives \(\|f_j\|\,\|\tau_j\|\le1\). Choosing \(b=2\), \(\varepsilon=1\), and \(I_j=\{j\}\) yields
\[
\left\|\sum_{i\in I_j}f_i(x)\tau_i\right\|\le\|x\|=(b-\varepsilon)\|x\|.
\]
No assumption on the summed operator, exact equality, or spectrum is needed.

The source does not require \(M\) to be universal, fixed, or bounded independently of \(n\). Therefore \(M=n\) is admissible for the literal statements. Weaver's original \(KS_r\) statement was separately checked and fixes \(r\) before the input, confirming that the missing block-count restriction is mathematically substantive.

Limit: this verification does not assess a repaired formulation with fixed or uniformly bounded \(M\).
