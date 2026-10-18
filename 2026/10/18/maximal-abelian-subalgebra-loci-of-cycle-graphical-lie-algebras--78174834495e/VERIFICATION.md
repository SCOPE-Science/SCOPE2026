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

# Verification of reduced maximum abelian-subalgebra loci

The proof is self-contained and relies on the vanishing of independent edge-bracket coordinates and the combinatorial run bound. It handles all \(n\ge4\) and fields, including characteristic two. The reported reduced-variety assertion does not claim that the original defining equations are scheme-theoretically reduced.

`verify.py` independently enumerates all \(\lfloor n/2\rfloor\)-dimensional row spaces of \(\mathbb F_q^n\), represented uniquely in reduced row-echelon form. It tests vanishing of every wedge minor associated with an adjacent edge, without relying on the support-classification proof. It checks all configurations \((n,q)=(4,2),(4,3),(4,5),(5,2),(5,3),(5,5),(6,2),(6,3),(7,2)\). Results: respectively \(2,2,2,10,15,25,2,2,14\), agreeing with the theorem. Terminal signal: `VERIFY_OK_CYCLE_MAXIMAL_ABELIAN`.

The enumerator supports prime fields directly; it does not purport to enumerate general extension fields. Finite enumeration corroborates the infinite-family result but is not its proof. Full geometric classification, node incidence, and genus follow from the separately supplied proof. Independent mathematical audit: not performed.
