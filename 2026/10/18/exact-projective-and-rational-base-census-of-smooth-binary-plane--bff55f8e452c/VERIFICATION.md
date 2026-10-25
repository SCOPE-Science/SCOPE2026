---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Smoothness is equivalent to surjectivity of the degree-10 map S_6+S_7^3->S_10 from F and its three partials: if the projective ideal has no zero, three generic quartics in it form a regular sequence with socle degree 9, so degree10 spans all 66 monomials; conversely surjectivity precludes a projective zero. Independently reimplemented all 32767 GF(2) quartic ranks, counted 10920 smooth forms, then all 17,390,184 unordered smooth pairs whose XOR is smooth, /3=5,796,728 pencils. Independent counts for rational base-set size 0..7 exactly [1883160,2388848,1171800,302904,45640,4200,168,8]. Independently enumerated GL3(F2), calculated representative fixed-pencil counts for element orders 1,2,3,4,7 as [5796728,0,98,0,7] and the full order-21 normalizer fixed count 1; Burnside produces 34539 orbits and orbit-size distribution as claimed. Full C++ original and Walsh program inspected; independent code, not saved logs, supplied the primary cross-check. The result classifies coefficient pencils over F2, not abstract curve isomorphism classes.

## originality

PASS

Earlier Asgarli/Ghioca and colleagues develop existence of smooth pencils, and Nart/Ritzenthaler classify individual genus-three curves. The assessed result counts all two-dimensional coefficient subspaces, projective coordinate orbits, and rational-point incidence histograms. Neither general existence nor classification of individual members automatically yields the pencil orbit census.

## value

PASS

An all-equation pencil count over the smallest finite field, geometric smoothness condition, complete projective symmetry orbit census and eight-cell rational base-point distribution form a natural finite algebraic-geometric classification. Exact all-object exhaustivity and two independent construction methods make this a substantive finite invariant, not a small arbitrary example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
