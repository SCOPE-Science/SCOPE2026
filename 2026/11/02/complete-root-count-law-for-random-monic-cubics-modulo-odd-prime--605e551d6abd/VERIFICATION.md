---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Every monic cubic mod p has one of five disjoint factorization types; reduction counts sum p^3. Hensel splitting of a distinct simple factor plus double root gives uniform discriminant modulo p^3, with 0,p,2p additional roots; triple reductions give 0,p,p^2 through p-adic digit conditions. The weighted PGF includes exactly root-count support {0,1,3,p,p+1,2p+1,p^2} (collisions at 3), P(R=p^2)=p^-5 and the stated fourth moment. Independent exhaustive enumeration of all 3^9=19683 monic cubics modulo 27 reproduced histogram {0:7452,1:9963,3:1215,4:486,7:486,9:81}. Separate rational differentiation at p=3,5,7,11 gave the claimed fourth-moment polynomial. General proof uses factorization and Hensel, not only finite enumeration.

## originality

PASS

The evaluated full modular-root law and fourth moment are distinct from first two moments known generally, from exact Q_p root laws that ignore temporary modular lifts, and from finite-field root counts. The seven-level singular-lift distribution is not stated in inspected primary papers. Prior cubic finite-ring tables might still give implicit coverage, a documented priority risk.

## value

PASS

Uniform random monic cubic is the lowest natural degree displaying simultaneous simple, double and triple singular root families at precision p^3; full law and p^-5 mass of p^2 roots are concrete reusable arithmetic statistics, not a rote calculation of known mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
