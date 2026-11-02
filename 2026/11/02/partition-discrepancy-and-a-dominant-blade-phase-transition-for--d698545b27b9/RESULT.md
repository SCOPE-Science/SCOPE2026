# Partition discrepancy and a dominant-blade phase transition for graph spread of clique bouquets

## Finding
Let \(r\ge2\) and let \(a_1,\ldots,a_r\) be arbitrary positive integers. Form a connected unit-edge graph \(G\) by taking disjoint cliques of orders \(a_i+1\) and identifying exactly one vertex from every clique as a common hub; other vertices are disjoint. Set
\[
T=\sum_{i=1}^r a_i,\quad N=T+1,\quad A=\max_i a_i,\quad Q=T-A,\quad
\delta=\min_{\varepsilon_i\in\{-1,1\}}\left|\sum_i\varepsilon_i a_i\right|.
\]
The exact sharp variance of a real one-Lipschitz function under uniform vertex measure is
\[
\boxed{\operatorname{spr}(G):=\max_{\operatorname{Lip}(f)\le1}\frac1N\sum_{v\in G}(f(v)-\bar f)^2
=\frac1{N^2}\begin{cases}
NT-\delta^2,&A\le3Q+1,\\
2NQ+\lfloor N^2/4\rfloor,&A\ge3Q+2.
\end{cases}}
\]
At \(A=3Q+2\), the two displayed numerators coincide, while a genuinely partly occupied clique first joins the optimizers. A partial pattern beats every fully signed clique assignment **strictly** exactly when \(A\ge3Q+3\), with exact squared-numerator gap
\[
\boxed{\left\lfloor\frac{(A-3Q-1)^2}{4}\right\rfloor.}
\]
All equality cases are classified below. Up to adding a constant, reversing signs, and permuting vertices inside each clique, if \(A\le3Q+1\) every optimizer assigns the hub value \(0\) and assigns a uniform value \(\varepsilon_i\in\{-1,1\}\) to each nonhub clique, with \(\left|\sum_i\varepsilon_i a_i\right|=\delta\). At \(A=3Q+2\) these remain optimizers, and there are additional optimizers: the unique largest clique contains \(A-1\) nonhub vertices at \(+1\) and one at \(0\), while every other nonhub vertex is at \(-1\). If \(A\ge3Q+3\), all optimizers have this latter pattern with \(k\) vertices of the largest clique at \(+1\), its remaining \(A-k\) vertices at \(0\), and all other nonhub vertices at \(-1\), where
\[
k\in\left\{1,\ldots,A-1\right\}\quad\text{minimizes}\quad
\left|k-\left(Q+\frac N2\right)\right|.
\]
Here descriptions of partial patterns also allow the global reversal of all signs.

For equal blade sizes \(a_i=a\) and \(r\ge2\), the formula simplifies to
\[
\operatorname{spr}(G)=\frac{ra}{ra+1}-\frac{a^2}{(ra+1)^2}\mathbf1_{\{r\text{ odd}\}}.
\]
For one large clique with \(Q\) nonhub vertices outside it fixed, \(\operatorname{spr}(G)\to1/4\) as \(A\to\infty\), despite the graph's diameter remaining two.

## Assumptions and scope
The graph has at least two clique blocks, all nonhub blade sizes \(a_i\ge1\), no edges between distinct blades, unweighted graph distance, and uniform probability measure on the \(N\) vertices. The seminorm is \(\operatorname{Lip}(f)=\max_{uv\in E(G)}|f(u)-f(v)|\); this equals the metric Lipschitz constant on the shortest-path metric. The variance is centered with \(\bar f=N^{-1}\sum_v f(v)\). No statement concerns the subgaussian constant (which is generally different from the graph spread).

## Proof

**1. Strict convexity and the one-blade polytope.** Translate every candidate so that the hub has value zero. The anchored Lipschitz feasible set is a product of polytopes
\[
P_a=\{z\in[-1,1]^a:|z_j-z_k|\le1\text{ for all }j,k\}.
\]
The map \(f\mapsto\sum_v(f(v)-\bar f)^2\) is strictly convex on anchored functions: its quadratic form has only constants in its kernel, and the anchor removes that kernel. Hence **every** maximizer is an extreme point of the product polytope. At an extreme point of \(P_a\), a uniform small translation must be impossible, so either the maximum coordinate is \(+1\) or the minimum is \(-1\). Both cannot occur because their distance would be \(2\). In the former case all coordinates lie in \([0,1]\), and any interior coordinate can be perturbed, so all coordinates are \(0\) or \(1\). The latter case is its negative. Conversely these \(0/1\) and \(0/-1\) patterns with at least one nonzero coordinate are vertices. This also covers \(a=1\), for which the only vertices are \(\pm1\).

Thus at an extremizer each blade has one sign \(\varepsilon_i\) and precisely \(k_i\in\{1,\ldots,a_i\}\) nonzero vertices with that sign. Put \(K=\sum_i k_i\), \(S=\sum_i\varepsilon_i k_i\). Direct centering gives
\[
N^2\operatorname{Var}(f)=NK-S^2.
\]

**2. The structure forced by a partial blade.** Suppose some blade is partial, so \(k_i<a_i\). We may reverse every sign and assume \(S\ge0\). A partially occupied negative blade could gain one extra negative vertex, increasing \(K\) by one and decreasing \(S\) by one; the numerator improves by \(N+2S-1>0\). If \(S=0\), filling any partial blade improves by \(N-1>0\). Consequently \(S>0\) and every partial blade is positive. Increasing its active count by one changes the numerator by \(N-2S-1\), so maximality forces
\[
S\ge\frac{N-1}{2}.
\]
For any positive blade with \(k_j<S\), reversing its sign changes the numerator by \(4k_j(S-k_j)>0\). Thus every positive blade has \(k_j\ge S\). If there were at least two positive blades, the total positive active count \(P\) would satisfy \(P\ge2S\). But \(K=2P-S\ge3S\ge3(N-1)/2>N-1\), contradicting \(K\le T=N-1\). Hence there is exactly one positive blade, and all the others are negative and full. Write \(a\) for its size, \(Q'=T-a\), and \(k<a\) for its positive active count. Then \(S=k-Q'\), and the local maximality bound, together with \(k\le a-1\), forces
\[
a\ge3Q'+2.
\]
Such a blade, if it exists, is strictly larger than the sum of all other blade sizes. It is therefore the unique largest blade, so \(a=A\) and \(Q'=Q\).

**3. The full-sign regime.** If \(A\le3Q+1\), no partially occupied blade can occur by step 2. Every blade is full, so \(K=T\). Maximizing \(NT-S^2\) reduces exactly to the signed-partition discrepancy \(\delta\), yielding \(NT-\delta^2\) and all the stated fully signed equality cases.

**4. The dominant regime and equality.** Assume \(A\ge3Q+2\). Since \(A>Q\), the least discrepancy among full assignments is \(\delta=A-Q\), uniquely obtained by giving the largest blade the opposite sign from all others. Every partial optimizer also has this sign disposition by step 2, so it suffices to maximize
\[
F(k)=N(k+Q)-(k-Q)^2
=2NQ+\frac{N^2}{4}-\left(k-Q-\frac N2\right)^2,
\]
over integers \(1\le k\le A\), where \(k=A\) represents the full choice. The center \(k_*=Q+N/2=(A+3Q+1)/2\) lies at least half a unit below \(A\) and strictly above \(1\) in this regime. The nearest allowed integer(s) therefore attain the maximum. Since \(N\) is integral, \(\max F(k)=2NQ+\lfloor N^2/4\rfloor\). When \(A=3Q+2\), \(k_*=A-1/2\), giving exactly the two choices \(k=A-1,A\). When \(A\ge3Q+3\), its nearest integers are all strictly smaller than \(A\), giving only partial optimal patterns. Every maximizer is already covered by steps 1–2, so the equality classification is exhaustive.

**5. Sharp phase gap.** The best full-sign numerator is \(NT-(A-Q)^2\). Using \(N=(A-Q)+(2Q+1)\), direct subtraction yields
\[
2NQ+\lfloor N^2/4\rfloor-\bigl(NT-(A-Q)^2\bigr)
=\left\lfloor\frac{(A-3Q-1)^2}{4}\right\rfloor.
\]
The right side is zero exactly at the stated transition value \(A=3Q+2\) within this regime and is strictly positive for larger \(A\).

**6. Consequences.** If all \(a_i=a\), the signed sum has minimum absolute value zero for even \(r\), or \(a\) for odd \(r\). The dominant condition is impossible for \(r\ge2\); substitution proves the equal-blade formula. With fixed \(Q\) and \(A\to\infty\), the dominant formula becomes \(2Q/N+\lfloor N^2/4\rfloor/N^2\to1/4\). All conclusions follow.

## Verification
The standalone Python program `verify_clique_bouquet_spread.py` tests the exact formulas via (i) exhaustive signed active-count assignments for 203 tuples of sizes, (ii) direct enumeration of 27,726 labelled integral anchored Lipschitz functions over 40 graph instances, (iii) exact phase thresholds for 168 parameter choices, and (iv) equal-petal and giant-blade special cases. It uses integer arithmetic, checks results without invoking the analytic formula inside the independent brute-force optimizers, and prints explicit success labels. These finite computations are diagnostics, not proofs of the all-parameter theorem; steps 1–6 give the proof.

## Relationship to prior work
Alon, Boppana and Spencer introduced the spread constant of finite graph metrics and proved existence of integral extremizers, as well as its role in sharp product-space concentration. Their general theorem does not provide this closed formula or the dominant-clique transition. Addario-Berry, Janson and McDiarmid subsequently analyzed spread of random graphs, rather than exact sharp constants of arbitrary vertex-glued clique bouquets. Yancey's results on variance extremizers address structural constraints and examples involving long hairs; they do not give the present complete heterogeneous-clique calculation. Results about generalized roundness, nonlinear heat-flow stability, or tree double-broom spread use different invariants or metric families and do not imply this theorem. The novel content assessed here is specifically the exact arithmetic-discrepancy formula for **all** positive clique-size tuples, the full extremizer classification, and the squared strict-phase gap.

## Limitations
The classification concerns real-valued functions, uniform vertex measure, exactly one common hub and unweighted clique blocks. It does not classify graphs whose maximal cliques overlap in larger vertex sets, nonuniform vertex masses, other centered moments, or subgaussian constants. Literature searching is not a uniqueness proof; differently phrased results could already contain the same formula. No independent mathematical audit has been performed.

## References
1. N. Alon, R. Boppana, and J. Spencer, *An Asymptotic Isoperimetric Inequality*, Geometric and Functional Analysis **8** (1998), 411–436. Author-hosted full text: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf ; DOI: 10.1007/s000390050062.
2. L. Addario-Berry, S. Janson, and C. McDiarmid, *On the Spread of Random Graphs*, preprint first public February 6, 2009, arXiv:0902.1156, published in Combinatorics, Probability and Computing (2014). https://arxiv.org/abs/0902.1156.
3. M. Yancey, *Probabilistic and Geometrical Applications to Graph Theory*, preprint first public May 26, 2017, arXiv:1705.09725. https://arxiv.org/abs/1705.09725.
