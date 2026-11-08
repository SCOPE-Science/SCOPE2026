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

For u,v>=1 the torus fixes monomial ambient ideals containing (x^u y^v), in bijection with partitions λ with λ_(v+1)<=u. Euler localization reduces each invariant constructible µ stratum to this finite torus-fixed combinatorics at each colength. Ambient minimal generator count is 1+number of distinct positive row lengths; in the quotient exactly one generator disappears iff λ_v>u and λ_(v+1)=u. Splitting k parts >u gives B_u(q,z) and q-binomial upper factor T_(u,k); the corner correction yields the exact two-variable formula. For any finite-colength ideal, not merely monomial ideals, x+y is a nonzerodivisor and length(R/(x+y))=u+v, so from exact sequence length(I/(x+y)I)=u+v and µ(I)<=u+v. Three disjoint maximal-corner classes telescope to q^choose(u+v,2)/(P_u P_v). Independent direct Young diagram enumeration checks top-generator coefficients for all u,v=1..3 through colength16; notably (2,2) coefficients at n6,7,8 are 1,2,5. Infinite claims follow combinatorial and exact-sequence proofs.

## originality

PASS

Luan 2026 directly studies Hilbert schemes of fat nodes and some Poincaré data; Huang–Jiang–Oblomkov 2026-10-26 supplies a more general all-u,v unrefined motivic zeta function and contact-length refinements, so the z=1 specialization here is covered prior art. Their published abstract describes contact length along branch, not µ=dim I/mI. Hsiao–Szenes compute generator-number strata for punctual ideals of the smooth plane, not quotient-ring generators of fat nodes; the missing one-corner correction is essential. No observed source establishes the generator-refined fat-node Euler series and top-generator product; the inaccessible full Huang–Jiang–Oblomkov article is a substantive possible implicit coverage risk, not erased.

## value

PASS

Minimal number of ideal generators is a canonical measure of presentation complexity of punctual subschemes. A complete generator-graded Euler series, uniform nonmonomial generator ceiling, and sharp extremal stratum for every fat-node pair are natural geometry refinements of the already-known unrefined motivic series; the one-corner quotient correction has substantive mathematical content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
