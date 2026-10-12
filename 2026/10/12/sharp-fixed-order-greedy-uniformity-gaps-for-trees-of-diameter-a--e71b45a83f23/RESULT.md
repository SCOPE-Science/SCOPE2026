# Sharp fixed-order greedy-uniformity gaps for trees of diameter at most three

## Finding
Let \(b(T)\) be the total-variation distance from the random-permutation greedy maximal-independent-set output law to the uniform distribution on all maximal independent sets of a nonempty tree \(T\). For each integer \(n\ge3\), among connected \(n\)-vertex trees of diameter at most three, the sharp minimum is
\[
\beta_n=\begin{cases}
\frac16,&n=3,\\
\frac1{12},&n=4,\\
\frac1{15},&n=5,\\
\frac19,&n=6,\\
\frac13-\frac{n-1}{n(n-2)},&n\ge7.
\end{cases}
\]
The unique minimizers, up to graph isomorphism, are respectively \(P_3\), \(D_{1,1}\), \(D_{1,2}\), \(D_{2,2}\), and \(D_{1,n-3}\). In particular, \(\inf_{\operatorname{diam}(T)\le3,\ |V(T)|\ge3} b(T)=1/15\), attained uniquely by the five-vertex fork \(D_{1,2}\).

## Assumptions and scope
All graphs are finite, simple, and undirected. Greedy scans a uniformly random permutation of the vertices and accepts each vertex exactly when no accepted neighbor exists. Every output is a maximal independent set. If \(\mathcal M(T)\) is the set of such sets, write \(p_T(I)\) for output probability and
\[
b(T)=\frac12\sum_{I\in\mathcal M(T)}\left|p_T(I)-\frac1{|\mathcal M(T)|}\right|.
\]
The diameter is graph distance diameter; the scope includes stars (diameter two) and double stars (diameter three), and excludes the one- and two-vertex trivial trees. Define \(D_{a,b}\), for integers \(a,b\ge1\), to have adjacent centers \(u,v\), with leaf sets \(A,B\) of sizes \(a,b\) attached respectively to \(u,v\). Interchanging \(a,b\) gives an isomorphic tree. Set \(n=a+b+2\).

## Proof
**Tree classification.** A connected finite tree of diameter two is a star, and one of diameter three is a double star. There are no further types under the hypotheses.

**Exact double-star law.** Precisely three maximal independent sets occur:
\[
I_u=\{u\}\cup B,\qquad I_v=\{v\}\cup A,\qquad I_0=A\cup B.
\]
Indeed, if either center is selected, every leaf opposite it must be selected; if neither center is selected, all leaves must be selected. Assign independent uniform arrival priorities in \([0,1]\) to each vertex. For \(I_u\) to occur, \(u\) must arrive before every member of \(A\), but the exceptional forbidden event is that \(v\) arrives earlier than \(u\) and every member of \(B\), so that \(v\) is accepted and blocks \(u\). Integrating first over the priority \(t\) of \(u\), then that of \(v\), gives
\[
\begin{aligned}
p_T(I_u)
&=\frac1{a+1}-\int_0^1(1-t)^a\int_0^t(1-s)^b\,ds\,dt\\
&=\frac1{a+1}-\frac1{b+1}\left(\frac1{a+1}-\frac1{a+b+2}\right)\\
&=\frac{n-1}{n(a+1)}.
\end{aligned}
\]
Interchanging centers gives \(p_T(I_v)=(n-1)/(n(b+1))\) and \(p_T(I_0)=1-p_T(I_u)-p_T(I_v)\). For a distribution on three states, total variation from the uniform law is its largest absolute coordinate deviation from \(1/3\), since the deviations sum to zero.

**Optimize double stars at fixed order.** Assume \(1\le a\le b\), so \(a+b=n-2\). If \(a=1\), then \(b=n-3\). For \(n\ge5\) the exact probabilities are
\[
\frac{n-1}{2n}>\frac13,\qquad
\frac{n-1}{n(n-2)}<\frac13,\qquad
\frac{n-3}{2(n-2)}\ge\frac13,
\]
respectively. Hence
\[
\operatorname{TV}(D_{1,n-3})
=\frac13-\frac{n-1}{n(n-2)}\quad(n\ge5).
\]
If \(a\ge2\), then both center-containing outcomes have probability at most \((n-1)/(3n)<1/3\). Consequently
\[
\operatorname{TV}(D_{a,b})
=\frac23-\frac{n-1}{n}\left(\frac1{a+1}+\frac1{b+1}\right).
\]
For fixed \(a+b=n-2\) and \(2\le a\le b\), the reciprocal sum is maximized uniquely at \(a=2\), since its first summand declines faster than the second rises as \(a\) approaches the middle. Thus among this group \(D_{2,n-4}\) is optimal. Compare its bias against the \(a=1\) competitor, for \(n\ge6\):
\[
\operatorname{TV}(D_{2,n-4})-\operatorname{TV}(D_{1,n-3})
=\frac{n^2-8n+9}{3n(n-3)(n-2)}.
\]
This is negative at \(n=6\) and strictly positive for every integer \(n\ge7\). Thus \(D_{2,2}\) wins uniquely at \(n=6\), whereas \(D_{1,n-3}\) wins uniquely for all \(n\ge7\). The exceptional small orders have \(D_{1,1}\) at \(n=4\) with bias \(1/12\), and \(D_{1,2}\) at \(n=5\) with bias \(1/15\).

**Compare stars.** A star with \(m=n-1\ge2\) leaves has exactly two maximal independent sets, the center alone and the whole leaf set. Their greedy probabilities are \(1/n\) and \((n-1)/n\), so the bias is \((n-2)/(2n)\). At \(n=3\) this is \(1/6\). At \(n=4\), the star bias is \(1/4>1/12\). For every \(n\ge5\),
\[
\frac{n-2}{2n}-\left(\frac13-\frac{n-1}{n(n-2)}\right)
=\frac{n^2-2n+6}{6n(n-2)}>0.
\]
Hence no star beats the selected double-star at any \(n\ge4\), establishing the displayed fixed-order minimum and uniqueness.

**Global sharpness.** For \(n\ge7\), the expression \(1/3-(n-1)/(n(n-2))\) increases with \(n\) and already equals \(17/105>1/15\) at \(n=7\). Comparing the explicit \(n=3,4,5,6\) cases proves the global \(1/15\) assertion.

## Verification
Run `python3 verify.py` from the same directory; it uses only the Python standard library. The companion `verification_output.txt` records `ALL CHECKS PASSED`. The verifier exhaustively scans every permutation on eleven selected double-star parameter profiles (up to nine vertices), independently checks the three predicted output probabilities, verifies the analytic bias inequality for \(20,100\) pairs with \(1\le a\le b\le200\), and checks fixed-order minima and unique minimizers for \(198\) orders (\(3\) through \(200\)). These finite checks corroborate, but do not substitute for, the infinite proof above.

## Relationship to prior work
Fairfax-Ball (arXiv:2610.02276v1, October 1, 2026) proves exact greedy-uniformity occurs only for \(K_1\) and \(K_2\), and gives a near-uniform family of diameter-four mixed spiders. That paper also calculates the output law of its mixed-spider family; its one-length-two-arm special case already covers the subfamily \(D_{1,b}\). The present contribution is **not** those published formulas, the nonuniformity theorem, or the near-uniform spider construction. It supplies the entire double-star greedy law and, crucially, an all-order optimization and unique extremal classification across every tree of diameter at most three, including double stars with both leaf counts at least two. In combination with the published diameter-four family, the bound shows that diameter four is the least diameter permitting a sequence of nontrivial trees whose greedy bias tends to zero. Krivelevich–Mészáros–Michaeli–Shikhelman (2024) study the random greedy process principally through expected size and local limits, not this finite-state uniformity extremum.

## Limitations
The theorem is restricted to connected trees of diameter at most three and uses total variation on maximal **sets**, not a law conditioned on set cardinality. It does not claim the minimum over all trees at each order, nor a new diameter-four construction. The literature comparison cannot rule out unindexed equivalent results. The computational tests cover finite parameter ranges; only the analytic proof establishes the universal ranges. The work has not received an independent external audit.

## References
1. John Fairfax-Ball, *Greedy Uniformity on Trees: Exact Obstruction and Near-Uniform Spiders*, arXiv:2610.02276v1 (first public October 1, 2026), https://arxiv.org/html/2610.02276v1.
2. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms 64 (2024), 986–1015, https://doi.org/10.1002/rsa.21200.
3. I. Kryven, R. Versendaal, M. de Vries, *Unified framework for asymptotically uniform iterative construction of generalised random graphs with local constraints*, arXiv:2608.07239 (2026), https://arxiv.org/abs/2608.07239.
