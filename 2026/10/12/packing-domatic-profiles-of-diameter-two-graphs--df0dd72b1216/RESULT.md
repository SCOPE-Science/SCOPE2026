# Packing domatic profiles of diameter-two graphs

## Finding

Let \(G\) be a finite connected graph of order \(n\) and diameter \(2\). Let \(S=(s_1,s_2,\ldots)\) be a nondecreasing sequence of positive integers satisfying
\[
s_1=1,\qquad s_2\ge2.
\]
Write
\[
\mathcal M(G)=\{|D|:D\subseteq V(G)\text{ is a maximal independent set}\},
\]
let \(\alpha=\alpha(G)\), and put
\[
c=n-\alpha+1.
\]
Then for every integer \(1\le k\le n\),
\[
\chi_{S,k}(G)=
\begin{cases}
c,&k\le c,\\
k,&k>c\text{ and }n-k+1\in\mathcal M(G),\\
k+1,&k>c\text{ and }n-k+1\notin\mathcal M(G).
\end{cases}
\]

Consequently, the complete profile \(k\mapsto\chi_{S,k}(G)\) determines the set of cardinalities of maximal independent sets. Indeed,
\[
\alpha=n-c+1,
\]
and for each integer \(s<\alpha\),
\[
s\in\mathcal M(G)
\quad\Longleftrightarrow\quad
\chi_{S,n-s+1}(G)=n-s+1.
\]

For the ordinary packing sequence \(S=(1,2,3,\ldots)\), this gives the full packing \(k\)-domatic chromatic profile of every diameter-two graph.

As an explicit family, let
\[
G=K_{n_1,\ldots,n_r}
\]
be a connected complete multipartite graph of diameter \(2\), let
\[
N=\sum_i n_i,\qquad L=\max_i n_i.
\]
Its maximal independent sets are exactly its partite classes. Hence
\[
\chi_{S,k}(G)=
\begin{cases}
N-L+1,&k\le N-L+1,\\
k,&k>N-L+1\text{ and }N-k+1\in\{n_1,\ldots,n_r\},\\
k+1,&\text{otherwise}.
\end{cases}
\]

## Assumptions and scope

Graphs are finite, simple, undirected, connected, and have diameter exactly \(2\). The sequence \(S=(s_1,s_2,\ldots)\) is nondecreasing, consists of positive integers, and satisfies \(s_1=1\) and \(s_2\ge2\).

An \(S\)-packing coloring \(f:V(G)\to\mathbb N\) requires
\[
d_G(u,v)>s_i
\]
whenever two distinct vertices \(u,v\) both receive color \(i\). It is a packing \(k\)-domatic coloring if \(V(G)\) can be partitioned into \(k\) nonempty sets such that the restriction of \(f\) to each part is a dominating broadcast, where a vertex colored \(i\) broadcasts to distance \(i\). The number \(\chi_{S,k}(G)\) is the least largest color among such colorings.

The theorem does not assert an analogous formula for graphs of diameter at least \(3\), where colors \(2,3,\ldots\) may repeat and a single higher-colored vertex need not dominate the graph.

## Proof

Because \(\operatorname{diam}(G)=2\) and \(s_i\ge s_2\ge2\) for every \(i\ge2\), two distinct vertices can never share a color \(i\ge2\). Thus every color at least \(2\) is used on at most one vertex. Since \(s_1=1\), the color-\(1\) class is an independent set.

Let \(f\) be any \(S\)-packing coloring and let
\[
A=\{v:f(v)=1\}.
\]
Every vertex with color at least \(2\) has broadcast radius at least \(2\), hence by the diameter assumption it individually dominates all of \(G\).

Now consider a block \(B\) in a broadcast-domatic partition which contains only color-\(1\) vertices. Since \(B\subseteq A\) and \(A\) is independent, no vertex of \(A\setminus B\) is adjacent to a vertex of \(B\). Therefore \(B\) can dominate \(G\) only if \(A\setminus B=\varnothing\), so \(B=A\). In that case \(B\) dominates if and only if every vertex outside \(A\) has a neighbor in \(A\), equivalently if and only if \(A\) is a maximal independent set.

It follows that a packing coloring using colors in \([t]\) has at most \(t-1\) vertices of color at least \(2\), and a broadcast-domatic partition can have at most one further block containing only color-\(1\) vertices. Hence every packing \(k\)-domatic coloring on a diameter-two graph satisfies
\[
t\ge k.
\]

For the first regime, let \(A\) be a maximum independent set. Then \(|A|=\alpha\), \(A\) is maximal and hence dominating, and assigning color \(1\) to \(A\) and pairwise distinct colors
\[
2,3,\ldots,n-\alpha+1
\]
to the remaining vertices gives an \(S\)-packing coloring with largest color \(c=n-\alpha+1\). The block \(A\), together with the \(n-\alpha\) singleton higher-color blocks, is a broadcast-domatic partition into \(c\) blocks. Merging blocks gives such a partition into every \(k\le c\) blocks. Since every \(S\)-packing coloring needs at least \(n-\alpha+1\) colors, one obtains
\[
\chi_{S,k}(G)=c
\]
for every \(k\le c\).

Now suppose \(k>c\). The preceding lower bound gives
\[
\chi_{S,k}(G)\ge k.
\]
Assume first that equality holds. A coloring with largest color \(k\) has at most \(k-1\) higher-colored vertices. To obtain \(k\) broadcast-dominating blocks it must therefore have exactly \(k-1\) higher-colored vertices and exactly one color-\(1\)-only block. Consequently the color-\(1\) class has size
\[
n-(k-1)=n-k+1,
\]
and, by the preceding characterization, it must be a maximal independent set. Thus
\[
\chi_{S,k}(G)=k
\quad\Longrightarrow\quad
n-k+1\in\mathcal M(G).
\]

Conversely, if \(D\) is a maximal independent set of size \(n-k+1\), assign color \(1\) to \(D\) and distinct colors \(2,\ldots,k\) to the remaining \(k-1\) vertices. The set \(D\) is a dominating color-\(1\) block and every remaining singleton block contains a vertex of radius at least \(2\), so this is a packing \(k\)-domatic coloring using colors in \([k]\). Hence
\[
n-k+1\in\mathcal M(G)
\quad\Longrightarrow\quad
\chi_{S,k}(G)=k.
\]

Finally, suppose \(n-k+1\notin\mathcal M(G)\). The previous equivalence rules out value \(k\). Since \(k>c=n-\alpha+1\),
\[
n-k\le\alpha-2.
\]
Choose any independent set \(A\) of size \(n-k\); if \(k=n\), take \(A=\varnothing\). Color \(A\) with \(1\) and color the remaining \(k\) vertices distinctly with
\[
2,3,\ldots,k+1.
\]
Put each higher-colored vertex in a separate block and distribute the vertices of \(A\) arbitrarily among those blocks. Every block contains a vertex of broadcast radius at least \(2\), so every block dominates \(G\). Therefore
\[
\chi_{S,k}(G)\le k+1.
\]
Together with the exclusion of \(k\), this proves
\[
\chi_{S,k}(G)=k+1.
\]

For a complete multipartite graph of diameter \(2\), the maximal independent sets are precisely the whole partite classes, so substituting
\[
\mathcal M(G)=\{n_1,\ldots,n_r\}
\]
gives the displayed multipartite formula.

## Verification

The accompanying script `artifacts/verify.py` reconstructs the definition directly for the ordinary packing sequence \(S=(1,2,3,\ldots)\). It enumerates every labeled graph of diameter exactly \(2\) on \(3\), \(4\), and \(5\) vertices.

For each graph it computes all-pairs shortest-path distances, enumerates every coloring with colors in
\[
\{1,\ldots,n+1\},
\]
tests the packing condition from distances, and independently searches set partitions into broadcast-dominating blocks. It compares the resulting minimum largest color for every \(k\) against the theorem's maximal-independent-set formula.

The checker covers \(395\) labeled diameter-two graphs and examines \(2,869,609\) color assignments before pruning by the packing condition.

The finite check is corroborative only. The theorem for arbitrary order and for every nondecreasing \(S\) with \(s_1=1\) and \(s_2\ge2\) is proved analytically above.

## Relationship to prior work

Brešar, Ferme, and Hu introduced \(S\)-packing \(k\)-domatic colorings in 2026. Their Proposition 2.6 proves that for a diameter-two graph and \(s_1=1\), \(s_2\ge2\),
\[
\operatorname{dom}_{\chi_S}(G)=n-\alpha(G)+1,
\]
equivalently, an optimal \(S\)-packing coloring supports exactly up to \(n-\alpha(G)+1\) broadcast-dominating blocks. Their paper also studies exact values on paths and cycles and poses further questions about the behavior of \(\chi_{\rho,k}\).

The present theorem begins where Proposition 2.6 stops: it determines \(\chi_{S,k}(G)\) for every larger \(k\) as well. The tail is not controlled by \(\alpha(G)\) alone; it records which smaller cardinalities occur among maximal independent sets. Thus the complete \(k\)-profile recovers a classical structural spectrum that is invisible to the single optimal-color packing domatic number.

For complete multipartite graphs, the theorem becomes fully explicit because the maximal independent sets are exactly the partite classes. No complete-multipartite formula or maximal-independent-set tail criterion appears in the inspected full text of arXiv:2610.03477v1, and targeted database searches did not locate an equivalent statement.

## Limitations

The diameter-two hypothesis is essential to the proof mechanism. For larger diameter, colors at least \(2\) can repeat, and a higher-colored singleton does not necessarily dominate the graph.

The computational verification uses only the ordinary packing sequence and orders through \(5\); it is not evidence for the infinite quantifier by itself. The extension to all permitted sequences \(S\) follows from the analytic observation that every color at least \(2\) is forced to be unique when \(\operatorname{diam}(G)=2\) and \(s_2\ge2\).

The originality assessment is literature-based. Because the invariant was introduced only recently, concurrent or poorly indexed work could contain an equivalent tail characterization.

## References

1. B. Brešar, J. Ferme, and W. Hu, “Partitioning an \(S\)-packing coloring into broadcast dominating sets,” arXiv:2610.03477v1, first public October 2, 2026. In particular, Proposition 2.6 treats the optimal-color packing domatic number for diameter-two graphs.
