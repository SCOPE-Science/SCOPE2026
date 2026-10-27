# A linear-time formula for one-types over rooted-forest parameters in the random poset

## Finding
Let \(\mathcal R\) be the countable homogeneous universal partial order and let \(P\subset\mathcal R\) be a finite induced subposet whose strict Hasse diagram is a **rooted forest oriented away from its minimal roots**: every nonroot point has exactly one lower cover. The empty forest is permitted. Let \(t(P)\) count complete nonalgebraic one-types over the individually named elements of \(P\).

For each \(v\in P\), let \(C(v)\) be its set of immediate children and recursively define, from leaves upwards,
\[
 d_v=1+\prod_{c\in C(v)}d_c.
\]
If \(R\) is the set of roots, let \(D=\prod_{r\in R}d_r\), interpreting empty products as \(1\), and put \(n=|P|\). Then the exact number of complete nonalgebraic one-types is
\[
\boxed{t(P)=2D+\sum_{v\in P}d_v-2n-1.}
\]
This uses only one integer per subtree, and therefore takes \(O(n)\) exact-arithmetic operations after the forest has been supplied by its cover edges, with integers of \(O(n)\) bits and polynomial bit complexity.

For comparison, the formula yields \(t(P)=1+n(n+3)/2\) on a chain of \(n\) elements, \(t(P)=3\cdot2^{n-1}\) on a rooted star with \(n\ge1\) elements, and \(t(P)=2^{n+1}-1\) on an antichain of \(n\) elements (also valid for \(n=0\)). These examples are consequences, not separate novelty claims.

## Assumptions and scope
The language is the sole strict order symbol (or equivalently its non-strict version together with equality). The named parameters are distinct and fixed pointwise. A complete nonalgebraic one-type describes a new element \(x\notin P\); types realized by the already named parameters are excluded. Distinct valid ways of relating \(x\) to the named points are distinct complete types because the generic poset is ultrahomogeneous and has quantifier elimination. No assumption is made about the number of branches, components, or depth. A rooted forest here is an **ancestor-order forest**; the result does not cover arbitrary acyclic undirected cover graphs with mixed edge orientations.

## Proof
**Step 1: The finite-extension coding.** Given a possible new point \(x\), write \(L=\{p\in P:p<x\}\) and \(U=\{p\in P:x<p\}\). Transitivity requires \(L\) to be a downset, \(U\) to be an upset, and each \(l\in L\) to be strictly below each \(u\in U\). Conversely these three conditions (with \(L\cap U=\varnothing\)) make the original order together with the declared comparisons to \(x\) a partial order. Every such finite extension embeds into \(\mathcal R\) over \(P\) by the Fraïssé extension property. Any finite number of mutually incomparable new points with identical comparisons to \(P\) can be added simultaneously, proving every such type is nonalgebraic. Homogeneity gives the converse classification of complete types.

**Step 2: Count downsets.** A downset of the principal descendant subtree \(P_{\ge v}\) is either empty, or includes \(v\) and independently chooses a downset of each child subtree. Consequently its number is exactly \(d_v=1+\prod_{c\in C(v)}d_c\). Since different rooted components are incomparable, the total number of downsets of \(P\) is \(D=\prod_{r\in R}d_r\).

**Step 3: Fix the nonempty upper set.** Every nonempty upset \(U\) is uniquely the upward closure of its nonempty antichain \(A=\min U\). The condition that every point of \(L\) lie strictly below every point of \(U\) is equivalent to \(L\) being a downset inside the common strict ancestor set
\[
 B(A)=\bigcap_{a\in A}\{v\in P:v<a\}.
\]
In an ancestor-order forest, \(B(A)\) is a (possibly empty) initial chain, so exactly \(1+|B(A)|\) downsets \(L\) are available. Therefore the total contribution of all nonempty upper sets equals
\[
\sum_{\varnothing\ne A\text{ antichain}}(1+|B(A)|)
=(D-1)+\sum_{v\in P}N_v,
\]
where \(N_v\) is the number of nonempty antichains contained strictly above \(v\). Indeed, the second sum counts each pair \((v,A)\) with \(v\) a strict common ancestor of all points of \(A\).

**Step 4: Count strict-descendant antichains.** The strict descendants of \(v\) form the disjoint union of child subtrees. Their antichains (including the empty one) are enumerated by \(\prod_{c\in C(v)}d_c=d_v-1\). Excluding the empty antichain gives \(N_v=d_v-2\). The contribution from \(U=\varnothing\) is precisely \(D\), because \(L\) may be any downset of \(P\). Thus
\[
 t(P)=D+(D-1)+\sum_{v\in P}(d_v-2)
=2D+\sum_{v\in P}d_v-2n-1.
\]
All equalities remain valid for the empty forest: \(D=1\), the vertex sum is \(0\), and \(t(\varnothing)=1\).

## Verification
The included script `forest_type_check.py` independently counts all ternary relation profiles by constructing the complete \((n+1)\)-point order relation and explicitly testing transitivity, without using the ideal/filter formula. It compares this direct count with the subtree recurrence on every recursive-parent representation with \(0\le n\le6\), totaling \(874\) forests, and checks \(24\) independently evaluated chain, star and antichain formulas. All tests pass, as recorded in `verification_output.txt`. The all-size theorem rests on the proof above, not these bounded tests.

## Relationship to prior work
Fraïssé theory supplies the generic universal homogeneous partial order, and the ideal/filter description of one-point extensions is classical. Pretzel (1980) studies possible insertion positions for finite posets, particularly a height-two setting; his publicly accessible abstract does not state the rooted-forest count and the full article could not be inspected. A published counting result for one-types over the random poset gives the general ideal/filter encoding and \(\#\mathrm P\)-completeness on unrestricted finite parameters, but its accessible indexed summary does not provide this particular constant-state all-rooted-forest formula. Earlier finite-parameter calculations also cover chains, stars and antichains separately. The new content here is the **simultaneous exact all-forest formula and one-number-per-subtree computation**, not the general type encoding or these previously known special cases. An exhaustive priority claim is not made.

## Limitations
The forest must be oriented in the ancestor direction. This argument does not yield the same formula for arbitrary finite posets or general orientations of cover trees. Arithmetic-operation complexity is not a uniform bit-operation bound. A relevant older insertion-poset article was inspected only at the abstract level; full-text novelty comparison remains a residual risk. The accessible published random-poset counting record was read as an indexed abstract, not as an entire manuscript. Independent validation has not been performed.

## References
1. A. S. Kechris, V. G. Pestov, and S. Todorcevic, *Fraïssé Limits, Ramsey Theory, and Topological Dynamics of Automorphism Groups*, arXiv:math/0305241v1, first posted 2003-05-16.
2. J. Hubička, *Combinatorial Properties of Finite Models*, arXiv:1009.0566v1, posted 2010-09-03, in particular Chapter 3 on the generic partial order.
3. O. Pretzel, *A construction for partially ordered sets*, Discrete Mathematics 32 (1980), 59–68, DOI: 10.1016/0012-365X(80)90100-4.
4. *Finite-parameter 1-type counting in the random poset is #P-complete*, published mathematical result, 2026. Indexed abstract consulted for the general type characterization and hardness assertion.
