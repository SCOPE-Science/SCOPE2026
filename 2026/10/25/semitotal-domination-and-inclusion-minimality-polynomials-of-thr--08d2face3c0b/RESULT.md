# Semitotal-domination and inclusion-minimality polynomials of three-layer clique paths

## Finding
For each integer \(n\ge3\), let \(G_n=K_n\square P_3\). Let \(A\), \(B\), and \(C\) denote the subsets of column indices selected in the first, middle, and third complete-graph layers, respectively. The exact trivariate generating polynomial for semitotal dominating sets, with \(x,y,z\) recording the selected vertices in the three layers, is
\[
\begin{aligned}
\mathcal P_n(x,y,z)={}&((1+x)^n-1)((1+y)^n-1)((1+z)^n-1)\\
&+y^n((1+x)^n+(1+z)^n-1)\\
&+(x+z+xz)^n-x^n-z^n-n(xz^{n-1}+x^{n-1}z).
\end{aligned}
\]
Equivalently, the polynomial by total cardinality is
\[
\mathcal P_n(u)=((1+u)^n-1)^3+u^n(2(1+u)^n-2n-3)+(2u+u^2)^n.
\]
The polynomial counting *inclusion-minimal* semitotal dominating sets by cardinality is
\[
\mathcal M_n(u)=\begin{cases}
28u^3+12u^4,&n=3,\\
n^3u^3+(2^n-2n-1)u^n+2nu^{n+1},&n\ge4.
\end{cases}
\]
In particular, the semitotal domination number is \(\gamma_{t2}(G_n)=3\), the upper semitotal domination number is \(\Gamma_{t2}(G_n)=n+1\), and their gap is \(n-2\), unbounded as \(n\) grows. For \(n\ge5\), no inclusion-minimal semitotal dominating set has cardinality strictly between \(3\) and \(n\).

## Assumptions and scope
The graphs are finite, simple, undirected, and have the Cartesian-product adjacency: vertices \((i,\ell)\) and \((j,m)\) are adjacent exactly when \(\ell=m\) and \(i\ne j\), or when \(i=j\) and \(|\ell-m|=1\). Here \(1\le i,j\le n\) and \(\ell,m\in\{1,2,3\}\). A vertex set \(S\) is *semitotal dominating* if every vertex outside \(S\) has a neighbor in \(S\), and every vertex of \(S\) has a **different** vertex of \(S\) at distance at most two in the original graph. Inclusion-minimal means that deleting any one selected vertex destroys this property. An empty subset of indices is denoted \(\varnothing\), and \([n]=\{1,\ldots,n\}\).

## Proof
**Step 1: Full feasible-set classification.** If \(B\ne\varnothing\), all vertices in the middle layer are dominated. Unless \(A\ne\varnothing\), every first-layer vertex must be dominated by its own matched middle-layer vertex, forcing \(B=[n]\); likewise \(C=\varnothing\) forces \(B=[n]\). Conversely, either \(A,B,C\) are all nonempty, or \(B=[n]\), suffices for domination. It also suffices for the semitotal condition: when all three layers are met, each selected vertex is within distance at most two of a selected middle-layer vertex (and each middle-layer selection has an outer-layer partner); when \(B=[n]\), each selected middle vertex has another middle-layer partner because \(n\ge3\), and every outer selection has a middle-layer partner. The two cases are disjoint if the latter is restricted to at least one empty outer layer.

If \(B=\varnothing\), domination requires \(A,C\ne\varnothing\) and \(A\cup C=[n]\): without a selected middle vertex, each middle vertex needs the selected first- or third-layer vertex in its own column. Two first-layer vertices are mutually adjacent, as are two third-layer vertices; a selected first-layer and third-layer vertex are at distance two when their column indices coincide and at distance three otherwise. Thus the semitotal condition automatically holds if \(|A|,|C|\ge2\). If \(A\) is a singleton \(\{i\}\), it holds exactly when \(i\in C\); a symmetric condition applies to singleton \(C\). For \(n\ge3\), among nonempty pairs covering \([n]\), the only forbidden pairs are \((A,C)=(\{i\},[n]\setminus\{i\})\) and their reversals, \(2n\) pairs.

**Step 2: All-set polynomial.** When all layers are nonempty, the generating factor is the first product in \(\mathcal P_n(x,y,z)\). When \(B=[n]\) and at least one outer layer is empty, the disjoint contribution is \(y^n((1+x)^n+(1+z)^n-1)\). With \(B=\varnothing\), covering all columns by the two nonempty outer index sets permits exactly the three column states \(A\setminus C\), \(C\setminus A\), and \(A\cap C\). Its contribution is \((x+z+xz)^n-x^n-z^n\) minus the \(2n\) forbidden configurations \(n(xz^{n-1}+x^{n-1}z)\). This proves the trivariate formula. Substituting \(x=y=z=u\) yields the one-variable formula.

**Step 3: Inclusion-minimal classification.** A feasible set meeting all three layers is inclusion-minimal exactly when it selects one vertex from each; there are \(n^3\) such three-vertex sets, and deleting any of the three destroys domination because \(n\ge3\). In the case \(B=[n]\), deleting outer selections remains feasible, so the only inclusion-minimal member is \(A=C=\varnothing\), contributing one set of size \(n\).

For feasible sets with \(B=\varnothing\), if \(A,C\) are disjoint, they partition \([n]\). Such a set is feasible precisely when \(|A|,|C|\ge2\), and it is inclusion-minimal since every chosen vertex is the unique selected vertex in its column. There are \(2^n-2n-2\) such partitions when \(n\ge4\), each of size \(n\). If \(A\cap C\ne\varnothing\) and one set is a singleton, the other must be all of \([n]\); every such pair is inclusion-minimal, because deleting its lone singleton empties an outer layer, deleting the overlapping vertex from the full layer creates a forbidden singleton/disjoint-complement configuration, and deleting any other vertex leaves its column undominated. There are \(2n\) such sets of size \(n+1\).

Finally, suppose \(A\cap C\ne\varnothing\) and \(|A|,|C|\ge2\). If either index set has at least three members, deleting an overlapping selection from that side leaves the union covering \([n]\) and both outer sizes at least two, so the set is not minimal. The only remaining possibility is \(|A|=|C|=2\) with an overlap; then \(|A\cup C|\le3\). For \(n\ge4\) this cannot dominate the middle layer. For \(n=3\), exact one-index overlap gives six additional inclusion-minimal sets of size four, counted by choosing the distinct omitted index from each size-two set; an overlap of two does not cover \([3]\). The disjoint-partition case is empty at \(n=3\). Collecting contributions gives both branches of \(\mathcal M_n\).

Since \(n^3\) three-vertex minima exist and no feasible set has size below three, \(\gamma_{t2}=3\). Since the outer singleton/full constructions have size \(n+1\), and the above classification has no larger inclusion-minimal set, \(\Gamma_{t2}=n+1\). All assertions follow.

## Verification
The independent standard-library program `verify_semitotal.py` explicitly constructs \(G_n\), computes graph distances by breadth-first search, tests the original domination and semitotal predicates for every selected subset, and tests each one-vertex deletion. It separately computes the predicted three-layer polynomial coefficients and the inclusion-minimal polynomial. It verified \(n=3,4,5\) over \(2^9+2^{12}+2^{15}=37{,}376\) vertex subsets with no discrepancies. Execute `python verify_semitotal.py` using Python 3. No external package, dataset, or unshipped artifact is required. The finite check does not establish the statements for unbounded \(n\); the proof above does.

## Relationship to prior work
Henning introduced and studied the upper semitotal domination number and established general upper bounds, including \(\Gamma_{t2}(G)\le |V(G)|-\delta(G)\) under standard hypotheses. For \(G_n\), this general bound gives \(\Gamma_{t2}(G_n)\le2n\), which does not imply the exact \(n+1\) value or the polynomial coefficients. Asplund, Davila, and Krop studied semitotal domination of Cartesian products and proved general lower bounds for the **minimum** number; their inspected nine-page preprint does not give a classification or generating polynomial for \(K_n\square P_3\). The present calculation addresses an explicit product family and refines both scalar extremal parameters by counting all feasible and all inclusion-minimal sets.

## Limitations
The theorem concerns exactly \(K_n\square P_3\) for integers \(n\ge3\), not longer clique paths or arbitrary Cartesian products. The computational check covers only \(n=3,4,5\). Bibliographic search and mathematical comparison found no equivalent census, but this does not establish universal priority; the full text of the directly relevant 2017 upper-semitotal-domination article was not available for complete inspection. A differently formulated prior specialization may exist.

## References
1. M. A. Henning, “Edge Weighting Functions on Semitotal Dominating Sets,” *Graphs and Combinatorics* **33** (2017), 403–417, DOI: 10.1007/s00373-017-1769-4 (first online 2017-02-08); publicly accessible abstract and metadata: https://doi.org/10.1007/s00373-017-1769-4.
2. J. Asplund, R. Davila, and E. Krop, “A Vizing-type result for semi-total domination,” arXiv:1803.04746 (first posted 2018-03-13), https://arxiv.org/abs/1803.04746 ; inspected preprint: https://arxiv.org/pdf/1803.04746.
3. M. A. Henning and A. Pandey, “Algorithmic aspects of semitotal domination in graphs,” *Theoretical Computer Science* **766** (2019), 46–57, DOI: 10.1016/j.tcs.2018.09.019, abstract: https://doi.org/10.1016/j.tcs.2018.09.019.
