# The sharp fixed-order maximum of bounded morphisms from rooted trees to the Boolean diamond

## Finding and scope

Let \(T\) be a finite nonempty rooted tree, ordered by reflexive ancestry, and \(B_2=\{0,a,b,1\}\) the Boolean diamond with \(0<a,b<1\) and \(a,b\) incomparable. Count all functions \(f:T\to B_2\) with \(f(\uparrow v)=\uparrow f(v)\) at each vertex \(v\) (equivalently the forth and back conditions), **without** requiring surjectivity. The target is fixed and labelled, and functions on the fixed vertices are not taken modulo automorphisms. Let \(N(T)\) be the count. The exact maximum on \(n\) vertices is
\[
\max_{|T|=n}N(T)=\begin{cases}
1,&n=1,\\
3,&n=2,\\
2+3^{(n-1)/2},&n\ge3\ \text{odd},\\
2+5\cdot3^{(n-4)/2},&n\ge4\ \text{even}.
\end{cases}
\]
The maximizing rooted tree is unique up to root-preserving isomorphism. For odd \(n\ge3\) its root carries only two-vertex chain child subtrees. For even \(n\ge4\) it carries one three-vertex chain child subtree and \((n-4)/2\) two-vertex chain child subtrees. At \(n=1,2\) there is only one rooted tree up to isomorphism. The formulas give growth base \(\sqrt3\) per vertex, with distinct parity constants.

## Proof

**Recurrence from the companion census.** The state recurrence for the onto census in [1] implies the following all-map recursion upon specializing to the diamond and summing states. For completeness, let \(Q(S)\) count maps with a specified middle image at the root of \(S\), and \(Z(S)\) count those with root image zero. The top-root map is unique and \(N=Z+2Q+1\). For a leaf, \(Q=Z=0\) because the required images above either bottom or middle cannot be lifted, so \(N=1\). If \(S\) has child subtrees \(S_j\), a middle root allows independently the same middle image or top on each child root, and each child subtree already provides a top image. Hence \(Q(S)=\prod_j(1+Q(S_j))\). For a bottom root, any choice of child morphisms is valid if and only if both middle images occur below it; top then also occurs. Omitting either fixed middle image allows only the opposite middle image or top at each child root, and omitting both permits only the constant top maps. Thus
\[
Z(S)=\prod_j N(S_j)-2\prod_j(1+Q(S_j))+1,
\qquad N(S)=2+\prod_j N(S_j).
\]
In particular, the minimum for \(n\ge2\) is \(3\), with equality only when all root children are leaves (the center-rooted star). This is an immediate consequence of the recurrence, not part of the novelty claim.

**Partition envelope.** Let \(F(k)\) be the largest product of weights over partitions of \(k\) into parts of sizes \(1,2,3\), given weights \(1,3,5\), respectively. One can strictly improve any partition containing \(1+1\), \(1+2\), or \(1+3\), replacing these by \(2\), \(3\), or \(2+2\). Two threes can be replaced by three twos since \(25<27\). Thus the unique optimal partition at \(k\ge2\) uses all twos, with one three exactly when \(k\) is odd. This yields \(F(1)=1\), \(F(2r)=3^r\) for \(r\ge1\), and \(F(2r+3)=5\cdot3^r\) for \(r\ge0\). Concatenation gives \(F(s)F(t)\le F(s+t)\).

By the recurrence \(N(S)\le F(|S|)\) at orders \(1,2,3\), with equality at order three only for the chain rooted at an end. For order \(n\ge4\), induction on the positive sizes \(n_j\) of the child subtrees gives
\[
 N(S)\le 2+\prod_j F(n_j)\le 2+F(n-1)<F(n).
\]
The last difference \(F(n)-F(n-1)-2\) is \(4\cdot3^{r-2}-2>0\) at \(n=2r\ge4\), and \(2\cdot3^{r-1}-2>0\) at \(n=2r+1\ge5\). Therefore the optimum at \(n\ge2\) cannot exceed \(2+F(n-1)\). The optimal partition of \(n-1\) is realized by the claimed chain child subtrees (or one leaf when \(n=2\)), and each child attains its envelope bound. Equality requires each child to attain its own bound and the child sizes to attain the best partition product. Strictness excludes every child of order at least four; the uniqueness of the optimal partition and of the attaining smaller rooted chains proves uniqueness of the extremizer.

## Verification and relationship to prior work

The companion `check_tree.py` compares recurrence extrema and maximizer counts over rooted tree shapes through order ten. For each shape through order seven its separate counting procedure prunes maps failing order preservation and tests image-cone equality. It also checks witness shapes through forty vertices. Run `python3 check_tree.py`; the accompanying `check_tree.out` ends with `ALL_CHECKS_PASS`. These are finite checks; the partition-envelope argument proves the result for all orders.

The companion census [1] uses the same ancestor and target conventions and counts globally surjective maps by root states on a fan with an arbitrary number of labelled middle worlds. Summing its states at two middle worlds gives the recurrence used here, and then the fixed-order minimum is immediate. Its threshold for the smallest source admitting an onto map and its complete-tree growth result do not solve the fixed-order maximum for all maps. The distinct claim here is precisely that sharp maximum and its full extremizer classification. Bounded morphisms are standard [2]. An extremal count of connected graph subtrees [3] is a different invariant: even on a star, the count of connected subtrees containing the center is exponential in the number of leaves while the present count is constant. No extension is claimed to one-step or reversed accessibility, general finite posets or targets, or an onto-only optimization.

[1] *Exact bounded-morphism census and sharp branching threshold*, Resultary record 9537b2b1e958, [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-exact-bounded-morphism-census-and-sharp-branching-threshold-for--9537b2b1e958/RESULT.md), proof sections on state decomposition, middle state and bottom state.

[2] *Introduction to Modal Logics*, draft dated 16 September 2011, Definition 2.9, https://gki.informatik.uni-freiburg.de/teaching/ss11/ml/script.pdf.

[3] X.-M. Zhang, X.-D. Zhang, D. Gray and H. Wang, *Trees with the most subtrees—an algorithmic approach*, https://arxiv.org/abs/1210.2871.
