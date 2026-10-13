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

# Reproducibility

Run `python3 verify.py` with Python 3 and no additional packages. All field operations are implemented explicitly; the order-four field uses the irreducible polynomial \(t^2+t+1\) over \(\mathbb F_2\).

The checker enumerates all \(q^8\) ordered pairs of \(2\times 2\) matrices for each \(q\in\{2,3,4,5\}\). It verifies the commuting-fiber count and, in characteristic two, the count for every nonzero scalar commutator. It then enumerates actual quotient Lie-algebra classes and all ordered pairs in them for one edge over \(q=2,3,4\), and for a two-edge path, a three-edge path, and a triangle over \(q=2\).

Observed selected direct quotient results:

- \(\mathbb F_2\), one two-arrow class: quotient size \(8\), commuting pairs \(28\), probability \(7/16\).
- \(\mathbb F_3\), one two-arrow class: quotient size \(27\), commuting pairs \(105\), probability \(35/243\).
- \(\mathbb F_4\), one two-arrow class: quotient size \(64\), commuting pairs \(496\), probability \(31/256\).
- \(\mathbb F_2\), three-edge forest: quotient size \(512\), commuting pairs \(21952\), probability \(343/4096\).
- \(\mathbb F_2\), triangle: quotient size \(1024\), commuting pairs \(52096\), probability \(407/8192\).

The checker also independently compares the graph subset expansion with enumeration of scalar vertex coboundaries. Successful final line: `VERIFY_OK`. These are exhaustive **finite examples**; the theorem for all quivers and all finite fields follows from the written algebraic proof, not from extrapolation of the checks. Independent audit has not been performed.
