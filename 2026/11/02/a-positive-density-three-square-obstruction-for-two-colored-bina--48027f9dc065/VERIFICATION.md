---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The formal binary-partition product B(x)=product_j(1-x^{2^j})^-2 satisfies B(x^2)=(1-x)^2B(x) and B(x)≡1+2x+5x² (mod 8) from a coefficientwise Mahler induction. Finite polynomial T(x)=product_{j=0}^6 (sum_{a=0}^{2^{7-j}-1}x^{a2^j})² has degree 1538, and B(x)=T(x)(1-x^128)^-14 B(x^128). Decimating yields T_r(y)B(y)/(1-y)^14. A complete finite coefficient certificate checks T_r identities for all r=0..127, exactly r=36,62 give identically 112 (mod 128) for every t>=0. Independent modular polynomial construction and first 120 decimated coefficients of all 128 classes confirmed exactly these two. Legendre: 112+128t=16(8t+7) never three squares. Two progressions give lower density 1/64 without existence of total obstruction density.

## originality

PASS

Gawron–Miska–Ulas Theorem 5.4 already identifies valuation 4 on broad progressions modulo32, which implies neither odd parts modulo8 nor exact residues 112 modulo128. Sobolewski–Ulas 2023 study three-square binary partitions and their Problem7.2 explicitly asks about other color counts including two. Their automaticity statements do not supply these particular uniform congruences. Best-of-knowledge precise two-colored congruence/density contribution PASS; residual possibility of earlier computable table or general automata output.

## value

PASS

Positive-density explicit three-square nonrepresentability for the natural two-color binary partition function, addressing a recognized gap beyond special 2^k-1 color counts. Exact 128-class census is mathematically motivated by Legendre obstruction and cannot be inferred solely from valuation-4 theorems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
