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

For every n>=5, S_n=C_n^2 has adjacency interpreted in C_n by x!=y AND (E_C(x,y) OR exists z E_C(x,z) AND E_C(z,y)); this adds at most one quantifier. Brown--Hoshino (2007), Theorem 4.9, establishes C_m equiv_5 C_n for m,n>=19, hence S_m equiv_4 S_n. The recursive exact tuple-type invariant tau_{r+1}(a)=(atomic diagram,{tau_r(a,b):b in V}) is equivalent to bounded-rank equivalence. I independently compiled and ran the supplied dihedral-reduced C++ recurrence, not just read its transcript: ranks-four empty-tuple type IDs for n=5..18 were all distinct, and n=19..24 shared ID 364. This computational finite distinction plus the analytic published infinite-tail implication prove the full family classification, 15 classes and sharp tail at 19; finite computation alone does not prove the infinite tail.

## originality

PASS

PASS on available primary texts: the 2007 undirected-cycle theorem supplies the tail after the one-quantifier interpretation, but not the n=5..18 pairwise separation of C_n squared. A powers-of-cycles biclique-colouring paper studies a different invariant. Search returned no exact previously published fifteen-class square-cycle census; duplicate specialist finite-model-theory tables remain possible.

## value

PASS

The bounded-rank elementary-equivalence partition is a natural logical invariant of a canonical four-regular family. An exact fifteen-theory classification and sharp smallest-representative cutoff distinguish finite small cycle-square graphs even though one tail class is eventually indistinguishable; not merely a renamed parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
