---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For zero-sum input row x and centered zero-sum column w, direct counting without-replacement permutation moments over equal, two-equal and all-distinct triples gives E(x_pi·w)^3 = [d/((d-1)(d-2))](Σx³)(Σw³). A doubly stochastic P has zero-sum columns after subtracting J, so summing this identity over output columns gives one-step scalar κ(P); fresh independent permutations allow exact conditional iteration over all finite L. An r-regular zero-one adjacency kernel has dr entries 1/r, giving (d-r)(d-2r)/[r²(d-1)(d-2)] and sign/zero transitions including r=d. Full enumeration of d=4 two-by-two averaging kernel confirms 4th moment ratios 11/21 and 2/3, so fourth scalar closure genuinely fails. Independent rational checks also verified the κ polynomial for d=3..7. d≥3, independent shuffles, double-stochasticity and finite depth are essential; C3 is signed, not a distance.

## originality

PASS

Chiclana's full accessible primary article, same shuffled-doubly-stochastic model, proves exact quadratic/chi-square contraction and regular-degree second-moment factors, not the examined third-centered-moment identity or degree-dependent sign reversal. Those nonnegative quadratic factors do not imply a signed cubic invariant. More general symmetric-group tensor-invariant theory may encapsulate the elementary third-order expectation; best-of-knowledge originality remains conditional on that risk. Loizou–Richtárik randomized gossip uses mean-square convergence under other updates.

## value

PASS

Signed cubic centered dispersion measures skewness/asymmetry of a stochastic profile and is qualitatively invisible in existing quadratic mixing estimates. An exact scalar factor for arbitrary kernels, negative regular-degree factors above half density, and a concrete fourth-order nonclosure obstruction identify the precise special structure of degree three, making the result useful even without a mixing-time theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
