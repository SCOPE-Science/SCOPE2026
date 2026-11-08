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

Decompose L=U+V+Z with V=Z=F_q[T]/(T^n-1). For x=a u0+b u1+w+z, im(ad_x)=(a+bT)R+span{w,Tw}. With zero pencil, rank of (w,Tw) is 0,1,2, and cyclic shift has g one-dimensional eigenspaces over F_q, even if char divides n. Nonzero unit pencil gives rank n; exactly g(q-1) nonunit linear pencils have image codim1, raised to n iff w outside ideal, counting q^{n-1} rank n-1 vectors per pencil. Multiply all counts by q^n central choices; ranks distinct when n>=4, sum q^{2n+2}. At n4 evaluate q=3^k odd/even k to get gcd 2/4, excluding any single rational polynomial. Independent direct bracket-matrix Gaussian elimination checked small finite fields/ranges, including n4 q2,3,5 and n5,6; the unbounded formula rests on cyclic-module proof.

## originality

PASS

Qualified PASS for an exact all-n cyclotomic rank enumeration and nonpolynomial 8-dimensional Lie-family specialization. Rossmann graphical groups use distinct central edge generators, unlike repeated cyclic labels; Godoy Molina–Lagos original full preprint classifies graded derivations for all-one/all-distinct bipartite edge labels, not this intermediate coloring or adjoint ranks. Older general cyclic pencil enumerators could subsume it; residual risk stated.

## value

PASS

Adjoint-rank distribution controls centralizer dimensions and related finite Lie group commuting class data. This is a natural proper n-coloring of K_{2,n} between one-label and every-edge-distinct extremes; the gcd(n,q-1) parameter exhibits a structural arithmetic failure of expected polynomiality in a complete infinite-field family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
