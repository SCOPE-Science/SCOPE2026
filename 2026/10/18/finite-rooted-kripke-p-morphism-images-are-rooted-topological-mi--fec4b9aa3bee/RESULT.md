# Finite rooted Kripke p-morphism images are rooted topological minors

## Finding
For all finite nonempty rooted trees \(T\) and \(U\), give their vertices the reflexive ancestor relations. There exists a surjective bounded morphism (also called a simple \(p\)-morphism) of Kripke frames \(T\to U\) **if and only if** there is an injective map \(e:V(U)\to V(T)\) preserving *strict ancestry* and *least common ancestors*:
\[
x<_{U}y\Longrightarrow e(x)<_{T}e(y),\qquad e(x\wedge_U y)=e(x)\wedge_Te(y).
\]
The embedding is **not** required to send the root of \(U\) to the root of \(T\), or a leaf to a leaf. Equivalently, a subdivision of \(U\) appears as a rooted, ancestor-oriented subtree of \(T\), with each branch split occurring at the image of its original branching vertex. Thus the p-morphic-image quasi-order on finite rooted trees agrees exactly with the (root-relaxed, leaf-unrestricted) topological-minor quasi-order. Existence is decidable by a polynomial-time dynamic program using bipartite matching.

## Assumptions and scope
A finite rooted tree is a nonempty finite connected acyclic graph with a distinguished root and unordered child sets. Write \(x\leq_Ty\) if \(x\) is an ancestor of \(y\), including equality, and \(T_x=\{z:x\leq_Tz\}\). A bounded morphism \(f:T\to U\) is a function such that for all \(x\in T\),
\[
f(T_x)=U_{f(x)}.\tag{1}
\]
Condition (1) is exactly the conjunction of the usual forward and back conditions for the reflexive transitive accessibility relations. A surjective map necessarily sends the source root to the target root: (1) at the source root identifies its image with the target cone, which can equal the entire target only at its root. No vertex labels, propositional valuations or additional accessibility relations are part of the theorem.

For source vertex \(s\) and target vertex \(t\), define \(P(s,t)\) as the existence of a bounded morphism \(T_s\to U_t\) sending \(s\) to \(t\). Define \(E(s,t)\) as the existence of the displayed embedding of \(U_t\) somewhere in \(T_s\). Both are nonempty rooted-subtree problems, with child sets \(C_T(s)\) and \(C_U(t)\).

## Proof
**Step 1: a complete recursion for bounded morphisms.** For every \(s,t\), \(P(s,t)\) is true precisely when at least one of these conditions holds:

(A) Some child \(c\in C_T(s)\) has \(P(c,t)\).

(B) There exists an injection \(\iota:C_U(t)\hookrightarrow C_T(s)\) such that \(P(\iota(d),d)\) holds for every \(d\in C_U(t)\). For a leaf \(t\), the empty injection makes (B) true.

Indeed, given a bounded morphism \(f\) with \(f(s)=t\), if any source child \(c\) maps to \(t\), then (1) on the child cone gives (A). Otherwise, for each child \(d\) of \(t\), (1) at \(s\) provides a descendant \(y\) of \(s\) with \(f(y)=d\). Let \(c\) be the first child of \(s\) on the path to \(y\). Forward preservation yields \(t\leq_U f(c)\leq_U d\); since \(d\) covers \(t\), and by hypothesis \(f(c)\ne t\), we have \(f(c)=d\). Distinct children \(d\) give distinct source children \(c\). The restrictions to these source child cones satisfy \(P(c,d)\), proving (B).

Conversely, given (A), use the witness on \(T_c\), send \(s\) to \(t\), and map every *other* source-child subtree constantly to an arbitrary leaf \(\ell\) of \(U_t\). A constant map to \(\ell\) satisfies (1) since \(U_\ell=\{\ell\}\), and (1) at \(s\) follows from the distinguished child map covering all of \(U_t\). Given (B), use the witnesses \(T_{\iota(d)}\to U_d\), send \(s\) to \(t\), and map unassigned source-child subtrees constantly to a target leaf. The images of the assigned subtrees together with \(t\) exhaust \(U_t\), so (1) holds at \(s\) and at every descendant. Finiteness ensures a leaf always exists.

**Step 2: the identical recursion for embeddings.** Suppose \(E(s,t)\). If the embedded root \(e(t)\) is strictly below \(s\), the whole embedding lies in a unique child cone \(T_c\) and gives (A) with \(E\) instead of \(P\). If \(e(t)=s\), then the least-common-ancestor condition places the embedded roots of distinct child subtrees of \(U_t\) in different child cones of \(s\); restrictions give (B) with \(E\). Conversely, (A) gives an embedding into one child cone; and (B) combines embeddings in disjoint child cones with the assignment \(e(t)=s\). Their intercone least common ancestors are exactly \(s\), so the combined map preserves all least common ancestors and strict ancestry.

**Step 3: simultaneous induction.** In the two recursions, each \((c,t)\) or \((c,d)\) has strictly smaller source subtree than \((s,t)\). For a source leaf, both predicates are true exactly when \(t\) is a leaf. Induction on \(|T_s|\) therefore gives \(P(s,t)\iff E(s,t)\) for every pair of vertices. At the roots this is the stated equivalence, including surjectivity because (1) at the root yields the whole target.

**Algorithm.** Process source nodes from leaves to root; for each source node process all target nodes. Let \(Q(s,t)\) be true when a bipartite matching saturates \(C_U(t)\), using an edge \((d,c)\) exactly when \(Q(c,d)\) is true. Set \(P(s,t)\) to \(Q(s,t)\) or to the disjunction of \(P(c,t)\) over source children \(c\). All dependencies concern smaller source subtrees. A maximum bipartite matching can be found in polynomial time at each of at most \(|T|\,|U|\) states. Thus the decision problem is polynomial-time (even without a bound on branching or height). Classical Kruskal well-quasi-ordering for finite rooted trees then also applies to the p-morphic-image quasi-order in this class.

## Verification
The self-contained standard-library file `check_trees.py` represents unordered rooted trees recursively. It implements the p-morphism recursion and independently implements the injective least-common-ancestor embedding condition, and compares their truth values for all \(5{,}016\) ordered pairs of isomorphism types with source order at most \(7\) and target order no larger than source order. It separately enumerates all possible root-preserving functions to test the forward/back conditions directly for \(196\) pairs with source order at most \(5\). The observed results were `DP_VS_EMBED_OK 5016` and `BRUTE_VS_DP_OK 196`. These finite comparisons are regression tests, not a substitute for the proof.

A sharp elementary consequence illustrates the exact branching obstruction: a finite rooted binary tree cannot admit a bounded-morphism surjection onto the four-vertex star with three children of its root, regardless of depth. Such a target cannot embed because it needs three diverging source child cones from a single source vertex.

## Relationship to prior work
Endriss (2003, §3.5–3.6, Lemma 3.32) develops p-morphisms for ordered-tree modal frames and proves a tree-preservation statement for **surjective bidirectional morphisms of an irreflexive immediate-successor structure**; this does not give the present if-and-only-if existence criterion for the **single reflexive ancestor** relation on arbitrary finite unordered trees. Bodirsky–Piguet (2010) study topological embeddings of **rooted binary plane trees** with a **leaf-preservation constraint**, and prove a Ramsey theorem; they do not identify these embeddings with finite Kripke bounded-morphism quotients. The 2015 article on first-order S4 discusses p-morphisms, including onto maps from the **infinite** binary tree; that infinite-tree phenomenon does not imply the finite criterion. Chopra–Pakhomov (2026, Def. 3.5) articulate least-common-ancestor-preserving tree embeddings and Kruskal's order, but do not characterize them as bounded-morphism images. The equivalence above explicitly removes leaf-preservation and root-to-root restrictions.

## Limitations
The result does not count distinct p-morphisms, classify the images of general preorders or graphs, handle infinite trees, or preserve extra modal relations or arbitrary propositional valuations. The matching algorithm decides existence, not the number of maps. The well-quasi-order consequence is inherited from the established Kruskal theorem rather than a new proof. Existing adjacent tree-embedding and modal-quotient results leave some residual bibliographic risk even after comparing the closest accessible primary sources.

## References
1. U. Endriss, *Modal Logics of Ordered Trees* (revised thesis, 2003), §§3.5–3.6, especially Definition 3.20 and Lemma 3.32, https://staff.science.uva.nl/u.endriss/pubs/files/otl.pdf .
2. M. Bodirsky and D. Piguet, *Finite trees are Ramsey under topological embeddings*, arXiv:1002.1557v1 (first posted 2010-02-08), https://arxiv.org/html/1002.1557v1 . The arXiv submission date is the verified historical literature date used in metadata, **not a date of this finding**.
3. *First order S4 and its measure-theoretic semantics*, *Annals of Pure and Applied Logic* 166 (2015), 187–218, DOI:10.1016/j.apal.2014.10.002 .
4. A. D. Chopra and F. Pakhomov, *Well-quasi-orders on finite trees and transfinite sequences*, arXiv:2602.09830v2 (2026), Defs. 3.2–3.5 and Thm. 3.7, https://arxiv.org/html/2602.09830v2 .
