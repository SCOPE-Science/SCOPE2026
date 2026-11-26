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

Gaussian integration of exp[(α+u)ξ+(β+v)ξ̄] gives exp[(α+u)(β+v)], and coefficient extraction gives the block λ exp(D) with the stated derivatives. For N=λ(exp(D)−I), D lowers degree and N^m=λ^m A^m, A=β∂z+α∂w, since using a second derivative or any extra power kills total degree ≤m. The Laurent expansion terminates and after order-m+1 scaling converges uniformly in angle in norm to this leading coefficient, up to a unit scalar. To check the actual norm independently, complete the square with c=ᾱ+β and translate the two real coordinates to independent centered normals of variance 1/2. In these coordinates A=d∂x+e∂y, d=(β+α)/2 and e=i(α−β)/2. Monic product Hermites of bidegree (j,k) have squared norm j!k!/2^(j+k) before the common factor exp(|c|²). Only j+k=m contributes to A^m, with output m! d^j e^k. Duality therefore gives squared operator norm 2^m m!(|d|²+|e|²)^m=m!(|α|²+|β|²)^m after canceling the same factor on the constant output. This nonzero norm proves exact pole order. Complex Hermite orthogonality (equivalently the moments from exp(uv)) verifies the stated attaining vector. Directional differentiation is onto from homogeneous degree j to j−1 in adapted linear coordinates; descending correction for the second derivative gives the stated ranks and Jordan lengths. Uniform radial bounds and boundedness away from λ give the radius asymptotic. 'Maximal distance' here is the supremum, since the defining strict inequality generally does not attain it. VERIFICATION.md and the real-rational finite-degree verifier were inspected without rerunning the latter.

## originality

PASS

The Gaussian convolution identity, qualitative eigenstructure, and general resolvent pole mechanism are not distinct contributions. The supported addition is the exact leading coefficient in the inherited weighted Gaussian metric for arbitrary complex directions, with its associated sharp radius. The closest primary source gives the action on coefficients but not the metric calculation. This is a bounded literature judgment, not a priority claim.

## value

PASS

An exact perturbation scale near the Berezin eigenvalue is not determined by the qualitative fixed-point theory or the size of its Jordan blocks. It depends materially on the norm; using a coefficient norm in place of the inherited one could change the claimed scale. The sharp inherited coefficient, its attained form and the disk bounds provide a quantitative statement on these natural invariant sectors without making an invalid boundedness claim about the full Gaussian L² space.

The dated certificate retains the supplied scientific assessment, sources and limitations.
