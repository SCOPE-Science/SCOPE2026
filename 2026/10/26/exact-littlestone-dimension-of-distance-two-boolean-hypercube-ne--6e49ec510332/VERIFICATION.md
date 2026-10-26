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

# Verification instructions and limits

`python3 verify_shell2.py` requires Python 3.10 or later, the standard library, and the adjacent exact file `shell2_witnesses.json`. Run with the two files in the same directory. The code checks all 54 root-to-leaf paths in complete binary mistake trees at dimensions \(2,3,5,7\), confirms their depths and distinct leaf centers, computes the Littlestone recurrence independently for all dimensions \(1\) through \(7\), and tests weight-two intersection profiles for dimensions \(5\) through \(12\). It separately enumerates all four-point VC candidates in dimension five, verifying that \(\operatorname{VCdim}=3\) there, while the tree has dimension four.

The expected terminal line is `VERIFICATION_OK`; the exact recorded console output is `verify_shell2_output.txt`. All vectors in the JSON tree are nonnegative integers using binary coordinate encodings; a query/center pair has label one precisely when the bit count of their XOR is two. The file contains no probabilistic certificates or hidden dependencies.

The finite execution confirms its concrete witnesses and small cases, not the universal upper bound. The latter is the separate proof that any post-positive-branch query on the weight-two center layer sees only a full set, a two-vertex edge cut, an internal four-clique, or an empty set, and that the cut's two-star subfamily has rank at most three. No independent scientific audit or formal proof assistant certification has been performed.
