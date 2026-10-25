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

# Reproducibility and verification

Run `python3 verify.py` from the extracted package folder. Python 3.10+ standard library suffices; no network, dataset, or external inputs are required.

The program constructs the \(2n\) points from the explicit latitude-ring coordinates, enumerates every vertex triple to identify supporting facets, compares the minimum supporting-plane distance to \(\min\{h,\beta_n(h)\}\), counts all farthest normal directions, checks the pairwise minimum chord length, and tests sampled height inequalities. The executed run reported **2412 passed numerical checks**, including \(n=3,4,5,6,9,13\), four characteristic heights, and sampled heights throughout \((0,1)\).

These computations do not constitute an exhaustive proof for unbounded \(n\) or continuum-valued \(h\). The supplied analytic proof uses the complete exposed-facet enumeration for antiprisms and exact monotonicity to establish all quantified claims. No independent audit or formal proof certification was performed. The only full-text access limitation materially relevant to novelty is the unavailable specialist eight-cap literature.
