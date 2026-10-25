# Exact two-point and fixed-arity type spectra over antichains in the random poset

## Finding
Let \(\mathbb P\) denote the countable universal ultrahomogeneous partial order and let \(A_n\subset\mathbb P\) be an induced antichain of \(n\ge0\) individually named elements. Write \(T_r(n)\) for the number of complete first-order types over \(A_n\) of **ordered tuples of \(r\) pairwise distinct elements outside \(A_n\)**. Thus the parameter equalities and repeated tuple coordinates are deliberately excluded. In particular, \(T_0(n)=1\).

For every \(n\ge0\), the exact two-point count is
\[
\boxed{T_2(n)=4\cdot4^n+6\cdot3^n-8\cdot2^n+1.}
\]
Partition the types according to whether the tuple entries are increasing, decreasing, or incomparable. For each individual strict orientation the exact count is
\[
C(n)=4^n+2\cdot3^n-2\cdot2^n,
\]
while for incomparability it is
\[
I(n)=2\cdot4^n+2\cdot3^n-4\cdot2^n+1.
\]
Consequently, their respective proportions tend to \(1/4,1/4,1/2\). The ordinary generating function is
\[
\sum_{n\ge0}T_2(n)z^n=\frac4{1-4z}+\frac6{1-3z}-\frac8{1-2z}+\frac1{1-z}.
\]
Its minimal-order homogeneous linear recurrence has characteristic polynomial \((t-1)(t-2)(t-3)(t-4)\), since all four distinct exponential coefficients are nonzero. Initial counts are \(3,19,87,355,1383,5299\) at \(n=0,1,2,3,4,5\).

More generally, **for every fixed \(r\ge0\)** there is an explicit inclusion-exclusion formula expressing \(T_r(n)\) as a finite integer linear combination of \(j^n\) with integer \(0\le j\le3^r\). Thus the ordinary generating function of \(T_r(n)\) in \(n\) is rational and the sequence satisfies a constant-coefficient linear recurrence (with order depending on \(r\)). No efficiency claim uniform in growing \(r\) is made.

## Assumptions and scope
A partial order is represented by its strict, transitive, irreflexive relation. The generic poset is the Fraïssé limit of all finite posets, so every finite extension occurs and ultrahomogeneity identifies complete finite-tuple types with isomorphism classes **over the individually fixed, named base**. The tuple points are pairwise different and outside the base. By homogeneity, all named antichains of the same size have equal type counts.

We write \(\mathcal P_r\) for the set of all **labelled** partial orders on \(\{1,\ldots,r\}\). For \(Q\in\mathcal P_r\), let \(\Omega_Q\) consist of all disjoint pairs \((L,U)\) of subsets of \(Q\) satisfying: \(L\) is an upper set of \(Q\), \(U\) is a lower set of \(Q\), and every element of \(U\) is strictly below every element of \(L\) in \(Q\). The semantics for a new base point \(a\) are \(L=\{q:a<q\}\) and \(U=\{q:q<a\}\). Empty sets are permitted.

For every map \(\sigma:Q\to\{0,1\}\), define
\[
C_{Q,\sigma}=\{(L,U)\in\Omega_Q:\ L\subseteq\sigma^{-1}(1),\ U\subseteq\sigma^{-1}(0)\}.
\]
These are finite, explicitly enumerable sets. Here \(0^0=1\) means the cardinality of the unique empty sequence, including when an intersection is empty.

## Proof
**1. Finite-extension characterization.** Fix the induced labelled poset \(Q\) on the distinct tuple points. Each named parameter \(a\) has a relation to every tuple point: below, above, or incomparable. Transitivity involving \(a\) and points of \(Q\) holds exactly when its upper- and lower-neighbour sets form \((L_a,U_a)\in\Omega_Q\).

Because the parameters themselves are an antichain, two different base points cannot become comparable via an intermediate tuple point. This happens precisely if there is a tuple vertex lying above one named parameter and below another, i.e., precisely if
\[
\left(\bigcup_{a\in A_n}L_a\right)\cap\left(\bigcup_{a\in A_n}U_a\right)\ne\varnothing.
\]
Thus the necessary and sufficient global compatibility condition is **disjointness** of these two unions. Sufficiency follows by checking all possible two-step paths: paths internal to \(Q\) are handled by transitivity of \(Q\); paths through one parameter are handled by its upper/lower-set and cross-order conditions; paths from one base element to another through \(Q\) are ruled out by union disjointness. No other two-step path exists, since distinct base points have no direct relation.

**2. Fixed-arity exponential representation.** A tuple of local patterns satisfies the global compatibility condition if and only if each tuple point can be assigned one bit determining which of the two unions, if either, may contain it. Equivalently, there exists \(\sigma:Q\to\{0,1\}\) such that every parameter pattern lies in \(C_{Q,\sigma}\). Hence, writing \(N_Q(n)\) for the compatible assignments on \(n\) distinguishable base elements, we have the finite union \(\bigcup_{\sigma\in\{0,1\}^{Q}} C_{Q,\sigma}^{n}\). Inclusion-exclusion gives the **explicit** formula
\[
\boxed{N_Q(n)=\sum_{\varnothing\ne S\subseteq\{0,1\}^{Q}}(-1)^{|S|+1}
\left|\bigcap_{\sigma\in S}C_{Q,\sigma}\right|^n.}
\]
For fixed \(Q\), each intersection cardinality is an integer between zero and \(3^r\), as there are only three statuses per tuple vertex. Summing over the \(r\)-point labelled posets gives \(T_r(n)=\sum_{Q\in\mathcal P_r}N_Q(n)\), a finite integer combination of powers from this bounded set of bases, proving rationality and a recurrence for every fixed \(r\).

**3. Evaluating the two-point case.** There are exactly three labelled \(Q\): the two strict chains and the incomparable pair. For either strict-chain \(Q\), direct enumeration of its locally allowed relation patterns and the four orientation sets \(C_{Q,\sigma}\) gives the following **nonzero inclusion-exclusion base coefficients**:
\[
N_{\mathrm{chain}}(n)=4^n+2\cdot3^n-2\cdot2^n.
\]
For the incomparable \(Q\), the corresponding coefficients give
\[
N_{\mathrm{inc}}(n)=2\cdot4^n+2\cdot3^n-4\cdot2^n+1.
\]
For clarity, the exact coefficient dictionaries \(\{\text{base}:\text{coefficient}\}\) are \(\{2:-2,3:2,4:1\}\) for either chain, and \(\{1:1,2:-4,3:2,4:2\}\) for incomparability; all other coefficients vanish. These follow by enumerating the four possible maps \(\sigma\) and their fifteen nonempty selections in the displayed inclusion-exclusion formula, not by fitting a sequence. Adding twice the chain count and once the incomparable count yields the boxed formula. Dominant terms \(4^n\), \(4^n\), and \(2\cdot4^n\) prove the limiting frequencies. The distinct nonzero bases \(1,2,3,4\) prove that no recurrence of order less than four exists over characteristic zero.

## Verification
The standalone `verify_antichain.py` uses three independent implementations: (i) enumerating all base-to-tuple ternary relations and checking irreflexivity and transitivity on the resulting full relation, (ii) a state dynamic program over unions of local lower/upper masks, and (iii) finite inclusion-exclusion over the orientation sets. It covers every labelled poset of tuple sizes zero through three, base sizes zero through three; seven distinct labelled four-point posets with base sizes zero through two; direct two-tuple extension counts through five base points; and a longer two-tuple dynamic-program check through thirty base points. The embedded `verification_output.txt` reports 148 comparisons plus closed-form checks and `ALL_TESTS_PASS`. This is finite corroboration; the all-parameter theorem follows from the preceding proof.

Reproduction: in an ordinary Python 3 interpreter run `python verify_antichain.py` with both files in the same directory. No third-party Python packages, repository files, or external data are required.

## Relationship to prior work
Fraïssé theory establishes the homogeneous universal random poset and identifies finite tuple types with finite extensions. Dolinka and Mašulović, Lemma 3.3, explicitly encode **one-point** extensions of finite posets by lower/upper sets. That encoding is prior work, not a new claim here. Previously published exact random-poset 1-type counting likewise gives \(2^{n+1}-1\) over an antichain; this is a unary, not a pair-type, count.

Published work enumerating all labelled finite posets, including Brinkmann and McKay, treats unrestricted tuples without a specified labelled antichain. A published global tuple-orbit-profile theorem also counts no-parameter orbit types, corresponding to \(n=0\); it does not give the nonempty-parameter sequence or the general fixed-arity inclusion-exclusion representation. A published weak-order mapping-space recurrence counts order-preserving functions, not finite antichain extensions. These are object/implication comparisons rather than title-only exclusions.

Targeted published-record and broader literature searches under aliases including 'two-point extension of an antichain', 'random/generic poset complete pair types', 'finite posets with a fixed induced antichain', and 'antichain parameter orbit counts' did not identify either the displayed four-exponential identity or the arbitrary-fixed-arity representation. Unindexed equivalent enumeration formulas remain possible.

## Limitations
The count applies to injective tuples outside the named base; it does not directly count types permitting tuple repetitions or equality with base parameters. The reduction to finite poset extensions relies on ultrahomogeneity, not arbitrary posets. The general representation has combinatorially many labelled posets and orientation subsets as \(r\) grows; no tractable algorithm with variable \(r\) is asserted. The minimal order-four recurrence applies specifically to the two-point count. Originality and priority remain best-of-knowledge, not exhaustive assurances about historical enumeration literature. Independent review has not been performed.

## References
1. Igor Dolinka and Dragan Mašulović, 'A universality result for endomorphism monoids of some ultrahomogeneous structures', arXiv:1009.2892, first public 2010-09-15, Lemma 3.3 (one-point finite-poset extension). https://arxiv.org/abs/1009.2892.
2. Manfred Droste and Dietrich Kuske, 'On Random Relational Structures', Journal of Combinatorial Theory, Series A 102 (2003), 241–254, DOI 10.1016/S0097-3165(03)00004-9. https://eiche.theoinf.tu-ilmenau.de/kuske/Publications/random.pdf.
3. Gunnar Brinkmann and Brendan D. McKay, 'Posets on up to 16 Points', https://users.cecs.anu.edu.au/~bdm/papers/posets.pdf (finite labelled-poset enumeration).
4. 'Finite-parameter 1-type counting in the random poset is #P-complete', published record https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1.
5. 'Exact ordered-tuple orbit profiles of the five random-poset reduct groups', published record https://github.com/published-finding corpus/2026/tree/main/2026/9/30/SCOPE-exact-ordered-tuple-orbit-profiles-of-the-five-random-poset-redu--635ca0d5aff9.
