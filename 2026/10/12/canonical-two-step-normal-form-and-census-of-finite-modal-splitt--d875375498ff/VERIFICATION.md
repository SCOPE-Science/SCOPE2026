---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Finite normal modal algebras on powerset of n Boolean atoms correspond uniquely to relations R with Box_R(A)={x:R[x]⊆A}. Box_R^3(0)=1 iff no directed walk of three edges, which forces acyclicity. Congruence ideals P(U) stable under Diamond_R correspond precisely to predecessor-closed U. In any finite DAG, nonempty predecessor-closed sets contain a source; the least nonzero such ideal exists iff there is a unique source. A single source reaches all vertices. For n≥2, classify nonroot vertices into B reachable by one step but never a two-step path and C endpoints of two-step paths: r connects to every b∈B; each c∈C has an arbitrary nonempty B-parent subset plus independent optional r shortcut, and C is terminal; converse has no three-walk and unique source. Canonical partition is intrinsic. Choose r, B size k≥1, and independent parents/shortcut per other vertex to obtain labeled count L_n=n∑C(n−1,k)[2(2^k−1)]^(n−1−k). For isomorphism, S_k acts on T_k=(nonempty subsets[k])×{shortcut bit}; unlabeled C vertices are multisets of T_k and Burnside coefficient ∏cycles(1−t^length)^(-1), giving stated U_n. Independently enumerated all binary relations for n=1,2,3,4, evaluated all predecessor-closed ideals and isomorphism orbits, obtaining (L,U)=(1,1),(2,1),(15,3),(124,8). Separately implemented multiset Burnside cycle computation for all n=1..8 and reproduced L=(1,2,15,124,1525,26106,618695,20279288), U=(1,1,3,8,24,77,283,1182). These checks support the formulas; the general proof is structural.

## originality

PASS

The rootedness criterion for finite subdirectly irreducible modal complex algebras is already known, as are Jankov splitting templates and general DAG-count machinery. The precise no-three-walk, two-step parent-set/shortcut canonical normal form and full labeled/isomorphism enumeration for this natural height-restricted SI class are the claim to priority.

## value

PASS

The first nonstar finite-height layer of subdirectly irreducible modal algebras supplies natural bounded Jankov splitting templates. Canonical parent-set/shortcut parameters and complete labeled and unlabeled enumerators give directly usable finite model/type libraries rather than isolated tiny examples, with separate independent exhaustive low-atom validation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
