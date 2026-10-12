# Exact \(k\)-rainbow total domination of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), positive part sizes, total order \(N=\sum_i n_i\), and smallest part size \(s=\min_i n_i\). For every integer \(k\ge2\), put \(q=\lfloor k/2\rfloor\) and define
\[
h_k(s)=
\begin{cases}
k,&s\le q,\\
s+q+1,&s>q.
\end{cases}
\]
Then
\[
\gamma_{k\mathrm{rt}}(G)=\min\{N,2k,h_k(s)\}.
\]
Equivalently, using the established identity between rainbow total domination and total domination in generalized prisms,
\[
\gamma_t(G\square K_k)=\min\{N,2k,h_k(s)\}.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. There are at least two nonempty partite classes. A \(k\)-rainbow total dominating function is a map \(f:V(G)\to2^{[k]}\) such that every vertex with empty label sees all \(k\) colors in its open neighborhood, and every vertex with a singleton label \(\{c\}\) has a neighbor whose label contains \(c\). Its weight is \(\sum_v|f(v)|\), and \(\gamma_{k\mathrm{rt}}(G)\) is the minimum weight. The theorem is stated for \(k\ge2\); the same displayed minimum also reduces to the usual total-domination value when \(k=1\).

## Proof
Write \(q=\lfloor k/2\rfloor\).

There are three universal upper constructions. First, label every vertex by the same singleton color. Since every vertex has a neighbor in another part, this is a valid function of weight \(N\). Second, choose vertices in two distinct parts and label both by \([k]\), leaving all other vertices empty. Every empty vertex sees one of the two full-color labels, so this has weight \(2k\).

For the third construction choose a smallest part \(A\) of size \(s\). If \(s\le q\), partition the \(k\) colors into \(s\) nonempty blocks of size at least two and place one block on each vertex of \(A\), leaving every other vertex empty. No labeled vertex carries a singleton, and every empty vertex sees all colors in \(A\); the weight is \(k\).

Suppose now that \(s>q\). Give \(q\) vertices of \(A\) labels of size two. When \(k\) is even these pairs cover all colors; when \(k\) is odd they cover the first \(k-1\) colors. Give each remaining vertex of \(A\) the singleton label \(\{k\}\). Choose one vertex outside \(A\) and also label it \(\{k\}\), leaving every other vertex empty. The singleton vertices in \(A\) and the outside singleton support one another, while the union of labels on \(A\) is \([k]\), so every empty vertex is valid. The weight is
\[
2q+(s-q)+1=s+q+1.
\]
This proves the upper bound by the displayed minimum.

For the lower bound, let \(f\) have weight \(W\). If \(W\ge N\) or \(W\ge2k\), there is nothing to prove, so assume \(W<N\) and \(W<2k\). Some vertex is empty. If every part contained an empty vertex, then each color would have to occur in at least two distinct parts: a color occurring in only one part would be invisible to an empty vertex in that part. Hence \(W\ge2k\), a contradiction. Therefore some part \(A\) is full, meaning every vertex of \(A\) has a nonempty label. Put \(a=|A|\), so \(a\ge s\).

If \(s\le q\), any empty vertex must see all \(k\) colors, immediately giving \(W\ge k=h_k(s)\). It remains to consider \(s>q\), so also \(a>q\).

Let \(p\) be the number of singleton-labeled vertices in \(A\), let \(r_0\) be the number of distinct colors occurring on those singleton labels, let \(w_A\) be the contribution of \(A\), and let \(U_A\) be the union of the colors used on \(A\). If \(p=0\), then every vertex of \(A\) has label size at least two, and
\[
W\ge w_A\ge2a\ge a+q+1\ge s+q+1.
\]

Assume \(p>0\). Then \(w_A\ge2a-p\) and \(r_0\ge1\). Every singleton color used in \(A\) must occur outside \(A\). Also, because an empty vertex exists outside the full part \(A\), every color missing from \(U_A\) must occur outside \(A\). These two color sets are disjoint. Moreover
\[
|U_A|\le w_A-(p-r_0),
\]
because the \(p\) singleton incidences contribute only \(r_0\) distinct colors. Consequently
\[
W\ge w_A+r_0+k-|U_A|\ge k+p,
\]
and independently
\[
W\ge w_A+r_0\ge2a-p+1.
\]
Thus
\[
W\ge\max\{k+p,2a-p+1\}.
\]
This maximum is always at least \(a+q+1\). Indeed, if both terms were smaller, then for even \(k=2q\) one would have simultaneously \(p>a-q\) and \(p<a-q+1\), impossible for an integer \(p\); for odd \(k=2q+1\) one would obtain the incompatible strict inequalities \(p>a-q\) and \(p<a-q\). Hence
\[
W\ge a+q+1\ge s+q+1=h_k(s).
\]
The lower bound matches the constructions and proves the formula.

## Verification
The accompanying `verify.py` checks the definition directly, without using the theorem, for every complete-multipartite part-size profile of total order from two through five and every \(k\in\{2,3,4\}\). It enumerates all vertex labels in \(2^{[k]}\), computes the true minimum, and compares it with the formula. It also checks algebraically that the formula specializes to the published complete-bipartite expression over a broad finite parameter range. The finalized replay output is included in `verification_output.txt`. These finite computations are stress tests only; the arbitrary-order result follows from the proof above.

## Relationship to prior work
Erveš, Kraner Šumenjak, and Tepeh study the same \(k\)-rainbow total domination invariant, prove NP-completeness for every fixed \(k\), and list primary MSC 05C69. Their accessible full article contains no occurrence of “multipartite” or “complete bipartite”; it focuses on complexity and bounds rather than exact complete-multipartite values.

Ojakian, Škrekovski, and Tepeh give an exact formula for \(\gamma_{k\mathrm{rt}}(K_{a,b})\). Their Proposition 3 has precisely the three regimes obtained by specializing the theorem above to two parts: \(k\) for a sufficiently small shore, an intermediate value \(a+\lceil(k+1)/2\rceil\), and \(2k\) beyond the threshold, with the order \(a+b\) taking over when it is at most \(k\). Their full text has no complete-multipartite occurrence. Thus the bipartite theorem is genuine prior coverage of the \(r=2\) slice, but it does not imply the arbitrary-multipartite theorem.

Targeted searches under the invariant name, its generalized-prism formulation, and complete-multipartite aliases found no statement covering the formula. The closest indexed same-family result located concerns ordinary 2-rainbow domination, which omits the singleton-support condition and therefore does not imply the total variant.

## Limitations
The theorem concerns complete multipartite graphs and does not classify all minimum functions. It gives an exact scalar invariant and its generalized-prism equivalent, not a weight enumerator. Search-based originality checks cannot establish absolute absence from unindexed literature, and an older equivalent result under different notation remains a residual risk. Independent audit has not been performed.

## References
1. R. Erveš, T. Kraner Šumenjak, and A. Tepeh, *On k-Rainbow Total Domination and a Related Conjecture*, Bulletin of the Malaysian Mathematical Sciences Society 49 (2026), article 62, DOI:10.1007/s40840-026-02060-2, published 19 February 2026.
2. K. Ojakian, R. Škrekovski, and A. Tepeh, *Bounding the k-rainbow total domination number*, Discrete Mathematics 344 (2021), 112425; arXiv:2003.09470. Proposition 3 gives the exact complete-bipartite formula.
3. T. Kraner Šumenjak and A. Tepeh, *Complexity of 2-Rainbow Total Domination Problem*, Bulletin of the Malaysian Mathematical Sciences Society 47 (2024), article 155, DOI:10.1007/s40840-024-01747-8.
