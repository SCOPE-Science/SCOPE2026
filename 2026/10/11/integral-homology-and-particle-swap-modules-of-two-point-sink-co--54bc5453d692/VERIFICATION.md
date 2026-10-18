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

PASS. Read actual RESULT.md 8e3d8aae5aee92344e839eec9b3a2906b71be3d4 and verifier c3458ae331d40c6f79599172813a2d85effd49f5. Ramos sink model allows all graph-vertex collisions but removes E diagonal square interiors. Relative LES on D subset GxG yields 0→H2(D)→C⊗C→Z^E→H1(D)→C^2→0 with C the integral zero-row/zero-column cycle lattice of K_mn rank b=(m-1)(n-1). Phi is coordinatewise product of cycles. For m,n>=3, rectangles sharing exactly one chosen edge map to each edge standard unit so im(Phi)=Z^E, saturated. For m=2,n>=3 products of (z,-z) span exactly primitive equal-row units, rank n; for m=n=2 their one cycle square gives primitive rank one image. Thus rho=E, max(m,n),1 respectively, H1 free 2b+E-rho, H2 free b²-rho. Degree 2 particle swap is negative factor exchange, deleted squares -id; rational exact splitting implies H2+=wedge²U, H2-=ker(Sym²U→P_m⊠P_n) with U=W_m⊠W_n, H1+=U, H1-=U⊕coker Phi. Cauchy identities and pointwise multiplication Sym²W_t→P_t (onto for t>=3) yield displayed modules, including thin t=2 exceptions. Independently checked numerical boundary values K2,2:(1,5,0), K2,3:(1,7,1), K3,3:(1,8,7), K3,4:(1,12,24). Inspected complete script reconstructs matrices for 7 finite size pairs, signs and group characters (not independently executed); finite cases cannot prove infinite presentation.

## originality

PASS

PASS best knowledge. Ramos–Yun 2026 was inspected via lawful complete source text (pages 14–24): it explicitly defines Conf2 as collision-free ordered points and computes stability of ordinary K_n,n modules under only the diagonal S_n action, not all-vertex sink collisions nor the full S_m×S_n×swap representation for unequal sides. Ramos's earlier sink theorem is a modeling result without this cycle-product saturation and all-size module decomposition. Resultary earlier cycle-sink special K2,2 and other complete-graph sink results do not dominate the proposed all-bipartite m,n formula.

## value

PASS

PASS. This fully determines an all-size integral topological invariant and rational automorphism-plus-particle symmetry for a natural biclique family, identifying the sharp structural transition at min(m,n)=2 and a nontrivial m=n=2 boundary. The character decomposition is useful beyond Betti numbers; deriving saturated image and Cauchy kernel is not a mere formal renaming of collision-free stable tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
