# Sharp Horn witness arity and symmetry transition in Kneser disjointness concept lattices

## Finding

For every pair of integers \(n\ge 2k\ge 2\), the Galois closure of the Kneser disjointness context admits an explicit description and a sharp premise-witness bound. Put \(U=[n]\), \(\mathcal K=\binom Uk\), and take objects and attributes to be two copies of \(\mathcal K\), with incidence \(X I Y\) precisely when \(X\cap Y=\varnothing\). For \(B\subseteq\mathcal K\), let \(c(B)=B''\) be its attribute closure. Writing \(W=\bigcup B\), the complete formula is
\[
c(B)=\begin{cases}
\{A\in\mathcal K:A\subseteq W\},& |W|\le n-k,\\
\mathcal K,& |W|\ge n-k+1.
\end{cases}
\]
The closed-intent lattice has exactly
\[
2+\sum_{j=k}^{n-k}\binom nj
\]
elements, ordered by inclusion. The corresponding formal concept lattice is its order dual, so all stated automorphism, modularity, and isomorphism conclusions apply to both.

Define the Horn witness number \(h(c)\) to be the maximum, over all \(B\subseteq\mathcal K\) and \(A\in c(B)\), of the minimum cardinality of \(B_0\subseteq B\) with \(A\in c(B_0)\). Then
\[
h(c)=\begin{cases}1,&k=1,\\n-2k+2,&k\ge2.\end{cases}
\]
For \(k\ge2\), this coincides numerically with the **known** Lovász chromatic-number formula for the Kneser graph, \(\chi(KG(n,k))=n-2k+2\); this does not constitute a new proof of the chromatic-number theorem.

The full order-preserving automorphism group has the sharp transition
\[
\operatorname{Aut}(\mathcal L_{n,k})\cong
\begin{cases}
\mathfrak S_{\binom{2k}{k}},&n=2k,\\
\mathfrak S_n,&n>2k.
\end{cases}
\]
The lattice is modular precisely when \(k=1\) or \(n=2k\); it is distributive precisely when \(k=1\). Two such lattices are isomorphic if and only if their parameter pairs \((n,k)\) agree.

For example, \((n,k)=(4,2)\) yields an eight-element rank-two lattice with automorphism group \(\mathfrak S_6\); \((5,2)\) yields a 22-element lattice with automorphism group \(\mathfrak S_5\). Both have sharp Horn witness number \(2\) and \(3\), respectively.

## Assumptions and scope

The ground set is finite and \(n,k\) are positive integers satisfying \(n\ge2k\). Incidence is **disjointness between two copies of the family of \(k\)-subsets**, not element-membership incidence between \(k\)-sets and points. The closure operator acts on families of attributes, not on subsets of ground points. No variables are weighted and no additional incidence conditions are assumed. All lattice automorphisms preserve order; no assertion is made about arbitrary anti-automorphisms.

## Proof

**Exact closure.** A copy of \(X\in\mathcal K\) is incident with every attribute of \(B\) if and only if \(X\subseteq U\setminus W\), where \(W=\bigcup B\). If \(|U\setminus W|\ge k\), the union of **all** such \(k\)-sets equals \(U\setminus W\); a given attribute \(A\) is incident with all of them precisely when \(A\subseteq W\). If \(|U\setminus W|<k\), there are no common objects, so every attribute belongs to the double prime. This proves the formula even for \(B=\varnothing\).

**All closed intents and their rank.** If \(k\le |W|\le n-k\), the family \(F_W=\{A\in\mathcal K:A\subseteq W\}\) is closed. It determines \(W\) uniquely because the union of its members is \(W\). Besides these families the only closed intents are \(\varnothing\) and \(\mathcal K\). Their order is exactly the inclusion order of the labels \(W\), with a new least and greatest element. This gives the stated count. It is a graded lattice of length \(n-2k+2\), with atoms indexed by the \(k\)-sets and the rank of \(F_W\) equal to \(|W|-k+1\).

**Upper bound on witnesses.** Put \(r=n-2k+2\). For \(k=1\), the closure formula is the identity, proving \(h(c)=1\). Let \(k\ge2\), \(B\subseteq\mathcal K\) and \(A\in c(B)\). If \(A\not\subseteq\bigcup B\), the closure formula forces \(|\bigcup B|\ge n-k+1\). Starting from one \(k\)-set and repeatedly adjoining a member of \(B\) increasing the covered union gives at most \(r\) sets before reaching \(n-k+1=k+r-1\) covered points. Their closure is all of \(\mathcal K\).

If instead \(A\subseteq\bigcup B\), choose an inclusion-minimal subfamily \(B'\subseteq B\) covering \(A\). Every member of \(B'\) has a private point of \(A\) absent from all other members. Therefore any \(s\) distinct members of \(B'\) have a union of size at least \(k+s-1\): take the \(k\) points in one member and a distinct private point from each of the remaining \(s-1\) members. If \(|B'|\le r\), it directly witnesses \(A\); if \(|B'|>r\), any \(r\) members have union size at least \(k+r-1=n-k+1\) and witness \(A\) by producing the whole closure. Thus \(h(c)\le r\).

**Sharpness.** Take any \((k-1)\)-element set \(C\), and distinct points \(x_1,\ldots,x_r\notin C\). Let \(B=\{C\cup\{x_i\}:1\le i\le r\}\). Its union has exactly \(n-k+1\) elements, leaving \(k-1>0\) ground points outside. Choose a \(k\)-set \(A\) containing one of those omitted points. Then \(A\in c(B)=\mathcal K\). Every proper subfamily of \(B\) has union of size at most \(n-k\) and still omits that point, so it does not imply \(A\). Exactly \(r\) premises are necessary. This proves equality for every \(k\ge2\).

**Automorphisms.** For \(n=2k\), there are no intermediate ranks: the lattice consists of a bottom, a top, and \(\binom{2k}{k}\) incomparable atoms. Thus every permutation of its atoms is an order automorphism. For \(n>2k\), two different atoms labeled \(A,B\in\binom Uk\) have join of rank two exactly when \(|A\cap B|=k-1\), i.e. when they are adjacent in the Johnson graph \(J(n,k)\). A lattice automorphism therefore induces an automorphism of this Johnson graph. If \(k=1\), these are arbitrary permutations of the \(n\) atoms, as required. If \(k\ge2\), every maximal clique of \(J(n,k)\) lies either in a star indexed by a \((k-1)\)-subset, of cardinality \(n-k+1\), or in a top indexed by a \((k+1)\)-subset, of cardinality \(k+1\). Indeed, fix adjacent \(k\)-sets \(A=C\cup\{a\}\) and \(B=C\cup\{b\}\), where \(|C|=k-1\). Any third neighbor of both either contains \(C\) or is of the form \((C\setminus\{c\})\cup\{a,b\}\); a member of the first form using an element outside \(C\cup\{a,b\}\) cannot be adjacent to a member of the second form. Therefore an entire clique lies in one of these two families. Since \(n>2k\), stars are strictly larger and so are intrinsic. Their intersections recover adjacency of the \((k-1)\)-subsets, and induction on \(k\) identifies every automorphism with a unique permutation of the underlying \(n\) ground elements. Conversely every such permutation acts on the entire closed-intent lattice. Hence the automorphism group is exactly \(\mathfrak S_n\).

**Modularity and distributivity.** For \(k=1\), the lattice is Boolean. For \(n=2k\), its rank is two, so it is modular; when \(k\ge2\), it has at least three atoms and is not distributive. For \(n>2k\) and \(k\ge2\), choose disjoint \(k\)-sets \(A,B\), a point \(b\in B\), and the closed rank-two element \(Z=F_{A\cup\{b\}}\). Then the atom \(F_A\le Z\), while \(F_B\wedge Z=\varnothing\) and \((F_A\vee F_B)\wedge Z=Z\ne F_A=F_A\vee(F_B\wedge Z)\). The modular law fails. Thus the asserted criteria are exact.

**Recovery of parameters.** From the abstract lattice read its length \(h=n-2k+2\) and its atom count \(m=\binom nk=\binom{2k+h-2}{k}\). For each fixed \(h\ge2\), this binomial coefficient is strictly increasing with the positive integer \(k\): map every \(k\)-subset of a \((2k+h-2)\)-element set to a \((k+1)\)-subset after adjoining one distinguished new point in a ground set enlarged by two points, leaving extra \((k+1)\)-subsets. Hence \(m\) determines \(k\), and then \(n=h+2k-2\). No different parameter pairs give isomorphic lattices.

## Verification

The companion standard-library Python program `verify_kneser.py` reconstructs closures directly by enumerating common **disjoint** object sets, separately computes the closed-set formula, enumerates Möbius values, checks the modularity counterexamples, enumerates all small Horn witnesses, and counts Johnson-graph automorphisms from adjacency. It returns `VERIFY_OK`. Full closure comparisons are exhaustive when \(\binom nk\le13\), with deterministic pseudorandom comparisons otherwise. The automorphism checks include the exceptional \((4,2)\) case and nonexceptional \((5,2)\) and \((6,2)\) cases. Finite checks are corroboration, not a proof for arbitrary parameters; the preceding arguments establish the general theorem.

## Relationship to prior work

The foundational 2023 treatment by Rawson, Myers, Green, Robinson and Joslyn identifies general concept-lattice representations of hypergraph incidence and motivates structural questions for uniform families. Cattaneo, Chiaselotti, Ciucci and Gentile (2016), Proposition 4.12, explicitly classify the lattice of a **different** complete-uniform incidence context, whose attributes are individual ground points and whose incidence is set membership: its intent lattice uses \(\{T\subseteq U:|T|\le k\}\cup\{U\}\). Here the attributes are themselves \(k\)-subsets and the incidence is disjointness, producing the band \(k\le|T|\le n-k\). Neither inspected source supplies the sharp disjointness Horn-witness arity or automorphism-group jump.

The formula \(\chi(KG(n,k))=n-2k+2\) for Kneser graphs at \(k\ge2\) is Lovász's **established theorem**. Its numerical equality with the witness bound is an observed corollary here, not a new chromatic proof. Standard Johnson-graph automorphism ideas and the general FCA double-prime construction are used with attribution.

A published rank-band antichain census studies the proper Boolean ranks two through four on six points, which overlaps the **abstract underlying poset** for one parameter pair, but not the new closure witness invariant or all-parameter automorphism transition. Consequently novelty is assessed as a combination of exact statements, not as novelty of the rank-truncated Boolean poset itself.

## Limitations

The theorem concerns only complete uniform disjointness contexts with \(n\ge2k\), ordinary (unweighted) implications, and order-preserving automorphisms. The classification does not extend without proof to arbitrary Kneser-type hypergraphs, partial uniform families, or weighted implications. The chromatic connection is an equality of proven formulas, not a claimed structural equivalence between coloring and Horn witnesses. Although the closest relevant full-text publications were examined, an older equivalent formulation under another terminology cannot be excluded without independent literature review. Independent audit has not been performed.

## References

1. D. Rawson, A. Myers, L. Green, C. Robinson, and R. Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681 (first version 2023-07-21), https://arxiv.org/abs/2307.11681.
2. G. Cattaneo, G. Chiaselotti, D. Ciucci, and T. Gentile, *On the connection of Hypergraph Theory with Formal Concept Analysis and Rough Set Theory*, Information Sciences **330** (2016), 342–357, DOI:10.1016/j.ins.2015.09.054; author-accepted open text https://boa.unimib.it/retrieve/e39773b2-f7e4-35a3-e053-3a05fe0aac26/HypFINAL.pdf.
3. L. Lovász, *Kneser's conjecture, chromatic number, and homotopy*, Journal of Combinatorial Theory, Series A **25** (1978), 319–324, DOI:10.1016/0097-3165(78)90022-5.
