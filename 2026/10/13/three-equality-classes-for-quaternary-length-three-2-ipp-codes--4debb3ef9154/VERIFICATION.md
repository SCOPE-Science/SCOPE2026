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

The scalar upper bound is checked against the inspected full proof for the quaternary case: the selected partial-order-minimal maximum can only be type III or IV; the source bounds those cases by five and supplies equality witnesses.

The equality classification is replayed by `verify.cpp`. It enumerates every five-word code containing `000`, computes all descendants of every coalition of size one or two, intersects all coalitions capable of producing each descendant, and accepts exactly when every such intersection is nonempty. It then canonicalizes the coordinatewise equality partitions under all five-word orderings and all coordinate permutations.

A reviewed replay produced:

`VERIFY_OK containing_zero=4320 labeled_maxima=55296 classes=3 group=82944`

The three normalized class counts were `1620`, `1080`, and `1620`; the derived orbit sizes were `20736`, `13824`, and `20736`; the stabilizers were `4`, `6`, and `4`; and `orbit_sum=55296`.

The program is exhaustive only for the stated finite equality layer. The impossibility of six codewords is not inferred from a timeout or partial search; it comes from the reconstructed published q=4 upper-bound argument. No statement is made for other alphabet sizes or lengths.
