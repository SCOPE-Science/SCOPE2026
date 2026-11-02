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

For integer m,N>=1 on normalized-area complex harmonic Bergman space, the orthonormal Fourier monomials e_k are shifted by T_m=P_h M_{z^m} with explicit positive weights derived from the radial moment 1/(q+1). The all-positive weights are bounded away from zero for fixed m, giving invertible contraction, forward norm1. For a length-N forward shift path staying on one side of zero, squared weight products telescope; crossing paths have reciprocal square F_{a,b}(j) proportional to [(am+j+1)(bm+m-j+1)]/[(j+1)^2(m-j+1)^2]. Its log second derivative is strictly positive on j∈[0,m], so crossing-residue maxima occur only at actual endpoint paths. The exact maximum is max_{0<=t<=N}(mt+1)(m(N-t)+1), attained only for balanced integers; the inverse INPUT (terminal of forward path) modes are e_{m floor N/2}, e_{m ceil N/2}. Thus ||T_m^{-N}||² equals the balanced product with dimension one for even N and two for odd N. Compact perturbation of m bilateral shifts plus spectral-radius bounds yields unit-circle spectrum, linear inverse norm slope m/2. Independently computed exact rational Fourier weights and inverse products for 72 parameter pairs with correct norming indices. This bounded check supplements, but does not replace, strict log convexity proof.

## originality

PASS

Best-of-knowledge mathematical comparison of the same object, definitions, parameter quantifiers, and implication strength. Foundation and partial coverage are credited explicitly; neither failed searches nor inaccessible full literature alone are represented as novelty proof. Unit-circle spectrum and weight formulas are established context, but exact power amplification is a strictly stronger numerical/operator invariant not fixed by spectrum. Spectral localization and coefficient computations alone do not imply the stated norm/equality classification without nontrivial optimization.

## value

PASS

An explicit harmonic Bergman Toeplitz operator is spectrally unitary-looking (spectrum unit circle and norm-one forward powers) but has sharply quantified inverse-power nonnormal amplification. Exact all-horizon norm and complete norming subspace reveal a discrete balancing mechanism in this natural function-space operator; the invariant is not mechanically the spectrum or a weight list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
