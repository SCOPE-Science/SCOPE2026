---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For every m≥1, the norm of the circumradius-one regular 4m-gon satisfies E(z)≤N_m(z)≤E(z)/c_m with c_m=cos(π/(4m)); equality in the first bound holds exactly on vertex rays and in the second exactly on facet-normal rays. For x,y not both zero, multiply the two output inequalities, use the denominator lower comparison and the exact Euclidean identity E(x+y)^2 E(x−y)^2=(E(x)^2+E(y)^2)^2−4(x·y)^2. The upper bound is sec²(π/(4m)), strictly >1 so x=0 or y=0 cannot maximize. If the bound is sharp, x,y are nonzero orthogonal vertex vectors and both x±y lie on facet normals. After a dihedral transformation x=a(1,0), y=b(0,1), so the first quadrant angle |atan(b/a)| must equal (2j+1)π/(4m), 0≤j<m. Conversely these ratios make both x±y facet-normal vectors and saturate every bound. Thus the iff classification and scalar constant hold for all m, including m=1 square, m=2 octagon and sign/exchange cases. Independently reconstructed an exact six-entry Git tree; 4,960 candidate pairs for m=1..15, each within 9e-16 of the predicted optimum, and 4,500 seeded random inputs all below the analytic bound. The finite corroboration does not replace the unrestricted proof.

## originality

PASS

Best-of-knowledge PASS with genuine caveats: the scalar formula C_Z=sec²(π/(4m)) is already implied by Mizuguchi–Saito (2011/2012) Proposition 3.1 for real absolute normalized norms ψ≥ψ₂. The actual assessed stronger claim is the complete iff equality-set on every real regular 4m-gon. The full 2011 §3 and full 2012 result establish upper bounds and attaining coordinate-axis witnesses but do not classify all attaining pairs or state the angle-ratio ladder. Separate published findings on the same polygon family address Euler–Lagrange sum-of-squares constants; published Zbăganu optimizer work on a hexagon addresses a different norm. Resultary exact self-match was excluded as independent priority evidence. Full 2010 foundational paper was inaccessible after authorized access interruption, so an unexamined historical equality analysis or mechanically deducible observation is a residual risk; neither a failed web search nor unread document is claimed to certify originality.

## value

PASS

The Zbăganu constant is a standard geometric Banach-space invariant connected to nonsquareness and the parallelogram defect; regular 4m-gonal planes form a canonical infinite, symmetry-rich approximation family. Although the scalar extremum was known, its complete maximizing-pair locus is finer equality geometry: two perpendicular vertex rays with a discrete full finite ladder of allowable nonzero length ratios. It gives sharpness witnesses and necessary conditions for every m and distinguishes the direction and scale geometry not encoded in C_Z alone. No general fixed-point or stability consequence is asserted; the proof is elementary and the known inequality makes the novelty margin limited, but the all-family natural complete classification is a worthwhile self-contained exact result under the stated value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
