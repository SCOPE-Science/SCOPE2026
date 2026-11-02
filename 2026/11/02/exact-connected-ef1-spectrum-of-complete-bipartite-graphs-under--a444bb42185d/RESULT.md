# Exact connected EF1 spectrum of complete bipartite graphs under arbitrary monotone valuations

## Finding

**Theorem.** Let \(1\le a\le b\) be integers, let \(G=K_{a,b}\) have bipartition \(L\sqcup R\), with \(|L|=a\) and \(|R|=b\), and let \(1\le n\le a+b\). The following statement holds for **every** profile of \(n\) normalized, nonnegative, monotone valuations (possibly different and nonadditive): the vertices admit a partition into \(n\) nonempty connected bundles that is ordinary EF1 **if and only if**

\[
 n\in\{1,2,\ldots,a\}\ \cup\ \{b,b+1,\ldots,a+b\}.
\]

In fact, whenever \(n\ge b\), there is a connected \(\mathrm{EF1}_{\mathrm{outer}}\) allocation in which every bundle has at most two vertices, constructed using only singleton-value queries. For \(a<n<b\), *even identical unit additive valuations* make connected ordinary EF1 impossible. Thus the forbidden interval contains exactly \(\max\{b-a-1,0\}\) agent counts.

The low-agent existence range was already established by the result cited in Reference 2. The new contribution is the unrestricted-value, high-agent construction and hence the assembled exact spectrum (including a possibly unbounded forbidden interval).

## Assumptions and scope

A connected bundle is a nonempty vertex set inducing a connected subgraph of \(G\). For each agent \(i\), a valuation is a function \(v_i:2^{V(G)}\to\mathbb R_{\ge0}\) with \(v_i(\varnothing)=0\), monotone in set inclusion; no additivity, continuity, homogeneity, or commonality is assumed. It is sufficient that valuations be defined on connected subsets and the empty set. An ordinary EF1 allocation \((A_1,\ldots,A_n)\) has, for every ordered pair of distinct agents \(i,j\), some \(g\in A_j\) satisfying \(v_i(A_i)\ge v_i(A_j\setminus\{g\})\). Under \(\mathrm{EF1}_{\mathrm{outer}}\), the removed good must also leave \(A_j\setminus\{g\}\) connected (or empty). The case \(n>a+b\), which would require empty bundles, is excluded by assumption.

## Proof

**1. The low-agent range.** At \(n=1\), assign all vertices to the sole agent. For \(2\le n\le a\le b\), Proposition 4.8 of Bei, Igarashi, Lu and Suksompong (Reference 2) proves connected EF1 on \(K_{a,b}\) for arbitrary monotone valuations whenever both side sizes are at least \(n\). This proves the first existence range without asserting it is new.

**2. The high-agent construction.** Assume \(b\le n\le a+b\), and put \(t=a+b-n\). As \(a\le b\), we have \(0\le t\le a\). Enumerate the agents in any order. In succession, each agent \(i\) chooses a remaining vertex \(p_i\) maximizing her own singleton value \(v_i(\{p\})\). The vertices \(p_1,\ldots,p_n\) are distinct. Temporarily give agent \(i\) the singleton \(\{p_i\}\).

Let \(x\) of the \(t\) unchosen vertices lie in \(L\), and \(y=t-x\) lie in \(R\). There are \(b-y\) chosen vertices in \(R\) and \(a-x\) in \(L\). The inequalities

\[
 x\le b-y\quad\text{and}\quad y\le a-x
\]

both follow from \(x+y=t\le a\le b\). Attach each of the \(x\) unchosen left-side vertices to the bundle of a **different** chosen right-side vertex, and each of the \(y\) unchosen right-side vertices to the bundle of a **different** chosen left-side vertex. There are enough opposite-side chosen vertices by the displayed inequalities. No chosen vertex receives more than one attachment, since an individual chosen vertex lies on exactly one side. Every final bundle is a singleton or one cross-edge; thus all bundles are nonempty and connected, and all vertices are allocated.

For any agents \(i,j\), agent \(i\)'s final bundle \(A_i\) contains \(p_i\), so monotonicity gives \(v_i(A_i)\ge v_i(\{p_i\})\). If \(A_j=\{p_j\}\), remove \(p_j\), leaving the empty set of value zero. Otherwise \(A_j=\{p_j,u\}\), where \(u\) is one of the vertices unchosen after all agents' singleton picks. In particular, \(u\) was still available at the instant agent \(i\) chose \(p_i\). Hence

\[
 v_i(A_i)\ge v_i(\{p_i\})\ge v_i(\{u\})
 =v_i(A_j\setminus\{p_j\}).
\]

Removing \(p_j\) leaves the connected singleton \(\{u\}\); removing it from a singleton leaves the empty set. This establishes \(\mathrm{EF1}_{\mathrm{outer}}\), including for nonadditive valuations. With an oracle for singleton values, straightforward picking takes at most \(n(a+b)\) singleton queries and the two matchings are obtained in linear additional time.

**3. Every intermediate agent count fails.** Assume \(a<n<b\). Give all agents the identical unit additive valuation \(v_i(S)=|S|\). In any connected partition among \(n\) agents, at most \(a\) bundles can intersect \(L\), since the bundles are disjoint and \(|L|=a\). Because \(n>a\), some agent receives only vertices of \(R\); connectivity forces that bundle to be a singleton. Ordinary EF1, applied to this singleton-owning agent, requires that every other bundle have size at most two (otherwise removing one vertex leaves at least two unit-valued vertices and produces strict envy). A connected bundle of size two must consist of one vertex from each part, and there can be at most \(a\) such bundles. Therefore an EF1 partition could cover at most \(n+a\) vertices, strictly fewer than \(a+b\) because \(n<b\), a contradiction. This works at every integer in the open interval. Combining Parts 1--3 proves the theorem. \(\square\)

## Verification

The standalone `verify_biclique.py` uses exact finite integers and a fixed pseudorandom seed. It checked 58,546 possibilities for residual vertex subsets and the required opposite-side matching cardinalities (over \(1\le a\le6\), \(a\le b\le10\)); verified 11,100 high-range allocations across heterogeneous singleton weights, including monotone pair complementarities; and confirmed the counting contradiction in 116 intermediate-range parameter instances. The verifier is **not** the infinite proof: the proof above is symbolic and covers all positive integer parameters. Execute `python verify_biclique.py` with Python 3 and no external packages. No learned or outside certificate is required.

## Relationship to prior work

Bei, Igarashi, Lu and Suksompong (Reference 2), Proposition 4.8, already establish the low range \(n\le a\), and their Theorem 4.9 classifies the special case of three agents on complete bipartite graphs. Chen and Zwicker (Reference 1), Theorem 1, provide a general cutset obstruction from which the intermediate negative range can also be inferred. Their high-agent Observation 2 and Theorem 5 cover at least \(n\ge |V|-1\) and, under a degree condition, \(n=|V|-2\), but not the entire range \(n\ge b=|V|-a\) when \(a\) grows. The construction here gives the entire upper range for arbitrary heterogeneous monotone valuations, even with the stronger outer-vertex condition, and closes the complete spectrum.

Bilò and coauthors (Reference 3) supply foundational results on connected EF1 and EF1 with outer removal for traceable graphs and low agent counts; their traceability hypothesis is not a general substitute for this asymmetric biclique construction. A related 2026 paper (Reference 4) discusses the broader structural setting and tree spectra; its full text was not accessible during this comparison, leaving a publication-priority risk, although no known inspected result directly implies the upper-range statement. Literature searches and database checks are evidence of comparison rather than proof of novelty.

## Limitations

The classification concerns **complete bipartite** item graphs, not arbitrary bipartite or general graphs. Bundles must be nonempty, so there are at most \(a+b\) agents. In the lower range the established Proposition 4.8 ensures ordinary EF1, not the outer-vertex variant; the strengthened outer guarantee is claimed only for the upper range. Access to full text of a plausible 2026 related paper was unavailable; undiscovered equivalent specialized theorems remain a priority risk. No independent audit or theorem-prover certificate is asserted.

## References

1. J. Chen and W. S. Zwicker, *Cutsets and EF1 Fair Division of Graphs*, first arXiv version 2024-02-08, arXiv:2402.05884, https://arxiv.org/html/2402.05884v1 . Especially Theorem 1 and Section 5.
2. X. Bei, A. Igarashi, X. Lu and W. Suksompong, *The Price of Connectivity in Fair Division*, first arXiv version 2019-08-15, arXiv:1908.05433, https://arxiv.org/abs/1908.05433 . Especially Proposition 4.8 and Theorem 4.9.
3. V. Bilò et al., *Almost Envy-Free Allocations with Connected Bundles*, arXiv:1808.09406, https://arxiv.org/abs/1808.09406 .
4. N. Bousquet, F. Connor, A. Totschnig and S. Zeitoun, *Fair Division of Graphs: Beyond Traceability*, arXiv:2608.29902, first posted 2026-08-30, https://arxiv.org/abs/2608.29902 . Abstract available; full text not inspected.
