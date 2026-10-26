# Parity-sharp voting times and maximal-delay census for lollipop majority dynamics

## Finding
For integers \(m\ge3\) and \(\ell\ge2\), attach one end of a path of \(\ell\) new vertices to a distinguished vertex of a clique \(K_m\), forming a lollipop graph \(L_{m,\ell}\). Let every vertex synchronously take the strict majority of its *open* neighbors, retaining its own bit on ties. If \(F\) is the resulting map, define the first periodic-entry time
\[
\tau(s)=\min\{t\ge0:F^{t+2}(s)=F^t(s)\}.
\]
The exact sharp maximum and the number of labelled configurations attaining it are
\[
\boxed{\max_s\tau(s)=\begin{cases}\ell+2,&m\text{ odd},\\\ell+1,&m\text{ even},\end{cases}\qquad
\#\{s:\tau(s)=\max\tau\}=\begin{cases}
2\binom{m-1}{(m-1)/2},&m\text{ odd},\\
2^{m-1},&m\text{ even}.
\end{cases}}
\]
For odd \(m\), every trajectory becomes fixed. For even \(m=2k\), the **only** primitive two-periodic configurations have exactly \(k\) ones among the distinguished clique vertex and its \(m-1\) clique mates, and the pendant path alternates starting with the bit opposite to that of the distinguished vertex. Every such state is already two-periodic at time zero, and their number is \(2\binom{m-1}{k}\); all other states eventually become fixed.

The exact proportions of uniformly chosen initial states reaching the maximal delay are \(2^{-\ell}\binom{2k}{k}/2^{2k}\) when \(m=2k+1\), and \(2^{-\ell-1}\) when \(m\) is even. At fixed \(\ell\), the first decays as \(2^{-\ell}/\sqrt{\pi k}\) as \(k\to\infty\), while the second is independent of clique size.

## Assumptions and scope
All graphs are finite, simple, loopless and labelled. The clique has \(m\) vertices, one hub \(v\) connected to the path \(u_1,\dots,u_\ell\) through the single edge \(vu_1\). Denote the other \(q=m-1\) clique vertices by \(S\), their initial number of ones by \(a\), the hub bit by \(h\), and path bits by \(x_1,\dots,x_\ell\). No randomness, asynchronous updating, or tie-breaking coins are used. The definition of \(\tau\) includes periodic states at time zero; for a fixed-point trajectory it is the first time the full configuration becomes constant.

For completeness, the configurations at the maximal delay can be specified without simulation. For odd \(m=2k+1\), they satisfy \(a=k\) and the path word is strictly alternating, starting at \(x_1=1-h\). For even \(m=2k\), they form two disjoint classes:

1. **Unbalanced clique:** either \(h=0,\ a\ge k+1\), or \(h=1,\ a\le k-2\); the path alternates starting with \(1-h\).
2. **Critical clique:** \(a+h=k\), the path begins with \(1-h\), its first \(\ell-1\) positions alternate, and the final bit repeats the penultimate bit, \(x_\ell=x_{\ell-1}\). The condition on the alternating prefix is vacuous for a one-bit prefix.

## Proof
**1. The clique transition.** At any time \(t\), write \(a_t\) for the number of ones among the \(m-1\) ordinary clique vertices, \(h_t\) for the hub bit, and \(y_t=x_1(t)\). For an ordinary clique vertex currently equal to \(b\), the number of its one-valued neighbors is \(a_t-b+h_t\). The hub sees \(a_t+y_t\) ones among \(m\) neighbors. Consequently, when \(m=2k+1\) the ordinary clique vertices all become the same bit
\[
c=\mathbf 1_{\{a_0+h_0\ge k+1\}}
\]
after one update. This unanimous state persists (each ordinary vertex has \(2k-1\) agreeing clique neighbors). At time two the hub must equal \(c\), regardless of the path, since its \(2k\) ordinary clique neighbors already agree. The hub and ordinary clique vertices then remain \(c\).

When \(m=2k\), the ordinary clique vertices at the next step are all zero if \(a_t+h_t<k\), all one if \(a_t+h_t>k\), and the bitwise complement of their current vector if \(a_t+h_t=k\). In the first two cases the hub also becomes the same unanimous bit \(c\) immediately, because its \(2k\) neighbors include the \(2k-1\) ordinary clique vertices and one path vertex. This clique consensus persists. In the critical case \(a_t+h_t=k\), the hub's next bit is exactly \(y_t\): if \(h_t=0\), then \(a_t=k\) and the hub is one precisely when \(y_t=1\); if \(h_t=1\), then \(a_t=k-1\), and the hub is zero precisely when \(y_t=0\). These conclusions include the ties with retained hub bit.

**2. Frozen pairs and fronts on the path.** For \(1\le j<\ell\), the path update is the three-input majority of \(x_{j-1},x_j,x_{j+1}\), with \(x_0=h\); the endpoint obeys \(x_\ell(t+1)=x_{\ell-1}(t)\). Two equal adjacent *path* bits remain permanently equal and unchanged: at each member of the pair an agreeing neighbor prevents a flip, including at the endpoint. A frozen pair propagates one vertex per round into a neighboring alternating stretch: a neighboring opposite bit flips to the pair's value, unless it already has an equal neighboring bit, in which case it was frozen anyway. Thus any path vertex at distance \(d\) from an initially equal adjacent path pair is frozen by time \(d\), unless another frozen pair reaches it sooner.

Likewise, if the hub is fixed to \(c\) from time \(s\), the path vertices \(x_j\) are fixed by time \(s+j\). Inductively, if \(x_j\) has no agreeing neighbor at the previous time it flips and becomes equal to the already-fixed left neighbor; if it does have an agreeing neighbor, it is already part of a permanent equal pair. The same statement holds at the terminal vertex using its copying rule.

**3. Odd cliques and their unique maximal-delay pattern.** Part 1 fixes the hub by time two, and Part 2 fixes every path vertex by time \(\ell+2\). An initially equal pair \(x_j=x_{j+1}\) shortens this bound: the prefix to its left freezes by time at most \(2+j-1\), while the suffix to its right is frozen by time at most \(\ell-(j+1)\). Both are strictly smaller than \(\ell+2\). Hence maximal delay requires an initially strictly alternating path.

If initially \(x_1=h\), the first path update creates an equal path pair \(x_1=x_2\) (since \(x_1\) is retained while \(x_2\) flips), excluding maximal delay. Thus \(x_1=1-h\), and all path bits flip in the first update. To avoid an equal pair in the next update one must have \(h_1=1-h\); then all path bits flip again and \(x_1(2)=1-h\). To obtain the last possible time \(\ell+2\), one must also have \(h_2=c=h\), rather than \(h_2=x_1(2)\). From the hub majority rule with \(y_0=1-h\), \(h_1=1-h\) means \(a\ge k\) when \(h=0\) and \(a\le k\) when \(h=1\). The condition \(c=h\) means \(a\le k\) when \(h=0\) and \(a\ge k\) when \(h=1\). Thus necessarily \(a=k\), for either value of \(h\). Conversely these conditions make the path strictly alternating through time two, with fixed hub \(c=h\) from then on. The fixed hub's front reaches the last path vertex for the first time at \(\ell+2\). Counting the choices of the \(k\) initial one-bits in the \(2k\) ordinary clique vertices and the two hub choices gives \(2\binom{2k}{k}\).

**4. Even cliques outside the critical threshold.** If \(a+h\ne k\), Part 1 fixes the hub and ordinary clique vertices from time one. Therefore \(\tau\le\ell+1\). An initial equal path pair shortens this time. If the path initially alternates, its first update remains alternating only when \(x_1\ne h\). The boundary front starts as late as time one exactly when the consensus bit \(c\) is opposite the original hub bit \(h\), so the post-update path still alternates away from the hub. The possibilities are \(h=0,a\ge k+1\) and \(h=1,a\le k-2\), with the path alternating from \(1-h\). Conversely these conditions keep every path position unfrozen until the left front reaches it, precisely at update \(\ell+1\).

**5. Even cliques at the critical threshold.** Suppose \(a+h=k\). If \(x_1=h\), then both the hub and \(x_1\) remain equal to \(h\), and the ordinary clique vertices become unanimous \(h\) by time two. Thus \(\tau\le\max\{2,\ell\}<\ell+1\). Suppose instead \(x_1=1-h\). If the entire path is alternating, each tail vertex flips, the ordinary clique vector complements, and the hub takes the opposite bit. The new clique again satisfies the critical equality, so the *entire state* is a primitive two-cycle from time zero.

Otherwise let \(p\), with \(1\le p\le\ell-1\), be the leftmost index for which \(x_p=x_{p+1}\) initially. The initial frozen pair spreads left through the otherwise alternating prefix, making \(x_1\) constant by time \(p-1\); it spreads right to freeze the rest of the path by time at most \(\ell-p-1\). Prior to the arrival at \(x_1\), the hub and ordinary clique vertices alternate bitwise each round and remain at the critical threshold. At time \(p-1\), the now-frozen \(x_1=c\) is opposite the current hub bit \(h'\): this follows immediately by alternating the prefix from the initial \(x_1=1-h\), noting that the propagated frozen color is the initial \(x_p\). The core then follows the exact three-step sequence
\[
(a',h',c)=(k-h',h',1-h')
\ \longrightarrow\ (k-1+h',1-h',c)
\ \longrightarrow\ (k-h',1-h',c)
\ \longrightarrow\ ( (2k-1)c,c,c),
\]
where the first coordinate is the ordinary-clique one-count. In the last step every ordinary clique vertex equals \(c\). Thus the full state is fixed by time
\[
\max\{p+2,\ell-p-1\}\le\ell+1.
\]
Equality with \(\ell+1\) is possible exactly for \(p=\ell-1\): the alternating prefix reaches the endpoint's equal pair only at the end, and the clique completes the displayed transition at time \(p+2=\ell+1\). This is precisely the critical maximal-delay word specified in the scope.

**6. Counting and cycles.** In the even case the critical maximal patterns contribute \(2\binom{2k-1}{k}\) states. The unbalanced patterns contribute \(2\sum_{j=k+1}^{2k-1}\binom{2k-1}{j}\) states. By binomial symmetry their sum equals
\[
2\sum_{j=k}^{2k-1}\binom{2k-1}{j}=2^{2k-1}=2^{m-1}.
\]
The only nonfixed recurrent orbits are the critical strictly alternating two-cycles in Part 5, with \(2\binom{2k-1}{k}\) labelled periodic states; no initial state outside that family joins a two-cycle later. All assertions follow. \(\square\)

## Verification
Run the accompanying standalone script `verify.py` using Python 3. It independently constructs every graph's adjacency lists, computes synchronous neighbour majorities directly for every labelled binary configuration in the finite test range, finds exact functional-graph preperiods and primitive periods, and compares the theorem's maximal-time formula, extremal descriptions and periodic-two descriptions point by point. It checks all \(53\) pairs with \(3\le m\le8\), \(2\le\ell\le10\) and \(m+\ell\le17\), covering \(768{,}032\) initial states. The output is recorded in `verification_output.txt`. These finite checks corroborate but do not replace the all-size proof above.

## Relationship to prior work
Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519v1, 14 August 2015), §§1 and 3 and its appendices, establish general voting-time bounds using graph modules and illustrate how clique symmetry affects convergence. Their graph-uniform estimate does not give the parity-dependent sharp lollipop value, terminal-layer multiplicity or explicit two-cycle classification. Mertzios, Nikoletseas, Raptopoulos and Spirakis (arXiv:1404.7671v1, 30 April 2014), §5.3, use precisely a clique joined to a line as an interaction graph for a **stochastic three-state pairwise population protocol**. Their probabilistic absorption statements do not imply this deterministic synchronous binary transition theorem. Classical finite-graph period-at-most-two results are used only as context; the present proof independently establishes all actual periodic-state possibilities on this family. Related exact studies of circular Rule-232 majority and of a bridge between two cliques concern different boundary systems and do not imply the two propagation mechanisms or the stated extrema for a single clique with a terminal copying endpoint.

## Limitations
The graph is a one-clique lollipop with \(m\ge3\) and \(\ell\ge2\); the cases \(\ell=1\), more than one attachment, alternative tie conventions, asynchronous updates, weighted edges and probabilistic sampling are not claimed. The count concerns labelled bit assignments, not configuration classes modulo graph automorphisms. An overlap search is not a proof of historical uniqueness; an unindexed equivalent statement remains possible. No independent audit is claimed.

## References
1. D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1 (first public version 2015-08-14), https://arxiv.org/html/1508.03519v1.
2. G. B. Mertzios, S. E. Nikoletseas, C. L. Raptopoulos, P. G. Spirakis, *Determining Majority in Networks with Local Interactions and very Small Local Memory*, arXiv:1404.7671v1 (first public version 2014-04-30), https://arxiv.org/abs/1404.7671.
3. S. Frischknecht, B. Keller, R. Wattenhofer, *Convergence in (Social) Influence Networks*, DISC 2013, DOI:10.1007/978-3-642-41527-2_30 (general majority convergence context).
