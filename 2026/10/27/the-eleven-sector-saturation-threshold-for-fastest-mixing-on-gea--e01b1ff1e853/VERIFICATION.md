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

Convex dihedral averaging preserves feasibility and suffices for the global value. For the invariant feasible triangle 0≤p≤1/n, 0≤q≤(1−p)/2, the positive first-frequency eigenvalue decreases strictly in q and its saturated boundary value decreases strictly in p under the stated n≥11 inequality. Equality in that lower bound therefore requires both saturated weights within the invariant family. At this corner the maximum among nonzero frequencies is the positive k=1 value, with the other competing modulus from the negative radial eigenvalue. Exact rational comparisons at 10 and 11 and the increasing cubic bound for n≥12 give the claimed switch. At 10 the isolated active negative mode is not in the kernel of the outer-edge Laplacian (equal rim coordinates in a radial eigenvector would force all three coordinates to give the constant eigenvector); thus moving q down strictly improves the objective locally. For the maximum-degree rule the two nonzero eigenvalues of the radial Laplacian before dividing by n have sum n+5 and product 4n+2. The small root tends to 4 and the large root is n+1+O(1/n), so neither radial modulus competes asymptotically with the positive k=1 transition eigenvalue. Taylor expansion of both dominant eigenvalues gives the stated coefficients and ratio.

## originality

PASS

The strongest exact published SLEM case inspected is the ordinary wheel, not the gear graph. The distinct indexed comparator with exactly the saturated gear weights optimizes a different spectral objective and has a different cutoff. The supported distinct claim is the explicit gear SLEM optimum with the 10/11 boundary and its spectral-gap comparison, not symmetrization, Fourier decomposition in general, or maximum-degree weighting.

## value

PASS

The weights give a usable exactly optimal chain on a natural relay-augmented wheel. The sharp integer onset explains a genuine change in the active spectral constraint: the negative radial mode obstructs full saturation at ten, while the positive first Fourier mode certifies it from eleven. The benchmark gap ratio is nontrivial and quantified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
