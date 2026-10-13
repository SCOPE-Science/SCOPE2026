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

The file `verify.py` can be run with `python verify.py` without installing third-party packages. It uses distinct implementations of the original unitized-quandle multiplication and triangular-coordinate multiplication. It exhaustively checks every pair of algebra elements and every potential zero-product arrow for nine finite examples:

\[(q,n)\in\{(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(4,3),(5,2),(5,3)\}.\]

The two order-four checks implement \(\mathbb F_4\) using the relation \(z^2+z+1=0\). The program confirms the three strata, complete arrow rule, every ordered degree pair, the loopless arrow count, and the ring isomorphism in all these examples. The end marker is `VERIFY_OK`. The separately reconstructed small graph automorphism groups have orders \(2\), \(144\), and \(768\) for \((q,n)=(2,2),(2,3),(3,2)\), respectively; these separately computed group orders are not needed to run `verify.py`.

Finite enumeration has no logical force for arbitrary \(q\) or \(n\). The all-parameter argument is the triangular-algebra and neighborhood-block proof in `RESULT.md`; this file documents reproducibility and its boundaries only.
