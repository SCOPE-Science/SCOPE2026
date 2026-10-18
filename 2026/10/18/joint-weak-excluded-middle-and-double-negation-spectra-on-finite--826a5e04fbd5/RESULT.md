# Joint weak-excluded-middle and double-negation spectra on finite Heyting frames

## Finding
Let \(P\) be a nonempty finite poset, let \(H=\operatorname{Up}(P)\) be its Heyting algebra of upward-closed subsets, and let \(P_1,\ldots,P_c\) be the connected components of the undirected comparability graph of \(P\). Write \(M_i=\operatorname{Max}(P_i)\), \(m=\sum_i|M_i|\), \(N=|H|\), and \(u(Q)=|\operatorname{Up}(Q)|\), including \(u(\varnothing)=1\). Put
\[
W=\prod_{i=1}^c\left(1+u(P_i\setminus M_i)\right).
\]
For a uniformly selected \(U\in H\), consider the two one-variable classical principles
\[
\mathrm{WEM}:\quad \neg U\vee\neg\neg U=P,
\qquad
\mathrm{DNE}:\quad \neg\neg U=U.
\]
Their **entire joint satisfaction spectrum** is exactly
\[
\begin{array}{c|cc}
&\mathrm{DNE}&\neg\mathrm{DNE}\\\hline
\mathrm{WEM}&2^c&W-2^c\\
\neg\mathrm{WEM}&2^m-2^c&N-W-2^m+2^c
\end{array}.
\]
In particular the corresponding joint probabilities are these four integers divided by \(N\). This formula applies to **every** finite Heyting algebra via finite distributive-lattice representation.

There is also an exact structural characterization of the zero bottom-right entry: every \(U\in H\) satisfies WEM **or** DNE if and only if precisely one of the following possibilities holds:

1. Every comparability component of \(P\) has exactly one maximal element; in this case WEM holds for every \(U\).
2. There is exactly one component \(C\) with at least two maximal elements, every other component is a singleton, and every nonmaximal point \(p\in C\) lies below **every** maximal element of \(C\).

Consequently, the algebraic relation \(\Pr(\mathrm{WEM})+\Pr(\mathrm{DNE})=1+\Pr(U\vee\neg U=P)\) holds exactly on this explicitly classified family of finite frames. The conventional probability in this last display is computed with the same uniform choice of \(U\).

For example, a three-point fork (one minimum below two incomparable maxima) has joint counts \(2,1,2,0\) in the order (both, WEM-only, DNE-only, neither). Taking its disjoint union with a two-point chain changes the counts to \(4,5,4,2\): the previously absent neither-category becomes nonempty through independent interactions across components.

## Assumptions and scope
The poset \(P\) is finite, nonempty, and antisymmetric; no gradedness, height bound, connectedness, or restriction on the number of maximal points is assumed. The order-theoretic representation \(H\cong\operatorname{Up}(P)\) is the standard finite distributive-lattice representation. The negation is Heyting pseudocomplement \(\neg U=U\to\varnothing\), not set-theoretic complement. The truth of WEM/DNE is evaluated separately at each algebra element; no global axiom is presumed. All counts count distinct elements of \(H\), not labelled valuations or isomorphism types.

For any point \(p\), let \(M(p)=\{q\in\operatorname{Max}(P):p\le q\}\). It is nonempty. The restriction \(P_i\setminus M_i\) is the induced poset, and \(u(P_i\setminus M_i)\) counts all upsets of this induced poset.

## Proof
**Negation and double negation.** For any upset \(U\), residuation gives \(\neg U=\{p:\uparrow p\cap U=\varnothing\}\). Finiteness and upward closure show
\[
p\in\neg U\iff M(p)\cap U=\varnothing,
\qquad
p\in\neg\neg U\iff M(p)\subseteq U.
\]
For the second equivalence, \(p\in\neg\neg U\) means no \(q\ge p\) belongs to \(\neg U\); if a maximal \(r\ge p\) is outside \(U\), then \(r\in\neg U\). Conversely, if every maximal \(r\ge p\) belongs to \(U\), each \(q\ge p\) lies below such an \(r\), hence \(q\notin\neg U\). Thus \(\neg\neg U\) is determined by \(A=U\cap\operatorname{Max}(P)\), and every \(A\subseteq\operatorname{Max}(P)\) determines a distinct fixed point
\[
F(A)=\{p:M(p)\subseteq A\}.
\]
The set \(F(A)\) is an upset: \(p\le q\) implies \(M(q)\subseteq M(p)\), and it has exactly \(A\) as maximal points. Hence exactly \(2^m\) upsets satisfy DNE.

**Weak excluded middle.** At a given point \(p\), the equality \(p\in\neg U\cup\neg\neg U\) holds precisely when all maxima in \(M(p)\) have the same membership in \(U\): either none or all. If \(p\le q\), then \(M(q)\subseteq M(p)\), so the monochromatic choices for \(M(p)\) and \(M(q)\) agree. By comparability-connectedness, the color assigned to maxima is constant throughout each component \(P_i\). Conversely, monochromatic membership in each component makes every \(M(p)\) monochromatic. Since a nonempty upset contains a maximal point, within each component WEM thus means either \(U\cap P_i=\varnothing\) or \(M_i\subseteq U\cap P_i\).

Upward-closed subsets of \(P_i\) containing all maximal points are in bijection with upsets of \(P_i\setminus M_i\) by deletion or adjoining of \(M_i\). The empty upset is a further, disjoint choice. Choices multiply across components, proving the value \(W\).

**Intersection and joint table.** A DNE-fixed upset \(F(A)\) is also WEM exactly when \(A\) is a union of the sets \(M_i\). For each component this selects either all or none of its maximal points, giving \(2^c\) choices. These are precisely the complemented upsets, i.e. unions of whole comparability components, which satisfy \(U\vee\neg U=P\). The four entries follow by inclusion–exclusion from \(N,W,2^m,2^c\).

**Classification when the neither cell vanishes.** If each component has just one maximum, its WEM condition is automatic, giving case 1. Suppose a component \(C\) has at least two maxima. Since \(C\) is comparability-connected, it contains a nonmaximal point. It has a WEM-only upset, namely \(M(C)\), since its double-negation closure is all of \(C\); and it has a DNE-only upset \(F(A)\) for any proper nonempty subset \(A\subset M(C)\), since not all maxima have the same membership.

If a distinct component \(D\) is nonsingleton and has one maximal point, its maximal-point singleton is WEM-only. If instead \(D\) has several maxima, it too possesses a WEM-only upset. Combining a DNE-only upset on \(C\), a WEM-only upset on \(D\), and empty upsets on the remaining components produces a global valuation satisfying neither principle. Thus the absence of such a valuation requires exactly one multimaximal component, with all other components singletons.

For this one component \(C\), if a nonmaximal \(p\) has \(M(p)\subsetneq M(C)\), the upset \(U=M(p)\) has both kinds of maxima and therefore fails WEM; but \(p\in F(M(p))\setminus U\), so it fails DNE too. Hence the stated all-maxima-above condition is necessary. Conversely, if every nonmaximal \(p\) lies below all maxima, any upset containing all maxima satisfies WEM, while any upset lacking at least one maximum consists only of maximal points and equals its double-negation closure, satisfying DNE. Singleton components satisfy both principles universally. This proves sufficiency, completes the classification, and establishes the probability equality.

## Verification
The companion `verify_joint.py` builds all labelled posets with at most five elements (4,473 reflexive transitive antisymmetric labelled orders in total), independently enumerates their upsets and computes negation as an order-theoretic pseudocomplement. For every poset it checks both coordinate counts, the overlap, and the complete frame classification of vanishing neither count. Running `python verify_joint.py` returns `VERIFY_OK all labelled posets <=5 4473`. The independent finite enumeration checks instances; the arbitrary-order statements rest on the proof above.

## Relationship to prior work
Bumpus and Kocsis, *Degree of Satisfiability in Heyting Algebras* (arXiv:2110.11515, first posted 2021-10-21), introduce the degree-of-satisfiability approach and specifically identify the joint behavior of WEM and DNE as a motivating example in their discussion of relative degrees (§6.6). Their §1.16–§1.22 recalls the Boolean center, the Glivenko double-negation-fixed subalgebra, and related inequalities. The general facts that complemented and regular elements form Boolean structures are classical; neither those facts nor the general Heyting–poset correspondence are claimed as new. The contribution here is the full joint numerical distribution in **every** finite dual poset and a necessary-and-sufficient global structural classification of when the union of the two satisfaction sets is all of the algebra. It is distinct from separate one-variable gap classifications, individual Boolean-center proportions, and specialized Boolean-plus-chain materializer calculations.

Kocsis's *Apartness relations between propositions* (arXiv:2209.03920, 2022-09-08) proves a global weak-excluded-middle condition equivalent to definability of a nontrivial apartness term (§4.8). The inspected introduction and §4.8 address term existence and universal validity, not counts of satisfying elements or the relative two-law exhaustion criterion. This comparison is about mathematical implication, not mere terminology.

## Limitations
This is a finite theorem only; neither asymptotic distribution over random posets nor full relative-degree classification for all pairs of one-variable formulas is established. Formula evaluation presupposes uniform distribution over distinct elements of a finite algebra. Ordinary double-negation and component lemmas are standard. Earlier independent derivation of these exact formulas or the frame classification, especially in specialized intuitionistic frame enumeration, remains possible. No independent mathematical audit or priority certification has been performed.

## References
1. Benjamin Merlin Bumpus and Zoltan A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515v1 (first posted 2021-10-21), especially §§1.16–1.22 and 6.6; published in *Journal of Symbolic Logic*, doi:10.1017/jsl.2024.2.
2. Zoltan A. Kocsis, *Apartness relations between propositions*, arXiv:2209.03920v1 (first posted 2022-09-08).
3. V. Glivenko, *Sur quelques points de la logique de M. Brouwer*, 1929 (classical double-negation theorem, as referenced in [1]).
