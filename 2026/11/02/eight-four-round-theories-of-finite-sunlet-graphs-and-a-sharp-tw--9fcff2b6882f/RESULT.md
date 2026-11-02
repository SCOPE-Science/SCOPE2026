# Eight four-round theories of finite sunlet graphs and a sharp twenty-vertex cutoff

## Finding

For every integer \(n\ge3\), let \(S_n\) be the *sunlet graph*: start with the undirected cycle \(C_n\) and attach exactly one new leaf to each cycle vertex. Thus \(S_n\) is the graph corona \(C_n\circ K_1\), has \(2n\) vertices, and is a connected unicyclic graph of maximum degree three. In first-order logic with equality and the *uncoloured* symmetric adjacency relation, write \(G\equiv_4 H\) if the structures agree on all sentences of quantifier rank at most four.

**Theorem.** For every \(m,n\ge3\),
\[
S_m\equiv_4 S_n\quad\Longleftrightarrow\quad (m=n<10)\ \lor\ (m,n\ge10).
\]
Consequently this family has exactly eight rank-four theories, represented by \(S_3,S_4,\ldots,S_{10}\). Its sharp smallest-possible maximum representative order is \(20\) vertices, attained by \(S_{10}\).

## Assumptions and scope

The vertex set is \(\{(i,s):i\in\mathbb Z/n\mathbb Z,\ s\in\{0,1\}\}\), where \(s=0\) means a rim vertex and \(s=1\) its pendant leaf. Distinct vertices are adjacent exactly when either they have the same coordinate and opposite sides or both have side zero and their coordinates differ by \(1\) modulo \(n\). There are no additional predicates naming the rim, leaves, orientation, or coordinates; equality is part of the language. All structures are finite simple undirected graphs. The theorem is relative to the family \(\{S_n:n\ge3\}\), not a uniform assertion about every graph of maximum degree three.

## Proof

**1. Transfer from cycles.** For any two graphs \(A\) and \(B\), if Duplicator has a winning strategy in the four-round Ehrenfeucht–Fraïssé game on \(A,B\), she also wins the four-round game on \(A\circ K_1,B\circ K_1\). To respond to a vertex \((a,s)\), she plays coordinate \(a\) in the underlying game, receives \(b\), and chooses \((b,s)\). A selected tuple is an atomic partial isomorphism in the corona exactly when its coordinate equalities and adjacencies, together with its side labels, satisfy the corresponding conditions; these are preserved by the base-game strategy. Repeated coordinate selections are allowed and are handled by the base-game equality condition. Thus the transfer does not increase quantifier rank.

Brown and Hoshino (2007), Theorem 4.9, establish that all simple undirected cycles of lengths at least \(11\) are four-round equivalent. Applying the transfer proves \(S_m\equiv_4 S_n\) whenever \(m,n\ge11\).

**2. Exact finite boundary.** For a finite graph \(G\), a tuple \(\bar v\), and integer \(r\ge0\), define its recursive \(r\)-type \(\tau_r^G(\bar v)\) by
\[
\tau_0^G(\bar v)=\text{the complete equality-and-adjacency diagram of }\bar v,
\]
\[
\tau_{r+1}^G(\bar v)=
 \left(\tau_0^G(\bar v),\left\{\tau_r^G(\bar v,w):w\in V(G)\right\}\right).
\]
By induction on first-order formulas, two tuples have the same \(r\)-type exactly when they satisfy the same formulas of quantifier rank at most \(r\) whose free variables are among the tuple entries. The atomic case is immediate; boolean connectives preserve type, and an existential quantifier is decided by the displayed set of one-point extension types. Negation handles universal quantification. For empty tuples, equality of \(\tau_4\) is exactly \(\equiv_4\).

We compute these exact types for every \(3\le n\le12\), with tuple lengths \(4,3,2,1,0\) and remaining ranks \(0,1,2,3,4\), respectively, using `sunlet_direct.py`. Crucially, tuples are **ordered and may repeat vertices**, and at every stage type signatures are interned globally across all graph orders being compared (rather than separately within each graph). The resulting equivalence partition is
\[
\{3\},\ \{4\},\ \{5\},\ \{6\},\ \{7\},\ \{8\},\ \{9\},\ \{10,11,12\}.
\]
The exhaustive recursion is finite, exact integer-and-set computation, not a statistical experiment.

A second implementation, `sunlet_orbit.py`, computes the same recursion after quotienting tuple configurations by rotation and reflection of the rim. Given a nonempty tuple, it translates the first rim coordinate to zero and takes the lexicographically least of that tuple and its reflection, **without exchanging leaves and rim vertices**. These are precisely the two dihedral normalizations sending the first selected coordinate to zero. Since the dihedral maps are graph automorphisms, replacing tuples by these representatives preserves all atomic diagrams and all extension-type sets. It finds the same eight classes for every \(3\le n\le15\). The pair of calculations checks the finite boundary using both full enumeration and a structurally different orbit reduction.

In particular \(S_{10}\equiv_4S_{11}\), while \(S_3,\ldots,S_9\) lie in seven distinct classes and none is equivalent to \(S_{10}\). Combining the finite bridge with Step 1 gives the asserted infinite classification by transitivity.

**3. Optimal bound.** The representatives \(S_3,\ldots,S_{10}\) have sizes \(6,8,10,12,14,16,18,20\), respectively. Since no smaller member of the family is equivalent to \(S_{10}\), the bound of twenty vertices cannot be reduced within the family.

## Verification

Use Python 3 with its standard library and run, in the directory containing these files:

```sh
python3 sunlet_direct.py 12 direct_result.json
python3 sunlet_orbit.py 15 orbit_result.json
```

These programs were executed from the packaged paths. The direct implementation enumerated \(971088\) ordered four-tuples across the ten graphs of rim orders \(3\) through \(12\); its successive numbers of type signatures, from length four to length zero, were \(116,122,46,14,8\). The orbit implementation reached the same numbers of type signatures and the same eight-part partition while examining all rim orders through \(15\). Exact result objects are included in `direct_result.json` and `orbit_result.json`.

The published cycle theorem supplies the infinite tail independently of any finite extrapolation. Neither enumeration, on its own, establishes that infinitely many additional cases have the same type.

## Relationship to prior work

Brown and Hoshino (2007) provide the complete four-round equivalence classification for plain undirected cycles, with stabilization at length \(11\), not for leaf-decorated sunlets. Their result and the transfer lemma imply only that sunlets stabilize *by* length \(11\); the exact earlier equivalence of lengths \(10\) and \(11\) and the preceding pairwise separations require the new finite-boundary argument. Barik, Pati and Sarma (2007) study spectra of graph corona products and provide related graph-product context without making bounded-rank logical equivalence claims. Iqbal et al. (2021) study connected safe numbers of sunlet graphs, a different graph invariant.

The same objects may appear under the names *sunlet*, *sun graph*, *hairy cycle*, or \(C_n\circ K_1\); the term *crown graph* has multiple conflicting graph-theoretic meanings. Searches for these names and logical equivalence did not locate a prior exact four-round classification. Such searches do not establish historical priority, and an inaccessible or unindexed result could still cover the assertion.

## Limitations

The theorem is for uncoloured first-order adjacency with equality and quantifier rank exactly at most four. It does not determine higher-rank theories, interpretations with explicitly named leaves, or the logical equivalence of general unicyclic graphs. The supporting finite calculations have undergone internal mathematical review, not independent mathematical validation. Historical-priority search is necessarily incomplete.

## References

1. S. Barik, S. Pati and B. K. Sarma, *The Spectrum of the Corona of Two Graphs*, SIAM J. Discrete Math. 21 (2007), 47–56, doi:10.1137/050624029. First available online 2007-01-12.
2. J. Brown and R. Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles*, Ars Combinatoria 83 (2007), 193–212, Theorem 4.9. Published 2007-04-30. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf
3. R. Iqbal, M. S. Sardar, D. Alrowaili, S. Zafar and I. Siddique, *On the Connected Safe Number of Some Classes of Graphs*, J. Mathematics (2021), article 9483892, section 4, doi:10.1155/2021/9483892.
