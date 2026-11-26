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

RESULT.md:22–26 is the exact derivative of a finite tilted mean: qμ'_n=Cov_q(C,I). For q=1, contracting the two prescribed arcs to residual paths gives H_(n−2) plus the already closed cycles, valid even when there are zero paths. With i<j fixed, the descending image pairs force loops or a 2-cycle in (i−1)+(n−j)+1 cases, giving conditional mean H_n−[2(j−i)−1]/[n(n−1)]. Hence summing pair covariances gives −(2n−1)/12. Near 0, all one-inversion neighbors of identity merge two cycles and yield −(n−1)q. Near infinity, the reversal is the unique top state and its adjacent swaps are all next-to-top states. Swaps merge cycles except that the unique central adjacent pair for even n splits one; the resulting mean correction is (−n+1)/q for odd n and (−n+3)/q for even n. The rational functions are analytic in the relevant endpoint variables, so taking q times the derivative gives the claimed high-bias coefficients and the signs for n≥3. On a compact interval with negative derivative at the left endpoint q=1 and positive derivative at its right endpoint, a minimizer must be interior. n=1 is deterministic and n=2 has covariance −q/(1+q)². Independent exact n=3 enumeration gave the displayed partition and numerator polynomials, and their derivative numerator has exactly one positive root by its one coefficient sign change and endpoint signs. Bisection gives 2.324963524095. Independent enumeration for n=3–7 agreed at the uniform and reversal endpoints. The frozen script was not executed. No claim of general uniqueness was evaluated.

## originality

PASS

The uniform covariance is already known and is explicitly credited. The strongest prior related high-inversion finding establishes a different, parity-signed fixed-point theorem, which does not determine the total cycle count. The supported distinct result is the fixed-size total-cycle reversal, its parity-dependent coefficient and n=2 boundary, with the n=3 crossing as a special case. No strong prior coverage of that result was located in the comparisons below.

## value

PASS

The all-size reversal shows that total cycles do not respond monotonically to inversion bias, despite their negative uniform response and their extremal identity value. It isolates the adjacency mechanism distinguishing odd from even sizes, yields an exact first-size boundary, and distinguishes total cycles from fixed points. This value comes from the general qualitative reversal, not solely a small polynomial or the already known uniform invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
