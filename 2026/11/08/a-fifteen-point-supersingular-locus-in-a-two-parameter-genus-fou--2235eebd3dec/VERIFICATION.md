---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For v(u²−4v)(1+u+v)≠0, the rational map w=4x²/(x²+1)² shows the degree-ten hyperelliptic defining polynomial is squarefree and genus four. Quotients under two commuting x↦−x involutions are isomorphic smooth genus-two curves with prime-to-five Jacobian-square isogeny. In characteristic five the genus-two Cartier coefficient matrix is [[A,4ab],[2,D]], A=a²+2ab+2b, D=2a+1, with P=AD−8ab. Rank is 2 when P≠0 and 1 when P=0; rank-one semilinear square vanishes iff A^5+D=0. Writing P=L(a)b+K(a), L=2−a²−2a, K=a²(2a+1), substitution gives H(a) of degree15. Its roots avoid smoothness exclusions and are simple; H=(a+1)J with irreducible degree14 factor J. Independently computed sympy GF5 gcd(H,H′)=1 and factor degrees [1,14] (both multiplicity one); RESULT.md and verify.py supply exact polynomial identities, Rabin irreducibility conditions, F5/F25 point-count checks. The genus-two p-rank/Newton cases 2/1/0 double to genus four 4/2/0 and a-number 0/2/2 by prime-to-five isogeny. Finite checks do not replace the geometric argument.

## originality

PASS

The exact 15-point locus, one Frobenius-14 orbit and complete p-rank/Newton/a-number stratification exceed the verified previous same-family findings. Prior stronger family characterization of nonordinary curve and one rational point does NOT determine all geometric supersingular points over algebraic closure, their irreducible degree-14 orbit, or full nonordinary Newton slopes. Those are genuinely additional specific claims.

## value

PASS

An exact geometric supersingularity census, all Newton strata and a-number in a structurally distinguished genus-four square-Jacobian family is a natural and useful classification beyond the previously known Hasse divisor and one rational point. The 1+14 Frobenius orbit and exclusion of superspeciality give substantive arithmetic-geometric information, with explicit finite-field certificates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
