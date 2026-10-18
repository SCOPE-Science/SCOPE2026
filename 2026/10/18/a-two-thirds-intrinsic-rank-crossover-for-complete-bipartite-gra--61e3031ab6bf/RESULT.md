# A two-thirds intrinsic-rank crossover for complete-bipartite graphical zonotopes

## Finding

Let \(q\ge2\) be an integer, let \(K_{2,q}\) have distinct vertices \(a,b,v_1,\ldots,v_q\), and equip its standard graphical zonotope
\[
Z_q=\sum_{j=1}^{q}\bigl([0,e_a-e_{v_j}]+[0,e_b-e_{v_j}]\bigr)
\]
with the induced Euclidean metric on its \((q+1)\)-dimensional linear span. For every integer \(0\le k\le q+1\), its intrinsic volume in the Steiner normalization is exactly
\[
\boxed{V_k(Z_q)=J_{q,k}+D_{q,k}},
\]
where the *joined-hub* and *disconnected-hub* contributions are
\[
J_{q,k}=\binom q{k-1}(k-1)2^{k-2}\sqrt{k+1}
\quad(2\le k\le q+1),
\]
\[
D_{q,k}=\binom qk\sum_{j=0}^{k}\binom kj\sqrt{(j+1)(k-j+1)}
\quad(0\le k\le q).
\]
Set \(J_{q,k}=0\) outside its displayed range and \(D_{q,k}=0\) outside its displayed range. In particular, \(V_0(Z_q)=1\), \(V_1(Z_q)=2q\sqrt2\), and \(V_{q+1}(Z_q)=q2^{q-1}\sqrt{q+2}\).

Choose a size-\(k\) forest \(F\subseteq E(K_{2,q})\) with probability proportional to its Euclidean parallelotope volume
\[
w(F)=\sqrt{\det(B_F^{\mathsf T}B_F)}
=\prod_{C\in\operatorname{Comp}(F)}\sqrt{|C|},
\]
where \(B_F\) is its oriented edge-incidence matrix and isolated graph vertices count as singleton components. Let \(P_{q,k}\) denote the probability that the two hubs \(a,b\) belong to the same component. Then \(P_{q,k}=J_{q,k}/(J_{q,k}+D_{q,k})\).

**Sharp intrinsic-rank crossover.** For any sequence of integers \(0\le k_q\le q+1\) such that \(k_q/q^{2/3}\to t\) as \(q\to\infty\),
\[
\boxed{P_{q,k_q}\longrightarrow\frac{t^{3/2}}{2+t^{3/2}}}
\qquad(0<t<\infty).
\]
For \(t=0\), the limit is zero; for \(t=\infty\), the limit is one. Thus \(q^{2/3}\) is the sharp intrinsic-rank scale at which the determinant-weighted forest changes from separating its two hubs to connecting them. The limiting crossover value at \(t=1\) is \(1/3\).

**Geometric change of the critical exponent.** If instead the forest is chosen **uniformly** from all size-\(k\) acyclic edge sets, its hub-connection probability \(P^{\mathrm{unif}}_{q,k}\) has exact odds
\[
\frac{P^{\mathrm{unif}}_{q,k}}{1-P^{\mathrm{unif}}_{q,k}}
=\frac{k(k-1)}{4(q-k+1)}
\quad(2\le k\le q).
\]
Consequently, for \(k_q/\sqrt q\to s\in(0,\infty)\),
\[
\boxed{P^{\mathrm{unif}}_{q,k_q}\longrightarrow\frac{s^2}{4+s^2}.}
\]
The zero and one limits hold for ratios tending respectively to zero and infinity, including the endpoint ranks. Thus Euclidean Gram weighting shifts the hub-connection threshold from \(\sqrt q\) to \(q^{2/3}\). This distinction is a central part of the finding.

## Assumptions and scope

The graph is simple and unweighted; there are exactly two distinguished vertices on the small bipartition side and \(q\) labelled vertices on the other side. The segments have their actual lengths \(\sqrt2\); no edge-length normalization or lattice-normalized volume is applied. Intrinsic volumes are defined by the Euclidean Steiner formula in the affine span, with \(V_0=1\) and top intrinsic volume equal to ordinary intrinsic Euclidean volume. The forest probability is **not** the uniform spanning-forest measure: each acyclic \(k\)-edge subset receives its own Gram-volume weight. All conclusions are about the stated graph family and metric, and the limit concerns \(q\to\infty\) with the ranks as indicated.

## Proof

**1. The Gram-volume identity.** Orient each graph edge arbitrarily. A forest with \(k\) edges has an incidence matrix \(B_F\) with independent columns. For a component on \(s\) vertices, the corresponding tree incidence matrix \(B_C\) has \(s-1\) columns and satisfies \(\det(B_C^{\mathsf T}B_C)=s\). Indeed, by Cauchy–Binet, this determinant is the sum of squared maximal incidence minors; precisely \(s\) are nonzero, obtained by omitting any one vertex row, and each equals one in absolute value. The empty component determinant is one. Different connected components occupy disjoint row supports. Consequently,
\[
\sqrt{\det(B_F^{\mathsf T}B_F)}
=\prod_C\sqrt{|C|}.
\]
The general intrinsic-volume decomposition for a zonotope gives \(V_k(Z_q)\) as the sum of precisely these wedge/Gram volumes over all independent size-\(k\) sets of its generator segments [2, Corollary 1]. In a graph, such edge sets are exactly forests.

**2. Exhaustion by the two hub-connectivity types.** All non-isolated components of a forest in \(K_{2,q}\) must contain at least one of \(a,b\), because no edges join two right-side vertices. If the two hubs lie in a *single* component, that component contains exactly \(k-1\) right vertices. First choose them in \(\binom q{k-1}\) ways. A spanning tree of \(K_{2,k-1}\) must contain one unique length-two path between the hubs, with its middle right-side vertex chosen in \(k-1\) ways; each of the remaining \(k-2\) right vertices attaches to either hub, giving \(2^{k-2}\) possibilities. All other right vertices are isolated. Its unique nontrivial component has size \(k+1\), so its Gram volume is \(\sqrt{k+1}\). This gives \(J_{q,k}\) for \(2\le k\le q+1\).

If the hubs lie in *different* components, exactly \(k\) right vertices have an incident selected edge. Choose them in \(\binom qk\) ways. With \(j\) attached to \(a\) and \(k-j\) attached to \(b\), there are \(\binom kj\) assignments; their star-component sizes are \(j+1\) and \(k-j+1\). Their Gram volume is \(\sqrt{(j+1)(k-j+1)}\). All unused vertices are isolated. This gives \(D_{q,k}\) for \(0\le k\le q\). There are no other forest types. The two types partition the intrinsic-volume sum, proving the exact formula, boundary values, and the weighted connectivity probability.

**3. Uniform-forest benchmark.** Before applying Gram weights, the connected-hub and separated-hub cases counted in Step 2 contain respectively \(\binom q{k-1}(k-1)2^{k-2}\) and \(\binom qk2^k\) forests. Their ratio is exactly \(k(k-1)/(4(q-k+1))\) in the interior rank range. Taking \(k/\sqrt q\to s\in(0,\infty)\) gives the stated \(s^2/(4+s^2)\) limit. Bounded ranks and the top rank are handled by the explicit count formulas, establishing both extreme regimes without any approximation.

**4. Gram-weighted critical scaling and both outer regimes.** Let \(X_k\sim\operatorname{Binomial}(k,1/2)\). For \(2\le k\le q\), set
\[
H_k=\mathbb E\sqrt{(X_k+1)(k-X_k+1)}.
\]
Then \(D_{q,k}=\binom qk2^kH_k\), so the exact ratio is
\[
\frac{J_{q,k}}{D_{q,k}}
=\frac{k(k-1)\sqrt{k+1}}{4(q-k+1)H_k}.
\]
Since \(X_k/k\to1/2\) in probability and the random quantities \(k^{-1}\sqrt{(X_k+1)(k-X_k+1)}\) are bounded by \((k+2)/(2k)\), bounded convergence in probability yields \(H_k/k\to1/2\). Therefore, for any \(k\to\infty\) with \(2\le k\le q\),
\[
\frac{J_{q,k}}{D_{q,k}}
\sim\frac{k^{3/2}}{2(q-k+1)}.
\]
If \(k/q^{2/3}\to t\in(0,\infty)\), then \(k=o(q)\) and the ratio tends to \(t^{3/2}/2\); dividing it by one plus itself gives the stated crossover. For \(k=o(q^{2/3})\) with bounded \(k\ge2\), the exact ratio is \(O_k(q^{-1})\); for unbounded \(k\), the displayed asymptotic makes it tend to zero. Standard subsequence separation covers a sequence mixing bounded and unbounded ranks. The cases \(k=0,1\) have zero joining weight by definition. If \(k/q^{2/3}\to\infty\), the ratio diverges since \(q-k+1\le q\), with \(P_{q,q+1}=1\) at the top rank. This completes every regime.

## Verification

The accompanying pure-standard-library `verify.py` independently enumerates all acyclic edge subsets for \(2\le q\le7\), computes every component-size weight directly, partitions the totals according to hub connectivity, and compares the resulting \(q+2\) intrinsic-volume coefficients with the closed formula. It examines 10,383 forest subsets and also checks the separate unweighted forest counts against the exact binomial count formulas. For \(2\le q\le4\), 258 of those forests additionally receive an exact fraction-free integer determinant calculation from the edge-incidence Gram matrix. It also evaluates both the Gram-weighted and the uniform-forest critical probabilities at \(q=100000\) for three positive scaling parameters each. All comparisons passed. Run `python3 verify.py` in a standard Python 3 environment; expected concluding output is `VERIFY_OK`.

Finite calculations are corroboration, not the proof of the asymptotic transition; that proof is the bounded-expectation and ratio argument above.

## Relationship to prior work

Padrol, Pilaud and Poullot [1] define graphical zonotopes and classify their deformation cones; the present metric and family agree with their standard edge-segment convention up to translation. Joós and Lángi [2] proved the **general** intrinsic-volume sum of wedge norms used in Step 1. Neither that general identity nor the special calculation at \(q=2\) is claimed as novel. Dong and Ge [3] study the distinct problem of enumerating complete-bipartite spanning trees containing a prescribed forest; their results reinforce the classical bipartite-tree counting background.

The new assessed contribution is the all-rank two-hub decomposition **together with** its exact Gram-weighted connectivity law and the sharp, demonstrable shift of the threshold exponent from \(1/2\) under uniform forests to \(2/3\) under geometric weighting. The specialization follows from known universal identities, but the scale and limiting law require the separate forest-type analysis and binomial asymptotic comparison. The limit does not follow by simply substituting parameters in an existing stated limit theorem located in the checked sources.

## Limitations

The statement concerns the unweighted \(K_{2,q}\) family, not arbitrary \(K_{p,q}\) with growing small side or anisotropically weighted edges. The crossover describes a specific forest measure induced by intrinsic volumes; it does not describe uniform random spanning forests. The exponent is a sharp threshold within this family, not a universal exponent for all graphical zonotopes. The search of the literature cannot rule out an equivalent formulation under different terminology, and no independent mathematical validation has been carried out.

## References

[1] A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, first public preprint 24 November 2021, arXiv:2111.12422. https://arxiv.org/abs/2111.12422 . The associated journal version lists 52B11 as its first MSC classification.

[2] A. Joós and Z. Lángi, *Isoperimetric Problems for Zonotopes*, first public preprint 7 June 2022, arXiv:2206.03204, especially Corollary 1. https://arxiv.org/abs/2206.03204 .

[3] F. Dong and J. Ge, *Counting Spanning Trees in a Complete Bipartite Graph Which Contain a Given Spanning Forest*, first public preprint 9 March 2021, arXiv:2103.05294. https://arxiv.org/abs/2103.05294 .
