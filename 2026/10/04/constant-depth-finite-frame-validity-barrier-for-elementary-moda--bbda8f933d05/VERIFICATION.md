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

The proof has two independently checkable steps.

1. **Modal-to-first-order reduction.** For a finitely axiomatizable elementary unimodal logic \(L\), the finite validating frames are exactly the finite models of one fixed first-order sentence \(\alpha\). This is the finite reduction established in the primary 2026 source.

2. **First-order-to-circuit compilation.** Fix \(\alpha\). On the labeled universe \([n]\), an atom \(R(x,y)\) reads one adjacency bit, equality is hardwired, Boolean connectives give constant-depth Boolean gates, and each quantifier contributes one unbounded AND or OR over \([n]\). Since \(\alpha\) is fixed, the number of quantifier layers and variables is independent of \(n\). The resulting circuit family has constant depth and polynomial size. With quantifier rank \(q\) and variable width \(w\), the direct construction has depth \(O(q+1)\) and size \(O(n^w)\).

The contrapositive is purely logical. The parity corollary additionally uses the classical theorem that parity is not in \(\mathsf{AC}^0\) and closure of \(\mathsf{AC}^0\) under circuit composition.

## Limits

The verification is for canonical adjacency-matrix encodings of labeled finite frames. It does not transfer automatically to compressed edge-list encodings, and it does not establish an application-specific lower bound for any particular modal logic.
