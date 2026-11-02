# Sharp single-joker cyclic binary factor-cover length

## Finding
Fix an integer \(k\ge1\). A *cyclic one-joker binary host* is a cyclic string \(W\) of length \(N\ge k\) over \(\{0,1,\diamond\}\), with exactly one occurrence of \(\diamond\). Its length-\(k\) factors are the \(N\) cyclic windows, one beginning at each position. Each factor containing the joker represents two ordinary binary words, with \(\diamond\) replaced by either bit; the resolution can differ between distinct factor observations. A host is *covering* if all \(2^k\) binary length-\(k\) words are represented at least once. Repetitions are allowed.

**Theorem.** The minimum length of a covering cyclic one-joker host is
\[
L(1)=1,\qquad L(k)=2^k-k+1\quad(k\ge2).
\]
For every \(k\ge2\), a shortest host represents exactly \(2^k+1\) ordinary length-\(k\) factors counted with multiplicity: every binary word appears once, except one word appearing twice. The proof below gives a constructive finite algorithm for such a host for every \(k\).

## Assumptions and scope
The alphabet is binary and labeled. Exactly one joker is required, the cyclic host length satisfies \(N\ge k\), and coverage means *contiguous cyclic factors with multiplicity ignored for the coverage condition*. The joker is not required to have a consistent replacement across different windows. These conventions distinguish the problem from exact-once universal partial cycles, linear partial words, and scattered-subsequence covering.

Write \(G_k\) for the binary de Bruijn digraph whose vertices are the \((k-1)\)-bit words and whose labeled edges are the \(k\)-bit words; an edge \(a_1\cdots a_k\) runs from \(a_1\cdots a_{k-1}\) to \(a_2\cdots a_k\). Each vertex has in- and out-degree two. For \(k\ge2\), a binary string of length \(k-1+t\) with successive length-\(k\) factors defines a directed walk of \(t\) edges in \(G_k\).

## Proof
**1. Counting and the sharp obstruction.** Rotate the host to start with its unique joker. Since \(N\ge k\), exactly \(k\) cyclic windows contain the joker and the other \(N-k\) are ordinary binary windows. Thus the total number of resolved length-\(k\) factors, counted with multiplicity, is precisely \(N+k\). To cover all binary words, necessarily \(N+k\ge2^k\); hence \(N\ge2^k-k\).

For \(k=2\), equality would mean \(N=2\). The only hosts up to rotation are \(\diamond0\) and \(\diamond1\), which respectively miss \(11\) and \(00\). Therefore \(L(2)\ge3\).

For \(k\ge3\), suppose equality \(N=2^k-k\) holds. Since \(N-k=2^k-2k>0\), there are ordinary cyclic windows. Write \(U\) for the \((k-1)\)-bit block immediately preceding the joker and \(V\) for the \((k-1)\)-bit block immediately following it. The \(k\) joker-containing windows, with the joker resolved as \(b\in\{0,1\}\), are precisely the successive \(k\)-windows of \(UbV\). They therefore form two directed walks \(P_0,P_1\) from \(U\) to \(V\), each of length \(k\). The ordinary windows form a nonempty directed walk from \(V\) to \(U\).

By equality in counting, these three walks together use every edge of \(G_k\) *exactly once*. In the edge-incidence balance of the union, the two \(U\)-to-\(V\) walks and one \(V\)-to-\(U\) walk yield an out-minus-in excess of \(+1\) at \(U\), and \(-1\) at \(V\), unless \(U=V\). Because the complete graph \(G_k\) is balanced, \(U=V\). In this case, however, the initial edges of \(P_0\) and \(P_1\) are exactly the two distinct edges leaving \(U\), labeled \(U0\) and \(U1\). The nonempty ordinary walk also begins at \(V=U\) and requires a third outgoing edge at \(U\), impossible when each edge is to be used once. Thus \(N\ne 2^k-k\) for \(k\ge3\). This proves \(L(k)\ge2^k-k+1\) for every \(k\ge2\).

**2. Small orders.** The length-one host \(\diamond\) covers both one-bit words. The hosts \(\diamond10\) for \(k=2\) and \(\diamond10001\) for \(k=3\) cover all required words; their lengths are respectively \(3\) and \(6\), attaining the lower bound.

**3. Explicit construction for every \(k\ge4\).** Define the two distinct vertices
\[
U=0^{k-2}1,\qquad V=0^{k-3}10.
\]
For each \(b\in\{0,1\}\), take the \(k\) successive length-\(k\) factors of the length-\((2k-1)\) word \(UbV\), and let \(S\) be the *set* of all such factors. The two paths run from \(U\) to \(V\). A direct examination of the one-positions proves that \(U0V\) has \(k-1\) distinct length-\(k\) factors (only \(U0\), the first and last factor, is repeated), while \(U1V\) has \(k\) distinct length-\(k\) factors, all different from the factors of \(U0V\). To see disjointness, the words from \(U0V\) have at most one one, except the single factor with two ones separated by \(k-1\) places; every factor from \(U1V\) has at least two ones at separation at most \(k-2\). Hence \(|S|=2k-1\), and the resolved factors of \(U\diamond V\) cover \(S\) with only \(U0\) counted twice.

Let \(H\) be the directed graph formed by deleting the \(2k-1\) edges labeled by \(S\) from \(G_k\). The two resolved \(U\)-to-\(V\) walks collectively have incidence excess \(+2\) at \(U\) and \(-2\) at \(V\). Since their multiset comprises the edges of \(S\) plus one extra copy of the edge \(U0:U\to V\), the set \(S\) has excess \(+1\) at \(U\) and \(-1\) at \(V\). Therefore \(H\) has excess \(+1\) at \(V\) and \(-1\) at \(U\), with balanced degrees at all other vertices.

It remains to verify that the nonzero-edge part of \(H\) is weakly connected; no appeal to computational experimentation is needed. Among the deleted edges, those whose last bit is one are *exactly*
\[
0^{k-2}11,\qquad 10^{k-2}1,\qquad 110^{k-3}1.
\]
Consider following the outgoing edge obtained by appending \(1\), repeatedly, from any \((k-1)\)-bit vertex until the all-one vertex is reached. Such a walk lies entirely in \(H\) unless its starting vertex belongs to the four-element exceptional set
\[
\{0^{k-1},\ 0^{k-2}1,\ 10^{k-2},\ 110^{k-3}\}.
\]
Indeed, an excluded append-one edge may occur at the first step only for the last three vertices; at the second step only for the first or third vertices, since then the appended edge ends in \(11\); and at subsequent steps every appended edge ends in at least three consecutive ones, so none is excluded. The exceptions also lie in the same weak component as the all-one vertex because the following four *retained* edges connect them (in underlying undirected order):
\[
0^{k-1}1,\quad 10^{k-1},\quad 110^{k-2},\quad 1110^{k-3}.
\]
Respectively these connect \(0^{k-1}\) to \(U\), \(10^{k-2}\) to \(0^{k-1}\), \(110^{k-3}\) to \(10^{k-2}\), and \(1110^{k-4}\) to \(110^{k-3}\); the vertex \(1110^{k-4}\) is not exceptional. Each edge is absent from \(S\) by the explicit one-patterns above. Consequently all vertices of \(H\) are weakly connected via retained edges.

The directed Euler-trail criterion now supplies an Euler trail through all edges of \(H\), starting at \(V\) and ending at \(U\). Write its ordinary binary representation as the initial block \(V\), followed by the last bit of each traversed edge, and call the resulting string \(T\). Form the cyclic host \(W=\diamond T\). Its joker windows realize the two paths through \(U\diamond V\) as above, and its ordinary windows realize exactly the edges of \(H\) once each. Thus the distinct resolved factors cover all \(2^k\) edges of \(G_k\), with the single extra copy of \(U0\). The length is
\[
|W|=1+(k-1)+\bigl(2^k-(2k-1)\bigr)=2^k-k+1.
\]
This achieves the lower bound and finishes the proof for every integer \(k\ge1\).

**4. Multiplicity at equality.** At a shortest length for \(k\ge2\), the resolved occurrence count is \(L(k)+k=2^k+1\). Since all \(2^k\) distinct words appear, exactly one binary word has multiplicity two and all others have multiplicity one.

## Verification
The accompanying standalone `one_joker_cover_verifier.py` uses only the Python standard library. It implements the above set deletion and an Euler-trail construction, checks every resolved cyclic window for orders \(1\) through \(12\), confirms precisely one duplicate for orders at least two, and exhaustively rules out all shorter cyclic single-joker words at orders \(2,3,4\). A separate direct structural check of the deleted-ending-one edge list, the exceptional paths, and all four connecting retained edges was performed for orders \(4\) through \(14\). Finite checks corroborate, but do not replace, the all-order graph proof.

Run: `python3 one_joker_cover_verifier.py`. Expected terminal line:
`VERIFY_OK k=1..12, checked_window_positions=8123, short_host_exhaustion=4118`.

## Relationship to prior work
Blanchet-Sadri, Schwartz, Stich, and Wyatt (2010) establish a sharp *linear* one-hole binary de Bruijn partial-word length and give a graph-theoretic Euler-trail construction. Their Theorem 4 concerns a noncyclic word of length \(2^k-1\); it does not state the cyclic optimum here. Cutting the cycle immediately *after* the joker and appending the first \(k-1\) ordinary bits unrolls a length-\(N\) cyclic host into a linear one-joker word of length \(N+k-1\), so the published linear lower bound implies only \(N\ge2^k-k\), precisely the bound shown above to be unattainable by cyclic one-joker words. Their noncyclic attaining trail does not automatically close into the required cyclic host. This theorem supplies the additional Euler-balance obstruction and a different single-overlap construction attaining the sharp cyclic optimum.

Orenstein, Yu, and Berger (2018) investigate at-least-once k-mer covering with joker characters under prescribed repeating templates, giving algorithms, an integer-linear formulation, and general lower bounds. The present theorem is an exact binary *single-joker-total* cyclic specialization, with a closed all-order formula and an explicit optimal family, not the full prescribed-template optimization problem. Chen, Kitaev, Mütze, and Sun (2016/2017), and Fillmore and collaborators (2023), consider universal partial words/cycles with each k-mer covered *exactly once*; those statements do not imply the relaxed at-least-once optimum here. The closest older primary paper has been inspected in full; a source-access caveat for the 2018 paper is reported in the scientific review.

## Limitations
The formula is for the binary alphabet, exactly one joker in a cyclic host, and host length at least the factor length. It does not assert an optimal count for linear hosts, arbitrary numbers of jokers, fixed repeating joker templates, larger alphabets, or exact-once partial cycles. The proof is self-contained for its domain, but originality remains subject to unindexed or differently stated cyclic covering results and to any portions of the 2018 paper's displayed-equation content that were not machine-accessible during source comparison. No independent scientific audit has been performed.

## References
1. F. Blanchet-Sadri, J. Schwartz, S. Stich, and B. J. Wyatt, *Binary De Bruijn Partial Words with One Hole*, TAMC 2010, DOI: https://doi.org/10.1007/978-3-642-13562-0_13. Accessible full-text mirror: https://paperzz.com/doc/7670913/binary-de-bruijn-partial-words-with-one-hole.
2. Y. Orenstein, Y. W. Yu, and B. Berger, *Joker de Bruijn: Covering k-Mers Using Joker Characters*, Journal of Computational Biology 25 (2018), 1171-1178; DOI: https://doi.org/10.1089/cmb.2018.0032; PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC6247992/.
3. H. Z. Q. Chen, S. Kitaev, T. Mütze, and B. Y. Sun, *On Universal Partial Words*, arXiv:1601.06456 (initial version 2016), https://arxiv.org/abs/1601.06456.
4. D. Fillmore, B. Goeckner, R. Kirsch, K. Martin, and D. McGinnis, *The Existence and Structure of Universal Partial Cycles*, arXiv:2310.13067 (initial version 2023), https://arxiv.org/abs/2310.13067.
