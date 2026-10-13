---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

`artifacts/verify.py` reconstructs the Kulkarni--Kiyavash source convention directly for every \(2\le n\le11\). For every source pair it compares two independently implemented compatibility tests: exact intersection of the distinct one-deletion shadows, and a dynamic-programming longest-common-subsequence calculation. The two tests agree on every pair.

For each length, the script enumerates every candidate subset at successive sizes until the first cardinality with no compatible subset. This proves the optimum sequence \(1,1,1,1,1,1,2,2,3,4\) for lengths \(2\) through \(11\), together with maximizer counts \(1,1,1,2,3,4,1,6,3,3\). At length \(11\), all \(\binom{19}{5}=11628\) five-subsets are checked and rejected, while exactly three four-subsets survive.

The verifier checks the three explicit maxima, their common all-zero word, the weight-two condition on every other codeword, the shadow-size profile \(1,5,5,5\), total received-word coverage \(16\), and the reversal orbit sizes \(1\) and \(2\). It separately evaluates Kulkarni--Kiyavash Theorem V.2 at \((n,d)=(11,2)\) as \(823/105\), whose integer consequence is only the upper bound \(7\).

The claim is finite and exact. No random sampling, heuristic search, timeout result, or extrapolation beyond length \(11\) is used.
