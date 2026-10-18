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

# Verification scope

The proof works with \(s\) positive integer species counts and a fixed census \(N\). The exact reduction to partitions of \(k=N-s\) allows the first seven excess-individual layers to be certified by a finite table without fixing or bounding \(s\). In this certificate, ties are distinguished from strict reversals. The positive-abundance requirement excludes zero-frequency symbols.

# How to replay

Run `python3 verify.py` using the standalone included file and a standard Python runtime. It uses `functools`, `itertools`, and `math`, with arbitrary-precision built-in integers and no external dependencies. It exhausts ordinary partitions for \(k\in\{0,1,2,3,4,5,6,7\}\), checks all pairs, confirms the two order-two tie classes at \(k=6\), the unique strict reversal at \(k=7\), and exact product and square-sum identities for examples at 58 successive richness values. An additional analytic two-species argument covers \(s=1,2\).

The finite loops are complete for the theorem's first-disagreement thresholds **only because** the mathematical reduction bounds the excess integer partition size by seven. Nothing claims that the code exhausts all larger census sizes. Numerical rounding, entropy floating-point evaluation, and external packages are unnecessary to certify the finite table.

# Status and limitations

Same-model correctness, originality, and value review passed; independent audit has not been performed. Some historical full texts, particularly Nagendra (2002), were inaccessible. A finite literature search cannot prove worldwide uniqueness; unindexed stronger theorems could change the originality assessment. The result makes no inference about empirical data uncertainty or stochastic community assembly.
