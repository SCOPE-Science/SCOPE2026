# Super domination and exact exchange distances on crown graphs

## Finding
For every integer \(n\ge4\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph with matched nonedges \(a_i b_i\), \(i\in[n]\). A set \(D\) is super dominating when each \(x\notin D\) has a witness \(y\in D\) satisfying \(N(y)\cap(V\setminus D)=\{x\}\).

**All-cardinality classification.** Write \(U=\{i:a_i\notin D\}\) and \(W=\{i:b_i\notin D\}\). Then \(D\) is super dominating if and only if \(|U|,|W|\le2\) and, whenever at least one of these sizes equals \(2\), \(U\cap W=\varnothing\). The polynomial enumerating these sets by the number of omitted vertices is
\[
F_n(t)=1+2nt+\bigl(n^2+2\binom n2\bigr)t^2
 +2n\binom{n-1}{2}t^3
 +\binom n2\binom{n-2}{2}t^4.
\]
The ordinary cardinality polynomial is \(S_n(z)=z^{2n}F_n(z^{-1})\). In particular,
\[
\gamma_{\rm sp}(\operatorname{Cr}_n)=2n-4,\qquad
N_n=\binom n2\binom{n-2}{2}=6\binom n4
\]
minimum super dominating sets exist.

**Exact minimum-set exchange metric.** Each minimum set corresponds uniquely to an ordered pair \((U,W)\) of disjoint two-subsets of \([n]\). In the fixed-cardinality token-jumping graph, two configurations are adjacent when one selected graph vertex is replaced by an omitted graph vertex and the resulting set remains minimum super dominating. For \(n=4\), this graph consists of six isolated vertices. For \(n\ge5\), it is connected, \(4(n-4)\)-regular, has \(N_n\) vertices and \(2(n-4)N_n\) edges, and its distance is exactly
\[
d((U,W),(U',W'))=
4-|U\cap U'|-|W\cap W'|
 +\mathbf1_{\{U\cup W=U'\cup W',\ (U,W)\ne(U',W')\}}.
\]
Its diameter is \(5\). Exactly one vertex lies at distance \(5\) from any fixed configuration, namely \((W,U)\). The distance-shell polynomial from every fixed vertex is
\[
\begin{aligned}
P_n(t)={}&1+4(n-4)t+(n-4)(5n-17)t^2\\
&+2(n-3)(n^2-8n+18)t^3\\
&+\frac{(n-4)(n-3)(n^2-7n+18)}4t^4+t^5.
\end{aligned}
\]
Consequently the ordered-pair distance polynomial is \(N_nP_n(t)\). In contrast, the original-graph token-sliding reconfiguration graph of minimum sets has no edges for any \(n\ge4\).

## Assumptions and scope
All graphs are finite, undirected, simple and labeled. The two bipartition classes \(\{a_i\}\) and \(\{b_i\}\) have edges \(a_ib_j\) exactly when \(i\ne j\). Token jumping permits replacing any single vertex regardless of adjacency in the original graph; token sliding additionally requires adjacency between the removed and inserted vertices. The formulas count labeled vertex subsets, not isomorphism classes. The distance assertion for connected graphs is stated only for \(n\ge5\); no finite distance between different isolated configurations is asserted for \(n=4\).

## Proof
**1. Characterization.** For \(a_i\notin D\), a witness necessarily has the form \(b_j\in D\) with \(j\ne i\), and its omitted neighbors are exactly \(U\setminus\{j\}\). If \(|U|\ge3\), no such witness can expose only \(a_i\). If \(|U|=2\), the witness for either omitted vertex must be the selected \(b_j\) indexed by the other omitted vertex; therefore \(U\cap W=\varnothing\) is necessary and sufficient. If \(|U|=1\), the requirement is some selected \(b_j\) with \(j\ne i\), automatic since \(|W|\le2\) and \(n\ge4\). The symmetric argument applies to the \(b\)-vertices. This proves the iff condition, including the empty-set cases.

**2. Counting.** The numbers of pairs \((U,W)\) with total omission size \(0,1,2,3,4\) are, respectively, \(1\), \(2n\), \(2\binom n2+n^2\), \(2\binom n2(n-2)=2n\binom{n-1}2\), and \(\binom n2\binom{n-2}2\). No larger omission is possible. The stated polynomial, minimum and number of minima follow.

**3. Reconfiguration identification.** At minimum, both omission classes contain two indices and are disjoint. A token jump on the selected vertices changes exactly one omitted member from one class to another index; to preserve disjointness the arriving index must belong to the set of \(n-4\) unused indices. Conversely every such one-coordinate exchange is legal. There are four choices of the departing omission index and \(n-4\) choices of an unused index, giving degree \(4(n-4)\). Double counting edges gives \(2(n-4)N_n\). A token slide between \(a\) and \(b\) would change the number of omissions on both shores, contradicting their necessary minimum counts of two, so no token slide preserves a minimum set.

**4. Distance.** Color each index of \([n]\) by \(1\) if in \(U\), by \(2\) if in \(W\), and by \(0\) otherwise. Exactly two indices have each nonzero color. A legal exchange swaps a nonzero color with a zero at arbitrary two indices. Let \(b=4-|U\cap U'|-|W\cap W'|\), the number of initially occupied positions whose colors disagree with the goal. Every such original colored position must be vacated at least once, hence at least \(b\) moves are necessary.

Construct a balanced directed multigraph on colors \(0,1,2\): for each miscolored index add an arrow from its initial color to its desired color. Both initial and final color profiles are \((n-4,2,2)\), so each color's in- and outdegrees are equal. Whenever some zero position changes to nonzero, this graph has arrows involving \(0\). All nontrivial arrows belong to the same nonisolated connected component: any cycle on \(1,2\) intersects a color incident to \(0\). Hence all arrows admit one or several directed closed walks based at \(0\), which may be processed consecutively. For each walk, begin at an initially vacant position needing a nonzero color; move a token of that color from the index whose desired color is the next color along the walk, and repeat, terminating at an index required to be vacant. In each such walk every originally misplaced occupied index is moved once and no correctly placed occupied index is touched. The total is exactly \(b\) moves.

If the two occupied unions coincide but the configurations differ, every miscolored position changes between colors \(1\) and \(2\), and there are no arrows incident to \(0\). Because their color counts agree, the nontrivial arrows form a balanced two-color circuit. A currently zero and finally zero index (present because \(n\ge5\)) acts as a temporary buffer: move one mismatched token into it, rotate the remaining mismatched tokens through the successive holes, and finally move the buffered token into the last hole. This takes precisely \(b+1\) moves. Conversely, the first move necessarily fills a position that should ultimately be zero; its occupant must subsequently be moved again. Thus at least one extra move beyond the \(b\) vacatings is unavoidable. The formula follows. In particular, the disjoint full swap \((U,W)\mapsto(W,U)\) has distance \(5\), while every other target lies at distance at most \(4\), proving diameter and unique antipode.

**5. Distance distribution.** Fix source \((U,W)\). Introduce bookkeeping variables \(u,v\) for the two target color counts. The polynomial
\[
B_n(t)=[u^2v^2](u+tv+t)^2(tu+v+t)^2(1+u+v)^{n-4}
\]
counts each target with weight \(t^b\). The six targets having the same occupied union include the source, four partial swaps with baseline \(b=2\), and one full swap with baseline \(b=4\). The distance correction from Step 4 therefore yields
\[
P_n(t)=B_n(t)+4(t^3-t^2)+(t^5-t^4).
\]
Expanding the coefficient gives the displayed degree-five polynomial. The action of simultaneous index permutations on both classes is transitive on minimum configurations, so the shell polynomial is independent of the source.

## Verification
The included standalone `verify_crown_superdom.py` uses only Python's standard library. It independently constructs original crown-graph neighborhoods, tests the witness condition on all subsets for \(4\le n\le8\), and compares every coefficient with the theorem. It constructs the minimum-configuration exchange graph and computes exact breadth-first distances from a reference state for \(4\le n\le10\), comparing every target against the metric. Symmetric transitivity then covers all ordered configuration pairs for these finite sizes. The script terminates with `VERIFY_OK`; this finite computation does not replace the proof above.

## Relationship to prior work
Ghanbari, Jäger and Lehtilä (2022), *Super Domination: Graph Classes, Products and Enumeration*, study super domination and enumerate minimum super dominating sets of paths, cycles and other graph classes, establishing the enumerative motivation. Bousquet and coauthors (2022) survey domination-set reconfiguration under token jumping and token sliding. The general colored-token swapping framework of Yamanaka and coauthors (2018) includes much more general configurations on complete graphs, but does not by itself characterize which configurations arise as minimum super dominating sets of crown graphs or give the stated family-specific enumerator and distance-shell counts. The novelty assessment concerns precisely the crown-graph classification and its combined enumeration and reconfiguration consequences, not the generic definitions of super domination or token swapping.

## Limitations
No claim is made for \(n<4\), for nonminimum reconfiguration distances, or for other domination predicates. The exact distance proof exploits precisely two nonzero color classes and at least one vacant ground index. A prior equivalent result may exist outside indexed literature, and generic colored-token swapping algorithms could imply the metric component after nontrivial specialization; independent literature and proof review remain outstanding.

## References
1. N. Ghanbari, G. Jäger, T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, first public September 5, 2022, arXiv:2209.01795, https://arxiv.org/abs/2209.01795.
2. N. Bousquet et al., *A survey on the parameterized complexity of the independent set and (connected) dominating set reconfiguration problems*, 2022, arXiv:2204.10526, https://arxiv.org/abs/2204.10526.
3. K. Yamanaka, T. Horiyama, J. M. Keil, D. Kirkpatrick, Y. Otachi, T. Saitoh, R. Uehara and Y. Uno, *Swapping colored tokens on graphs*, Theoretical Computer Science 729 (2018), 1–10, https://doi.org/10.1016/j.tcs.2018.03.016.
