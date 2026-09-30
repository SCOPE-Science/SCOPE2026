# Independent Audit — Independent domination stabilizes on iterated central graphs

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned/current source tree:** `e4781fd85636f2d7f7555671ac9d76dc255dc3f3`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The inventory-snapshot and current-main directory entries match exactly by child Git blob/tree SHA, so the assigned source-tree SHA remains the current tree audited. GitHub was used read-only as evidence.

## Correctness — PASSED

PASS. The m subdivision vertices of C(G) are independent. If an independent set contains original vertices Q, those originals form a clique in G and any included subdivision vertex must correspond to an edge of G-Q, giving |S|≤|Q|+|E(G-Q)|=m-r(Q)+|Q|. Connectedness and n≥3 imply r(Q)≥|Q| in all cases, so alpha(C(G))=m. Substituting H=C(Y), with |V(H)|=r+s, |E(H)|=binom(r,2)+s and alpha(H)=s, into the source paper's closed formula for i(C^2(H)) makes its final two terms equal |E(H)|, hence i(C^k(G))=2m_{k-2} for every k≥3. The displayed recurrences and the k=3,4 closed forms expand correctly.

## Originality — PASSED

PASS, narrowly scoped. Cabrera-Martínez et al. develop independent domination for central graphs and give the C^2 formula used here. Targeted searches for independent domination of higher iterated central graphs did not locate the stabilization law. The new ingredient is small—the exact alpha(C(G)) identity followed by substitution—but it yields an all-iterate theorem not stated in the source. The audit does not treat the source C^2 formula or routine central-graph vertex/edge recurrences as original.

## Scientific value — PASSED

PASS. The collapse i(C^k(G))=2m_{k-2} shows that after three central iterations the independent domination number forgets all structure of the seed graph beyond order and size. This is a clean structural consequence covering infinitely many iterates and is stronger than a list of low-order computations, despite its short proof.

## Independent checks

- Reproved alpha(C(G))=|E(G)|, including the q=1, q=2, and q>=3 incident-edge cases.
- Reperformed the algebraic substitution into the cited C^2 independent-domination formula.
- Expanded the recurrences independently to recover the stated C^3 and C^4 formulas.
- Compared against the complete claim scope of the September 2026 central-graph source and targeted higher-iterate searches.
- Verified inventory-snapshot and current-main record entries are byte-identical by child Git blob/tree SHA.

## Limitations

- The theorem assumes finite connected simple graphs of order at least three, matching the source theorem used in the proof.
- Its originality is a concise higher-iterate corollary rather than a new independent-domination technique.
- The primary source is very recent, so unindexed parallel work cannot be excluded absolutely.

## Evidence and references

- https://arxiv.org/abs/2609.16357
- https://doi.org/10.1007/s00373-026-03028-6
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/independent-domination-iterated-central-graphs--19ed12461a84

This staged audit changes only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
