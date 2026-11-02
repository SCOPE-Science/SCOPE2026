# The first closed-Johnson online-shattering gap and its four-query trace spectrum

## Finding

Write \(J(n,k)\) for the graph on the \(k\)-subsets of \([n]\), with two distinct vertices adjacent when their intersection has size \(k-1\). For a center \(C\), let its *closed* neighborhood be \(B_C=\{Q:|C\cap Q|\ge k-1\}\). Membership in \(B_C\) is a Boolean concept on the graph vertices.

For \(J(6,3)\), there are exactly twenty centers and twenty query vertices. If \(S\) is any four-element subset of the query vertices, set \(\tau(S)=|\{B_C\cap S:C\in\binom{[6]}3\}|\). The complete four-query trace distribution is

\[
\begin{array}{c|rrr}
\tau(S)&4&8&14\\\hline
|\{S:|S|=4,\ \tau(S)=\tau\}|&45&1680&3120.
\end{array}
\]

In particular, no four-query support is shattered, while three queries can be shattered, and the closed-neighborhood concept class has
\[
\operatorname{VCdim}=3,\qquad\operatorname{Ldim}=4.
\]

For comparison, the *open* neighborhoods of the same graph, defined by \(|C\cap Q|=2\), have \(\operatorname{VCdim}=\operatorname{Ldim}=4\). Thus adding the center itself to every open neighborhood reduces the static shattering dimension without reducing the optimal adaptive shattering depth.

Moreover, among all Johnson graphs ordered by their number of vertices, \(J(6,3)\) is a smallest example with \(\operatorname{VCdim}<\operatorname{Ldim}\) for the family of closed neighborhoods. The smaller nontrivial parameter cases \((n,k)=(4,2),(5,2),(6,2)\) have respective dimension pairs \((1,1),(2,2),(3,3)\); rank-one Johnson graphs have pair \((0,0)\).

## Assumptions and scope

All graphs, concept families and decision trees are finite. The ground set \([n]\) is labeled. The adaptive dimension is the greatest depth of a complete binary decision tree whose internal nodes are query vertices and whose root-to-leaf answer sequences can each be realized by a center. The VC dimension is the greatest cardinality of a set of query vertices realizing all Boolean labelings. A label of one in the closed system means \(|C\cap Q|\ge k-1\), **including** \(C=Q\); in the open system it means exactly \(k-1\).

The trace distribution is for *unordered four-element query supports* and *distinct traces*, not ordered queries or multiplicities of centers. Graph isomorphism identifies \(J(n,k)\) with \(J(n,n-k)\).

## Proof

**Four-query trace distribution.** Enumerate the twenty three-element subsets of \([6]\) in lexicographic order. The symmetric group on six labels acts on every four-subset \(S\) of these twenty vertices, preserving \(\tau(S)\). The exhaustive orbit certificate `orbits.json` lists twenty-one representative supports. The companion program `verify.py` generates all \(720\) label permutations, computes each representative's orbit and directly evaluates all twenty possible center traces. It proves that the listed orbits are pairwise disjoint and cover all \(\binom{20}{4}=4845\) supports. The orbit-weighted trace histogram is exactly the displayed distribution. Independently, the same program enumerates all \(4845\) supports without orbit reduction, directly recomputes their traces and compares the histograms. These two finite enumerations establish the distribution exhaustively; there is no assumption that checking representatives alone establishes coverage.

The complement map on the twenty centers provides an additional normalization check: for every center \(C\) and query \(Q\), exactly one of \(C\) and \([6]\setminus C\) lies within closed Johnson distance one of \(Q\). Thus all traces occur in complementary pairs, consistently with the even trace spectrum. The three queries \(\{1,2,3\},\{1,2,4\},\{1,2,5\}\) realize all eight answer patterns by direct examination of the twenty centers. The four-query distribution excludes sixteen patterns for any four queries, so \(\operatorname{VCdim}=3\).

**Adaptive dimension.** There are twenty distinct closed-neighborhood hypotheses, so any complete depth-five decision tree would require at least \(2^5=32\) different centers at its leaves, which is impossible. The file `tree.json` contains a full depth-four decision tree with fifteen internal query nodes and sixteen leaves labeled by *pairwise distinct* three-element centers. The verifier recursively propagates the set of centers consistent with each answer and confirms that every leaf witness realizes the entire answer path. This proves \(\operatorname{Ldim}\ge4\), and hence equality.

**Open neighborhoods.** The four-query support \(\{1,2,3\},\{1,2,4\},\{1,3,5\},\{1,4,6\}\) is directly verified as shattered using the strict intersection test \(|C\cap Q|=2\); this also agrees with the published open-neighborhood result cited below. Hence the open-neighborhood VC dimension is at least four. The upper bound from twenty hypotheses is four for both VC and Littlestone dimension, while VC dimension always bounds Littlestone dimension from below. Both open-neighborhood dimensions are therefore four.

**Minimality by graph order.** Complete graphs \(J(n,1)\) and \(J(n,n-1)\) have one distinct closed-neighborhood concept and both dimensions zero. Up to complementing the rank, the only Johnson graphs with fewer than twenty vertices outside this complete-graph case are \(J(4,2),J(5,2),J(6,2)\) (along with smaller trivial ranks). The direct finite checks in `verify.py` establish their pairs as above. One can see their online upper bounds without exhaustive recursion: \(J(4,2)\) has one negative center for every query, preventing depth two; \(J(5,2)\) has three negative centers for every query, preventing depth three; and \(J(6,2)\) has fifteen hypotheses, preventing depth four. The stated VC lower bounds are given by the query supports \(\{1,2\}\), \(\{1,2\},\{1,3\}\), and \(\{1,2\},\{1,3\},\{1,4\}\), respectively, each of which realizes all patterns. For \(n\ge7\) and \(2\le k\le n-2\), the vertex count \(\binom nk\ge\binom n2\ge21\). Thus no smaller Johnson graph has a closed-neighborhood gap.

## Verification

Execute `python verify.py` in the directory containing `verify.py`, `tree.json`, and `orbits.json`. Python 3 standard library suffices. The program generates all Johnson incidence matrices itself; checks every representative orbit, all permutations, disjointness and full coverage; recomputes the four-query trace histogram independently without symmetry reduction; verifies the depth-four tree and its distinct leaf witnesses; and checks every rank (up to rank complementation) for orders at most six, as well as both open and closed dimensions at \(J(6,3)\). No numerical solver or external certificate is required.

## Relationship to prior work

Adler, Benediktsson and Macpherson (first public arXiv version 31 July 2020) prove the maximum VC dimension for *open* neighborhoods of Johnson graphs, including an explicit open-neighborhood four-query witness for \(J(6,3)\). They note that closed-neighborhood VC dimension is bounded, but their inspected open-neighborhood theorems and discussion do not provide this exact closed trace spectrum or its adaptive dimension. Ghazi, Golowich, Kumar and Manurangsi (2021) study general Littlestone-dimension closure bounds, not the exact finite Johnson instance. Neither source's broader statement implies the numerical closed-neighborhood results here; in particular, adjoining the equality case changes the concept class and need not preserve VC dimension.

## Limitations

This is an exact **finite** classification of the first closed-Johnson discrepancy, not a formula for closed neighborhoods of all Johnson graphs. The trace histogram is proved by a complete executable case enumeration rather than by a hand-derived closed-form orbit-count argument. General higher-rank behavior and historical priority under alternative terminology (e.g., binary Johnson association schemes or diagonal-augmented incidence) have not been fully settled. The file package contains the entire finite certificate and no claims of independent verification.

## References

1. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (first public 2020-07-31), later *Discrete Applied Mathematics* 312 (2022), 29–44; https://arxiv.org/abs/2007.16042 .
2. B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, ALT / PMLR 132 (2021), 686–696; https://proceedings.mlr.press/v132/ghazi21a.html .
