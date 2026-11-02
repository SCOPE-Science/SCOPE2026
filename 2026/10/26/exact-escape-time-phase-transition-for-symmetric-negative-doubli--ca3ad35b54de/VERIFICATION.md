---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For 0<a<=2/5, the left/right inverse branches are affine and each shrinks Lebesgue length by 1/2. For a<=1/3 only alternating outer intervals survive; at 1/3<=a<=2/5 the four disjoint B_L,C_L,C_R,B_R blocks form an exact inverse-branch Markov transition with c_{n+1}=c_n/2 and b_{n+1}=(b_n+c_n)/2, initialized by c_1=(3a-1)/2 and b_1=a/2. Inductively m(E_n)=2^-n[2a+2n(3a-1)_+] for every real a and n>=0. Normalized initial law gives the stated tail, hazard and expected entrance time; above 2/5 the formerly forbidden inverse branches add (5a-2)/2 to the n=2 extension, with true mass 6a-2. Both equality parameters are explicitly handled. An independent standard-library exact-rational interval inverse-iteration gave 114 horizon/parameter tests and three upper-range boundary witnesses. The exact all-horizon result rests on the block inclusions/recurrence, not the finite tests.

## originality

PASS

Best-of-knowledge mathematical comparison of the same object, definitions, parameter quantifiers, and implication strength. Foundation and partial coverage are credited explicitly; neither failed searches nor inaccessible full literature alone are represented as novelty proof. The same object and threshold numbers are prior art, but a periodic-orbit zeta is not the same as finite-time Lebesgue measure of points that may escape. Nonimplication from identical zeta across continuum of distinct E_n is decisive; direct inverse-branch measure geometry is new mathematical work beyond prior orbit census.

## value

PASS

The parameter a=1/3 changes an exact geometric first-exit law into n*2^-n decay without changing escape exponent log2, while a=2/5 marks the sharp upper validity endpoint. This is an explicit Lebesgue observable for a natural open Lorenz/negative-doubling family, invisible to topological entropy and fixed-point/zeta counts; complete real-parameter exact law is useful even when generic transfer-matrix methods exist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
