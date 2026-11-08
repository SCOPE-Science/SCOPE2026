---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For A SPD with distinct extreme eigenvalues 0<a<b, Gaussian S (s×N), s>=2 and post-sketch selected nonzero vector in the plane of extreme eigenvectors, the restricted Gram G^T G has positive determinant almost surely. The symmetric sketched denominator matrix H=diag(a,b)C symmetrized has positive diagonals and det H=ab C11 C22−(a+b)^2 C12^2/4; a negative eigenvalue occurs iff |C12|/sqrt(C11 C22)>rho*=2sqrt(ab)/(a+b). Gaussian columns are independent rotationally invariant, giving R²~Beta(1/2,(s−1)/2), so Pr(exists negative quotient)=I_{((b−a)/(b+a))²}((s−1)/2,1/2), specifically .4 for s=3,b/a=9. Deterministic Kantorovich spectral bound shows cosine(Av,v)>=rho* for all v; the operator-norm perturbation inequality ensures ⟨Av,Wv⟩>0 for SPD W with ||W−I||<rho*. The extremizing vector v=(sqrt(b/(a+b)),sqrt(a/(a+b))) in the extremes and a Householder reflector U with Uv=Av/||Av|| produce W=I−epsilon U SPD for epsilon<1, denominator zero at rho* and negative above it. This establishes sharpness and quantifier specificity. For N>2 the exact beta law is only for the extreme plane, not all vectors.

## originality

PASS

PASS, qualified. Güttel/Liu/Nyman 2026 develop sketched harmonic Arnoldi and derive a deterministic sufficient positivity condition for sketched Ritz values via a numerical-range/inverse-eigenvalue estimate in §5.3, but do not report the Gaussian extreme-plane adaptive probability or sharp rho* all-SPD perturbation frontier. Prior fixed-vector Gaussian sign tail is credited and has different order of quantifiers. Classical beta angular law and Kantorovich cosine bound are used without novelty claim. The theorem may be implicit in broader random Gram matrix or embedding literature.

## value

PASS

A post-sketch adversarial/algorithm-adaptive direction is a genuinely different safety event from testing a prechosen vector. Its exact Gaussian beta tail and sharp all-vector embedding distortion identify a natural failure threshold relevant to sketched harmonic Rayleigh quantities. The result is a bounded illustrative stability criterion, not a promised iterative Krylov guarantee; it is mathematically nontrivial in its quantifier change and exactness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
