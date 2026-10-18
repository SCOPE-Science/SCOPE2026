---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Evenness in X gives a nontrivial involution. Setting Y=X²+T²+1 on Z=1 yields quotient function field Y²=−T(T+1)(T+2). Translation s=T+1 yields s−s³, genus one with distinct cubic roots and j=1728. The projective fixed locus contains plane X=0 plus [1:0:0], but p is not on the quartic; fixed-plane section has polynomial T^4+T^3+5T²+2T+1 with discriminant 4257≠0 and hence four distinct points, consistent with RH genus 3→1. For any PGL transformation fixing p, matrix block upper triangular; X³ terms force shear b=c=0 and X² and constant coefficients reduce to q(Nv)=q(v) and r(Nv)=r(v). An independently recomputed exact Gröbner basis is {u−s,v,w,s²−1}, proving N=±I and marked stabilizer exactly C2. Independent patch Jacobian ideals establish smoothness over C. This does NOT assert full unmarked automorphism group.

## originality

PASS

The full Bannai–Tokunaga–Yorisaki source supplies this exact quartic, four concurrent bitangents and related ambient elliptic surface; its inspected Example 6.1 does not identify the plane-quartic quotient E or j=1728 or exact marked PGL stabilizer. Bielliptic-quartic general theory permits involutions but does not compute this marked example from its equation.

## value

PASS

The four concurrent bitangents give a geometrically distinguished nonarbitrary mark in an extremal family. The explicit CM quotient and exact marked symmetry group reveal the arithmetic/geometric structure behind that extremal presentation, beyond merely recounting its bitangents. Exact stabilizer proof is the substantive additional invariant, not the mere observation that an even polynomial is invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
