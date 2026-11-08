---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Every endomorphism of the free class-two Lie algebra V⊕Λ²V has block data (A,B;0,Λ²A). For commuting idempotents the quotient A_i and center D_i=Λ²A_i have simultaneous binary weights; the exact sequence of modules for the semisimple product algebra F_q^{2^k} splits equivariantly, giving one central shear f with B_i=fA_i−D_if simultaneously, also in characteristic two. For eigenspace multiplicities n_c, center weight w_c counts unordered wedge pairs with bitwise AND c. The number of shear cosets is q^{n binom(n,2)−Σ_c n_c w_c}; GL_n-orbit counting yields T_{n,k}, the rank refinement, and signed-Stirling clique counts. Maximal families refine quotient to n lines and contain all subset projections; a centralizer of those line projections has no additional idempotents. Independent direct enumeration of all n=2 endomorphism (A,B) pairs over F_2 and F_3 gave (T_1,T_2)=(14,88) and (38,292), matching the theorem, but not a proof for arbitrary n.

## originality

PASS

The homomorphism generator-extension and shear machinery is prior; an earlier finite-field result establishes individual idempotent rank spectrum. Neither the inspected structural literature nor published Resultary records gave the exact higher-arity commuting-idempotent Lie-retraction tuple count or complete maximal-clique number. The claim is not a restatement of matrices because Λ²A forces nontrivial coupling and the shear exponent.

## value

PASS

Higher-arity simultaneous Lie-retraction counts and all maximal Boolean families are natural structural invariants of a central extension. The exterior-square bitwise-AND weights are not simply the standard GL_n matrix idempotent formula, and their exact evaluation is useful for reconstructing commutation clique structures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
