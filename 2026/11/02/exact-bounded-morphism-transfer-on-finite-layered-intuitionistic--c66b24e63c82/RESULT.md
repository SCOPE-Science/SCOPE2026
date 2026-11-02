# Exact bounded-morphism transfer on finite layered intuitionistic frames

## Finding

For arbitrary integers \(h,k\ge 1\), let \(P=A_1\oplus\cdots\oplus A_h\) and \(Q=B_1\oplus\cdots\oplus B_k\) be finite ordinal sums of nonempty antichains. Set \(a_i=|A_i|\), \(b_j=|B_j|\), with every point distinctly labelled. Let \(N(P,Q)\) count **surjective bounded morphisms** of intuitionistic Kripke frames: functions \(f:P\to Q\) for which \(f(\uparrow_P x)=\uparrow_Q f(x)\) for every \(x\in P\).

Write \(s(a,b)=b!\left\{\begin{smallmatrix}a\\b\end{smallmatrix}\right\}\) for the number of surjections from an \(a\)-element labelled set onto a \(b\)-element labelled set, with \(s(a,b)=0\) when \(a<b\). The following \(k+1\)-state recurrence counts **all** such maps exactly, with no enumeration of individual functions.

Start with \(D_0(k)=1\), and \(D_0(j)=0\) for \(0\le j<k\). For \(r=0,\ldots,h-1\), process the next source layer from top to bottom, of size \(a=a_{h-r}\). From each state \(j\in\{0,\ldots,k\}\), add the following weighted contributions to \(D_{r+1}\):

* **Stay at \(j\):** weight \(1\), exactly when \(j<k\) and \(b_{j+1}=1\); otherwise no stay transition.
* **Advance from \(j\) to \(j-1\), for \(1\le j\le k\):** weight \(s(a,b_j)\), except when \(j<k\) and \(b_{j+1}=1\), in which case the weight is \(s(a,b_j)+s(a,b_j+1)\).

Then \(\boxed{N(P,Q)=D_h(0)}\). In each state, \(j\) is the number of bottom target layers not yet covered; the already-covered part is the complete upset \(B_{j+1}\cup\cdots\cup B_k\). Once the surjection numbers are available, the recurrence takes \(O(hk)\) integer-arithmetic operations and also decides existence by testing whether the final count is positive.

There is a sharp rigidity consequence. If **all** \(b_j\ge2\), then
\[
\boxed{N(P,Q)=\begin{cases}\prod_{i=1}^{k}s(a_i,b_i),&h=k,\\0,&h\ne k.\end{cases}}
\]
Thus each source layer must map surjectively onto the corresponding target layer; no source level may be merged or split. The threshold is sharp: for \(P\) with level sizes \((2,2,2)\), the targets with levels \((2,2)\), \((1,2)\), and \((2,1)\) respectively have \(0\), \(2\), and \(2\) surjective bounded morphisms. A single singleton target level permits height collapse that is impossible for a target whose levels all have at least two points.

## Assumptions and scope

The source and target are **finite nonempty posets**, each presented as an ordinal sum of nonempty antichains: \(x<y\) precisely when the level index of \(x\) is lower than the level index of \(y\). The partial orders are reflexive; distinct elements within the same level are incomparable. A bounded morphism satisfies both order preservation and the back condition; these are jointly equivalent to the principal-upset equality displayed above. We count functions between the fixed underlying labelled carriers, not maps up to isomorphism. A target singleton means a level of size exactly one, not a unique root in all cases. The proof and formula require no comparability of elements within a level.

## Proof

**1. A single source-level test.** For \(x\in A_i\), its principal upset is \(\{x\}\cup A_{i+1}\cup\cdots\cup A_h\). Put \(U_i=f(A_{i+1}\cup\cdots\cup A_h)\). Thus the bounded-morphism requirements at \(x\) are equivalent to
\[
U_i\cup\{f(x)\}=\uparrow_Q f(x).
\]
Equivalently, every element of \(A_i\) may map only to a point of \(E(U_i)=\{y\in Q:U_i\cup\{y\}=\uparrow_Q y\}\), and every assignment to these eligible points independently satisfies the local forth/back test. The complete collection of local tests is equivalent to the global bounded-morphism conditions.

**2. No partial non-singleton frontier survives.** In a bounded morphism, the image of any union of top source levels is upward closed: if \(y=f(x)\) and \(y\le z\), the back condition provides a preimage of \(z\) above \(x\), still in the chosen top source levels. Every nonempty upset \(U\subseteq Q\) has the form \(B_{t+1}\cup\cdots\cup B_k\cup S\), with nonempty \(S\subseteq B_t\). If \(S\) is a proper subset of \(B_t\), then \(|B_t|\ge2\). If \(|S|=1\), the only point eligible in \(E(U)\) is the already-used member of \(S\); if \(|S|\ge2\), no point is eligible. In either case no lower source layer can add the missing elements of \(B_t\). Consequently **every** top-source-level image that can extend to a surjective bounded morphism is a *complete* upper suffix \(B_{j+1}\cup\cdots\cup B_k\), including the empty suffix before any assignment.

**3. Exact eligible points at a completed suffix.** For \(U=\varnothing\), \(E(U)=B_k\). For \(U=B_{j+1}\cup\cdots\cup B_k\) with \(0\le j<k\), direct inspection of principal upsets gives
\[
E(U)=\begin{cases}B_j,&j\ge1,\ b_{j+1}\ge2,\\B_j\cup B_{j+1},&j\ge1,\ b_{j+1}=1,\\\varnothing,&j=0,\ b_1\ge2,\\B_1,&j=0,\ b_1=1.\end{cases}
\]
In the second case \(B_{j+1}\) is a singleton. A source layer can either retain the same completed suffix by mapping constantly to its bottom singleton (one possibility), or introduce **every** point of the next lower target level \(B_j\). In the latter case there are \(s(a,b_j)\) assignments when no old singleton is available. When the old frontier is a singleton, there are \(s(a,b_j)\) assignments using only \(B_j\) and \(s(a,b_j+1)\) assignments using \(B_j\) and that old singleton. There are no other viable transitions. This is exactly the stated recurrence. Induction from the top source level therefore counts each surjective bounded morphism once and only once, proving \(N(P,Q)=D_h(0)\).

**4. Rigidity of thick targets.** If every target level has size at least two, no stay transition and no optional-old-singleton choice exists. Beginning with \(j=k\), exactly one target level must therefore be covered by each source level. A successful path exists only when \(h=k\), and then its count is the product of independent surjection numbers \(s(a_i,b_i)\). For the sharp examples, substitute \(a=(2,2,2)\) and \(b=(2,2),(1,2),(2,1)\) into the same recurrence.

## Verification

The standalone \(\texttt{checker.py}\) contains an exact-integer Stirling-transfer implementation and a second, direct enumerator using the order-preservation and back clauses separately. The latter enumerates all functions between each pair of shapes, discards nonsurjections, and tests every ordered pair and successor witness. All **449** admissible pairs of source/target shapes with total source size at most six, total target size at most five, and at most three levels (with layer sizes at most three) agree exactly. A further sweep checks the all-thick product formula and the height-mismatch zero bound through four levels, with each level size ranging from two through four. The checker prints \(\texttt{ALL_CHECKS_OK}\). These finite tests corroborate, but do not substitute for, the preceding all-size proof.

## Relationship to prior work

Rzążewski and Stronkowski's *Tabular intermediate logics comparison* (first public version September 8, 2025, arXiv:2509.06841) defines the same bounded-morphism problem and establishes hardness for several restricted poset classes and a decision algorithm for tree sources. The present result counts **all** surjective bounded morphisms for ordinal sums of antichains, including non-tree sources (e.g. any source having at least two points in each of its first two levels). It is not an assertion that tabular logic inclusion and bounded-morphism existence coincide for every nonrooted input.

The published *Exact cardinality recurrence for mapping spaces between finite weak orders* (identifier \(\texttt{1cee64311a06}\)) counts ordinary order-preserving maps. These are a strictly larger class: they need not satisfy \(f(\uparrow x)=\uparrow f(x)\), need not be surjective, and their stated recurrence does not give the bounded-morphism counts. The related *Singleton-gap criterion for retracts and eventual images of finite weak orders* (identifier \(\texttt{4d39f7ca58cd}\)) concerns images of endomorphisms, not all surjections between separately specified frames. Only summaries of these two records were accessible during the comparison; no full-text noncoverage claim is made on their behalf.

## Limitations

This is a classification for finite **ordinal sums of antichains**, not arbitrary finite intuitionistic frames, and its counts use fixed labels; isomorphism-class counts are not asserted. The transfer uses exact integer arithmetic; its operation count is not a bit-complexity claim about very large output integers. The proof is self-contained, but a historically equivalent result in work on finite poset coverings, locally surjective maps, or modal bounded morphisms remains possible. The result does not independently establish a new general complexity bound for unrestricted bounded-morphism existence or unrestricted intermediate-logic containment. Independent validation has not been performed.

## References

1. Paweł Rzążewski and Michał Stronkowski, *Tabular intermediate logics comparison*, arXiv:2509.06841, first submitted September 8, 2025; https://arxiv.org/abs/2509.06841 .
2. *Exact cardinality recurrence for mapping spaces between finite weak orders*, published mathematical record \(\texttt{1cee64311a06}\); summary consulted, full text not retrieved.
3. *Singleton-gap criterion for retracts and eventual images of finite weak orders*, published mathematical record \(\texttt{4d39f7ca58cd}\); summary consulted, full text not retrieved.
