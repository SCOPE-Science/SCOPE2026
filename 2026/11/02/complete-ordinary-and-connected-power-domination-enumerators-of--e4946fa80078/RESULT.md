# Complete ordinary and connected power-domination enumerators of rook graphs

## Finding

For integers \(m,n\ge 2\), let \(R_{m,n}=K_m\square K_n\) be the rook graph with vertex set \([m]\times[n]\), adjacent cells sharing a row or column. A nonempty initial sensor set \(S\) is *power dominating* if closed-neighborhood observation followed by repeated unique-unobserved-neighbor forcing observes every cell. Write \(r(S)\) and \(c(S)\) for the numbers of rows and columns met by \(S\).

**Structural theorem.** Every \(S\subseteq V(R_{m,n})\) is power dominating exactly when
\[
 r(S)\ge m-1\quad\text{or}\quad c(S)\ge n-1.
\]
Every successful placement finishes after the initial domination step or after one further parallel forcing step; no successful placement needs two forcing steps.

Let \(F_{r,c}(z)\) enumerate edge subsets of \(K_{r,c}\) by cardinality that meet every vertex on both sides. For \(r,c\ge0\) set
\[
F_{r,c}(z)=\sum_{i=0}^{r}\sum_{j=0}^{c}(-1)^{i+j}\binom ri\binom cj(1+z)^{(r-i)(c-j)}.
\]
In particular, \(F_{0,0}=1\), and \(F_{r,0}=F_{0,c}=0\) for a positive opposite index. The complete power-domination polynomial is
\[
\boxed{\mathcal P_{m,n}(z)=\sum_{\substack{0\le r\le m,\ 0\le c\le n\\ r\ge m-1\ \mathrm{or}\ c\ge n-1}}\binom mr\binom ncF_{r,c}(z)
=(1+z)^{mn}-\sum_{r=0}^{m-2}\sum_{c=0}^{n-2}\binom mr\binom ncF_{r,c}(z).}
\]
The coefficient \([z^k]\mathcal P_{m,n}(z)\) counts *every* power-dominating subset of cardinality \(k\), including those whose induced subgraph is disconnected.

For the connected refinement, let \(Q_{r,c}(z)\) count connected spanning subgraphs of the complete bipartite graph \(K_{r,c}\), with \(z\) marking selected edges. Its coefficients are explicitly specified by the formal-power-series identity
\[
\sum_{r,c\ge1}\frac{Q_{r,c}(z)}{r!c!}x^r y^c
=\log\!\left(\sum_{r,c\ge0}\frac{(1+z)^{rc}}{r!c!}x^r y^c\right)-x-y.
\]
Here all algebra is over the rational formal power series ring in \(x,y,z\). Then the complete *connected* power-domination polynomial is
\[
\boxed{\mathcal P^{\mathrm{conn}}_{m,n}(z)=\sum_{\substack{1\le r\le m,\ 1\le c\le n\\ r\ge m-1\ \mathrm{or}\ c\ge n-1}}\binom mr\binom ncQ_{r,c}(z).}
\]
Thus both the unrestricted and connected cardinality distributions are determined, for all rectangle dimensions, by finite sums and explicit formal-series coefficients.

The minimum degree of both polynomials equals \(d=\min(m,n)-1\). The numbers of minimum sensor sets, denoted \(N_{m,n}\) and \(N^{\mathrm{conn}}_{m,n}\), are
\[
N_{m,n}=\begin{cases}m n^{m-1},&2\le m<n,\\2m^m-m^2(m-1)!,&m=n,\end{cases}
\quad
N^{\mathrm{conn}}_{m,n}=\begin{cases}mn,&2\le m<n,\\4,&m=n=2,\\2m^2,&m=n\ge3.\end{cases}
\]
The formulas for \(m>n\) follow by interchanging the factors. Moreover, *every* \(k\)-vertex subset is power dominating for all \(k>(m-2)(n-2)\), and this threshold is sharp: a failed set of exactly \((m-2)(n-2)\) vertices exists, including the empty set for a dimension two.

## Assumptions and scope

All graphs are finite, simple, and labeled by their stated row and column coordinates. Power domination uses the standard initial closed-neighborhood observation \(N[S]\), followed by the rule that an observed vertex with exactly one unobserved neighbor forces that neighbor. For the time assertion, a *parallel forcing step* applies all eligible forces simultaneously. The connected refinement requires \(R_{m,n}[S]\) to be connected, with a single selected vertex regarded as connected. The empty set is never power dominating for \(m,n\ge2\). Graphs of dimension one are deliberately excluded. Counting is by distinct labeled vertex subsets, not up to automorphism. The formula for \(Q_{r,c}\) uses formal series, with coefficient extraction degree bounded by the desired values of \(r,c\).

## Proof

**1. Observation rectangle.** Let \(A\subseteq[m]\) and \(B\subseteq[n]\) be the sets of rows and columns not met by \(S\), of cardinalities \(a=m-r(S)\) and \(b=n-c(S)\). A cell lies in \(N[S]\) precisely when its row or its column meets \(S\). Hence the unobserved cells after the domination step are *exactly* \(A\times B\).

If \(a,b\ge2\), an observed vertex in a row outside \(A\) and a column in \(B\) has exactly \(a\ge2\) unobserved neighbors. An observed vertex in a row in \(A\) and a column outside \(B\) has exactly \(b\ge2\) unobserved neighbors. Any other observed vertex has no unobserved neighbor. Thus no force is possible, and observation never completes. If \(a=0\) or \(b=0\), nothing remains unobserved. If \(a=1\) and \(b\ge1\), for every column \(j\in B\), select any row \(i\notin A\), which exists since \(S\ne\varnothing\). The observed vertex \((i,j)\) has exactly one unobserved neighbor, namely the cell in \(A\times\{j\}\). All missing cells are forced in one parallel step. The case \(b=1\) is symmetric. For \(S=\varnothing\), both \(a=m\ge2\) and \(b=n\ge2\), and failure follows from the first case. This proves the exact structural theorem and time bound.

**2. Complete ordinary polynomial.** To have exactly \(r\) used rows and \(c\) used columns, first choose them in \(\binom mr\binom nc\) ways. The selected cells must then meet every one of those rows and columns. Inclusion-exclusion over unused rows and columns gives precisely \(F_{r,c}(z)\). The success criterion from step 1 imposes \(r\ge m-1\) or \(c\ge n-1\), yielding the first sum. Subtracting its disjoint complementary support profiles from the polynomial \((1+z)^{mn}\) of all subsets gives the second sum. Both include their correct empty-set contribution: it is removed once from the failure sum.

**3. Connected refinement.** Regard each selected cell \((i,j)\) as an edge between the row vertex \(i\) and column vertex \(j\) of \(K_{m,n}\). The selected rook subgraph is the line graph of the corresponding bipartite edge graph \(H\). Since the vertices of \(H\) used in its nonempty edge set have no isolates, the line graph is connected exactly when \(H\) is connected. Thus for fixed row/column support of sizes \(r,c\), connected choices are counted by \(Q_{r,c}(z)\).

For completeness, the bivariate exponential formula decomposes every labeled bipartite edge graph into connected components. The EGF for all such graphs, with \(r\) labeled row vertices and \(c\) labeled column vertices, is \(\sum_{r,c\ge0}(1+z)^{rc}x^r y^c/(r!c!)\): each possible edge is independently absent or present with weight \(z\). Its formal logarithm selects one connected component; the terms \(x,y\) are singleton vertices without edges and must be removed. All remaining components meet both shores and are counted by \(Q_{r,c}\). Summing these over the same success support profiles gives the stated connected polynomial. This establishes the formula with no assumptions about how many cycles the selected incidence graph contains.

An alternative all-integer recurrence, useful for exact computation, sets \(U_{r,c}(z)=(1+z)^{rc}\), \(Q_{1,0}=1\), \(Q_{r,0}=0\) when \(r>1\), and for every \(r\ge1,c\ge0\) decomposes by the component containing the first row vertex:
\[
U_{r,c}(z)=\sum_{i=1}^r\sum_{j=0}^c\binom{r-1}{i-1}\binom cj Q_{i,j}(z)U_{r-i,c-j}(z).
\]
The term \((i,j)=(r,c)\) determines \(Q_{r,c}\) recursively.

**4. Smallest sets and extremal counts.** The success condition forces at least \(m-1\) selected cells or at least \(n-1\), so the minimum is \(\min(m,n)-1\). For \(m<n\), a minimum set has one selected cell in each of \(m-1\) distinct rows: choose the omitted row in \(m\) ways and one of \(n\) columns independently for each selected row, giving \(m n^{m-1}\). Its induced rook graph is connected precisely when all selected cells occupy the same column, giving \(mn\) choices. For \(m=n=q\), minimum sets are the union of the distinct-row and distinct-column types. Each has \(q^q\) choices; their intersection consists of \(q-1\) nonattacking cells, counted by \(q^2(q-1)!\). This proves the ordinary count. The connected types are complete partial columns or rows, with \(q^2\) choices each. Their intersection exists only for \(q=2\), when the chosen set is a singleton, giving the claimed connected counts. Finally, a failed set uses at most \(m-2\) rows and \(n-2\) columns, hence at most \((m-2)(n-2)\) cells; taking the whole rectangle on those supports attains the bound (the empty rectangle when a dimension is two).

## Verification

The included standalone `verify.py` independently constructs rook-graph adjacency lists, enumerates all nonempty vertex subsets in eight test graphs, simulates the closed-neighborhood step and every subsequently available forcing move to exhaustion, and checks connectivity by graph search. It compares every ordinary coefficient with the inclusion-exclusion formula and every connected coefficient with an integer connected-bipartite-graph recurrence; the latter is different from the logarithmic EGF representation. The program also compares minimum-set multiplicities and counts the number of forcing waves for each successful subset. The cases are \((m,n)=(2,2),(2,3),(2,4),(2,6),(3,3),(3,4),(3,5),(4,4)\), totaling exactly 107336 nonempty labeled subsets. The program reports `VERIFY_OK` and checks the additional six connected-polynomial cases against the recurrence. For instance,
\[
\mathcal P_{3,3}(z)=36z^2+84z^3+126z^4+126z^5+84z^6+36z^7+9z^8+z^9,
\]
whereas
\[
\mathcal P^{\mathrm{conn}}_{3,3}(z)=18z^2+42z^3+81z^4+117z^5+84z^6+36z^7+9z^8+z^9.
\]
These finite tests corroborate but do not replace the all-parameter proof above. Run `python3 verify.py` with Python 3 and its standard library only.

## Relationship to prior work

Brimkov, Patel, Suriyanarayana, and Teich introduced the power-domination polynomial and developed general structural results and explicit computations for several graph families in a preprint of 28 May 2018 (arXiv:1805.10984). Their inspected full-text treatment does not enumerate the full two-factor complete Cartesian product family in the present theorem. Brimkov, Mikesell, and Smith introduced and studied connected power domination (arXiv:1712.02388, 6 December 2017); their full text addresses general complexity, structural operations, trees, block graphs, and cactus graphs, rather than this complete rook-graph cardinality distribution. Earlier work of Koh and Soh determined the *scalar* ordinary power-domination number of Cartesian products of two complete graphs. Ganesamurthy, Jeyaranjan, and Srimathi later determined the matching scalar **connected** power-domination number, in Theorem 10 of their preprint of 11 May 2022 (arXiv:2205.05274). Both previously known minimum values are credited, not claimed as new. The contribution here is the exact all-cardinality ordinary and connected distribution, the one-step dynamics, and extremal multiplicities. The line-graph formulation \(R_{m,n}=L(K_{m,n})\) is an equivalent description of the objects, not evidence of a separate novelty claim.

## Limitations

No claim is made about arbitrary Cartesian products, general graph products, or power domination with a different propagation rule. The full-polynomial formulas use finite inclusion-exclusion and formal-coefficient extraction, not a uniform low-degree expression independent of \(m,n\). Connectedness refers to the induced subgraph of sensor locations, not to intermediate observed vertices. Finite enumeration only covers the stated test cases; the proof supplies the infinite extension. The novelty search included the available literature and mathematical research records but cannot certify global publication priority. The 2016 journal source's full text was not continuously retrievable through the publisher during the comparison, so a bibliographic priority risk remains.

## References

1. B. Brimkov, R. Patel, V. Suriyanarayana, and A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1, 28 May 2018. https://arxiv.org/html/1805.10984v1
2. B. Brimkov, D. Mikesell, and L. Smith, *Connected power domination in graphs*, arXiv:1712.02388v1, 6 December 2017. https://arxiv.org/abs/1712.02388
3. S. Ganesamurthy, J. Jeyaranjan, and R. Srimathi, *Connected power domination number of product graphs*, arXiv:2205.05274v1, 11 May 2022. https://arxiv.org/abs/2205.05274
4. K. M. Koh and K. W. Soh, *Power domination of the Cartesian product of graphs*, AKCE International Journal of Graphs and Combinatorics 13 (2016), 22–30. https://doi.org/10.1016/j.akcej.2016.02.004
