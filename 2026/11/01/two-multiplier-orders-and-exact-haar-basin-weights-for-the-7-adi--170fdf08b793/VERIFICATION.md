---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For f(x)=x^2+1 on Z_7, the two fixed roots are alpha≡3, beta≡5 (mod7), alpha≡31, beta≡19 (mod49); multipliers 2alpha and 2beta have residue orders e=2 and 6, with lambda_alpha^2≡22, lambda_beta^6≡15 mod49. Their return-map quadratic coefficients vanish modulo 7 and linear displacement has valuation m+1 for points in depth-m shells. Odd-prime cycle lifting then yields lengths e*7^j and corresponding minimal odometers; three alpha sign-orbit components and one beta six-orbit shell at each m. Residue precursor branches are two for alpha and four for beta; critical residue zero enters B1 with measure 1/7, giving alpha basin 4/7^{m+1}, beta B1=31/49, Bm(m>=2)=24/7^{m+1}. Totals 2/7 and 5/7. Independent modular branch and cycle counts checked mod 7^2,7^3,7^4, supporting but not replacing all-depth proof.

## originality

PASS

Best-of-knowledge originality resides in this polynomial/prime-specific complete shell and PRE-iteration Haar basin census, not in general minimal decompositions or p-adic cycle-growing. Fan–Liao arXiv:1010.5583 proves a broad qualitative decomposition and extensively treats Z_2 quadratics, without the present explicit Z_7 f=x^2+1 counts in the inspected material. Related squaring-map work concerns f=x^2, not x^2+1; an unindexed identical worked example remains possible.

## value

PASS

Complete minimal-component and pre-iteration Haar basin census on the natural quadratic x²+1 over the first small prime showing both neutral fixed points with distinct multiplier orders. The critical branch produces a 31/49 first-shell weight rather than the generic 24/49, a nontrivial measure-theoretic distinction absent from qualitative cycle-lifting theorems. Exact odometer types and basin totals are useful dynamical invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
