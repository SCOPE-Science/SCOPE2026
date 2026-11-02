# Almost-Johnson geodesics in Desargues zero-forcing reconfiguration

## Finding

Let \(D=GP(10,3)\) be the Desargues graph. Let \(\mathcal Z(D)\) have one vertex for each minimum ordinary zero-forcing set of \(D\), with two such sets joined exactly when one chosen vertex is replaced by one unchosen vertex. For sets \(A,B\), put \(j(A,B)=8-|A\cap B|\), the distance between them in the unrestricted Johnson graph \(J(20,8)\), and let \(d(A,B)\) be their distance in \(\mathcal Z(D)\).

**Exact finite metric theorem.** For every pair of minimum ordinary zero-forcing sets,
\[
 j(A,B)\le d(A,B)\le j(A,B)+1.
\]
The two distances differ for exactly **47,380 unordered pairs** out of \(\binom{13520}{2}=91{,}388{,}440\) pairs. The precise distribution of the exceptional pairs according to their Johnson distance is
\[
\begin{array}{c|rrrrr}
 j&2&3&4&5&6\\\hline
 \#\{\{A,B\}:d=j+1\}&16080&25080&5730&360&130
\end{array}.
\]
No pair with Johnson distance \(1\), \(7\), or \(8\) requires a detour. The exchange graph has **radius \(7\)** and **diameter \(8\)**; exactly \(980\) vertices have eccentricity \(7\), and the other \(12{,}540\) have eccentricity \(8\). In particular, the minimum zero-forcing reconfiguration is connected, but its natural embedding in \(J(20,8)\) is not isometric.

Auxiliary enumerative checks give \(Z(D)=8\), \(13{,}520\) minimum zero-forcing sets, \(178{,}560\) exchange edges and degree distribution
\[
\begin{aligned}
P(z)={}&240z^{20}+120z^{21}+360z^{22}+480z^{23}+1340z^{24}\\
&+1800z^{25}+3000z^{26}+240z^{27}+4380z^{28}\\
&+480z^{29}+960z^{30}+120z^{32}.
\end{aligned}
\]
These auxiliary counts are included to make the metric certificate self-contained; the main claim is the sharp near-geodesic bound and full defect/eccentricity census.

## Assumptions and scope

All graphs are finite, simple and undirected. Label the twenty vertices of \(D\) by \(0,1,\ldots,19\), writing \(u_i=i\) and \(v_i=10+i\) for indices \(i\) modulo ten. Its thirty edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\) for each \(i\in\mathbb Z/10\mathbb Z\). Thus \(D\) is the cubic generalized Petersen graph \(GP(10,3)\), equivalently the bipartite Kneser graph \(H(5,2)\).

Starting from a set \(S\) of blue vertices, the *ordinary zero-forcing rule* allows a blue vertex with exactly one white neighbor to turn that neighbor blue. A set is zero forcing if repeated applications turn all vertices blue. The minimum size is \(Z(D)\). A reconfiguration step changes exactly one selected vertex; it does **not** require the removed and inserted vertices to be adjacent in \(D\). Unordered distinct pairs, not ordered pairs, are counted throughout.

## Proof

This is a finite exhaustive proof with fully specified bounds and a standalone replayable checker, not an inference from sampled cases.

**Lemma 1 (closure test).** For an initial blue set \(S\), repeatedly color simultaneously every white vertex that is a unique white neighbor of at least one blue vertex. The process stabilizes after at most \(20-|S|\) nonempty rounds. Its fixed point is the maximal zero-forcing closure of \(S\). A set is zero forcing if and only if the fixed point is the whole vertex set. To see independence of the forcing order, observe that blue sets grow monotonically and a force legal earlier remains accomplished or legal as more vertices turn blue; every legal force is eventually included at the fixed point. This also follows from the standard uniqueness-of-closure property of the color-change rule.

**Lemma 2 (exhaustive state and exchange graph).** Encode \(S\) as \(M(S)=\sum_{i\in S}2^i\). The exact fixed-population enumerator in `verify_desargues_metric.cpp` visits each of the \(\binom{20}{7}=77{,}520\) seven-element masks and each of the \(\binom{20}{8}=125{,}970\) eight-element masks exactly once. By Lemma 1 it finds no zero-forcing seven-element set and exactly \(13{,}520\) zero-forcing eight-element sets. Since zero forcing is upward closed, the absence of any seven-element set also excludes all smaller sizes, so these are exactly the minimum configurations. For each such mask it tests all \(8(20-8)=96\) replacements of one chosen and one unchosen bit, linking it to a configuration if and only if that replacement occurs in the complete sorted membership array. Symmetry of every link is explicitly checked. The resulting graph has \(178{,}560\) undirected edges, with the displayed degree distribution.

**Lemma 3 (complete metric census).** Breadth-first search in an unweighted graph computes exact shortest-path distances by increasing path length. The checker runs a full BFS from **every one of the \(13{,}520\) configurations**, asserts that each BFS reaches all configurations, and examines each of the \(\binom{13520}{2}=91{,}388{,}440\) unordered pairs exactly once. For each pair it computes the Johnson lower bound directly by an intersection population count. Every exchange can reduce the size of the intersection with the target by at most one, hence \(d\ge j\). The exhaustive pair comparison yields \(91{,}341{,}060\) equal-distance pairs and exactly \(47{,}380\) pairs with \(d=j+1\), no larger excess, with the displayed Johnson-distance refinement. Taking the maxima in every BFS row gives the asserted eccentricities, radius and diameter.

**Concrete strictness witness.** For the above vertex labels, the four masks \(255,639,879,999\) represent minimum forcing sets and form a length-three exchange path. The endpoints have Johnson distance \(2\), whereas the exhaustive adjacency/BFS check gives distance \(3\). Their selected-vertex sets are respectively \(\{0,1,2,3,4,5,6,7\}\) and \(\{0,1,2,5,6,7,8,9\}\), so the defect is genuinely nonzero. This proves the upper bound cannot be replaced by universal equality.

The preceding complete finite enumerations, deterministic graph reconstruction, explicit loop bounds, and exact all-source BFS prove every asserted value, provided the included checker is executed and its assertions pass. No numerical approximation or unverified extrapolation is involved.

## Verification

The standalone `verify_desargues_metric.cpp` performs the complete two-population forcing census, full exchange-graph construction, reciprocal adjacency and degree checks, all-source BFS, exact pairwise defect histogram, eccentricity distribution, and strictness witness. It uses integer operations only. Compile and run from the extracted package with

```sh
g++ -std=c++17 -O3 verify_desargues_metric.cpp -o verify_desargues_metric
./verify_desargues_metric
```

`verify_desargues_alternate.py` independently constructs the same Desargues graph as the bipartite Kneser graph on two-subsets of a five-element set, and uses one-force-at-a-time closure rather than parallel forcing. It independently verifies the zero-forcing minimum, total number of minimum sets, exchange-edge and degree census, connectivity and sampled distance inequalities. Run `python3 verify_desargues_alternate.py`. The independent implementation is a *second computational cross-check*, not an independent mathematical audit. Complete all-pairs metrics are checked by the first program. Exact expected outputs are recorded in `certificate.json`.

## Relationship to prior work

Butler, Grout and Hall determined the ordinary zero-forcing number \(Z(D)=8\) and studied the Desargues graph's inertia constraints. Their theorem and examples do not determine the reconfiguration metric among all minimum sets. Geneson, Haas and Hogben define minimum-zero-forcing-set exchange graphs, prove general properties, and provide the generic exhaustive enumeration algorithm; the inspected text does not state the distance, radius, or exception census for \(D\). The graph is also the bipartite Kneser graph \(H(5,2)\), so that alternative naming was included in the literature search. A generic exhaustive algorithm makes these numbers computable but does not supply their values without the present complete instance analysis.

The new point is the *sharply bounded deviation from Johnson geodesics*, including exactly where and how often one extra exchange is needed. This distinguishes mere connectivity from near-optimal reconfiguration of minimal forcing seeds.

## Limitations

This is an exact theorem for the single canonical 20-vertex Desargues graph, not a theorem for every generalized Petersen graph or arbitrary zero-forcing reconfiguration graph. Its proof is finite and computer-assisted, and depends on executing and checking the included standalone exhaustive code. The second implementation independently verifies the state/edge reconstruction but does not independently repeat every all-pairs BFS. A mathematically equivalent result could exist in unindexed literature or data tables; no absence-of-prior-result theorem is claimed. No separate external mathematical audit has been performed.

## References

1. S. Butler, J. Grout and H. T. Hall, *Zero forcing for inertia sets*, arXiv:1211.4618 (first version 19 November 2012); Electronic Journal of Linear Algebra 30 (2015), 1–18. https://arxiv.org/abs/1211.4618
2. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (first version 1 September 2020); Discrete Applied Mathematics 329 (2023), 126–139. https://arxiv.org/abs/2009.00220
3. E. W. Weisstein, *Desargues Graph*, MathWorld, https://mathworld.wolfram.com/DesarguesGraph.html (used only for graph aliases and presentation).
