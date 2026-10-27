# Leaf-color normal form and sharp fan-profile collapse for finite rooted Kripke trees

## Finding
For every nonempty finite rooted tree \(T\), equip its vertices with the **reflexive ancestor relation**: \(uRv\) exactly when \(u\) is an ancestor of \(v\), possibly equal. For each integer \(k\ge2\), let \(F_k\) be the reflexive fan of one bottom point \(0\) and \(k\) incomparable maximal points \(1,\ldots,k\). Let \(N_k(T)\) count all bounded morphisms \(T\to F_k\), not requiring surjectivity.

**Leaf-color normal form.** Such a morphism is uniquely determined by its restriction to the leaves, and a leaf coloring \(c:L(T)\to\{1,\ldots,k\}\) extends if and only if, for each vertex \(v\), the set \(c(L(T_v))\) contains either exactly one color or all \(k\) colors. Here \(T_v\) is the subtree below \(v\). The corresponding morphism takes value \(i\) on a one-colored subtree of color \(i\), and value \(0\) on a subtree containing all \(k\) colors.

Let \(S(d,k)\) be the Stirling number of the second kind, with \(k!S(d,k)=0\) if \(d<k\). For a leaf, \(N_k=k\), and for an internal vertex with \(d\) children having subtrees \(T_1,\ldots,T_d\),
\[
N_k(T)=k+\prod_{i=1}^{d}N_k(T_i)-k^d+k!S(d,k).
\]

**Sharp recovery and extremality.** With \(\ell\) leaves and maximum number \(\Delta\) of children at a vertex,
\[
N_2(T)=2^\ell,\qquad N_k(T)>k\iff 2\le k\le\Delta.
\]
The empty set of such \(k\) identifies \(\Delta\le1\), and otherwise its largest element is \(\Delta\). For \(k\ge3\),
\[
k\le N_k(T)\le k+k!S(\ell,k).
\]
When \(\ell<k\), equality holds throughout for every tree. When \(\ell\ge k\), equality in the upper bound holds precisely when suppressing unary vertices turns \(T\) into a rooted star with \(\ell\) leaves. Thus, for every \(k\ge3\), the unique reduced extremal tree at fixed \(\ell\ge k\) is the star. For \(k=2\), every rooted-tree shape with \(\ell\) leaves ties.

**A depth signal and collisions.** If there is exactly one three-child vertex and every other vertex has at most two children, and \(b\) is the number of two-child ancestors of the three-child vertex, then
\[
N_3(T)=3+6\cdot3^b.
\]
Every full-binary rooted tree (every internal vertex has two children) with \(\ell\) leaves has the entire sequence \(N_2=2^\ell\) and \(N_k=k\) for \(k\ge3\). Balanced and caterpillar full-binary shapes give distinct trees with this identical complete profile for every \(\ell\ge4\). At four leaves the complete set of possible three-fan counts is \(\{3,9,21,39\}\).

## Assumptions and scope
A rooted tree is finite, nonempty and unlabelled as a shape, but its individual vertices are distinguished when counting functions. The accessibility relation is the reflexive **transitive** ancestor order, not the immediate parent-edge relation. Each target fan carries the reflexive partial order \(0\le i\) for each top \(i\), and no comparisons between distinct tops. A bounded morphism is a function \(f\) such that (forth) \(uRv\implies f(u)R'f(v)\), and (back) if \(f(u)R'w\), there exists \(v\) with \(uRv\) and \(f(v)=w\). Both constant maps and onto maps count, without taking a quotient by automorphisms or permuting the labeled fan maxima. The result covers all \(k\ge2\) and all nonempty finite rooted trees, including a singleton and unary paths. Subdivisions and unary paths are meant only up to rooted isomorphism after suppressing vertices with exactly one child.

## Proof
**1. Leaves and unique extension.** If \(v\) is a leaf, its successor set in the ancestor frame is \(\{v\}\). Were \(f(v)=0\), the back condition would demand successors realizing all \(k\) maxima, impossible for \(k\ge2\); hence \(f(v)\) is a maximal point. If \(f(u)=i\) is maximal, forth forces every descendant of \(u\) to map to \(i\), so all descendant leaves share color \(i\). If \(f(u)=0\), back gives a descendant mapping to each maximal color; the descendants of any vertex mapping to a top include a leaf with the same color, so all \(k\) colors occur among the leaves below \(u\). Therefore each subtree has either exactly one leaf color or all \(k\), and those leaves determine \(f(u)\) uniquely.

Conversely, start with a leaf coloring whose support on every subtree has cardinality \(1\) or \(k\). Define \(f(u)=i\) in the first case and \(f(u)=0\) in the second. If \(uRv\), the leaf-color set below \(v\) is contained in that below \(u\). Thus, when \(f(u)\) is a maximal point, \(f(v)\) is the same point, and when \(f(u)=0\) any target point is above it: forth holds. At a zero-valued vertex every top is realized by a leaf descendant, and zero is realized by the vertex itself; at a top-valued vertex its only accessible target is that same top. Hence back holds. This proves the bijection.

**2. Recurrence.** Every permitted child-subtree coloring belongs to one of \(N_k(T_i)\) possibilities. The root may be monochromatic (exactly \(k\) choices), or contain all colors. Full-color root assignments with some full-color child are counted by \(\prod_iN_k(T_i)-k^d\). If all children are monochromatic, exactly \(k!S(d,k)\) colorings of their \(d\) roots collectively use all \(k\) colors. These cases are disjoint and exhaustive; this gives the recurrence. At a leaf there are \(k\) choices. For \(k=2\), every nonempty subset of two colors has cardinality either one or two, so **all** \(2^\ell\) leaf assignments extend.

**3. Degree threshold.** If every vertex has fewer than \(k\) children, induction upward shows every permitted subtree coloring is monochromatic: with fewer than \(k\) monochromatic child subtrees one cannot realize all \(k\) colors. Thus \(N_k(T)=k\). Conversely, at any vertex with at least \(k\) children, choose \(k\) child subtrees and color their leaves uniformly in all \(k\) distinct colors. Color every other leaf uniformly with the first color. The unique color-set support is then either a singleton or the full palette throughout the tree, yielding a nonconstant morphism in addition to the \(k\) constant morphisms. This proves the threshold equivalence.

**4. Sharp upper bound and equality.** For any permitted coloring, the root has either one color or all \(k\) colors. There are \(k\) monochromatic leaf assignments and \(k!S(\ell,k)\) onto leaf assignments, yielding the upper bound. For a rooted star (and for unary subdivisions of its arms or a unary stem) every global onto coloring is permitted because every proper descendant subtree is monochromatic; hence equality.

Assume \(k\ge3\), \(\ell\ge k\), and the reduced tree is not a star. There is a vertex with at least two children and a proper child subtree containing \(s\) leaves, where \(2\le s\le\ell-1\). Put \(t=\ell-s\ge1\), and choose an integer \(h=\max(2,k-t)\). Since \(\ell\ge k\), \(s\ge2\), and \(k\ge3\), we have \(2\le h\le\min(s,k-1)\), and \(1\le k-h\le t\). Color the \(s\) leaves inside this child subtree so they realize exactly \(h\) colors, and color the \(t\) exterior leaves so they realize the other \(k-h\) colors. This globally onto coloring fails the local condition at the chosen child subtree (its support is neither \(1\) nor \(k\)), so the upper bound is strict. When \(\ell<k\), no onto coloring exists and all morphisms are constant, proving the stated exception.

**5. One ternary vertex.** In any subtree with all child degrees at most two, the threshold in step 3 gives \(N_3=3\). At the sole three-child vertex, all three child values are \(3\), so the recurrence yields \(N_3=3+6=9\). At an ancestor with one child, the recurrence leaves \(N_3\) unchanged; at an ancestor with two children, the other child subtree has count \(3\), so the recurrence gives \(N_3=3+3(N_3(\mathrm{marked\ child})-3)\). Every such two-child ancestor therefore multiplies the excess over \(3\) by \(3\). The displayed formula follows. A full-binary tree has \(\Delta=2\); step 3 gives all \(N_k=k\) for \(k\ge3\), while step 2 gives \(N_2=2^\ell\). Two distinct full-binary shapes occur at every \(\ell\ge4\). With four leaves, reduced trees comprise the full-binary shapes, a unique ternary vertex either below zero or one binary ancestor, or a four-child star, yielding respectively \(3,9,21,3+3!S(4,3)=39\).

## Verification
Run `python verify.py` with Python 3 and no nonstandard packages. The checker independently enumerates **every vertex map** into fans with \(k=2,3,4\) on all increasingly labelled rooted trees of at most six vertices, tests forth and back directly via descendant sets, and compares the results with a separate enumeration of admissible leaf assignments and the recurrence. Every rooted shape of at most six vertices has an increasingly labelled representative. It also verifies the degree threshold, upper-bound equality criterion, unique-trivalent formula, and a pair of four-leaf full-binary collisions. Recorded output is in `verification_output.json`.

The finite checker confirms only finite cases; the universal statements follow from the proofs above.

## Relationship to prior work
Bounded morphisms and their forth/back conditions are classical modal-model-theoretic tools (Blackburn, de Rijke and Venema; Goranko and Otto). Endriss studies p-morphisms in ordered-tree semantics, including extra bidirectional frame conditions for that enriched language. None of those notions or definitions is claimed as new. The contribution is the **exact fan-target leaf-color normal form**, the unrestricted profile and degree-threshold laws, and the sharp equality classification and collision families. Mapping into a two-level fan with incomparable maxima is distinct from mapping into chains, three-level fork/crown frames, or graph-incidence fans. A complete absence of implicit prior derivations cannot be established by bibliographic search alone.

## Limitations
The counts are for reflexive transitive ancestor frames and do not transfer unchanged to irreflexive parent-edge accessibility or to globally surjective-only maps. The upper extremizer is unique only after suppression of unary vertices, and only for \(k\ge3\) with at least \(k\) leaves. The entire numerical fan profile is generally incomplete as a rooted-tree isomorphism invariant; the full-binary collision family proves this. No independent scientific audit has been performed.

## References
- P. Blackburn, M. de Rijke and Y. Venema, *Modal Logic*, Cambridge University Press, 2001, especially the introduction of bounded morphisms in Chapter 2; DOI `10.1017/CBO9781107050884`.
- U. Endriss, *Modal Logics of Ordered Trees*, revised thesis, March 2003, Section 3.5 (`https://staff.science.uva.nl/u.endriss/pubs/files/otl.pdf`).
- V. Goranko and M. Otto, *Model Theory of Modal Logic*, *Handbook of Modal Logic* (2007), Section 2.2 (`https://www.mathematik.tu-darmstadt.de/~otto/papers/Chapter5_02_05_06.pdf`), DOI `10.1016/S1570-2464(07)80008-5`.
- A. V. Figallo, I. Pascual and A. Ziliani, *Monadic distributive lattices and monadic augmented Kripke frames*, preprint first posted 27 March 2012, arXiv `1203.6059`; cited only as related finite-frame morphism literature, not as a source of the counting statements.
