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

# Verification record

The proof in `RESULT.md` is integral and applies to every integer \(t\ge3\) and all vectors of nonnegative integers \((q_1,\ldots,q_t)\). Its nonstandard step is that the integral Mayer--Vietoris connecting morphism is a unit, witnessed by the explicit product of peripheral suspension cycles. This is checked symbolically in the proof, not inferred from a finite log.

`verify_bouquet.py` independently generates forbidden clique masks and all admissible faces; it computes simplicial boundary ranks over \(\mathbb F_2\), derives all reduced Betti numbers, and checks the alternating face count. The exact run printed in `verification_output.txt` covered 57 parameter tuples with \(t\in\{3,4,5\}\), at most 13 graph vertices, and 130,478 faces. Rerun from the same directory with `python3 verify_bouquet.py`.

No finite test determines the infinite homotopy type or integral torsion; no claim of an external or independent audit is made. The two-source mathematical comparison and the restrictions on larger clique attachments are stated in `RESULT.md` and `REVIEW.md`.
