# Independent scientific audit — SCOPE-20260917-7dc2104ad847

Audited at: 2026-10-01T06:12:13.318800Z

Disposition: **passed**

## Correctness — PASS

For a connected graph \(H\) of order at least three, any independent set in its central graph contains a clique \(X\) of original vertices and only subdivision vertices coming from edges of \(H-X\). Connectivity and the clique property imply that at least \(|X|\) edges of \(H\) are incident with \(X\), hence \(|X|+|E(H-X)|\le |E(H)|\); all subdivision vertices attain equality, proving \(\alpha(C(H))=|E(H)|\). Substituting this identity together with the exact order/size formulas for a central graph into the cited second-iterate formula simplifies algebraically to \(i(C^k(G))=2|E(C^{k-2}(G))|\); the \(K_2,k=3\) boundary case is checked separately.

## Originality — PASS

The cited September 2026 primary source supplies the second-iterate independent-domination formula, while targeted exact and synonymous searches did not locate a prior statement of the all-iterate collapse. The new structural ingredient is the central-graph independence identity and its iteration consequence.

### Equivalent formulations

No earlier equivalent all-\(k\) identity was located.

### Broader coverage

That result does not by itself remove dependence on \(\alpha(H)\) at all subsequent iterates; the audited lemma supplies the collapsing substitution.

### Exact database or table

The theorem is structural rather than a recomputation of known tabulated values.

### Claim versus prior implication

The final theorem is a short but nontrivial structural corollary once the new lemma is available.

## Value — PASS

The theorem gives a natural complete tail formula for an iterated graph operator and shows that all finer structure disappears after two iterations. The independence-number lemma and the resulting all-iterate collapse are useful structural facts, not an arbitrary finite slice.

## Sources inspected

- Independent domination in central graphs — https://arxiv.org/abs/2609.16357. PARTIAL_ACCESS_NOT_DECISIVE: The source is confirmed as the second-iterate independent-domination paper. The audit does not claim whole-document absence from an unread full text; residual access risk is recorded.

## Residual risks

- The full external text of the very recent source was not independently retrieved, so the exact scope of unpublished remarks beyond the quoted theorem remains a literature-access risk.
- The elementary identity \(\alpha(C(H))=|E(H)|\) may exist in older central-graph literature under different terminology.

## Limitations

- The result concerns finite simple connected graphs.
- It does not classify the minimum independent dominating sets.
- Its proof uses the cited second-iterate formula as an external theorem.
