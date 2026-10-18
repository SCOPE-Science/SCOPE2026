---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Checked the dimension-independent two-region norm inequalities directly. Set q=p1+p2, with p2(x+a)=p2(x) from a·Lambda2 subset Z. Because S1 and S1+a⊂S2 are disjoint, ||q(·+a)-q||^2_{S1}<=2||q||^2_{S1∪S2}; the A1 Riesz bound and phase gap m yield ||c1||^2<=2||q||^2/(A1 m^2). On S2, ||p2||^2<=2||q||^2+2 C12||c1||^2 and A2 lower Riesz yields the displayed coefficient reciprocal L. Cauchy-Schwarz with energies (B1+C12)||c1||^2 and <=2 B2||c2||^2 gives U=B1+C12+2B2. Completeness is not inferred from boundedness: translate f1 to S1+a and apply Lambda2 completeness; the remaining Lambda1 Fourier factors (1-e^{-2pi i a·lambda}) are nonzero, so f1=f2=0. The phase gap is positive due to dist(Lambda1,Gamma_a)>0. This reconstructs a full Riesz basis, not just finite-coefficient bounds.

## originality

PASS

Lee Theorem 4 establishes the same qualitative translated-domain union basis, and its quantitative formulas are not stated in the materially inspected theorem/proof. The candidate derives explicit conditional lower and upper bounds from a direct finite-coefficient difference calculation, with C12 as a data input. Nearby construction papers use different interval/rectangle structures. Best-of-knowledge quantitative distinctness is plausible, without implying qualitative basis existence itself is new.

## value

PASS

A direct usable conditioning bound with deterioration as m→0 for a translated-domain Riesz basis union is a quantitatively motivated question, not a generic numerical slice. It upgrades Lee’s existence theorem to uniform estimates in arbitrary finite dimension when standard constituent constants and one cross-Bessel constant are available.

The dated certificate retains the supplied scientific assessment, sources and limitations.
