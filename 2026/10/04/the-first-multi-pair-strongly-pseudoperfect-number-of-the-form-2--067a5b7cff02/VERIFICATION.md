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

The proof has two independent layers.

First, the symbolic reduction is reversible. For \(n=2^a p\), every strongly pseudoperfect representation is a union of complementary pairs \((2^i,p2^{a-i})\). If \(I\) indexes the omitted pairs, then the condition that the retained divisor sum is \(2n\) is exactly
\[
2^{a+1}-1-A_I=p(1+B_I).
\]
Thus each mask determines at most one possible odd prime \(p\), and every integral prime quotient gives a valid representation.

Second, `verify.py` exhausts the finite cutoff using exact integers. Since \(p\ge3\), every \(2^a p\le11776\) has \(a\le11\). The verifier checks every subset mask for these exponents, uses deterministic trial division for primality, groups all representations by \(n\), and directly recomputes retained divisor sums. It then verifies that the only candidates up to the boundary are \(6,28,352,496,8128,11776\), that \(352\) has the unique mask \(\{3\}\), and that \(11776\) has the unique mask \(\{4,6\}\).

This finite computation certifies only the stated cutoff. It is not used as evidence for a classification at larger \(a\).
