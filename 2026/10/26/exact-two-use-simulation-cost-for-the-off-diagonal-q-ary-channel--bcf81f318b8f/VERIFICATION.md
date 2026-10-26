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

The result is verified by the analytic proof in `RESULT.md`. The exact support size is \((q-1)^2\); for outputs at Hamming distance \(d\), the intersection of their input neighborhoods has size \((q-1)^{2-d}(q-2)^d\). The three-output construction has a valid index for every input, and the stabilizer-transitivity argument gives the exact target distribution. For \(q=2\), each input has a singleton target support, forcing all four outputs. These arguments cover all integers \(q\ge2\) without an asymptotic or numerical inference.

The literature comparison inspected the full text of arXiv:2610.15877 (simulation model, definitions, positive-dispersion assumption and main theorem), arXiv:2212.11666 (worst-case total-variation model and ternary off-diagonal example), and arXiv:2401.16707 (i.i.d.-source exact synthesis model). Exact-formulation searches were performed for q-ary two-use simulation cost, Hamming-distance-two support covers, and zero-error off-diagonal channel simulation. Search failure is not treated as proof of novelty. Independent audit and external validation remain unperformed.
