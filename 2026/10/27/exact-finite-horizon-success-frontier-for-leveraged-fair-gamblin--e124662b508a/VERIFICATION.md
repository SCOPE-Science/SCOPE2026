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

Reconstructed the finite-horizon Bellman induction for arbitrary conditional next-wealth laws. At k=1 the affine bound from the mean touches only at the legal endpoints. For k>=2 and a=(L-1)z, the logarithmic derivative of V_(k-1)(u)/(u+a) has the sign of z(M/u)^(1/(k-1))-u for L>1, with opposite signs at small u and u=M, and a unique zero at u*=z(M/z)^(1/k). The line c(y+a) also dominates the terminal value for y<=0, so the mean gives Lzc for every conditional law, not merely binary bets. Equality forces support at -a and u*, and the mean fixes the two masses. Induction along the visited surviving history gives the exact value and uniqueness; the two-point construction stops within budget. For L=1 stopped nonnegative fair wealth gives x/M, attained immediately. Strict convexity of log(1+(exp(t)-1)/L) gives strict budget monotonicity; its quadratic coefficient is (L-1)/(2L^2), giving the displayed deficit. The unlimited supremum follows by bounding success by time N and taking the increasing union for each policy, together with finite-budget achievability. The frozen grid tests were inspected, not run or used as the universal proof.

## originality

PASS

Credit Kuszmaul for the model, the strategy attaining the displayed expression, and the unlimited-horizon bound. The supported distinct result is the matching finite-horizon upper bound over arbitrary adaptive laws, its equality characterization, and the resulting sharp expansion of optimal success. Neither the inspected assertions nor the nearest indexed results establish this finite-budget optimum.

## value

PASS

The sharp finite budget changes the attainable success despite unchanged fair leverage constraints. Proving the global upper bound and equality law settles whether adaptive laws can improve on the known fixed-multiplier strategy and quantifies exactly how the optimum approaches the unlimited value; it is not just evaluation of that strategy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
