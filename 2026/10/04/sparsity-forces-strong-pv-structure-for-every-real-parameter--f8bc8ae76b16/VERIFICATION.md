---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The total-reality hypothesis can indeed be removed from Campbell's proof. For a sparse noninteger real parameter \(a\), Campbell's lemmas first exclude \(a\in(0,1)\). If a nontrivial conjugate \(a^\ast\) is nonreal, then it is automatically outside the real compact set \([0,1]\cup\{a\}\); if it is real but not in \((0,1)\), irreducibility excludes the endpoints \(0,1\), so it is again outside that set. This replaces the sole load-bearing use of total reality in Campbell's proof. The remaining transfinite-diameter argument, the identification of complete conjugacy classes in the compact set with only \(0,1\), and the auxiliary polynomial contradiction then run unchanged. Pinch's real discreteness-to-algebraic-integrality input and the Fenner--Green--Homer strong-PV uniform-discreteness theorem supply the two outer implications.

## originality

PASS

Campbell proves the necessity direction only under the explicit additional assumption that \(a\) is totally real. Inspection of the complete proof shows that this hypothesis is used to declare the chosen bad conjugate real before excluding it from \([0,1]\); a nonreal conjugate is already excluded from that real set, so the argument extends. Fenner, Green and Homer formulate the strong-PV discreteness converse as an open conjecture and prove the strong-PV sufficiency. Current Resultary search returned only the assigned all-real-parameter resolution and no broader prior theorem. The audited result therefore genuinely enlarges the published theorem and resolves the full real-parameter necessity, rather than merely specializing an existing statement.

## value

PASS

The theorem removes a substantive algebraic hypothesis from a newly published proof and settles the entire real-parameter case of a strong-PV discreteness characterization that is explicitly open in the modern theory. Automatic total reality is a structural conclusion about the parameter, so this is a natural theorem-level closure rather than a cosmetic sharpening.

The dated certificate retains the supplied scientific assessment, sources and limitations.
