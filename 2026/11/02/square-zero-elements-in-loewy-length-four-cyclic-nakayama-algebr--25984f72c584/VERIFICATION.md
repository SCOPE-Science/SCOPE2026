---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

All square-zero elements have no length-zero path coefficients because k^n has no nonzero square-zero elements. Direct path concatenation yields a_i a_{i+1}=0 and a_i b_{i+1}+b_i a_{i+2}=0; length-three coefficients are free. For independent occupied support S the bipartite matrix incidence components are stars (a degree-two row cannot be adjacent to a degree-two column without consecutive occupied sites), hence rank exactly 2|S|-t_2(S)-t_3(S) regardless of field characteristic or nonzero scalars. Counting gives (q-1)^|S| q^(2n-rank). The five-state cyclic triple transfer matrix encodes precisely distance-two/three support interactions; its determinant 1-t-qwt^2+(q-1)wt^4, w=(q-1)/q^2, and Cayley-Hamilton give D_n=q^2 D_(n-1)+q^3(q-1)D_(n-2)-q^6(q-1)^2D_(n-4). Initial values are obtained from explicit small cycles, not extrapolated. Fresh support enumeration and transfer calculations checked q=2,3,4,5 and n=3..10. Tests are finite, not the all-q proof.

## originality

PASS

The exact finite-field square-zero-locus cardinality and distance-interaction transfer recurrence were not obtained from the inspected categorical/bimodule references or Resultary search. This is a best-of-knowledge judgment; a general arithmetic quiver-variety counting formula could imply it.

## value

PASS

Uniformly oriented truncated cycle algebras are a canonical family; counting actual nilpotent elements (rather than isoclasses) at every field size with one exact recurrence gives a structural arithmetic invariant. The support-incidence rank formula is independently useful for similar path-length decompositions, not a cosmetic restatement of categorical invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
