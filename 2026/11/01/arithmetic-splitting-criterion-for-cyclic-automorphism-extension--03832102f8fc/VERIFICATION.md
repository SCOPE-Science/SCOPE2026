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

The structure matrix of the prescribed block-cyclic evolution algebra reduces by permutation layers to det=1-(-1)^m a, so the nonvanishing condition gives perfectness. Its strongly connected support graph plus the ideal closure under multiplication by basis elements forces simplicity. Perfectness makes images of pairwise zero-product basis elements support-disjoint and every automorphism monomial. Directed support graph outdegrees and internal chain lengths force its permutation to be common block rotation C_m. The diagonal kernel is d of order M=2^h-1, since all layer scalars are t_i^(2^j) and cross relations force equal t_i in the kernel. Because M is odd, inverse of 2 modulo M exists; the stated rotation lift phi(e_(i,j))=c_i^(u2^j)e_(i+1,j) obeys cross-square relations and satisfies phi^m=d^(ur), with phi commuting with d. Every element is d^v phi^s, 0<=v<M,0<=s<m, so the Smith form of the two relations gives C_g×C_(mM/g), g=gcd(m,M,r). An m-order section exists exactly when mv+ur≡0 mod M, equivalent to gcd(m,M)|r. The special odd-prime construction follows from h=ord_p(2) and r=1, with determinant nonzero. Independently exhaustively checked these arithmetic congruence equivalences for bounded m,h,r; the proof, not the finite field checker's log, covers arbitrary fields with a primitive M-th root. No group scheme assertion.

## originality

PASS

The 2019 automorphism/graph exact sequence, 2025 weighted-graph machinery, and the 2026 isolated nonsplit C9 example are genuine prior art. No inspected primary theorem computes this concrete three-parameter invariant-factor formula and criterion for splitting over the *unweighted* rotation quotient; weighted-graph semidirect statements concern a different quotient. Originality is only the parameterwise arithmetic evaluation, with possible implicit coverage risk.

## value

PASS

The splitting of automorphism-group extensions for perfect evolution algebras is a motivated open question. This connected simple, perfect weighted family yields both split and nonsplit extensions, explicit invariant factors and a sharp arithmetic boundary, with infinitely many nonsplit prime examples. This is a substantive family answer, not a claim to solve the general open problem or to rediscover the known C9 case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
