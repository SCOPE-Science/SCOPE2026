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

# Reproducibility notes

The finite checker is standard-library Python and can be run from the containing directory:

```text
python3 verification/check_rook.py
```

The expected successful final line is `ROOK_VERIFICATION_OK`. Direct row/column and open-neighbourhood checks cover all constructed examples for square orders \(2\le n\le16\), and rectangular background examples with \(2\le m<n\le14\). Exact exhaustive enumeration covers every proper named-palette colouring for \(n=2,3\) and \(q=n,n+1,n+2\): the cases \(n=2,q=3\) and \(n=3,q=4\) have respectively 18 and 1,056 proper arrays, none fully conflict-free, and minimum defect counts 2 and 3. The code compares the formula \(U=\sum_s a_s^2\) directly with independently counted neighbour multiplicities and checks that any minimum-defect cells occupy distinct rows and columns.

Mathematical proof, not exhaustive computation, establishes the statement for every integer \(n\ge2\). Its decisive steps are: (i) row/column palette inequality exactly characterizes a neighbour witness; (ii) properness balances colour occurrence counts between row and column omissions; (iii) missed-colour equality defines vertex-disjoint balanced bicliques of defective cells; (iv) the sum of squared omission multiplicities is minimized at distinct omissions; and (v) a deleted-row-and-column cyclic Latin-square construction attains equality.

The checker neither certifies the infinite claim nor establishes novelty. Independent scientific review has not been performed.
