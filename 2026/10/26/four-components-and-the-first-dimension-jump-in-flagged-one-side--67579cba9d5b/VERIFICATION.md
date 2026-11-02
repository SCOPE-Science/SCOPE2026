---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For strict upper triangular 4-by-4 matrices the three product equations reduce to I=(xp,zr,xh+yr) in k[x,y,z,p,h,r] times six free coordinates. The direct ideal identity I=(x,r)∩(p,h,r)∩(x,y,z)∩(z,p,xh+yr) is valid over every field: the first triple intersection is (xp,xh,rx,ry,rz), and reduction modulo I plus P4∩(x,y)=(p,z)(x,y)+(xh+yr) proves the reverse inclusion. All four ideals are prime, including the geometrically integral determinantal quadric, hence geometric reducedness and dimensions 10,9,9,9. The x=0 and x!=0 branches count q^4+3q^3−4q²+q active points, then q^6 free coordinates give q^10+3q^9−4q^8+q^7; n=2,3 are equidimensional. Independently reconstructed the Gröbner intersection over Q and enumerated active solutions over F2,F3,F5, recovering 26,129,905. Existing original scripts including F4 arithmetic and characteristic checks were inspected. The all-field assertion follows from the exact ideal identity, not finite fields.

## originality

PASS

The exact one-sided fixed-complete-flag nilradical fiber and its reduced four-prime n=4 decomposition are not consequences of the inspected two-sided mutual-annihilation classification or unrestricted varieties of complexes, despite shared matrix language. Chen–Wang (2016) is unusually plausible because it treats zero products in the same strict-triangular algebra, but its accessible abstract concerns nonlinear preservers rather than the scheme; its full text was not accessible, leaving explicit historical priority risk. Best-of-knowledge PASS, not a claim that the unavailable paper has been excluded.

## value

PASS

The first failure of equidimensionality in a canonical flagged zero-product scheme, exact geometric component structure with a quadric cone, radicality over all characteristics, and exact point-count polynomial are motivated natural invariants. The n=4 boundary is mathematically structural rather than an arbitrary finite count; no theorem for n>=5 is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
