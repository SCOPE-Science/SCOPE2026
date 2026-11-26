---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The flip-equivariant pair map turns an inner inverse into an equivariant section of the image: fixed outputs must have fixed preimages, and the two-point orbits admit paired sections. Conditional on j missed labels, the independent unordered input pairs avoid j of n² outputs, giving the exact weight (1−j/n²)^(n(n−1)/2). Its log is −j/2+j/(2n)−j²/(4n²)+O(1/n) uniformly on 0≤j≤n. The tilted occupancy partition function is (n!/nⁿ)[tⁿ](exp(t)−1+z)ⁿ. At the unique solution x∈(0,1), the associated independent box counts Y have mean 1 and variance x; their tilt conditioned on ΣY=n gives exactly the tilted vacancy law. The span-one local limit and Stirling give exp((x−1)n)/√x. To check the conditional CLT without a tail gap, put J=1{Y=0}; the conditional characteristic function at u is a ratio of Fourier integrals over v∈[−π,π] of [E exp(i(v(Y−1)+u(J−θ)/√n))]ⁿ, with u=0 in the denominator. Away from v=0 span one makes the integral exponentially small; near zero, positive definite covariance (three noncollinear support points) bounds the modulus by exp(−c n v²). With v scaled by √n, the Gaussian integral ratio gives variance θ(1−θ)−θ²/x, using Cov(Y,J)=−θ. This entails E_n/n→θ under the tilt. The bounded remaining weight converges in L¹ to exp(θ/2−θ²/4), giving both the prefactor and normalized reweighting convergence in total variation. At n=1 the exact formula has weight one, and the conditioned asymptotics concern n→∞. Finite checks were inspected, not used as proof.

## originality

PASS

Credit the exact algebraic criterion and labeled count to Baiduk–Kozerenko. The supported distinct claim is the sharp exponential proportion with its multiplicative constant and the conditional Gaussian vacancy law. These require an exponential occupancy tilt, an order-one correction, and a conditional covariance computation; the inspected sources do not cover these specific results.

## value

PASS

The exact prevalence of regular elements and the conditional defect are natural invariants of this monoid. The rate and prefactor quantify an exponential rarity not evident from a class count, and the change in the vacancy center plus its Gaussian variance describe a typical regular operation. The finite tilting correction is essential for the leading constant and the result is not merely recomputation of an exact table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
