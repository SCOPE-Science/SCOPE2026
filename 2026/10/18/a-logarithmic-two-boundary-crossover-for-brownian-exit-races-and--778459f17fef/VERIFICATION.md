---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Expanding the exact hyperbolic-sine Laplace transforms in exp(-2L_N sqrt(s/D)) gives both stated signed image series, with distances d and L_N-d in the leading terms. The remaining image distances have a uniform gap in squared action near L_N=2d, and their Gaussian tails are uniformly negligible for t=b/(c_N+y) on compact y sets. The erfc prefactor and centering give intensities e^(-y) and e^(-2theta-y), since the relative right action change times c_N+y tends to 2theta. The event for the inverse-time CDF is survival to t, not exit by t. Multiplying each leading flux by N and the absolute Jacobian yields the two marked intensities; the common survival factor gives the joint densities, which factor and have total mass one. For restart, iid episode pairs give a geometric count, and truncation at a fixed count with a uniform geometric tail allows replacing each scaled duration by one without assuming finite-N mark-duration independence. For the moment claim, survival from Ab/log N to any fixed t_* is at most exp(-N^(1-1/A+o(1))) for A>1. For t>=t_*, a Gaussian step displacement larger than a common interval-length upper bound gives a uniformly positive exit probability from every possible position; the Markov property then bounds survival by q^(N floor(t/t_*)) for q<1. These bounds justify the weighted tail integrals for every fixed positive integer moment. The renewal mean is E[T_N]/p_N, so the normalized mean tends to C_theta. The finite diagnostic script was inspected, not executed; it is not needed for any limit.

## originality

PASS

The same resetting protocol and the exact finite-population renewal formulas are established prior work. The distinct finding is the moving 1/log N competition window with a joint time/mark law and the ensuing scaled geometric completion law and mean. No inspected statement covers that combined regime.

## value

PASS

This resolves the natural near-tie scale of an established physical model and identifies both the competition probabilities and their joint timing fluctuations. It distinguishes the continuous single-episode fluctuation from a discrete scaled completion law and determines the leading mean throughout the window.

The dated certificate retains the supplied scientific assessment, sources and limitations.
