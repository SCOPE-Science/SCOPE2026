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

For the unaugmented entry-equation scheme X^m=0, first-order expansion gives D_m(A)(B)=sum_{j=0}^{m-1}A^jBA^(m-1-j). On an ordered pair of Jordan blocks b,c<=m, identify rectangular matrices with k[u,v]/(u^b,v^c). Multiplication by h_m=sum u^j v^(m-1-j) satisfies (u-v)h_m=0, and the nonzero homogeneous multiples are exactly degrees through b+c-m-1; they are linearly independent in every characteristic, so rank is max(0,b+c-m). Summing proves formula, dual-number fiber q^(n^2-R_m), and GL_n orbit size gives full labeled matrix census. Dominance of partition (m^a,r) and centralizer formula give reduced dense orbit dimension n^2-(ma^2+2ar+r); rank computation yields tangent excess min(r,m-r), vanishing precisely when m divides n; regular local generic reducedness follows from equal tangent and Krull dimensions. Fresh modular row elimination verified ordered-pair ranks p=2,3,5 through m=6 and dense excess n<=11,m<=9. Finite checks corroborate the characteristic-free symbolic argument.

## originality

PASS

Prasad–Singla–Spallone Section 6.2 gives the same linearized map L_N on Jordan blocks and addresses similarity classifications, but the inspected sections do not furnish the stated uniform block-rank plus all-partition labeled dual-number matrix count and generic reducedness boundary. Weyman Theorems 1–2 concern the radical orbit-closure ideal with characteristic-polynomial generators imposed, unlike this unaugmented scheme. Earlier square-zero ring enumeration and one-block nilpotency-index tables cover special cases explicitly excluded from novelty. Algebraic simplification of Prasad et al could implicitly yield the rank formula: meaningful priority risk.

## value

PASS

The distinction between set-theoretic nilpotent variety and the nonreduced entry-equation scheme is substantive deformation geometry. Exact all-characteristic tangent rank, sharp generically-reduced divisibility and full finite dual-number labeled census are useful natural structural invariants of schemes of matrix power equations, not arbitrary small computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
