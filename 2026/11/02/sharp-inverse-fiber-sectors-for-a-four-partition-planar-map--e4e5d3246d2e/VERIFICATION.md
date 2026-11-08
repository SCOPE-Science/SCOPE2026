---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS. Each source quadrant has an exact nonsingular linear map whose image is the positive cone between two adjacent axis images (1,1),(a,c),(1,-1),(-a,c). For |a|>|c|, eliminating y gives Y=x+(c/|a|)|X-|x|| with all piece slopes between 1-|c|/|a| and 1+|c|/|a|, proving a unique inverse. For |c|>|a|, the ordered image rays partition target angle into cone covering counts 0,2,4,2,0 (for both signs c), with 4fold region c>0: Y>X and tX>bY, or c<0: X+Y<0 and tX+bY>0 (b=|a|,t=|c|). The outer support inequalities and critical ray counts follow by tracking quadrant cone interiors and deduplicating shared source-axis points; b=0 coalesced rays handled separately. Since no nonzero source maps to the apex and each cone is pointed, properness and signed degree statements follow. Wedge angle theta-pi/4 gives exact disk-area fraction <=1/8. Independent rational Cramers-rule enumeration checked parameter/target grids including signs and critical rays. Singular parameters |a|=|c| intentionally excluded; finite enumeration is not the proof.

## originality

PASS

PASS, carefully delimited. Tikjha 2026 defines this exact four-partition piecewise-linear map and studies noninvertibility/critical curves; general same-sign-Jacobian invertibility is already proved by Poggiolini and Spadini 2011. New assessment is not invertibility but opposite-sign exact global target fiber multiplicities and boundary counts, with sharp four-sheet aperture and area fraction. Relevant 2018 inversion theory is general and accessible introduction did not give a demonstrated implication of these sector formulas. Full original Tikjha paper and full 2018 comparison remain limited by inaccessible lawful complete texts; prior equivalence risk is explicit.

## value

PASS

PASS. For a concrete published planar noninvertible map, exact inverse-branch regions and critical-ray counts are natural data for reconstructing preimages, invariant sets and bifurcation geometry. The complete 0/2/4 sector partition with sharp quantified fourfold aperture is a meaningful classification, not the already-covered homeomorphism case or an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
