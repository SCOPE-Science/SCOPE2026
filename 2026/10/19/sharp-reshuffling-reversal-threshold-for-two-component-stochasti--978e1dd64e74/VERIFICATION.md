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

Projector idempotence makes each same-sample update I−kP_i, with eigenvalues 1 and 1−k. The two cross products are transposes whose off-diagonal terms cancel upon averaging their Gram matrices; the two repeat words contribute (I−kP_i)^4. Thus RR and WR are diagonal in the two bisectors, and the maxima are taken after averaging. The factorizations give W_+<W_− and R_−<W_−; the remaining difference R_+−W_− is −k(2−k)P/4. Positivity follows from the nonzero cross-product off-diagonal magnitude kab·kt in the strict domain. Equality of norms through both RR steps would require a nonzero vector in both kernels; the repeat words give the same obstruction for WR in expectation. Hence both factors are strictly below one. To locate the first reversal, P>0 for k≤1 and for t≥1/√3 when k<2 by the displayed factorizations. On 0≤t≤1/√3, ∂_kP<0 for 3/2≤k≤2: at t=0 it is −2(k−1); elsewhere use E(t)−3t(1−t²)=6t³+t²−2t−1≤t²−1<0. Also P(3/2,t)−1/3=(t−1/3)²(27t+15)/4, and P(2,1/3)=−8/9. The compact angular minimum is strictly decreasing on that step interval. It crosses zero at a unique interior angle since P at both angular endpoints is positive for k<2 and ∂_tP has exactly one positive root for 3/2≤k<2. An independently written exact check reproduced the resultant 48k⁴Q(k), Sturm endpoint variations 4 and 3, and witness R−W=5/729. The witness Hessian has eigenvalues 2/3 and 1/3. No uploaded script was executed.

## originality

PASS

The supported distinct claim is the exact comparison of the two worst-start factors and the global effective-step frontier. The same operators, two-step moment matrices, and existence of a directional reversal are covered by the indexed overrelaxed Kaczmarz comparison; none of those is credited separately as original. Its pointwise threshold differs mathematically from the worst-start frontier.

## value

PASS

This isolates the difference between directional reversal and deterioration of a sharp worst-start guarantee. The exact first step where the latter happens, and a rational condition-number-two witness where both methods contract, make the counterexample useful for interpreting finite-horizon sampling comparisons. It is not merely the sign reversal of a single direction or a change of algorithm name.

The dated certificate retains the supplied scientific assessment, sources and limitations.
