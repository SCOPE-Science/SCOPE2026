# Countable products force maximal horoball non-determinism
## Finding
Let \(G\) be an infinite countable group equipped with a proper right-invariant metric \(\rho\). For each \(i\ge 1\), let \((X_i,T_i,G)\) be a nonempty compact metrizable dynamical system, and give
\[
X=\prod_{i\ge1}X_i
\]
the coordinatewise action \(T^g((x_i)_i)=(T_i^g x_i)_i\). Let \(d\) be any metric inducing the product topology on \(X\).

If infinitely many factors \(X_i\) have at least two points, then for every \(\varepsilon>0\) there are distinct \(x,y\in X\) satisfying
\[
d(T^g x,T^g y)<\varepsilon\qquad\text{for every }g\in G.
\]
Hence every horofunction is \(\varepsilon\)-non-deterministic for every \(\varepsilon>0\), so
\[
\operatorname{ND}_{\varepsilon}(X)=\operatorname{ND}(X)=\partial(G,\rho).
\]
Thus countably many nontrivial coordinates force maximal horoball non-determinism, independently of the dynamics in the factors.

As an exact expansiveness boundary, the coordinatewise countable product action is expansive if and only if only finitely many factors are non-singletons and each non-singleton factor action is expansive.

## Assumptions and scope
The phase spaces are nonempty compact metrizable spaces. The acting group is infinite and countable and carries a proper right-invariant metric only so that the horofunction boundary \(\partial(G,\rho)\) and the sets \(\operatorname{ND}_{\varepsilon}(X)\) are defined as in Bitar--Donoso--Petite. The global orbit-closeness statement itself uses only the coordinatewise form of the action and compact product topology; it does not use algebraic properties of \(G\), invertibility, minimality, entropy, or any geometric property of horoballs.

The metric \(d\) is arbitrary among metrics compatible with the product topology. Thus the conclusion is not an artifact of a particular weighted product metric.

## Proof
Choose compatible metrics \(d_i\) on \(X_i\), each bounded by \(1\), and define the standard product metric
\[
\delta(x,y)=\sum_{i=1}^\infty 2^{-i}d_i(x_i,y_i).
\]
This metric induces the product topology. Since \(X\) is compact and \(d\) and \(\delta\) induce the same topology, the identity map from \((X,\delta)\) to \((X,d)\) is uniformly continuous.

Fix \(\varepsilon>0\). Choose \(\eta>0\) such that
\[
\delta(u,v)<\eta\quad\Longrightarrow\quad d(u,v)<\varepsilon.
\]
Choose \(N\) with \(2^{-N}<\eta\). Whenever two points agree in their first \(N\) coordinates,
\[
\delta(u,v)\le \sum_{i>N}2^{-i}=2^{-N}<\eta,
\]
so \(d(u,v)<\varepsilon\).

Because infinitely many factors are non-singletons, choose \(j>N\) and distinct points \(a,b\in X_j\). Choose \(x,y\in X\) equal in every coordinate except \(j\), with \(x_j=a\) and \(y_j=b\). Then \(x\ne y\). For every \(g\in G\), coordinatewise action preserves equality of the first \(N\) coordinates, so
\[
d(T^g x,T^g y)<\varepsilon.
\]
This proves the global orbit-closeness assertion.

Now let \(h\in\partial(G,\rho)\). Bitar--Donoso--Petite call \(h\) \(\varepsilon\)-non-deterministic when there are distinct points whose images remain \(\varepsilon\)-close for every group element in the horoball \(\{h<0\}\). The pair just constructed is \(\varepsilon\)-close for every element of \(G\), hence in particular on \(\{h<0\}\). Since \(h\) was arbitrary,
\[
\operatorname{ND}_{\varepsilon}(X)=\partial(G,\rho).
\]
Intersecting over \(\varepsilon>0\) gives \(\operatorname{ND}(X)=\partial(G,\rho)\).

For the expansiveness classification, the preceding construction shows that infinitely many non-singleton factors rule out any expansivity constant. If only finitely many factors are non-singletons, the system is conjugate to a finite product. A finite product of expansive actions is expansive, and if one of its non-singleton factors is not expansive then pairs differing only in that coordinate show that the product is not expansive. Uniform equivalence of compatible metrics on compact spaces makes this conclusion independent of the chosen compatible product metric.

## Verification
The proof was checked at each quantifier. The integer \(N\) is chosen after \(\varepsilon\), while the nontrivial coordinate \(j>N\) exists because there are infinitely many non-singleton factors. The same pair \(x,y\) works simultaneously for every \(g\in G\), which is stronger than the horoball condition and avoids any issue about the geometry of a particular horoball.

No finite experiment, enumeration, asymptotic approximation, or unproved computational certificate is used. The only topological input is uniform equivalence of compatible metrics on the compact countable product.

## Relationship to prior work
Bitar, Donoso, and Petite introduced the notation \(\operatorname{ND}_{\varepsilon}(X)\) and \(\operatorname{ND}(X)\) for non-deterministic horofunctions and study existence, closedness, intersections, and geometric restrictions. Their September 22, 2026 preprint has primary MSC 37B05. Its inspected text does not state a countable-product theorem; in particular, searches of the full text for “product”, “Cartesian”, and “countable product” did not locate a result implying the theorem above.

The earlier geometric framework of Donoso, Maass, and Petite remarks that asymptotic pairs in a product dynamical system have a product structure. That observation does not imply the countable-tail phenomenon proved here: the present result produces, at every scale, a pair that stays close under the whole group and therefore makes every horofunction non-deterministic. The mechanism depends essentially on having arbitrarily remote nontrivial coordinates.

There is also a concrete comparison with Mangang's 2014 paper *Product Dynamical Systems*. Its Theorem 2.16 states, for the standard countable-product metric, that a countable product dynamical system is expansive if and only if every factor is expansive. The tail argument above shows that the countable-product direction cannot hold when infinitely many factors are non-singletons. The proof here therefore supplies the missing finite-support condition in the compact metrizable setting. This comparison is not used in the proof of the horofunction statement.

## Limitations
The theorem concerns coordinatewise countable products. It does not address inverse limits with non-coordinate bonding, skew products with coupling between coordinates, or uncountable products that are not metrizable. The maximal non-determinism conclusion is specific to infinitely many non-singleton coordinates; finite products can retain nontrivial directional information.

An older equivalent formulation may exist under classical expansiveness terminology, because the tail argument is elementary. The checked literature did not locate a prior statement of the stronger conclusion \(\operatorname{ND}_{\varepsilon}(X)=\partial(G,\rho)\) for the 2026 horofunction invariant. This residual literature risk is recorded rather than treated as a proof of novelty.

## References
1. N. Bitar, S. Donoso, and S. Petite, *Non-determinism in group actions and topological minimal self-joinings*, arXiv:2609.26479v1, first submitted 2026-09-22. Primary MSC 37B05.
2. S. Donoso, A. Maass, and S. Petite, *A geometric framework for asymptoticity and expansivity in topological dynamics*, arXiv:2210.00115; Transactions of the American Mathematical Society 377 (2024), DOI 10.1090/tran/9269.
3. K. B. Mangang, *Product Dynamical Systems*, Far East Journal of Dynamical Systems 24 (2014), 1--13. Theorem 2.16 is the countable-product expansiveness statement compared above.
