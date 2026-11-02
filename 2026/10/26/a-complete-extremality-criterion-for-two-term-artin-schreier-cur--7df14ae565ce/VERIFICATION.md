---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The trace quadratic form Q(x)=Tr(a x^(p+1)+b x^2) on the 4-dimensional F_p-space determines the point count as 1+p #Q^{-1}(0). Its polar radical is the kernel of the separable linearized H(z)=a z+2 b^p z^p+a^p z^(p^2), whose F_p dimension is at most 2. The quadratic-form zero count reaches the +/- Hasse–Weil extreme precisely at radical dimension two. H fully splits over F_(p^4) iff it right-divides z^(p^4)-z; coefficient comparison with a linearized left cofactor yields t^(p+1)=N^{-1}-N^{-p} plus t^(p^2)=-t. The first equality enforces the second since its nonzero RHS is anti-Frobenius in F_(p^2). Norm fibers and (p+1)-st-power fibers yield exactly (p^2-p)(p^2+1)(p+1)=p(p^4-1) coefficient pairs. Independently built F_81 and checked all 6400 ordered nonzero pairs against an independently evaluated H-kernel: 240 extremal pairs, of which 160 maximal and 80 minimal in characteristic three. This corroborates, not replaces, the arbitrary odd-prime argument.

## originality

PASS

General Artin–Schreier quadratic-form and linearized-subspace criteria predate the claim, including Ito–Tatematsu–Tsushima. The new assessed contribution is the explicit unrestricted two-nonzero-coefficient equality on F_(p^4), its all-odd-prime existence and exact ordered-model count, in the parameter regime asked about by Almeida Filho–Tafazolian–Vieira. These can possibly be obtained from earlier general algorithms; unavailable full relevant papers remain a material implication/priority risk. On inspected evidence no explicit full-pair criterion with the exact uniform count was established.

## value

PASS

This is a complete naturally parameterized arithmetic classification, not just a sample computation: it answers a nontrivial field-size/existence question, distinguishes coefficient models from isomorphism classes, and gives a closed count for every odd prime. The exact radical condition is usable in subsequent point-count or family classification work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
