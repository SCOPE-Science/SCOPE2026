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

Over F2 any commutative algebra has F2-linear squaring map A; over F_{2^s}, x^2=x iff x=A sigma(x). Fitting decomposition kills the nilpotent component and reduces to invertible B on stable image W=im A^n, dimension r. A normal basis of F_{2^L} for L=ord(B) explicitly parameterizes all 2^r geometric idempotents; Jacobian I for equations x-A x^[2] ensures the zero-dimensional scheme is reduced finite etale. Arithmetic Frobenius acts B^{-1}, giving N_s=2^{dim ker(A^s-I)} and Mobius closed-point/zeta formula. In the perfect case the first nonzero idempotent appears when some eigenvalue order divides s; its minimal eigenvalue order is <=2^n-1, and equality forces a primitive irreducible characteristic polynomial of degree n. Conversely every primitive companion realizes it, one Frobenius orbit on the nonzero idempotents. Independently enumerated all 16 2x2 binary matrices over F2 extension degrees 1..4, five 3x3 matrices at degrees 1..3, comparing direct idempotent enumeration against matrix-power nullities without relying on check.py; every case agreed. Inspected actual check.py, including cubic order-seven and nonsemisimple intended cases.

## originality

PASS

Earlier evolution algebra papers give existence and classification of idempotents in small dimensions and some graphical subfamilies; a published result for fixed points of iterated squaring in graphical evolution algebras already contains a restricted one-step counting identity. That special case does not cover arbitrary binary structure matrices, all extension degrees, full Frobenius orbit zeta, or sharp primitive-polynomial iff characterization. General linearized-polynomial/Hilbert 90 theory makes these deductions elementary, so an equivalent general semilinear fixed-point classification is a plausible priority risk; no decisive covering source was identified. The most relevant 2026 survey full text was inaccessible (institutional VPN disconnected) after OA attempts; this alone is not scientific rejection.

## value

PASS

The first extension degree where a perfect binary evolution algebra gains a nonzero idempotent is a natural arithmetic splitting invariant; it can be exponentially delayed in dimension, with exact extremizers and complete closed-point data. This is an exact classification of a motivated phenomenon, not a re-labelled numerical table, although its tools are classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
