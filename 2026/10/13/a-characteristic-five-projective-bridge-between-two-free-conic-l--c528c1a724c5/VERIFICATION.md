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

# Reproducibility checks

Run `python3 verify.py` with Python 3.9 or later, without third-party dependencies. The script uses exact integer determinants, gcds, quadratic discriminants, and modular arithmetic. A successful run prints `VERIFY_OK: integral incidence certificate, all primes >=7, p=5 degeneration, projective CL4 bridge`.

The checks enumerate all 35 line triples and all 21 line-pair intersections of \(\mathcal{CL}_{10}\), solve all seven binary conic-section equations over the rationals, verify 12 primitive intersection coordinates and their multiplicities, and inspect all 66 pairwise cross-product contents for exceptional primes. The script separately enumerates the complete 31-point projective plane over \(\mathbb F_5\), checks the six reduced-support singular points, transversality of conic and lines, the invertibility of \(M\), the pullback identities for every reduced line, and the conic identity across all 125 coordinate triples.

The conclusion for infinitely many primes is algebraic: exact integral discriminants, triple determinants and cross-products prove that the exceptional-prime set in the specified range is \(\{5\}\). The finite-field enumeration is exhaustive only at characteristic five; it is not used to extrapolate from a sample of good characteristics. Independent audit and external certification have not been performed.
