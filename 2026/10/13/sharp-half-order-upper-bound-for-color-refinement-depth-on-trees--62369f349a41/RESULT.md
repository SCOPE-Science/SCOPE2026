# Sharp half-order upper bound for color-refinement depth on trees
## Finding
Let \(T\) be a finite tree on \(n\ge2\) vertices. For ordinary color refinement from the uniform coloring,
\[
\operatorname{Stab}(T)\le \left\lfloor\frac{n-1}{2}\right\rfloor.
\]
The bound is sharp for every \(n\): the path \(P_n\) satisfies
\[
\operatorname{Stab}(P_n)=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
Consequently the exact maximum stabilization depth among all \(n\)-vertex trees is \(\lfloor(n-1)/2\rfloor\).

The key structural statement is a two-front witness lemma. If two vertices of a tree still have the same color after round \(s-1\) but receive different colors in round \(s\), then the tree has at least \(2s+1\) vertices. Thus a strict refinement in round \(s\) forces \(s\le\lfloor(n-1)/2\rfloor\).

## Assumptions and scope
All graphs are finite, simple, undirected, and initially uncolored. Round \(0\) is the uniform coloring, and
\[
C^{r+1}(v)=\left(C^r(v),\{\!\{C^r(w):w\in N(v)\}\!\}\right)
\]
up to renaming of colors. The stabilization depth \(\operatorname{Stab}(T)\) is the least \(s\) such that rounds \(s\) and \(s+1\) induce the same vertex partition.

For an oriented edge \(vw\), write \(T_{w\mid v}\) for the component containing \(w\) after deleting \(vw\), rooted at \(w\). Let \(\tau_r(R,x)\) denote the rooted isomorphism type of the depth-\(r\) truncation of a rooted tree \((R,x)\). On a tree, the round-\(r\) color of a vertex is exactly its rooted depth-\(r\) truncation type; this is the tree specialization of the universal-cover/color-refinement correspondence of Krebs and Verbitsky.

## Proof
We first prove the two-front witness lemma.

**Lemma.** If \(u\ne v\) satisfy \(C^{s-1}(u)=C^{s-1}(v)\) and \(C^s(u)\ne C^s(v)\), then \(|V(T)|\ge2s+1\).

For a rooted tree, equality of depth-\(r\) types is recursive: the depth-\(r\) type at the root is determined by the multiset of depth-\((r-1)\) types of the rooted branches obtained after deleting the incident root edges. Hence at \(u,v\), equality in round \(s-1\) means that their incident branches can be matched so that the matched rooted branches agree through depth \(s-2\), while the split in round \(s\) means that, for every such coarse matching, some matched pair differs at depth \(s-1\).

Follow the unique \(u\)-\(v\) geodesic and call at each current root the branch pointing toward the other root the *inward* branch; every other branch is *outward*. Perform the following peeling argument, initially with the pair \((u,v)\) and target depth \(s\).

If a mismatched pair of branches can be chosen outward at both roots, those two rooted branch components are vertex-disjoint. Their depth-\((t-2)\) truncations agree and their depth-\((t-1)\) truncations differ, where \(t\) is the current target depth. Therefore both branches contain a root-to-depth-\((t-2)\) path and at least one contains a root-to-depth-\((t-1)\) path. Their total number of vertices is at least
\[
(t-1)+t=2t-1.
\]
If \(j\) inward peeling steps have already occurred, the \(2j\) previously peeled geodesic vertices and the two current roots are disjoint from those branches. Since \(t=s-j\), the tree then has at least
\[
2j+2+(2t-1)=2s+1
\]
vertices.

Otherwise no outward-outward pair carries the first disagreement. Within each common depth-\((t-2)\) branch type, all outward branches on the two sides that can be paired have the same depth-\((t-1)\) type; consequently the fine-type discrepancy is forced into the two inward branches. Move both current roots one edge inward along the geodesic and lower the target depth from \(t\) to \(t-1\). The two roots just left behind are distinct and can never re-enter a later middle component, so each such step permanently contributes two vertices to the count.

This inward peeling cannot pass through the meeting point of the two fronts without exposing an outward disagreement: when the fronts become adjacent, the inward branch at either root is precisely the rooted component on the opposite side of the connecting edge, so if all corresponding outward branch types agree at the finer level then the two inward branch types agree as well. The same observation at a single middle vertex handles an odd-length geodesic. Thus either the outward case occurs earlier, giving the preceding \(2s+1\) count, or peeling reaches target depth \(t=1\). In the latter case the two current roots agree at depth \(0\) but differ at depth \(1\), so their remaining degrees differ; besides the \(2(s-1)\) already peeled vertices and the two current roots, at least one further neighbor is present. Again \(|V(T)|\ge2(s-1)+2+1=2s+1\). This proves the lemma.

Now let \(q=\operatorname{Stab}(T)\). If \(q=0\) there is nothing to prove. Otherwise round \(q\) is a strict refinement, so some pair of vertices has the same round-\((q-1)\) color and different round-\(q\) colors. The lemma yields \(n\ge2q+1\), hence
\[
q\le\left\lfloor\frac{n-1}{2}\right\rfloor.
\]

Sharpness is supplied by the path. Its two leaves split from the interior in round \(1\), and in each subsequent round the distinguished distance-from-an-end information advances one edge toward the center. The process stabilizes after exactly \(\lfloor(n-1)/2\rfloor\) rounds, a standard calculation recorded explicitly by Kiefer and McKay. Therefore the displayed upper bound is the exact extremal value over all \(n\)-vertex trees.

## Verification
The accompanying checker exhaustively enumerates all unlabeled trees on \(2\le n\le17\) vertices using NetworkX, runs color refinement from the uniform coloring, checks the upper bound on every tree, and checks that the maximum at every order equals \(\lfloor(n-1)/2\rfloor\). It returns:

`VERIFY_OK trees=81136 n=2..17 extremal_instances=113 bound_and_sharpness=PASS`

The computation is corroborative only; the all-order result follows from the witness lemma above.

## Relationship to prior work
Krebs and Verbitsky established the universal-cover interpretation of color refinement and showed that unrestricted graphs can require \((1-o(1))n\) rounds. Their framework makes rooted truncations the natural language for the proof above, but the inspected paper does not give a tree-specific half-order extremal theorem. Kiefer and McKay later proved that the unrestricted \(n-1\) upper bound is tight and explicitly recorded \(\operatorname{Stab}(P_n)=\lfloor(n-1)/2\rfloor\); their full text contains no occurrence of “tree” or “forest”, so it does not state the upper bound over all trees.

A paper by Tatsuro Ito titled *The Weisfeiler-Leman stability: the case of trees* is a plausible title-level collision, but the inspected material is about Weisfeiler-Leman stability in the algebraic/coherent-configuration sense rather than the one-dimensional iteration number considered here. Targeted searches for tree/forest iteration numbers and the exact half-order formula did not locate an equivalent result.

## Limitations
The theorem concerns ordinary one-dimensional color refinement on a single tree with uniform initial coloring. It does not classify all extremal trees, does not treat forests with multiple components, and does not give corresponding sharp bounds for higher-dimensional Weisfeiler-Leman refinement or arbitrary initial colorings. The literature audit was targeted rather than exhaustive, so an obscure tree-specific occurrence remains a residual priority risk.

## References
1. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014; LICS 2015.
2. S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, arXiv:2005.10182; ICALP 2020, DOI: 10.4230/LIPIcs.ICALP.2020.73.
3. T. Ito, *The Weisfeiler-Leman stability: the case of trees*, RIMS Kôkyûroku 2169 (2020), 120–144.
