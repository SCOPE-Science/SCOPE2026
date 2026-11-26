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

For fixed interior p, Y_i=pX_i can be coupled to min(p,V_1,…,V_i) with iid uniform V_i. After the first V_i<p, jumps equal ordinary lower-record indicators, independent Bernoulli(1/i) by insertion ranks. The discrepancy is bounded by a geometric random time. Thus N_n/log n→1 in L² and almost surely (for the latter, the centered weighted variance sum with weights 1/log i is finite, and Kronecker's lemma applies). The exact tail of Y_i gives E N_n=log n+O(1) and summability of E Y_i². The jump density is p, the stay probability 1−pX_{i−1}, and the score variance given the past is p^(−2)Y_{i−1}/(1−Y_{i−1}); its difference from p^(−2)Y_{i−1} is summable in expectation. The martingale compensation of N_n makes the normalized predictable score variance tend to one, and interior p gives bounded increments for the martingale CLT. In the locally uniform Hessian the jump term is −N_n/q², while the stay term is almost surely bounded on compact interior intervals. Taylor expansion gives LAN. For the MLE, the stated fixed-M local bracketing is read with arbitrary tolerance: for each tolerance choose M, then let n grow. Alternatively for fixed small epsilon>0, the curvature on [p−epsilon,p+epsilon] is bounded below in magnitude by N_n/(p+epsilon)², and S_n(p)=O_P(sqrt(log n)), so the scores at the two endpoints have opposite signs with probability tending to one. Strict concavity and the score equation give consistency and the stated Gaussian limit; LAN also gives regularity under the stated local shifts. The endpoint atom contributes n²(1−p)^(n−2), which vanishes. The z=nx density and score converge to pe^(−pz) and 1/p−z, dominated in the information integral by a constant times exp(−pz/2)(1+z²). Both first-order information constants and the normalization are therefore correct. The supplied verification script was inspected, not executed; its finite checks are not used as evidence for LAN.

## originality

PASS

The supported distinction is inference from the complete discrete path at a fixed horizon: logarithmic Fisher information, LAN, and an efficient MLE, with the endpoint comparison. The endpoint limit is a short consequence of the known exact marginal plus score control, not a standalone novelty claim. The primary and catalogue comparisons do not establish coverage of the complete-path inference theorem. This is not a historical-priority certification.

## value

PASS

The result quantifies how a decreasing process remains estimable from its complete discrete trajectory despite a vanishing jump rate. It shows that one endpoint loses a logarithm in Fisher information, gives the correct sqrt(log n) local scale with its sharp constant, and shows that the full-path MLE attains it. This is a distinction between observation experiments, not just a transformation of the known marginal law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
