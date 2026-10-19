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

# Reproducibility and limits

Execute `python3 verify.py` in a directory containing the extracted files. The program uses only the Python standard library; its deterministic stdout is supplied in `verification_output.txt`.

The first independent check constructs every permitted full length-\(n\) edge for several small \((q,n)\), calculates the exact directed Matrix-Tree cofactor by fraction-free integer elimination, applies the BEST degree product, and compares against the closed form. The second check enumerates complete local outgoing-order permutations with a fixed initial root edge, traverses every permitted arc greedily, and accepts only complete closed Euler tours. It never invokes the reduced colored determinant and independently reproduces several counts.

The checks include \(q=2\) for \(2\le n\le10\), \(q=3\) for \(2\le n\le6\), \(q=4\) for \(2\le n\le4\), and \(q=5\) for \(n=2,3\) in the full determinant calculation, with exhaustive tour enumerations on smaller parameters. Larger parameter values are established by the analytical graph proof, **not** by extrapolation of computation.

The exact theorem is for nonbinary labelled alphabets and rotation equivalence alone. The binary check confirms consistency with established earlier results but is not offered as a new binary theorem. The relevant external literature comparison is in RESULT.md and REVIEW.md. Independent audit is not performed.
