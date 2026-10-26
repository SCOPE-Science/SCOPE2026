# Exact bounded-morphism census and sharp branching threshold for rooted trees

## Finding

Write \(Q_m\), for an integer \(m\ge2\), for the reflexive three-level Kripke frame whose worlds are \(0,c_1,\ldots,c_m,1\), with \(0<c_i<1\), pairwise incomparable middle worlds, and reflexive reachability. Let \(T\) be any nonempty finite rooted tree regarded as the reflexive ancestor partial order. Every vertex and target world is distinguished; maps, not orbits, are counted. A bounded morphism is an order-preserving map \(f\) such that for every vertex \(v\) and target world \(q\ge f(v)\), some descendant \(w\ge v\) satisfies \(f(w)=q\).

For each vertex \(v\), write \(\operatorname{ch}(v)\) for its children and compute two nonnegative integers \(A_v,B_v\) from the leaves upwards. A leaf has \(A_v=B_v=0\); at an internal vertex, set

\[
B_v=\prod_{u\in\operatorname{ch}(v)}(1+B_u),
\]

\[
A_v=\prod_{u\in\operatorname{ch}(v)}(1+mB_u+A_u)
+\sum_{j=1}^{m}(-1)^j\binom mj
\prod_{u\in\operatorname{ch}(v)}(1+(m-j)B_u).
\]

The second displayed equation also applies to leaves (where each empty product is \(1\)), and returns \(0\). **The exact number of globally surjective bounded morphisms \(T\to Q_m\) is \(A_r\), with \(r\) the root.** The arrays are computable with \(O(m|T|)\) integer arithmetic operations; they are polynomial-time computable in the binary input and output bit sizes, using the immediate zero shortcut when \(m>|T|\).

Moreover, **such a morphism exists if and only if some vertex has at least \(m\) children that are themselves nonleaves**. Thus its source has at least \(2m+1\) vertices; equality is possible only for the two-edge-arm spider with exactly \(m\) arms, on which the count is exactly \(m!\).

For the complete rooted \(d\)-ary tree of height \(h\) (root-to-leaf edge distance), the count is positive exactly when \(d\ge m\) and \(h\ge2\). With \(A_0=B_0=0\), the recurrence specializes for \(h\ge1\) to

\[
 B_h=(1+B_{h-1})^d,
 \qquad
 A_h=(1+mB_{h-1}+A_{h-1})^d
 +\sum_{j=1}^{m}(-1)^j\binom mj(1+(m-j)B_{h-1})^d.
\]

The first positive value is
\[
 A_2=\sum_{j=0}^{m}(-1)^j\binom mj(m+1-j)^d
 =\sum_{s=m}^{d}\binom ds m!\left\{\begin{matrix}s\\m\end{matrix}\right\},
\]
where the braces denote Stirling numbers of the second kind. For every \(d\ge m\ge2\), the limiting source-volume entropy exists and is strictly positive and finite:
\[
0< L_{d,m}:=\lim_{h\to\infty}\frac{\log A_h}{d^h}<\infty.
\]
More explicitly,
\[
\frac{\log(m!)}{d^2}\le L_{d,m}\le\frac{d}{d-1}\log(m+2).
\]

## Assumptions and scope

The tree is finite, nonempty, unordered (children are distinguishable vertices but have no specified planar order), and its accessibility relation is the **reflexive transitive ancestor relation**, not just the parent edge relation. The target is the **reflexive** order described above. Each of the \(m\) middle worlds is individually labelled. Globally surjective means surjective onto all \(m+2\) target worlds. No claim concerns valuation-preserving model morphisms, inverse-back maps, or a target with several incomparable bottom or top points. The results hold for every \(m\ge2\), including trees of one vertex and trees having leaves at differing depths.

## Proof

**State decomposition.** For a rooted subtree \(T_v\), consider bounded morphisms on \(T_v\) with specified image of its root. Let \(A_v\) count those whose root goes to \(0\), and let \(B_v\) count those whose root goes to a fixed middle world \(c_i\); by symmetry \(B_v\) does not depend on \(i\). A root sent to the top world has exactly one possible morphism, the constant map. A root sent to \(0\) has to reach every target world in its descendant subtree by the bounded-morphism lifting condition, hence is automatically onto. At a leaf there is no way to lift from \(0\) to any \(c_i\), or from \(c_i\) to \(1\), giving the zero base cases.

**Middle state.** If \(v\) is internal and \(f(v)=c_i\), each child root can have image only \(c_i\) or \(1\). A child sent to \(1\) is forced to stay at \(1\); a child sent to \(c_i\) admits exactly \(B_u\) maps and already reaches \(1\) somewhere below it. Since there is at least one child, every choice of these alternatives automatically lifts \(c_i\to1\) from \(v\). Independent child choices yield the product defining \(B_v\).

**Bottom state.** For a root \(v\) sent to \(0\), each child root may be sent to \(0\) (\(A_u\) choices), any one of the \(m\) middle worlds (\(B_u\) choices each), or \(1\) (one choice). Every such selection is order-preserving and is locally bounded away from \(v\). The condition at \(v\) is that every middle colour \(c_i\) occur in its descendants (reaching \(1\) is then automatic). If a child root goes to \(0\), that child subtree already contains every colour. Thus the only invalid selections have no child root sent to \(0\) and omit at least one middle colour. Inclusion-exclusion on the omitted set of \(j\) colours counts these invalid selections and subtracts them, producing the displayed formula for \(A_v\). This proves the recursion and the global census inductively.

**Sharp branching obstruction.** Let a surjective map exist and pick a maximal member \(z\) of the nonempty downset \(f^{-1}(0)\). Every strict descendant of \(z\) maps to a middle world or to \(1\). The lifting property at \(z\) supplies, for each \(c_i\), a descendant with image \(c_i\). It must lie below an immediate child mapped to \(c_i\), and distinct \(c_i\)'s require distinct children. Each such child must itself reach \(1\), so it cannot be a leaf. Hence \(z\) has at least \(m\) nonleaf children.

Conversely, suppose a vertex \(z\) has distinct nonleaf children \(u_1,\ldots,u_m\). Send the entire root-to-\(z\) path to \(0\), each \(u_i\) to \(c_i\), and all other vertices to \(1\). Every \(u_i\) has a child, hence has a top-world descendant. Every zero-labelled ancestor sees every middle world and the top through \(z\). Monotonicity and lifting hold everywhere, giving an onto bounded morphism. The smallest realizing tree therefore contains \(z\), those \(m\) children, and a child of each: at least \(2m+1\) distinct vertices. Equality forces \(z\) to be the root with exactly those two-edge arms; then the middle labels are assigned bijectively to the \(m\) arms, giving \(m!\) maps.

**Regular trees and entropy.** Every internal vertex of a complete \(d\)-ary height-\(h\) tree has \(d\) isomorphic child subtrees, giving the scalar recurrences. The branching criterion gives precisely \(d\ge m\) and \(h\ge2\). At height \(2\), every child root is either a middle world with its leaf children forced top, or itself top. Inclusion-exclusion on middle labels yields the first expression for \(A_2\); choosing the \(s\) children mapped to middles and surjecting their labels gives the Stirling expression.

For \(h\ge2\), putting independently any bottom-root morphism of height \(h\) into each of the \(d\) child subtrees and mapping the new root to \(0\) yields a bottom-root morphism of height \(h+1\). Therefore \(A_{h+1}\ge A_h^d\). As \(A_2\ge m!>1\), the sequence \(d^{-h}\log A_h\) is nondecreasing and at least \(d^{-2}\log(m!)\). At most \((m+2)^{(d^{h+1}-1)/(d-1)}\) functions from the source vertex set to \(Q_m\) exist, bounding the same sequence by \(d\log(m+2)/(d-1)\). Monotone convergence proves the claimed positive finite limit; no closed elementary expression for it is asserted.

**Complexity.** Compute \(B_v\), then the \(m+1\) products occurring in \(A_v\), at each vertex in postorder. Summing child degrees over the tree gives \(|T|-1\). Binomial coefficients up to \(m\) can be precomputed; thus there are \(O(m|T|)\) integer multiplications/additions. If \(m>|T|\), no surjection exists and return zero without forming large arrays. Otherwise counts have \(O(|T|\log(m+2))\) bits, giving polynomial bit complexity by standard integer arithmetic.

## Verification

The independent program \(VERIFY.py\) evaluates the recursion and directly enumerates candidate functions for sampled parent-array rooted trees (all sufficiently small sizes), applying the monotonicity and lifting clauses to every vertex. It checks 1,928 tree/target configurations for agreement, and it checks regular-tree first-positive and branching cases. Run with \(\texttt{python VERIFY.py}\); the expected final line begins with \(\texttt{ALL_TESTS_PASS}\). Its brute-force tests are finite corroboration; the proof above establishes the unbounded statements.

## Relationship to prior work

Bounded morphisms (also called p-morphisms or interior maps in finite Alexandroff spaces) and their preservation properties are standard, as discussed by Bezhanishvili and Harding (2012), especially their Section 2, and by Endriss (2003), especially his discussion of frame morphisms in Section 3.5. The finite-tree semantics of the modal logics \(\mathrm{S4.Grz}\) and \(\mathrm{S4.Grz}_n\) is classical and is discussed in the 2012 article. These works are not claimed as new and do not state the particular two-state quotient recursion, the threshold in terms of nonleaf children, or the regular-tree entropy assertion established here.

General dynamic programming on trees and inclusion-exclusion are established methods; the contribution lies in the exact specialization to surjective Kripke bounded morphisms to the stated height-three target and the resulting complete branching characterization and census. Distinguish this from enumerating all continuous order maps (which omit the lifting requirement) or from enumerating bounded morphisms with Boolean-lattice source or weak-order source. In particular, the previously considered Boolean-to-three-level target census does not cover this source-tree family.

## Limitations

This is a self-review, not an independent audit. The entropy limit is established by bounding and monotonicity, not evaluated in closed form. The finite verifier checks only finite trees and small target values. Specialized or unindexed modal-logic literature could contain an equivalent recursion or branching criterion; searches are not a proof of global novelty. The 2003 ordered-tree work studies additional directional and sibling relations, so its morphism concept must not be silently conflated with the present reflexive ancestor-order maps. A publication on metric-space modal logics, although exact-dated in December 2014, supplies contextual S4 frame background rather than a direct quotient census.

## References

1. G. Bezhanishvili and J. Harding, *Modal Logics of Stone Spaces*, Order **29** (2012), 271–292, DOI: 10.1007/s11083-011-9224-2. Author-hosted paper: https://math.nmsu.edu/people/personal-pages/files/2010-Modal-logics-of-Stone-spaces.pdf.
2. U. Endriss, *Modal Logics of Ordered Trees*, PhD thesis, King's College London, revised edition March 2003, https://staff.science.uva.nl/u.endriss/pubs/files/otl.pdf.
3. G. Bezhanishvili, D. Gabelaia and J. Lucero-Bryan, *Modal Logics of Metric Spaces*, Review of Symbolic Logic **8** (2015), 178–191, first public journal online 2014-12-18, DOI: 10.1017/S1755020314000446.
