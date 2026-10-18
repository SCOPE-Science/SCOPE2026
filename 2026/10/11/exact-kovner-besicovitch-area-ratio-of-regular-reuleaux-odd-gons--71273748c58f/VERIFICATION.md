---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Every symmetric subset with center c is contained in C_c=K∩(2c-K). Convex Minkowski interpolation C_tc+(1-t)d supersets tC_c+(1-t)C_d; planar Brunn–Minkowski gives concavity of sqrt(area C_c). The odd dihedral rotation orbit averages to origin, giving optimal C_0. The reflected n centers interlace into 2n uniformly spaced circle centers. The limiting disk for any radial ray is the one with smallest dot product, so its quadratic yields s(delta)=-r cos delta+sqrt(1-r² sin² delta), delta in [-pi/k,pi/k]. Exact integration of k sectors gives F(k,r). Each generating vertex violates its reflected disk as 2r_n>1, giving strict proper inclusion. An independent mpmath evaluation confirms beta(3)=0.8403426028066864, beta(5)=0.9479862949042737; independent symbolic Taylor of F verifies the coefficients through n^-4. All-n proof is analytic, not ray-grid quadrature.

## originality

PASS

Best-of-knowledge not covered: relevant papers on area-minimal constant-width bodies, Minkowski chord asymmetry, Estermann outer centrally symmetric hull, and diameter-bisection symmetry optimize different functionals. The inaccessible Besicovitch 1951 primary constant-width asymmetry paper is a material priority risk, but its absence alone is not a negative originality proof and is explicitly retained.

## value

PASS

The Kovner–Besicovitch maximum centrally symmetric inner-area fraction is a classical natural asymmetry invariant. Computing its exact value simultaneously for every regular odd Reuleaux polygon, with a global symmetry-center theorem and sharp second-order and fourth-order convergence to symmetry, is a substantive natural family result beyond one benchmark. Potential use in comparisons of convex constant-width asymmetry measures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
