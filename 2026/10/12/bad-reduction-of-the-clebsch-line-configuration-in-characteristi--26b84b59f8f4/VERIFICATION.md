---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For the Clebsch diagonal cubic H=sum xi=F=sum xi^3=0 over algebraic closure F5, singularity equations force all xi^2 equal; sign choices have zero sum mod 5 only when all signs agree, giving unique p=[1:1:1:1:1]. In local affine coordinates the quadratic term 3(a^2+b^2+c^2+(a+b+c)^2) has symmetric matrix with determinant 4 in F5, so p is A1. The one-nodal cubic-surface line theorem yields 21 geometric lines, 6 through node and 15 away. An independent enumeration of all 806 two-spaces of F5^4 satisfying the restricted cubic found 21 F5-lines with exactly 6 through p; hence this is the entire geometric set, not a finite sample standing for closure. The 15 classical diagonal lines survive. Reduction phi=(1+sqrt5)/2 ->3 at the ramified prime turns 12 displayed smooth golden-ratio double-six equations into 6 distinct lines, each twice; independent Gaussian elimination verified precisely the six node lines. Enumerating all 120 coordinate permutations gives S5 orbits 15 and 6, stabilizers of orders 8 and 20, respectively D8 Sylow2 and normalizer C5⋊C4 of Sylow5. This is the reduced geometric line set, not the nonreduced Fano scheme.

## originality

PASS

Dolgachev–Duncan and Busé–Nonkané establish singularity/bad discriminant of the Clebsch model at characteristic five. Huybrechts gives the smooth Clebsch orbit split (15 diagonal and 12 golden-ratio double-six) and line equations. Dolgachev–van Geemen–Kondō Section 2.14 establishes that an arbitrary one-nodal cubic has 21 lines, 6 through node as pairwise limits and 15 others. These are credited; their general facts do not state which of the two Clebsch S5 orbits folds in the arithmetic specialization nor classify stabilizers of the actual reduced bad fiber. The new exact phi->3 specialization, identification with Sylow normalizers and exhaustive finite-field action supply additional model-specific math. Older classical Clebsch surface degeneration literature is a genuine priority risk.

## value

PASS

Characteristic five is the exceptional prime for the integral Clebsch cubic, and its two famous smooth S5-orbits of 15+12 lines degenerate to 15+6 in an arithmetically constrained way. Identifying explicitly which orbit folds and the resulting Sylow symmetry is a motivated structural invariant of this natural bad fiber, not merely the known 21-line nodal total.

The dated certificate retains the supplied scientific assessment, sources and limitations.
