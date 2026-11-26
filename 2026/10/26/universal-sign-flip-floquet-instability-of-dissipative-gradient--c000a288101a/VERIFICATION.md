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

Independently assembled the two real steps in primary/auxiliary block order: their diagonal primary skew terms have opposite signs, so the negative step is the transpose of the positive one. An orthogonal singular-vector basis for A splits the real product into complex 2-by-2 Hermitian Gram blocks and their conjugates. For c=1-rho and t=eta*sigma, the step has diagonal c-it,c and real off-diagonal rho. The squared determinant modulus is (1-2rho)^2+c^2 t^2>0 and the squared Frobenius norm is 2(c^2+rho^2)+t^2. The period characteristic polynomial at 1 equals -rho(2-rho)t^2, so one root lies on each side of 1; both are positive. A synchronized mode (v,v) has period Rayleigh quotient 1+t^2/2 by direct application of the one-step block, so its expanding projection is nonzero. The upper-right Gram entry rho(2c+it) is nonzero, so the expanding eigenvector has nonzero primary component and the decaying component cannot conceal its asymptotic growth. Orthogonal real modes cannot cancel. This gives the asserted multiplicities and geometric divergence for exactly the specified initialization class. At rho=eta=1/2, the static complex step roots are 1/2 ± sqrt(3)/4 plus an imaginary part of magnitude 1/4, giving the stated radius, while the period roots are (5 ± sqrt(21))/8. The OGDA reduction follows from hat z_(k+1)=z_(k+1)+eta K_k z_k at rho=1/2. The strict inequality 1<1+t^2/2 follows simply from t>0. The attached verifier was not executed and is not essential to these exact calculations.

## originality

PASS

The static DGDA update, generic transpose-product identity, and qualitative period-two optimism counterexample are not new. The supported distinct result is the complete contractive/expansive Floquet spectrum and divergence of every synchronized nonzero start for every invertible square coupling and the entire stated damping and positive stepsize range. The strongest retrieved prior results did not imply that statement.

## value

PASS

The exact spectrum separates full-state stability from what happens under the algorithm's standard initialization. The universal excitation result rules out reducing the positive step as a remedy for this concrete switch, and the separately stable static example makes the distinction operational for saddle algorithms. This is more than the familiar observation that arbitrary products of stable matrices can be unstable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
