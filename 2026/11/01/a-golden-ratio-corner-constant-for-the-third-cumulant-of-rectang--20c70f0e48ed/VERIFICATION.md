---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The normalized Fock projection has kernel K(z,w)=π^-1exp(z conjugate(w)-(|z|²+|w|²)/2). Trace powers 1,2,3 reduce to an area integral, a Gaussian displacement integral with rectangular overlap (A-|x|)_+(B-|y|)_+, and a four-real-variable three-point integral with intersection overlap (A-Δ(x,s))_+(B-Δ(y,t))_+. Exponential Gaussian tails justify removing truncations with O(exp(-cR²)). The complex three-point phase gives the explicitly inspected 4×4 quadratic M with det M=1 and C=M^-1/2, where pairwise real covariances have variance 1/2 and cross correlations consist of three zeros and six ±i/2. Analytic continuation of the absolute bivariate Gaussian identity H(ρ)=[sqrt(1-ρ²)+ρarcsinρ]/π leads to E[Δ(X)Δ(Y)]=3/(4π)(1+sqrt(5)-log φ); direct substitution cancels area and perimeter in Tr(T-3T²+2T³). Independent exact SymPy inversion and correlation reconstruction confirmed the matrix, pattern and numeric positive 0.11472437826741096. Finite matrix algebra alone does not prove complex-Gaussian continuation or trace tails; these are addressed by the analytic argument.

## originality

PASS

Best-of-knowledge originality after primary comparisons: No source inspected has an implication to the constant without the nontrivial magnetic trilinear Gaussian integral. The exact mathematical assumptions/implications, not titles or absence of search matches alone, determine this decision.

## value

PASS

This is a natural exact corner contribution to the third counting cumulant of the infinite Ginibre determinantal process, where leading area and perimeter terms cancel completely. The third cumulant detects non-Gaussian shape effects unavailable from the leading second cumulant or a central limit theorem. The exact positive golden-ratio expression and aspect-ratio independence for all fixed positive rectangles provide a reusable invariant for the Fock projection, not an arbitrary toy constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
