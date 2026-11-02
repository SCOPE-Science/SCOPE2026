---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof is self-contained and depends only on the elementary endpoint observation for classically \(123\)-avoiding permutations and the explicit construction. The endpoint observation, interior avoidance argument, cyclic jump bounds, and saturation rigidity were checked algebraically, including \(m=1\), \(n=3\), the transition \(n=m+2\), and the transition \(n=2m+2\).

The file `verify_cyclic_jump.py`, included alongside this text, was run with Python 3 and completed with the exact terminal marker `VERIFY_OK sharp bandwidth, constructive witnesses, and rigid boundary`. It checked all \(2418\) supplied construction parameter pairs, exhaustive classical pattern-avoidance minimization for \(3\le n\le9\), and complete boundary-case enumeration for \(m=2,3,4\), giving \(1,4,35\) labelled admissible permutations, respectively. Finite computations corroborate, but do not replace, the infinite proof. The boundary enumeration counts are checks only, not part of the mathematical claim.

Prior-work searches covered the original linear-adjacency paper, cyclic-order avoidance, cyclic consecutive avoidance, searchable indexed mathematical claims, and a relevant sequence database. The original paper's reverse-diagonal theorem already implies the *necessary* upper length bound; it does not establish the all-parameter constructive sufficiency and rigidity reported here. Comprehensive historical-priority verification and independent validation have not occurred.
