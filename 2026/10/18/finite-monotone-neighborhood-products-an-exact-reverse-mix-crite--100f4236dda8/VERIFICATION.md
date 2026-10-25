---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At a fixed product point P⊆X×Y, set Q={u:P_u∈G}. Rectangle □ means some U∈F,V∈G with U×V⊆P, while □1□2 means Q∈F. For finite nonempty upward-closed reflexive F,G, if {x}∈F then {x}×P_x works; if G binary-intersection closed, the finite intersection of P_u for u∈Q works. Conversely when singleton absent and G nonintersection closed, choose inclusion-minimal U∈F of size≥2 and B0,B1∈G with intersection not in G; sections B0/B1 over distinct members of U force □1□2 but any witness rectangle must use U and its vertical neighborhood would lie in the forbidden intersection. Transpose proves second equivalence. A nonintersection-closed reflexive family requires carrier≥3, so one reverse fail needs 2×3=6 and both need 3×3=9. Verified explicit 6- and 9-point truth sets; the 9-point valuation makes both iterated boxes true and rectangle box false. No infinite generalization.

## originality

PASS

Previous full-product filter semantics and normal-frame rectangularization theorem are directly relevant and were inspected. Their hypotheses assume intersection-closed families; all finite such filters are principal, so their reverse mix cannot fail, whereas this claim characterizes the nonnormal monotone case and proves finite cardinality sharpness. It does not rebrand the known forward implication or normal collapse as novel.

## value

PASS

The factorwise iff criterion settles when two-step neighborhood quantification reduces to a rectangle under precisely weakened nonnormal hypotheses. Six- and nine-world sharp thresholds identify the first natural expressive separation; this is structural modal semantics, not a one-off tiny-model calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
