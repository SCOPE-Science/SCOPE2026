---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For X=Bl_p(P^2) glued to a second copy along its (-1)-exceptional P^1, the local transverse equation is uv=0 and each normal bundle N_{E/F1}=O_{P1}(-1), so the standard double-locus formula gives sheaf Ext^1=O_E(-2) !=0 with zero H^0. Verified the sequence 0->T_X->T_{F1}(-log E)^(direct sum 2)->T_E->0; the P2-stabilizer of p acts as all PGL2 on E, giving surjection on global tangent sections. R^1 ruling pushforward of T_rel=0 and pi_*T_rel=O(-1)⊕O⊕O(1) imply H^1(F1,T_F1)=H^1(F1,T_F1(-log E))=0, hence H^1(X,T_X)=0. The local-to-global Ext exact sequence then forces global Ext^1(Ω_X,O_X)=0. Ample anti-canonical bundles restrict compatibly to O_E(1) and descend from finite normalization, so X is projective. No claims on affine cones or higher-order deformations.

## originality

PASS

Nisse arXiv:2512.13203v1 Section 4.2 asserts projective nonvanishing of untwisted global Ext from positive-dimensional support via a twisted Ext calculation and cone comparison, while explicitly observing the missing untwisting inference. The audited projective example gives a concrete opposing computation. Tziolas provides the normal-bundle product but does not supply this particular first-order globally rigid projective pushout. Best-of-knowledge counterexample priority.

## value

PASS

The counterexample separates sheaf-level local smoothing support from global first-order deformation rigidity in a concrete projective SNC surface; it corrects a specifically located implication in contemporary primary literature, a substantive warning for global deformation arguments rather than a terminology check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
