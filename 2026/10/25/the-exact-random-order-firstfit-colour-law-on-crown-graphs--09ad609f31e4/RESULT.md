# The exact random-order FirstFit colour law on crown graphs

## Finding
Let \(n\ge2\), and let \(G_n=K_{n,n}-M_n\) be the labelled crown graph with parts \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and edges \(a_i b_j\) exactly when \(i\ne j\). Expose its \(2n\) vertices in a uniformly random order and colour each arriving vertex with the smallest positive colour not used by an earlier neighbour (FirstFit). Let \(X_n\) be the final number of colours.

For \(n\ge2\), put \(T_{n,2}=1\) and \(T_{n,n+1}=0\). For each integer \(3\le k\le n\), define
\[
T_{n,k}=\frac{n!}{(n-k+2)!}\frac{3^{k-3}(2n-2k+6)!}{(n-k+3)^2(2n)!}.
\]
Then the complete distribution is
\[
\Pr(X_n\ge k)=T_{n,k}\quad(2\le k\le n+1),\qquad
\Pr(X_n=k)=T_{n,k}-T_{n,k+1}\quad(2\le k\le n).
\]
In particular, for \(n\ge3\),
\[
\Pr(X_n=2)=1-\frac1n,\qquad
\Pr(X_n\ge4)=\frac3{(2n-2)(2n-1)}\quad(n\ge4).
\]
The exact mean is \(\mathbb E X_n=2+\sum_{k=3}^{n}T_{n,k}\), and hence
\[
\mathbb E X_n=2+\frac1n+\frac3{(2n-2)(2n-1)}+O(n^{-3})
=2+\frac1n+\frac{3}{4n^2}+O(n^{-3}).
\]
For \(n\ge3\), the number of vertex orders that attain the worst possible \(n\) colours is exactly
\[
40\,n!\,3^{n-3}.
\]
For \(n=2\), every order uses exactly two colours.

## Assumptions and scope
All vertices are distinct and each of the \((2n)!\) orders has probability \(1/(2n)!\). Colour names are the positive integers and are always assigned greedily with no recolouring. The graph is the complete bipartite graph with one fixed perfect matching of edges removed, and the result concerns the number of colours used, not the joint distribution of vertex-colour assignments. We assume \(n\ge2\); in the edgeless two-vertex case \(n=1\), FirstFit uses one colour.

## Proof
**1. The first colour is either a deleted matching pair or a complete side class.** Suppose the first vertex is \(a_i\) (the other case is symmetric). If \(b_i\) arrives before every other vertex of \(A\), then \(a_i,b_i\) both receive colour one, and no other vertex receives colour one. Indeed, each other \(b_j\) appears after \(a_i\), and each other \(a_j\) appears after \(b_i\); their earlier neighbours block colour one. Moreover, all remaining vertices already see colour one at their arrival, so deleting \(a_i,b_i\) from the arrival order and decrementing subsequent colour names recovers exactly FirstFit on a crown graph of order \(2(n-1)\). If a second \(A\)-vertex arrives first, then it also gets colour one. Thereafter every vertex of \(A\) gets colour one, while every vertex of \(B\) gets colour two (possibly some \(B\)-vertices were already given colour two). Thus in this case exactly two colours are used. The same dichotomy applies recursively after each paired colour class, whenever at least two deleted matching pairs remain.

**2. A partial order characterizes high colour counts.** Fix an integer \(t\) with \(1\le t\le n-2\). By step 1, \(X_n\ge t+2\) if and only if the first \(t\) complete colour classes consist of respective matched nonedges \(\{a_{i_1},b_{i_1}\},\ldots,\{a_{i_t},b_{i_t}\}\). The order of these \(t\) distinct indices is uniquely determined by the colouring. Rename them \(1,\ldots,t\), and label all remaining indices arbitrarily as \(t+1,\ldots,n\). The first \(t\) classes are exactly these pairs in this order if and only if, for every \(1\le i\le t\) and \(i<j\le n\),
\[
a_i\text{ arrives before }b_j,\qquad b_i\text{ arrives before }a_j.
\]
Necessity follows because the vertex in pair \(j\) must already see colour \(i\) on an opposite-side neighbour when it arrives; sufficiency follows inductively because the designated pair \(i\) sees every earlier colour but never sees its own mate. The remaining \(n-t\ge2\) matched index-pairs form a smaller crown graph, so they necessarily use at least two additional colours. The displayed precedence constraints define a poset \(P_{n,t}\) on all \(2n\) vertices.

**3. Count the linear extensions.** Write \(L_{n,t}\) for the number of total orders respecting \(P_{n,t}\). For \(t=1\), the two disjoint size-\(n\) sets \(\{a_1,b_2,\ldots,b_n\}\) and \(\{b_1,a_2,\ldots,a_n\}\) each have a specified element required to be first within their set. A uniform total order satisfies these independent relative-order requirements with probability \(1/n^2\), whence
\[
L_{n,1}=\frac{(2n)!}{n^2}.
\]
For \(2\le t\le n-2\), an extension must start with either \(a_1\) or \(b_1\). If it starts with \(a_1\), its second vertex is either \(b_1\) or \(b_2\). The prefix \((a_1,b_1)\) leaves any extension of \(P_{n-1,t-1}\). The prefix \((a_1,b_2)\) forces \(b_1\) next; it leaves an extension of \(P_{n-1,t-1}\) whose first vertex is \(b_2\). By interchange symmetry of the two bipartition classes, exactly half of all extensions of this smaller poset begin with \(b_2\). There are symmetric cases beginning with \(b_1\), yielding
\[
L_{n,t}=3L_{n-1,t-1}.
\]
Put \(s=n-t+1\). Iteration to the base case gives
\[
L_{n,t}=3^{t-1}\frac{(2s)!}{s^2}.
\]
There are exactly \(n!/(n-t)!\) ordered selections of \(t\) matching indices; their corresponding poset order sets are disjoint by uniqueness of the initial coloured pairs. Dividing their total number \(\frac{n!}{(n-t)!}L_{n,t}\) by \((2n)!\) gives the asserted \(T_{n,t+2}\), and differences of the tails give the mass function.

**4. Consequences and boundaries.** For \(n\ge3\), setting \(t=1\) gives \(T_{n,3}=1/n\); for \(n\ge4\), setting \(t=2\) gives \(T_{n,4}=3/((2n-2)(2n-1))\). For \(n\ge3\), setting \(t=n-2\) gives \(L_{n,n-2}=80\cdot3^{n-3}\), so the number of worst-colour orders is \((n!/2)\cdot80\cdot3^{n-3}\). The maximum number of colours is at most \(n\), since each vertex has degree \(n-1\), and the last formula shows this bound is attained. The tail-sum identity proves the exact mean. If \(s=n-t+1\), consecutive high-colour tails have ratio
\[
\frac{T_{n,t+3}}{T_{n,t+2}}=\frac{3s}{2(s-1)(2s-1)}\quad(1\le t\le n-3).
\]
For \(s\ge4\) this ratio is at most \(2/7\); in particular the combined contribution of all \(k\ge5\) to the mean is \(O(n^{-3})\). This proves both asymptotic expressions. The case \(n=2\) follows directly from the two disjoint edges.

## Verification
A self-contained C++17 program, `verify.cpp`, was compiled and run from the actual package. It checks the formula against all arrival orders for \(n=2,3,4,5\) (a total of \(3{,}669{,}864\) orders). Independently, it counts topological orderings of each finite poset \(P_{n,t}\) by subset dynamic programming for all \(3\le n\le9\), \(1\le t\le n-2\) (28 distinct parameter cases), and checks the derived linear-extension formula. Its output is:

`VERIFY_OK exhaustive_crown_orders=3669864 poset_cases=28 maximal_order_count_n5=43200`

For example, the exact probabilities for \(n=4\) are \((3/4,5/28,1/14)\) at colour counts \((2,3,4)\); the exact mean \(65/28\) is consistent with earlier published random-order simulations. Exhaustive verification is finite evidence only; the proof above establishes the claims for all integers \(n\ge2\).

## Relationship to prior work
Kordecki and Łyczkowska-Hanćkowiak (2016, arXiv:1601.00252, Section 4, Table 1) reported simulations of the unbuffered random-order greedy algorithm on crown graphs, but their analytic colour-distribution formulas in Section 3 concern a different buffered algorithm with a prescribed alternating arrival order. Ye, Xu, Wang, Zheng, and Li (2026, arXiv:2608.29603, Section 3.1, Theorem 3) proved the weaker bound \(\mathbb E X_n\le2.5+O(1/n)\) for a uniform random order. Li and Li (2026, arXiv:2610.15468, Introduction, Section 1.2) cite that estimate while studying other bipartite inputs. Neither inspected source states the exact distribution, its factor-three poset recursion, the sharp optimum probability, or the count of worst-case orders. The formulas here do not purport to solve arbitrary bipartite-graph random-arrival problems.

## Limitations
All probabilities are with respect to uniformly random permutations of the labelled vertices and ordinary irrevocable FirstFit colouring; they do not apply automatically to buffered algorithms, other graph families, nonuniform arrival models, or weighted arrivals. The asymptotics hold as \(n\to\infty\). A historical-priority risk remains for unlocated earlier treatments under the terminology *Johnson graph*, *Grundy colouring*, or random linear extensions. This analysis has not undergone independent mathematical audit.

## References
1. X. Ye, Y. Xu, Z. Wang, J. Zheng and Y. Li, *FirstFit online coloring in the random order model*, arXiv:2608.29603 (first public version 2026-08-30), https://arxiv.org/abs/2608.29603, Section 3.1.
2. W. Kordecki and A. Łyczkowska-Hanćkowiak, *Greedy online colouring with buffering*, arXiv:1601.00252 (2016), https://arxiv.org/pdf/1601.00252, Sections 3.1 and 4.
3. Y. Li and X. Li, *FirstFit coloring process of random bipartite graphs and an online coloring lower bound in the random order model*, arXiv:2610.15468 (2026), https://arxiv.org/html/2610.15468, Section 1.2.
