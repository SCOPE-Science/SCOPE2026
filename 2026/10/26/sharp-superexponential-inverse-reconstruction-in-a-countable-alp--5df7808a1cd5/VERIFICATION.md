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

The active edge lowers the rank by one, so the run length L_i is at most r_i for every configuration. Taking the xor of output bits through i+L_i inverts by cancellation in both directions, with a finite rank/data neighborhood at each point. For any R a descent from R+1 to 0 makes a flip of the output bit at R+1 change the inverse at 0 without changing the observation; this rules out a finite memory set (every finite set fits in some such window). Conditional on the ranks, the data map is a continuous automorphism of the compact fair-bit group, preserving product Haar measure. Equivalently its restrictions to any finite set of output coordinates are triangular in those input bits once outside input bits are fixed. The xor through min(L_0,R) is observable, since only ranks 0 through R are needed to decide whether a break occurs before R. On L_0≤R it is exact; on L_0≥R+1 the missed xor contains an unseen independent fair bit even after conditioning on all ranks and observed bits. Thus the error of this decision conditional on observations is P(L_0≥R+1 | observations)/2≤1/2, which proves optimality among all measurable decisions, including at R=0 and for rank laws with zeros. Summing disjoint descending cylinders yields the stated product sum; writing their starting rank as R+1+h gives geometric factor q^{(R+2)h} and initial exponent (R+1)(R+2)/2. The quadratic logarithmic limit and strict positivity follow for fixed 0<q<1. The canonical disagreement is a bounded observable of the shift-ergodic output, giving the spatial frequency. The frozen checker and recorded output were inspected, not executed. The three posterior masses in the recorded finite test also agree by substituting (8,4,2,1)/15 into the exact cylinder formula.

## originality

PASS

Pass the fixed-window Bayes risk and its exact rank-product and geometric consequences, not the deterministic automaton or nonreversibility. Yang's rank-direction construction already supplies the same descending-chain inverse mechanism by freezing the direction to the right. The closest indexed Bayesian reconstruction result uses a noninjective binary additive map and biased finite-seed decoding rather than prediction of one inverse bit for a bijective ranked map. The inspected coding-radius literature concerns other codes and does not yield the posterior parity argument or this rank law.

## value

PASS

For a natural example of an inverse that has no uniform memory, the risk is an operationally meaningful comparison between exact symbolic memory and typical fixed-window reconstruction. Strict positivity at each radius together with an exact superexponential rate quantifies this distinction. The lower bound rules out improvements by nonlinear decisions and by using the opposite side of the window; a truncation upper bound or the topological example alone would not establish that.

The dated certificate retains the supplied scientific assessment, sources and limitations.
