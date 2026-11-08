---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

A strictly upper-triangular binary matrix B with Boolean B²=0 has disjoint sets S of nonzero rows and T of nonzero columns (any overlap would create a 2-step path). Off isolates, each index is S or T, and each active edge runs forward S to T. An ordered word with a=|S|, b=|T| encodes exactly one Ferrers inversion diagram lambda inside a×b, with ab−|lambda| permitted edges. For fixed j and lambda, the probability of any active zero row or column among 2^(ab−|lambda|) assignments is bounded by a*2^(−(b−|lambda|))+b*2^(−(a−|lambda|)), tending to zero. The exact isolated-vertex deletion convolution H_n=∑_u binom(n,u) H_(n-u)^0, Gaussian-binomial/partition-product majorant Q^(−2) and lower bound 2^floor(n²/4) imply isolates negligible. Pointwise counts normalized by 2^m² (even) tend to 2^(−j²−|lambda|), and by 2^(m(m+1)) (odd) to 2^(j−j²−|lambda|). Countable dominated convergence and Scheffe yield total variation, product law P_even(j,lambda)=(2^(−j²)/Z0)*Q*2^(−|lambda|), P_odd=(2^(j−j²)/Z1)*Q*2^(−|lambda|). Exhaustive direct n=1..6 integer counts 1,2,6,26,158,1330 corroborate combinatorial premises, not the n→∞ convergence.

## originality

PASS

The exact total counts and theta normalizers are prior work (OEIS A135922, earlier Kotesovec asymptotics), and Bevan–Cheon–Kitaev give exact poset/q-Stirling enumeration. Neither inspected source establishes independence of the entire inversion Ferrers diagram and source imbalance in total variation. Possible equivalent asymptotic from Mallows words/q-Stirling Boltzmann measures remains an explicit priority risk.

## value

PASS

The full partition-valued law refines known total enumeration of naturally labelled height≤2 posets and identifies typical ordered support geometry at O(1) inversion deficit. Asymptotic independence from the source-side cardinality defect provides a naturally motivated microscopic/mesoscopic decomposition; total sequence asymptotics alone do not determine this distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
