# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/sharp-dissociation-independence-gap-bipartite-graphs--80664f4dba18`  
Assigned and audited source tree: `a4f7974cc7cbddb7b8fac70bd974b1aa726a1217`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `f5f6ccf7ba71608b65cc083a4ebb3e198275d8ad`  
Disposition: **passed**

## Correctness

**independently_supported**. The order bound and equality classification are correct. Connectedness for n>=3 forces diss(G)<=n-1, while bipartiteness gives alpha(G)>=ceil(n/2), so their difference has the claimed bound and equality forces both constituent inequalities to be tight. If a maximum dissociation set D has n-1 vertices, every component of G[D] is K1 or K2. The omitted vertex must meet every component for connectedness, and bipartiteness forbids it from meeting both endpoints of a K2, forcing exactly the subdivided-star family H(q,r). The formula alpha(H(q,r))=q+max(r,1) then yields uniquely H(m-1,1) in even order and exactly H(m,0), H(m-1,2) in odd order (with the n=3 coincidence). The dual 3-path-cover statement follows by complementation.

## Originality

**qualified_supported_elementary_extremal_refinement**. Bock-Pardey-Penso-Rautenbach study the relation between dissociation and independence, including stronger degree-sensitive inequalities for bipartite graphs, and the vertex-k-path-cover literature supplies the dual language. The checked statements do not give this fixed-order maximum of diss-alpha together with its complete parity-sensitive equality classification. Repository-wide targeted searches also found no overlapping SCOPE record. Because the numerical bound is elementary once the two tight constituent inequalities are juxtaposed, an equivalent result under 3-path-cover terminology remains a plausible residual prior-art risk.

## Scientific value

**modest_but_complete_extremal_classification**. The main quantitative inequality is elementary, but equality is rigid: all extremizers are forced to be trees and the isomorphism classes are completely determined for every order. The exact defect decomposition also separates the two independent mechanisms of non-extremality.

## Independent checks

- Reconstructed the defect decomposition from diss(G)<=n-1 and alpha(G)>=ceil(n/2).
- Checked that the omitted-vertex argument excludes every additional edge/cycle while preserving connectedness.
- Solved the even- and odd-order Diophantine constraints on q,r and verified the n=3 boundary case.
- Checked the dissociation/3-path-cover complement identity.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/sharp-dissociation-independence-gap-bipartite-graphs--80664f4dba18
- https://doi.org/10.1137/0210022
- https://doi.org/10.1016/j.dam.2013.02.024
- https://arxiv.org/abs/2202.01004
- https://arxiv.org/abs/2205.03404
## Limitations

- Finite simple connected bipartite graphs only.
- The numerical upper bound itself is a short consequence of two standard inequalities; the main content is the equality structure.
- Equivalent prior coverage under 3-path vertex-cover/deletion terminology remains the principal originality risk.
