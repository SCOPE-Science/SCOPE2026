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

For p>=5 prime, N>=2, B0 BN!=0, the invariant field u=X^(p-1), v=Y/X^2 obeys u²v^p-v=Psi(u), deg Psi=(p^N-1)/(p-1). The tame group fixes infinity and (0,0) with stabilizer p-1 and the p-1 points (0,b!=0) with stabilizer 2; Riemann-Hurwitz gives quotient genus (p^N-1)/2. At infinity the degree-p u-map and d=deg(Psi)-2≡-1 mod p force pole valuations ord(u)=-p, ord(v)=-d and a unique point. Local coordinates w=1/v, u=w^((p-1)/2)z give z²-1=w Psi(w^L z), so exactly two finite poles of v with ord(u)=L, ord(v)=-1. Thus f_j=u^ceil(j/L) v^j has no finite poles. Its residue-class pole orders form the displayed Apéry set; numerical semigroup gap genus matches the curve genus, proving equality. Independently reconstructed residue-Dijkstra minimum, genus and conductor in 8 cases p=5,7,11,13 and N=2,3; computations check arithmetic, not global geometry. Type L and every RR dimension follow from the explicit Apéry poset. Assumptions exclude p=2,3 and B0 BN=0.

## originality

PASS

The proposed result gives the exact one-point semigroup H=<p,p+d,...,p+Ld> on a specific tame scalar quotient. Mendoza's generalized semigroup theorem concerns totally ramified places of constant-coefficient linearized-field extensions L(y)=h(x); the quotient equation u²v^p-v=Psi(u) has variable leading u² and is a different subfield, so neither equality nor a straightforward parameter substitution follows. Zhang–Zhao's 2026 result also treats totally ramified points of linearized fields, not this quotient as stated in its abstract. A general Apéry method establishes how to verify a candidate, not this candidate. Resultary search found only adjacent Artin–Schreier and Kummer themes, no actual same semigroup formula; this is not novelty proof. Best-of-knowledge PASS with specific full-text access risk.

## value

PASS

Complete Weierstrass semigroups and their minimal generators control one-point Riemann–Roch dimensions, pole orders and AG-code constructions; a coefficient-independent exact classification for a natural scalar-quotient curve family is a meaningful geometric invariant rather than a renamed textbook formula. The proof explicitly identifies nontrivial quotient branches, genus, conductor, and type; no extra coding performance theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
