# Directed-cut shattering and comparison queries on one-descent permutations

## Finding

Let \(D=(V,A)\) be any finite **oriented simple graph**, with at most one arc between any unordered pair. For each vertex labeling \(x:V\to\{0,1\}\), form the directed-cut concept \(c_x:A\to\{0,1\}\), where \(c_x(u\to v)=1\) precisely when \(x(u)=0\) and \(x(v)=1\). A query support \(S\subseteq A\) is VC-shattered by these concepts **if and only if** every nontrivial weak component of \((V,S)\) is an oriented star: its underlying graph is a star and all its arcs point either toward its center or away from its center. Isolated vertices are allowed.

As an application, let \(\mathcal D_n\) consist of all permutations of \([n]\) with at most one descent in their one-line notation, represented by Boolean comparison queries \(q_{ij}(\pi)=1\) when label \(j\) precedes label \(i\), for \(1\le i<j\le n\). A comparison support \(S\) is shattered by \(\mathcal D_n\) exactly when it is a star forest, with each nontrivial star centered at either the minimum or the maximum label in its component. In particular, for all \(n\ge1\),

\[
\operatorname{VCdim}(\mathcal D_n)=\operatorname{Ldim}(\mathcal D_n)=n-1.
\]

Let \(P_n(z)\) enumerate shattered supports by their number of comparison edges. The complete enumeration satisfies

\[
\sum_{n\ge0}\frac{P_n(z)t^n}{n!}=\exp\!\left(t+\frac{zt^2}{2}+2\sum_{r\ge3}\frac{z^{r-1}t^r}{r!}\right),\qquad P_0(z)=1.
\]

For \(n\ge3\), precisely two maximum supports exist: the full star centered at label \(1\) and the full star centered at label \(n\). At \(n=2\), there is one maximum support, and at \(n=1\) the empty support is unique.

## Assumptions and scope

All graphs are finite, simple and have no loops. An oriented simple graph chooses at most one direction for each unordered vertex pair, but need not be acyclic. An oriented star has one vertex incident to all its edges and, when it has at least two edges, that vertex is either the source of all those edges or their sink. A single directed edge is an oriented star in either interpretation. An empty query support is shattered by every nonempty concept class.

The concepts for permutations distinguish *value labels*, not positions: querying \(i<j\) asks whether the larger value \(j\) occurs before the smaller value \(i\). The one-line descent count is \(|\{a:\pi_a>\pi_{a+1}\}|\); it is not the inversion count. The restrictions on supports and all formulas are asserted for every integer \(n\ge1\), with the empty zero-vertex convention used only to state the exponential generating function.

The Littlestone dimension here is the maximum depth of a complete binary online shattering tree under the same fixed universe of pair-comparison queries, where the adversary may choose the next query based on previous answers.

## Proof

**Oriented-cut characterization (necessity).** Suppose \(S\) is shattered. In particular, the all-positive assignment on \(S\) occurs under some vertex labeling. Every vertex incident with an arc of \(S\) must therefore have only outgoing arcs (label \(0\)) or only incoming arcs (label \(1\)); a vertex with both an incoming and outgoing selected arc would require both labels. Thus the underlying selected graph is bipartite, with every selected arc directed from its source-part to its sink-part.

If its underlying graph contained a simple path on four vertices, write the path as \(v_1,v_2,v_3,v_4\). The source/sink restriction forces the directions to alternate along the path. Assign positive answers to its first and third edges, and a negative answer to its middle edge; answers on any other selected edges may be fixed arbitrarily. Positivity of the two outer edges forces the label of every vertex on the path, in particular both endpoint labels of its middle edge are exactly the values making that middle edge positive. This contradicts shattering. Hence the selected graph has no simple path of length three. Every connected simple graph that is bipartite and has no path of length three is a star (or a single vertex): otherwise, two edges without a common endpoint can be joined to exhibit such a path. The selected components are therefore consistently oriented stars.

**Oriented-cut characterization (sufficiency).** Fix an arbitrary prescribed \(0/1\) answer on each selected arc. For an out-star put its center in vertex class \(0\); put each leaf in class \(1\) exactly when its incident arc is prescribed positive, otherwise in class \(0\). For an in-star put its center in class \(1\); put each leaf in class \(0\) exactly when its incident arc is prescribed positive, otherwise in class \(1\). The components are vertex-disjoint, so these prescriptions never conflict; label isolated vertices arbitrarily. The resulting directed cut realizes the entire prescribed pattern.

**Reduction from one-descent rankings.** Every permutation with at most one descent can be written as an increasing listing of a subset \(B\subseteq[n]\), followed by an increasing listing of its complement. Conversely, every subset \(B\) yields such a permutation. For \(i<j\), the query \(q_{ij}\) returns \(1\) exactly when \(j\in B\) but \(i\notin B\). This is the directed-cut predicate for the transitive orientation \(i\to j\) of the complete graph, with vertex bit \(x(v)=1_{v\in B}\). Applying the general characterization, all consistently oriented stars in this tournament have their centers at the minimum (out-star) or maximum (in-star) of their components, proving the stated complete support characterization.

**Dimensions.** For \(n\ge2\), the \(n-1\) comparisons involving the minimum label form an out-star and are shattered, hence both dimensions are at least \(n-1\). There are \(2^n\) subset choices \(B\). Exactly the \(n+1\) initial segments \(B=\{1,\ldots,r\}\), including the empty and full sets, give the identical increasing permutation, while all other subset choices yield pairwise distinct one-descent permutations, because the unique descent identifies the two blocks. Thus \(|\mathcal D_n|=2^n-n\). For \(n\ge2\), \(2^{n-1}\le 2^n-n<2^n\); any depth-\(d\) Littlestone tree requires at least \(2^d\) different concepts. Therefore \(\operatorname{Ldim}\le n-1\) and equality follows; \(\operatorname{VCdim}\le\operatorname{Ldim}\). The one-element case has a single concept and both dimensions zero.

**Counting all supports.** For a specified component-vertex set of size \(r\), the number of allowable connected selected-edge structures is \(1\) when \(r=1\) or \(r=2\), and \(2\) when \(r\ge3\): the two different centers are its minimum and maximum elements. Each such component has exactly \(r-1\) selected edges. The labeled exponential formula for a set of components immediately gives the displayed exponential generating function. Alternatively, writing \(a_1=a_2=1\) and \(a_r=2\) for \(r\ge3\), the polynomials are uniquely determined by

\[
P_n(z)=\sum_{r=1}^n\binom{n-1}{r-1}a_r z^{r-1}P_{n-r}(z),\quad P_0(z)=1.
\]

A star forest on \(n\) vertices has at most \(n-1\) edges, with equality only if it is one spanning star. Its only permissible centers in the transitive tournament are the smallest or largest label, which are distinct exactly when \(n\ge3\). This proves the count of maximum supports.

## Verification

A standalone standard-library script `verify.py` independently builds all one-descent permutations as permutation words and enumerates every comparison-query support for \(1\le n\le6\), checking the shattering definition directly against the structural criterion and the exponential-generating-function coefficient recurrence. It also exhausts every orientation-or-absence choice for the six possible pairs of four labeled vertices: all \(729\) oriented simple graphs and all \(15,625\) resulting support cases pass. Run `python verify.py` from the package directory. The recorded stdout appears in `verification_output.txt`.

These exhaustive calculations corroborate the proof over the finite ranges specified; unrestricted validity follows from the structural proof, not finite extrapolation.

## Relationship to prior work

Peters and Procaccia (2021) study pairwise-comparison preference elicitation with distributional priors, including Mallows and Plackett–Luce models; they do not establish this one-descent Boolean shattering classification or its polynomial. Alon, Bollobás, Gyárfás, Lehel and Scott (2007) analyze extremal sizes of directed cuts, not the traces of all cuts on selected arc supports. Kozma and Moran (2013) derive shattering tools for graph **orientations** subject to graph constraints, not for vertex-bipartition-directed-cut edge indicators. Raz (2000) defines a different permutation VC parameter using complete pattern realization on selected labels, rather than Boolean edge-comparison traces. These comparisons concern mathematical implications, not merely differences in terminology.

The elementary Eulerian count of permutations with at most one descent is background. The contribution asserted here is the forbidden-support characterization for all oriented graphs and its complete one-descent ranking consequences, particularly the all-degree enumerator and maximum-support classification.

## Limitations

The claim is about Boolean shattering and Littlestone dimensions, not exact worst-case identification-query complexity or optimal sorting algorithms. The exhaustive code only covers \(n\le6\) for rankings and four-vertex oriented graphs. No formal independent proof audit or exhaustive historical-priority determination has been made. An older theorem formulated in terms of Boolean conjunction queries or directed cut traces could imply the present result without using the same terminology; that remains a historical-priority risk.

## References

- Peters, D., and Procaccia, A. D. (2021), *Preference Elicitation as Average-Case Sorting*, Proceedings of the AAAI Conference on Artificial Intelligence 35(6), 5647–5655, DOI: 10.1609/aaai.v35i6.16709, first official publication May 18, 2021. https://ojs.aaai.org/index.php/AAAI/article/view/16709/16516
- Alon, N., Bollobás, B., Gyárfás, A., Lehel, J., and Scott, A. (2007), *Maximum directed cuts in acyclic digraphs*, https://web.math.princeton.edu/~nalon/PDFS/abgls4.pdf
- Kozma, L., and Moran, S. (2013), *Shattering, Graph Orientations, and Connectivity*, Electronic Journal of Combinatorics 20(3), P44, DOI: 10.37236/3326. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p44/pdf/
- Raz, R. (2000), *VC-dimension of sets of permutations*, Combinatorica 20, 241–255, DOI: 10.1007/s004930070023.
