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

The exact closed-neighborhood system over F2 is c_(j-1)+Bc_j+c_(j+1)=0, B=I+A(P6). Its characteristic polynomial is (x^3+x+1)^2; the Fibonacci-polynomial recurrence has f9(B)=0 and coprime residues for f1 through f8, hence exactly the n+1 divisible by 9 kernels are six-dimensional. T^9=diag(B^7,B^7) and boundary reflections replicate eight-column weights q times when n+1=9q. The complete independently checked 64-first-column table gives coefficients 1,4,12,12,3,12,15,4,1 at weights 0,18,20,22,24,26,28,30,36. New independent GF2 elimination reconstructed the whole kernels for n=1..27, including n=8,17,26. The finite table is exhaustively 64 cases; all-n statement follows from symbolic recurrence, not finite extrapolation.

## originality

PASS

Qualified best-of-knowledge originality after claim-level comparisons with actual literature; no identified decisive prior theorem entailed the precise asserted value-bearing formula. Full-text limitations and possible indirect dominance are explicitly recorded.

## value

PASS

The six-row grid is a canonical resonant Lights Out/closed-neighborhood code family: the exact Hamming enumerator and minimum silent-press weight 18q are natural coding/parity invariants not determined by the previously known nullity or existence periodicity. Full spectra determine probabilities under independent biased button selection and quantify pattern sparsity; this is more than a routine restatement of the recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
