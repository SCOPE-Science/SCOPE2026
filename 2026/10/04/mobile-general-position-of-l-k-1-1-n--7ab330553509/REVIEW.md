# Review

## Correctness

**PASS.** The final claim is reconstructed directly from definitions. The line graph \(L(K_{1,1,n})\) has one universal vertex \(x\), two \(n\)-cliques \(A,B\), and exactly the perfect-matching edges \(a_i b_i\) between them, giving \(K_1\vee(K_n\square K_2)\). Because the graph has diameter two, general-position sets are exactly those whose induced components are cliques; the proof of this fact is included rather than assumed. This yields \(\operatorname{gp}=n+1\). Every \((n+1)\)-set is then shown immobile, including all maximum triangles at \(n=2\), while the explicit configuration \(\{x,b_1,\ldots,b_{n-1}\}\) has reversible legal excursions that visit every omitted vertex. No computation is needed for the infinite statement.

## Originality

**PASS with residual bibliographic risk.** The earliest anchor source, arXiv:2209.12631v1, determines mobile general position for \(L(K_m)\) and explicitly proposes investigating arbitrary line graphs; it does not treat \(L(K_{1,1,n})\). The later product/join paper arXiv:2505.00535v1 determines \(\operatorname{Mob}_{\mathrm{gp}}(K_n\square K_2)=n\) and gives bounds for \(G\vee K_1\), but those statements do not imply the exact value for \(K_1\vee(K_n\square K_2)\). Exact-name, complete-tripartite, universal-vertex-prism, and equivalent join-form searches produced no statement covering the theorem. Nearby indexed results concern different invariants such as connected mutual visibility or other general-position variants.

Residual risk remains because no finite search can exclude all unpublished, uncatalogued, or differently phrased equivalent results.

## Value

**PASS.** The theorem gives a natural infinite family directly within an open direction posed in the foundational mobile-general-position paper: line graphs beyond complete graphs. It also isolates a transparent interaction between two operations already central in the literature: the base prism \(K_n\square K_2\) has mobile value \(n\), and adjoining one universal vertex preserves that mobile value while increasing the static general-position number to \(n+1\). The proof is elementary, exact for every \(n\ge2\), and exposes the obstruction—maximum configurations are frozen—rather than merely supplying a numerical formula.

## Closest literature and limitations

The closest primary sources are arXiv:2209.12631v1 / DOI 10.1017/S0004972723000102 and arXiv:2505.00535v1 / DOI 10.1016/j.dam.2025.10.041. The result does not extend here to \(L(K_{r,s,t})\) in general or to arbitrary line graphs.

Same-model review: passed. Independent audit: not yet performed.
