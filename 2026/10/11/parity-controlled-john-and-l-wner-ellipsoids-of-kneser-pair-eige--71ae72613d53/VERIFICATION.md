---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification and reproducibility

Run from the extracted package root:

```
python3 artifacts/verify.py
python3 artifacts/check_petersen_hull.py
```

The first command uses only the Python standard library and exact rational arithmetic. It enumerates all extreme supports of the fractional perfect-matching polytope of \(K_n\) for \(n=5,6,7,8\), validates every incidence constraint, checks all calculated polar-normal squared norms, identifies each maximizer, and checks the spectral projector identity and constant vertex norm. It produces:

```
VERIFY_OK Kneser-pair-eigenpolytope n=5..8 exact_half_integral_vertices=yes projector_idempotent=yes parity_contact_counts=yes John_Lowner_radii=yes
```

The second command is an independent numerical convex-hull reconstruction requiring `numpy` and `scipy`. It constructs an orthonormal basis for the kernel of the unsigned incidence matrix of \(K_5\) and deduplicates facets by exact support index sets, obtaining:

```
HULL_OK Petersen eigenpolytope facets=22 support_spectrum={6:10,5:12} closest_facets=10 inradius_squared=1/18
```

Exact enumerations give, respectively for \(n=5,6,7,8\): \(22,25,717,1057\) polar vertices, \(10,15,105,105\) tangential facets, squared inradii \(1/18,1/60,1/78,1/168\), and squared circumradii \(1/2,3/5,2/3,5/7\). These computations check only their stated finite range. The theorem for every \(n\ge5\) follows from the explicit spectral projection, affine polar bijection, complete support-component classification, exact norm identity, and the irreducible symmetry argument in `RESULT.md`. No formal-proof-system or independent audit is claimed.
