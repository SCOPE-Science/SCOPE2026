---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Beta-weighted monomial moments produce coefficients O(k^{-alpha-1}); the twice-differentiated angular series is absolutely uniform for alpha>2. At the four roots of unity, first and alternating Fourier vectors diagonalize the exact 4×4 circulant Hessian; only rotation is in its kernel. Root-of-unity filters give the positive integral eigenvalues lambda1=4(alpha+1)∫(1-t)^alpha[A+B]dt and lambda2=8(alpha+1)∫(1-t)^alpha Bdt. Their difference uses F=(alpha+1)∫(1-t)^alpha(A−B)dt. The rational ratio B/A=4t(1+t)^4/(1+t²)^3 is strictly increasing from zero to eight, hence A−B has one sign change; a monotone likelihood-ratio argument proves at most one zero of F. Exact partial fractions give F(2)=24log2−12−3pi/2<0 and F(3)=120log2+6pi−102>0, establishing existence. Fresh independent exact symbolic differentiation verified R’/R=(1−t)(t²+6t+1)/(t(1+t)(1+t²)); numerical integrals independently checked both endpoint expressions and root 2.727841735934682. The second-variation Taylor formula yields the claimed sharp local quotient coefficient. The alpha=2 integral is used only for a continuous endpoint sign, not a Hessian at alpha=2.

## originality

PASS

Best-of-knowledge originality is restricted to the unique four-pole, variable-power soft-Hessian mode crossover, exact root characterization and transverse isotropy; global Chui minimization, Fourier symmetry and fixed-weight Hessian diagonalization are prior. Corbett 2026 explicitly discusses a Hessian in its abstract, but the full text was inaccessible; this is a material priority risk, not fabricated contrary evidence.

## value

PASS

For a classical regular-polygon minimizer in weighted Bergman energy, the local curvature determines sensitivity to perturbations beyond the binary global-minimum statement. Four poles are the first equispaced configuration with two distinct nonrotational real Fourier symmetry classes. Their unique soft-mode switch and one isotropic exponent are a sharp natural spectral phase classification with exact stability coefficient and rigorously identified transition, not a mere normalization or known minimum restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
