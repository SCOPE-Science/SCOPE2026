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

# Reproducibility and limits

Run `python3 verify.py` with a standard Python 3 installation. The script has no third-party dependencies. It enumerates ordered equal-degree squarefree quadruples using product multiplicities and separately counts canonical coprime factors for a smaller overlapping parameter range; all comparisons must agree. It also checks the unrestricted degree-\(n\) count and truncated Euler-product inequality. A successful execution ends with `VERIFY_OK`.

Completed checks: field sizes \(q\in\{2,3,5\}\) with \(n\le6,4,3\), respectively. The independent canonical enumeration checks \(n\le4,3,2\) respectively. These computations demonstrate only those finite cases. The general asymptotic, Euler-product positivity, and the strict comparison follow from the explicit proof in `RESULT.md`. The numerical product truncation is not used to establish a global inequality.

Independent audit is not performed; the accompanying review is a self-review, not outside certification.
