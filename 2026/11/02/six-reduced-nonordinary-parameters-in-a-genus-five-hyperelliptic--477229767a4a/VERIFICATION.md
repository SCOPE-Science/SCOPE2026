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

For y²=(x⁴−1)(x⁸+t x⁴+1), t≠±2 over char13, the coefficients of F(z)^6, F(z)=(z−1)(z²+tz+1), give sparse Hasse–Witt matrix whose prime-field basis diagonalizes all Frobenius twists. Eigenvalue factors involve P=(t−6)(t²+3t+6) with multiplicity two and Q=(t+6)(t²+5t−4) with multiplicity two. The coprime squarefree cubics have six roots, two F13-rational, all F169-rational. Their zeros force stable p-rank3, a-number2; other smooth t give p-rank5,a0; determinant 8(t+2)^12 P²Q² has double zeros at all six exceptional smooth parameters. Recomputed F(z)^6 by exact polynomial convolution and independently verified coefficient identities and 5x5 determinant factorization modulo13; independently evaluated rational zero sets P:{6}, Q:{7}. These identities hold over algebraic closure via polynomial algebra, not just a finite cutoff.

## originality

PASS

Best-of-knowledge qualified PASS: Ohashi--Kudo arXiv:2603.21569 section 4.2 studies an isomorphic marked genus-five family with degree-power-two isogeny to elliptic factors; Proposition 4.6 and Corollary 4.7 do not in inspected text state the char13 p-rank3 roots P,Q. Bouchet et al. arXiv:2506.06457 concern broader hyperelliptic p-rank moduli and sampling, not an identified exact determinant for this pencil. Classical Yui Hasse–Witt coefficient matrix formula provides an essential known computation tool, not the particular factorized six-root divisor. Exact claimed additions have not been shown covered by the inspected published results; residual priority risks remain explicit.

## value

PASS

A fully explicit nonordinary divisor, multiplicities and paired p-rank jump in a natural genus-five one-parameter hyperelliptic family; it refines a previously known isogeny/superspecial framework by exact geometric parameter equations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
