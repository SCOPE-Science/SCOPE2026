---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the six frozen quintics, the affine differential has rank 3 on the torus: two of its 3×3 minors would force a³=b³=−c³ there, and a third then has nonzero factor −18c⁹. The common factor abc of the maximal minors does not alone give this exclusion. On a=0 the a-row vanishes and u_3=c⁵, u_5=−5b²c³ give independent derivatives in b,c away from the vertices; b=0 follows by swapping a,b and permuting and negating the target coordinates. On c=0, u_1=−a⁵,u_2=b⁵ suffice. At vertices only the radial derivative survives. Euler's identity then gives precisely the stated projective ranks. In each cusp chart the normalized coordinates all lie in C[[t−t_0,x²,x³]]. Two depend only on t and y=x³ with invertible 2×2 Jacobian there outside the indicated exceptions; a third is a unit in the recovered t,y times x². For instance on a=x,b=t,c=1, use u_4/u_3 and u_5/u_3 with determinant −50t(t³+1), and use u_1/u_3=x²(5−y)/(1−5y). On c=x,a=1,b=t one may use u_5/u_1 and u_6/u_1 with determinant 50t(t³+1), and u_3/u_1; b=0 follows by symmetry. The pullback of O_X(1) is ample, so the proper map contracts no curve and is finite. The line restrictions recover t rationally, and for each line its two identically vanishing coordinates impose two cubic equations off that line, leaving at most finitely many possible extra preimages. Thus a general closed point of each curve has only the indicated preimage. The injection from the reduced image local ring into the finite pushforward remains injective on completion, and the unique preimage identifies the completed pushforward with the source completion at that point. Hence the calculated image subring is the actual completed local ring, not merely a parametrized branch. It is the cusp with a smooth parameter, and its normalization is obtained by adjoining x. An independent exact SymPy replay confirmed the minors, vertex ranks and chart determinants; the supplied script was inspected without executing it.

## originality

PASS

The supported distinct claims are the exact rank strata for the six-dimensional base-point-free quintic system and the precise generic analytic germ on its three coordinate-line images. The strongest inspected prior exact-map result proves finite birational normalization and degree 25 but explicitly does not identify differential strata or singularities. The founding paper gives the system and invites investigation of its image; the strongest related Fermat-family literature either uses another system or does not determine the cusp subring. These are affirmative statement-level distinctions, not a claim of exhaustive novelty.

## value

PASS

The object is the specific companion image introduced in the source's explicit question. The exact rank stratification resolves where its normalization parametrization loses immersion everywhere, including the extreme vertex behavior. The actual image cusp model identifies how it loses normality in codimension one on three natural curves, which neither the degree nor mere nonnormality tells a later study of the surface. This is a motivated, reusable exact result without requiring a full singular-locus theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
