# A counting formula for maximum shattered comparison supports of linear extensions

## Finding

Let \(P=(V,<_{P})\) be a nonempty finite labeled strict poset of height \(h\), and let the concepts be all linear extensions of \(P\), queried on unordered pairs of distinct vertices. Maximum VC-shattered supports admit a canonical ordered partition: their connected components are the fibers of a **unique** strict order-preserving surjection \(f:V\to[h]\). Conversely, every such surjection and every choice of a spanning tree on each fiber gives one maximum support, with no duplication across distinct surjections. Consequently the number of maximum supports is
\[
N(P)=\sum_{\substack{f:V\twoheadrightarrow[h]\\ x<_{P}y\Rightarrow f(x)<f(y)}}\prod_{i=1}^{h}\tau(|f^{-1}(i)|),\qquad
\tau(t)=\begin{cases}1,&t=1,\\t^{t-2},&t\ge2.\end{cases}
\]
The sum uses all strict surjections to \([h]\), not just the map assigning to each element the length of a longest chain ending there. This replaces a count over forests subject to quotient-acyclicity tests by a count over ordered antichain layers with explicit multiplicative weights. For instance, if \(P\) consists of \(a<b<c\) and a fourth element \(x\) incomparable to the chain, the three maximum supports are the single queries \(ax,bx,cx\), corresponding to the three possible layers of \(x\).

## Assumptions and scope

The domain contains every unordered pair of distinct elements with a fixed reference orientation for interpreting its Boolean answer. Shattering means realizing every simultaneous assignment on the support by some linear extension. Height counts vertices in a chain. A one-vertex tree is allowed, and a chain has one maximum support (the empty set). The formula counts labeled supports, not linear extensions or orientations of trees.

## Proof

Use the forest-contraction criterion [1]: a support is shattered exactly if it forms a forest on \(V\) and the comparison digraph on its components is acyclic, with a loop for any comparable pair in the same component. To recall the criterion, an undirected support cycle can be oriented cyclically. In a forest, a quotient cycle of comparisons lifts to a directed cycle by orienting the unique connecting paths in the components on the cycle. In the other direction, an arbitrary query orientation cannot produce a directed cycle entirely within a tree; any cycle using comparison arcs would project to a directed closed walk in the quotient. Hence every orientation admits a linear extension.

Fix a longest chain \(x_1<_{P}\cdots<_{P}x_h\). Its elements must occupy distinct components of any shattered support. Thus the support has at most \(|V|-h\) edges. The bound is attained by trees on the levels of the longest-chain-ending rank map, since each comparison strictly increases rank. These two facts also follow from [1].

For a maximum support the \(h\) chain elements use *all* its components. The quotient contains a directed path through those components in the order of the chain. Every topological ordering of the quotient must respect that path, so its component order is unique and independent of the choice of longest chain. Assign the integer \(i\) to the entire component of \(x_i\); this gives the asserted strict surjection. Each component is its fiber's spanning tree. Conversely, if trees are chosen on the fibers of any strict surjection to \([h]\), every quotient arc increases the fiber index, so the support is shattered and has \(|V|-h\) edges. Recovering the surjection from the support makes this correspondence a bijection. Counting the independent labeled tree choices by Cayley's formula [2] yields the sum.

## Verification and limitations

The accompanying `verify_linear_extensions_vc.py` and `verification_output.txt` provide finite corroboration through five labeled vertices, including the maximum-support count. Run `python3 verify_linear_extensions_vc.py 5` in the directory containing that script. The finite enumeration does not prove the theorem; the argument above applies to arbitrary finite nonempty posets. The rank-map sum is an exact enumeration identity, not a polynomial-time algorithm for general input posets.

## Relationship to other results

The forest-contraction criterion and the dimension \(|V|-h\) are shared with [1] and are used here as background, not claimed as distinct contributions. In particular, the rank-layer construction in [1] produces maximizers, while the uniqueness argument here accounts for all maximizers and yields the weighted count. The ranking complexes in [3, §10] give the same pair-query model geometrically; the counting identity concerns the extremal shattered coordinate supports, not the number of chambers.

## References

1. [*Comparison shattering for linear extensions of finite posets*](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-comparison-shattering-for-linear-extensions-of-finite-posets--aed8bda32d56), Resultary record, Finding and proof Steps 4–6.
2. A. Cayley, *A theorem on trees*, Quarterly Journal of Mathematics 23 (1889), 376–378.
3. H.-J. Bandelt, V. Chepoi and K. Knauer, *COMs: Complexes of Oriented Matroids*, [arXiv:1507.06111](https://arxiv.org/abs/1507.06111), §10.
