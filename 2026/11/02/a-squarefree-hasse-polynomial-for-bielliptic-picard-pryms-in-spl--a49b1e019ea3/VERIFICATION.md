---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

The mathematical proof uses Cartier's coefficient-extraction formula, Lucas's theorem, two explicit second-order coefficient differential equations, and the prime-to-characteristic Prym–elliptic isogeny. In the proof, \(B=b^m(a^2-4b)^mQ\) leads to the same differential equation for \(Q\) as for \(H_m\); comparing leading coefficients proves the exact factorization. The same equation proves that its Hasse roots are simple away from the discriminant boundary. No reliance on exhaustive finite testing is made for the infinite-prime theorem.

The included stand-alone standard-library Python program `verify_picard_prym.py` was run successfully. It checks formal identities for the nine primes \(7,13,19,31,37,43,61,67,73\), the polynomial degree and boundary nonvanishing, and simple roots observed over each prime field. For primes \(7,13,19\) it exhaustively enumerates all smooth prime-field coefficient pairs and checks the direct rational-point count modulo \(p\) against the Cartier trace. Final check output: `PICARD_PRYM_HASSE_ALL_TESTS_PASS`.

The formal checks are exact for the listed primes but are not a proof for arbitrarily large primes. The proof of the complete geometric root count uses polynomial degree and separability over an algebraic closure, not a finite-field root census. The p-rank and a-number conclusion holds only for \(p\equiv1\pmod6\), and the isomorphism count is geometric rather than a finite-field census. Independent mathematical validation has not been performed.
