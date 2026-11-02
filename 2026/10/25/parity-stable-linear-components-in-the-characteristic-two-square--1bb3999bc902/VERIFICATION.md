---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The relation D(t^n)=n t^{n−1}D(t) makes f=D(t) unrestricted at even n but divisible by t at odd n. Writing f=a(t²)+t b(t²) or f=t²a(t²)+t b(t²), respectively, gives the same S² coordinate space. In char2, D² is again a derivation, and D²(t)=f f′, f′=b(t²), so D²=0 iff ab=b²=0 in S in either parity. Since b²=0 forces v_s(b)>=ceil(m/2), its b-valuation strata lie in closed linear subspaces L_j, none contained in another. All components have m dimensions, intersection L_j∩L_l dimension m−(l−j), consecutive additions count q^m−q^{m−1} new points, and the map on odd monomials gives rank m−min(v_s(a),v_s(b)). The acyclic rank m requires even n and unit a (hence b=0). Independent exhaustive coefficient equations in GF(2), m=1..6, gave 2,6,12,32,64,160 points and component counts 1,2,2,3,3,4. These finite checks do not substitute for symbolic all-field proof.

## originality

PASS

Premet studies regular derivations in truncated polynomial rings with characteristic p>2 and p-power truncation assumptions, not the characteristic-two square-zero restricted cone for arbitrary even and odd lengths. General p-DG and square-zero matrix theories do not incorporate the Leibniz equations ab=b²=0 here. The inspected sources and Resultary semantic results did not yield a dominating reduced-component classification or the parity-paired point counts. Best-of-knowledge priority remains uncertain for modular Witt p-nilpotent cone literature.

## value

PASS

Square-zero is intrinsic restricted nilpotence for derivations in characteristic two. The theorem classifies an infinite family of reduced derivation cones, reveals an unexpected even/odd linear isomorphism, determines their entire component intersection pattern and exact field arithmetic, and characterizes acyclic differentials. These natural invariants are not a textbook matrix-rank count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
