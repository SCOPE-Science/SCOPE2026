---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For f=x0 xor g(y) with y in F2^4 and odd wt(g), g has degree 4 and nonlinearity s in {1,3,5} (odd affine distance, four-variable covering-radius bound). A closest affine ell makes g+ell the indicator of an affinely independent s-point subset: the s=5 dependent case would lie in an affine hyperplane, toggling its affine indicator to reduce distance to 3. Affine input changes reduce to S={0},{0,e1,e2},{0,e1,e2,e3,e4}. Every degree<=2 polynomial is A(y)+x0 B(y), dim A=11, dim B=5; the top-degree quotient rank of gB is s (explicit 5x5 matrices), hence restriction rank 11+s to both graph supports and each annihilator dim 5-s. No nonzero degree-1 annihilator because g has degree 4; the degree-3 restriction kernel is nonzero since dim RM(3,5)=26>16. Therefore AI=3 iff s=5, NL(f)=2s. Independent computation directly formed full graph restriction evaluation rows and recovered kernel dimensions 4,2,0 in the three normal forms. The order-five one-cycle 24,1128,896 nonlinearity counts are Turan 2012, not new; independent source checker enumerates 2048 maximum-period feedback functions but logs alone are not relied upon.

## originality

PASS

Turan 2012 already tabulates precisely the 24/1128/896 maximum-period nonlinearity distribution and parity restriction. The additional asserted all-odd-g annihilator-rank identity and AI equivalence are not found in inspected primary material; general algebraic-immunity literature discusses different families. Qualified originality PASS for the rank theorem, not for the counts.

## value

PASS

Algebraic immunity and nonlinearity are generally distinct cryptographic invariants; for a naturally constrained maximal-period feedback family, a complete exact rank law relates them and classifies all quadratic annihilator dimensions. The parity hypothesis, normal forms, and immunity threshold make this a useful intrinsic structural theorem; reusing the known maximum-period nonlinearity multiplicities alone would not be valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
