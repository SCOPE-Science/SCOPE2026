# Sharp four-step relaxation and exact last-transient basins in bipartite bi-threshold dynamics

## Finding

Let \(F\) be the synchronous closed-neighborhood binary bi-threshold map on \(K_{a,b}\), with \(a,b\ge1\) and the **same** positive integer up-threshold \(u\) and down-threshold \(d\) at every vertex. Put \(h=d-1\). Every labelled initial state satisfies
\[
F^{6}(x)=F^{4}(x).
\]
Consequently every state enters a fixed point or primitive two-cycle in at most four updates. This universal bound is attained for some thresholds and initial state **if and only if** \(\min(a,b)\ge2\) and \(|a-b|\ge2\).

More precisely, let \(i\) and \(j\) be the initial numbers of ones on the shores of sizes \(a\) and \(b\), respectively. Write \(T(x)\) for the first \(t\ge0\) for which \(F^t(x)\) belongs to a periodic orbit. Then \(T(x)=4\) exactly when
\[
u\le \min\{i,a-i,j,b-j\}
\]
and at least one of
\[
\max\{b,i\}<h\le a-i, \qquad \max\{a,j\}<h\le b-j
\]
holds. The two inequalities cannot hold simultaneously. Every state with \(T=4\) enters the same alternating shore-consensus two-cycle \((0^a,1^b)\leftrightarrow(1^a,0^b)\).

Define the finite binomial interval sum (zero for an empty interval)
\[
\mathcal B(n;\ell,r)=\sum_{k=\ell}^{r}\binom nk,
\]
with the convention that terms outside \(0\le k\le n\) vanish. The **exact labelled size of the last-transient layer**, \(N_4(a,b;u,d)=|\{x:T(x)=4\}|\), is
\[
\begin{split}
N_4(a,b;u,d)={}&\mathbf 1_{\{h>b\}}\mathcal B(a;u,\min\{a-h,h-1\})\mathcal B(b;u,b-u)\\
&+\mathbf 1_{\{h>a\}}\mathcal B(a;u,a-u)\mathcal B(b;u,\min\{b-h,h-1\}).
\end{split}
\]
For example, \(K_{4,2}\) with \((u,d)=(1,4)\) has exactly eight initial states first becoming periodic at time four. Neither the global cutoff nor the final-layer formula imposes a bound on graph size or on positive integer thresholds.

## Assumptions and scope

The graph is simple, undirected and complete bipartite with two nonempty labelled shores. Every vertex updates simultaneously. The threshold count includes **the vertex's own old state**: a zero becomes one if its closed-neighborhood count is at least \(u\); a one remains one if that count is at least \(d\), and otherwise becomes zero. The thresholds are uniform across both shores; the theorem does not cover heterogeneous thresholds, asynchronous updates, or open-neighborhood conventions. The input range is \(a,b\in\mathbb Z_{\ge1}\) and \(u,d\in\mathbb Z_{\ge1}\), without further restrictions.

## Proof

**Step 1 (four forms of every shore).** Fix an initial state. On shore \(A\), write \(I\) for its initial set of active vertices, \(|I|=i\); on \(B\), write \(J\) for its initial active set, \(|J|=j\). If the opposing shore currently has \(s\) active vertices, the new state at a vertex of the first shore is
\[
(1-x_v)\mathbf1_{\{s\ge u\}}+x_v\mathbf1_{\{s\ge h\}}.
\]
Hence that entire shore becomes (in order of the two indicator bits) all zeros, all ones, its existing pattern, or its complement. By induction, at every time shore \(A\) is one of \(\varnothing,A,I,A\setminus I\) and shore \(B\) is one of \(\varnothing,B,J,B\setminus J\). Their population counts therefore belong to \(\{0,a,i,a-i\}\) and \(\{0,b,j,b-j\}\), respectively. The sets, rather than their possibly equal population counts, serve as the symbolic labels: this retains the labelled-state dynamics when \(i=a-i\), for example.

**Step 2 (exhaustive order-type lemma).** The comparisons used by the map involve only the seven quantities
\[
0,\ a,\ i,\ a-i,\ b,\ j,\ b-j
\]
and their positions relative to \(u\) and \(h\). Resolve ties in any way compatible with \(0\) first, \(a\) after both \(i,a-i\), and \(b\) after both \(j,b-j\). Such a linear extension always exists: the inequalities are non-strict for actual inputs, but equality groups have identical threshold-comparison bits and can be internally ordered as required. The six nonzero-labelled quantities have exactly \(6!/(3\cdot3)=80\) such strict linear extensions. Since \(u\ge1\), the cut for \(u\) can occupy any of seven positions following \(0\). Since \(h\ge0\), its cut can occupy any of eight positions, including before \(0\). These \(80\cdot7\cdot8=4480\) formal cases therefore **overcover** every actual integer parameter/input configuration; some formal cases need not be arithmetically realizable.

In each case, update the pair of symbolic labels using the four-form rule from Step 1. The accompanying `symbolic_checker.py` exhausts all 4480 cases without enumerating graph sizes. It confirms symbolically that the time-six pair equals the time-four pair in every case. It also confirms the exact equivalence
\[
F^5(x)\ne F^3(x)\quad\Longleftrightarrow\quad
u\le\min\{i,a-i,j,b-j\}\ \land\
\bigl(\max\{b,i\}<h\le a-i\ \lor\ \max\{a,j\}<h\le b-j\bigr).
\]
There are precisely 16 formal exceptional cases, eight for either shore ordering. In all 16, the \(u\)-cut is immediately after zero and the \(h\)-cut follows the fifth item in the ordered list (zero included); the asserted inequalities spell out their two types. The full checker source, rather than an unexplained transcript, is part of the proof certificate.

**Step 3 (entry time and sharp graph criterion).** The identity \(F^6=F^4\) implies that \(F^4(x)\) is periodic with period dividing two. It follows that \(T(x)=4\) if and only if \(F^5(x)\ne F^3(x)\). The equivalence in Step 2 establishes the individual-state criterion. Its first inequalities require both shores to contain at least one zero and one one; thus \(a,b\ge2\). If the first further inequality holds, \(a-i\ge h>b\), so \(a\ge b+2\); the second analogously requires \(b\ge a+2\). Conversely, if \(a\ge b+2\), choose \(u=1,d=b+2,i=j=1\); both shores are mixed and the first inequality is satisfied. Interchanging the shores covers the other imbalance direction. At time four such configurations are at opposite uniform states, which thereafter exchange each step by direct substitution into the update rule.

**Step 4 (last-layer count).** In the first possible orientation \(b<h\), the individual-state criterion reduces to
\[
u\le i\le\min\{a-h,h-1\},\qquad u\le j\le b-u.
\]
There are \(\binom ai\binom bj\) labelled states with these counts. The other orientation is symmetric, and the two are disjoint. Summing their binomial weights proves the displayed formula.

## Verification

Running `python3 symbolic_checker.py` produces an exact order-type certificate: 80 linear extensions, 4480 threshold-cut cases, no counterexample to \(F^6=F^4\), and precisely 16 last-transient symbolic cases. This is exhaustive in the seven-comparison quotient, not an extrapolation from small graph sizes.

Separately, compile `direct_checker.cpp` using `g++ -std=c++17 -O2 -o direct_checker direct_checker.cpp`, and run `./direct_checker`. It evolves the labelled vertex states directly (independent of the symbolic checker) on every \(K_{a,b}\) with \(1\le a,b\le7\), all \(1\le u,d\le\max(a,b)+2\), and all initial bit strings. It checked 2632 graph/threshold combinations and 4,884,036 initial strings, including the binomial count. This finite enumeration is a consistency check; the all-size claim rests on Step 2.

## Relationship to prior work

Kuhlman, Mortveit, Murrugarra and Kumar established the synchronous bi-threshold framework and period-at-most-two theorem in *Bifurcations in Boolean Networks* (2011), arXiv:1108.2974. Their full accessible preprint was examined: the synchronous theorem appears in Section 3.1, and the special graph constructions in Section 4 concern principally asynchronous updates on trees. The established period restriction alone does not bound first-entry times or count a sharp transient layer. The present theorem specializes to uniform thresholds and a complete bipartite graph, giving a sharp size-independent four-step entrance identity and a binomial last-layer census. General majority dynamics and complete-multipartite parity automata are distinct update rules and do not imply these statements.

## Limitations

No formula for all shorter transient layers or the full partition into fixed-point versus two-cycle basins is asserted. The symbolic quotient depends essentially on uniform thresholds and the fact that all vertices in one shore see the same opposite-shore count. This has not been extended to irregular bipartite graphs. A related but different threshold protocol game on complete bipartite graphs was located; its asynchronous/game-theoretic mechanism does not provide the present synchronous theorem. An unindexed historical equivalent cannot be ruled out by database searches. No independent external audit has been performed.

## References

1. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974 (first version 2011-08-15), https://arxiv.org/abs/1108.2974, full PDF https://arxiv.org/pdf/1108.2974.
2. E. Goles and J. Olivos, *Comportement périodique des fonctions à seuil binaires et applications* (1981), period-two background cited and discussed in [1].
3. A. Fedrigo, *End Behavior of the Threshold Protocol Game on Complete and Bipartite Graphs*, *Games* **15** (2024), DOI:10.3390/g15060041; a different update model.
