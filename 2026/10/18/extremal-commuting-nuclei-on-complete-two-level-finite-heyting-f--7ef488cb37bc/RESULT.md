# Extremal commuting nuclei on complete two-level finite Heyting frames

## Finding
For integers \(r,s\geq 2\), let \(P_{r,s}=R\sqcup T\) be the finite poset with \(|R|=r\), \(|T|=s\), both levels antichains, and \(b<t\) for every \(b\in R\) and \(t\in T\). Let \(H_{r,s}=\operatorname{Up}(P_{r,s})\), the Heyting algebra of upward-closed sets. A *nucleus* on \(H_{r,s}\) is an extensive, monotone, idempotent self-map preserving finite meets. A family *commutes* if every pair of its nuclei commutes under function composition.

**Theorem.** The \(2^{r+s}\) nuclei are uniquely indexed by \((B,A)\in\mathcal P(R)\times\mathcal P(T)\), with the explicit maps \(j_{B,A}\) given below. Two such nuclei commute if and only if
\[
 B\setminus D\ne\varnothing\ \Longrightarrow\ C\subseteq A,
 \qquad
 D\setminus B\ne\varnothing\ \Longrightarrow\ A\subseteq C
\]
for \(j_{B,A}\) and \(j_{D,C}\). Every pairwise-commuting family has at most
\[
\boxed{2^r+2^s-1}
\]
members. **Exactly two families attain this upper bound**, namely
\[
 \mathcal E_-=\{j_{B,\varnothing}: B\subseteq R\}\cup
 \{j_{R,A}:A\subseteq T\},
 \quad
 \mathcal E_+=\{j_{B,T}:B\subseteq R\}\cup
 \{j_{\varnothing,A}:A\subseteq T\}.
\]
The exact number of ordered commuting pairs, including equal pairs, is
\[
\boxed{N_{r,s}=2^r4^s+2(3^r-2^r)3^s+(4^r-2\cdot3^r+2^r)2^s}.
\]
For independently uniform nuclei, the commutation probability is \(N_{r,s}/4^{r+s}\). In the balanced regime,
\[
 \Pr(\text{commute in }H_{n,n})\sim 2(9/16)^n.
\]
Here "exactly two" concerns families of **maximum cardinality**, not all inclusion-maximal families.

## Assumptions and scope
All levels and elements of \(P_{r,s}\) are labelled, and \(r,s\) are positive integers with \(r,s\ge 2\). The order has **every** lower-to-upper relation and no relations within either level. The Heyting meet on \(H_{r,s}\) is set intersection. There is no preservation-of-joins assumption on a nucleus. Families consist of distinct functions (not multisets), while ordered pairs include repetitions. No statement is made for arbitrary finite posets, higher-level weak orders, or general closure operators failing meet preservation.

Write \(U_R=U\cap R\) and \(U_T=U\cap T\). For \(B\subseteq R\) and \(A\subseteq T\), define
\[
 j_{B,A}(U)=\{x\in P_{r,s}: (B\cup A)\cap\uparrow x\subseteq U\}.
\]
This is upward closed. Its top part and bottom-membership rule are
\[
 j_{B,A}(U)\cap T=U_T\cup(T\setminus A),
\]
\[
 b\in j_{B,A}(U)\ \Longleftrightarrow\
 \bigl(b\in B\ \text{and}\ b\in U\bigr)
 \ \text{or}\ \bigl(b\notin B\ \text{and}\ A\subseteq U_T\bigr).
\]

## Proof
**1. Complete normal form.** For any subset \(S\) of a finite poset \(P\), the map
\[
 j_S(U)=\{x:\uparrow x\cap S\subseteq U\},\qquad U\in\operatorname{Up}(P),
\]
is extensive and monotone, preserves intersections, and is idempotent: \(j_S(U)\cap S=U\cap S\). The finite-poset subset-to-nucleus bijection is the established Lindenhovius theorem (applied to the opposite order; see references), with an explicit inverse discussed by Ochs. Hence these maps exhaust all nuclei, and distinct \(S\)'s give distinct maps. Taking \(S=B\sqcup A\) gives the displayed normal form and \(2^{r+s}\) operators. The top and bottom formulas follow by using \(\uparrow t=\{t\}\) for \(t\in T\) and \(\uparrow b=\{b\}\cup T\) for \(b\in R\).

**2. Composition criterion.** The top part of either composite \(j_{B,A}\circ j_{D,C}\) or \(j_{D,C}\circ j_{B,A}\) equals \(U_T\cup(T\setminus(A\cap C))\). If \(b\in B\cap D\), both composites contain \(b\) exactly when \(b\in U\); if \(b\notin B\cup D\), both contain \(b\) exactly when \(A\cap C\subseteq U_T\). For \(b\in B\setminus D\), the first contains \(b\) precisely when \(C\subseteq U_T\) while the second contains \(b\) precisely when \(A\cap C\subseteq U_T\). These agree for every upward-closed \(U\) exactly when \(C\subseteq A\), since every subset of \(T\) is itself an upward-closed set. Exchanging \((B,A)\) and \((D,C)\) treats \(b\in D\setminus B\). This proves the if-and-only-if criterion without discarding any case of \(U\) that contains lower points.

Equivalently, if both bottom coordinates and both top coordinates differ, the coordinates must be strictly comparable in the **same** direction. In particular, if \(B\) and \(D\) are incomparable, then compatibility forces \(A=C\).

**3. The forest bound.** Represent a commuting family \(\mathcal F\) as a bipartite graph \(G(\mathcal F)\) with left vertices all \(2^r\) subsets of \(R\), right vertices all \(2^s\) subsets of \(T\), and one edge \((B,A)\) per operator. For two edges with different left and different right endpoints, compatibility forces the endpoints in both Boolean lattices to be strictly comparable, in the same direction. Consequently, any matching gives an order-preserving bijection between two finite chains consisting of its left and right endpoints.

Suppose that \(G(\mathcal F)\) contained a cycle. Its two alternating perfect matchings are distinct bijections on the **same** sets of left and right vertices. Each must be an increasing bijection between the same two finite total orders, but such a bijection is unique. Contradiction. Hence the graph is a forest. It has \(2^r+2^s\) vertices, so it has at most \(2^r+2^s-1\) edges.

**4. All equality cases.** The displayed families \(\mathcal E_-\) and \(\mathcal E_+\) satisfy the composition criterion and each has \(2^r+2^s-1\) distinct members. Conversely, a commuting family attaining the bound has a spanning tree as its bipartite graph.

For \(r\ge 2\), every nonempty proper subset \(B\subsetneq R\) has another such subset incomparable with it. The incomparability graph on all nonempty proper subsets is connected: each \(B\) is incomparable with some singleton \(\{b\}\) for \(b\notin B\), and distinct singletons are mutually incomparable. Whenever two left vertices are incomparable, all edges incident to either must have the **same** right endpoint; hence they are both leaves. Connectivity of that incomparability graph forces every nonempty proper left subset to be a leaf joined to one common right vertex \(A_0\).

Every other right vertex can then be incident only to the two exceptional left vertices \(\varnothing\) and \(R\). Compatibility with the edges \((B,A_0)\), for nonempty proper \(B\), forces any right neighbor \(A\) of \(\varnothing\) to satisfy \(A\subseteq A_0\), and any right neighbor \(A\) of \(R\) to satisfy \(A_0\subseteq A\). Because the tree spans **all** right vertices, every subset of \(T\) must be comparable with \(A_0\). In a Boolean lattice, that happens only when \(A_0=\varnothing\) or \(A_0=T\) (the assumption \(s\ge2\) ensures that a nontrivial proper subset has an incomparable subset). In the first case, the edges incident to \(\varnothing\) can only meet \(\varnothing\) on the right, while every other right vertex must meet \(R\); connectedness supplies the edge \((R,\varnothing)\), giving exactly \(\mathcal E_-\). The second case symmetrically gives \(\mathcal E_+\). Thus equality has exactly these two realizations.

**5. Ordered-pair census.** Classify ordered pairs \((B,D)\) of bottom subsets. There are \(2^r\) equal pairs, \(2(3^r-2^r)\) strictly comparable pairs (in either orientation), and \(4^r-2\cdot3^r+2^r\) incomparable pairs. The top-coordinate choices \((A,C)\) allowed by the criterion number respectively \(4^s\), \(3^s\), and \(2^s\). Multiplication and addition give the formula for \(N_{r,s}\). For \(r=s=n\), division by \(4^{2n}\) yields
\[
 \Pr(\text{commute})=2(9/16)^n+2(1/2)^n-4(3/8)^n+(1/4)^n,
\]
which has the asserted asymptotics because \(9/16>1/2>3/8>1/4\).

## Verification
The standalone `verify.py` uses two two separately specified descriptions of the nuclei: direct upper-cone evaluation on **all upsets** and the proposed bitset compatibility rule. It checks the defining nucleus identities, equality of direct and predicted pairwise commutation, and the exact ordered-pair formula for \((r,s)=(2,2),(2,3),(3,2),(3,3)\). It finds all maximal commuting cliques by a separate Bron–Kerbosch search, confirming the extremal sizes and exactly two maximizers. For \((2,2)\), it additionally enumerates all meet-closed fixed-point families of the Heyting lattice and recovers precisely the \(16\) nuclei, without assuming the subset normal form. Run `python verify.py` with Python 3; the expected final line is `VERIFY_OK`. These are **finite checks**, not proofs for arbitrary \(r,s\); the all-parameter proof appears above.

The checked ordered-pair totals are \(162\), \(542\), \(542\), and \(1682\), respectively. The maximum-family sizes are \(7\), \(11\), \(11\), and \(15\).

## Relationship to prior work
Lindenhovius establishes the bijection between subsets of a finite poset and nuclei on its frame of downsets. Ochs gives the inverse formula explicitly (use the opposite poset for the present upset convention). Hemelaer studies cardinalities of Grothendieck-topology families, and Escardó studies composition of prenuclei and joins of nuclei. None of those inspected portions gives the present simultaneous commutation criterion, bipartite-forest extremal argument, two unique maximizers, or ordered-pair census for complete two-level frames. This is a claim about implications of inspected results, not a claim that all historical literature has been exhausted.

A previously obtained rooted-star classification treats one lower point, whereas the present theorem requires \(r\ge2\). Merely substituting into that one-root result cannot yield the behavior of incomparable bottom subsets, which is the basis of the forest and uniqueness arguments here. The general subset-to-nucleus bijection is **not** claimed as new.

## Limitations
The classification of **all inclusion-maximal** commuting families is not attempted; only the exact maximum size and its equality cases are established. General height-two posets lacking all cross-relations, higher weak-order levels, and non-meet-preserving closure maps are not covered. Finite computer checks support but do not certify the infinite statements. An earlier equivalent commutation-graph result under alternative terminology remains possible; the literature comparisons do not amount to an independent audit.

## References
1. E. Ochs, *On a formula that is not in "Grothendieck Topologies in Posets"*, arXiv:2107.08501, first posted 2021-07-18, https://arxiv.org/abs/2107.08501. Relevant material: pp. 1–4, the explicit nucleus-to-subset inverse.
2. A. J. Lindenhovius, *Grothendieck topologies on a poset*, arXiv:1405.4408, first posted 2014-05-17, https://arxiv.org/abs/1405.4408. Relevant material: Appendix C, Theorem C.4, pp. 74–76.
3. J. Hemelaer, *Grothendieck topologies on posets*, arXiv:1811.10039, first posted 2018-11-25, https://arxiv.org/abs/1811.10039. Relevant material: Sections 3 and 6.
4. M. H. Escardó, *Joins in the frame of nuclei*, https://martinescardo.github.io/papers/hmj.pdf. Relevant material: Sections 1 and 3, nuclear composition and joins.
