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

# Reproducible mathematical checks

Run `python checker.py` using Python 3 and SymPy 1.12 or later. The program recomputes the exact resultant and the lexicographic Gröbner relation from the stationary equations, isolates every real root of the degree-ten eliminant with Sturm rational intervals, and proves the signs on the three positive intervals using interval Horner arithmetic. It verifies polynomial-divisibility identities ensuring that the surviving root gives a genuine stationary point and excludes \(v=1\). It verifies a nonboundary strict witness, exact coefficient-convolution formulas, and strict finite-character-order aliasing for orders four through nine. A successful run ends with `CERTIFICATE_PASS`.

The exact polynomial identities are the proof's finite certificates; the supplementary randomized complex-coefficient comparisons test implementation consistency only. Root isolation is exhaustive for the specified univariate polynomial because the exact Sturm method counts all real roots; it does not enumerate infinitely many groups. The compactness, orthogonality and character-pushforward arguments cover the full stated family. The reported decimal values are for human interpretation, not verification of global optimality. No independent audit or external certification is claimed.
