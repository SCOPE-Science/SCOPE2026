# Higher-arity Henson type enumeration and exact-counting hardness

## Finding
Let \(H_3\) be the countable homogeneous universal triangle-free graph. Let \(A\subset H_3\) be a finite induced subgraph, identified with a labelled finite triangle-free graph \(G\). For each fixed integer \(r\ge 2\), let \(T_r(G)\) count complete types over \(A\) of ordered \(r\)-tuples \((x_1,\ldots,x_r)\) satisfying \(x_i\notin A\) and \(x_i\ne x_j\) for \(i\ne j\). Equivalently, it counts pointwise-\(A\)-stabilizer orbits on these tuples.

For a finite graph \(J\), let \(i(J)\) count its independent vertex sets, including the empty set. Let \(\mathcal T_r\) be the finite collection of **labelled** triangle-free graphs on \([r]\), and let \(\square\) denote the Cartesian graph product. Then
\[
\boxed{T_r(G)=\sum_{F\in\mathcal T_r} i(G\square F).}
\]
Moreover, for every fixed \(r\ge2\), computing \(T_r(G)\) from a finite triangle-free input graph is **\(\#\mathrm P\)-complete under polynomial-time metric reductions, even when the input graph is bipartite**. The hardness reduction uses one oracle query and integer postprocessing.

For the independent parameter graph \(G=E_m\), where \(m\ge0\), the same identity specializes to
\[
T_r(E_m)=\sum_{F\in\mathcal T_r}i(F)^m.
\]
In particular, \(T_2(E_m)=4^m+3^m\), \(T_3(E_m)=8^m+3\cdot6^m+3\cdot5^m\). For each fixed \(r\ge3\), the first two exponential terms are exactly
\[
T_r(E_m)=2^{rm}+\binom r2(3\cdot2^{r-2})^m+O_r((5\cdot2^{r-3})^m),\quad m\to\infty.
\]

## Assumptions and scope
Graphs are finite simple undirected graphs, with the one countable homogeneous graph \(H_3\) used only to interpret the finite type invariant. Ordered tuple coordinates are distinct and lie outside the named finite parameter set. This is not a count of all types allowing repetitions or equality with a named parameter. The arity \(r\) is fixed in the complexity assertion; an input graph with a triangle is rejected (or assigned value zero) in its total computational extension. The result concerns exact counts, not approximation hardness. Exponents and binomial coefficients in displayed formulas have their usual integer meanings.

## Proof
**1. Types as finite extensions.** The age of \(H_3\) is precisely the finite triangle-free graphs, and every isomorphism between finite induced subgraphs extends to an automorphism. Consequently each complete type of an ordered injective tuple outside \(A\) is represented uniquely by the labelled edge pattern on the tuple and its edges to \(A\), provided that the resulting finite extension is triangle-free. The representation is unique up to an automorphism fixing \(A\) pointwise. The extension exists: the age and the extension property realize the relevant finite graph over the specified copy of \(A\).

**2. Cartesian product identity.** Fix the induced graph \(F\) on the \(r\) new ordered vertices. Necessarily \(F\in\mathcal T_r\). For each \(j\in[r]\), write \(S_j\subseteq V(G)\) for the parameter vertices adjacent to the \(j\)-th new vertex. A triangle in the combined extension can occur in exactly four ways: wholly inside \(G\), wholly inside \(F\), from one new vertex and an edge of \(G\), or from one parameter vertex and an edge of \(F\). The first two are ruled out by assumption. The third is ruled out precisely when each \(S_j\) is independent in \(G\). The fourth is ruled out precisely when \(S_j\cap S_\ell=\varnothing\) for each edge \(\{j,\ell\}\in E(F)\). These conditions say exactly that
\[
U=\{(v,j):v\in S_j\}\subseteq V(G\square F)
\]
is an independent set. This is a bijection, including the empty choice. Hence for each fixed \(F\) the number of permitted types is \(i(G\square F)\). Summing over distinct labelled \(F\) proves the boxed identity.

**3. Membership in \(\#\mathrm P\).** For fixed \(r\), nondeterministically guess all \(\binom r2\) tuple-edge bits and all \(r|V(G)|\) tuple-to-parameter edge bits. Reject unless the combined graph is triangle-free and the input graph is triangle-free. Each accepting bit string represents exactly one admissible ordered injective type, so the number of accepting paths is \(T_r(G)\). All checks are polynomial time.

**4. One-query hardness, with bipartite inputs.** Let \(B\) be an arbitrary bipartite graph on \(b\) vertices. Exact computation of \(i(B)\) is \(\#\mathrm P\)-complete. Fix \(r\ge2\), put \(c=\binom r2\), choose
\[
m=3(rb+c+2),\qquad G=B\sqcup E_m.
\]
The graph \(G\) is again bipartite and has polynomial size. Cartesian products distribute over disjoint unions, so
\[
T_r(G)=\sum_{F\in\mathcal T_r}i(B\square F)i(F)^m.
\]
For the edgeless labelled graph \(F=E_r\), \(i(F)=2^r\) and \(i(B\square F)=i(B)^r\). For every other \(F\), selecting one of its edges shows \(i(F)\le3\cdot2^{r-2}\): at most three of four choices for that edge's endpoints are allowed. There are at most \(2^c\) labelled \(F\), and \(i(B\square F)\le2^{rb}\). Therefore
\[
0\le\frac{T_r(G)}{2^{rm}}-i(B)^r
\le2^{rb+c}(3/4)^m
=2^{rb+c}(27/64)^{rb+c+2}<\tfrac14.
\]
(The last inequality follows from \(27/64<1/2\).) Thus an exact single oracle value \(T_r(G)\) recovers
\[
\boxed{i(B)^r=\left\lfloor\frac{T_r(G)}{2^{rm}}\right\rfloor.}
\]
Its unique nonnegative integer \(r\)-th root gives \(i(B)\); exact integer root extraction is polynomial time in the output bit length. Since the output has at most \(r(b+m)+c+1\) bits, this is a polynomial-time metric reduction from exact bipartite independent-set counting. Together with step 3, this proves the claimed completeness, including the bipartite promise.

**5. Independent-parameter spectrum.** For \(G=E_m\), \(E_m\square F\) is a disjoint union of \(m\) copies of \(F\), proving \(T_r(E_m)=\sum_Fi(F)^m\). Among labelled graphs on \([r]\), the unique graph with \(i(F)=2^r\) is edgeless. Exactly \(\binom r2\) graphs have a single edge, each with \(i(F)=3\cdot2^{r-2}\). If \(F\) has at least two edges, consider any two: two adjacent edges forbid enough subsets to give \(i(F)\le5\cdot2^{r-3}\); two disjoint edges (possible only for \(r\ge4\)) give the smaller bound \(9\cdot2^{r-4}\). This proves the stated two-term expansion for fixed \(r\ge3\). Direct enumeration gives the displayed formulas for \(r=2\) and \(r=3\).

## Verification
The standalone standard-library program `verify.py` enumerates admissible finite extensions directly, then separately enumerates independent sets of the associated Cartesian product; it compares both counts for 263 small labelled cases. It also checks 14 independent-parameter profile identities and 443 exact single-query padding reductions for small bipartite inputs with arities 2, 3 and 4. The actual output in `verification_output.txt` is:

```
DIRECT_EXTENSION_VS_PRODUCT_PASS 263
INDEPENDENT_PARAMETER_EXACT_PROFILES_PASS 14
ONE_QUERY_METRIC_REDUCTION_PASS 443
ALL_TESTS_PASS
```

These computations are finite corroboration only. The proof establishes the claims for all permitted finite inputs and every fixed arity.

## Relationship to prior work
Henson established the countable homogeneous universal triangle-free graph and its finite extension property. Conant's 2014 manuscript, Section 3, gives the graph-theoretic description of injective tuple types and finite extension consistency; hence the *existence criterion itself is prior*, not claimed as novel. The corresponding higher-arity Cartesian-product **counting identity** makes that criterion explicit.

A published published-finding corpus finding, *Exact finite-parameter 1-type counting in Henson graphs is #P-complete* (2026), proves the independent-set polynomial and counting complexity **for 1-types**. This is the closest direct result; it explicitly excludes higher arity from its scope. The new hardness assertion is for each fixed arity at least two, with a separate one-query padding reduction and the bipartite input restriction. Neither the 2014 finite-extension criterion nor the 1-type complexity result states or logically supplies that specific higher-arity reduction without additional argument.

Provan and Ball's earlier work supplies the \(\#\mathrm P\)-complete source problem of bipartite vertex-cover counting, equivalent by complementation to counting independent sets. Exact first- and higher-arity comparisons were searched under finite parameter types, automorphism orbits, independent-set products, prism graphs, and counting complexity; no equivalent fixed-higher-arity theorem was located.

## Limitations
This result does not assert a parsimonious hardness reduction, any hardness of approximate type counting, or complexity bounds uniform when arity is part of the input. Its mathematical novelty depends primarily on the higher-arity product-count formulation and the fixed-higher-arity metric hardness reduction; the finite-extension admissibility facts are classical. Unindexed or differently phrased specialized treatments could subsume some of these conclusions.

## References
1. C. W. Henson, “A family of countable homogeneous graphs,” *Pacific Journal of Mathematics* 38 (1971), 69–83. DOI: 10.2140/pjm.1971.38.69. https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-p.pdf
2. G. Conant, “Forking and dividing in Henson graphs,” first arXiv submission 2014-01-08, arXiv:1401.1570; *Notre Dame Journal of Formal Logic* 58 (2017), 555–566. https://arxiv.org/html/1401.1570v1
3. J. S. Provan and M. O. Ball, “The complexity of counting cuts and of computing the probability that a graph is connected,” *SIAM Journal on Computing* 12 (1983), 777–788. DOI: 10.1137/0212053.
4. “Exact finite-parameter 1-type counting in Henson graphs is #P-complete,” publicly indexed research finding, 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650
