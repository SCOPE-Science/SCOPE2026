# A sharp seven-patch threshold for protecting one surviving habitat link

## Finding
Let \(T=(V,E)\) be any finite, simple, unweighted tree with \(n=|V|\ge2\). One habitat patch \(v\in V\) is protected permanently; each other patch survives independently with the same probability \(p\in(0,1)\). Denote by \(R_v(p)\) the probability that at least one edge has **both** endpoints surviving. Such an edge represents a minimally surviving local opportunity for dispersal or interaction, not a claim about long-term ecological persistence.

**Theorem.** For every tree with \(2\le n\le6\), there is a vertex maximizing \(R_v(p)\) simultaneously for all \(0<p<1\). At \(n=7\), exactly one tree up to isomorphism fails to admit any such universal protected vertex: the spider with a degree-three center and three arms of two edges each. Its unique optimum change occurs at \(\alpha=(\sqrt5-1)/2\). This order threshold is sharp.

For the exception take vertices \(\{0,1,2,3,4,5,6\}\) and edges \(\{01,03,05,12,34,56\}\). Vertex \(0\) is the center. The optimum is vertex \(0\) for \(p<\alpha\), any of vertices \(1,3,5\) for \(p>\alpha\), and any of \(0,1,3,5\) at equality. All leaves are inferior for all interior probabilities. Explicitly,
\[
R_0(p)=1-(1-p)^3,\quad R_1(p)=R_3(p)=R_5(p)=1-(1-p)^4(1+p)^2,
\]
\[
R_0(p)-R_1(p)=p(1-p)^3(1-p-p^2).
\]

## Assumptions and scope
The edge set is fixed and perfectly traversable when both endpoints survive. Each nonprotected vertex survives independently with identical \(p\), and exactly one vertex is forced to survive. The random surviving subgraph may be disconnected. Success is the **existence of at least one adjacent surviving pair**, not connectivity of *all* surviving vertices, expected component size, or persistence of a metapopulation through time. The result is a theorem of finite stochastic network structure, not a field-data prediction.

## Proof
Put \(q=1-p\), \(t=p/q>0\), and for any graph \(H\) define the independence polynomial
\[
I(H;t)=\sum_{S\subseteq V(H):\, S\text{ independent}} t^{|S|}.
\]
If \(v\) is protected, absence of any surviving edge forces all neighbors of \(v\) to fail. Among the remaining vertices in \(T-N_T[v]\), the survivors must form an independent set. Thus the exact failure probability is
\[
1-R_v(p)=q^{n-1}I(T-N_T[v];t).\tag{1}
\]
Here \(N_T[v]\) is the closed neighborhood. Indeed, for an independent set \(S\) of the complement the probability of exactly that survivor set is \(p^{|S|}q^{n-1-|S|}\). Equation (1) follows by summing. The factor \(q^{n-1}\) is independent of the protected vertex, so the optimal protected vertices minimize \(I(T-N_T[v];t)\) for positive \(t\).

For each \(2\le n\le7\), the accompanying verifier enumerates **every labeled tree**, using all \(n^{n-2}\) Prüfer words of length \(n-2\) and the deterministic inverse Prüfer construction. For every constructed tree it exactly enumerates the independent vertex subsets of each induced graph \(T-N_T[v]\). Its coefficient vector \(c_v=(c_{v,0},\ldots,c_{v,n-1})\) consists of nonnegative integers. If one vertex \(v\) has \(c_{v,k}\le c_{w,k}\) for every vertex \(w\) and all indices \(k\), it is uniformly optimal by (1).

The exhaustive integer comparison proves that all \(1+3+16+125+1296=1441\) labeled trees with orders two through six admit such a coefficientwise-minimal vertex. At order seven, exactly \(15967\) of the \(16807\) labeled trees also do so. For every one of the remaining \(840\) trees, a direct structural test finds one degree-three center adjacent to three degree-two vertices, each with its own leaf. Hence all \(840=7!/6\) exceptions are labelings of a **single** unlabeled tree. No claim that absence of coefficient dominance always implies a probability crossover is needed: the sole exceptional class is analyzed next.

For that spider, the center has three isolated residual vertices, so
\[
I(T-N_T[0];t)=(1+t)^3.
\]
For each arm-neighbor, the residual graph is two disjoint edges, so
\[
I(T-N_T[1];t)=(1+2t)^2.
\]
For each leaf, the residual forest has independence polynomial \(1+5t+6t^2+t^3\), coefficientwise larger than the arm-neighbor polynomial. The difference between the first two independent-set polynomials is
\[
(1+t)^3-(1+2t)^2=t(t^2-t-1),
\]
which crosses exactly once for \(t>0\), at \(t=(1+\sqrt5)/2\). Under \(t=p/(1-p)\), this is precisely \(p=(\sqrt5-1)/2\). Substituting into (1) gives the displayed success probabilities and their signed difference. This proves both uniqueness and strict optimality on the two sides of the threshold, completing the sharp classification.

The Prüfer inverse is complete: each word corresponds to exactly one labeled tree, and deleting the smallest available leaf gives the inverse encoding. Thus this is a finite exhaustive proof rather than a probabilistic or sampled assertion.

## Verification
The standalone standard-library program `verify.py` recomputes the complete labeled-tree census and checks every root's independent-set coefficient vector. It asserts the absence of non-dominated trees through six vertices, verifies the exact count \(840\) at seven, and verifies that every such case has the subdivided three-star structure and the three displayed polynomial types. A second implementation directly enumerates the \(2^6\) survival patterns of the explicit seven-patch witness at rational probabilities \(1/4,1/2,3/4,9/10\), checking the derived formula exactly with fractions. `certificate.json` records the deterministic output. Run `python3 verify.py > reproduced.json` and compare `reproduced.json` with `certificate.json` byte-for-byte. The finite classification is exhaustive through order seven only; the theorem does not extrapolate it to larger trees.

## Relationship to prior work
Gilbert, Gonzalez and Evans-Freke (1998) provide experimental motivation for the ecological relevance of corridors between surviving habitat patches; their experimental design and outcomes do not examine this exact single-patch stochastic protection objective. Levit and Mandrescu (2002) develop independence-polynomial identities and the combinatorics of well-covered spiders, but their mathematical conclusions concern unimodality and related graph transformations, not uniform choice of a protected vertex or the present seven-patch cutoff. Goldschmidt, Jaillet and Lasota (1994) study *all-survivors-connected* node reliability among graph designs, rather than existence of **some** surviving adjacent pair after protecting one vertex. Amin, Siegrist and Slater (1993) study the *expected number* of connected pairs and graph-design comparisons, not this binary event or vertex intervention. These different random variables do not imply the present sharp statement without additional arguments.

## Limitations
The model captures minimal structural functionality, not ecological resilience, migration rate, colonization, total patch occupancy, or actual viability. It assumes equal independent survival for all unprotected sites and an infallible intervention. The full publisher texts of two older graph-reliability articles were not accessible, so undiscovered equivalent prior results remain a bibliographic risk. The present classwise census is limited to \(n\le7\); no uniqueness claim about larger-order trees is made. 

## References
- Gilbert, F., Gonzalez, A., and Evans-Freke, I. (1998). *Corridors maintain species richness in the fragmented landscapes of a microecosystem*. Proceedings of the Royal Society B **265**, 577–582. DOI: 10.1098/rspb.1998.0333. Full text: https://ecology.nottingham.ac.uk/~plzfg/pdf%20files/1998%20Gilbert%20et%20al_moss%20patches.pdf
- Levit, V. E., and Mandrescu, E. (2002). *On Unimodality of Independence Polynomials of some Well-Covered Trees*. arXiv:math/0211036. https://arxiv.org/pdf/math/0211036
- Goldschmidt, O., Jaillet, P., and Lasota, R. (1994). *On reliability of graphs with node failures*. Networks **24**, 251–259. DOI: 10.1002/net.3230240407 (publisher abstract inspected).
- Amin, A. T., Siegrist, K. T., and Slater, P. J. (1993). *On uniformly optimally reliable graphs for pair-connected reliability with vertex failures*. Networks **23**, 185–193. DOI: 10.1002/net.3230230306 (abstract inspected).
