---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

A Ritt power \(T^N\) is power bounded, hence so is \(T\). Spectral mapping then forces every peripheral point of \(T\) to be an \(N\)-th root of unity, making the least common multiple \(d\) finite and necessary for every Ritt exponent. For sufficiency, set \(S=T^d\) and \(a=N/d\). The only possible peripheral point of \(S\) is \(1\), so \(Q_a(z)=1+z+\cdots+z^{a-1}\) has no zero on \(\sigma(S)\) and \(Q_a(S)\) is invertible. The identity \(I-S^a=(I-S)Q_a(S)\) transfers the discrete derivative estimate from the Ritt operator \(S^a\) to \(S\). Positive powers of a Ritt operator are Ritt by a finite telescoping argument. This proves necessity and sufficiency, including \(d=1\).

## originality

PASS

Bouabdillah–Le Merdy provide the finite-peripheral Ritt\(_E\) framework and derivative criteria, but the inspected theorem statements do not classify all ordinary-Ritt powers of one operator. Badea's 2026 abstract gives universal Ritt powers under displacement hypotheses and characterizes odd Ritt powers in uniformly convex settings, not the exact operator-specific divisibility ray under the sole assumption that one Ritt power exists. Its full PDF was not accessible in this run, so that plausible source is recorded as a residual risk rather than treated as noncoverage evidence.

## value

PASS

Once existence of one Ritt power is known, the theorem completely determines every Ritt exponent from the peripheral spectrum, gives the unique least exponent, and yields gcd closure. This is a natural reusable structural completion of the power question rather than a routine estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
