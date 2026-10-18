---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: With the exact displayed ideal R=C[a,b,c,d,e,f]/(ab,bc,ca,de,ef,fd), disjoint triples factor R=A tensor_C A_prime, each A=C[a,b,c]/(ab,bc,ca). Height-two ideal has Hilbert--Burch resolution 0->S3(-3)^2->S3(-2)^3->S3->A->0, with explicit syzygies. Tensor over C gives minimal S-resolution Betti beta_(0,0)=1, beta_(1,2)=6, beta_(2,3)=4, beta_(2,4)=9, beta_(3,5)=12, beta_(4,6)=4. Projective dimension 4 and dim R=2 give depth2 (Auslander--Buchsbaum), hence CM. Last rank4 in single shift gives level type4, not Gorenstein. H=(1+2t)^2/(1-t)^2 yields multiplicity9. Independently enumerated all 64 induced subcomplexes of K3,3, computed Hochster reduced-H0 and H1, reproducing every graded Betti count and Hilbert numerator; no reliance on stored VERIFY_OK. Product singularities are exactly six affine coordinate axes; Proj is nine coordinate lines K3,3 with six triple incidence points and arithmetic genus4. This verifies the algebraic conclusions conditional on Wan identifying the deformation germ by this precise homogeneous ideal; primary full-text access was restricted.

## originality

PASS

PASS, qualified: Wan states the fixed-threefold semiuniversal germ as product of two triple-axis curves, nine two-plane branches, not (in abstract and available material) the full graded minimal resolution, CM type4/level, multiplicity, stratification and projective genus4. The commutative algebra is standard after the ideal, so novelty is only the assembled exact profile for this newly constructed motivated deformation singularity, not Hilbert--Burch/Hochster tools. Published Resultary search finds only the assigned exact record for this profile; complete Wan paper could not be reread because both OA/arXiv full-text routes failed and authorized Oxford access said vpn_disconnected; genuine priority risk remains.

## value

PASS

PASS, narrowly qualified: In a specific semiuniversal deformation germ of an actual Igusa Calabi--Yau tangent bundle, Cohen--Macaulayness, non-Gorenstein type4, multiplicity9, and singular branch stratification diagnose moduli obstruction geometry that one could naturally need to compare deformations or coarse quotients. Although formulas are an elementary tensor-product calculation once Wan gives the ideal, the complete structural invariants of that newly presented natural germ are a motivated exact package, not an arbitrary monomial slice. No claim for automorphism quotient or a general theorem about deformation spaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
