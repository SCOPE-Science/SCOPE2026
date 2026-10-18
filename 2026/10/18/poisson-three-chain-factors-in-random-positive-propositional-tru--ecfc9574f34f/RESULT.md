# Poisson three-chain factors in random positive propositional truth-set lattices

## Finding
Let \(m\ge1\) propositional letters independently receive fair Boolean valuations at each of \(n\ge2\) labelled worlds. Let \(\mathcal L_{m,n}\subseteq\mathcal P([n])\) be the bounded distributive lattice of truth sets of formulas made from the letters, \(\wedge,\vee,\bot,\top\), with no negation; write \(K_{m,n}=|\mathcal L_{m,n}|\). Put
\[
\alpha_m=2(3/4)^m-2^{-m},\quad \beta_m=(5/8)^m,\quad N=\binom n2,\quad \lambda_{m,n}=N\alpha_m,
\qquad H_{m,n}=\log_{4/3}\left(\frac{2^n}{K_{m,n}}\right).
\]
For every \(m\ge1,n\ge2\), the total-variation distance between the real-valued law of \(H_{m,n}\) and a Poisson law on the nonnegative integers obeys
\[
 d_{\mathrm{TV}}\left(\mathcal L(H_{m,n}),\operatorname{Poisson}(\lambda_{m,n})\right)
 \le 2N\bigl((2n-3)\alpha_m^2+8(n-2)\beta_m\bigr)
       +N2^{-m}+12\binom n3\beta_m.\tag{1}
\]
Here \(\mathcal L(\cdot)\) inside the distance denotes probability law, not a truth-set lattice.

If \(m\to\infty\) and \(n/(4/3)^{m/2}\to t\in(0,\infty)\), then
\[
 H_{m,n}\xrightarrow{\mathrm{TV}}\operatorname{Poisson}(t^2),
 \qquad \frac{K_{m,n}}{2^n}\xrightarrow{\mathrm d}(3/4)^Z,
 \quad Z\sim\operatorname{Poisson}(t^2).
\]
Moreover, for each fixed nonnegative integer \(k\),
\[
 \Pr\bigl(\mathcal L_{m,n}\cong \mathbf 3^{\,k}\times
 \mathbf 2^{\,n-2k}\bigr)\longrightarrow
 e^{-t^2}\frac{t^{2k}}{k!},\tag{2}
\]
where \(\mathbf j\) is the \(j\)-element chain and \(n\ge2k\) for all sufficiently large \(m\). In particular,
\[
 \Pr(K_{m,n}=2^n)\to e^{-t^2},\qquad
 \mathbb E\left[\frac{K_{m,n}}{2^n}\right]\to e^{-t^2/4}.
\]
At this same scale, allowing Boolean negation yields every subset of worlds with probability tending to one. Thus the complete limiting *isomorphism type*, not merely the previously studied number of comparable sampled subsets, measures the random loss of positive expressive power.

## Assumptions and scope
Write \(V_w\in\{0,1\}^m\) for the valuation vector at world \(w\); all \(mn\) entries are independent Bernoulli variables of mean \(1/2\). Equip \(\{0,1\}^m\) with the coordinatewise order. In a formula, empty conjunction means \(\top\), and empty disjunction means \(\bot\). Truth sets are counted as distinct subsets of the \(n\) labelled worlds, regardless of formula syntax. The theorem concerns finite worlds and the indicated simultaneous growth of \(n\) and \(m\); no assertions about infinite Boolean algebras or biased valuations are made. For a random variable with values in \(\mathbb R\), total variation means the supremum of probability differences over Borel sets.

## Proof
**Deterministic lattice representation.** Let \(Q\subseteq\{0,1\}^m\) be the set of distinct realised vectors and let \(\pi:[n]\to Q\) send a world to its vector. Every positive formula is coordinatewise monotone, hence its truth set is the inverse image of an upset of \(Q\). Conversely, for any upset \(U\subseteq Q\), take its minimal elements and form
\[
 \varphi_U=\bigvee_{a\in\min(U)}\ \bigwedge_{j:a_j=1}p_j.
\]
On realised vectors its truth set equals \(\pi^{-1}(U)\). Thus \(\mathcal L_{m,n}\cong\operatorname{Up}(Q)\), including when \(U\) is empty. The Boolean formula language instead defines exactly the unions of the nonempty fibres of \(\pi\), using conjunctions of both positive and negative literals. It defines all \(2^n\) world subsets precisely when the sampled vectors are distinct.

**Comparability graph and exact good-event structure.** Define a graph on the labelled worlds, joining \(u,v\) whenever \(V_u\le V_v\) or \(V_v\le V_u\), including equality. Let \(Z\) count its edges. If the sampled vectors are distinct and the graph has maximum degree at most one, then the realised poset \(Q\) is a disjoint union of \(Z\) two-point chains and \(n-2Z\) isolated points. Its upset lattice is consequently
\[
 \mathcal L_{m,n}\cong\mathbf3^{\,Z}\times\mathbf2^{\,n-2Z},\qquad
 K_{m,n}=3^Z2^{n-2Z},\qquad H_{m,n}=Z.\tag{3}
\]
This is an isomorphism of bounded lattices, not merely an equality of cardinalities. Its rank-generating polynomial is
\((1+x+x^2)^Z(1+x)^{n-2Z}\).

**Rare-overlap bounds.** For a pair of independent fair \(m\)-vectors, one orientation of containment has probability \((3/4)^m\) and equality has probability \(2^{-m}\). Therefore a graph edge has probability exactly \(\alpha_m\). For three independently sampled vectors, the event that the two edges incident to a prescribed central vector both appear is a union of four oriented comparisons. The per-coordinate success probability of a same-direction pair is \(5/8\), and that of a mixed-direction pair is \(1/2\). Thus each overlapping-edge pair has probability at most \(4\beta_m\).

There are \(N\) possible graph edges; each has at most \(2n-3\) edges including itself in its dependency neighbourhood, and exactly \(2(n-2)\) other incident edges. The local-dependence Stein--Chen inequality for Bernoulli sums (indicators on disjoint pairs are independent) gives
\[
 d_{\mathrm{TV}}(\mathcal L(Z),\operatorname{Poisson}(\lambda_{m,n}))
 \le 2N\bigl((2n-3)\alpha_m^2+8(n-2)\beta_m\bigr).\tag{4}
\]
The probability that any two sampled vectors coincide is at most \(N2^{-m}\). Any vertex of graph degree at least two is the centre of one of at most \(3\binom n3\) unordered adjacent-edge pairs; the union bound above therefore controls that event by \(12\binom n3\beta_m\). Coupling \(H_{m,n}\) and \(Z\) using the same random vectors, (3) implies they agree outside the union of these bad events. Combining with (4) proves (1).

**Critical window and structural law.** Under \(n/(4/3)^{m/2}\to t\), the mean \(\lambda_{m,n}\to t^2\). All errors in (1) tend to zero because
\[
 (4/3)^{3/2}(5/8)=5/(3\sqrt3)<1,
 \quad (4/3)^{3/2}(9/16)=\sqrt3/2<1,
 \quad (4/3)2^{-1}=2/3<1.
\]
Since Poisson laws are continuous in their means in total variation, this proves the claim for \(H\). The good event has probability tending to one, so (3) and Poisson convergence give (2) and the distributional limit for \(K_{m,n}/2^n\). The latter fraction is in \([0,1]\), so bounded convergence in distribution yields its expectation limit
\(\mathbb E(3/4)^Z=\exp(t^2((3/4)-1))=e^{-t^2/4}\). The good event also implies \(K_{m,n}=2^n\) exactly when \(Z=0\), up to an event of vanishing probability. Finally, \(N2^{-m}\to0\) ensures that all vectors are distinct with high probability, and the deterministic Boolean characterization gives full Boolean expressive power.

## Verification
The accompanying standalone script `verify.py` uses only Python's standard library. It independently enumerates 5,058 finite labelled valuations, generates all positive formulas through iterative closure under union and intersection, independently enumerates all upsets of the coordinatewise valuation preorder, and compares the resulting truth-set families. It also constructs the Boolean closure, verifies the chain-product cardinality on 245 eligible examples, and checks six exact rational edge probabilities and triple-overlap inequalities. Run `python3 verify.py` in the package directory. Expected final line:

`VERIFY_OK 5058 exhaustive finite valuations; 245 matching-poset factorizations; 6 exact moment bounds`

These computations verify finite instances and the finite probability identities, not the asymptotic argument. The infinite conclusion follows from the stated local-dependence inequality and the proven exponential bounds.

## Relationship to prior work
Rényi's earlier antichain transition and Dudley Stark's 2004 *Convergence in Distribution for Subset Counts Between Random Sets* already prove, for this same random-set model, the Poisson law for comparable pairs and its quantitative approximation. **Neither that count limit nor its threshold is claimed as new here.** The added result is the random **bounded distributive lattice** of positive definable truth sets: a high-probability product decomposition, a quantitative law for its logarithmic size deficit, and the resulting exact distribution and expectation of retained expressive power. Its extra argument controls components of size greater than two; counting comparable pairs alone does not determine the order-ideal lattice on arbitrary instances.

Marcelino and Rivieccio study algebraic logics of distributive lattices with negation and their axiomatization, rather than random finite truth-set lattices. Borlido and Suarez treat bounded sublattices of powersets in Pervin and Frith semantics, with no random-generator law. Balogh and Krueger analyze a different sampling scheme (independent retention of each element of a Boolean lattice) and maximum antichains; Alon, Gilboa, and Gueron optimize containment probabilities over sampling distributions. The deterministic upset representation itself is standard finite distributive-lattice duality and is not presented as an original theorem.

## Limitations
The novelty assessment concerns the combined random truth-set lattice law, not the underlying classical Poisson theorem or order-ideal duality. A prior formulation of this particular random-lattice product distribution might exist in probabilistic lattice or random-order literature; priority is not established by unsuccessful searches. The error bound is asymptotically effective but may be numerically weak at moderate parameter sizes. Non-fair, correlated, or non-Boolean valuations are outside the claim. No independent external verification of this work has been performed.

## References
- S. Marcelino and U. Rivieccio, *Finite axiomatizability of logics of distributive lattices with negation*, arXiv:2102.05421 (first public version, 10 February 2021).
- C. Borlido and A. L. Suarez, *A pointfree theory of Pervin spaces*, arXiv:2201.06266 (first public version, January 2022).
- D. Stark, *Convergence in Distribution for Subset Counts Between Random Sets*, Electronic Journal of Combinatorics **11** (2004), R59, doi:10.37236/1812.
- J. Balogh and R. A. Krueger, *A sharp threshold for a random version of Sperner's Theorem*, arXiv:2205.11630 (first public version, May 2022).
- N. Alon, S. Gilboa, and S. Gueron, *A probabilistic variant of Sperner's theorem and of maximal r-cover free families*, arXiv:1803.07591 (first public version, March 2018).
