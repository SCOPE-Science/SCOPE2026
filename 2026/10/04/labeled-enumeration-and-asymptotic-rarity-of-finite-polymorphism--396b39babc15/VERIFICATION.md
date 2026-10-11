---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Fresh species reconstruction confirms the EGF and asymptotic. The finite monounary classification says either there are no sources (permutations) or all sources have one common positive height h. A rooted attached tree with all leaves exactly h below its root satisfies T_0=z and T_h=z(exp(T_{h−1})−1); a cycle vertex may carry an arbitrary set of T_{h−1}-trees, giving D_h=z exp(T_{h−1}) and F_h=SET(CYC(D_h))=1/(1−D_h). Subtracting the shared permutation class makes the height strata disjoint. Independent coefficient recomputation reproduced 1,4,27,232,2285,25716,324583,4571904,71321769,1225291780. For h=1 the unique dominant positive pole solves \(\rho e^\rho=1\) with residue 1/(1+ρ). On |z|≤0.58 all h≥2 satisfy \(|z\exp(T_{h-1}(z))|\le 0.58\exp(0.58(e^{0.58}-1))<1\) uniformly, so their coefficient total is \(O(n\,0.58^{-n})=o(\rho^{-n})\).

## originality

PASS

The structural classification is prior; the labeled functional-digraph enumeration and dominant-pole asymptotic are not found in the inspected primary or database literature. Fresh searches for polymorphism-homogeneous monounary enumeration, source-height functional digraphs and the exact initial sequence found the classification paper and nearby all-leaves-same-level tree sequences, but no matching labeled unary-map EGF or asymptotic.

## value

PASS

This is a natural complete enumeration of a previously classified finite algebraic class. It gives an explicit EGF, concrete counts and an exponential-rarity law among all unary operations; the asymptotic is governed by a clean Lambert-W singularity. That is a meaningful quantitative refinement rather than recomputation of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
