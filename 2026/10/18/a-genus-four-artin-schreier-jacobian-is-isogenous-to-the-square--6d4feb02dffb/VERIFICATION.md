---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For the smooth F3 model y³−y=x²/(x³+2x²+1), denominator is irreducible cubic, yielding 3 simple geometric poles, genus four via Artin–Schreier Riemann–Hurwitz and 3-rank four by Deuring–Shafarevich. Correctly count three rational points over infinity and one per rational pole; independent exhaustive finite-field arithmetic at F_{3^n}, n=1..4 reproduces N_n=(6,12,42,132). Newton identities and genus-four Weil functional equation uniquely give L_X=1+2T+3T²+8T³+25T⁴+24T⁵+27T⁶+54T⁷+81T⁸=(1+T+T²+3T³+9T⁴)². The genus-two curve v²=u⁵+u⁴+u²+1 is smooth by the explicit polynomial Bézout identity; independent counts (5,11) over F3,F9 plus genus-two functional equation determine L_C=1+T+T²+3T³+9T⁴. Tate's isogeny theorem gives unpolarized J(X)∼J(C)² over F3. Frobenius quartic t⁴+t³+t²+3t+9 modulo 2 is Φ5 irreducible, showing F3 simplicity; middle coefficient prime to 3 gives ordinarity. #JX(F3)=L_X(1)=225. No explicit isogeny morphism/polarization claimed.

## originality

PASS

Best-of-knowledge mathematical noncoverage after statement-and-implication comparisons. Resultary query by exact rational function and square isogeny yielded unrelated genus-two curves and Jacobian models, not a matching zeta table; focused web equation/polynomial searches also found no exact match, not evidence of historical impossibility. No negative search establishes absolute novelty.

## value

PASS

An explicit ordinary genus-four Artin–Schreier example with only cyclic geometric automorphisms has a surprisingly repeated simple genus-two Frobenius factor. Determining its complete zeta function and an explicit genus-two Jacobian realizing the square isogeny gives all extension point counts and the entire F3 isogeny class, a natural exact arithmetic invariant not recoverable from genus, p-rank or automorphism group alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
