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

Checked both actual reduct operations: a↔b=top on equality and min otherwise, and a ~∧ b=top iff both positive, else zero. The scalar nonconstant maps fix bottom/top, have strictly increasing intermediate surviving prefix into intermediate target positions, then collapse to top, counted by sum binom(n-2,k). Two active source-coordinate restrictions violate 0↔0=top vs 0 ~∧0=bottom using cross-coordinate embeddings of bottom; ↔ decomposition establishes unique one-coordinate dependence. Bijective scalars on an equal chain are identity, giving S_r. Idempotent arrows must point to fixed-point loop roots of prefix-retractions; compatible labels count w_{m,p}, giving the stated forest/star sum and labeled exponential formula. Independently exhausted scalar maps for 2<=m,n<=4 by actual two-operation tables (counts m=n=4: 5); inspected bundled independent verify.py covering mixed product maps, idempotents and finite EGF coefficients. Finite checks support but do not substitute for universal proof.

## originality

PASS

The base EARS reducts, representation and general retractions are prior, as are counts of full-Heyting Gödel homomorphisms. The one-coordinate rigidity and weighted rooted-star idempotent EGF are specialized to a weaker binary reduct and do not follow from those sources. Resultary search returned no EARS matching product spectrum. Best-of-knowledge original with risk of unindexed categorical or semigroup generalization.

## value

PASS

Gives exact hom-set and retract-map enumerations, coordinate rigidity and automorphism classification for natural finite products in the algebraic semantics of a logical fragment. Counts are structurally weighted forests, not parameter substitution into full-Heyting homcounts; tractable complete finite-product subclass is an independently useful reference invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
