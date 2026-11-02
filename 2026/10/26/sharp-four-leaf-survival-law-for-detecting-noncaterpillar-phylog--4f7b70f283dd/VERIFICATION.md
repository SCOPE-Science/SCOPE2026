---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

A noncaterpillar unrooted binary tree has a vertex with three components containing >=2 leaves. Deleting a leaf can remove such a witness only if the leaf lies in a branch of exactly two leaves; for r>=7 at most two such branches can occur, giving at most four destructive deletions. If exactly four deletions are destructive, there is a unique triply internal vertex, with two cherry branches and one rooted comb branch, the F_r shape. Uniform sequential pruning from n to k has conditional survival at least (r-4)/r, telescoping to (k)_4/(n)_4; only F_n achieves equality at each step if 6<=k<n, with k=n a universal equality. An induced noncaterpillar sextet has one central vertex selecting exactly two leaves from each component, so N6=Σ_v binom(a_v,2)binom(b_v,2)binom(c_v,2). Independent generation of unlabelled binary trees through n=9 confirmed noncaterpillar counts and unique minimum sextet counts 1,3,6,10 for n=6,7,8,9. These experiments corroborate the all-n deletion argument and do not prove it alone.

## originality

PASS

Related tree inducibility optimizes rooted pattern densities and classical phylogenetic balance treats edge splits. In the inspected statements these do not establish the universal lower probability of surviving noncaterpillar taxon rarefaction, the four-destructive-leaf lemma, or a unique unrooted extremizer F_n. This is the bounded best-of-knowledge contribution.

## value

PASS

The exact survival probability addresses the natural sample-complexity of recognizing noncaterpillar topology from randomly retained taxa. The unique worst-case F_n and sharp n^4 effort requirement make the structural four-leaf deletion fact useful for rarefaction design rather than an arbitrary count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
