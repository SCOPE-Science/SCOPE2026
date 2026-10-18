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

For the Leibniz bracket [e2,e1]=[e2,e2]=e1, direct evaluation of all four ordered Nijenhuis equations for N=[[a,b],[c,d]] gives c^2=0, c(a-b-d)=0 and a^2-ab-2ad+bc+bd+d^2=0. Over any field this is equivalent to c=0 and (a-d)(a-b-d)=0, including characteristic two. An automorphism must preserve the derived line, and bracket preservation forces Phi_t=[[t,t-1],[0,1]], t nonzero. Direct conjugation gives u=b+d-a -> t u while a,d are invariant. One plane u=0 consists of singleton orbits Q_(a,d); the other a=d has one nonzero b orbit J_a per scalar, no overlap with Q. Thus over Fq the union of two affine planes contains 2q^2-q operators and q^2+q orbits. Independent polynomial torsion reconstruction and direct exhaustive field checks F2,F3,F5 verify operator sets of sizes 6,15,45; the universal proof is symbolic, not inferred from finite enumeration.

## originality

PASS

Mondal–Saha’s exact Example 2.10 solves the operator equations for this same non-Lie Leibniz algebra but never forms its automorphism quotient or counts finite-field orbits. The new invariant u and the complete orbit stabilizers are a further theorem. Li–Ma–Wang and Ma–Sun–Zheng study compatible triangular Leibniz bialgebra data, a stronger additional structure rather than all arbitrary Nijenhuis operators modulo algebra automorphisms. Ma–Sun–Zheng was only abstract-accessible; after public preprint/OA searches an authorized institutional request returned vpn_disconnected. No conclusion about its whole classification table is drawn from that abstract, which remains an overlap risk, but no positive covering theorem was found.

## value

PASS

Complete orbit decomposition of the named motivating example, valid over all fields and giving exact finite-field class counts, is a natural isomorphism invariant of Nijenhuis Leibniz pairs. It distinguishes the fixed plane from nontrivial Jordan classes and moves beyond solving raw torsion equations; the small dimension does not make a natural complete classification worthless.

The dated certificate retains the supplied scientific assessment, sources and limitations.
