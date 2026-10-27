# A two-state exact calculus for one-types over series–parallel posets

## Finding
Let \(\mathcal R\) be the countable universal ultrahomogeneous poset in the pure order language. A **series–parallel poset** is any finite poset obtained from singletons and the empty poset by iterating disjoint union \(P\parallel Q\) and ordinal sum \(P\oplus Q\), with every element of \(P\) below every element of \(Q\) in the latter. Fix all elements of a finite series–parallel parameter poset \(P\subseteq\mathcal R\) individually, and let \(t(P)\) be its number of complete nonalgebraic one-types.

There is an exact two-integer evaluation of \(t(P)\). Initialize a singleton with \((a,b)=(1,0)\) and the empty poset with \((a,b)=(0,0)\). On a decomposition tree, use
\[
\begin{aligned}
(a,b)(P\parallel Q)&=(a_P+a_Q+a_Pa_Q,\ b_P+b_Q),\\
(a,b)(P\oplus Q)&=(a_P+a_Q,\ b_P+b_Q+a_Pa_Q).
\end{aligned}
\]
Then
\[
\boxed{t(P)=2a_P+b_P+1.}
\]
The two integers have intrinsic interpretations: \(a_P\) is the number of nonempty order ideals of \(P\), while \(b_P\) is the number of consistent one-point extension profiles in which the new point has at least one named point below and at least one above it. Consequently, the result is independent of the chosen decomposition tree. Given a binary decomposition with \(n\) leaves, computing the exact count takes \(O(n)\) integer-arithmetic operations on integers with \(O(n)\) bits; classical integer arithmetic gives a polynomial bit-time algorithm.

This covers posets with diamonds and other nested compositions not covered by ancestor-order rooted-forest formulas. For the four-element diamond \(P=\{u\}\oplus(\{v\}\parallel\{w\})\oplus\{z\}\), the invariant is \((a_P,b_P)=(5,7)\) and \(t(P)=18\).

## Assumptions and scope
The base poset is finite, with a given expression in binary ordinal sums and disjoint unions. The order is strict when comparisons to a new point are written. All base points are individually named and fixed pointwise. A type is nonalgebraic when it is realized by a new point outside the base, not by one of the named points. The empty base is permitted and has one nonalgebraic one-type. No upper bound on series–parallel width, height, or number of alternations is imposed. Complexity is measured for a supplied decomposition, not for an arbitrary encoded poset lacking one.

## Proof
**Step 1 (finite-extension correspondence).** For an element \(x\notin P\) of a one-point extension, define
\[
L=\{p\in P:p<x\},\qquad U=\{p\in P:x<p\}.
\]
Transitivity holds precisely when \(L\) is a downset, \(U\) is an upset, and \(l<u\) for every \(l\in L,u\in U\). Conversely these conditions make a consistent strict partial order on \(P\cup\{x\}\). The finite-extension property of \(\mathcal R\) realizes every such profile. Arbitrarily many pairwise incomparable new points can realize the same profile, proving nonalgebraicity. Homogeneity makes distinct profiles distinct complete types, so \(t(P)\) equals their number.

**Step 2 (decomposition of types).** Write \(I(P)\) for the number of downsets including the empty downset, and \(B(P)\) for profiles with both \(L\ne\varnothing\) and \(U\ne\varnothing\). Exactly \(I(P)\) profiles have \(U=\varnothing\), and exactly \(I(P)\) have \(L=\varnothing\) (upsets are complements of downsets). Only the completely incomparable profile is counted twice. Thus
\[
t(P)=2I(P)-1+B(P),\quad a_P=I(P)-1,\quad b_P=B(P).
\]

**Step 3 (parallel composition).** In \(P\parallel Q\) a downset consists of independent downsets of \(P\) and \(Q\). Hence \(I(P\parallel Q)=I(P)I(Q)\), giving the parallel recurrence for \(a\). A two-sided profile cannot have a lower point in one component and an upper point in the other, because those points are incomparable in the base. It must therefore be a two-sided profile entirely inside one component, with the new point incomparable to every base element of the other. The alternatives are disjoint, so \(B(P\parallel Q)=B(P)+B(Q)\).

**Step 4 (series composition).** Every downset of \(P\oplus Q\) is either a downset properly contained in \(P\), or all of \(P\) together with a downset of \(Q\). Accounting once for the shared case \(P\),
\[
I(P\oplus Q)=I(P)+I(Q)-1.
\]
Any two-sided profile in \(P\oplus Q\) is of exactly one of three forms: (i) both lower and upper sets meet \(P\), so their restrictions give a two-sided profile in \(P\), while every point of \(Q\) lies above \(x\); (ii) both sets meet \(Q\), with a two-sided profile there and every point of \(P\) below \(x\); or (iii) a nonempty lower ideal contained in \(P\) and a nonempty upper filter contained in \(Q\). There are \(B(P)\), \(B(Q)\), and \((I(P)-1)(I(Q)-1)\) such profiles, respectively. These are exhaustive: if any point of \(Q\) lies below \(x\), all of \(P\) does; if any point of \(P\) lies above \(x\), all of \(Q\) does. In particular a profile cannot mix an upper point of \(P\) with a lower point of \(Q\). This proves the series recurrence for \(b\).

**Step 5 (initial conditions, runtime and examples).** A singleton has exactly two nonempty / empty downset choices, and no two-sided profile, so \((a,b)=(1,0)\). For an empty poset, \((a,b)=(0,0)\). Induction over the decomposition establishes the asserted pair of invariants and the formula for every series–parallel poset. A chain of \(n\) points has \((a,b)=(n,\binom n2)\) and \(t=1+n(n+3)/2\); an antichain has \((a,b)=(2^n-1,0)\) and \(t=2^{n+1}-1\). The diamond calculation is \((1,0)\oplus((1,0)\parallel(1,0))\oplus(1,0)=(5,7)\), yielding \(18\). A decomposition has \(O(n)\) nodes, and all counts are at most \(3^n\), hence each integer has \(O(n)\) bits.

## Verification
Run `python3 verify_series_parallel.py` with standard Python. The script generates every binary expression tree with ordered consecutive leaf labels and either series or parallel at each internal node, for \(1\le n\le6\); these yield \(1,2,6,22,90,394\) distinct labelled structures in that expression convention. It constructs the entire strict order for each generated structure, independently enumerates all three-way comparisons of a new point to the old vertices and tests them against transitivity and the required strict lower–upper comparisons, and independently counts downsets by subsets. It then compares both exact counts with the two-state recursion. It also verifies \(260\) reproducibly sampled larger expressions on \(7\)–\(10\) vertices and checks the empty and diamond cases. The actual execution record is in `verification_output.txt`. These finite tests corroborate but do not replace the all-size inductive proof.

## Relationship to prior work
The generic poset and the finite extension/homogeneity principle are classical; no novelty is claimed there. Valdes–Tarjan–Lawler studied recognition and decomposition of series–parallel digraphs, not these type-counting recurrences in their accessible abstracts. Pretzel's 1980 insertion-position construction is closely related to one-point types; its accessible abstract concerns dimension and particular height restrictions, and its full text was not available for a decisive comparison. A published general finite-parameter one-type counting result supplies the ideal/filter characterization and unrestricted \(\#\mathrm P\)-hardness, but its accessible index does not state the exact series–parallel two-state calculus. A prior rooted-forest parameter formula handles ancestor-order forests but does not cover arbitrary nested series–parallel orders, such as the diamond above. The contribution here is the exact evaluation on the entire series–parallel closure by the intrinsically meaningful two-state algebra; specialized precedence-counting literature may still contain related formulas.

## Limitations
The result requires an expression as a finite series–parallel poset. It does not give a constant-state computation on unrestricted finite posets, for which exact type counting is hard. No claim is made that the recurrence is the first ever algorithm for insertion counting in this class. The specialized older insertion-position literature could not be fully read; priority is therefore qualified. Independent scientific validation has not been performed.

## References
1. J. Valdes, R. E. Tarjan, and E. L. Lawler, *The recognition of series parallel digraphs*, STOC 1979, pp. 1–12, DOI: 10.1145/800135.804393 (30 April 1979).
2. O. Pretzel, *A construction for partially ordered sets*, Discrete Mathematics 32 (1980), 59–68, DOI: 10.1016/0012-365X(80)90100-4.
3. A. S. Kechris, V. G. Pestov, and S. Todorcevic, *Fraïssé Limits, Ramsey Theory, and Topological Dynamics of Automorphism Groups*, arXiv:math/0305241v1 (16 May 2003), general Fraïssé framework.
4. J. Hubička, *Combinatorial Properties of Finite Models*, arXiv:1009.0566v1 (3 September 2010), Chapter 3 on the generic partial order.
5. *Finite-parameter 1-type counting in the random poset is #P-complete*, published research-index finding (2026), identifier `2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1`, indexed summary inspected.
