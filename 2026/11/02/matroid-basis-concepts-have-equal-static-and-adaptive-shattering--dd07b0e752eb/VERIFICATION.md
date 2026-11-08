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

For any finite matroid M including loops/coloops and empty ground, a support S is VC-shattered by basis-incidence concepts iff S is independent in both M and dual M*: all-ones label requires inclusion in a basis, all-zeros a disjoint basis, and for any T subset S the spanning complement E\S and basis-extension axiom realize exactly T. Edmonds intersection yields nu=min_A(2r(A)+|E\A|-r(E)). For every e neither loop nor coloop, split the rank-minimum indexing family by e in A: nu(M\e)=min_{A not containing e}F_M(A)-1 and nu(M/e)=min_{A containing e}F_M(A)-1, so nu(M)=1+min{nu(M\e),nu(M/e)} for each legal root. The standard binary-tree Littlestone recurrence and induction prove Ldim=VCdim=nu and any nonconstant element optimal at root. I independently enumerated 340 binary-matrix matroid instances up to four columns, computed all basis concepts, exact dynamic Littlestone and VC, and checked eligible roots. Original verify.py (including seeded larger cases) was inspected; these checks are not exhaustive for nonrepresentable matroids.

## originality

PASS

The substantive claimed result was compared at the level of mathematical objects, exact implications and limitations against same-family primary results, general theorems and Resultary; accepted as best-of-knowledge, with identified prior components and explicit residual risks, not an assertion of exhaustive historical priority.

## value

PASS

Adaptive shattering can generally exceed static VC dimension, so proving equality for *every* finite matroid basis family, an explicit matroid-intersection min formula and universal optimal-root freedom is a meaningful structural result with algorithmic consequences. The statement is not a mere renaming of Edmonds: it derives an online learning dimension invariant and a strong recursion for any nonconstant basis coordinate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
