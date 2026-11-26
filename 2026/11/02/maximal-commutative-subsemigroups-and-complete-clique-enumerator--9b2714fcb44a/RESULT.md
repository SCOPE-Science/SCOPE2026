# Complete commuting-clique polynomial of a finite Brandt semigroup

## Finding

Let \(G\) be a finite group of order \(m\), and let \(n\ge2\). Write
\[
P_G(z)=\sum_{\substack{X\subseteq G\\ab=ba\text{ for all }a,b\in X}}z^{|X|}.
\]
Let \(C_{n,G}(z)\) be the cardinality polynomial of all pairwise-commuting subsets of the nonzero elements of the Brandt semigroup \(B_n(G)\). Both polynomials include the empty set. For \(s,t\ge1\), define
\[
F^{(m)}_{s,t}(z)=\sum_{i=0}^{s}\sum_{j=0}^{t}(-1)^{s+t-i-j}\binom si\binom tj(1+z)^{mij}.
\]
Then
\[
\boxed{C_{n,G}(z)=P_G(z)^n+\sum_{\substack{s,t\ge1\\s+t\le n}}\binom{n}{s,t,n-s-t}P_G(z)^{n-s-t}F^{(m)}_{s,t}(z).}
\]
If zero is included as a vertex, the corresponding polynomial is \((1+z)C_{n,G}(z)\). In particular, to obtain every commuting-clique coefficient for a given index size it suffices to know the group commuting-subset polynomial and the order of the group.

## Assumptions and scope

The nonzero elements are \((i,g,j)\) with \(i,j\in[n]\) and \(g\in G\). The product \((i,g,j)(k,h,\ell)\) is \((i,gh,\ell)\) when \(j=k\), and zero otherwise. Zero annihilates all elements. The commuting graph here joins distinct commuting nonzero elements. The polynomial counts subsets, not ordered tuples, maximal cliques only, or necessarily product-closed subsemigroups. No commutativity assumption on \(G\) is made.

## Proof

Two diagonal elements at distinct indices commute since both products vanish; at the same index they commute exactly when their group labels do. A diagonal element and an off-diagonal element commute exactly when the diagonal index is not an endpoint of the off-diagonal element: at an endpoint precisely one of the two products is nonzero. Two off-diagonal elements commute exactly when both products are zero. Indeed, if both products are nonzero their indices have the form \((i,j)\) and \((j,i)\) for \(i\ne j\), and the products lie at distinct diagonal indices.

Thus a clique with no off-diagonal elements contributes to \(P_G(z)^n\). Otherwise let \(S\) be the set of first indices of its off-diagonal elements and \(T\) the set of last indices. These are nonempty and disjoint by the off-diagonal commutation rule, and the clique itself determines them uniquely. No diagonal member can occur at an index in \(S\cup T\), while each index outside \(S\cup T\) independently contributes a group commuting subset. At a fixed pair in \(S\times T\), the \(m\) available labels can be selected independently. However, each index of \(S\) and each index of \(T\) must be used at least once. If selection is restricted to \(i\) of the sources and \(j\) of the targets, the polynomial with no further support restrictions is \((1+z)^{mij}\). Inclusion–exclusion over unused indices gives exactly \(F^{(m)}_{s,t}\) when \(|S|=s\) and \(|T|=t\). The multinomial coefficient counts the choices of the ordered support partition. Summing once per occupied support proves the identity. Zero commutes with everything and is independently optional.

## Verification

The accompanying finite checker constructs Brandt multiplication directly, enumerates cliques including the empty clique, and compares their size counts with the formula. For instance, \(C_{2,C_1}(z)=1+4z+z^2\). For the symmetric group \(S_3\), \(P_{S_3}(z)=1+6z+6z^2+z^3\), and \(C_{2,S_3}(z)=1+24z+78z^2+114z^3+78z^4+24z^5+3z^6\). These are finite checks; the proof supplies the result at all index sizes and for all finite structure groups.

## Relationship to prior work

Kumar, Dalal and Pandey, *On the commuting graphs of Brandt semigroups* ([arXiv:2010.05000](https://arxiv.org/abs/2010.05000), Lemma 3.10 and Theorem 3.14), use disjoint source and target sets for extremal cliques in the trivial-group case. The Resultary record [*Maximal commutative subsemigroups of Brandt semigroups: exact size spectra and a Gaussian law*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-maximal-commutative-subsemigroups-of-brandt-semigroups-exact-siz--4fb43e2cf90b) gives the size polynomial of inclusion-maximal commutative subsemigroups. Those sizes do not count arbitrary subcliques, which can extend to more than one maximal family. The present formula counts each clique by its actual occupied supports, including incomplete off-diagonal rectangles and nonmaximal diagonal subsets. The classification and enumeration of maximal commutative subsemigroups are not asserted here as contributions.

## Limitations

Evaluating \(P_G\) for a large nonabelian group can be a separate counting problem. The product rule is specific to Brandt semigroups; the formula does not claim to count cliques in a general Rees matrix semigroup. This comparison with known results does not establish publication priority.
