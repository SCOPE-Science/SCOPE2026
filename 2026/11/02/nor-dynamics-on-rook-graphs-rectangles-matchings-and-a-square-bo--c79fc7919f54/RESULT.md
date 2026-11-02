# NOR dynamics on rook graphs: rectangles, matchings, and a square-board gap

## Finding

Let \(a,b\ge2\) be integers and let \(R_{a,b}=K_a\square K_b\) be the labelled rook graph with vertex set \([a]\times[b]\): two different squares are adjacent precisely when they share a row or column. For a set \(S\) of active squares, synchronous **open-neighborhood NOR** sends it to
\[
F(S)=\{v:N(v)\cap S=\varnothing\}.
\]
The state of \(v\) itself is **not** an input at \(v\). The following is a complete classification of periodic states, together with an exact orbit census.

Call a set of squares a *partial matching* if no two share a row or column. For \(r,c\ge1\), call \(A\times B\), with \(|A|=r\) and \(|B|=c\), a full \(r\)-by-\(c\) rectangle. Put
\[
\eta(p,q)=
\begin{cases}
1,&p=q=0,\\
1,&p\ge1,\ q\ge1,\ p+q\ge3,\\
0,&\text{otherwise},
\end{cases}
\]
and, for all \(a,b\ge2\), define
\[
M_{a,b}=\sum_{k=0}^{\min(a,b)}\binom ak\binom bk k!
-\mathbf1_{a=b}\,a\,a!,
\]
\[
T_{a,b}=\sum_{r=1}^a\sum_{c=1}^b
\mathbf1_{rc\ge2}\binom ar\binom bc
\sum_{k=0}^{\min(a-r,b-c)}
\binom{a-r}{k}\binom{b-c}{k}k!\,
\eta(a-r-k,b-c-k).
\]

**Classification.** Every state reaches a fixed state or a primitive two-cycle after at most one update. A state is periodic if and only if its active set is exactly one of the following, with no duplication between cases:

1. A partial matching of any size, except a matching of size \(a-1\) on a square board with \(a=b\).
2. A disjoint union \((A\times B)\mathbin{\dot\cup}I\), where \(|A||B|\ge2\), \(I\) is a partial matching using no row of \(A\) and no column of \(B\), and \(\eta(a-|A|-|I|,b-|B|-|I|)=1\).

There are exactly \(P_{a,b}=M_{a,b}+T_{a,b}\) labelled periodic states, of which
\[
E_{a,b}=\frac{\max(a,b)!}{|a-b|!}
\]
are fixed. Hence the number of distinct primitive temporal two-cycle orbits (the two phases counted once) is
\[
\boxed{Q_{a,b}=\frac12\left(M_{a,b}+T_{a,b}-\frac{\max(a,b)!}{|a-b|!}\right).}
\]
In particular, for the two-row family,
\[
\boxed{Q_{2,b}=2^b-1\quad(b\ge3),\qquad Q_{2,2}=1.}
\]
The exclusion of size-\(a-1\) partial matchings occurs **only** on square boards, and is the precise boundary at which the otherwise complete matching layer fails to be recurrent.

## Assumptions and scope

The graph is finite, undirected, simple and loopless; rows and columns are labelled. The rule is simultaneous at all sites and uses the open neighborhood, not the closed neighborhood and not a sequential update. The state space is \(\{0,1\}^{ab}\); a primitive orbit is counted modulo phase shift, not modulo row/column permutations. The theorem applies to all integers \(a,b\ge2\), including \(a=b=2\); no assertion is made about other Boolean local rules or higher-dimensional rook graphs.

## Proof

**1. General one-step entry.** For any finite undirected graph, \(F\) is order-reversing under inclusion. Moreover \(S\subseteq F^2(S)\): if \(v\in S\), every neighbor of \(v\) receives zero in \(F(S)\), so \(v\in F^2(S)\). Consequently \(F^3(S)\subseteq F(S)\). Applying \(S\subseteq F^2(S)\) with \(F(S)\) in place of \(S\) gives \(F(S)\subseteq F^3(S)\). Thus \(F^3=F\). Every image state \(Y=F(S)\) satisfies \(F^2(Y)=Y\), and conversely every periodic state lies in the image. Therefore \(\operatorname{Per}(F)=\operatorname{im}(F)\), with all periods dividing two and first entry at time at most one.

**2. Rook-image lemma.** For an arbitrary starting set \(S\), let \(A\) be its completely empty rows and \(B\) its completely empty columns. Let \(I\subseteq S\) consist of active squares with no other active square in their row or column. For a square \(v=(i,j)\), absence of active *other* squares in its row and column occurs in precisely two mutually exclusive situations: (i) its row and column are empty, or (ii) \(v\in S\) is isolated from all other active squares in the rook graph. Therefore
\[
F(S)=(A\times B)\mathbin{\dot\cup}I.
\]
The members of \(I\) form a partial matching disjoint from the selected rows and columns of \(A\times B\).

**3. Realizability.** Conversely prescribe empty-row and empty-column sets \(A,B\), and an isolated-rook matching \(I\) avoiding them. Write \(r=|A|\), \(c=|B|\), \(k=|I|\), \(p=a-r-k\), \(q=b-c-k\). After the designated empty rows/columns and isolated active cells have been removed, all remaining \(p\) rows and \(q\) columns must each contain an active square, but no remaining active square can be isolated in both its row and column. This is possible exactly when \(p=q=0\) or \(p,q\ge1\) with \(p+q\ge3\). The necessity follows because an unused row or column would contradict the prescribed empty-row/column sets; a single residual row and column would force one isolated square. Sufficiency follows by filling the whole residual \(p\times q\) block when both positive (its squares have an active neighbor if \(p+q\ge3\)), or leaving it empty when \(p=q=0\). Hence realizability is equivalent to \(\eta(p,q)=1\).

**4. Unique counting of nonmatching images.** If \(|A||B|\ge2\), the filled rectangle is a single nontrivial connected component of the induced rook graph on \(F(S)\). Every vertex of \(I\) is isolated in that induced graph. Thus the rectangle, its row set, its column set, and \(I\) are uniquely recoverable from the image. Choosing \(A,B\) contributes \(\binom ar\binom bc\), and choosing a size-\(k\) matching on their complementary rows and columns contributes \(\binom{a-r}{k}\binom{b-c}{k}k!\). The realizability condition supplies the factor \(\eta\). Summing gives \(T_{a,b}\) without double counting.

**5. The matching boundary.** If the image is a partial matching of size \(k\), it cannot contain a rectangle of more than one square. When \(k=\min(a,b)\), taking \(S\) to be the matching itself gives \(F(S)=S\): every row or every column is occupied and the rectangle of empty rows times empty columns vanishes. If \(k<\min(a,b)\), let \(p=a-k\) and \(q=b-k\). When \(p+q\ge3\), take \(S\) to consist of the prescribed matching plus the full complementary \(p\times q\) block. No row or column of \(S\) is empty; the matching squares are its only isolated active squares, so \(F(S)\) is precisely the matching. When \(p=q=1\), equivalently \(a=b=k+1\), no generating state exists: its prospective empty-row/column rectangle must either be empty or be a single square belonging to the requested matching. In the first case the one residual row and column force an extra isolated active square; in the second case, after assigning the chosen square to the rectangle, one residual row and column again force an extra isolated active square. Any larger nonempty rectangle would introduce adjacent output squares, contradicting the matching condition. Therefore exactly the near-perfect matchings on square boards are excluded. The number of size-\(k\) matchings is \(\binom ak\binom bk k!\), and for \(a=b\) the excluded size-\(a-1\) layer contains \(a^2(a-1)!=a\,a!\) matchings. This gives \(M_{a,b}\).

**6. Fixed states and orbit counts.** A fixed state \(S=F(S)\) is necessarily independent: an active square with an active neighbor would be switched off. It is also dominating in the ordinary closed-neighborhood sense: every inactive square must have an active neighbor, or it would be switched on. Thus fixed states are exactly maximal independent sets of the rook graph. They are the partial matchings occupying every row or every column; otherwise an unused row and an unused column permit an additional rook. Each has size \(\min(a,b)\), and their number is \(\max(a,b)!/|a-b|!\). All other image states form disjoint two-cycles by Step 1, so \(Q_{a,b}=(P_{a,b}-E_{a,b})/2\).

**7. Two-row simplification.** Suppose \(a=2\), \(b\ge3\). Direct use of the rook-image lemma partitions the image into disjoint types: empty (one), full (one), a nonempty set of at most \(b-2\) squares in just one row (\(2\sum_{j=1}^{b-2}\binom bj\)), a two-rook matching (\(b(b-1)\)), or one rook in one row together with all \(b-1\) squares in the other row outside its column (\(2b\)). These exhaust the cases according to the occupancy counts of the two input rows. Hence
\[
P_{2,b}=2+2\sum_{j=1}^{b-2}\binom bj+b(b-1)+2b
=2^{b+1}-2+b(b-1).
\]
Since \(E_{2,b}=b(b-1)\), this proves \(Q_{2,b}=2^b-1\). For \(b=2\), the final two described types coincide and must not be counted twice: directly \(P_{2,2}=4\), \(E_{2,2}=2\), and \(Q_{2,2}=1\).

## Verification

The included standalone C++17 source `verify_rook_nor.cpp` independently computes the NOR map using row and column occupancies, enumerates all configurations on fifteen rook graphs with \(2\le a\le4\), \(a\le b\le10\), and \(ab\le20\), tests \(F^3(S)=F(S)\), independently checks the structural if-and-only-if classification for **every** configuration, and checks the exact binomial formulas, equilibrium count, and two-row corollary. It performed **2,811,728** direct configuration checks and returned `ALL_CHECKS_PASSED`; the observed complete output is in `verification_output.txt`. Run with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_rook_nor.cpp -o verify_rook_nor && ./verify_rook_nor`. Finite tests corroborate but do not replace the all-size argument in the Proof.

## Relationship to prior work

The previously established correspondence between fixed points of all-negative conjunctive networks and maximal independent sets is used in Step 6; it is not claimed as new. Aracena, Richard and Salinas (first public arXiv version July 22, 2015) analyze fixed-point extrema over signings and graph contractions, not this simultaneous rook-graph recurrence census. Aledo, Martinez and Valverde's open-access survey (March 24, 2015) summarizes broad NOR/NAND period restrictions in parallel graph systems, with its standard self-inclusive local dependence; those period restrictions do not give the open-neighborhood rook-image classification or enumerator. Later work of Aledo and collaborators gives general period-point results for minterm/maxterm systems, often with self-inclusive inputs; Gadouleau and Kutner study the same open-neighborhood independent-set network primarily under sequential updates. These works supply context but not the displayed rectangle-plus-matching theorem in the material inspected. The open-neighborhood graph-join NOR identities known for \(G\vee H\) do not yield the rook result, since the rook graph is \(K_a\square K_b=L(K_{a,b})\), not a join, and the present proof uses row-column occupancy and isolated-rook separation.

## Limitations

No independent external mathematical audit has been performed. The literature comparison cannot rule out unindexed historical equivalences, particularly under formal-concept or Boolean-closure terminology. The full text of every potentially relevant historical source was not accessible; a full PDF of the most directly relevant fixed-point primary paper was accessed and its introduction, theorem statements and relevant proof sections inspected, while accessible sections/excerpts of later sources were compared. The formula is for labelled rectangular rook graphs and the specified synchronous **open**-neighborhood NOR rule only. The finite experiment checks \(ab\le20\), whereas the theorem for all \(a,b\ge2\) relies on the elementary structural proof, not extrapolation. It is not claimed that generic period-two restrictions or maximal-independent-set fixed-point correspondences are new.

## References

1. J. A. Aledo, S. Martinez, and J. C. Valverde, "Parallel Dynamical Systems over Graphs and Related Topics: A Survey," *Journal of Applied Mathematics* (2015), article 594294, published March 24, 2015. https://doi.org/10.1155/2015/594294
2. J. Aracena, A. Richard, and L. Salinas, "Fixed points in conjunctive networks and maximal independent sets in graph contractions," arXiv:1507.06141, first public July 22, 2015; later revisions. https://arxiv.org/abs/1507.06141
3. J. A. Aledo et al., "Counting Periodic Points in Parallel Graph Dynamical Systems," *Complexity* (2020), article 9708347. https://doi.org/10.1155/2020/9708347
4. M. Gadouleau and D. C. Kutner, "Generalising the maximum independent set algorithm via Boolean networks," arXiv:2403.17658, first public March 26, 2024; *Information and Computation* **303** (2025), article 105266. https://arxiv.org/abs/2403.17658
