# Independent Audit — 2026/09/20/minimum-order-consecutive-distributed-degree-sets--e18549b65fe7

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `9924c99eccf274cdb132a2344ca242bf5ff574ea`
- Disposition: **PASSED**

## Correctness

**PASS** — The minimum-order formula is correct. If |X|=x and |Y|=y, realizing D_Y=[b] gives e>=S_b+(y-b), while realizing D_X=[a] gives e<=ax-a(a-1)/2. The resulting lower bound on x+y is strictly increasing in y and is minimized at y=b, yielding N(a,b)=a+b+ceil((S_b-S_a)/a). For sharpness, the proposed column partition C=(b,b-1,...,1) is self-conjugate and decomposes as P union L, while the row partition R=Q union L has the same total with P majorizing Q; adjoining the common L preserves majorization, so C majorizes R and Gale--Ryser gives a simple bipartite realization. Independent Gale--Ryser checks for every 1<=a<30 and a<=b<60 found no exception. The connected-realization switching lemma is valid: if e>=n-1, a minimum-component realization cannot have every component a tree, and a 2-switch using a cycle edge merges two components while preserving degrees and simplicity. The displayed inequality e>=n-1 holds for the sharp sequences when a>=2. The a=1 obstruction is immediate.

## Originality

**PASS** — Manoussakis--Patil 2014 determine minimum orders for distributed bipartite degree sets only when the two prescribed sets have the same cardinality. Iványi--Pirzada--Dar 2015 give constructions for arbitrary prescribed distributed degree sets but do not solve the minimum-order problem. The audited theorem resolves the unequal-cardinality consecutive family [a],[b] exactly and adds the connected-realization boundary. Searches for the displayed formula and consecutive distributed-degree-set terminology found no equivalent result.

## Scientific value

**PASS** — The theorem settles a natural structured portion of the unequal-cardinality minimum-order problem left outside the 2014 exact theory, with an explicit closed formula, a transparent Gale--Ryser construction, and an exact connectedness exception. It is a meaningful extremal graph-theory result even though it does not solve arbitrary unequal sets.

## Sources

- **On degree sets and the minimum orders in bipartite graphs** — Y. Manoussakis; H. P. Patil. https://doi.org/10.7151/dmgt.1742 — Prior minimum-order theory for pairs of distributed degree sets of the same cardinality.
- **Tripartite graphs with given degree set** — Antal Iványi; Shariefuddin Pirzada; Feroz Ahmad Dar. https://doi.org/10.1515/ausi-2015-0013 — Provides algorithms realizing arbitrary prescribed global and distributed degree sets in bipartite/tripartite graphs, without the audited exact minimum-order formula.
- **Bipartite Graphs and their Degree Sets** — Yannis Manoussakis; H. P. Patil. https://doi.org/10.1016/S1571-0653(04)00554-2 — Earlier equal-cardinality distributed degree-set existence/minimum connected-order work.

## Limitations

- The theorem treats only consecutive positive sets [a] and [b], not arbitrary unequal-cardinality distributed degree sets.
- The equal-cardinality specialization is prior territory and is not part of the novelty claim.
- Equivalent results under alternate terminology such as partite degree sets remain a residual search risk.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "gale_ryser_construction_checked_a_lt_30_b_lt_60": true,
  "connected_switching_lemma_checked": true,
  "prior_same_cardinality_scope_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access and preprint sources were checked first; no decisive comparison remained inaccessible, so Oxford Download was not required.
