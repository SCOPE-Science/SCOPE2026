---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Eliminating b and using the bijection u=2a−x gives 3xu²=4y−x³. For a unit x, the target is affine-equivalent to u²: the (p²−p)/2 unit squares each have two simple roots and zero has p roots. For x=pv≠0, first require y=pw, then cancel p from the congruence before reducing to 3v u²=4w modulo p; each solution has p lifts. This gives one fiber of size p and (p−1)/2 of size 2p for each of the p−1 such x. At x=0 there is only the fiber at y=0 of size p². These cases give exactly the stated histogram, including p²−1 fibers of size p. Summing nonempty fibers and squared multiplicities gives the stated support and energy. Frequency orthogonality contributes p⁴ and the coefficient normalization contributes p⁻⁸, so the constant-input moment is energy divided by p⁴ as asserted. An independent per-slice direct enumeration verified all of these multiplicity levels and energy for p=5,7,11,19,29; at p=5 the histogram in level order is (392,200,24,8,1).

## originality

PASS

The indexed prior work on exponential spectra uses the same graph, but its statement is a classification of orthogonal exponential bases, not ordered convolution fibers. Field extension results and scalar two-cube counts do not include the required prime-square graph lifts. A later, stronger prime-power census gives exactly this specialization and is credited as verified overlap, not as a prior result based on the dated records. The assessment is best-of-knowledge.

## value

PASS

The first nonreduced level is a natural comparison with the field cubic graph. The exact ordered convolution partition quantifies the singular strata that the field and the normalized moment alone do not exhibit; it yields exact support and a test value for ring extension problems. The square-root step uses standard lifting, but the motivated, complete decomposition of the graph convolution is the useful result, not the lifting fact itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
