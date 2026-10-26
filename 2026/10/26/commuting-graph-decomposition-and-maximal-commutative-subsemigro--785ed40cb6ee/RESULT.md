# Commuting-graph decomposition and maximal commutative subsemigroups of free left legal semigroups

## Finding

**Theorem.** For an integer \(n\ge2\), let \(S_n\) be the free left legal semigroup on an \(n\)-letter alphabet, with defining identity \(xyx=xy\). Its (simple, undirected) commuting graph \(G_n\) has every element of \(S_n\) as a vertex and an edge between two distinct elements precisely when they commute. There are no central elements, so this agrees with the usual convention that central vertices are omitted.

Put \((m)_j=m!/(m-j)!\), \(B_m=\sum_{j=0}^{m}(m)_j\), and \(C_m=\sum_{j=0}^{m}(2j+1)(m)_j\). Let \(T_m\) be the comparability graph of the prefix order on all injective words (including the empty word) over an \(m\)-letter alphabet. Then

\[
G_n\cong n\left(K_1\vee T_{n-1}\right)\;\sqcup\;n(n-1)T_{n-2}.
\]

Here \(\sqcup\) is disjoint union, \(\vee\) is graph join, and integer coefficients denote disjoint copies. In particular, \(G_n\) has exactly \(n^2\) connected components, \(2nB_{n-1}\) vertices, and

\[
\#\{(u,v)\in S_n^2:uv=vu\}
=n\bigl(C_{n-1}+2B_{n-1}+1\bigr)+n(n-1)C_{n-2}
\]

ordered commuting pairs (diagonal pairs included).

**Maximal commutative subsemigroups.** Exactly \(2n!\) maximal commutative subsemigroups exist: \(n!\) have size \(n+1\), and \(n!\) have size \(n-1\). They are precisely the chains represented, for any ordered listing \(a,b_1,\ldots,b_{n-1}\) of the alphabet, by

\[
\{a,aa,aab_1,aab_1b_2,\ldots,aab_1\cdots b_{n-1}\}
\]

and, for any ordered listing \(a,b,c_1,\ldots,c_{n-2}\), by

\[
\{ab,abc_1,abc_1c_2,\ldots,abc_1\cdots c_{n-2}\}.
\]

These families are distinct, including the \(n=2\) boundary where the latter subsemigroups are singletons. The commuting graph is a cograph (hence perfect) and has independence number \(2n!\).

**Integral Laplacian spectrum.** Regard a spectrum as a multiset, and define \(\Lambda_0=\{0\}\). For \(m\ge1\) let

\[
\Lambda_m=\{0,B_m\}\uplus\{1^{[m-1]}\}
\uplus m\{\lambda+1:\lambda\in\Lambda_{m-1}\setminus\{0\}\},
\]

where \(1^{[0]}\) is empty, \(\uplus\) denotes multiset union, and \(m\{\cdots\}\) repeats each multiset member \(m\) times. Put

\[
\mathcal H_m=\{0,B_m+1\}\uplus\{\lambda+1:\lambda\in\Lambda_m\setminus\{0\}\}.
\]

Then the complete Laplacian spectrum of \(G_n\) is \(n\mathcal H_{n-1}\uplus n(n-1)\Lambda_{n-2}\). Thus every Laplacian eigenvalue is an integer; eigenvalue zero has multiplicity exactly \(n^2\).

## Assumptions and scope

The alphabet has \(n\ge2\) distinct symbols; the free algebra is a **semigroup without an adjoined identity**. The identity \(xyx=xy\) defines the variety of left legal semigroups. Ordinary equality of semigroup elements is equality of the unique word normal forms from Nagy's Theorem 3. Graph vertices represent distinct semigroup elements rather than words in an ambient free monoid, and a commuting pair \((u,u)\) counts once in the ordered-pair formula but does not create a loop. Laplacians are unweighted combinatorial graph Laplacians \(L=D-A\).

For completeness, write \(w=a_1\cdots a_r\) for an injective word. It has two distinct normal-form incarnations: the **plain** element \(w\) and the **doubled** element \(a_1w\), whose first letter appears twice. Multiplication concatenates representations, deletes subsequent appearances of letters, and keeps the initial letter doubled if and only if the first two letters of the concatenation agree. There are \(2\sum_{r=1}^n(n)_r=2nB_{n-1}\) elements. This multiplication rule is established in the cited primary source, not asserted as new.

## Proof

**1. Complete commutation criterion.** The first letter of a product is the first letter of its left operand, so any two commuting elements have the same first letter, say \(a\). When both are doubled and start with \(aa\), their products are doubled and are equal exactly when their underlying injective words are prefix-comparable: the product in either direction retains the first word, followed by all previously unseen letters of the second. Two plain elements of lengths at least two similarly commute exactly when their underlying injective words are prefix-comparable. Indeed, when their first two letters are distinct, neither concatenation creates a doubled initial letter, and the two concatenations have the same first-occurrence order exactly when one of the two injective words is a prefix of the other. If one plain word has length at least two and the other word is doubled, the products have different initial-double flags and cannot agree.

The remaining case involves the plain singleton \(a\). It commutes with every doubled word beginning \(aa\) (both products equal the doubled word), but with no longer plain word beginning \(a\) (the two products have different double flags). Distinct initial letters never commute. A plain singleton commutes with itself, as any element does. This proves the criterion in every boundary case.

**2. Components.** For each initial letter \(a\), the plain singleton \(a\) and all doubled elements \(aa v\), with \(v\) an injective word on the other \(n-1\) letters (possibly empty), form a connected component \(K_1\vee T_{n-1}\). Separately, plain words of length at least two partition by their ordered initial pair \((a,b)\), \(a\ne b\), with suffix an injective word on the other \(n-2\) letters. Each such component is \(T_{n-2}\). All these comparability graphs contain their root, hence are connected. The asserted disjoint-union isomorphism, component count and vertex count follow.

**3. Maximal commuting families.** A clique in any prefix-comparability graph is exactly a chain, and its maximal chains extend from the empty word to a word containing every available letter. A component \(K_1\vee T_{n-1}\) has \((n-1)!\) maximal cliques of size \(n+1\); a component \(T_{n-2}\) has \((n-2)!\) maximal cliques of size \(n-1\). These multiply by \(n\) and \(n(n-1)\), respectively, giving \(n!\) of each type. In either family every product of two distinct elements equals the longer prefix, except that the singleton \(a\) squares to \(aa\) within the displayed big clique. The product of any element with itself also stays in the family. Thus each maximal clique is a commutative subsemigroup; conversely, any maximal commutative subsemigroup is a maximal clique because every clique can be enlarged to one of these explicitly closed maximal chains. This proves both the cardinalities and the representatives.

**4. Pair count, cograph property, independence.** In \(T_m\), a vertex corresponding to a word of length \(j\) has exactly \(j\) shorter prefix-neighbors. Counting ordered commuting pairs yields \(C_m=B_m+2\sum_{j=0}^m j(m)_j\). The joined singleton contributes \(2B_m+1\) more ordered pairs. Summing over components gives the displayed formula. Prefix trees obey \(T_0=K_1\), \(T_m=K_1\vee(mT_{m-1})\). Since cographs are generated from one vertex by disjoint union and join, all components and their union are cographs, hence perfect. For a rooted prefix tree, an antichain injects into the set of leaves by extending each word; thus \(\alpha(T_m)=m!\) for \(m\ge0\). In a joined component the root contributes no improvement over an antichain of \(T_{n-1}\); summing \(n(n-1)!+n(n-1)(n-2)!=2n!\) proves the independence number.

**5. Laplacian spectrum.** The total order of \(T_m\) is \(B_m=1+mB_{m-1}\). In \(T_m=K_1\vee(mT_{m-1})\), a constant vector gives eigenvalue zero, the contrast between root and remainder gives \(B_m\), contrasts among the \(m\) component-wise constant vectors give eigenvalue one with multiplicity \(m-1\), and every nonconstant eigenvector of a \(T_{m-1}\) copy acquires eigenvalue \(\lambda+1\). This is exactly the recursion for \(\Lambda_m\). The same join calculation gives \(\mathcal H_m\) for \(K_1\vee T_m\). Taking disjoint-union multiplicities yields the claimed full spectrum. In particular, all eigenvalues are integral and zero multiplicity equals the connected-component count.

## Verification

The included `verify.py` independently enumerates all normal-form words, multiplies raw concatenated words by a first-occurrence normalizer, constructs the commuting graph, finds its connected components and maximal cliques, and checks the ordered commuting-pair count. For \(n=2,3,4\) it also computes the exact rational nullity of every predicted Laplacian eigenspace and checks that the multiplicities exhaust the whole graph. Because the Laplacian is real symmetric, eigenspace dimensions equal algebraic multiplicities. This uses only the Python standard library.

Recorded passing outputs:

- \(n=2\): 8 elements; 4 components; 20 ordered commuting pairs; 2 maximal cliques of each size 1 and 3.
- \(n=3\): 30 elements; 9 components; 108 ordered commuting pairs; 6 maximal cliques of each size 2 and 4.
- \(n=4\): 128 elements; 16 components; 664 ordered commuting pairs; 24 maximal cliques of each size 3 and 5.

These checks are finite corroborations; the general graph, subsemigroup and spectrum statements follow from the proof above.

## Relationship to prior work

Nagy, *On left legal semigroups* (2023), Theorem 3 and equation (1), supplies the free semigroup normal forms and multiplication (including the original two-generator multiplication table). That source studies variety structure, retract ideals, separativity and semilattice congruences, not the full commuting graph, maximal commutative subsemigroup census or Laplacian spectrum proved here. The proof above does not claim new normal forms, new associativity or new free-object constructions.

Brauner, Commins and Reiner study free **left regular bands**, whose generators are already idempotent. Their combinatorial structures provide context but do not determine the doubled-generator components of this non-band semigroup. Likewise, work on commuting graphs of completely simple semigroups does not directly cover this free semigroup: its square is a proper two-sided ideal (the plain generators lie outside it). General facts about prefix-tree comparability graphs and graph joins are used as elementary ingredients rather than claimed as discoveries.

## Limitations

The classification concerns **finite rank** \(n\ge2\) and the specified free left legal semigroup without identity. It does not classify maximal commutative subsemigroups of arbitrary quotients, non-free left legal semigroups, or infinite-rank versions. The statements give finite exact spectra, not asymptotic spectral limits. The result is a derived structural theorem over Nagy's normal form; no claim of exhaustive priority across all terminology for commuting semigroup graphs or prefix-tree graph constructions is made.

## References

1. A. Nagy, *On left legal semigroups*, arXiv:2301.08793, first posted 20 January 2023, Theorem 3, equation (1), and Section 3. https://arxiv.org/abs/2301.08793
2. A. Brauner, J. Commins and V. Reiner, *Invariant theory for the free left-regular band and a q-analogue*, arXiv:2206.11406 (2022). https://arxiv.org/abs/2206.11406
3. F. Bastidas, A. Brauner and F. Saliola, *Left regular bands of groups and the Mantaci–Reutenauer algebra*, arXiv:2306.14985 (2023), especially the free-left-regular-band background. https://arxiv.org/abs/2306.14985
