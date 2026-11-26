---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For z=u+vt and w=x+yt the constant commutator coefficient is a(vσ(y)−yσ(v)). When v≠0 it vanishes exactly for y=cv with c∈F, and the t-coefficient then vanishes exactly for x−cu∈F. For v=0 and u∉F the t-coefficient forces y=0, giving K=F+Fu. This proves both the commuting center F and C(z)=F+Fz for z∉F, with no division by 2. Noncentral commutation is equality of projective lines in the three-dimensional quotient by F, with q(q−1) vertices per line. The ordered-pair count includes loops and all central elements: q·q⁴+(q⁴−q)q². For a∈F×, choose b with bσ(b)=a; the representation u+vt↦(x↦ux+vbσ(x)) preserves multiplication and is injective because σ is not the identity (evaluate at 1 and at x∉F). For a∉F, a nonzero left factor with v=0 immediately forces a zero right factor if the product is zero; with v≠0, u=0 also forces x=y=0, and otherwise elimination of y gives (N(u)−aN(v))x=0 with nonzero coefficient. So there are no zero divisors and all nonzero left/right multiplication maps are bijective by finiteness. The associator on (t,t,t) is (a−σ(a))t. Finally z²−Tr(u)z=aN(v)−N(u) lies outside F for v≠0, and (F+Fz)∩K=F there; thus C(z) is not closed under multiplication. The clique in the stated graph is C(z) minus F, not the whole commutant.

## originality

PASS

The split graph is not a distinct contribution. The originality pass is for the exact proper quadratic Petit commutation law across parameters and its juxtaposition with split matrix commutation, including the systematic nonclosure of the proper v≠0 commutants. Inspected comparative results do not cover that combination or imply the proper calculation.

## value

PASS

A natural all-characteristic comparison shows that the same entire commuting graph and probability can occur for a split matrix algebra and a proper division algebra even though one has multiplication-closed commutants and the other has an explicit whole class of nonclosed commutants. The graph therefore loses a precise structural property; the uniform elementwise description also resolves every centralizer size, rather than merely fitting graph counts at small q.

The dated certificate retains the supplied scientific assessment, sources and limitations.
