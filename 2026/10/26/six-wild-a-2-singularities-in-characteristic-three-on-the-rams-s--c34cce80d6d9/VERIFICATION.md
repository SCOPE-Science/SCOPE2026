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

In characteristic 3 the x and y derivatives are yq and xq. On the base line u=v=0 the other derivatives are x^3 and y^3, so no point there is singular. Off the base line and q=0, a singular point would require x=y=0 and a multiple projective zero of g. In a chart at a simple root r of q, write s=t-r and w=ax+y+b. The restriction is w^3, and the coefficient of s on w=0 is exactly the stated monic P_r; the other derivatives vanish at s=w=0, giving three singular points per root. The same argument works with the variables reversed and covers infinity. Since P_r' is nonzero at each root, replacing x by H=(F-w^3)/s gives an invertible formal coordinate change there. Thus the exact completed equation is sξ+w^3, and the hypersurface Fitting ideal is (s,ξ) in its coordinate ring, giving the length-three local algebra and length 18 total. Blowing up this model at the origin gives smooth charts (for example in the w chart the strict transform is s'ξ'+w=0) and two transverse exceptional lines; discrepancy is zero by ambient adjunction and multiplicity two. These are the A2 rational double points also in characteristic 3. Finite singular support excludes both intersecting hypersurface components and multiplicities; S2 and R1 give normality. Quartic adjunction and the hypersurface exact sequence give trivial canonical bundle and H^1(O)=0, preserved on the crepant resolution by rationality of the singularities. Independently expanding the two example charts gives the two cubics T^3-T+2 and T^3-T+1. The quartic has derivative (t-1)^3, value 2 at 1, and nonzero value at infinity. Both cubics are separable with no F3 root; Frobenius acts on their roots by translation by 1 and 2 respectively. This verifies the witness and the two orbits directly, without inferring geometric support from an F27 census. Separability is open by the discriminant on the simple root cover and its purely inseparable base change. No all-degenerations or smooth-characteristic line characterization is claimed.

## originality

PASS

Credit the equation, standard A2 local and resolution theory, and the known triple-line fiber pattern. The supported distinct contribution is to classify the actual singular points and their Fitting schemes on this coefficientwise characteristic-three specialization under the stated open conditions. A later record contains substantial geometric overlap but is not earlier coverage.

## value

PASS

The classical equation comes from a family whose source expressly excludes characteristic three. A concrete open-locus classification in that omitted characteristic gives both the resolved K3 configuration and the embedded distinction between six geometric points and length eighteen. This is useful for recognizing the bad-characteristic specialization and interpreting a Jacobian scheme, beyond a single quartic census or a general A2 derivative observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
