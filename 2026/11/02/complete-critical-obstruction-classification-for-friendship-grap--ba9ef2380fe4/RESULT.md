# Complete critical-obstruction classification for friendship-graph pebbling

## Finding

Let \(m\ge2\) be an integer, and let the friendship graph \(F_m=K_1\vee(mK_2)\) have a distinguished hub \(h\) and \(m\) labelled peripheral pairs \(\{a_i,b_i\}\). A pebbling move along an edge removes two pebbles from its source and deposits one at its target. A configuration is *stackable* if a sequence of moves leaves pebbles on exactly one vertex, and *clearable* if a sequence leaves exactly one pebble. The stacking and clearing numbers are the least positive integer \(t\ge2\) for which every configuration of size \(t\) has the respective property.

**Theorem (complete critical classification).** For every integer \(m\ge2\), among all labelled configurations of exactly \(4m-1\) pebbles, precisely \(2m\) are not stackable; these are also precisely the nonclearable configurations. The previously established scalar thresholds are \(\operatorname{stack}(F_m)=\operatorname{clear}(F_m)=4m\); the new assertion is **exhaustiveness of the critical obstruction orbit**, not the threshold value or the existence of one witness. For each exceptional configuration, choose one of the \(2m\) peripheral vertices, place \(2m+1\) pebbles there, zero at its paired neighbor and at the hub, and one pebble on every other peripheral vertex. Every other configuration of size \(4m-1\) is clearable.

For comparison, \(F_1=K_3\) has stacking and clearing numbers both equal to \(4\); its critical configuration classification differs: the all-one configuration is the unique nonstackable size-three configuration, whereas the three single-vertex piles of size three are also nonclearable.

## Assumptions and scope

Graphs are finite, undirected, simple, and labelled. The pebbling rule permits only adjacent transfers \(2\mapsto1\), and every move strictly decreases the total count by one. Configurations are arbitrary functions from vertices to nonnegative integers; no hypothesis restricts the initial support or assumes almost-stacked configurations. A final stack may have any positive number of pebbles, whereas clearing requires exactly one. The critical configuration count treats distinct choices of the exceptional peripheral vertex as distinct. The new exhaustive classification is unconditional for all \(m\ge2\); no hypothesis about general almost-stacked extremality is used. The scalar threshold and a representative obstruction were known before this classification.

## Proof

**1. Local harvesting and elimination.** For a configuration \(c\), set \(s=c(h)\), let \(r\) be the number of odd entries among the \(2m\) peripheral pebble counts, and put
\[
B=s+\sum_{i=1}^{m}\left(\left\lfloor\frac{c(a_i)}2\right\rfloor+\left\lfloor\frac{c(b_i)}2\right\rfloor\right).
\]
Sending \(\lfloor c(v)/2\rfloor\) pebbles from each peripheral vertex \(v\) to the hub produces \(B\) hub pebbles and leaves only zeros or ones outside. If \(T=\|c\|\), then
\[
T=2B-s+r\le2B+2m.
\]
Each peripheral pair with residual pattern \((1,0)\) or \((0,1)\) can be emptied at net cost one hub pebble: with at least two hub pebbles, send one to the occupied leaf and then send the resulting pair back. A residual \((1,1)\) can likewise be emptied at net hub cost one via \(h\to a_i\to b_i\to h\), using the legal sequence \((h,a_i,b_i)=(H,1,1)\to(H-2,2,1)\to(H-2,0,2)\to(H-1,0,0)\). Thus, if there are \(q\ge1\) nonempty residual pairs and \(B\ge q+1\), first empty \(q-1\) of them, retaining at least \(B-q+1\ge2\) at the hub. On the last triangle, either at least four pebbles remain (and the standard complete-graph clearing lemma for \(K_3\) applies), or exactly three remain in pattern \((2,1,0)\), which clears by two moves. If \(q=0\), the hub stack has size \(T\), and it clears whenever \(T\ge4\) by the same \(K_3\) lemma.

The \(K_3\) lemma itself follows by inspecting the four partitions of four into at most three parts, \((4)\), \((3,1)\), \((2,2)\), \((2,1,1)\), and then inducting: for any configuration with at least five pebbles, an applicable move can be chosen so that the smaller configuration still has at least four; repeating reaches the four-pebble base cases. This also agrees with the published equality \(\operatorname{clear}(K_3)=4\).

We need two further *free-elimination* moves. For residual counts with original parity \((2k,2\ell+1)\), \(k\ge1\), first move from the even peripheral pile to its odd mate, obtaining \((2k-2,2\ell+2)\), and then harvest all of that pair to the hub. This contributes exactly \(k+\ell\) hub pebbles, the same contribution as ordinary harvesting, but leaves neither residual leaf. Similarly, for \((2k+1,2\ell+1)\), \(k\ge1\), move first from the larger odd pile to its mate, then from the mate back to the first leaf, obtaining \((2k,2\ell)\), and harvest. This contributes \(k+\ell\) hub pebbles with no residual leaf, again exactly the ordinary-harvest contribution.

**2. Clearing every configuration of size at least \(4m\).** The inequality above gives \(B\ge m\). If \(B\ge m+1\), the hub-assisted elimination proves clearing because \(q\le m\). If \(B=m\), necessarily \(T=4m\), \(s=0\), and \(r=2m\). Every peripheral entry is odd, and the sum of their integer halves equals \(m\). Hence some pair contains an entry at least three; both entries in that pair are odd. Apply the odd-odd free elimination before harvesting elsewhere. The hub receives exactly \(m\) pebbles, but there are only \(m-1\) remaining nonempty residual pairs. Because \(m\ge2\), at least one residual pair remains, and the first paragraph now clears the entire configuration. This reconstructs the already known upper threshold and provides the mechanism needed to classify every critical configuration.

**3. Every nonexceptional configuration of size \(4m-1\) clears.** Again \(B\ge m\). The case \(B\ge m+1\) is done. Suppose \(B=m\). Then
\[
r=2m-1+s,
\]
so \(s\) is zero or one. If \(s=1\), every peripheral entry is odd and the sum of its integer halves is \(m-1\ge1\); an odd-odd free elimination exists. If \(s=0\), exactly one peripheral entry is even and the sum of all integer halves is \(m\). If this even entry is at least two, its mate is odd and even-odd free elimination applies. If this even entry is zero and any other pair contains an entry at least three, odd-odd free elimination applies. In all these cases the hub ends with \(m\) pebbles and exactly \(m-1\) nonempty residual pairs, which can be cleared as in step 1. The only remaining possibility is that the unique even peripheral entry is zero, all entries outside its own pair equal one, and its odd mate has \(2m+1\) pebbles. These are exactly the \(2m\) announced exceptional configurations.

**4. A hub-flux obstruction.** We prove more: fix a peripheral pair \(P_0\), put \(2m+1\) pebbles on one of its vertices and zero on its mate and at the hub, and put either \((1,0)\) or \((1,1)\) on each of the other \(m-1\) pairs. Such a configuration is not stackable.

For any time interval starting at this initial configuration, and any peripheral pair \(P\), write \(X_P\) for the number of peripheral-to-hub moves from that pair, \(Y_P\) for hub-to-peripheral moves, and \(Z_P\) for moves along the pair edge. If the pair starts with total \(p_P\) and currently holds \(p'_P\) pebbles, conservation gives
\[
p'_P=p_P-2X_P+Y_P-Z_P,
\qquad d_P:=X_P-2Y_P=\frac{p_P-p'_P-Z_P-3Y_P}{2}.
\]
Here \(d_P\) is its *net contribution* to the hub pebble count. All counts are nonnegative integers. Every ordinary pair initially has one or two pebbles, at most one at each vertex. If such a pair is emptied, it must have received a hub-to-pair move, so \(Y_P\ge1\), and then \(d_P\le-1\). If an ordinary pair is not empty, the same identity gives \(d_P\le0\).

The exceptional large pair starts with \(2m+1\). If it is not empty, the identity gives \(d_{P_0}\le m\). If it is empty, then \(d_{P_0}\le m-1\): to obtain the larger value \(m\), we would need \(Z_{P_0}=1\) and \(Y_{P_0}=0\). But with only one move across the pair edge, no hub-to-pair move, and the mate initially empty, the last pebble on that mate could not be removed. Thus the value \(m\) is impossible when the large pair is emptied.

Suppose a stacked configuration were reached. If it is stacked at the hub, then every pair is empty, so the hub has at most \((m-1)-(m-1)=0\) pebbles, impossible. If it is stacked on a peripheral vertex, let \(P_*\) be that vertex's pair. All other pairs must be empty. When \(P_*=P_0\), the hub has at most \(m-(m-1)=1\) pebbles at any intermediate moment when the other pairs are empty. When \(P_*\ne P_0\), the hub has at most \((m-1)-(m-2)+0=1\) pebbles whenever the other pairs are empty (the target pair contributes at most zero even if nonempty). But a final peripheral stack has an empty hub, and all the initially occupied ordinary pairs require a hub interaction to disappear. Consider the **last** move involving the hub. It must send a pebble from the hub to the final target pair: a last incoming move would leave a positive hub pebble, while sending to another pair would leave pebbles there with no subsequent way to remove the last one without another hub interaction. Every other pair is already empty before that last move, because internal moves confined to a two-vertex pair cannot remove its last pebble. The hub must therefore have at least two pebbles immediately before its last outgoing move, contradicting the bound of one. No stacked outcome is reachable.

The configurations in this paragraph have exactly \(3m+j\) pebbles, where \(j\in\{0,\ldots,m-1\}\) is the number of ordinary pairs loaded with two pebbles. Thus each size from \(3m\) through \(4m-1\) has a nonstackable configuration. The established general bound \(\operatorname{stack}(G)\ge3\alpha(G)+1\) for connected \(G\ne K_2\) gives \(\operatorname{stack}(F_m)\ge3m+1\) because \(\alpha(F_m)=m\). Combined with the explicit obstruction for every larger size below \(4m\), this excludes all smaller candidate thresholds. Consequently the previously known threshold is recovered. More importantly, at size \(4m-1\), step 3 proves **every** configuration outside the stated family clears, and step 4 proves **every** member of the family fails even to stack. Thus the critical failure set is exactly one orbit of size \(2m\), proving the new exhaustive classification.

## Verification

`verify.py` reconstructs each labelled friendship graph and uses independent, memoized reachability under the original pebbling rule, considering **every legal move**. It exhaustively checks the complete critical layer for \(m=1,2,3,4\), confirms that precisely \(2m\) exceptional configurations fail both conditions for \(m=2,3,4\), and checks every configuration on the threshold layer for \(m=1,2,3\). It also directly tests the broader obstruction patterns at sizes \(3m,\ldots,4m-1\) for \(m=2,3,4\). The verifier is a corroborating finite experiment, not a substitute for the unlimited-parameter proof.

Run with `python3 verify.py` using only the Python standard library. No data downloads, external packages, or private files are required.

## Relationship to prior work

Csernák and Soukup introduced the stacking and clearing numbers in *Stacking and clearing in graph pebbling*, arXiv:2604.22341v1, first submitted 2026-04-24. Their full original manuscript proves the general lower bound \(\operatorname{stack}(G)\ge3\alpha(G)+1\), the equality for complete graphs and certain complete multipartite graphs, and general upper bounds, but does not give the friendship-graph formula or its extremal configuration classification. A separate earlier exact analysis of this family had already obtained the scalar threshold \(4m\) and one family of nonstackable sharp witnesses. The present result is the strictly stronger **complete determination of all critical nonstackable and nonclearable configurations**, which does not follow from that threshold and one witness. In particular, a friendship graph with at least two triangles is **not** a complete multipartite graph. The general lower bound and the \(K_3\) clearing lemma are credited above.

The authors' later paper *The Almost Stacked Hypothesis: A Conjectural Analogue of Sjöstrand's Cover Pebbling Theorem*, arXiv:2610.09650v1, first posted 2026-10-07, treats extremality reductions, cycles, trees, and perfectly pebblable graphs. The available abstract does not announce a friendship-graph formula; its entire manuscript could not be inspected here, so an unrecognized implication remains a priority risk. The current theorem is unconditional and does not invoke that hypothesis.

## Limitations

The theorem concerns \(m\) triangles sharing **one vertex**. It does not determine stacking or clearing numbers of longer cycle bouquets, arbitrary block graphs, or generalized windmills with cliques larger than triangles. The novelty claim is limited to the exhaustive obstruction classification and remains provisional against unindexed or inaccessible literature; self-review is not independent mathematical certification.

## References

1. T. Csernák and L. Soukup, *Stacking and clearing in graph pebbling*, arXiv:2604.22341v1, 2026-04-24, https://arxiv.org/abs/2604.22341 . In particular Sections 2, 5, and 8.
2. T. Csernák and L. Soukup, *The Almost Stacked Hypothesis: A Conjectural Analogue of Sjöstrand's Cover Pebbling Theorem*, arXiv:2610.09650v1, 2026-10-07, https://arxiv.org/abs/2610.09650 . Abstract inspected; full text not inspected.
