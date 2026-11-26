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

For a nonzero symmetric rank-one matrix, A=c uu^T over the ground field, and A^2=0 exactly when u is isotropic. Independent image vectors give independent opposite rank-one tensors, so commutation forces their pairing to be zero; dependent isotropic vectors already pair to zero. The allowed entries in a fixed b-plane number q^b, including zero; subspace inversion is therefore identical to the surjective-map count. Orthogonal line counting follows by splitting off a hyperbolic plane: the number of quadratic zeros in dimension d is (q-1)q^(d-2) plus q times the zero count in the residual space; isotropic flags give the stated products. In characteristic two the sum-zero hyperplane is symplectic for odd n, and in even n its radical is the all-ones line. The graph and inverse-image strata give the two terms q^b S_(m-1)(b) and S_(m-1)(b-1). For b<m the two odd-type ratios to S_(m-1)(b) average to (q^(2m-b)-1)/(q^(2(m-b))-1), agreeing with the characteristic-two ratio by Gaussian cancellation; the maximal b=m case is verified separately. Geometrically the full-span incidence is locally a nonempty open in a product of rank-one cones of total fiber dimension rt, and the concatenated column matrix recovers its isotropic plane on the constant-rank locus. Lower-rank points lie in its closure in any containing isotropic r-plane. In characteristic two with even n and r<m, choose the radical-deformation vector inside H intersect U-perp but outside U (the intersection has dimension 2m-r); this ensures the moving plane stays totally isotropic. Radical-containing planes are then limits of the irreducible radical-free stratum. At r=m the base is the Lagrangian Grassmannian of H/R. In odd characteristic the maximal even-dimensional orthogonal case has two base components by the determinant criterion for the orthogonal stabilizer; lower spans extend into both. These checks give the component dimensions and count on the reduced variety, with no claim about the defining scheme. Source checker inspected, not executed.

## originality

PASS

Credit the classical polar counts, standard maximal orthogonal component split, and the odd-field tuple enumeration already subsumed by the distinct indexed arbitrary-rank result. The supported distinct claim is the characteristic-two transition of the reduced standard-transpose, rank-at-most-one tuple variety together with its exact point-count comparison to the two formal odd orthogonal types. Neither the odd-field specialization nor the adjacent symplectic result covers that combined statement. This decision does not establish historical priority or count every ingredient as novel.

## value

PASS

The characteristic-two comparison is useful because equal geometric dimensions conceal a genuine merger of components, while the actual point counts pick out the mean of two formal orthogonal types. Identifying the radical geometry explains both features and supplies an explicit all-tuple-length boundary and counting formula. This value is in the joint cross-characteristic result, not in rederiving individual classical polar counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
