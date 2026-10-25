# Exact stacking number of friendship graphs

## Finding

For every integer \(k\ge1\), let the friendship graph \(F_k=K_1\vee(kK_2)\) consist of \(k\) edge-disjoint triangles sharing exactly one hub. A pebbling move takes two pebbles from a vertex and places one on an adjacent vertex. A configuration is **stackable** when some finite sequence of moves leaves all remaining pebbles on one vertex. The stacking number is the least integer \(t\ge2\) for which every configuration of total size \(t\) is stackable.

**Theorem.** For all integers \(k\ge1\),
\[
\operatorname{stack}(F_k)=4k.
\]
Stronger upper-bound statement: every configuration of size \(4k\) can be transformed into one supported **at the hub**. For \(k\ge2\), a sharp nonstackable configuration of size \(4k-1\) puts \(2k+1\) pebbles at one outer vertex, zero at its mate and at the hub, and one pebble at each of the other \(2(k-1)\) outer vertices. For \(k=1\), three singleton pebbles on the triangle witness the lower bound.

## Assumptions and scope

The graph is finite, simple, connected, undirected, and has exactly \(2k+1\) vertices. Its outer vertices are paired into \(k\) triangles; vertices from different pairs are not adjacent. All pebble counts are nonnegative integers. Stacking allows one or more pebbles at the final vertex; this theorem does **not** assert an equality for the separate clearing number.

## Proof

**Upper bound.** Label the hub \(h\) and the outer pair counts \((a_i,b_i)\), for \(1\le i\le k\). From any configuration of size \(4k\), repeatedly move two pebbles from an outer vertex directly to \(h\) until each outer count is zero or one. Put
\[
P=\sum_{i=1}^k\left(\left\lfloor\frac{a_i}{2}\right\rfloor+\left\lfloor\frac{b_i}{2}\right\rfloor\right),\quad
S=\sum_{i=1}^k(a_i\bmod2+b_i\bmod2),
\]
and let \(r\) be the number of pairs with at least one odd outer count. The hub now has \(H=c(h)+P=(4k+c(h)-S)/2\) pebbles. Since \(S\le2r\),
\[
H\ge2k-r\ge r.
\]
If \(H\ge r+1\), eliminate the residual pairs one by one. A residual pair \((1,0)\) or \((0,1)\) is cleared by \(h\to a_i\to h\); each arrow denotes a legal pebbling move, with the first consuming two hub pebbles and the second returning one. A residual pair \((1,1)\) is cleared by \(h\to a_i\to b_i\to h\), where the first move creates two pebbles at \(a_i\). Each elimination reduces the hub count by one and requires at least two hub pebbles beforehand. Beginning with \(H\ge r+1\) guarantees legality throughout and leaves at least one hub pebble.

Only \(H=r\) remains. The inequalities above force \(r=k\) and \(H=k\), and equality in \(H=(4k+c(h)-S)/2\) forces \(c(h)=0\), \(S=2k\) and \(P=k>0\). Thus every outer count is initially odd and some pair has counts \((a,b)\) with \(a\ge3\), \(b\ge1\). Before the direct-to-hub preprocessing, handle this pair with the two within-pair moves \(a\to b\) and \(b\to a\). Its resulting counts are \((a-1,b-1)\), both even. Moving their halves directly to the hub clears the pair and contributes exactly \((a+b-2)/2\), the same hub contribution as the original direct-to-hub preprocessing. Process all other pairs directly as before. Now the hub count is still \(k\), but only \(k-1\) residual pairs remain, so the previous elimination works. Hence every size-\(4k\) configuration stacks at the hub.

**Lower bound.** For \(k=1\), three pebbles placed one per triangle vertex admit no move. Fix \(k\ge2\). In the claimed size-\(4k-1\) configuration call the heavily loaded pair \(B_0\), initially \((2k+1,0)\), and call the remaining pairs *light*, initially \((1,1)\). Track an arbitrary legal move sequence. For \(B_0\), let \(A\) count moves from the hub to its outer vertices, \(B\) count moves from those vertices to the hub, and \(C\) count moves between its outer vertices. Its current total outer mass is \(2k+1+A-2B-C\ge0\). Its net contribution to the hub is \(\delta_0=B-2A\). Therefore
\[
2\delta_0+3A+C\le2k+1,
\quad\text{so}\quad \delta_0\le k.
\]
Moreover \(\delta_0=k\) implies \(3A+C\le1\), hence \(A=C=0\), \(B=k\), and the heavy outer pair has exactly one pebble on its originally occupied vertex and zero on its mate.

For any light pair, let \(A_i\), \(B_i\), \(C_i\) denote the analogous counts. Its outer mass is \(2+A_i-2B_i-C_i\ge0\), so its net hub contribution \(\delta_i=B_i-2A_i\) obeys
\[
2\delta_i+3A_i+C_i\le2.
\]
Before its first incoming hub move, the pair stays \((1,1)\), cannot make any move and has \(\delta_i=0\). After at least one incoming hub move, \(A_i\ge1\) permanently, so \(\delta_i\le-1\) permanently. Call such a pair *activated*. If \(q\) light pairs have been activated, the current hub count satisfies
\[
c(h)=\delta_0+\sum_{i=1}^{k-1}\delta_i\le k-q.
\]
Any stacked terminal configuration must have activated every light pair: otherwise two separate vertices retain their original singleton pebbles. Consider the first move that activates the last of the \(k-1\) light pairs. Immediately before it, \(q=k-2\) and the hub contains at least two pebbles; the inequality above forces \(c(h)=2\) and \(\delta_0=k\). Thus the heavy pair has already been reduced to a single frozen pebble. The activating move leaves the hub empty, and now \(q=k-1\), so \(c(h)\le1\) forever. No further move can leave the hub, and that heavy singleton can never be removed.

The last-activated light pair now has counts \((2,1)\). If it is never emptied, its support coexists with the heavy singleton. If it is emptied, it must make a move from one of its vertices into the hub: internal moves alone cannot remove the final pebble from a pair. Such a move leaves at least one pebble at the hub, which can never decrease again because no move may leave the hub. This also coexists with the heavy singleton. Either way, no stacked terminal state exists. Hence the size-\(4k-1\) configuration is nonstackable.

Finally, no integer \(t\) with \(2\le t\le2k+1\) is universally stackable: choose \(t\) distinct vertices with one pebble each. If every configuration of some size \(t>2k+1\) were stackable, every configuration of size \(t+1\) would be as well, since a legal first move always exists and reduces its size by one. Iterating this monotonicity would contradict the nonstackable size-\(4k-1\) witness. This proves that the minimum universal threshold is exactly \(4k\). \(\square\)

## Verification

The accompanying `verify.py` enumerates every configuration modulo the automorphism group generated by independent swaps within the \(k\) outer pairs and arbitrary permutations of the pairs. It uses a separate memoized recursive reachability test, strictly decreasing total pebble count, both for any single-vertex stack and for the more demanding hub-only goal. For \(k=1,2,3,4\), it confirms the displayed size-\(4k-1\) witness is nonstackable and every orbit of configurations of size \(4k\) reaches the hub. Orbit counts are 9, 92, 759 and 5265, respectively. Run `python verify.py` using Python 3.9 or later; its expected summary is in `verification_output.txt`. This finite check corroborates rather than substitutes for the unrestricted proof.

## Relationship to prior work

Csernák and Soukup introduced the undirected stacking invariant and established universal bounds, an independence-number lower bound \(3\alpha(G)+1\), and exact formulas for complete graphs, complete bipartite graphs, paths and complete multipartite graphs. Those results give \(\operatorname{stack}(F_1)=4\) because \(F_1\) is a triangle. For \(k\ge2\), \(F_k\) is neither complete multipartite nor a path. Its independence number is \(k\), so the general bound yields only \(3k+1\), strictly weaker than the formula proved here. The related directed-graph paper concerns strongly connected digraphs and an exact directed-cycle formula, not the friendship graph calculation. No priority or independent validation is claimed; equivalence under another graph-pebbling terminology remains a bibliographic risk.

## Limitations

This determines the stacking number, not the clearing number, on one infinite graph family. The proof makes no assertion about other windmill block sizes or about the Almost Stacked Hypothesis in general. The finite program is an additional check only. Bibliographic priority has not been independently established.

## References

1. T. Csernák and L. Soukup, *Stacking and clearing in graph pebbling*, arXiv:2604.22341v1, submitted 2026-04-24. https://arxiv.org/abs/2604.22341 .
2. T. Csernák and L. Soukup, *Stacking and Clearing in Directed Graph Pebbling*, arXiv:2606.04659v1, submitted 2026-06-03. https://arxiv.org/abs/2606.04659 .
