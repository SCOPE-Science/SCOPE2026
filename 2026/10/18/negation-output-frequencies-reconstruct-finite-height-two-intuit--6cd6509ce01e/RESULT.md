# Negation-output frequencies reconstruct finite height-two intuitionistic frames

## Finding
Let \(P\) be a nonempty finite poset of height at most two, \(M=\operatorname{Max}(P)\), and \(H=\operatorname{Up}(P)\), with implication defined by the usual Heyting adjunction. For each \(S\subseteq M\), put \(R_S=P\setminus\downarrow S\), using \(\downarrow\varnothing=\varnothing\). For uniformly random \(U\in H\), define the output probability
\[
p(S)=\Pr(\neg U=R_S).
\]
**Inverse negation theorem.** The distinct \(R_S\) are all the possible negation outputs. The probability law \(p\), together with the Boolean-lattice identification of its outputs (only up to relabeling its atoms), determines the entire order-isomorphism type of \(P\). Explicitly, for every nonempty \(T\subseteq M\),
\[
h(T)=\sum_{S\subseteq T}(-1)^{|T|-|S|}\log_2\frac{p(S)}{p(\varnothing)}
\]
is the number of nonmaximal points lying strictly below **exactly** the maximal points in \(T\).

**Exact recognition.** A strictly positive probability measure on an abstract Boolean algebra of \(2^m\) elements, \(m\ge1\), occurs as the negation-output law of a finite height-at-most-two poset exactly when (i) all ratios \(p(S)/p(\varnothing)\) are nonnegative integral powers of two, and (ii) the displayed Möbius coefficients for nonempty \(T\) are nonnegative integers. The reconstructed frame has \(m+\sum_{\varnothing\neq T\subseteq M}h(T)\) points. The test and inverse require \(O(m2^m)\) exact arithmetic operations given the indexed probability table.

**The indexing is essential.** For the six-point frames whose three lower vertices have maximal-successor multisets respectively \(\{\{c\},\{a,b,c\},\{a,b,c\}\}\) and \(\{\{a,b\},\{a,c\},\{b,c\}\}\), the unordered negation-fiber counts coincide: four fibers of size \(1\), three of size \(2\), and one of size \(8\). Yet the frames are nonisomorphic, since their lower points have different multisets of upper degrees, \(\{1,3,3\}\) and \(\{2,2,2\}\).

## Assumptions and scope
The order has no chain of three distinct elements. A point with no strict successors is maximal; every remaining point lies strictly below a nonempty subset of \(M\) and is incomparable with other nonmaximal points. The distribution is on *distinguished elements of the Boolean image of negation*, not on an unordered bag of numerical probabilities. The Boolean image itself is canonically available inside the finite Heyting algebra as the regular elements; one may relabel its atoms freely without changing the recovered isomorphism type.

## Proof
**Step 1: negation depends exactly on maximal trace.** For an upset \(U\), the pseudocomplement is
\[
\neg U=P\setminus\downarrow U.
\]
Indeed, a point belongs to \(\neg U\) exactly when its principal upset misses \(U\). Each point of the finite upset \(U\) lies below a maximal point of \(P\) in \(U\). Thus if \(S=U\cap M\), then \(\downarrow U=\downarrow S\), so \(\neg U=R_S\). Conversely, \(U=S\) is itself an upset and gives the output \(R_S\). Further, \(R_S\cap M=M\setminus S\), showing that distinct \(S\) have distinct outputs. They consequently form the regular Boolean algebra, with the order on outputs reversing inclusion of \(S\).

**Step 2: count each fiber.** For a nonmaximal point \(v\), write \(N(v)=\{m\in M:v<m\}\). Its set \(N(v)\) is nonempty. Holding \(U\cap M=S\) fixed, inclusion of \(v\) in an upset \(U\) is *allowed* precisely when \(N(v)\subseteq S\). Height at most two leaves all nonmaximal points incomparable, so these choices are independent. With \(h(T)=|\{v\in P\setminus M:N(v)=T\}|\), the number of upsets in the negation fiber is therefore
\[
f(S)=|\{U:\neg U=R_S\}|=2^{c(S)},\qquad
c(S)=\sum_{\varnothing\neq T\subseteq S}h(T).
\]
In particular, \(f(\varnothing)=1\), since only the empty upset has maximal trace \(\varnothing\), and \(|H|=\sum_{S\subseteq M}f(S)\). Hence \(p(S)=f(S)/|H|\) and \(f(S)=p(S)/p(\varnothing)\).

**Step 3: invert and reconstruct.** Extend \(h\) by \(h(\varnothing)=0\). The relation \(c(S)=\sum_{T\subseteq S}h(T)\) is the Boolean zeta transform. Möbius inversion gives
\[
h(T)=\sum_{S\subseteq T}(-1)^{|T|-|S|}c(S).
\]
This determines for each nonempty \(T\) how many mutually incomparable lower points are incident with exactly \(T\). There are no other order relations, so these integers determine \(P\) up to isomorphism. A relabeling of the Boolean atoms corresponds exactly to a relabeling of maximal points. The standard fast subset Möbius transform uses \(O(m2^m)\) additions and subtractions.

**Step 4: the converse and boundaries.** If positive rational or real probabilities satisfy the two stated conditions, construct \(m\) maxima and \(h(T)\) lower points with neighborhood \(T\) for every nonempty \(T\). Its fiber counts, by Step 2, equal all prescribed ratios. The normalized counts agree with the original probabilities because they both sum to one. Conversely, the formulas show the conditions are necessary. For the two six-point witnesses, direct substitution gives the same unordered multiset of counts, but their strict upper-degree multisets differ, so Boolean indexing cannot be discarded. In a three-element chain, there are three upsets containing its single maximum, showing that the power-of-two criterion cannot be extended to height three.

## Verification
The accompanying standalone program `verify_negation.py` independently enumerates every labelled incidence relation in a bounded family of height-at-most-two frames, constructs all upsets from the order relation, computes the pseudocomplement from principal-upset disjointness (rather than using the inversion formula), and checks each fiber, its normalization, and Möbius inversion. It verified 6,543 frames and 224,635 upsets, and checked the three-point-chain boundary. The general result is proved above, rather than inferred from the finite computations.

## Relationship to prior work
Bumpus and Kocsis introduced satisfiability-degree questions for finite Heyting algebras and prove that the image of the negation map is the Boolean algebra of double-negation fixed points (Proposition 2.12). That establishes the natural Boolean codomain, but not the incidence reconstruction from the *conditional distribution over its individual outputs*. Here the full probability table, instead of a single satisfiability degree or the Boolean image cardinality, is inverted to recover the frame. Boolean zeta/Möbius inversion is standard; the contribution is the complete exact identification of its input as Heyting-negation fiber probabilities, the inverse recognition theorem, and the explicit loss of identifiability when output labels are forgotten.

## Limitations
The theorem applies to finite frames of height at most two; height-three fibers can have non-power-of-two sizes. It assumes the full Boolean-indexed law is given exactly, not estimated from finitely many samples, and makes no sample-complexity or noise-robustness assertion. In particular, merely knowing the unordered histogram of fiber sizes does not suffice. Earlier equivalent formulations in distributive-lattice or hypergraph enumeration literature have not been excluded definitively. Independent external validation has not been performed.

## References
1. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515 (original version publicly posted 2021-10-21), especially §1.3 and Proposition 2.12. https://arxiv.org/abs/2110.11515
2. Boolean-lattice Möbius inversion and the finite representation of distributive lattices are standard background results; no priority for them is claimed.
