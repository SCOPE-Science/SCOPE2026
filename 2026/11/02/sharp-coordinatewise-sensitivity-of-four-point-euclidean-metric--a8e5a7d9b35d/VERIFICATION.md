---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Euclidean projection onto the finite polyhedral metric cone is piecewise affine; on a smooth active cell the Jacobian is the orthogonal projector H_B=I-B^T(BB^T)^dagger B, hence global ||.||infty Lipschitz bounded by max row sums over all 2^12 triangle-row subsets. Independently enumerated all 4096 row subsets with rational arithmetic, 466 distinct row spaces, rank maxima exactly (1,4/3,3/2,8/5,3/2,10/7,0). A separate 3-label calculation attains 4/3. For four labels, selected active constraints 3,8,11 and metric m=(2,2,1,2,1,3)/11 have nine strict complementary constraints; positive inputs z=m-0.01B^T1, z+0.0001v and v=(1,-1,1,-1,1,1) have exact primal/dual normal certificates; H_B v=(8,-3,4,-3,4,1)/5. Adding new labels at pairwise length1 keeps all new cross-triangle inequalities strictly feasible and leaves original multipliers, extending sharp lower bound n>=5. l-infinity objective nearness differs from l-infinity sensitivity of l2 minimizer. No equality of Ln for n>=5 claimed.

## originality

PASS

Dhillon–Sra–Tropp and Brickell et al define/solve metric nearness using l_p *objective* norms. The submitted claim instead measures l-infinity input-output sensitivity of the unique Euclidean minimizer. The later generalized-Jacobian algorithm paper supplies projection calculus but no explicit 4-point row-space census and sharp bound. Resultary nearby planar cone/disk Lipschitz results are geometrically different. Equivalent small-metric perturbation literature remains possible.

## value

PASS

Exact cross-norm stability of Euclidean metric repair is a useful small-scale natural invariant for four-point finite metric geometry, with a concrete worst-case face. It separates Euclidean nonexpansivity from coordinatewise amplification, not an arbitrary toy computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
