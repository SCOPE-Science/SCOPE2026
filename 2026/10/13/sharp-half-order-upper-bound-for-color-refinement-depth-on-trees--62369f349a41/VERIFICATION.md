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
The theorem has both a uniform proof and an exhaustive finite check.

The attached `verify.py` uses NetworkX's generator of non-isomorphic trees. For every tree on \(2\le n\le17\) vertices, it runs ordinary color refinement from the uniform coloring and verifies
\[
\operatorname{Stab}(T)\le\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
For each order it also checks that the maximum observed depth equals the claimed bound. Across these orders this covers 81,136 unlabeled trees and 113 extremal instances. The expected output is:

`VERIFY_OK trees=81136 n=2..17 extremal_instances=113 bound_and_sharpness=PASS`

The checker requires NetworkX. It is a consistency test only; the all-order theorem rests on the two-front witness lemma in `RESULT.md`.
