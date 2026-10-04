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

The final claim was checked directly from the published definition of Meyerovitch dynamical dimension. The lower inequality follows from inclusion of invariant-measure simplices. For the upper inequality, the proof was reconstructed with arbitrary left-coset representatives and does not require the subgroup to be normal.

The critical identities checked are:

1. If \(R\) represents the left cosets of \(H\), then for every \(H\)-invariant probability measure \(\mu\), the average \(m^{-1}\sum_{r\in R}(T_r)_*\mu\) is \(\Gamma\)-invariant.
2. If \(\mathcal W_r=T_{r^{-1}}\mathcal W\), then \(\operatorname{ord}(\mathcal W_r,x)=\operatorname{ord}(\mathcal W,T_r x)\).
3. Repeated application of Meyerovitch's Lemma 2.4 yields a joint refinement with pointwise order bounded by the sum of the pointwise orders.
4. Combining these facts gives the factor \(m\) with no extra constant.

Boundary cases were checked explicitly: simultaneous emptiness of invariant-measure simplices gives dimension \(-\infty\) on both sides; \(m=1\) gives equality; and if the full-action dimension is \(+\infty\), the upper inequality is automatic. The sharpness example uses a cyclic \(m\)-layer system, the published constant-orbit-size formula, and the published identification of dynamical dimension with covering dimension for trivial actions.

No finite computation or numerical experiment is used as a substitute for an infinite proof. Literature verification inspected the full primary source and targeted equivalent subgroup/iterate formulations. Two later relevant preprints were inspected only at the abstract level, which is retained as an originality risk rather than treated as negative evidence.
