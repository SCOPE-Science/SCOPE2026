---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For binary n=9 and at most one original-predecessor overwrite (including no error), the first bit is unchanged and global bit complement gives an isomorphism between its two 256-input halves; checked all 512 words exhaustively. In the leading-zero half the exact possible-output sets from bit-tuple overwrite yield a 256-vertex conflict graph with 2816 edges. The conflict edges are equivalent to pairwise intersection of possible-output balls. An independent SciPy 1.17/HiGHS 256-binary-variable MILP with all 2816 constraints solved globally with status 0, primal -39.000000000000064, dual -39.000000000000064, zero gap and 15,676 nodes (136.13 wall seconds), so under solver correctness the half-channel independence number is <=39. An independently reconstructed direct tuple-ball check finds 39 distinct witness half-words and 78 codewords after complement, all mutually disjoint, with 396 distinct received words. Thus the full optimum is 2*39=78. The finite exhaustiveness is at n=9 only. Checked all nine Git blob IDs on the current branch and independently recomputed their Git tree SHA equal to the assigned snapshot.

## originality

PASS

Best-of-knowledge priority assessment of the exact n=9, t=1 maximum, not of the model or generic bounding method. At the same channel and parameters Gabrys–Yaakobi–Dolecek arXiv:1307.7087v2, Table II, gives only 64 <= M(9,1) <= 112; Kashyap–Zémor supply general upper bounds and not an equality 78. A published complete M(6,1) extremizer census addresses a different blocklength. A particularly relevant 2015 Sharov–Roth article was found but its full text remained inaccessible; bibliography/abstract alone cannot rule out a prior exact value. No finding in the genuinely read primary material entails the claimed equality; unindexed exact computations remain a real priority risk.

## value

PASS

This is a natural exact finite coding invariant: n=9 is the immediately following blocklength after the known n=8 exact size 44 in a standard physically motivated single-overwrite channel. The best inspected published table leaves a substantial 64-to-112 interval at the exact parameter. A 78-word construction paired with a complete 39-per-half upper computation supplies a precise benchmark and closes both sides of that gap; it is not a routine substitution, known-table recomputation, or arbitrary unmotivated restriction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
