# Mixed extreme-value edge-cover times on irregular graphs and exact spider laws

## Finding

Let a graph edge be selected uniformly and independently at each discrete step, marking both endpoints as covered. **The full-vertex edge-cover time** is the first draw at which all vertices have been marked. For connected graphs with many degree-two vertices, the last uncovered vertices have a sharp competition between degree-one and degree-two populations. Denote their counts by \(L\) and \(D\), respectively; write \(R\) for the number of vertices of degree at least three, and \(m\) for the number of edges.

**Theorem A (two-class crossover).** For any sequence of finite connected simple graphs of at least three vertices with
\[
D\to\infty,\qquad \frac{L}{\sqrt D}\to c\in[0,\infty),
\qquad R=o(D^{3/2}),
\]
write \(T\) for the number of independent uniform edge draws (with replacement) required to cover all vertices. Then, at every real \(x\),
\[
\Pr\left(\frac{T}{m}-\frac12\log D\le x\right)
\longrightarrow \exp\left(-c e^{-x}-e^{-2x}\right).
\]
At the same scale the counts of yet-uncovered degree-one and degree-two vertices converge jointly to independent Poisson random variables with means \(c e^{-x}\) and \(e^{-2x}\). The probability that the final newly covered vertex has degree one tends to
\[
\vartheta(c)=\int_0^\infty c e^{-cy-y^2}\,dy
=\frac{\sqrt\pi c}{2}\,e^{c^2/4}\operatorname{erfc}(c/2),
\]
where \(\vartheta(0)=0\). In the limit, a possible simultaneous finishing draw has probability zero. For example, \(\vartheta(1)\approx0.54564136\).

**Theorem B (leaf-dominant crossover).** If instead \(L\to\infty\), \(D=o(L^2)\), and \(R=o(L^3)\), then for every real \(x\),
\[
\Pr\left(\frac{T}{m}-\log L\le x\right)\longrightarrow\exp(-e^{-x}),
\]
and the final newly covered vertex is a leaf with probability tending to one.

**Theorem C (exact finite spider distribution).** Let \(S_{k,\ell}\) be a star whose \(k\ge3\) edges are each subdivided to form a path with exactly \(\ell\ge3\) edges from the center to a leaf; thus \(m=k\ell\), \(L=k\), \(D=k(\ell-1)\), and \(R=1\). For any \(u\ge0\), put \(q=e^{-u}\), \(p=1-q\), and define
\[
F_0=F_1=1,\qquad F_j=pF_{j-1}+pqF_{j-2}\quad(j\ge2).
\]
Let \(U\) be the continuous cover time when each edge has an independent unit-rate Poisson clock. Then
\[
\boxed{\Pr(U\le u)=\bigl[pF_{\ell-1}\bigr]^k-\bigl[qp^2F_{\ell-3}\bigr]^k.}
\]
Writing this explicit polynomial in \(q\) as \(H_{k,\ell}(q)=\sum_{j=0}^{k\ell}a_jq^j\), the exact original discrete-draw distribution for **every** integer \(t\ge0\) is
\[
\boxed{\Pr(T\le t)=\sum_{j=0}^{k\ell}a_j\left(1-\frac j{k\ell}\right)^t.}
\]
At \(t=0\), each zeroth power, including \(0^0\), is interpreted as one. In particular, for \(k,\ell\to\infty\) with \(k/\ell\to\rho\in(0,\infty)\), Theorem A has \(c=\sqrt\rho\), whereas \(k/\ell\to0\) gives a pure degree-two extreme-value limit and \(k/\ell\to\infty\) gives the leaf-dominant Gumbel law.

## Assumptions and scope

All graph sequences consist of undirected finite simple connected graphs, with at least three vertices and no isolated vertices. Edges are sampled independently, uniformly and with replacement; one sampled edge covers both its endpoints. In the Poissonized process each edge has an independent Poisson clock of rate one (not one clock shared across all edges), so the combined edge-arrival rate is \(m\). All convergence is for deterministic graph sequences; the graph itself is not randomized. The number of vertices is at most \(2m\).

Theorem A's high-degree control is a sufficient hypothesis, not asserted optimal. The last-vertex statement refers to the degree of the vertex first covered at the last necessary edge arrival; when two vertices become covered in that same draw, use the event that at least one is a leaf. The proof shows asymptotically no tie involving two remaining classes.

## Proof

**1. Independent edge-clock representation.** Under independent unit-rate Poisson clocks, at time \(u\) an edge has not rung with probability \(q=e^{-u}\), independently over edges. If \(I_v(u)\) indicates that no edge incident to vertex \(v\) has rung by \(u\), then
\[
\Pr(I_v(u)=1)=q^{\deg(v)}.
\]
For every finite vertex set \(W\), exact independence of edge clocks gives
\[
\Pr\{I_v(u)=1\text{ for every }v\in W\}
=q^{\sum_{v\in W}\deg(v)-e_G(W)},
\tag{1}
\]
where \(e_G(W)\) is the number of graph edges with both endpoints in \(W\).

**2. Two independent rare populations.** Fix \(x\in\mathbb R\), set \(u=\frac12\log D+x\), and write \(q=D^{-1/2}e^{-x}\). Let \(X_1(u)\) and \(X_2(u)\) count uncovered vertices of degrees one and two. The expectations converge to \(ce^{-x}\) and \(e^{-2x}\).

We verify all joint factorial moments. For any fixed selection of \(a\) distinct degree-one vertices and \(b\) distinct degree-two vertices, the factor in (1) is simply \(q^{a+2b}\) unless two selected vertices are adjacent. In the selected induced subgraph, every nontrivial connected component is a path: a cycle made entirely of degree-two vertices would be a whole connected graph, impossible once \(D\to\infty\) with a fixed selected set; two leaves cannot be adjacent in a connected graph of at least three vertices. A selected path component with \(s\ge2\) vertices either has no leaf, in which case at most \(O(D)\) placements are possible and the contribution is bounded by \(O(Dq^{s+1})=O(D^{(1-s)/2})\), or has one leaf endpoint, in which case at most \(O(L)\) placements are possible and its contribution is bounded by \(O(Lq^s)=O(D^{(1-s)/2})\). There cannot be two leaf endpoints without disconnecting the graph. The constants depend only on \(a+b\), not on the graph. Each bound tends to zero. Multiple disjoint components factor by their disjoint incident-edge sets, while the remaining singleton selections give exactly the corresponding products of \(Lq\) and \(Dq^2\) in the limit. Thus, for every fixed \(a,b\ge0\),
\[
\mathbb E[(X_1)_a(X_2)_b]\to(ce^{-x})^a(e^{-2x})^b,
\]
which are the joint factorial moments of two independent Poisson variables. Standard factorial-moment uniqueness proves the asserted joint distribution. Vertices of degree at least three are negligible because
\[
\mathbb E\sum_{v:\deg(v)\ge3}I_v(u)\le Rq^3=o(1).
\]
Taking the probability that all these nonnegative integer counts vanish yields Theorem A's cover-time CDF for \(U\).

The same argument with separate fixed observation times \(u_1=\frac12\log D+x_1\) for leaf indicators and \(u_2=\frac12\log D+x_2\) for degree-two indicators yields independent limiting class-specific last-cover times: shared edge clocks require the later of the two observation times, but the exponent bounds for a nontrivial selected path change only by fixed multiplicative factors. Letting \(M_1,M_2\) be the two limiting class-specific centered last-cover times, their distributions are
\[
\Pr(M_1\le x)=e^{-ce^{-x}},\qquad
\Pr(M_2\le x)=e^{-e^{-2x}},
\]
with \(M_1=-\infty\) when \(c=0\). Their continuous independent laws have no ties. Integrating the density of \(M_1\) against the CDF of \(M_2\), followed by \(y=e^{-x}\), gives
\[
\Pr(M_1>M_2)=\int_{-\infty}^{\infty}
ce^{-x}\exp(-ce^{-x}-e^{-2x})\,dx
=\int_0^\infty ce^{-cy-y^2}\,dy.
\]
The probability that high-degree vertices finish last tends to zero. Any two vertices newly covered by a single edge must be adjacent. At a fixed centered time the expected number of adjacent uncovered low-degree pairs is at most \(O(Dq^3+Lq^2)=o(1)\), since a connected graph of at least three vertices has no adjacent leaves. The centered completion times are tight, so applying this estimate at the beginning of an arbitrarily wide fixed window proves that the probability of a tied last-cover event tends to zero. This proves the marked conclusion.

**3. Leaf-dominant regime.** At \(u=\log L+x\), \(q=L^{-1}e^{-x}\). Since the graph is connected with at least three vertices, distinct leaves have distinct incident edges. Their uncovered indicators are therefore exactly independent, giving \(\Pr(X_1=0)=(1-q)^L\to e^{-e^{-x}}\). Meanwhile the expected counts of uncovered degree-two and higher-degree vertices are bounded by \(Dq^2=o(1)\) and \(Rq^3=o(1)\). Consequently all remaining coverage occurs at leaves asymptotically. This proves Theorem B for the continuous clock process.

**4. De-Poissonization.** In the superposed edge-clock process the aggregate arrival rate is \(m\), each arrival label is an independent uniform edge, and the interarrival times are independent of all edge labels. We can therefore couple the original discrete cover count \(T\) and continuous cover time \(U\) by
\[
U=\frac1m\sum_{i=1}^{T}Z_i,
\]
where \(Z_i\) are independent rate-one exponential random variables independent of the edge draws. For all graphs, \(\Pr(T>t)\le |V|(1-1/m)^t\le2m e^{-t/m}\). Hence \(T=O_{\Pr}(m\log m)\). Conditional variance of \(U-T/m\) equals \(T/m^2\), which is \(O_{\Pr}(\log m/m)=o_{\Pr}(1)\), and its conditional mean is zero. Thus \(U-T/m\to0\) in probability, and both limiting CDF assertions transfer to discrete draws. The last newly covered vertices have exactly the same incident edge label at the coupled stopping times, so the mark statement also transfers.

**5. Exact balanced-spider formula.** Write the \(\ell\) edges along one arm, from center to leaf, as \(e_1,\ldots,e_\ell\). Each is independently present by time \(u\) with probability \(p\). All noncentral vertices on that arm are covered exactly when \(e_\ell\) is present and no two adjacent edges in \(e_1,\ldots,e_{\ell-1}\) are both absent. If \(F_j\) is the probability of no adjacent absent pair in a length-\(j\) independent edge-presence word, conditioning on the first edge being present, or on it being absent and the second present, gives
\[
F_j=pF_{j-1}+qpF_{j-2},\qquad F_0=F_1=1.
\]
Thus a complete noncentral arm has probability \(B=pF_{\ell-1}\), and all noncentral vertices are covered with probability \(B^k\). The center is uncovered precisely when the first edge in **every** arm is absent. Conditional on this, an arm's first noncentral vertex forces \(e_2\) to be present, the leaf forces \(e_\ell\) to be present, and the \(\ell-3\) intervening edges must have no adjacent absent pair. This event has probability \(A=qp^2F_{\ell-3}\) per arm, independently, so subtracting \(A^k\) proves the formula for \(U\).

Finally put \(H_{k,\ell}(q)=\sum_{j=0}^{m}a_jq^j\). The discrete-time completion probability \(h_t=\sum_j a_j(1-j/m)^t\) has Poisson transform
\[
\sum_{t=0}^\infty e^{-mu}\frac{(mu)^t}{t!}h_t
=\sum_j a_je^{-ju}=H_{k,\ell}(e^{-u}),
\]
which is the just-derived continuous completion law. Since \(U\) is the discrete cover event observed at independent Poisson arrival count \(N(mu)\), uniqueness of exponential generating functions gives \(h_t=\Pr(T\le t)\) for every integer \(t\ge0\). Substituting \(L=k\), \(D=k(\ell-1)\), \(R=1\) into Theorems A and B gives the three spider regimes, completing the proof.

## Verification

An accompanying standalone `checker.py` runs with Python 3 and SymPy. It verifies the exact arm recurrence by independent enumeration of binary edge-status strings, checks the spider completion polynomial against exhaustive edge-subset enumeration for small \((k,\ell)\), and separately compares the resulting exact discrete law with a state-by-state uniform edge-draw enumeration for draw counts \(0\) through \(7\). Numerical large-spider checks provide nonproof illustrations of the crossover. The checker passed 105 deterministic assertions. Infinite asymptotic statements are justified by the analytic rare-event and coupling arguments above, **not** by finite experiments.

## Relationship to prior work

Tauraso (2008) studies exactly this uniform random-edge endpoint-coverage process and gives general finite-cover enumerator transforms and mean formulas, especially for regular graphs. The exact generic transform is acknowledged; the stated finite contribution here is its compact evaluation for a subdivided star, not the invention of a cover-time representation. Falgas-Ravry, Larsson and Markström (2016) develop a broad structured-coupon-collector framework, including dependence-sensitive tools. Godbole, Grubb, Han and Kay (public preprint of 26 March 2018) study threshold progressions across covering contexts. The degree-stratified non-Gumbel extreme-value law, its leaf-vs-degree-two last-cover mark and the explicit balanced-spider evaluation are not stated in the inspected materials. General covering principles may offer alternative derivations; no uniqueness or historical priority is claimed.

## Limitations

The transition requires a graph sequence with the stated degree-class growth hypotheses, independent uniform edge draws with replacement and no isolated vertices. It does not extend automatically to random-walk edge visitation, nonuniform edge sampling, directed graphs or arbitrary degree mixtures. The high-degree growth bounds are sufficient and may not be optimal. The exact finite formula covers balanced spiders of arm length at least three; it is not asserted to be the first possible expression obtainable from general edge-cover enumerator formulas. Priority against every historical paper is not certified; independent mathematical validation has not been performed.

## References

1. R. Tauraso, "Edge Cover Time for Regular Graphs," *Journal of Integer Sequences* 11 (2008), Article 08.4.4. https://cs.uwaterloo.ca/journals/JIS/VOL11/Tauraso/tauraso18.pdf .
2. V. Falgas-Ravry, J. Larsson and K. Markström, "Speed and concentration of the covering time for structured coupon collectors," first public 18 January 2016, arXiv:1601.04455. https://arxiv.org/abs/1601.04455 .
3. A. Godbole, T. Grubb, K. Han and B. Kay, "Threshold Progressions in a Variety of Covering and Packing Contexts," first public 26 March 2018, arXiv:1803.09601. https://arxiv.org/abs/1803.09601 .
