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

The quotient elliptic double-cover equation gives H(u,v,w)=B(B²−AC) modulo 7. Independent SymPy GF7 elimination of the Rabinowitsch-saturated ideal (H1,H2,H3,tΔ−1) produced the seven monic leading monomials a³,ab,ac,b⁴,b³c⁴,bc⁵,c⁷; their standard-monomial complement has exactly 23 classes, proving the global geometric scheme length and excluding points outside F49. A separate independent 49³ field census found exactly 23 smooth common zeros; the exact 3×3 Jacobian determinant is nonzero for all 23, establishing reduced/transverse local structure and finite étaleness over F7. The four explicit group orbit sizes follow from finite group arithmetic. Prime-to-7 quotient Jacobian isogeny identifies p-divisible factors, so vanishing all three elliptic Hasse invariants is equivalent to superspecial genus-three Jacobian. Exhaustive finite-field points without the global saturation calculation would not establish completeness over algebraic closure; both were checked.

## originality

PASS

Ohashi already describes Ciani quartic smoothness, elliptic quotient isogenies, rationality of superspecial coefficients over Fp², and refers to Brock (1993) as studying their enumeration. None of those inspected results proves that this particular characteristic-seven marked Hasse intersection is a *reduced transverse scheme of degree 23*. Brock is a high-relevance plausible source with inaccessible full text; an authorized institutional retrieval attempt returned "Oxford worker unavailable or request invalid". This material risk does not, by itself, negate best-of-knowledge originality, but a complete Brock comparison could change priority.

## value

PASS

Scheme-theoretic reducedness and transversality refine an ordinary finite list of superspecial quartics; they make the Hasse divisor intersection multiplicity and geometric degree exact on a natural smooth genus-three coefficient family. Counting marked coefficient orbits rather than geometric isomorphism classes removes a frequent ambiguity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
