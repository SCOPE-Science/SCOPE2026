---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For any even-order projective plane q>=2 and matching F of omitted incidences size k<=q+1, Schmidt-rank cut identity gives S(F)=rank_F2(N+UV^T). Column and row binary incidence codes have minimum nonzero weight q+1 and minimum words exactly projective lines or pencils: with q even, N^TN=all-ones, and the line-through-point parity arguments prove both the bound and equality classification without requiring Desarguesian coordinates. The exact block rank-update identity yields rank increase k for k<=q. At k=q+1, each endpoint dependence is at most one-dimensional; selected collinear/pencil supports cause one-bit deficit; if both deficient the matching constraint forces the pencil center off the selected line and the remaining scalar pivot equals 1. Separate constructions attain gains q and q+1. For PG(2,2^a), expansion of (a dot x)^{2^a-1} into 3^a independent monomial evaluation vectors yields baseline binary rank 3^a+1. Independently enumerated every Fano-plane incidence matching k<=3 (counts 1,21,168,644) and directly recomputed every toggled binary rank; all 834 matched the formula, including 252 threshold-deficient matchings. Read original VERIFY.py; finite checks are corroboration, not proof for all even planes.

## originality

PASS

The graph-state cut-rank law is from Hein-Eisert-Briegel, and the minimum-weight incidence-code characterization is old (Smith/Delsarte et al., geometric proof Bagchi-Sastry 1985). The present new result is the combined sharp q+1 matching edge-removal threshold and iff geometric endpoint classification, including simultaneous-line/pencil case. Cautrès et al 2024 section 4.2 on point-line incidence graph resources studies vertex-minor pairability rather than deleted-gate entanglement response. No inspected prior result explicitly gives the matched rank-perturbation gain law; residual coding-theoretic matrix-rank equivalence risk remains.

## value

PASS

Projective incidence graph states are natural highly symmetric stabilizer resources. The exact fault tolerance/entanglement enhancement law and sharp q+1 geometry predict which matched gate omissions lose one bit; this is a motivated complete finite-geometric threshold applying to arbitrary even-order planes, including non-Desarguesian cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
