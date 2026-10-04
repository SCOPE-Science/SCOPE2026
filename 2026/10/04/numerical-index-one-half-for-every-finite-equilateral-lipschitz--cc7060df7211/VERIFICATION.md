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
# Verification

The proof was checked directly against the definitions of the real numerical radius and numerical index.

1. **Norm model.** For every zero-sum vector \(\mu\), direct transport from positive to negative coordinates has cost \(\tfrac12\sum_k|\mu_k|\), and an indicator Lipschitz function gives the matching lower bound.
2. **Unit-ball generators.** A unit vector has positive mass exactly \(1\) and negative mass exactly \(-1\), so a transport matrix decomposes it as a convex combination of molecules \(u_{ij}=e_i-e_j\).
3. **Universal lower bound.** A norm-one operator attains its norm on at least one molecule because the molecular convex hull is finite. For its image, the four sign patterns of the selected two coordinates produce an admissible norming indicator with absolute value at least \(1/2\).
4. **Sharp operator.** The stated cyclic operator on three coordinates sends a molecule to a vector of norm \(1\), \(1/2\), or \(0\) according to how many endpoints lie in the distinguished triple, so its operator norm is exactly \(1\).
5. **Numerical-radius bound.** A dual functional norming a molecule can be normalized to take values \(1\) and \(0\) at its endpoints, forcing all coordinates into \([0,1]\). Direct evaluation of the cyclic operator is then at most \(1/2\). For a general norming pair, convex decomposition shows every positive-weight molecule is normed by the same functional, so the bound persists.
6. **Boundary.** With two metric points the free space is one-dimensional and has numerical index \(1\); the theorem therefore begins at exactly three points.

No finite enumeration, numerical optimization, or external certificate is needed for correctness. Independent audit has not been performed.
