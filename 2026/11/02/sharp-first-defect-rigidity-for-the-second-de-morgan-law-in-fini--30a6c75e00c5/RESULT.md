# Sharp first-defect rigidity for the second De Morgan law in finite Heyting algebras

## Finding

Let \(H\) be a finite nontrivial Heyting algebra, and let \(\neg a=a\to\bot\). Define two defect counts:
\[
 u(H)=\bigl|\{a\in H:\neg a\vee\neg\neg a\ne\top\}\bigr|,
 \qquad
 b(H)=\bigl|\{(a,c)\in H^2:\neg(a\wedge c)\ne\neg a\vee\neg c\}\bigr|.
\]
The pairs in \(b(H)\) are **ordered**, and elements are sampled uniformly when probabilities are mentioned.

**Theorem.** For every such \(H\),
\[
 b(H)\ge u(H).
\]
Equality holds if and only if either both counts are zero, or \(H\cong J(A_2\oplus Q)\), where \(A_2\) is a two-point antichain and \(Q\) is an arbitrary nonempty finite poset. In the second case,
\[
 b(H)=u(H)=2,\qquad |H|=3+|J(Q)|.
\]
Here \(J(P)\) denotes the Heyting algebra of downsets of \(P\), and \(\oplus\) means ordinal sum: every point of the first poset is below every point of the second.

Consequently, if \(H\) has \(h\) elements and fails the second De Morgan law, then \(h\ge5\) and its two-variable degree of satisfaction satisfies the **sharp fixed-cardinality bound**
\[
 \frac{\bigl|\{(a,c)\in H^2:\neg(a\wedge c)=\neg a\vee\neg c\}\bigr|}{h^2}
 \ \le\ 1-\frac{2}{h^2}.
\]
Equality holds exactly for \(J(A_2\oplus Q)\) with \(Q\ne\varnothing\). Every integer \(h\ge5\) admits an equality algebra: choose \(Q\) as a chain on \(h-4\) points.

A related exact count gives the entire higher-minimum ordinal-sum family. For \(k\ge2\) and nonempty finite \(Q\),
\[
 \left|J(A_k\oplus Q)\right|=2^k-1+|J(Q)|,
 \qquad
 b\bigl(J(A_k\oplus Q)\bigr)=3^k-2^{k+1}+1.
\]
Thus, in this natural class, the number of binary failures depends only on the number of incomparable minimal points, while the satisfaction probability also depends on the number of downsets of \(Q\).

## Assumptions and scope

All posets, Heyting algebras, and the index sets used below are finite. The algebra is nontrivial. For \(P\), a *downset* \(A\) satisfies \(x\le y\in A\implies x\in A\); \(\downarrow p=\{x:x\le p\}\). Its set of minimal points is \(M=\operatorname{Min}(P)\). Every finite Heyting algebra is represented as \(J(P)\) for its poset of join-irreducible elements. In this representation meet and join are set intersection and union, respectively. The standard first De Morgan law is not the equation under investigation.

We compare the unary weak-excluded-middle defect \(u(H)\) with the binary *second* De Morgan defect \(b(H)\). Their universal zero-defect conditions are classically equivalent; the result concerns their nonzero **numbers of violating assignments** and the full equality cases. No statement about infinite algebras, nonuniform sampling, or a fixed number of join-irreducibles is asserted.

## Proof

**1. Pseudocomplements and a local witness.** For a downset \(A\subseteq P\), the pseudocomplement is
\[
 \neg A=\{p\in P:\downarrow p\cap A=\varnothing\}.
\]
This is a downset; it is disjoint from \(A\), and every downset disjoint from \(A\) is contained in it. It follows that the second De Morgan equation fails for downsets \(A,B\) exactly when some \(p\in P\) has
\[
 \downarrow p\cap A\ne\varnothing,
 \qquad \downarrow p\cap B\ne\varnothing,
 \qquad \downarrow p\cap A\cap B=\varnothing. \tag{1}
\]
Indeed, the first two requirements say \(p\notin\neg A\cup\neg B\), and the third says \(p\in\neg(A\cap B)\). Since \(A,B\) are downsets, (1) yields **distinct minimal points** \(a,b\in M\), respectively belonging to \(A\) and \(B\), with \(a,b\le p\). Conversely, any two distinct minimal points with a common upper bound \(p\) give the two failing ordered pairs \((\{a\},\{b\})\) and \((\{b\},\{a\})\). Hence a nonzero binary defect is at least two. There can be no such failure when every principal downset has only one minimal point.

**2. An injection from unary to binary failures.** In every Heyting algebra,
\(a\wedge\neg a=\bot\). If \(a\) violates weak excluded middle, then
\[
 \neg(a\wedge\neg a)=\top\ne\neg a\vee\neg\neg a.
\]
Therefore \(a\mapsto(a,\neg a)\) injects the set counted by \(u(H)\) into the ordered-pair set counted by \(b(H)\). This proves \(b(H)\ge u(H)\). Moreover, if a unary-bad first coordinate has two distinct binary-bad partners, the inequality is strict: only one of these partners can equal its pseudocomplement.

**3. Rigidity when the two counts agree.** Suppose \(b(H)>0\), fix two distinct minimal points \(a,b\le p\), and assume \(b(H)=u(H)\). The singleton downsets \(\{a\},\{b\}\) constitute unary-bad elements: \(p\) lies in neither \(\neg\{a\}\) nor \(\neg\neg\{a\}\), and similarly for \(b\).

If \(P\) had a third minimal point \(c\), both \((\{a\},\{b\})\) and \((\{a\},\{b,c\})\) would satisfy (1), since the first and second downsets are disjoint and \(p\) lies above \(a,b\). These are two distinct bad partners for the unary-bad first coordinate \(\{a\}\), contradicting equality. Thus \(M=\{a,b\}\).

If a nonminimal point \(q\) were not above both \(a,b\), it would lie above at least one of them, say \(a\), but not above \(b\). Then \((\{b\},\{a\})\) and \((\{b\},\downarrow q)\) are distinct bad ordered pairs, again witnessed by \(p\). This gives two bad partners for the unary-bad coordinate \(\{b\}\), another contradiction. Hence every nonminimal element lies above both minima. The induced order \(Q=P\setminus\{a,b\}\) is nonempty (it contains \(p\)), proving \(P\cong A_2\oplus Q\).

Conversely, if \(P=A_2\oplus Q\) with minimal points \(a,b\) and nonempty \(Q\), its downsets are exactly \(\varnothing\), \(\{a\}\), \(\{b\}\), and \(\{a,b\}\cup D\) for \(D\in J(Q)\). The pseudocomplements of the two singletons are each other, while every downset containing both minima has pseudocomplement \(\varnothing\). Thus precisely the two cross-pairs of singletons fail the second De Morgan law; precisely those two singleton elements fail weak excluded middle. Hence \(u(H)=b(H)=2\). If there is no binary failure, the injection and the classically equivalent zero-defect conditions imply \(u(H)=b(H)=0\). This completes the equality classification.

**4. Sharp satisfaction bound at every algebra size.** A second De Morgan failure requires two minimal points below a third point, so \(J(P)\) contains at least five distinct downsets: \(\varnothing\), the two singletons, their union, and the principal downset of that upper point. Thus \(h\ge5\). As \(b(H)\ge2\), exactly \(h^2-b(H)\) ordered pairs satisfy the equation and the displayed probability bound follows. Equality requires \(b(H)=2\), equivalent by Step 3 to \(P=A_2\oplus Q\). If \(Q\) is a chain with \(r\ge1\) elements, then \(|J(Q)|=r+1\), so \(|H|=r+4\). Taking \(r=h-4\) proves sharpness for every integer \(h\ge5\).

**5. Higher-minimum ordinal sums.** For \(P=A_k\oplus Q\), the downsets are all proper subsets of its \(k\) minimal points, plus sets containing every minimal point and an arbitrary downset of \(Q\). This proves the formula for \(|J(P)|\). Two downsets fail (1) precisely when they are disjoint, nonempty, proper subsets of the minimal antichain: a common upper point in the nonempty \(Q\) witnesses the failure. Assigning each of the \(k\) minimal points to the first subset, the second subset, or neither yields \(3^k\) assignments; excluding the two cases where one subset is empty and restoring the doubly empty case leaves \(3^k-2^{k+1}+1\). This proves the exact binary-defect formula.

**6. Optional computational reduction by minimal traces.** For \(U\subseteq M\) and \(p\in P\), write \(M_p=M\cap\downarrow p\), and put
\[
 P_U=\{x\in P\setminus M:M_x\subseteq U\},
 \qquad w(U)=|J(P_U)|.
\]
Every downset with minimal-point trace \(U\) is uniquely \(U\cup D\), with \(D\in J(P_U)\). Hence the exact binary defect can also be counted by
\[
 b(J(P))=\sum_{U,V\subseteq M}w(U)w(V)
 \mathbf1\bigl[\exists p\in P:\ U\cap M_p\ne\varnothing,\ V\cap M_p\ne\varnothing,\ U\cap V\cap M_p=\varnothing\bigr].
\]
This identity follows directly from (1); it offers an independent counting route and never substitutes a finite census for the preceding all-size proof.

## Verification

The included standalone Python 3 program `verify_second_demorgan.py` enumerates every naturally labeled poset through six points (respectively \(1,2,7,40,357,4824\) posets). It independently computes binary defects from the exact pseudocomplement operation and from minimal-point traces, checks \(b\ge u\), and tests the complete equality/ordinal-sum classification. It also checks sharp equality algebras of every size from five through twenty-three and the closed-form \(k\)-minimum count on 200 additional ordinal-sum instances.

As a boundary check showing that binary defects contain information beyond unary satisfiability counts, two five-point posets encoded by principal-downset bitmasks `(1,3,4,13,19)` and `(1,2,6,15,17)` both have eleven downsets and seven elements satisfying weak excluded middle; their ordered second De Morgan failure counts are respectively six and eight. The verifier recomputes these figures directly. The all-size theorem is proved in Steps 1–5, not inferred from these finite checks.

Run `python3 verify_second_demorgan.py` in the directory containing this document and the script. The script requires only the Python standard library and terminates with `ALL_SECOND_DEMORGAN_CHECKS_PASS examined_posets=5231` on success.

## Relationship to prior work

The second De Morgan law, also described as the Stone identity or extremal disconnectedness condition in this setting, and its equivalence to several qualitative conditions are established background. Arrieta's 2020 work (especially Proposition 2.4) studies this law and its infinite analogues. Bumpus and Kocsis (first public version 2021) formulate degrees of satisfiability for Heyting identities and analyze one-variable principles and selected two-variable classical principles. Their covered results do not state the present exact comparison of unary and ordered binary defects, the first nonzero defect's complete equality classification, or the sharp cardinality-dependent bound.

The classical equivalence of the **universal** unary and binary equations does not equate the number of failing assignments. This is also illustrated by the two eleven-element examples above. Searches under “Stone algebra”, “weak excluded middle”, “second De Morgan law”, “pseudocomplement”, and “degree of satisfiability” found no directly dominating quantitative theorem among the inspected accessible sources. This search cannot establish absolute historical priority.

## Limitations

The results apply only to finite Heyting algebras, uniform sampling with replacement, and ordered pairs. The numerical bound is indexed by the number of **algebra elements**, not the number of join-irreducibles. No full classification of all possible positive binary-defect counts is asserted. Computation covers only the finite instances explicitly stated above and is not an independent scientific audit. Further historical-priority checks, including literature under specialized Stone-algebra terminology, could uncover earlier equivalent results.

## References

1. Igor Arrieta, *On infinite variants of De Morgan law in locale theory*, arXiv:2001.09143, first posted 2020-01-24, https://arxiv.org/abs/2001.09143. See the definition of the second De Morgan law and Proposition 2.4.
2. Benjamin Merlin Bumpus and Zoltan A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515, first posted 2021-10-21, https://arxiv.org/abs/2110.11515. See the definition of degree of satisfiability and Sections 2–3.
