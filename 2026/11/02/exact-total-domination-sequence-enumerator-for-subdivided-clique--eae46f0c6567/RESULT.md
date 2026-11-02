# Exact total-domination sequence enumerator for subdivided cliques

## Finding

For every integer \(n\ge 2\), let \(H_n=S(K_n)\) be the incidence graph of the labeled complete graph \(K_n\): it has original vertices \([n]\), one subdivision vertex \(w_{ij}\) for every unordered pair \(\{i,j\}\), and precisely the edges \(iw_{ij}\) and \(jw_{ij}\). A *legal total-dominating sequence* is a sequence \((v_1,\ldots,v_\ell)\) of distinct vertices such that, for each \(i\), \(N(v_i)\) contains a vertex outside \(\bigcup_{j<i}N(v_j)\), and \(\bigcup_{i=1}^\ell N(v_i)=V(H_n)\). Orders count as distinct.

Let \(T_n(z)=\sum_{\ell}T_{n,\ell}z^\ell\) count these completed sequences by length. Define integers \(a_{r,k}\) for \(r,k\ge0\) by \(a_{0,0}=1\), zero outside the feasible range, and, for \(r\ge1\),

\[
a_{r,k}=r(r-1)a_{r-1,k-1}+\binom r2 a_{r-2,k-1},
\]

with a term having a negative subscript interpreted as zero. Then the **complete ordered-sequence polynomial** is

\[
\boxed{T_n(z)=n!\sum_{k=\lceil n/2\rceil}^{n-1}\binom{n-1+k}{n-1}a_{n,k}z^{n-1+k}.}
\]

Every exponent in the range \(n-1+\lceil n/2\rceil\) through \(2n-2\) occurs, and no other exponent occurs. Thus

\[
\gamma_t(H_n)=n-1+\lceil n/2\rceil,\qquad
\gamma_{\mathrm{gr}}^t(H_n)=2n-2.
\]

At the maximum exponent the exact coefficient is

\[
\boxed{T_{n,2n-2}=n!\binom{2n-2}{n-1}\binom n2(n-1)!(n-2)!.}
\]

For even \(n=2r\), the coefficient at the minimum exponent is

\[
T_{2r,3r-1}=(2r)!\binom{3r-1}{2r-1}\frac{(2r)!}{2^r}.
\]

For odd \(n=2r+1\), \(r\ge1\), it is

\[
T_{2r+1,3r+1}=(2r+1)!\binom{3r+1}{2r}\frac{(2r+1)!r(r+1)}{2^r}.
\]

## Assumptions and scope

The graphs are finite, simple, undirected, and labeled. A subdivision vertex \(w_{ij}\) corresponds to the **unordered** pair \(\{i,j\}\). The total domination requirement concerns *all* vertices, selected or unselected. Legal sequences are nonrepeating and terminate exactly when the entire graph has been totally dominated: an earlier completed sequence cannot be extended legally. No weighted or stochastic domination game is asserted. The theorem holds for each integer \(n\ge2\), including \(n=2\) and \(n=3\).

## Proof

**Step 1: two independent kinds of footprint.** Partition \(V(H_n)=A\sqcup B\), with \(A=[n]\) and \(B=\{w_{ij}:i<j\}\). Every neighborhood of a vertex in \(A\) lies wholly in \(B\), while every neighborhood of a vertex in \(B\) lies wholly in \(A\). Consequently the relative legality of selected \(A\)-vertices depends only on their own subsequence; likewise for \(B\). Moreover a complete sequence must separately dominate \(B\) via its \(A\)-subsequence and \(A\) via its \(B\)-subsequence. Conversely, any interleaving of two legal, separately covering subsequences is a legal total-dominating sequence; the two relative orders recover the interleaving uniquely.

**Step 2: the original-vertex subsequence.** Selecting an original vertex \(i\) newly dominates exactly the subdivision vertices corresponding to edges incident to \(i\) that were not previously covered. Thus a covering \(A\)-subsequence corresponds to a legal ordered vertex cover of \(K_n\). Before \(n-1\) distinct originals have been selected, at least two originals remain, and their connecting edge has not yet been covered. Every selection through position \(n-1\) therefore newly covers an edge; after \(n-1\) selections, all edges are covered and the last unchosen original is illegal. Accordingly this subsequence always has length exactly \(n-1\), with \(n!\) possibilities (choose the omitted vertex and order the other \(n-1\)).

**Step 3: the subdivision-vertex subsequence.** A selected \(w_{ij}\) covers original vertices \(i\) and \(j\). It is legal precisely when at least one of these two is not yet covered by preceding subdivision selections. Therefore the corresponding ordered edges of \(K_n\) cover every original vertex and at each step introduce one or two previously uncovered vertices. Write \(a_{n,k}\) for the number of these ordered covering edge histories of length \(k\) on a specified labeled \(n\)-vertex set. Classify the last edge by whether it introduces one or two vertices. If it introduces one, there are \(n\) choices for the new label, \(n-1\) choices for its old neighbor, and \(a_{n-1,k-1}\) preceding histories. If it introduces two, choose the new unordered pair in \(\binom n2\) ways, followed by one of the \(a_{n-2,k-1}\) preceding histories. The two cases are disjoint and exhaustive, proving the stated recurrence and its initial conditions.

The first chosen edge introduces two vertices and every later edge introduces at least one, so \(\lceil n/2\rceil\le k\le n-1\). Every integer in this interval occurs: partition \([n]\) into \(n-k\) blocks each of size at least two; in each block choose a star, take its initial edge before its other edges, and interleave the blocks. The resulting covering edge history uses exactly \(k\) edges.

**Step 4: shuffle and coefficients.** There are \(n!\) legal \(A\)-subsequences, \(a_{n,k}\) legal \(B\)-subsequences of length \(k\), and \(\binom{n-1+k}{n-1}\) ways to interleave any chosen pair without changing its relative orders. This is a bijection, proving the boxed polynomial and its complete nonzero exponent interval. The first and last exponents give the two extremal domination sequence lengths.

**Step 5: extreme coefficients.** For \(n=2r\) and \(k=r\), each edge must introduce two vertices, so the edges are an ordered perfect matching. Assign all \(n\) labels to ordered endpoint slots, divide by two for swapping the endpoints in each slot, and obtain \(a_{2r,r}=(2r)!/2^r\). For \(n=2r+1\) and \(k=r+1\), precisely one edge introduces only one vertex. If it occurs after \(j\) two-vertex introductions, it has \(2j\) choices for its previously seen endpoint. For each of the \(r\) possible placements \(1\le j\le r\), the assignment of all newly introduced labels contributes \((2r+1)!/2^r\). Summing \(2+4+\cdots+2r=r(r+1)\) gives \(a_{2r+1,r+1}=(2r+1)!r(r+1)/2^r\).

For \(k=n-1\), the first edge introduces two vertices and every subsequent edge introduces exactly one; the first edge has \(\binom n2\) choices and at a stage when \(c\) vertices have been covered the next edge has \(c(n-c)\) choices. Therefore

\[
a_{n,n-1}=\binom n2\prod_{c=2}^{n-1}c(n-c)
=\binom n2(n-1)!(n-2)!.
\]

Substitution into the shuffle formula proves all three extreme coefficient identities. The empty product convention handles \(n=2\).

## Verification

The accompanying standalone `verify_sequences.py` constructs the original subdivided graph adjacency and, without using the recurrence to enumerate histories, counts complete legal open-neighborhood sequences by dynamic programming over selected-vertex masks. Independently it calculates the proposed coefficients from the recurrence and the shuffle formula. For \(n=2,3,4,5\) the resulting polynomials agree exactly:

\[
\begin{aligned}
T_2(z)&=4z^2,\\
T_3(z)&=216z^4,\\
T_4(z)&=1440z^5+34560z^6,\\
T_5(z)&=756000z^7+12096000z^8.
\end{aligned}
\]

The verifier additionally checks interval support and both minimum/maximum coefficients. These finite computations corroborate, but do not prove, the universal identities, which follow from Steps 1--5.

## Relationship to prior work

Bahadır, Gözüpek, and Doğan (2020 preprint; 2021 journal article) introduced and analyzed the total-\(k\)-uniform classification problem; this motivates understanding the entire length distribution, not only its endpoints. Brešar, Henning, and Rall (2016), Section 8 and Theorem 8.4, already link total dominating sequences of incidence graphs to hypergraph covering sequences and determine the **maximum** length as twice the Grundy covering number. In particular the scalar maximum above follows from that general theorem combined with the elementary covering analysis of \(K_n\); it is **not** asserted to be new on its own. Brešar, Kos, Nasini, and Torres (2016/2018) study complexity and extremal lengths, rather than this ordered-sequence distribution.

The claimed contribution is the **complete number of labeled completed legal histories at every possible length**, with the exact recurrence, explicit extreme multiplicities, and exhaustive support. Ordinary *unordered* edge-cover counts of \(K_n\) do not equal these counts: the legality constraint and ordering matter, and a chosen edge set can have no legal ordering or multiple legal orderings.

## Limitations

The result concerns full single-edge subdivisions of complete graphs, not arbitrary incidence graphs or all graph subdivisions. The recurrence counts ordered legal histories, not unordered total dominating sets, and no asymptotic probability law is asserted. The principal literature comparisons include published extremal results and relevant mathematical-record searches; priority under another name for these refined coefficients cannot be ruled out without a comprehensive bibliographic audit. Independent mathematical validation has not been performed.

## References

1. S. Bahadır, D. Gözüpek, O. Doğan, *Total \(k\)-Uniform Graphs*, arXiv:2010.08368, first posted 2020-10-16; journal version *On graphs all of whose total dominating sequences have the same length*, Discrete Mathematics 344 (2021), article 112492. https://arxiv.org/abs/2010.08368
2. B. Brešar, M. A. Henning, D. F. Rall, *Total Dominating Sequences in Graphs*, Discrete Mathematics 339 (2016), 1665--1676; arXiv:1601.07525. https://arxiv.org/abs/1601.07525
3. B. Brešar, T. Kos, G. Nasini, P. Torres, *Total dominating sequences in trees, split graphs, and under modular decomposition*, Discrete Optimization 28 (2018), 16--30; arXiv:1608.06804. https://arxiv.org/abs/1608.06804
