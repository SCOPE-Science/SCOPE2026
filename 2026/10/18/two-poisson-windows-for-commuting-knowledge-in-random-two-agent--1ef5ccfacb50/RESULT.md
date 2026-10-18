# Two Poisson windows for commuting knowledge in random two-agent S5 frames

## Finding

For integers \(k\ge2\) and \(n\ge0\), independently give each of \(n\) labelled worlds two uniform labels in \([k]\), one for each of two agents. Worlds are indistinguishable to an agent precisely when their labels for that agent agree. Let \(Q_{k,n}\) be the probability that the two knowledge operators commute on **all** subsets of worlds (equivalently, that their compositions agree as modal operators).

There are two distinct transitions as \(k\to\infty\). For \(t>0\),

\[
 n/k^{2/3}\longrightarrow t \quad\Longrightarrow\quad Q_{k,n}\longrightarrow e^{-t^3},
\]

whereas for every real \(s\),

\[
 n=k^2(2\log k+s+o(1)) \quad\Longrightarrow\quad Q_{k,n}\longrightarrow \exp(-e^{-s}).
\]

In between, commutation typically fails: if \(k^{2/3}=o(n)\) and \(n\le k^2(2\log k-\omega(1))\), then \(Q_{k,n}\to0\). At the two extremes \(n=o(k^{2/3})\) and \(n\ge k^2(2\log k+\omega(1))\), respectively, \(Q_{k,n}\to1\). Here each \(\omega(1)\) denotes any positive diverging sequence, and the stated inequalities apply whenever their right-hand sides are nonnegative.

For reproducibility, there is also an exact finite formula (a weighted specialization of known finite commuting-equivalence enumeration), not asserted as original: Define integers \(A_{l,r,e}\) by \(A_{0,r,e}=\mathbf1_{e=0}\), \(A_{l,r,e}=0\) for \(e<0\), and for \(l\ge1\),

\[
A_{l,r,e}=A_{l-1,r,e}+
 \sum_{a=1}^l\sum_{b=1}^r {l-1\choose a-1}{r\choose b}A_{l-a,r-b,e-ab}.
\]

Let \(\left\{\begin{smallmatrix}n\\e\end{smallmatrix}\right\}\) denote a Stirling number of the second kind, with the usual convention for zero. Then

\[
\boxed{Q_{k,n}=k^{-2n}\sum_{e=0}^{\min(k^2,n)}A_{k,k,e}\,e!\left\{\begin{smallmatrix}n\\e\end{smallmatrix}\right\}.}
\]

The early limiting curve is decreasing and the late one increasing: knowledge commutativity is **reentrant** in this natural sampling model.

## Assumptions and scope

Each world's pair of labels is independently uniform on \([k]\times[k]\), with replacement. Labels need not be used. The resulting equivalence relations live on the \(n\) sampled worlds, not on the label set; repeated label pairs correspond to multiple worlds occupying the same cell. \(K_i(X)=\{w:[w]_{E_i}\subseteq X\}\) is the ordinary \(\mathsf{S5}\) knowledge operator. Commutation means \(K_1K_2(X)=K_2K_1(X)\) for **every** subset \(X\) of worlds, equivalently for every possible propositional valuation. Logarithms are natural.

## Proof

**1. Incidence characterization.** Form the simple bipartite graph \(G\) with one vertex per label on each side and an edge for every occupied label pair. Ignore isolated label vertices when interpreting the two equivalences. A standard permutability criterion for equivalence relations gives \(E_1\circ E_2=E_2\circ E_1\) if and only if every nontrivial connected component of \(G\) is complete bipartite. For completeness: a component formed by a complete rectangle lets every pair of worlds connect in either order; worlds in different components connect in neither order. Conversely, if a connected bipartite component is not complete, a shortest path from a left vertex to a nonadjacent right vertex begins with an induced three-edge path \((a,b),(a',b),(a',b')\) with \((a,b')\) absent. Worlds at the first and third edges are related by an \(E_2\)-then-\(E_1\) path, but not by the reverse two-step path. For box operators, equality on every subset is equivalent to equality of underlying composed relations (recover each successor set by testing complements of singletons). Hence commutation is equivalent to \(G\) being induced-\(P_4\)-free, or equivalently a disjoint union of complete bipartite components and isolated vertices.

**2. Exact enumeration.** Let \(A_{l,r,e}\) count simple bipartite graphs on specified labelled left and right vertex sets of sizes \(l,r\) having \(e\) edges and all nontrivial components complete bipartite. For a distinguished left vertex, either it is isolated, or it belongs to a complete component with \(a\) left vertices and \(b\) right vertices. Choosing the remaining vertices in that component gives the stated recurrence. For a fixed graph with \(e\) occupied cells, the number of onto maps from \(n\) distinguishable worlds to those \(e\) cells is \(e!\left\{\begin{smallmatrix}n\\e\end{smallmatrix}\right\}\). Dividing the total by the \(k^{2n}\) equally likely input labelings proves the formula. Equivalently, the edge-count generating polynomial is obtained by taking \((k!)^2[x^ky^k]\) in \(\exp(x+y+\sum_{a,b\ge1}x^ay^bz^{ab}/(a!b!))\).

**3. First Poisson window.** Let \(X\) be the number of three-element subsets of sample indices whose three pairs occupy three different corners of a \(2\times2\) rectangle. Direct counting gives

\[
\mathbb E X={n\choose3}\frac{6(k-1)^2}{k^4}\sim\frac{n^3}{k^2}.
\]

For \(n\sim tk^{2/3}\), factorial moments of \(X\) tend to those of \(\operatorname{Poisson}(t^3)\). Here is the overlap check: disjoint triples of sample indices contribute \((\mathbb EX)^r(1+o(1))\) to the \(r\)th factorial moment. A single three-edge bipartite path has four vertices, while every proper nonempty subgraph with \(h\) edges has strictly more than \(4h/3\) vertices. Identifying observations between distinct paths therefore makes the exponent \(v-4m/3\) strictly negative, where \(m\) is the number of distinct sampled edges and \(v\) the number of distinct label vertices in the overlapping union; summing the finitely many overlap types for each fixed \(r\) gives \(o(1)\). Thus \(X\Rightarrow\operatorname{Poisson}(t^3)\). The expected number of repeated occupied cells is \(O(n^2/k^2)=o(1)\); the expected number of fully occupied \(2\times2\) rectangles is \(O(n^4/k^4)=o(1)\). Consequently \(G\) has an induced \(P_4\) exactly when \(X>0\), with probability \(1-o(1)\). This proves the first limit. If \(n=o(k^{2/3})\), the first-moment estimate alone gives commutation with probability tending to one.

**4. Noncommuting middle range.** Uniformly whenever \(n\gg k^{2/3}\), direct classification of pairs of sample-index triples sharing one or two observations gives

\[
\operatorname{Var}X\le \mathbb EX+O(n^5/k^4+n^4/k^3),\qquad
\operatorname{Var}X/(\mathbb EX)^2=o(1).
\]

Let \(Y\) count these triples for which the fourth corner is occupied by an additional sample. Conditional on a triple's three corners, the chance of such occupancy is at most \(n/k^2\); hence \(\mathbb EY\le(n/k^2)\mathbb EX\). For \(k^{2/3}\ll n\ll k^2\), concentration of \(X\) and Markov's inequality for \(Y\) imply an induced \(P_4\) with high probability, so \(Q_{k,n}\to0\).

When \(n\gg k\log k\), the occupied bipartite graph is connected with high probability. Indeed, a separating cut with \(s\le k\) vertices on its smaller side has at least \(ks/2\) crossing cells; summing \({2k\choose s}e^{-ns/(2k)}\) over \(1\le s\le k\) gives \(o(1)\). In a connected bipartite graph, commutation requires every one of the \(k^2\) cells to be occupied. Let \(M\) be the number of empty cells. Its mean is \(k^2(1-k^{-2})^n\) and its variance is at most its mean (empty-cell indicators have nonpositive pairwise covariance). If \(n\le k^2(2\log k-\omega(1))\) and \(n\gg k\log k\), then \(\mathbb EM\to\infty\), and \(M>0\) with high probability. Combining the overlapping ranges proves the full middle regime.

**5. Final Poisson window.** For fixed \(r\ge1\), the exact empty-cell factorial moment is

\[
\mathbb E(M)_r=(k^2)_r(1-r/k^2)^n\longrightarrow e^{-rs}
\]

when \(n=k^2(2\log k+s+o(1))\). Therefore \(M\Rightarrow\operatorname{Poisson}(e^{-s})\). The graph is connected with high probability, so commutation is equivalent to \(M=0\) up to a vanishing error, proving \(\exp(-e^{-s})\). If \(n\ge k^2(2\log k+\omega(1))\), a union bound gives \(M=0\) with high probability, hence commutation.

## Verification

The standalone program `verifier.py` exhaustively checks every assignment of two agent labels in twelve ranges: \(k=2\) and \(0\le n\le6\), and \(k=3\) and \(0\le n\le4\). Across these ranges it tests 12,842 assignments, comparing the full Boolean-powerset action of the two composed knowledge operators against the induced-\(P_4\) criterion. Independently, it verifies the exact component recurrence and onto-assignment formula against full modal enumeration in all twelve parameter cases. Six additional finite calculations verify the exact probability for three sampled corners of a rectangle. Run `python3 verifier.py` from the package directory; success prints `VERIFY_OK` and `EXACT_COUNT_OK`. These finite checks do not establish the infinite limits, which follow from the proof above.

## Relationship to prior work

Burigana, Felli, Montali and Troquard (2023) introduce and use commutativity of epistemic \(\mathsf{S5}\) modalities for finite-depth reasoning and planning decidability; their frame axiom is the relevant logical starting point. Standard permutability of equivalence relations and the associated rectangular-cell characterization are not claimed as new. An earlier class-refined exponential generating function for commuting pairs of equivalence relations enumerates these same finite structures. Weighting their classes by injective choices of the available left/right label names recovers the exact finite probability above; this specialization is **not** claimed as new. The present claim concerns the two asymptotic Poisson windows and the intervening noncommutation regime in the independently labelled-world ensemble. Classical forbidden-subgraph Poisson counting and coupon-collector limits supply the probabilistic foundations. Do, Erde, Kang and Missethan study near-critical components of random bipartite graphs, rather than knowledge commutation or the two extremes of this sampling model. General results concerning random cographs could encompass portions of the asymptotics; see the limitations.

## Limitations

The two-agent input uses independently sampled, equally likely **label pairs**, not independently uniform set partitions; the laws need not hold for that different model. No estimate of the convergence rate is asserted. The exact recurrence is combinatorial and may be computationally expensive for large \(k\). Known graph-structure and probability techniques are explicitly credited. A general random-induced-subgraph theorem or a suitable asymptotic extraction from the known class-refined commuting-equivalence generating function might imply pieces of the two-window theorem; the available comparisons did not establish an equivalent combined result. No independent external scientific audit has been performed.

## References

1. Alessandro Burigana, Paolo Felli, Marco Montali and Nicolas Troquard, *A Semantic Approach to Decidability in Epistemic Planning (Extended Version)*, arXiv:2307.15485, first version 2023-07-28, especially Sections 3–4. https://arxiv.org/abs/2307.15485
2. Tuan Anh Do, Joshua Erde, Mihyun Kang and Michael Missethan, *Component behaviour and excess of random bipartite graphs near the critical point*, arXiv:2105.14883; *Electronic Journal of Combinatorics* 30 (2023), P3.7. https://arxiv.org/abs/2105.14883
3. Edward J. Green, *Semi-decidable equivalence relations obtained by composition and lattice join of decidable equivalence relations*, arXiv:1711.03056 (2017); background on relation composition, not a source for the finite enumeration. https://arxiv.org/abs/1711.03056
4. Standard facts used: equivalence-relation permutability, induced-\(P_4\) characterization of cographs, method of factorial moments for Poisson counts, and coupon-collector empty-box asymptotics. These foundations are not claimed as new.
