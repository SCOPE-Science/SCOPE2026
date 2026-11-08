---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For a nonempty-valued path-independent choice function C on all menus of labelled U, |U|<=5, with |C(A)|<=q, the Aizerman-Malishevski representation expresses every such C as the union of highest-priority singleton selections from a finite family of strict linear orders. Its converse is verified: pointwise OR of priority-maximizers is path independent. Exhaust all subsets of n! orders via exact bitmask union closure (n=5 produces 59386 distinct rules), and for q=1..5 test ALL capacity<=q source rules and ALL q-acceptant targets by inclusion on every menu. Independently authored and compiled a separate C++ exhaustive implementation from the mathematical specification; verified at n=5 source/target counts q1 120/120, q2 13710/480, q3 56140/80, q4 59385/5, q5 59386/1, all zero unexpandable, plus q=3 extension multiplicities 3340,7320,9540,11160,3780,7020,8460,3240,1840,440 for 1,2,4,6,8,10,12,16,24,36 expansions and exactly 39860 law-of-aggregate-demand violations. Verified every generated rule satisfies PI by direct all-menu-pairs test. Prior six-item obstruction reported by Chambers-Yenmez is NOT claimed new. Finite exhaustive proof depends on the classical representation but does NOT assert arbitrarily large |U|.

## originality

PASS

Best-of-knowledge PASS for the FINITE five-item universal existence guarantee and complete multiplicity census; the six-item counterexample, representation and general rejection characterization are acknowledged prior. The primary 2026 paper abstract was read but full text unavailable via lawful web/authorized institutional VPN, a significant residual historical-coverage risk but not by itself a proof of coverage.

## value

PASS

Sharp minimum size permitting failure is a natural finite-size boundary for acceptant expansion of Plott choice functions. Complete labelled n=5 census also quantifies expansion multiplicities and shows thousands of applicable rules violate the previously known sufficient law of aggregate demand. The result is valuable without a global solution for q<=3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
