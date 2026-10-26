# Independent-domination rigidity of the Tutte–Coxeter graph
## Finding
Let \(T\) denote the \(30\)-vertex Tutte–Coxeter graph, with its standard duad–syntheme incidence construction. The independent domination number of \(T\) is \(9\), and there are exactly \(90\) independent dominating sets of minimum size.

The natural \(S_6\) action partitions these \(90\) optimal sets into two orbits of size \(45\), distinguished by whether they contain \(4\) or \(5\) duad-vertices. Their complete classification is as follows. Choose a \(4\)-cycle \(C\) among the edges of \(K_6\), with its four-edge set \(D\), and let \(c\) be the edge joining the other two vertices of \(K_6\). Let \(F(E)\) denote the set of all perfect matchings of \(K_6\) using none of the edges in \(E\). Then the two optimal sets associated with \(C\) are
\[
I_0(C)=D\cup F(D),\qquad
I_1(C)=(D\cup\{c\})\cup F(D\cup\{c\}).
\]
Here each edge is interpreted as its duad-vertex and each perfect matching as its syntheme-vertex. One has \(\lvert F(D)\rvert=5\) and \(\lvert F(D\cup\{c\})\rvert=4\). Every optimal independent dominating set is exactly one of the above \(90\) sets: there are \(\binom62\cdot3=45\) choices of \(C\).

Define a token-jump exchange graph \(R\) on these optimal sets by joining distinct \(I,J\) precisely when \(\lvert I\setminus J\rvert=\lvert J\setminus I\rvert=1\). Then
\[
\boxed{R\cong 45K_2.}
\]
More precisely, its \(45\) edges are exactly \(I_0(C)I_1(C)\). For every such exchange, the deleted syntheme-vertex is incident in \(T\) to the added duad-vertex. Thus the token-slide exchange graph (which additionally requires the removed and added vertices to be adjacent in \(T\)) agrees with \(R\). Every optimal configuration has exactly one valid one-vertex replacement, and no sequence of such optimal replacements reaches a different \(4\)-cycle class.

## Assumptions and scope
The underlying set is \(X=\{0,1,2,3,4,5\}\). Its \(15\) duads are the two-element subsets of \(X\); its \(15\) synthemes are partitions of \(X\) into three disjoint duads. The bipartite graph \(T\) has one vertex for each duad and syntheme, with adjacency given by containment. Each vertex of \(T\) has degree \(3\).

An independent dominating set is an independent subset \(I\) that dominates every vertex, equivalently an inclusion-maximal independent subset. The independent domination number \(i(T)\) is the least cardinality of such a set. Token jump and token slide are defined only between minimum independent dominating sets, preserving that property at every step. No assertion is made about larger independent dominating sets or reconfiguration through nonoptimal intermediate configurations.

## Proof
**A forced-completion lemma.** Represent an independent set by its chosen duads \(D\subseteq E(K_6)\) and chosen synthemes \(M\). No chosen syntheme may contain any edge of \(D\). Every unchosen syntheme must be adjacent to a chosen duad if the set is dominating. Hence every syntheme avoiding \(D\) is forced to be chosen, and every syntheme containing an edge of \(D\) is forbidden. Therefore any independent dominating set has the unique form
\[
I(D)=D\cup F(D),\quad F(D)=\{m:\ m\text{ a perfect matching of }K_6,\ m\cap D=\varnothing\}.
\]
This set dominates the remaining duad-vertices exactly when every edge outside \(D\) lies in at least one perfect matching belonging to \(F(D)\):
\[
D\cup\bigcup_{m\in F(D)}m=E(K_6).
\tag{1}
\]
Thus (1) is both necessary and sufficient, and when it holds
\[
|I(D)|=|D|+|F(D)|.
\tag{2}
\]
These formulas reduce the full classification to exactly \(2^{15}=32768\) edge masks \(D\), with no unexamined choices of synthemes.

**Exact finite classification.** Generate all \(15\) perfect matchings recursively: match the smallest unused element to each possible partner and recurse on the other four elements. For each of the \(32768\) choices of \(D\), calculate \(F(D)\), its union, (1), and (2) with integer bit sets. The following entire finite table is independently reproducible from `verify_duad_syntheme.py`; a dash means no feasible set:

| \(\lvert D\rvert\) | Number satisfying (1) | Minimum \(\lvert I(D)\rvert\) | Number with \(\lvert I(D)\rvert=9\) |
|---:|---:|---:|---:|
| 0 | 1 | 15 | 0 |
| 1 | 15 | 13 | 0 |
| 2 | 105 | 11 | 0 |
| 3 | 375 | 10 | 0 |
| 4 | 735 | 9 | 45 |
| 5 | 837 | 9 | 45 |
| 6 | 610 | 10 | 0 |
| 7 | 270 | 10 | 0 |
| 8 | 195 | 11 | 0 |
| 9 | 60 | 11 | 0 |
| 10 | 45 | 12 | 0 |
| 11 | 0 | — | 0 |
| 12 | 15 | 13 | 0 |
| 13 | 0 | — | 0 |
| 14 | 0 | — | 0 |
| 15 | 1 | 15 | 0 |

This proves \(i(T)=9\), its \(90\) attaining sets, and also counts \(3264\) independent dominating sets of arbitrary size. The verifier checks that every attaining four-duad mask is precisely the edge set of a \(4\)-cycle in \(K_6\). A four-cycle uses four vertices; with its complementary duad \(c\), adding \(c\) to its duad mask produces one attaining five-duad mask. For each four-cycle, exactly one of the five synthemes avoiding \(D\) contains \(c\), so its removal turns \(I_0(C)\) into \(I_1(C)\). The remaining \(45\) attaining five-duad masks are exhausted by these distinct partners. Permuting the six labels maps any \(4\)-cycle to any other, proving the two claimed \(S_6\) orbits.

**Exact exchange classification.** For each of the \(90\) explicitly enumerated optimal sets, the verifier tries every ordered pair consisting of one selected and one unselected vertex of \(T\), testing whether their replacement is another optimal set. This complete search yields exactly \(45\) undirected exchanges, each equal to the above paired \(I_0(C)I_1(C)\), and degree one at every vertex. The deleted syntheme contains \(c\), so each exchange is also a token slide along an incidence edge. Conversely every token slide is a token jump. Therefore the two reconfiguration graphs coincide and are exactly \(45K_2\).

## Verification
Both reproducibility programs use only the Python standard library and contain all data needed to construct the graph:

1. Run `python3 verify_duad_syntheme.py` and compare with `duad_syntheme_output.txt`. It generates the \(15\) duads, all \(15\) synthemes, all \(32768\) duad choices and their unique completions. It tests all \(90\) optimal states for every one-for-one exchange, checks the \(45\)-cycle classification, and calculates the entire \(S_6\)-orbit by \(720\) label permutations. It terminates with `VERIFY_OK`.
2. Run `python3 verify_symplectic.py` and compare with `symplectic_output.txt`. It constructs the generalized quadrangle \(GQ(2,2)\) from an alternating nondegenerate form on \(\mathbb F_2^4\); a supplied \(30\)-vertex bijection checks each of the \(45\) edges against the duad–syntheme model. This checker independently recurses through independent vertex selections in that model, filters maximal sets via the neighborhood condition, and reconstructs all exchanges. Its counts reproduce \(3264\) inclusion-maximal independent sets, \(90\) optimal ones, and \(45\) token-slide exchanges.

The checkers prove exhaustive claims only for this finite \(30\)-vertex graph; no empirical sample or unverified extrapolation is used.

## Relationship to prior work
Prażmowska and Prażmowski's treatment of the Cremona–Richmond configuration supplies the historical duad–syntheme construction and its \(S_6\) symmetry; it does not calculate independent domination or optimal-set exchanges. Dorbec, Henning, Montassier and Southey study upper bounds for independent domination in cubic graphs, without a classification of optimal configurations for the Tutte–Coxeter graph. Perarnau and Perkins study independent-set counts and occupancy under cubic-girth hypotheses, not the maximal-independent-set metric at the minimum-size layer.

A publicly available exact computation of the *independence complex* of the same graph gives its homotopy type as a wedge of nine eight-spheres. Its full mathematical statement and proof concern homotopy of the independence complex, not the number, structure, or token-slide adjacency of the smallest maximal faces. Neither its Betti numbers nor its stated face vector implies the present paired exchange classification. These mathematical objects must not be confused: maximal independent sets need not be maximum independent sets, and the minimum maximal-set layer is not determined by ordinary independent-set cardinality counts alone.

## Limitations
The result applies to the stated Tutte–Coxeter graph and to exchanges that remain within minimum independent dominating sets. The explicit finite classification relies on exhaustive exact integer computation, with two independent implementations and a separately verified representation isomorphism; it is not a uniform family theorem. Literature comparisons are bounded by the accessible primary texts and searchable records; an equivalent older result under different vocabulary could remain unrecognized.

## References
1. K. Prażmowska and M. Prażmowski, *The Cremona–Richmond configuration revisited and generalized*, arXiv:1404.7166v1 (public 2014-04-28).
2. S. Dorbec, M. A. Henning, A. Montassier and J. Southey, *Independent domination in cubic graphs*, Journal of Graph Theory 80 (2015), DOI 10.1002/jgt.21855.
3. G. Perarnau and W. Perkins, *Counting independent sets in cubic graphs of given girth*, arXiv:1611.01474v1 (public 2016-11-04), later Journal of Combinatorial Theory B 133 (2018).
4. *The Tutte–Coxeter independence complex is a wedge of nine eight-spheres*, published scientific record 374e87ce82da (2026); see especially the independent-face enumeration and discrete-Morse argument.
