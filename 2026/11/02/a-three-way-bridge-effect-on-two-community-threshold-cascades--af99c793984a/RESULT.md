# A three-way bridge effect on two-community threshold cascades

## Finding
For integers \(a,b\ge3\) and a common adoption fraction \(0<\phi\le1\), consider two communities that are complete graphs of orders \(a\) and \(b\). Compare the disconnected union \(G_0=K_a\sqcup K_b\) with \(G_1\), obtained by adding one edge between distinguished bridge vertices. Adopted vertices never revert; every unadopted vertex activates when at least a fraction \(\phi\) of its current neighbors are adopted.

Write \(F_G(z)=\sum_{S\subseteq V(G):\,S\,\mathrm{activates\ all}}z^{|S|}\). Thus \([z^k]F_G\) is the number of successful \(k\)-vertex initial sets, and its sum of coefficients counts all successful initial sets. For \(n\in\{a,b\}\), define
\[
 r_n=\lceil\phi(n-1)\rceil,\quad R_n=\lceil\phi n\rceil,\qquad
 D_n(z)=\sum_{k=r_n}^n\binom nk z^k,
\]
\[
 L_n(z)=\mathbf1_{\{R_n=r_n\}}\binom{n-1}{r_n-1}z^{r_n-1},\qquad
 H_n(z)=\mathbf1_{\{R_n=n\}}z^{n-1},\quad U_n(z)=D_n(z)-H_n(z).
\]
The exact full-cascade polynomial is
\[
\boxed{F_{G_1}(z)=U_a(z)U_b(z)+U_a(z)[L_b(z)+H_b(z)]+[L_a(z)+H_a(z)]U_b(z).}
\]
In comparison with the disconnected graph, \(F_{G_0}=D_aD_b\), the bridge has the coefficientwise identity
\[
\boxed{F_{G_1}-F_{G_0}=L_aU_b+L_bU_a-H_aH_b.}
\]
Consequently exactly one of the following holds:

1. **Beneficial:** If \(R_a=r_a\) or \(R_b=r_b\), the bridge creates successful seed sets and destroys none. The difference polynomial has nonnegative coefficients and is not zero. The minimum number of seeds for full activation drops from \(r_a+r_b\) to \(r_a+r_b-1\).
2. **Harmful:** If \(R_a=a\) and \(R_b=b\), the bridge destroys exactly one previously successful seed set and creates none: the two bridge vertices are unseeded and every other vertex is seeded. The difference polynomial is \(-z^{a+b-2}\). The minimum seed count remains \(r_a+r_b\).
3. **Neutral:** In every other case, the exact family of successful seed sets is unchanged by adding the bridge: \(F_{G_1}=F_{G_0}\), and the minimum seed count remains \(r_a+r_b\).

The cases are disjoint because \(r_n\le n-1\). Thus a single cross-community tie may help, have no effect, or hurt the probability of full adoption, with the sign determined exactly by whether its endpoint's adoption requirement is unchanged or becomes the entire neighborhood.

## Assumptions and scope
Both cliques have order at least three, and \(\phi\) is a fixed real number with \(0<\phi\le1\). At time zero an arbitrary labeled subset \(S\) is permanently activated. At each subsequent synchronous round, every inactive vertex with at least \(\lceil\phi\deg(v)\rceil\) active neighbors activates. Because the process is progressive on a finite graph, it reaches a fixed point in finitely many rounds. The closure is independent of any fair order of asynchronous updates, but the theorem counts only the eventual closure, not its completion time.

The two graphs have exactly the same labeled vertex set and the same adoption fraction; their degrees, and hence their integer thresholds, are recomputed after adding the bridge. The random-seeding interpretation is optional: under independent Bernoulli seeding with probability \(p\in(0,1)\), full-adoption probability equals \((1-p)^{a+b}F_G(p/(1-p))\).

## Proof
**1. Isolated community.** A vertex of \(K_n\) has degree \(n-1\) and threshold \(r_n\). If a seed set contains at least \(r_n\) vertices, all remaining vertices activate at the next round. If it contains fewer than \(r_n\), no activation is possible. Therefore \(D_n\) is precisely the success polynomial for an isolated clique.

**2. Local classification with one external neighbor.** Fix a community of order \(n\). Let \(x\) denote the number of seeded ordinary (nonbridge) vertices and \(g\in\{0,1\}\) the seeded status of its bridge vertex. A nonbridge vertex has threshold \(r=r_n\), while the bridge vertex has threshold \(R=R_n\); \(R-r\in\{0,1\}\). If \(g=1\), the community fills precisely when \(x\ge r-1\). If \(g=0\) and \(x\ge r\), all ordinary vertices fill; its bridge vertex then activates without external help exactly when \(R\le n-1\). If \(g=0\) and \(x<r\), neither an ordinary vertex nor the bridge vertex can activate without external help.

A permanently active external bridge vertex can rescue such a locally stalled community in exactly two mutually exclusive cases: (i) \(R=r\), \(g=0\), \(x=r-1\), in which the external neighbor activates the bridge vertex and then the ordinary vertices; or (ii) \(R=n\), \(g=0\), \(x=n-1\), in which all ordinary vertices are already seeds and the external neighbor activates the last vertex. Here \(R=n\) implies \(r=n-1\), because \(0<\phi\le1\). No other local configuration can be rescued: if \(g=1\) with \(x<r-1\), the ordinary vertices remain below threshold, and if \(g=0\) with \(x<r\), the external neighbor can first activate the bridge only if \(x+1\ge R\), forcing case (i), except for the all-ordinary-seeded case (ii).

The locally *unassisted* configurations therefore have generating polynomial \(U_n=D_n-H_n\); the *externally rescuable but not unassisted* configurations have polynomial \(E_n=L_n+H_n\). The binomial factor in \(L_n\) chooses the \(r_n-1\) ordinary seeds, while \(H_n\) represents the unique set containing all ordinary vertices but not the gateway.

**3. Two-community closure.** Full activation occurs precisely when each community is either unassisted or externally rescuable, and at least one is unassisted. Indeed, an unassisted community eventually activates its own bridge vertex, enabling the other community if externally rescuable. Conversely, configurations outside those two classes cannot fully activate even with the external gateway permanently active. If both communities are externally rescuable but neither unassisted, neither bridge vertex is initially active and no internal process can create one; the two communities remain mutually blocked. This proves \(F_{G_1}=U_aU_b+U_aE_b+E_aU_b\).

**4. Exact bridge difference and sign.** Substitute \(E_n=L_n+H_n\) and \(U_n=D_n-H_n\), expand, and cancel to obtain \(F_{G_1}-D_aD_b=L_aU_b+L_bU_a-H_aH_b\). If at least one \(L_n\) is nonzero, the negative term vanishes because \(L_nH_n=0\). Both \(U_a,U_b\) are nonzero polynomials with nonnegative coefficients, so the difference is strictly coefficientwise nonnegative. Its smallest possible exponent is \(r_a+r_b-1\), achieved by the rescued community using \(r_n-1\) seeds and the other using \(r_m\) seeds. If neither \(L\) is nonzero, the difference is \(-H_aH_b\), either \(-z^{a+b-2}\) if both endpoint thresholds equal their degrees, or zero otherwise. The all-but-endpoints seed set is the sole lost configuration. When no \(L\) is present, every successful configuration contains at least \(r_a+r_b\) seeds and a suitable such configuration always exists (seed \(r_n\) vertices in each clique including each bridge vertex). This completes the classification.

## Verification
The included `verify.py` constructs both cliques and the bridge from their adjacency sets, exhaustively enumerates all seed sets, and iterates the actual synchronous fraction-threshold dynamics independently of the generating-polynomial formulas. It compares the full polynomial coefficient vectors, the three sign cases, and the sharp minimum seed sizes across \(16\) ordered pairs with \(3\le a,b\le6\) and \(46\) distinct rational fractions \(0<\phi\le1\). It also verifies the special six-vertex examples; this run passed \(2{,}211\) finite exact assertions. The proof above, not the finite enumeration, establishes the theorem for all real fractions and arbitrary clique sizes.

For example, if \(a=b=3\), at \(\phi=2/3\) one has \(r=R=2\), \(D=3z^2+z^3\), \(L=2z\), and \(F_{G_1}-F_{G_0}=4zD=12z^3+4z^4\). At \(\phi=1/2\) the bridge is neutral. At \(\phi=3/4\) one has \(r=2,R=3\) and the bridge deletes exactly one four-seed success: \(F_{G_1}-F_{G_0}=-z^4\).

## Relationship to prior work
Khoshkhah, Soltani, and Zaker (2012) define irreversible dynamic monopolies, discuss social-influence applications, and derive general degree/threshold bounds, not this two-community seed-set coefficient vector. Singh, Sreenivasan, Szymanski, and Korniss (2013) study seed size and clustering in fractional-threshold cascades, observing distinct community-level cascades; their model motivates the role of bridges, but their paper does not derive this exact comparison. Pei and colleagues (2017) study influence optimization and subcritical paths with message-passing methods, not an exact finite barbell seed polynomial. A separate result entitled *Zero forcing polynomial of bridge barbells* studies the same underlying two-clique graph but uses the zero-forcing color-change rule (a blue vertex with exactly one white neighbor), rather than fractional-neighbor irreversible threshold adoption; neither resulting polynomial determines the other. Earlier exact one-edge inhibition results for a single initiator over arbitrary connected graphs similarly do not determine the all-seed-size distribution here.

## Limitations
The result assumes two internally complete, homogeneous communities, one bridge, identical fixed fractional thresholds, permanent adoption, and deterministic eventual closure. It does not extend the formula to networks with several intercommunity ties, random edge failures, heterogeneous thresholds, adoption reversals, finite observation deadlines, or degree-preserving rewiring. Search and comparisons cannot exclude an unindexed equivalent enumeration. The finite verifier does not certify the infinite theorem independently, and no independent mathematical audit has been performed.

## References
1. K. Khoshkhah, H. Soltani, M. Zaker, *On dynamic monopolies of graphs: the average and strict majority thresholds*, arXiv:1202.1146v1 (6 February 2012), https://arxiv.org/abs/1202.1146.
2. P. Singh, S. Sreenivasan, B. K. Szymanski, G. Korniss, *Threshold-limited spreading in social networks with multiple initiators*, arXiv:1304.7034v1 (25 April 2013); Scientific Reports 3, 2330 (2013), https://arxiv.org/abs/1304.7034, https://doi.org/10.1038/srep02330.
3. S. Pei, X. Teng, J. Shaman, F. Morone, H. A. Makse, *Efficient collective influence maximization in cascading processes with first-order transitions*, Scientific Reports 7, 45240 (28 March 2017), https://doi.org/10.1038/srep45240.
