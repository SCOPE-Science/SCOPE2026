---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For every n>=2, concepts are full proper nontrivial clade indicators of rooted n-leaf hierarchies, both maximal(binary) and arbitrary(nonbinary). All-positive labeling of any shattered set forces laminarity and at most n-2 clades. The nested prefix queries P_2,...,P_{n-1} are shattered by explicit binary graftings; no extra intermediate prefix clade is created. For the online upper bound, conditioning a query A (|A|=k) positive yields exactly independent inner H_k and outer contracted H_{n-k+1} hierarchies, and all crossing queries fixed zero. The product Littlestone identity adds ranks, giving positive branch depth n-3 by strong induction, precluding root depth n-1. VC<=Ldim transfers equality to binary classes. Outgroup rooting transfers unrooted n-label split-membership to rooted (n-1)-label clades (n>=3); n=2 query domain empty. Independent concept-mask exact recursion for n=4 returned 26 hierarchies and Ldim2, consistent with the general proof.

## originality

PASS

Best-of-knowledge PASS for the exact Boolean whole-subset clade-membership VC=Littlestone formula, not the established hierarchy tree representation. Avdiukhin et al. obtain online sample-complexity/dimensions from labelled triplet comparisons, a distinct example domain and label structure, and the numerical n-2 recurrence under different concepts cannot imply this Boolean query theorem without an explicit dimension-preserving reduction. Hendriksen–Francis analyze hierarchy metrics and refinement; Chase–Freitag–Reyzin general query learning does not compute this class. Unrooted result is an exact reduction proven in the source, not an independently claimed unrelated novelty. Resultary relevant hits involve phylogenetic rank, ultrametric orbit counts and general tree-likeness instead.

## value

PASS

Whole-clade membership is an interpretable exact feature-query model for phylogenetic hierarchies. Exact equality of the static and adaptive shattering dimensions for both binary and multifurcating concepts is a natural structural classification, and unrooted outgroup transfer gives a useful separate model with n-3. It explains a linear online mistake budget despite superexponentially many binary trees, clarifies the effect of query semantics and is not just a textbook count of maximal hierarchies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
