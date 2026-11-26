---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A separated unordered pair at distance d gains (1-p)p^(d-1) after its path edge is upgraded. Doubling and dividing by n gives the stated increment for uniform starting patch, with no gain for diagonal pairs. PC and ECA are monotone transforms here. I generated all shapes by leaf extension from the singleton, not by replaying the packaged Prüfer verifier: deleting a leaf shows inductive exhaustiveness, and minimizing sorted rooted codes over all roots identifies exactly the unrooted isomorphism classes. I rebuilt the polynomials from unique endpoint paths. The counts for n=2..8 are 1,1,2,3,6,11,23. After deleting strictly coefficientwise dominated vectors there is one two-vector frontier at n=7, with difference p(1-p), and four at n=8, with differences up to sign p(2-p), p(1-p²), p(2p-1), and p(p²+p-1). The first two never change sign in the open interval; the other two are the stated witnesses and each crosses once. All noncandidate edges in the witnesses have a coefficientwise dominating candidate with at least one strict coefficient; the equal vectors identify the stated tied edges. This is a continuum certificate, not a probability grid.

## originality

PASS

The contribution supported here is the sharp and complete all-p bond-upgrade classification through eight tree vertices, not the objective, a fixed-p optimization algorithm, or the established ranking equivalence to edge removal. The closest inspected claims do not supply the classification.

## value

PASS

The first obstruction to parameter-independent edge intervention is a natural extremal invariant. The complete frontier classification rules out smaller obstructions and explains both eight-vertex switch mechanisms and ties, rather than reporting selected evaluations or arbitrary small counts. Its use is as a tree reliability benchmark, not ecological field guidance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
