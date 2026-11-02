# Thirteen rank-three theories of complete rooted trees under ancestry

## Finding
For integers \(b\ge2\) and \(h\ge0\), let \(T(b,h)\) have as vertices all finite words of length at most \(h\) over an alphabet of size \(b\). Its **only** nonlogical relation is strict ancestry \(u\prec v\), meaning that \(u\) is a proper prefix of \(v\). There is no designated root, successor relation, child relation, depth predicate, or order on siblings. Write \(\equiv_3\) for agreement on all first-order sentences of quantifier rank at most three in this signature, with equality.

**Theorem.** For any \(b,c\ge2\) and \(h,k\ge0\),
\[
T(b,h)\equiv_3T(c,k)
\iff
\bigl(h=k=0\bigr)\ \lor\
\bigl(h,k\ge1\ \land\ \min(h,6)=\min(k,6)\ \land\ (b=2\iff c=2)\bigr).
\]
Thus this two-parameter family has exactly **thirteen** rank-three theories: one at height zero, six binary-branching classes with smallest heights \(1,2,3,4,5,6\), and six classes with at least three children per internal node, again represented by heights \(1,2,3,4,5,6\). The depth cutoff \(6\) and the branching cutoff \(3\) are both sharp.

## Assumptions and scope
All trees are nonempty and finite, with uniform branching \(b\ge2\) at every non-leaf and leaves exactly at depth \(h\). The height counts **edges** from the empty word. The signature is precisely \(\{\prec\}\), together with logical equality. The theorem is not about unordered graph adjacency, a named root, the immediate-child relation, or arbitrary nonuniform trees.

For a node \(x\), put \(d(x)=|x|\) and \(t(x)=h-|x|\). We use the standard Ehrenfeucht–Fraïssé characterization: two structures agree to rank \(r\) exactly when Duplicator wins the \(r\)-move game, allowing repeated picks. For a fixed ordered tuple, its remaining-round type is obtained from the set of types of all possible one-point extensions; quantifier-free types consist of equality and strict-ancestry comparisons.

## Proof
**1. Exact one-move extension table for a selected pair.** Write \(I(x,y)\) when \(x,y\) are incomparable. For two selected vertices \(x,y\), the rank-one extension type is their atomic relation, together with the set of atomic triples \((x,y,z)\) realized by some \(z\). The following cases exhaust all possibilities; the occurrence of each position class follows immediately by tracing proper prefixes.

When \(x=y\), a third vertex can be equal, a strict ancestor if \(d(x)\ge1\), a strict descendant if \(t(x)\ge1\), or incomparable if \(d(x)\ge1\). Incomparability is available because \(b\ge2\).

When \(x\prec y\), write \(a=d(x)\), \(g=d(y)-d(x)\ge1\), and \(s=h-d(y)\). Besides the always-realizable cases \(z=x\), \(z=y\), and \(x\prec z\) with \(I(z,y)\), the third vertex can be a strict ancestor of both exactly if \(a\ge1\); incomparable to both exactly if \(a\ge1\); strictly between \(x\) and \(y\) exactly if \(g\ge2\); or a strict descendant of both exactly if \(s\ge1\). The case \(y\prec x\) is the same after interchanging their labels. These are all possible atomic triple types.

When \(I(x,y)\), let their longest common prefix have depth \(\ell\), and write \(u=d(x)-\ell\ge1\), \(v=d(y)-\ell\ge1\), \(s_x=h-d(x)\), and \(s_y=h-d(y)\). The possibilities \(z=x\), \(z=y\), and \(z\prec x,z\prec y\) always occur. A proper descendant of \(x\) (respectively \(y\)), incomparable with the other vertex, exists exactly when \(s_x\ge1\) (respectively \(s_y\ge1\)). An ancestor of \(x\) incomparable with \(y\) exists exactly when \(u\ge2\); symmetrically this happens for \(y\) exactly when \(v\ge2\). Finally, a vertex incomparable with **both** exists exactly when
\[
b\ge3\ \lor\ \ell\ge1\ \lor\ u\ge2\ \lor\ v\ge2.
\]
Indeed, such a vertex may branch off above their least common ancestor, from a third child of that ancestor, or beside a proper segment toward one of the selected vertices. Only the pair of distinct children of the root in a binary tree fails all four alternatives. No other triple order diagrams can occur because the predecessor set of every node is linearly ordered.

**2. Uniform cap for the two remaining moves.** Fix the first picked node \(x\), and let \(d=d(x)\) and \(t=h-d\). Its remaining-two-round type is the set of all pair rank-one types above, as \(y\) varies. We claim that this type depends *only* on
\[
\bigl(\min(b,3),\min(d,3),\min(t,3)\bigr).
\]
For ancestors \(y\) of \(x\), the possible gaps are integers \(g\in[1,d]\); the preceding table tests only whether \(g\ge2\), \(d-g\ge1\), and \(t\ge1\). For descendants, use \(g\in[1,t]\) and only the tests \(d\ge1\), \(g\ge2\), and \(t-g\ge1\). All feasible Boolean triples are unchanged once \(d\) and \(t\) are capped at three.

For incomparable \(y\), choose its common-prefix length \(\ell=d-u\) with \(1\le u\le d\), and choose \(1\le v\le u+t\). The table tests \(u\ge2\), \(v\ge2\), \(t\ge1\), \(u+t-v\ge1\), and the final displayed disjunction. The last disjunction is automatically true for \(u\ge2\) or \(v\ge2\), and for \(u=v=1\) reduces to \(b\ge3\) or \(d\ge2\). For fixed \(u\), the possible pairs \((v\ge2,\ u+t-v\ge1)\) depend only on \(\min(u+t,3)\). All \(u\ge3\) have the same relevant Boolean effect as \(u=3\), since the only exceptional disjunction occurs at \(u=v=1\). Hence the attainable incomparable-pair types likewise depend only on the three capped parameters. This establishes the claim for **all finite heights**, without relying on a finite sample.

**3. Upper bound on root types.** The three-round type of the whole tree is precisely the set of pointed remaining-two-round types from all choices of \(x\). At height \(h\) these types correspond to the capped pairs
\[
\left\{\bigl(\min(d,3),\min(h-d,3)\bigr):0\le d\le h\right\}.
\]
For every \(h\ge6\), this set is constant, consisting of
\[
(0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0).
\]
The additional branching cap is binary versus at least ternary. Thus trees in the same two saturated parameter classes are equivalent through rank three. Equal smaller heights with the same branching class have identical capped type sets as well.

**4. Sharpness: height.** For \(j\in\{0,1,2,3\}\), let \(U_j(x)\) say that \(x\) has at least \(j\) strict ancestors and \(D_j(x)\) say that it has at least \(j\) strict descendants along one chain. For \(j=0\) these predicates are true; \(U_1,U_2\) respectively have formulas \(\exists y(y\prec x)\) and \(\exists y\exists z(z\prec y\prec x)\); and
\[
U_3(x):=\exists y\bigl(y\prec x\land
 (\exists z\ z\prec y)\land(\exists z\ y\prec z\prec x)\bigr).
\]
Define the \(D_j\) dually. All \(U_j,D_j\) have quantifier rank at most two with \(x\) free. Therefore \(\exists x(U_a(x)\land D_b(x))\) has rank at most three and holds in \(T(b,h)\) if and only if \(h\ge a+b\). Taking \((a,b)=(0,1),(0,2),(1,2),(2,2),(3,2),(3,3)\) produces every sharp height cut \(h\ge1,2,3,4,5,6\). No two different truncated heights are equivalent.

**5. Sharpness: branching.** Let \(C(z,x)\) abbreviate equality or comparability by \(\prec\). The rank-three sentence
\[
\exists x\exists y\left(I(x,y)\land
 \forall z\,[C(z,x)\lor C(z,y)]\right)
\]
holds at every positive height exactly when \(b=2\). For a binary tree select its two children of the root; every vertex is comparable with at least one. With at least three children at the root, two incomparable vertices cannot cover every root branch, so a third incomparable vertex always exists. At height zero every branching parameter gives the same one-vertex structure. These formulas complete the converse.

## Verification
`tree3_symbolic.py` independently encodes all four pair-order cases as finite Boolean signatures and enumerates rank-three extension profiles. `tree3_explore.py` instead constructs canonical word representatives for every orbit of a third vertex under the pair stabilizer and computes the atomic diagrams directly. The two implementations agreed on **7,098** pair cases, for branching values \(2,3,4\) and heights through \(11\). The symbolic implementation also checked the 32 capped pointed profiles and all thirteen root types through height \(44\) for branching values \(2,3,4,5\).

A separate C++17 implementation, `tree3_direct.cpp`, enumerates **all actual vertices and all ordered triples**, with equality and repeated vertices, for binary trees through height six, ternary trees through height four, and quaternary trees through height three. It agrees with the symbolic classification in every case. `reproduce.sh` reruns both checks; `verification_output.txt` records the successful output. These finite tests corroborate, but do not replace, the general Boolean-case proof in Steps 1–3.

## Relationship to prior work
Backofen, Rogers, and Vijay-Shanker develop first-order axiomatizations for broad classes of finite trees, using a richer signature with parent, domination, and sibling-order relations. Their class-level axiomatization and finite-model reduction do not state an exact three-round classification for complete rooted trees in the ancestry-only reduct.

Berkholz, Krebs, and Verbitsky study quantifier depth and alternation hierarchy over finite trees and graphs, including constructions on colored and uncolored trees. Their theorem concerns finite-variable/alternation bounds rather than the specific two-parameter, depth-three ancestry-only equivalence classes proved here. Existing orbit-profile results for infinite homogeneous meet-trees and branching structures likewise address different structures and invariants. The explicit implication comparisons and historical limitations are recorded in `AUDIT.json` and `REVIEW.md`.

## Limitations
The statement holds only for uniform complete rooted trees with \(b\ge2\), at quantifier rank three, and in the strict-ancestry-only language. Adding root, successor, or sibling-order symbols can change the classification. It does not determine higher-rank types or the unrestricted class of rooted trees. Exhaustive historical priority and independent mathematical audit have not been completed.

## References
1. R. Backofen, J. Rogers, K. Vijay-Shanker, *A First-Order Axiomatization of the Theory of Finite Trees*, Journal of Logic, Language and Information (1995); accessible author PDF: https://www.eecis.udel.edu/~vijay/papers/jolli95.pdf.
2. C. Berkholz, A. Krebs, O. Verbitsky, *Bounds for the quantifier depth in finite-variable logics: Alternation hierarchy*, arXiv:1212.2747, first posted 2012-12-12, https://arxiv.org/abs/1212.2747.
3. Classical Ehrenfeucht–Fraïssé game characterization of bounded-quantifier-rank first-order equivalence.
