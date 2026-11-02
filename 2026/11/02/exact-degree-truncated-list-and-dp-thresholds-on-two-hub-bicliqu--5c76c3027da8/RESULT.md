# Exact degree-truncated list and DP thresholds on two-hub bicliques

## Finding

Let \(G_n=K_{2,n}\), where \(n\ge3\). Write \(\operatorname{ch}_{\mathrm{tr}}(G_n)\) for the least positive integer \(k\) such that every list assignment with at least \(\min\{k,d(v)\}\) colors at each vertex admits a proper coloring. Write \(\chi_{\mathrm{tr}}^{\mathrm{DP}}(G_n)\) for its analogous degree-truncated DP-correspondence choice number. Then
\[
\boxed{\operatorname{ch}_{\mathrm{tr}}(K_{2,n})=\lfloor\sqrt n\rfloor+1,\qquad
\chi_{\mathrm{tr}}^{\mathrm{DP}}(K_{2,n})=\lfloor\sqrt{2n}\rfloor+1.}
\]
Equivalently, for every integer \(k\ge2\), with \(h=\min\{k,n\}\), ordinary degree-truncated \(k\)-choosability holds precisely when \(n<h^2\), whereas the DP version holds precisely when \(2n<h^2\). In particular, their ratio tends to \(\sqrt 2\), and their difference grows without bound as \(n\to\infty\).

## Assumptions and scope

All graphs are finite and simple. The bipartition of \(K_{2,n}\) comprises hubs \(u,v\) of degree \(n\), and \(n\) independent common neighbors \(w_1,\ldots,w_n\) of degree two. For an ordinary list assignment, colors are names shared between vertices and equality on an edge is forbidden. A DP-cover assigns a disjoint fiber of permissible choices to each vertex and a (possibly partial) matching of forbidden pairs to each original edge. A DP-coloring selects one fiber element per vertex without selecting a matched forbidden pair. The degree-truncated condition requires at least \(\min\{k,d(x)\}\) choices in the fiber at vertex \(x\). It suffices to study assignments with exactly the prescribed fiber sizes, since deleting surplus choices cannot create a coloring absent from the original instance.

Both formulas are restricted to \(n\ge3\). This range is needed for the positive finite DP threshold; \(K_{2,2}\) is a cycle and has no finite degree-truncated DP threshold, whereas its ordinary threshold is two. The tree \(K_{2,1}\) also has no finite degree-truncated threshold of either kind.

## Proof

Fix \(n\ge3\) and \(k\ge2\), and set \(h=\min\{k,n\}\). The hubs have \(h\) permissible choices each; every common neighbor has two. The hub colors are independent because the hubs are nonadjacent.

**Ordinary lists, upper bound.** If the hub lists meet, select the same shared color at both hubs. Every common neighbor then has at most one forbidden color and can be colored. Otherwise the two \(h\)-element hub lists are disjoint. A two-element list at one common neighbor can exclude at most one ordered pair of hub colors: only a list containing one color from each hub list can exclude a pair, and that pair is uniquely determined. Thus fewer than \(h^2\) common neighbors cannot exclude all \(h^2\) pairs, and the assignment is colorable.

**Ordinary lists, sharp obstruction.** With \(n\ge h^2\), give the hubs disjoint lists \(\{a_1,\ldots,a_h\}\) and \(\{b_1,\ldots,b_h\}\). For each ordered pair \((i,j)\), give one common neighbor the list \(\{a_i,b_j\}\); give extra common neighbors arbitrary two-element lists. Every hub-color pair leaves one neighbor with no available color. Therefore ordinary truncated \(k\)-choosability holds if and only if \(n<h^2\).

**DP upper bound.** Consider a common neighbor with fiber \(\{z_0,z_1\}\). Let \(U_i\) be the hub-\(u\) color matched to \(z_i\), if one exists; likewise define \(V_i\) at hub \(v\). The matching property ensures \(U_0\ne U_1\) whenever both exist, and similarly \(V_0\ne V_1\). A hub choice \((a,b)\) fails to extend across this neighbor exactly when each of \(z_0,z_1\) is matched to either \(a\) or \(b\). If both leaf choices are blocked, the two blockers must come from different hubs; hence the only possibilities are \((U_0,V_1)\) and \((U_1,V_0)\), where both relevant elements exist. Thus one degree-two common neighbor forbids at most two hub choice pairs, and if it forbids two, the pairs use distinct choices at each hub. If \(2n<h^2\), at least one of the \(h^2\) hub pairs survives every neighbor, after which all neighbors are colored independently.

**DP sharp obstruction.** We first partition the \(h^2\) pairs in \([h]\times[h]\) into \(\lceil h^2/2\rceil\) blocks, each either a singleton or two pairs with disjoint coordinates. Write the pairs, in this order, by concatenating the \(h\) perfect matchings
\[
M_r=\bigl((i,(i+r)\bmod h):0\le i<h\bigr),\quad 0\le r<h.
\]
Pair successive terms of the concatenated sequence. Within any \(M_r\), two successive terms have distinct coordinates. Crossing between \(M_r\) and \(M_{r+1}\) is possible only for odd \(h\), hence \(h\ge3\); there the last and first column coordinates are \(r-1\) and \(r+1\) modulo \(h\), which differ. Hence every two-pair block is coordinate-disjoint.

Fix a two-pair block \(\{(a,b),(c,d)\}\). At its assigned common neighbor, use two fiber colors \(z_0,z_1\); match \(z_0\) to hub-\(u\) choice \(a\) and hub-\(v\) choice \(d\), and match \(z_1\) to hub-\(u\) choice \(c\) and hub-\(v\) choice \(b\). These are legitimate matchings on the two incident edges. Both leaf colors are blocked exactly when the hub pair is \((a,b)\) or \((c,d)\). For a singleton \(\{(a,b)\}\), match \(z_0\) only to choice \(a\) at \(u\) and \(z_1\) only to choice \(b\) at \(v\). That neighbor excludes exactly \((a,b)\). Place one such cover gadget at each of the \(\lceil h^2/2\rceil\) common neighbors; give remaining neighbors empty edge matchings. Every hub pair is excluded somewhere, so no DP-coloring exists whenever \(n\ge\lceil h^2/2\rceil\), equivalently \(2n\ge h^2\).

For \(k=1\), assigning the same unique permissible color to each vertex (or its DP analogue) gives an obstruction. Combining both threshold criteria and noting that \(h=n\) satisfies \(n<n^2\) and \(2n<n^2\) for \(n\ge3\), the least admissible integers are exactly \(\lfloor\sqrt n\rfloor+1\) and \(\lfloor\sqrt{2n}\rfloor+1\). This proves the theorem.

For \(n=2\), the graph is a four-cycle, which is list-two-choosable but has a noncolorable degree-two DP-cover obtained by twisting one edge matching around the cycle. As all degrees are two, raising \(k\) does not change those DP-fiber sizes. For \(n=1\), the two degree-one vertices may receive different forced colors, with the central degree-two vertex having exactly those two colors, preventing any ordinary list-coloring (and hence some DP-cover coloring) for every \(k\).

## Verification

The accompanying standalone standard-library Python script `verify.py` independently enumerates every pair of partial matchings incident to a two-choice common neighbor for hub fiber sizes two through seven; in every case it confirms that at most two hub pairs are excluded and that two excluded pairs have distinct row and column coordinates. It constructs and checks the explicit block-cover obstruction for each size. A separate exact subset dynamic program independently finds the minimum number of coordinate-disjoint blocks needed to cover the hub-choice grid for sizes two, three, and four. Finally, it checks both closed threshold formulas against the inequality criteria for all \(3\le n\le500\). Run `python verify.py`; the final output is `VERIFY_OK`. These computations test finite instances and are not substituted for the infinite proof above.

## Relationship to prior work

Zhou, Zhu, and Zhu (arXiv:2507.10453, first posted July 14, 2025) introduce the degree-truncated coloring framework in the present context and explicitly construct the ordinary-list obstruction on \(K_{2,k^2}\). That previously known obstruction is a premise here, **not** a novelty claim. Their inspected 12-page preprint proves general planar/minor-closed results rather than the present exact two-hub choice thresholds. Lo, Wang, Zhou, and Zhu (arXiv:2312.15962) prove DP bounds for \(K_{2,4}\)-minor-free graphs; \(K_{2,n}\) with \(n\ge4\) lies outside their forbidden-minor class, and their result does not imply these equalities. A later study of degree-truncated DP coloring of \(\{K_4,K_{2,t}\}\)-minor-free graphs (arXiv:2610.36586, posted October 27, 2026) gives class-wide square-root estimates but does not state the exact graph-specific threshold or its comparison with ordinary truncated lists. Kaul, Mudrock, Psyhogios, Sharma, Siutkin, and Upadhyay (arXiv:2609.33966, first posted September 27, 2026) treat ordinary **uniform-fold** DP coloring on complete bipartite graphs and related Cartesian products. Their uniform two-fold threshold \(\mu(2)=2\) concerns the four-cycle boundary; for the present variable \(h\), the two hubs have \(h\) choices but every common neighbor remains constrained to two choices. Their reported uniform-fold covering-family theorems do not give this asymmetric threshold. The mathematical distinction in the new result is the sharp two-pair obstruction contributed by one degree-two DP fiber, rather than one forbidden pair in the ordinary-list model.

## Limitations

The theorem concerns degree-truncated list/DP coloring of the specific two-hub complete bipartite graph; it does not imply analogous formulas for general \(K_{m,n}\) with \(m\ge3\), arbitrary two-terminal networks, or other coloring invariants. The literature comparison is a best-knowledge assessment, not a guarantee of historical priority. An equivalent result under alternate terminology may exist. No independent mathematical audit has been performed.

## References

1. Huan Zhou, Jialu Zhu, and Xuding Zhu, *Degree-truncated choosability of graphs*, arXiv:2507.10453 (first posted 2025-07-14), https://arxiv.org/abs/2507.10453.
2. On-Hei Solomon Lo, Cheng Wang, Huan Zhou, and Xuding Zhu, *Truncated degree DP-colourability of \(K_{2,4}\)-minor free graphs*, arXiv:2312.15962 (first posted 2023-12-26), https://arxiv.org/abs/2312.15962.
3. Hemanshu Kaul, Jeffrey A. Mudrock, Emily A. Psyhogios, Gunjan Sharma, Illia Siutkin, and Aparna Upadhyay, *Covering Families for DP-Coloring of Cartesian Products with Complete Bipartite Graphs*, arXiv:2609.33966 (first posted 2026-09-27), https://arxiv.org/abs/2609.33966.
4. Huan Zhou, *Degree-truncated DP-colouring of \(\{K_4,K_{2,t}\}\)-minor-free graphs*, arXiv:2610.36586 (first posted 2026-10-27), https://arxiv.org/abs/2610.36586.
