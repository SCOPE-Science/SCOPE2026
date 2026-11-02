# A coatom sphere theorem for convex union-closed team properties

## Finding

Let \(V\) be any finite set of \(n\geq 1\) valuations. Write \(\mathcal T=2^V\) for its possible teams and \(L(V)\) for the poset, under inclusion, of all **convex union-closed properties** \(P\subseteq\mathcal T\), including the empty property. A property is union-closed if \(s,t\in P\) implies \(s\cup t\in P\), and convex if \(s,t\in P\) and \(s\subseteq u\subseteq t\) imply \(u\in P\). Then \(L(V)\) is a finite bounded lattice, and its proper-part order complex has the homotopy type

\[\Delta(L(V)\setminus\{\hat 0,\hat 1\})\simeq S^{n-1}.\]

More precisely, **all** its coatoms are the \(n+1\) properties

\[C_* = 2^V\setminus\{\varnothing\},\qquad C_v=2^{V\setminus\{v\}}\quad (v\in V).\]

Here \(C_*\) contains every nonempty team, whereas \(C_v\) contains all teams that omit valuation \(v\). Consequently its top-to-bottom Möbius number is

\[\mu_{L(V)}(\hat0,\hat1)=(-1)^{n-1}.\]

For the usual semantic universe of \(k\geq1\) propositional letters, \(n=2^k\). By expressive completeness of convex union-closed propositional team logics, the same sphere and Möbius number describe their finite semantic-equivalence quotient ordered by inclusion of denotations: the sphere has dimension \(2^k-1\), and the Möbius number equals \(-1\).

## Assumptions and scope

A *team* is a subset of the finite valuation set \(V\), and a *property* is a set of teams. No nonemptiness of teams or properties is assumed: in particular the empty team \(\varnothing\), the empty property \(\hat0=\varnothing\), and the universal property \(\hat1=2^V\) are different objects. Union closure means closure under unions of two *member teams*, not closure under unions of arbitrary properties. The ground size \(n\) is arbitrary and finite with \(n\geq1\); it need not be a power of two for the combinatorial theorem.

The weak-ideal characterization and finite-variable expressive completeness are background theorems of Anttila and Knudstorp, and are reported in the 2026 semantic translation work. The new assertion is the precise coatom structure and the homotopy/Möbius type of the entire lattice of such properties. The order-complex statement means an ordinary homotopy equivalence of geometric realizations; it does not assert a simplicial isomorphism or a point-set homeomorphism.

## Proof

**1. Lattice structure.** Arbitrary intersections of convex union-closed properties are again convex and union-closed. In particular \(L(V)\) is a closure system inside the finite Boolean lattice of properties. Therefore it is a bounded lattice, with meet given by intersection, bottom the empty property, and top the universal property.

**2. Every proper property lies below a displayed coatom.** Let \(P\in L(V)\) be proper. If the empty team is absent from \(P\), then \(P\subseteq C_*\). Otherwise the empty team belongs to \(P\), so \(P\) is nonempty. Define

\[U=\bigcup_{t\in P}t.\]

Because \(V\) is finite, the nonempty family \(P\) is finite; repeated binary-union closure gives \(U\in P\). Every \(t\in P\) lies in \(U\). If \(U=V\), convexity between \(\varnothing\in P\) and \(V=U\in P\) forces \(P=2^V=\hat1\), contrary to propriety. Thus some \(v\in V\setminus U\) exists, and \(P\subseteq C_v\).

**3. These are exactly the coatoms.** Both \(C_*\) and all \(C_v\) satisfy union closure and convexity, and are proper. If a weak ideal contains \(C_*\) and additionally the empty team, it equals \(\hat1\). If a weak ideal contains \(C_v\) and additionally a team \(t\) with \(v\in t\), it also contains the team \(V\setminus\{v\}\in C_v\), and so union closure gives \(t\cup(V\setminus\{v\})=V\). Since \(\varnothing\in C_v\), convexity between \(\varnothing\) and \(V\) gives \(\hat1\). Thus each displayed element is maximal proper. Step 2 proves no others exist.

**4. The coatom nerve.** Let \(\overline L=L(V)\setminus\{\hat0,\hat1\}\). For each of the \(n+1\) coatoms \(C\), take the subcomplex \(K_C=\Delta((\hat0,C])\subseteq\Delta(\overline L)\). It is a cone with apex \(C\), and Step 2 shows these subcomplexes cover every chain of \(\overline L\). Since meets in \(L(V)\) are literal property intersections, for each nonempty selection \(\mathcal C\) of coatoms their common intersection is

\[\bigcap_{C\in\mathcal C}K_C=\Delta\bigl((\hat0,\bigcap_{C\in\mathcal C} C]\bigr).\]

This intersection is empty if the meet is the empty property, and otherwise is a cone at that nonempty meet. For any \(I\subseteq V\), the meets of selections from the \(C_v\)'s are

\[\bigcap_{v\in I}C_v=2^{V\setminus I},\]

which always contain the empty team and hence are nonempty as properties. When the additional coatom \(C_*\) is selected,

\[C_*\cap\bigcap_{v\in I}C_v=2^{V\setminus I}\setminus\{\varnothing\},\]

which is nonempty precisely when \(I\neq V\). Therefore the only empty nontrivial coatom intersection is the meet of all \(n+1\) coatoms. Their covering nerve has every proper subset of its \(n+1\) vertices as a face, but not the full set: it is the boundary of the \(n\)-simplex. The finite simplicial nerve lemma (equivalently, the coatom crosscut theorem) gives

\[\Delta(\overline L)\simeq\partial\Delta^n\simeq S^{n-1}.\]

**5. Möbius number and logical interpretation.** The Möbius invariant of a bounded finite poset is the reduced Euler characteristic of its proper-part order complex. Hence \(\mu(\hat0,\hat1)=\widetilde\chi(S^{n-1})=(-1)^{n-1}\). The background expressive-completeness theorem identifies the quotient of formulas by equality of supported-team denotations with the above property lattice; it preserves inclusion and thus its order complex. For \(k\geq1\), \(n=2^k\) is even, giving \(\mu=-1\).

## Verification

Run `python3 checker.py` with Python 3 and its standard library. The independent checker enumerates all candidate families of teams for \(n=1,2,3,4\), tests the defining closure conditions directly, checks the complete coatom list and all nonempty coatom intersections, and computes the Möbius invariant recursively from the bottom. It confirms \(4,11,42,283\) weak ideals, respectively, exactly \(n+1\) coatoms, and Möbius values \(1,-1,1,-1\). These finite checks are corroboration; the preceding proof establishes the theorem for all finite \(n\geq1\).

## Relationship to prior work

Anttila and Knudstorp establish expressive completeness for the convex union-closed propositional team properties and their semantic characterization. Aloni, Baltag, van Benthem, Bezhanishvili and Knudstorp use the same weak ideals in translations of bilateral state-based logic into semilattice modal logic. Neither of those examined works establishes the coatom list or an order-complex homotopy classification for the entire property lattice. The classical crosscut/nerve theorem supplies a general topological tool, but does not by itself identify the coatom intersections of this particular lattice. Thus the lattice-specific coatom analysis is essential.

## Limitations

This is an ordinary homotopy equivalence, not a canonical simplicial homeomorphism, and it computes the Möbius value only of the whole bounded lattice, not all intervals. It relies on finite valuation universes; for infinitely many valuations, finite-union closure need not produce a largest team. Logical realization of every weak ideal uses the cited expressive-completeness theorem, not a newly constructed formula translation. General order-theoretic statements might subsume the specific coatom analysis; prior-literature coverage outside the inspected sources remains a risk. No independent review has been performed.

## References

1. M. Aloni, A. Baltag, J. van Benthem, N. Bezhanishvili and S. B. Knudstorp, *Teams, Truthmakers, Translations*, arXiv:2610.15680v1 (public 2026-10-11), especially §3.1, https://arxiv.org/html/2610.15680v1 .
2. A. Anttila and S. B. Knudstorp, *Convex Team Logics*, arXiv:2503.21850v1 (public 2025-03-27), especially §3.1 and Theorem 3.5; version 3 also inspected, https://arxiv.org/abs/2503.21850 .
3. T. McConville, *Crosscut-simplicial Lattices*, arXiv:1409.6269 (2014), background on crosscut complexes, https://arxiv.org/abs/1409.6269 .
