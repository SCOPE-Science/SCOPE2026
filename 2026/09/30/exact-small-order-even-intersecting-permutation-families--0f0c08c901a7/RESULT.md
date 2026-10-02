# Exact maximum even-intersecting families in \(S_5\)

Let two permutations of \([5]\) be *even-intersecting* when they agree in an even number of positions. Let \(M(5)\) be the largest size of a family in \(S_5\) whose distinct members are pairwise even-intersecting.

## Theorem

\[
M(5)=13.
\]

Moreover, on the labeled set \([5]\) there are exactly \(240\) maximum even-intersecting families, and all \(240\) lie in a single orbit under the natural left-right action
\[
(\alpha,\beta)\colon \mathcal F\longmapsto
\{\alpha\sigma\beta^{-1}:\sigma\in\mathcal F\}.
\]

## Exact finite reduction

Left multiplication preserves the number of agreements between any two permutations. Hence every family can be left-normalized to contain the identity.

After this normalization, every other member must agree with the identity in an even number of positions. There are exactly \(64\) such nonidentity permutations in \(S_5\). Form a graph on these \(64\) permutations, joining two vertices exactly when the corresponding permutations agree in an even number of positions. A normalized even-intersecting family containing the identity is then exactly the identity together with a clique in this graph.

An exact exhaustive clique computation gives:

- maximum clique size \(12\), hence \(M(5)=13\);
- exactly \(26\) maximum cliques, hence \(26\) normalized maximum families.

Taking every left translate of these \(26\) normalized families yields exactly \(240\) distinct labeled maximum families.

Finally, starting from one maximum family and applying every pair in \(S_5\times S_5\) under the left-right action yields exactly \(240\) distinct families, and this orbit equals the complete labeled list. Thus the maximum families form a single left-right orbit.

The computation uses exact permutation comparisons only; no floating-point decisions enter the classification.

## Prior-work boundary

The general even-intersection problem and its asymptotic bounds were introduced in Banerjee, Dewan and Mishra, *Even-Intersecting Families of Permutations*, arXiv:2609.21645. That work also reports computational optimality checks for an even-order spectral linear program at orders \(6\) through \(16\) and gives odd-order constructions. The exact value \(M(5)=13\), the count \(240\), and the single-orbit classification above are not stated there.

## Limitation

This result is an exact finite classification at \(n=5\). It does not settle the general odd-order or even-order problems.
