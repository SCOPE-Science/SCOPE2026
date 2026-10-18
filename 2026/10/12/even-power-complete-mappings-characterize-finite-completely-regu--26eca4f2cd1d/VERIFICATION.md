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

For finite nonempty S and permutation alpha with theta(x)=x(alpha(x))^k also bijective, k>=2, F=theta circ alpha^{-1} permutes S and F(y)<=_L y^k<=_L y^2<=_L y. Around each finite F cycle principal left ideals cannot strictly decrease, so y L y^2; writing y=u y^2 implies y=u^{N-1}y^N for every N. Pick N>=2 with e=y^N idempotent; y=u^{N-1}e so ye=y, and y commutes with e hence ey=y. Since e commutes with y and y^N=e, y^{N-1} is the inverse of y in local monoid eSe. Thus S union of groups. Conversely for even k choose a positive a by CRT avoiding a=0 and 1+ka=0 modulo each prime of subgroup exponent E: at p=2 even k leaves 1 available; odd p leaves >=1 of p residues. Then x->x^a and x->x^{1+ka} permute all maximal subgroups and S. Odd-k C2 fails, and k=1 not asserted. Independent enumeration of all 122 labeled semigroup tables on 1,2,3 elements (1+8+113) found no disagreements for even k=2,4; general theorem is the principal-ideal and CRT argument.

## originality

PASS

Araújo–Bentz–Cameron–Hendrey–Kinyon 2026 Definition 15.1 formulates higher-k complete mappings and Problem 15.8 asks their existence classification. Their Theorem 2.1 obtains regularity for ordinary k=1 complete mappings, and Sections 11,13 address different stronger original-factor maps. Those do not settle necessity of complete regularity for k>=2 nor even-k converse on all finite semigroups. Existing published SCOPE semantic matches concern unrelated semigroup dynamics rather than this result. Equivalent older generalized orthomorphism terminology remains a possible unknown; qualified best-of-knowledge PASS.

## value

PASS

Answers a natural substantial subproblem of a published all-finite-semigroup existence question with sharp structural characterization, a uniform CRT power-map witness and a parity obstruction. Includes non-groups and no monoid/commutativity hypothesis; not merely k=1 renaming or small examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
