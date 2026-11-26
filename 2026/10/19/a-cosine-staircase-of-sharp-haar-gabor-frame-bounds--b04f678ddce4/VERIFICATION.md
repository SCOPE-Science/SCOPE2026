---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With d=1/b and a=1/2, periodization of modulation coefficients gives the Walnut factor 1/b. Exactly two translates contribute to the diagonal; the b<=1 case has no off-diagonal overlaps. When a<d<2a, only shifts +/-d overlap, and the forward shift contributes -1 precisely when the residue t of the starting point lies below a-(d-a). Residues along a fiber advance by d-a mod a; edges are exactly the advances without a wrap. Each component begins at t0 in [0,d-a) and has ceil((a-t0)/(d-a)) vertices. The maximal length L=ceil(a/(d-a)) occurs on an open interval of positive length contained in the direct-integral base [0,d), also when a/(d-a) is an integer. The sine eigenvectors of the finite Dirichlet path give the extreme spectral values on these fibers, so the two bounds are truly optimal. The jumps follow from the one-sided ceiling change, the critical limit from L~2/(2-b), and the b=2 fiber is the bilateral discrete Laplacian divided by 2, with zero spectral infimum. This proof uses no rationality hypothesis.

## originality

PASS

Credit is limited to the exact sharp spectral endpoints for the fixed half-translation slice in the overlapping regime, and their jump and critical laws. The qualitative frame set, the painless tight branch and the Jacobi eigensolve in isolation are not credited as new.

## value

PASS

The half-translation equals the length of one Haar step and is a natural parameter rather than a fitted slice. The exact norm and conditioning on that lattice, discontinuous thresholds at noncritical densities, and the sharp constant determining instability near b=2 provide spectral information a frame-set criterion alone cannot give.

The dated certificate retains the supplied scientific assessment, sources and limitations.
