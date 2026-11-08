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

Cohen R-transform on monic degree-n irreducible f, n≥2 over odd q, takes roots via θ(x)=(x+x^(-1))/2; Möbius ψ(x)=(x+1)/(x-1) conjugates θ to squaring. For a root β of exact degree n, y=ψ(β) lies in F_{q^n}*, and square/non-square preimages yield exactly two distinct n-degree irreducibles or irreducible degree 2n. In cyclic multiplicative group q^n−1=2^e o, v=v2(ord y): v=e gives J=0; 1≤v<e produces J=e−v; v=0 leads to a 1/2 geometric number of repeated odd-order branches and J=e+Z, Z>=0 geom P(Z=j)=2^(-j-1). Frobenius-exact-degree Möbius inversion of valuation-level counts w_v(d) gives integer C_v and PGF [Σ_{v≥1} C_v z^(e−v)+C_0 z^e/(2−z)]/N; exact tail C0/(N2^t) for t>=0. Mean is divisor sum Σμ(n/d)(q^d−1)(e−e_d+1)/Σμ(n/d)q^d; e_d=e for odd n gives 1, and the strictly positive exact-degree count in even n makes it <1. Original program factorized small fields, and independently the valuation counts and mean parity were confirmed via exact integers for q∈{3,5,7,9,25}, n=2..13; this does not prove all q,n. No guarantee after first successful doubling is claimed.

## originality

PASS

PASS qualified: the conjugacy to squaring, preimage factor dichotomy, valuation-tree depths and deterministic finite escape are all established by Ugolini and successors, and not independently claimed. The tested new statement is a uniform exact-degree irreducible input ensemble with independent coin choices, full Möbius-weighted probability generating function and sharp odd/even exact mean. Inspected theorems do not state this distribution; older specialized randomized algorithm analyses could already implicitly derive it.

## value

PASS

A constructive irreducible-polynomial procedure uses factorization until its first doubling. The random seed and fair factor policy define a canonical average-case model, whose exact full delay distribution and odd/even mean reveal performance beyond deterministic escape bounds. This precise arithmetic-probability statistic is independently useful, not an arbitrary tiny numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
