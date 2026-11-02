# Exact modal-expansion counts on finite Boolean–Kleene products

## Finding
Let \(\mathbf 2\) be the two-element Boolean chain and \(\mathbf 3\) the three-element Kleene chain \(0<u<1\). Both carry their ordinary lattice operations; the involution interchanges the endpoints and fixes \(u\) in \(\mathbf3\). Fix integers \(h,k\ge0\) with \(n=h+k\ge1\), and set
\[
K_{h,k}=\mathbf2^{\,h}\times\mathbf3^{\,k}.
\]
A **modal Kleene expansion** of this fixed labelled lattice-involution algebra is a unary operator \(\blacksquare\) obeying, for all \(x,y,z\),
\[
\begin{aligned}
\text{(MK)}&\quad \blacksquare(x\wedge y)=\blacksquare x\wedge\blacksquare y,\\
\text{(Pos)}&\quad \sim\blacksquare(z\vee\sim z)\le\blacksquare(z\vee\sim z),\\
\text{(Con)}&\quad \blacksquare(x\vee(z\wedge\sim z))\le\blacksquare x\vee\sim\blacksquare(x\vee(z\wedge\sim z)).
\end{aligned}
\]
These are the defining modal-Kleene axioms in Celani–Menchón–Miguelez (2026). The number of **distinct labelled unary operations** satisfying all three is exactly
\[
\boxed{N(h,k)=2^{h^2}\bigl(2^{h+k}+3^{h+k}\bigr)^k.}
\]
There is a complete independent-coordinate normal form, given next; hence the formula is not merely an asymptotic count.

## Assumptions and scope
Choose a labelled \(n\)-element set \(X\) and a distinguished subset \(H\subseteq X\) of size \(h\). Identify \(K_{h,k}\) with
\[
T_H=\{(A,B):A,B\subseteq X,\ A\cap B=\varnothing,\ H\subseteq A\cup B\},
\]
with \((A,B)\wedge(C,D)=(A\cap C,B\cup D)\), \((A,B)\vee(C,D)=(A\cup C,B\cap D)\), and \(\sim(A,B)=(B,A)\). The coordinates indexed by \(H\) admit two truth states and the remaining coordinates three; this is a literal isomorphism of bounded involutive lattices.

Every admissible \(\blacksquare:T_H\to T_H\) is **uniquely** given by
\[
\blacksquare(A,B)=(\Box A,\Diamond B),
\]
where \(\Box,\Diamond:\mathcal P(X)\to\mathcal P(X)\) are specified separately at each output atom \(y\in X\) as follows.

For \(y\in H\), choose an arbitrary \(S_y\subseteq H\). Then
\[
y\in\Box A\ \Longleftrightarrow\ S_y\subseteq A,\qquad
y\in\Diamond B\ \Longleftrightarrow\ S_y\cap B\ne\varnothing.
\]
For \(y\notin H\), make exactly one of these choices:

* **inactive box:** \(y\notin\Box A\) for all \(A\); choose any \(Q_y\subseteq X\), and put \(y\in\Diamond B\iff Q_y\cap B\ne\varnothing\);
* **active box:** choose \(P_y\subseteq X\) and \(Q_y\subseteq P_y\); put \(y\in\Box A\iff P_y\subseteq A\) and \(y\in\Diamond B\iff Q_y\cap B\ne\varnothing\).

Conversely all such independent choices define modal Kleene expansions. The count includes non-normal modal operations; no equation \(\blacksquare1=1\) is assumed, and no quotient by relabelling or algebra automorphisms is taken.

## Proof
**1. Separate the two set coordinates.** Let \(m:T_H\to T_H\) satisfy (MK), (Pos), (Con). Preservation of binary meets implies that \(m\) is monotone. Each positive element \((C,\varnothing)\), where \(C\supseteq H\), has the form \(z\vee\sim z\), taking \(z=(C,\varnothing)\). In this twist lattice an element \((E,F)\) is positive exactly when \(F=\varnothing\). Thus (Pos) implies the *second* coordinate of \(m(C,\varnothing)\) is empty.

For any \((A,B)\in T_H\), put \(C=A\cup H\). Then
\[
(A,B)=(X\setminus B,B)\wedge(C,\varnothing).
\]
Consequently (MK) and the preceding positivity observation show that the second coordinate of \(m(A,B)\) depends on \(B\) alone. Denote it by \(\Diamond B\).

For the first coordinate put \(D=B\cup H\) and \(r_A=(A,X\setminus A)\). Since \((D,\varnothing)\in T_H\),
\[
(A,B)=r_A\vee\bigl((D,\varnothing)\wedge\sim(D,\varnothing)\bigr).
\]
Monotonicity gives first-coordinate inclusion from \(m(r_A)\) into \(m(A,B)\). Applying (Con) to this displayed join yields the reverse inclusion: if \(m(A,B)=(E,F)\), the first coordinate of \(m(r_A)\vee\sim m(A,B)\) equals the union of the first coordinate of \(m(r_A)\) with \(F\); disjointness \(E\cap F=\varnothing\) removes the latter possibility. Hence the first coordinate depends only on \(A\). Denote it by \(\Box A\). Every \(A\) and every \(B\) occurs in some member of \(T_H\), so these maps are unique.

**2. Translate the axioms to set operations.** Apply (MK) to pairs \((A,X\setminus A)\) to obtain \(\Box(A\cap C)=\Box A\cap\Box C\), and similarly obtain \(\Diamond(B\cup D)=\Diamond B\cup\Diamond D\). Positivity at \((X,\varnothing)\) yields \(\Diamond\varnothing=\varnothing\). Because \(m(A,B)\) must lie in \(T_H\), we have
\[
\Box A\cap\Diamond B=\varnothing,
\quad H\subseteq\Box A\cup\Diamond B
\qquad(A\cap B=\varnothing,\ H\subseteq A\cup B).
\]
In fact, the first constraint also holds for *all* disjoint \(A,B\), without the coverage assumption: replace \(A\) by \(A\cup(H\setminus(A\cup B))\), and use monotonicity of \(\Box\).

Conversely, suppose a pair \((\Box,\Diamond)\) satisfies the two binary preservation laws, \(\Diamond\varnothing=\varnothing\), the full disjointness condition, and the displayed coverage condition. Then \(m(A,B)=(\Box A,\Diamond B)\) maps \(T_H\) into itself and preserves meets. It satisfies (Pos) because the second component at \((C,\varnothing)\) is empty. For (Con), \(x\) and \(x\vee(z\wedge\sim z)\) have the same first component, say \(A\); their images have the same first set \(\Box A\), and the latter image has a second set contained in the former because \(\Diamond\) is monotone. Using disjointness of the two components in each image directly gives the inequality in (Con). Thus the translation is an equivalence, not merely a necessary condition.

**3. Classify outputs of the Boolean operators.** For each output atom \(y\), binary-meet preservation makes \(\{A:y\in\Box A\}\) an upward closed, finite-intersection closed family. It is either empty or the principal filter generated by a unique \(P_y\subseteq X\); in the latter case \(y\in\Box A\iff P_y\subseteq A\). Binary-join preservation and \(\Diamond\varnothing=\varnothing\) similarly give a unique subset \(Q_y\subseteq X\) with \(y\in\Diamond B\iff Q_y\cap B\ne\varnothing\).

If the box family is empty, the disjointness requirement says nothing about \(Q_y\). If it is principal, that requirement holds for every disjoint \(A,B\) precisely when \(Q_y\subseteq P_y\): necessity follows by testing \(A=P_y\), \(B=\{q\}\), and sufficiency is immediate.

For \(y\in H\), coverage with \(A=H,B=\varnothing\) forces the box family to be principal and \(P_y\subseteq H\). Fix \(p\in P_y\) and test \(A=H\setminus\{p\}\), \(B=\{p\}\). Coverage forces \(p\in Q_y\). Therefore \(P_y\subseteq Q_y\), and disjointness gives \(Q_y=P_y\subseteq H\). Conversely these conditions ensure coverage for all disjoint pairs covering \(H\): if \(P_y\not\subseteq A\), some element of \(P_y\) lies in \(B\). No coverage restriction is imposed at \(y\notin H\).

**4. Count choices.** At each \(y\in H\) there are \(2^h\) choices. At each \(y\notin H\) there are \(2^n\) choices for an inactive box and \(\sum_{P\subseteq X}2^{|P|}=3^n\) choices for an active box. Different output atoms are independent. Multiplication yields \(2^{h^2}(2^n+3^n)^k\), as asserted.

## Verification
The accompanying `checker.py` performs two genuinely different finite checks. For all \(n=1,2,3,4\) and all \(2^n\) choices of \(H\), it independently enumerates the possible Boolean output-threshold sets and tests the original contact/coverage implications on all relevant subset pairs. It obtains the stated formula in all 30 cases. Separately, for fixed underlying carriers of sizes \(2,3,4,6\) (parameters \((h,k)=(1,0),(0,1),(2,0),(1,1)\)), it enumerates **every** unary function on the underlying lattice and directly evaluates (MK), (Pos), and (Con), without using the coordinate classification; the counts are respectively \(2,5,16,26\). Executing `python checker.py` prints `ALL_CHECKS_OK`. The arbitrary-parameter theorem follows from the preceding proof rather than finite tests.

## Relationship to prior work
Celani, Menchón and Miguelez (arXiv:2608.10937, first public version 2026-08-11) introduce modal Kleene algebras, modal contact lattices and triples, and show that their twist constructions give a categorical equivalence. In particular, their Definitions 3.1–3.5 supply the three axioms used here, and their Theorem 3.9 constructs the pair-valued modal operator from suitable lattice operators. The current theorem is a specialized *complete labelled finite census* on all products of two- and three-valued Kleene factors, with a concrete atom-by-atom normal form and a support-sensitive sharp formula. The cited general categorical theorem alone does not state that numeric classification. Jalali's earlier non-modal representation and standard Boolean relational semantics underlie the setting; the classical \(k=0\) subcase is the familiar \(2^{h^2}\) count of normal modal operators on a finite Boolean algebra.

## Limitations
This result counts **labelled** unary expansions only, not isomorphism classes, arbitrary finite Kleene algebras, modal implications or operators satisfying additional axioms. It does not assert that the known abstract representation or the classical Boolean boundary cases are new. Older equivalent enumerations might exist under different terminology for finite Kleene or De Morgan algebras; this remains a historical-priority risk.

## References
1. S. Celani, P. Menchón, V. Miguelez, *A Modal Expansion of Kleene Algebras via Twist Structures*, arXiv:2608.10937v1, 2026-08-11, especially §§2–3, Definitions 3.1–3.5 and Theorem 3.9. https://arxiv.org/abs/2608.10937
2. A. Jalali, *A representation of Kleene algebras and the characterisation of projective Kleene and De Morgan algebras*, Rend. Circ. Mat. Palermo Suppl. 29 (1992), 435–474 (prior non-modal representation, as cited in reference 8 of Celani et al.).
3. J. Kalman, *Lattices with involution*, Trans. Amer. Math. Soc. 87 (1958), 485–491 (foundational twist construction).
