# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

For a complete multipartite graph, the first inspected vertex determines the
entire random greedy maximal independent set: its whole part is accepted and
every vertex in every other part is rejected. This gives the exact
size-biased part-size distribution and the moment formula directly.

The extremal proof was checked separately from that distributional
observation. Conditioning away from a largest part gives a two-level
law-of-total-variance decomposition. The inequality
\[
\operatorname{Var}(Z)\le(M-\mathbb EZ)(\mathbb EZ-1)
\]
follows directly from \((Z-1)(M-Z)\ge0\). When the largest part has size at
least \(n/2\), the resulting quadratic expression is maximized only when every
other part is a singleton. If the largest part is smaller than \(n/2\), a
bounded-range variance estimate is beaten by an explicit complete split graph,
so such a partition cannot be globally extremal. The remaining
one-dimensional objective
\[
g_n(a)=a(n-a)(a-1)^2
\]
has discrete difference
\[
g_n(a+1)-g_n(a)=-a(4a^2-3na+n),
\]
which gives the stated unique maximizer. The possible integer tie at the
positive root is excluded by the divisibility condition \(3a-1\mid4\).

Boundary cases \(n=3\), \(M=n/2\), bipartite graphs, equal-sized parts, and
singleton parts were checked explicitly. A standalone verifier exhaustively
simulates all vertex orders for all connected complete multipartite types up
to order 8 and enumerates all multipartite types through order 40 for the
extremal statement. Computation is supporting evidence and is not required by
the proof.

## Originality

Originality is assessed **to the best of our knowledge**.

The directly relevant recent source is M. Shaikh, arXiv:2609.14826 (2026),
whose accessible abstract states a sharp variance bound for triangle-free
graphs and connected-star equality. The full text was not inspected here.
That restriction does not cover complete multipartite graphs with three or
more nonempty parts, although an uninspected special-case discussion remains a
residual risk.

The open full-text article of Krivelevich--Mészáros--Michaeli--Shikhelman on
random greedy maximal independent sets was inspected in its accessible HTML;
searches within it found no occurrence of "multipartite", "complete
bipartite", or "complete split". The article does discuss variance decay of the
greedy independence ratio for broad graph sequences, but not the finite-order
complete-multipartite extremum stated here; its main applications concern paths,
random graphs, random trees, sparse random planar graphs, and trees.

External searches also used combinations and synonymous formulations of:

- random greedy / greedy maximal independent set;
- complete multipartite and complete split graphs;
- complete bipartite graphs;
- variance and higher moments;
- random sequential adsorption;
- size-biased part-size distributions.

No equivalent or stronger theorem giving the sharp finite-order variance
maximum over complete multipartite graphs was found. The observation that the
first part wins is elementary, and the exact complete bipartite behavior is
not claimed as novel. The originality claim is specifically the finite-order
extremal classification, unique complete-split maximizer, and its asymptotic
constant.

The principal residual risks are an uninspected calculation in
arXiv:2609.14826, older random-sequential-adsorption literature using different
terminology, and very recent parallel work.

## Value

Variance of the random greedy MIS size has just become an explicit extremal
object in the recent triangle-free work. Complete multipartite graphs give a
natural dense test family in which the entire distribution is exactly
tractable, yet optimizing its variance is a nontrivial integer-partition
problem.

The result gives a sharp answer for every order \(n\), a unique extremal graph,
and a new asymptotic constant \(27/256\). It also explains the complete
bipartite specialization of the recent triangle-free bound: the bound becomes
\(|a-b|\le n-2\), with equality exactly for stars.

## Limitations

The theorem concerns connected complete multipartite graphs and \(n\ge3\).
It does not address the global maximum over all graphs or constraints such as a
fixed edge count or fixed chromatic number. The cited 2026 preprint was checked
through its accessible abstract rather than its full text. Originality remains
to the best of our knowledge, and independent audit has not been performed.
