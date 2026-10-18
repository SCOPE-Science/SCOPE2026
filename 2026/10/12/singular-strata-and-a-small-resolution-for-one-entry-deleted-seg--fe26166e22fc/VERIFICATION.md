---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Across all a,b>=2 the chart z_ij!=0 (i,j>1) has a free polynomial coordinate ring; row chart z_1j!=0 has independent A^{b-2} variables and the ring of 2-by-(a-1) rank-one matrices, via s_i=x_i/x_1 and w_i=x_i*y_1/(x_1*y_j), with the 2x2 minors generating the prime kernel; column charts transpose this. The rank-one cone D_{2,m} is smooth off its vertex (and everywhere for m=1), normal and has vertex multiplicity m, local class group Z for m>=2, and Q-Gorenstein iff m=2 by K=-2H_1-mH_2 versus H=H_1+H_2. This yields exactly the L_R (a>=3), L_C (b>=3) reduced singular strata, globally Q-Gorenstein iff a,b<=3, and a=b=2 smooth. Blowing up the Segre point omitted from the projection resolves the map; the only contracted curves are the two Segre rulings through that point. Their strict transform codimensions are a-1 and b-1, so the map is small precisely when a,b>=3 and then crepant in the Gorenstein a=b=3 case. Smallness is NOT asserted for a=2 or b=2; the smooth-locus-isomorphism condition would fail there. Source checker.py and checker.out were inspected; finite tests do not prove this infinite classification.

## originality

PASS

Best-of-knowledge PASS: existing rank-one determinantal and matrix-completion frameworks supply the ring/cone ingredients, but inspected relevant statements do not directly furnish the complete deleted-entry projective two-parameter singular strata, multiplicities, local class groups, global Gorenstein boundary, and explicit blowup smallness classification together. No direct Resultary hit; absence is not proof of novelty and specialization could be covered in other toric/matrix-completion sources.

## value

PASS

PASS: A fully classified infinite two-parameter family of concrete coordinate-projected Segre toric varieties, with normality/singular strata, transverse determinantal cones, Gorenstein threshold, local class groups and exact small-resolution behavior, is independently useful in birational geometry and matrix-completion degenerations. It is not an arbitrary parameter slice or merely a restatement of the determinantal cone local model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
