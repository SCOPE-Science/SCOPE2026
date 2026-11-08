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

The model y^3=x^5+a x^3+b x+1 is tame Kummer of degree 3 in characteristic 2: f=x f' +1 proves separability for every coefficient pair, five simple finite branch points and one at infinity give 2g-2=-6+12=6. The listed four differentials dx/y, dx/y², x dx/y², x² dx/y² are regular with infinity valuations (1,6,3,0), form a basis, and their semilinear Cartier map C(e1)=e4+sqrt(a)e3+sqrt(b)e2, C(e3)=e1, C(e2)=C(e4)=0 is obtained by extracting odd terms in f(x) dx. With w=C(e1), C(w)=a^(1/4)e1, so stable C^4-rank is zero exactly when a=0, otherwise two; rank C=2 throughout, so a-number 2. f'=(x²+sqrt(a)x+sqrt(b))² has 1 vs 2 distinct critical roots; count q coefficients with a=0 and q(q-1) elsewhere. This is set-theoretic, not a determinantal-scheme multiplicity. Independent GF(2) matrix rank powers for all (a,b) reproduce the four ranks; finite fields cannot prove the all-algebraically-closed classification.

## originality

PASS

PASS qualified: general superelliptic Cartier/a-number and genus-four 2-rank techniques are established; the final novelty is the parameter-specific stable Cartier-rank divisor in an everywhere-smooth cyclic trigonal genus-four family. The general a-number=2 is not independently new. Material checked from Dragutinović and Sankar does not give this exact coefficient-marked locus or derivative collision, but unindexed specializations remain possible.

## value

PASS

A natural two-parameter genus-four cyclic trigonal cover gives a sharp and nontrivial 2-rank jump despite constant a-number, localizes the rank-zero locus and relates it to a polynomial-critical-point collision. This supplies a concrete arithmetic stratum and exact finite-field marked counts; a technical stable-rank invariant is of mathematical use beyond generic ordinarity, without claiming moduli-level classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
