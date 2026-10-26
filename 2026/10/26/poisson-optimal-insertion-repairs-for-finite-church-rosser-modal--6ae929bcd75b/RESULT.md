# Poisson-optimal insertion repairs for finite Church–Rosser modal frames

## Finding

**Theorem (critical-window optimal insertion repair).** Fix \(t\in\mathbb R\). For sufficiently large \(n\), sample a loop-free directed frame \(R_n\) on \([n]\), inserting each ordered off-diagonal edge independently with probability
\[
p_n=\sqrt{\frac{2\log n+t}{n}}.
\]
Write \(N^+(u)=\{w:R_n(u,w)\}\) and define the set and number of *uncovered successor pairs*
\[
\mathcal B_n=\bigl\{\{u,v\}:u\ne v,\ N^+(u)\cap N^+(v)=\varnothing\bigr\},\qquad Z_n=|\mathcal B_n|.
\]
Let \(K_n\) be the minimum number of missing, nonloop directed edges that must be **added**, without deleting any edge or vertex, for the resulting frame to validate the Church–Rosser axiom \(\Diamond\Box q\to\Box\Diamond q\) for every valuation. Let \(H_n\) count the distinct optimal sets of added edges, with \(H_n=1\) when \(K_n=0\).

With \(\lambda=e^{-t}/2\), the following assertions hold:

1. \(Z_n\Rightarrow\operatorname{Poisson}(\lambda)\) and \(K_n\Rightarrow\operatorname{Poisson}(\lambda)\).
2. With probability tending to one, \(\mathcal B_n\) is a matching, every pair in \(\mathcal B_n\) has a common predecessor, every vertex has outdegree at least two, and **\(K_n=Z_n\)**.
3. On that event, the exact multiplicity of minimum insertion repairs is
\[
H_n=\prod_{\{u,v\}\in\mathcal B_n}
\bigl(d^+(u)+d^+(v)-\mathbf1_{R_n(u,v)}-\mathbf1_{R_n(v,u)}\bigr).
\]
Moreover \(H_n/(2np_n)^{K_n}\to1\) in probability, and the same asymptotic holds conditionally on any fixed value \(K_n=k\). In particular, the limiting probability of frame validity is
\[
\Pr(R_n\models \Diamond\Box q\to\Box\Diamond q)\longrightarrow \exp(-e^{-t}/2).
\]

The novelty claim is **the coincidence of global minimum insertion distance with the Poisson obstruction count, together with the complete optimal-repair multiplicity formula**, rather than the already familiar phenomenon that uncovered pairs of random-graph neighborhoods have Poisson critical windows.

## Assumptions and scope

All frames are finite, labelled, loop-free directed graphs; no edge deletions, self-loop insertions, vertex changes, or modifications of valuations are allowed. Modal operators use classical Kripke semantics; validity means every valuation at every world. For the probability law, \(t\) is fixed and \(n\to\infty\) through values making \(p_n\in(0,1)\). A missing pair has *a common predecessor* when some vertex has directed edges to both its members. The terms \(\mathcal B_n\) and \(Z_n\) concern shared **out-neighbors**, not shared predecessors; these are different properties in a directed frame. The empty product is one.

## Proof

**Modal correspondence.** On any frame, \(\Diamond\Box q\to\Box\Diamond q\) is valid iff
\[
\forall x,y,z\;\bigl(Rxy\wedge Rxz\implies\exists w\,(Ryw\wedge Rzw)\bigr).\tag{1}
\]
For necessity, if two successors \(y,z\) of \(x\) have no common successor, choose a valuation making \(q\) true on the successor set of \(y\) and false elsewhere; the antecedent is true via \(y\) while the consequent is false via \(z\). For sufficiency, a successor \(y\) witnessing \(\Diamond\Box q\) shares a successor with each \(z\) accessible from \(x\), so every such \(z\) satisfies \(\Diamond q\).

**Poisson obstruction law.** For each unordered \(\{u,v\}\), define \(I_{uv}=\mathbf1_{N^+(u)\cap N^+(v)=\varnothing}\). The common successor cannot be \(u\) or \(v\) because loops are excluded, hence
\[
\mathbb EI_{uv}=(1-p_n^2)^{n-2},\quad
\mathbb EZ_n=\binom n2(1-p_n^2)^{n-2}\to\lambda.
\]
For each fixed \(k\) and any \(k\) distinct unordered pairs, consider targets outside their at most \(2k\) endpoints. At any such target, the probability of being a simultaneous out-neighbor of *at least one* prescribed pair is \(kp_n^2+O_k(p_n^3)\): any two distinct pair events require at least three distinct edges. Independence across target vertices, and the fact that the remaining \(2k\) targets contribute a factor \(1+O_k(p_n^2)\), give, uniformly in the configuration of prescribed pairs,
\[
\Pr(I_{u_1v_1}=\cdots=I_{u_kv_k}=1)
=(1+o(1))\exp(-knp_n^2)
=(1+o(1))n^{-2k}e^{-kt}.
\]
Indeed \(np_n^3\to0\) and \(np_n^4\to0\). There are \((\binom n2)_k\sim n^{2k}/2^k\) ordered lists of distinct pairs, so all fixed factorial moments of \(Z_n\) converge to \(\lambda^k\). The Poisson law follows.

**Sparsity and activation of obstructions.** For distinct \(u,v,w\), the two bad-pair indicators \(I_{uv},I_{uw}\) have joint probability
\[
(1-p_n^2)^2(1-2p_n^2+p_n^3)^{n-3}=O(n^{-4}).
\]
There are \(3\binom n3\) unordered pairs of bad-pair candidates sharing a vertex. Thus their expected number is \(O(n^{-1})\); Markov's inequality shows that \(\mathcal B_n\) is a matching with probability tending to one.

For fixed distinct \(u,v\), the edges involved in having no common predecessor of \(u,v\) are disjoint from those involved in having no common successor (the no-loop convention removes both endpoint exceptions). These two events are independent and have probability \((1-p_n^2)^{n-2}\) each. Hence the expected number of bad pairs with no common predecessor is
\[
\binom n2(1-p_n^2)^{2(n-2)}=O(n^{-2}).
\]
Finally, a union bound and the binomial outdegree law show
\[
\Pr(\exists u:d^+(u)<2)
\le n\Big((1-p_n)^{n-1}+(n-1)p_n(1-p_n)^{n-2}\Big)=o(1).
\]
All three good conditions therefore hold simultaneously with probability tending to one.

**Sharp optimal distance.** Fix a frame satisfying the three good conditions. Every bad pair \(\{u,v\}\) is already a pair of successors of some \(x\), so (1) requires it to acquire a common successor. In an insertion-only repair, achieving this requires at least one added edge whose tail is \(u\) or \(v\). Because the bad pairs are endpoint-disjoint, a single added edge cannot serve the lower-bound requirement of two different bad pairs; hence \(K\ge Z\).

For each bad pair choose any \(w\in N^+(v)\setminus\{u\}\), which exists because \(d^+(v)\ge2\), and add \(u\to w\). The edge is necessarily missing, and is not a self-loop. Each resulting bad pair now has a common successor, while edge additions cannot destroy a previously existing common successor. Every pair of distinct vertices thus has intersecting out-neighborhoods. Every individual vertex has a nonempty out-neighborhood as well, so the diagonal case \(y=z\) of (1) holds. Therefore the repaired frame validates (1) and \(K\le Z\). The equality \(K=Z\) follows.

**Multiplicity.** On such a good frame, every minimum repair uses exactly one directed insertion with tail in each bad pair. Fix \(\{u,v\}\in\mathcal B\). An insertion from \(u\) must end at an old successor of \(v\) different from \(u\), providing \(d^+(v)-\mathbf1_{R(v,u)}\) choices; symmetrically insertions from \(v\) provide \(d^+(u)-\mathbf1_{R(u,v)}\) choices. These choices are disjoint, necessary, and sufficient. Because bad pairs have disjoint sets of possible insertion tails, selecting one insertion per pair gives distinct optimal edge sets and causes no interference. Multiplying proves the displayed exact formula. A Chernoff union bound shows \(\max_u|d^+(u)/(np_n)-1|\to0\) in probability because \(np_n\gg\log n\). Since \(Z_n=O_{\Pr}(1)\), the product formula then implies \(H_n/(2np_n)^{K_n}\to1\) in probability. The probability of \(K_n=k\) tends to a strictly positive Poisson mass for any fixed \(k\), proving the conditional assertion. On the good event, validity is equivalent to \(Z_n=0\); since that event's complement has vanishing probability, the validity limit follows from the Poisson law.

## Verification

The accompanying `verify.py` (standard-library Python 3) can be executed with `python verify.py`. It checks, by *direct evaluation of every valuation*, the equivalence between modal validity and (1) for all loop-free directed relations on up to four worlds. It exhaustively compares their first two factorial moments with symbolic Bernoulli formulas at \(p=1/2\), brute-force checks all insertion-repair distances on three worlds, and independently enumerates the optimal insertion sets for each of the 211 four-world frames satisfying the three good conditions, checking the multiplicity formula. It also tests 2,400 reproducibly sampled larger frames and their explicit repair certificates. These tests are finite corroboration, not the proof of the asymptotic law. The script prints `CHURCH_ROSSER_POISSON_INSERTION_CHECK_OK` upon success.

## Relationship to prior work

Takeda's 2026 investigation of modal frame definability motivates studying quantitative properties of explicit first-order modal frame conditions. The Church–Rosser correspondence itself is classical and **not new**. General random-graph common-neighbor calculations motivate the \(2\log n\) window; the Poisson obstruction approximation alone should not be treated as historical priority. This result instead proves that a *nonmonotone modal frame property* has, with high probability, an optimal **insertion-only** edit distance equal to that obstruction count, and exactly enumerates its optimal insertion repairs.

The 2015 *Abstract Model Repair* paper treats abstract CTL model repair and minimality but not this labelled directed random-frame distribution. Martin and Riasanovsky's 2020 random-graph edit-distance analysis treats undirected hereditary graph properties and does not give the insertion-only Church–Rosser minimum or its multiplicity. Knudstorp's 2025 modal-reduction work studies frame properties for a different axiom. This is a scientific scope comparison, **not** a claim that no theorem in the wider combinatorics literature could imply the current result.

## Limitations

The result covers **only edge insertion**, the indicated sparse independently sampled loop-free directed frames, and the fixed real critical-window parameter. It does not assert minimum deletions, full graph edit distance, other modalities, variable-density estimates outside the window, or exact finite-order distributions. It also does not claim first discovery of the classical modal correspondence or generic uncovered-pair Poisson laws. Relevant older random-digraph literature or more general random-graph repair theorems could yield the same quantitative statement. The motivating 2026 source's complete text was not accessible in this investigation; the bibliographic abstract and scope were examined, so specific theorem-level noncoverage by that paper is not certified. Historical priority is provisional until an independent literature audit.

## References

1. Yuto Takeda, *Frame definability in second-order arithmetic*, arXiv:2608.22822 (first public version 2026-08-24). Bibliographic record and abstract examined; full text unavailable here.
2. Konstantinos Chatzieleftheriou et al., *Abstract Model Repair*, arXiv:1506.06165 (2015). Accessible full text inspected, including framework and related-work sections.
3. Ryan Martin and Alex Riasanovsky, *On the edit distance function of the random graph*, arXiv:2007.08409 (2020). Accessible full text inspected, including definitions and main setup.
4. Jakob Knudstorp, *Knocking Down Boxes: The FMP for K+□^{m+k}p→□^m p*, arXiv:2510.00864 (2025). Accessible full text inspected, including primary modal frame definitions and main results.
