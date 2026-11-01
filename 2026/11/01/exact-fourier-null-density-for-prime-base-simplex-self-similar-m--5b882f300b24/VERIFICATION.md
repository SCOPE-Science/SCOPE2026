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

# Reproduction and scope

Run `python3 verify.py` with a standard Python interpreter. The checker uses only integer arithmetic and the standard library. It constructs integer polynomials \(1+\sum_i z^{m_i\bmod p^j}\) and divides by \(\Phi_{p^j}(z)=\sum_{r=0}^{p-1}z^{r p^{j-1}}\) using exact monic long division; no floating-point equality is used. It independently compares mask divisibility and the leading-digit criterion. The indicated finite cases also check residue-class count formulas. Only finite cases are machine checked; the complete arbitrary-prime, unbounded-frequency statement follows from the proof in RESULT.md.

The review was performed within one scientific review process; independent mathematical validation is not asserted. No unperformed external certification is implied.
