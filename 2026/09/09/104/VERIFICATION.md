---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Rebuilt the exact degree-seven apolar pairing independently: the entry for monomials of exponents α, β is (α+β)! on the four support exponents of F0 and zero elsewhere. Its kernels give the annihilator, and its pivot columns give ordered monomial quotient bases. Exact rational calculations give Hilbert function (1,3,6,10,10,6,3,1), the printed second higher Hessian by direct permutation expansion, and multiplication ranks (1,3,6,10,6,3,1) at x+2y+3z. The middle determinant is −36 in the verifier's ordered bases selected in increasing x exponent then increasing y exponent, not an invariant scalar. Nullities of powers 0–9 are (0,10,20,26,32,35,38,39,40,40), giving Jordan type (8,6,6,4,4,4,2,2,2,2). The ranks of S1 I_(d−1) at d=4–8 are (0,13,25,35,45) against dimensions (5,15,25,35,45), so there are exactly five quartic and two quintic generators, also checking the degree-eight endpoint that the supplied script omits. All higher degrees follow because I_8=S_8. Apolarity gives grade-three Gorenstein, so the seven-generator Buchsbaum–Eisenbud structural consequence is applicable; it is not a displayed matrix. No universal WLP or unproved Hessian bridge is being certified.

## originality

PASS

Pass only the exact tuple for the named sparse septic in the stipulated conventions. The exact indexed hit is this record itself. Standard theory supplies methods and broad background, not the bound tuple for F0; no distinct explicit or equivalent computation was found in the inspected sources.

## value

PASS

The compressed socle-seven Hilbert function is the next standard odd cell beyond the socle-five theorem. A simple four-term Fermat-plus-tail inverse system puts the full multiplication data and a mixed seven-generator presentation in the same explicit algebra. In particular the quintic pair is compatible with full Lefschetz ranks, so generator counts alone cannot use that pair as a failure diagnostic. This is a usable test case for comparisons of multiplication and generator strata, not a paper-scale claim about all compressed algebras or mere generic existence of WLP.

The dated certificate retains the supplied scientific assessment, sources and limitations.
