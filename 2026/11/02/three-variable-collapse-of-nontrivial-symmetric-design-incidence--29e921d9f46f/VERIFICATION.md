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

For finite symmetric 2-(v,k,lambda) designs with distinct blocks and 2<=k<=v-2, square point-block incidence N has NN^t=(k-lambda)I+lambda J and N1=N^t1=k1; invertibility since 0<lambda<k yields N^tN=(k-lambda)I+lambda J. For any two pebbled elements (including equal and cross-sort pairs), the occurrence of every desired equality/sort/incidence pattern for a third is parameter independent: two distinct points or blocks have lambda common, k-lambda one-sided, and v-2k+lambda=(v-k)(v-k-1)/(v-1)>0 neither incidences; point-block pairs have k-1,v-k or k,v-k-1 choices, all positive. Thus Duplicator preserves atomic relations under any three-pebble move for arbitrary rounds, proving common FO^3 theory without counting, including unary sorts; pure adjacency follows by reduct. Fano lambda1 incidence graph is C4-free, whereas complementary symmetric (7,4,2) design has 4-cycles, yielding a four-variable separating sentence. Independent exact Fano pair-intersection and four-cycle computations confirm boundary; unrestricted logic theorem follows from pair extension identities, not finite examples.

## originality

PASS

The bounded-variable back-and-forth theorem and symmetric-design pair intersection identities are standard ingredients; the asserted universal equivalence of *all* nontrivial symmetric designs in FO^3 at unbounded quantifier rank, plus a sharp 4-variable separation for Fano/complement, was not stated by inspected Grohe–Otto or design literature. The result is an application of robust 2-pebble extension spectra, but it classifies a natural infinite heterogeneous class; generic extension axioms alone do not explicitly furnish the design-specific parameter positivity.

## value

PASS

The inability of three-variable logic, despite arbitrary quantifier depth, to distinguish *any* nontrivial symmetric design is a strong uniform expressivity collapse that covers infinite families with differing block numbers and intersection parameters. The four-variable Fano/complement boundary demonstrates sharpness. This is a natural finite-model-theoretic structural theorem with relevance to design-incidence indistinguishability, not a tiny computational observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
