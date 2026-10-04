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
The standalone verifier `artifacts/verify.py` reconstructs the binary code from the source generator and checks the claim in three ways.

It exhausts all \(9!\) coordinate permutations and finds exactly \(192\) that preserve all eight codewords. Their coordinate orbits are \(\{1,2,4,5\}\), \(\{3,6,7,8\}\), and \(\{9\}\).

It independently exhausts all \(168\) matrices in \(\operatorname{GL}(3,2)\) and finds exactly two row actions preserving the generator-column multiset. Each admits \(4!2!2!=96\) compatible coordinate matchings.

Finally, it generates the subgroup produced by the \(S_4\) on the four identical columns, the two component swaps, and the factor transposition described in the source. This subgroup has order \(192\) and is identical to the brute-force automorphism set.

As consistency checks, the verifier confirms parameters \([9,3,3]_2\) and weight enumerator
\[
1+2z^3+z^4+z^5+2z^6+z^9.
\]
No random sampling is used.
