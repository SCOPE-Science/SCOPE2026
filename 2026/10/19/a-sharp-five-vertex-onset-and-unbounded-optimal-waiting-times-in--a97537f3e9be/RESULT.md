# A sharp five-vertex onset and unbounded optimal waiting times in sequential neutral fixation

## Finding

In a neutral death–birth process on three nested connected, simple, undirected population graphs, a **finite interior waiting time can maximize eventual cooperation fixation**, even without any penalty for waiting. Five vertices are the smallest final population for which this can happen. There is, moreover, a natural family of final trees whose unique optimal waiting time diverges logarithmically with population size.

Precisely, start with the single edge on vertices \(0,1\) and choose one of its two vertices uniformly as a cooperator, leaving the other a defector. Evolve for \(g\) copy updates, add defective vertex \(2\) and edges \(01,12\) (the path \(P_3\)), evolve for \(g\) further copy updates, then activate the other defective vertices and all edges of a connected final graph \(G\). The graph induced by \(\{0,1,2\}\) in \(G\) must be exactly \(P_3\). Continue the final process until consensus. Let \(d_0,d_1,d_2\) be the first three degrees in \(G\), and let \(V=\sum_{i\in V(G)}d_i=2|E(G)|\). For every integer \(g\ge0\), the probability of eventual all-cooperator fixation is

\[
F_g=\frac{3(d_0+d_1+d_2)}{8V}+\frac{d_0-d_2}{4V}\left(\frac23\right)^g+\frac{d_1-d_0-d_2}{8V}\left(\frac13\right)^g.
\]

The entire sign pattern of successive changes is exactly

\[
F_{g+1}-F_g=\frac{d_0-d_1+d_2-(d_0-d_2)2^g}{12V\,3^g}.
\]

For \(G\) with vertices \(0,1,2,3,4\) and edges \(01,12,23,30,04\) (a four-cycle with a pendant leaf), the formula becomes

\[
F_g=\frac{21}{80}+\frac1{40}\left(\frac23\right)^g-\frac3{80}\left(\frac13\right)^g,
\qquad F_{g+1}-F_g=\frac{3-2^g}{120\,3^g}.
\]

Consequently \(g=2\) is the **unique global maximizer** over nonnegative integers, with \(F_1=4/15\), \(F_2=97/360\), \(F_3=29/108\), and \(\lim_{g\to\infty}F_g=21/80\). For any sequence of at most four vertices with connected, strictly enlarging induced snapshots, at least two initial vertices and uniform single-cooperator initialization, the finite-wait fixation probability is monotone in \(g\).

Finally, for each integer \(t\ge1\), form a final tree by adding \(t+1\) pendant vertices to vertex \(0\) and \(t\) pendant vertices to vertex \(2\) of the intermediate path. It has \(2t+4\) vertices, and its unique optimal waiting time is

\[
g_{\mathrm{opt}}=\bigl\lceil\log_2(2t+1)\bigr\rceil.
\]

These optimal times are unbounded; this is not merely a small-graph exception.

## Assumptions and scope

Every snapshot is a finite, simple, connected, undirected, unweighted graph, and the vertex sets grow strictly by activation of previously dormant vertices. Each new vertex enters as a defector. On a snapshot with \(m\) active vertices, **one** update consists of selecting an active vertex uniformly with probability \(1/m\) and setting its binary state equal to that of a uniformly selected neighbor. Updates have no mutation and no selection: both types have fitness one. The first two snapshots evolve for exactly the same \(g\) individual updates (including the mathematical boundary \(g=0\)); after final growth the process runs indefinitely. All probability is over the initial uniformly selected cooperator and the independent uniform update/neighbor choices.

The displayed general formula holds for every connected final graph \(G\) with the specified induced initial path, regardless of the number or edges of the newly activated vertices. The minimum-order statement ranges over all connected strictly increasing induced-snapshot sequences that start with at least two vertices, end with at most four, and use the same number of updates on every nonfinal snapshot. The stated tree family is one explicit infinite subfamily, not an assertion of optimality among all possible growth rules. The conclusions do not concern positive selection or arbitrary unequal stage durations.

## Proof

**1. Final fixation is a degree-weighted linear functional.** Write \(X_i\in\{0,1\}\) for the opinion at vertex \(i\) in a connected final graph, and \(d_i\) for the final degree. Under one neutral copy update, the conditional change in \(\sum_i d_iX_i\) is

\[
\frac1{|V(G)|}\sum_i\sum_{j\sim i}(X_j-X_i)=0,
\]

because every undirected edge cancels between its two orientations. Consequently \(M=V^{-1}\sum_i d_iX_i\) is a bounded martingale. On a finite connected graph, the voter process reaches unanimous consensus almost surely: from any nonconstant state, a prescribed finite sequence of neighbor copying along a spanning tree has positive probability of propagating one existing opinion to every vertex, and finitely many configurations give a uniform positive chance of absorption over a bounded block. At consensus \(M\) equals the indicator of complete cooperative fixation. Its initial expectation is therefore exactly the fixation probability. In particular, the new defectors contribute zero, so only the three old vertices' expected states matter when the final stage starts.

**2. Intermediate expectation modes.** Uniformly locating one cooperator on the first edge gives initial coordinate expectations \((1/2,1/2)\). The constant vector is preserved by any neutral copy-update expectation operator, so the expected opinions at vertices \(0,1\) remain \((1/2,1/2)\), independently of the first \(g\) updates. The new middle-stage vertex \(2\) enters with state zero. If \(e_i(k)=\mathbb E[X_i]\) after \(k\) intermediate updates on \(0-1-2\), the exact expectation evolution is

\[
\begin{pmatrix}e_0(k+1)\\e_1(k+1)\\e_2(k+1)\end{pmatrix}
=\begin{pmatrix}2/3&1/3&0\\1/6&2/3&1/6\\0&1/3&2/3\end{pmatrix}
\begin{pmatrix}e_0(k)\\e_1(k)\\e_2(k)\end{pmatrix}.
\]

The eigenvalues are \(1,2/3,1/3\). Applying this matrix to \((1/2,1/2,0)\) and diagonalizing gives the exact identity

\[
\begin{pmatrix}e_0(g)\\e_1(g)\\e_2(g)\end{pmatrix}
=\frac38\begin{pmatrix}1\\1\\1\end{pmatrix}
+\frac14\left(\frac23\right)^g\begin{pmatrix}1\\0\\-1\end{pmatrix}
+\frac18\left(\frac13\right)^g\begin{pmatrix}-1\\1\\-1\end{pmatrix}.
\]

Substituting into \(F_g=V^{-1}\sum_{i=0}^2d_ie_i(g)\) proves the formula; subtracting successive values gives the increment formula.

**3. Five-vertex witness.** In the specified four-cycle-plus-leaf graph the first three final degrees are \((3,2,2)\) and \(V=10\). Substitution yields both displayed rational expressions. The sign of the increment is that of \(3-2^g\): it is positive for \(g=0,1\) and negative for every integer \(g\ge2\). Therefore the unique global optimum is \(g=2\). The three finite values and infinite limit follow by direct substitution. Notice the optimum is intrinsic to fixation probability; no waiting-time cost is included.

**4. Minimality at five vertices.** With only two snapshots, uniform single-cooperator initialization yields the constant vector of one-point expectations \((1/m,\ldots,1/m)\) on the first graph of size \(m\), so that vector is unchanged after any number of updates and the final fixation probability is independent of \(g\). With at least three strictly growing connected snapshots and final size at most four, one necessarily has the sizes \((2,3,4)\), beginning with an edge. The middle induced graph is either a triangle or a three-vertex path. In the triangle, the one-point expectation deviations from their common mean are multiplied by \(1/2\) at every update, so the final fixation probability is a constant plus a single multiple of \((1/2)^g\), hence monotone. In the path, relabeling the intermediate vertices to the order \(0-1-2\), write \(e_i\in\{0,1\}\) for whether vertex \(3\) is connected to old vertex \(i\); at least one \(e_i\) equals one. The degrees of old vertices are \((1+e_0,2+e_1,1+e_2)\). The sign of the fixation increment reduces to

\[
(e_0+e_2-e_1)-(e_0-e_2)2^g.
\]

If \(e_0=e_2\), its sign is independent of \(g\). If \((e_0,e_2)=(1,0)\), the expression is \(1-e_1-2^g\le0\); if \((e_0,e_2)=(0,1)\), it is \(1-e_1+2^g>0\). None can change sign with increasing integer \(g\). Thus all admissible sequences ending on at most four vertices have monotone fixation probability. The five-vertex witness is minimal.

**5. Unbounded optimum on trees.** In the stated family the first three final degrees are \((t+2,2,t+1)\), and \(G\) is a tree with \(2t+4\) vertices and \(2t+3\) edges. Its fixation increment has the sign of \(2t+1-2^g\). Since \(2t+1\) is an odd integer exceeding one, it is never a power of two. Therefore the increment is strictly positive up to \(g=\lceil\log_2(2t+1)\rceil-1\) and strictly negative thereafter, proving the unique optimizer and its divergence with \(t\).

## Verification

The standalone `verify_exact.py` uses only Python standard-library exact rational arithmetic. It checks the path eigen-expansion for 41 integer durations; directly verifies all seven connected ways to add one vertex to a path and all seven ways to add one vertex to a triangle; reproduces the five-vertex fixation probabilities and increment signs; and solves the complete five-vertex \(32\)-state absorbing-voter chain with exact Gaussian elimination, independently of the one-point formula. It additionally checks 100 tree-family members. The program passes **1,416 exact assertions**. Its finite checks are corroboration: the all-sizes statements are proved analytically above, not inferred from enumeration. Run with `python3 verify_exact.py` from the directory containing this document and the embedded code.

## Relationship to prior work

Sheng, Li and Wang (first publicly posted October 12, 2021; journal version 2023) define the same kind of sequential, induced-subgraph population growth and explicitly consider the neutral finite-duration process. Their main article reports monotonically increasing fixation with duration for several simulated synthetic and empirical networks and describes a regular-network sufficient condition for monotonicity in its supporting information. Their analysis of promotion relative to a static network and their numerical monotonicity examples are pre-existing results. Here the different mathematical question is a sharp **nonmonotonicity threshold for arbitrary connected growth schedules**, an explicit five-vertex reversal without an auxiliary time cost, and a family of tree networks with arbitrarily large exact finite optimizers. The standard degree-weighted voter martingale and eigenmode methods are not claimed as new.

Bhaumik and Masuda (2023) analyze fixation under birth–death updating on fixed-size temporally switching networks. Those networks alternate rather than grow, and their update is birth–death rather than the neutral death–birth copying studied here. Their fixation statements do not imply the stated five-vertex minimality or the tree optimizer. Literature and indexed research-record searches have not revealed a directly covering theorem, but searches alone do not establish priority. The source article's supplementary technical text could not be inspected completely; it remains a specific priority risk despite the narrower scope described in the available main text.

## Limitations

The threshold is specific to the neutral copying rule, uniform single-cooperator start, nested connected simple undirected induced graphs, simultaneous arrival of defective newcomers, and the common integer stage duration. The five-vertex minimum excludes isolated singleton stages, for which the prescribed neighbor-copying update is undefined. There is no claim of nonmonotonicity for every graph or for positive selection. It remains possible that a stronger previously published result or inaccessible supplementary calculation subsumes this exact statement. An independent scientific audit has not been performed.

## References

1. Anzhi Sheng, Aming Li, Long Wang. *Evolutionary dynamics on sequential temporal networks*. arXiv:2110.05995, submitted 2021-10-12, https://arxiv.org/abs/2110.05995; *PLOS Computational Biology* 19(8), e1011333 (2023), https://doi.org/10.1371/journal.pcbi.1011333.
2. Jnanajyoti Bhaumik, Naoki Masuda. *Fixation probability in evolutionary dynamics on switching temporal networks*. *Journal of Mathematical Biology* 87, 64 (2023), https://doi.org/10.1007/s00285-023-01987-5.
