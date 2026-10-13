# Cycle convexity on cactus graphs is a binary matroid closure

## Finding
For every finite, simple, connected cactus graph \(G=(V,E)\) with \(|V|\ge 3\), let \(\mathcal C\) be its set of cycle blocks and \(k=|\mathcal C|=|E|-|V|+1\). Define
\[
Q_G=\mathbf F_2^{V}/\operatorname{span}_{\mathbf F_2}\left\{\sum_{v\in V(C)}e_v:C\in\mathcal C\right\},
\]
and denote the image of \(e_v\) in \(Q_G\) by \(\overline e_v\). Then the *entire cycle-convex hull operator* has the linear representation
\[
\operatorname{Hull}_{cc}(S)=\left\{v\in V:\overline e_v\in\operatorname{span}_{\mathbf F_2}\{\overline e_s:s\in S\}\right\}\quad(S\subseteq V).
\]
In particular it is the closure operator of a loopless binary representable matroid of rank \(|V|-k\), so the three cycle-convexity parameters satisfy
\[
\boxed{\operatorname{hn}_{\mathrm{Helly}}(G)=\operatorname{rn}_{\mathrm{Radon}}(G)=\operatorname{rk}_{cc}(G)=|V|-k=2|V|-|E|-1.}
\]
Here the Helly and Radon symbols denote maximum sizes of Helly-independent and Radon-independent vertex sets, respectively, not the hull number or the usual geodetic invariant. Every basis of this matroid is simultaneously a maximum Helly-independent, Radon-independent and convexly independent set.

## Assumptions and scope
The graph is simple and connected, with every block a bridge or an induced cycle. A cactus may have arbitrarily many cycles sharing cut vertices or joined by bridge paths. A cycle-convex set \(S\) is closed under the operation that adjoins \(w\) if some simple cycle \(C\) satisfies \(V(C)\setminus S=\{w\}\); \(\operatorname{Hull}_{cc}(S)\) is its iterative closure. A set \(S\) is convexly independent if \(s\notin\operatorname{Hull}_{cc}(S\setminus\{s\})\) for every \(s\in S\). It is Helly independent if \(\bigcap_{s\in S}\operatorname{Hull}_{cc}(S\setminus\{s\})=\varnothing\), and Radon independent if no partition into two disjoint nonempty sets has intersecting hulls. Empty intersections and degenerate cases follow the standard finite-set conventions; the asserted parameters are positive for the stated graph orders.

## Proof
**1. Independence of the cycle relations.** In a cactus every simple cycle is one of its cycle blocks. The bipartite incidence graph with nodes for cycle blocks and for vertices belonging to them, and an incidence edge for each membership, is a forest: an alternating incidence cycle would give a second route among blocks and hence a simple graph cycle using more than one block, contrary to the cactus property. Every nonempty collection of cycle nodes has a terminal cycle node in a component of this incidence forest. That terminal cycle has at least two vertices appearing in no other selected cycle (its size is at least three and it meets the other selected cycles in at most one vertex). Consequently, the sum of any nonempty collection of vectors \(r_C=\sum_{v\in C}e_v\) has at least two nonzero coordinates. In particular the \(k\) vectors \(r_C\) are linearly independent and no standard basis vector lies in their span. Therefore \(\dim Q_G=|V|-k\) and each \(\overline e_v\ne0\).

**2. Cycle closure is contained in linear closure.** For every cycle \(C\), the equality \(\sum_{v\in C}\overline e_v=0\) implies that a vertex of \(C\) belongs to the span of the remaining vertices. The linear closure in the displayed formula is consequently closed under every cycle-infection step. Monotonicity gives \(\operatorname{Hull}_{cc}(S)\subseteq\operatorname{cl}_Q(S)\).

**3. The reverse containment.** Let \(H=\operatorname{Hull}_{cc}(S)\). Suppose \(w\notin H\) but \(w\in\operatorname{cl}_Q(H)\). By the definition of the quotient, there is a set \(T\) of cycle blocks whose incidence-vector symmetric difference has support contained in \(H\cup\{w\}\) and contains \(w\). Use the incidence forest for \(T\). Discard all components not containing \(w\), which cannot affect its coefficient or introduce any coordinate outside \(H\cup\{w\}\). Root the remaining component at its vertex node \(w\) and take a cycle node \(C\) farthest from the root. It has one parent vertex \(z\) and no descendant cycle nodes. Thus every vertex of \(C\setminus\{z\}\) occurs in precisely one selected cycle and belongs to \(H\) (none equals \(w\)). Because \(H\) is cycle-convex, \(z\in H\). If \(z=w\), this contradicts \(w\notin H\). Otherwise all vertices of \(C\) lie in \(H\); remove \(C\) from \(T\). The remaining vector sum still has support contained in \(H\cup\{w\}\) and contains \(w\), because the changed coordinates all lie in \(H\). Repeating on the now-smaller rooted component eventually yields a cycle adjacent to \(w\) and the same contradiction. So every \(H\) is linearly closed, proving equality of the operators.

**4. Three independence parameters.** In any closure space, a Helly-independent set must be convexly independent: if \(s\in\operatorname{Hull}(S\setminus\{s\})\), then \(s\) belongs to all the hulls occurring in the Helly intersection. Similarly Radon independence implies convex independence by the partition \(\{s\}\cup(S\setminus\{s\})\). For a loopless linear-matroid closure, every linearly independent \(S\) is both Helly and Radon independent. Indeed, the intersection of the spans of the sets \(S\setminus\{s\}\), over all \(s\in S\), is \(\{0\}\), which contains no ground vector because \(\overline e_v\ne0\). Likewise, disjoint subsets of independent \(S\) span subspaces intersecting only at \(0\), so their convex hulls have empty intersection. Hence all three maximal sizes equal the matroid rank \(\dim Q_G=|V|-k\).

## Verification
The accompanying standard-library program `verify.py` constructs \(15\) cactus profiles, including forests, cycle bouquets, nonuniform cycle chains, branching cycle blocks, and two cycles connected via a bridge with a pendant vertex. It computes every iterative cycle hull and every binary-span closure by distinct methods, and exhaustively evaluates Helly, Radon and convex independence for all \(3576\) subsets. Running `python3 verify.py` reproduces the checks in `verification_output.txt`. These finite tests corroborate but do not replace the proof for arbitrarily large cactus graphs.

## Relationship to prior work
Nair, Anand, Chandran, Nascimento and Anil (first public 28 September 2026) introduce complexity and extremal classifications of the Helly number, Radon number and rank under cycle convexity, including the thresholds \(|V|-1\) and \(|V|-2\). Those classifications concern special extremal levels and do not imply an exact formula or closure representation for cactus graphs of unbounded cycle rank. Araújo, Araújo, Medeiros, Nisse and Silva (2026; with an earlier technical report cited therein) study cycle-convex rank on several graph classes, including forests, cycles and chordal graphs. Those results already cover special instances (such as forests and some bouquets), which are not individually claimed to be novel here. An available abstract of that work does not describe the general cactus matroid representation; its full technical report was not accessible for material comparison. The earlier cycle-convexity literature establishes the definition of the hull operation and related optimization problems, not this binary quotient identity in the material inspected.

## Limitations
The theorem assumes the cactus block property: the incidence-forest argument need not hold when cycles overlap in edges or create additional cycles across blocks. The matroid rank formula is not claimed for arbitrary connected graphs, and no general graph characterization of when cycle convexity is matroidal is proved. The novelty comparison is limited by inaccessible full text of one relevant technical report and by the possibility of unindexed equivalent results. No independently conducted audit is claimed.

## References
1. R. S. Nair, B. S. Anand, U. Chandran S. V., J. R. Nascimento and A. Anil, *Computing the Helly Number, Radon Number and Rank in Cycle Convexity*, arXiv:2609.34236v1, first posted 28 September 2026, https://arxiv.org/abs/2609.34236.
2. J. Araújo, S. N. Araújo, P. P. Medeiros, N. Nisse and C. Silva, *On the Rank and the General Position Number in Cycle Convexity*, IWOCA 2026, LNCS 16587, pp. 73–87, DOI:10.1007/978-3-032-27732-9_6, https://link.springer.com/chapter/10.1007/978-3-032-27732-9_6.
3. J. Araújo et al., *Cycle Convexity and the Tunnel Number of Links*, arXiv:2012.05656, https://arxiv.org/abs/2012.05656.
4. B. S. Anand et al., *The Complexity of Convexity Number and Percolation Time in the Cycle Convexity*, arXiv:2404.09236, https://arxiv.org/abs/2404.09236.
