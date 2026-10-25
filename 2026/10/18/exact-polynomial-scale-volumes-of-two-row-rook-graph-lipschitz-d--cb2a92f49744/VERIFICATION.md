---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Read the frozen RESULT.md and checker.py. The within-layer Lipschitz constraints partition each clique potential into n unit cubes indexed by its unique minimizing vertex. Anchoring a_1=0 and retaining interlayer displacement delta is a determinant-1 coordinate change. For fixed within-layer shapes u,v, admissible delta has length 2-(max_i(u_i-v_i)-min_i(u_i-v_i)). If minimizing indices coincide, the difference array has one zero plus n-1 independent triangular U-V variables, yielding expected interval length 2J_{n-1}; if distinct it has independent -U and +U endpoints and n-2 triangular variables, yielding 2[J_{n-2}-(1-2^{-(n-1)})/(n-1)]. Sum n equal and n(n-1) unequal index pairs to derive exact formula. Laplace expansion J_m=sqrt(pi/(2m))+O(m^-3/2) proves asserted polynomial asymptotic. Independently enumerated lattice potentials and exact Ehrhart leading coefficients for n=2,3, matching V_2=16/3, V_3=49/5. The full formula is analytic, finite tests supplemental; anchored coordinate normalization essential.

## originality

PASS

Best-of-knowledge priority after direct frozen-result reconstruction, actual published Resultary semantic searches, primary-source comparisons, and explicit coverage/implication tests; novelty is not guaranteed. Exact limitations and unread or inaccessible papers are recorded.

## value

PASS

Graph K_n square K_2 is the standard two-row rook/line graph K_{2,n}; its exact high-dimensional anchored dual-ball volume with polynomial growth is a natural polar invariant in finite Lipschitz-free geometry, distinct from face counts and equilateral ball products. Exact finite rational formula and asymptotic are independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
