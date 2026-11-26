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

In the one-edge BA tree, summing endpoint depths over edges gives 2P_n-(n-1). The parent-depth conditional mean is therefore P_n/(n-1)-1/2; multiplying parent depth by the root-attachment indicator gives zero. Iterating the expectation recurrences gives m_n=E R_n as the stated gamma ratio and E P_n=(n-1)(H_{n-1}+1)/2. The covariance recurrence is c_{n+1}=(1+3/[2(n-1)])c_n-m_n H_{n-1}/[4(n-1)]. Dividing by m_{n+1}(2n+1) telescopes to the strictly positive B_n sum with c_2=0. Its harmonic form follows by expanding H_{k-1} and telescoping the partial fractions; the harmonic difference tends to -log 2. Dividing covariance by m_n gives the shift exactly, with no stochastic-order claim. As another check, weighting histories by R_n/m_n changes each transition to degree weights with just one extra unit at the root, and denominator 2n-1; this follows by telescoping the degree ratio along the root attachments. The tilted mean then satisfies p*_{n+1}=((2n+1)p*_n+n)/(2n-1), consistent with p*_n=E P_n-B_n. Independent exact weighting of 5,913 histories through n=8 verified both means, both forms of B_n and covariance (at n=8, -169549/40960); /workspace/branches/7ba111e7-f280-4901-a6d6-ae31187eb286/replay_record2.py and replay_n8.txt. The uploaded script was inspected, not executed. Finite replay is supplementary.

## originality

PASS

The supported distinct result is the mixed finite-size identity for the sum of distances from the first vertex under the specified zero-offset, edge-seeded attachment law, including the exact degree-size-biased shift. Bounded comparison with the same-model literature and neighboring catalogue statements did not establish equivalent prior coverage. This is a best-of-knowledge judgment, not a claim of bibliographic exhaustiveness.

## value

PASS

Comparing the first hub with a natural global depth statistic is different from comparing its degree to the leaf count or observing short mean pairwise distances. The exact finite-size shift is a quantitative benchmark for selection proportional to hub degree: it has a strict sign at every nontrivial size and a linear leading cost with a specified coefficient. Neither the sign nor the coefficient follows from the marginal means, and the result does not overstate an ordering of the two laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
