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

# Verification of the full-unitary diagonal criterion

The following analytical calculations determine the claim and its scope.

1. On normalized Gaussian monomials, \(z_i\partial_{z_j}\) transfers one occupation from mode \(j\) to mode \(i\) with coefficient \(\sqrt{(\alpha_i+1)\alpha_j}\). The commutator with a diagonal therefore has entries exactly equal to this coefficient times the diagonal difference. Each coordinate-transfer operator is an injective weighted shift, making its norm the supremum of its coefficient moduli.

2. Bounded commutator norms for the finitely many Lie generators imply a uniform-in-degree Duhamel estimate for their exponentials; the homogeneous Fock decomposition permits the estimate without a common bounded representation generator.

3. A norm-continuous compact-group conjugation orbit can be smoothed by convolution against \(C^\infty\) approximate identities. Averaging the smoothed operator over the diagonal torus produces norm-approximating diagonal operators whose group-orbit derivatives remain bounded. Matrix entries of the infinitesimal coordinate skew-rotation give the required finite weighted edge slopes.

4. Complex-valued bounded uniformly continuous arrays on the disjoint union of degree graphs are uniform limits of graph-Lipschitz arrays via real and imaginary infimal convolutions. The epsilon-delta approximation bound is uniform over all degrees and needs no finite truncation.

5. In two coordinates the arcsine angle has derivative \([x(m-x)]^{-1/2}\); integration and the beta integral \(\int_0^1[s(1-s)]^{-1/2}ds=\pi\) supply the exact path metric comparison. An explicit same-degree phase oscillation is a Toeplitz diagonal but not full-rotation continuous; a parity-of-degree array commutes with all rotations while violating Toeplitz square-root continuity.

Run `python3 verify.py` from a directory containing the extracted standalone script. It checks finite-dimensional generator coefficients, positive angular-distance inequalities, and the two separation witnesses. Its numerical checks are finite and do not replace Steps 2–4 of the analytic proof. No external or independent validation has been performed.
