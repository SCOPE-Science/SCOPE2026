---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

I independently checked exact 2×2 matrices K=diag(1,0), U=[[0,1],[0,0]], W=H, Λ=K, C=C’=I. E(f)=|f1|²=||K*f||², R(U)=R(K)=span e1, U*f=(0,f1), and ||U*f||=||K*f||. However UW=span e1 and ΛU*P_UW=0 identically, contradicting any positive K-lower frame bound at e1. Theorem 2.3 at publisher pp114–115 imposes no injectivity of U. For closed-range K, (K†)*K*=P_R(K), not identity; applying it to U*f requires R(U*)⊆R(K). The published sufficient-bound algebra follows with the added range hypothesis if image fusion spaces are closed. The false theorem’s necessary half was not refuted.

## originality

PASS

The novel final claim is a concrete counterexample to a named implication and diagnosis of its exact missing adjoint-range geometry, not a restatement of the published theorem. Full publisher PDF pages 111–120, including complete Theorem 2.3 proof, was inspected. Other image-transport theorems require invertibility or commutation and do not supply this failure. Exact erratum/counterexample and range-alias searches returned no same counterexample; database negatives do not establish absolute priority.

## value

PASS

A formally stated iff transport criterion for controlled K-g-fusion frames fails even with equality in its numerical condition and with closed image subspace. The constructive failure isolates a meaningful hidden adjoint-range condition affecting usable operator-transfer criteria, not a cosmetic constant or textbook renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
