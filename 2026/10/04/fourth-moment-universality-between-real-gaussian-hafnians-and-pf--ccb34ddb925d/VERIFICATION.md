---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Expanding along one vertex makes the hafnian conditionally Gaussian with variance \(V=\sum_j A_j^2\), so \(M_n=3\mathbb E V^2\). The diagonal cofactor terms contribute \((2n-1)M_{n-1}\). For distinct cofactors, deleting both labeled vertices and conditioning on the remaining internal edges gives two independent Gaussian linear forms with common variance \(U\); adjoining one fresh vertex identifies \(M_{n-1}=3\mathbb E U^2\). Therefore \(M_n=(2n-1)(2n+1)M_{n-1}\), and the base \(M_1=3\) yields the formula. The second moment and symmetry follow from the same expansion. An independent Wick-expansion replay in this audit gives fourth moments 3, 45, and 1575 for \(n=1,2,3\), exactly matching the recurrence.

## originality

PASS

The accessible primary abstract of Zhao 2609.06526 explicitly advertises the exact second moment for the same real symmetric Gaussian-hafnian limit, not a fourth-moment formula. Zhao 2608.17065 concerns a different complex finite-row Gram hafnian. Dumitriu-Forrester concern the antisymmetric Gaussian/Pfaffian benchmark. Resultary searches found no published record with the real symmetric hafnian fourth moment. Full text of the exact same-model Zhao paper could not be obtained in this run: after open/arXiv full-text routes failed, the valid authorized institutional request returned `Oxford worker unavailable or request invalid`; no further retry was made. This is retained as a concrete residual risk, not treated as negative evidence.

## value

PASS

The fourth standardized moment is a natural quantitative invariant in the same Gaussian-hafnian anticoncentration program. The exact linear kurtosis law measures heavy normalized tails and the all-order first-four-moment coincidence with the Pfaffian is a structural comparison beyond the known low-order equality in law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
