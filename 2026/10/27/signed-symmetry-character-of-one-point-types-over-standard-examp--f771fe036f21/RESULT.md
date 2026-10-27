# Signed symmetry character of one-point types over standard-example posets

## Finding

Let \(n\ge2\), and let \(S_n\) be the standard-example partial order on \(2n\) distinct elements \(a_1,\ldots,a_n,b_1,\ldots,b_n\), with strict comparisons \(a_i<b_j\) exactly when \(i\ne j\). Embed it as a finite induced parameter structure in the countable universal homogeneous partial order \(\mathbb P\). Write \(\mathcal T_n\) for the set of complete **nonalgebraic** one-types over its individually named parameters. Equivalently, \(\mathcal T_n\) consists of order diagrams of one new point over \(S_n\) that are consistent with transitivity.

Simultaneous permutation of the index labels gives an action of \(S_n^{\mathrm{sym}}\), the symmetric group of degree \(n\), on \(\mathcal T_n\). Exchanging \(a_i\) with \(b_i\) while reversing the partial order induces a commuting involution \(\tau\) on extension types. Together they act as \(G_n\cong S_n^{\mathrm{sym}}\times C_2\). This is an action on diagrams, including order reversal; it does not assert that \(\tau\) is an order-preserving automorphism of \(\mathbb P\).

For a permutation \(\sigma\in S_n^{\mathrm{sym}}\), let \(c(\sigma)\) be its number of cycles (including fixed points), \(f(\sigma)\) its number of fixed points, and \(e(\sigma)\) its number of **even-length cycles**. Then the complete fixed-point character of the action is

\[
|\operatorname{Fix}_{\mathcal T_n}(\sigma)|
=3^{c(\sigma)}+2^{c(\sigma)+1}+2f(\sigma)-2,
\qquad
|\operatorname{Fix}_{\mathcal T_n}(\sigma\tau)|
=3^{e(\sigma)}.
\]

Consequently the named and symmetry-reduced counts are, respectively,

\[
|\mathcal T_n|=3^n+2^{n+1}+2n-2,
\qquad
|\mathcal T_n/S_n^{\mathrm{sym}}|=\frac{(n+1)(n+6)}2,
\]

\[
|\mathcal T_n/G_n|=2n+2+\left\lfloor\frac{n^2}{4}\right\rfloor.
\]

The first character depends only on the number of cycles and fixed points, while the order-duality character depends only on the number of even cycles. Hence exponentially many parameter-labelled one-types collapse to quadratically many symmetry classes. The named scalar count is obtainable from existing general height-two counting theory; the **equivariant fixed-character, parity law, and full orbit classifications** are the specific assertions here.

## Assumptions and scope

The order is strict and the parameter elements are distinct. The bound \(n\ge2\) excludes the degenerate case in which the two displayed levels are the same undifferentiated antichain. Types of equality with a named parameter are excluded. The parameter order is induced, so noncomparabilities are genuine. Every admissible finite one-point extension is realized in \(\mathbb P\), and homogeneity identifies precisely those realizations with the same order diagram over the fixed parameter set.

The label-permutation action permutes both indices of each pair \((a_i,b_i)\). The duality action is defined combinatorially on order diagrams by exchanging lower and upper relations and swapping the two parameter levels; it is not an additional order-preserving stabilizer action. The full \(G_n\)-orbit count includes this explicitly declared order-dual equivalence.

## Proof

**1. One-point extension criterion.** Given an external point \(x\), define \(L=\{p\in S_n:p<x\}\) and \(U=\{p\in S_n:x<p\}\). Precisely the following pairs occur: \(L\) is a lower set, \(U\) an upper set, \(L\cap U=\varnothing\), and \(l<u\) holds in \(S_n\) for every \(l\in L\) and \(u\in U\). Necessity is immediate from transitivity. Conversely, declare \(l<x\) exactly for \(l\in L\), and \(x<u\) exactly for \(u\in U\), retaining all original comparisons. The four conditions ensure that transitive closure neither identifies two points nor adds any comparison absent from the declared diagram. The resulting finite poset is a one-point extension of \(S_n\). Homogeneity of \(\mathbb P\) proves that these pairs enumerate complete nonalgebraic one-types.

**2. Equivariant partition.** Every lower set has the form \(L=X\cup Y\), where \(X\subseteq A=\{a_i\}\) and \(Y\subseteq B=\{b_i\}\). If \(Y=\varnothing\), \(X\) is arbitrary; if \(X=A\), \(Y\) is arbitrary; the remaining lower sets containing upper-level elements are exactly \(X=A\setminus\{a_i\}\), \(Y=\{b_i\}\), for some index \(i\). This is an exhaustive **disjoint** decomposition if the second class is required to have \(Y\ne\varnothing\):

(a) \(Y=\varnothing\), with \(2^n\) choices; (b) \(X=A\) and \(Y\ne\varnothing\), with \(2^n-1\) choices; (c) \(X=A\setminus\{a_i\}\), \(Y=\{b_i\}\), with \(n\) choices.

The same description applies dually to upper sets. Let \(c=c(\sigma)\) and \(f=f(\sigma)\). The numbers of \(\sigma\)-invariant downsets in classes (a), (b), (c) are \(2^c\), \(2^c-1\), and \(f\), so there are \(2^{c+1}+f-1\) fixed lower sets (and equally many fixed upper sets).

When both \(L,U\) are nonempty, each element of \(L\) must be minimal and each element of \(U\) maximal: otherwise the condition \(L<U\) fails. Thus mixed types correspond exactly to an ordered pair of **nonempty disjoint index subsets** \(X,Y\subseteq[n]\), by \(L=\{a_i:i\in X\}\) and \(U=\{b_j:j\in Y\}\). Indeed \(a_i<b_j\) holds exactly for unequal indices. Such a pair is \(\sigma\)-invariant if and only if each cycle is assigned one of three statuses (in \(X\), in \(Y\), in neither), with both first statuses represented. Inclusion-exclusion gives \(3^c-2^{c+1}+1\) invariant mixed types.

The remaining one-sided types have \(L=\varnothing\) or \(U=\varnothing\). There are twice \(2^{c+1}+f-1\) invariant choices, minus one for the common empty pair. Adding the mixed count gives

\[
|\operatorname{Fix}(\sigma)|
=2(2^{c+1}+f-1)-1+3^c-2^{c+1}+1
=3^c+2^{c+1}+2f-2.
\]

**3. Duality and even-cycle law.** Let \(\delta(a_i)=b_i\) and \(\delta(b_i)=a_i\), an order-reversing bijection of \(S_n\). The induced involution on types is \(\tau(L,U)=(\delta(U),\delta(L))\). A one-sided type is sent to the opposite one-sided class; among these only \((\varnothing,\varnothing)\) is fixed by \(\sigma\tau\). A mixed type represented by \((X,Y)\) is fixed by \(\sigma\tau\) exactly when \(X=\sigma(Y)\) and \(Y=\sigma(X)\). Equivalently, \(X\) is invariant under \(\sigma^2\), \(Y=\sigma(X)\), and \(X\cap\sigma(X)=\varnothing\).

On an odd-length cycle of \(\sigma\), invariance under \(\sigma^2\) forces \(X\) to occupy either all or none of that cycle; disjointness forces none. On an even-length cycle, \(\sigma^2\) has two alternating orbits, so \(X\) may occupy neither, the even-position half, or the odd-position half. Hence there are \(3^{e(\sigma)}\) valid choices including \(X=Y=\varnothing\). The latter does not define a mixed type, but it is replaced by the one fixed empty-pair type. Therefore \(|\operatorname{Fix}(\sigma\tau)|=3^{e(\sigma)}\).

**4. Exact orbit classification.** The first two downset classes contain \(n+1\) and \(n\) index-permutation orbits, determined by subset cardinality, while the exceptional class (c) contributes one. Thus lower sets have exactly \(2n+2\) orbits, as do upper sets. One-sided types therefore give \(4n+3\) orbits under \(S_n^{\mathrm{sym}}\), after identifying the common empty pair. Mixed types have one orbit per ordered pair \((k,l)\) of positive subset sizes satisfying \(k+l\le n\), giving \(n(n-1)/2\) more. This proves \((n+1)(n+6)/2\) index-permutation orbits. Under duality the two one-sided classes are paired, leaving \(2n+2\) orbits, and the mixed sizes \((k,l)\) and \((l,k)\) are identified. The number of unordered positive pairs with sum at most \(n\) is \(\lfloor n^2/4\rfloor\), proving the final formula. The scalar type count is the identity-permutation case of the first character formula.

## Verification

A separate standard-library Python checker, `verify.py`, constructs the strict comparability relation on all \(2n\) parameters, enumerates lower and upper subsets by direct closure tests, tests all pairwise \(L<U\) constraints, and applies every permutation of the \(n\) indices. It does not use the symbolic three-class classification in the proof. For \(2\le n\le6\), it checked the cardinalities and both characters for all \(872\) permutations in total. It also directly enumerated symmetry orbits for \(2\le n\le4\) and independently verified both Burnside orbit formulas. The actual execution printed `ALL_TESTS_PASS` (see `verification-output.txt`). These finite checks are corroboration and are not substituted for the general proof.

## Relationship to prior work

Dushnik–Miller standard examples are extremal finite posets for order dimension. Biró–Hamburger–Pór (2013), especially its Introduction and Sections 2–4, studies the dimension implications of avoiding such examples; Biró–Hamburger–Pór–Trotter (2014) develops sharp dimension containment results. Neither inspected manuscript states the fixed one-type characters of the present theorem. Fraïssé homogeneity and the one-point-extension correspondence are standard background. Earlier general height-two one-type counting formulas imply the **scalar** special-case value \(|\mathcal T_n|\); the contribution asserted here is the exact symmetry action, its fixed-point character under both automorphisms and order duality, and the complete orbit distribution.

The distinction from general finite-poset one-type counting is substantive: a non-equivariant total count alone cannot determine how many types each permutation or order-duality operation fixes. The parity-only twisted law provides genuinely finer information than scalar enumeration. No claim is made that the classical standard examples or the basic ideal/filter parametrization are new.

## Limitations

The result concerns one new element and the standard-example family, not higher-arity types or arbitrary height-two parameter posets. The involution \(\tau\) reverses the order, so \(G_n\) is an action on extension diagrams, not an order-preserving automorphism group of the named structure. Neither the finite checker nor the literature searches prove global novelty. Specialized or unindexed studies of equivariant one-point extensions could contain equivalent statements; independent scientific audit has not been performed.

## References

1. C. Biró, P. Hamburger and A. Pór, *Standard Examples as Subposets of Posets*, arXiv:1311.6518v1, first posted 26 November 2013, https://arxiv.org/html/1311.6518v1.
2. C. Biró, P. Hamburger, A. Pór and W. T. Trotter, *Forcing Posets with Large Dimension to Contain Large Standard Examples*, arXiv:1402.5113, first posted 20 February 2014, https://arxiv.org/abs/1402.5113.
3. M. Droste and D. Kuske, *On random relational structures*, J. Combin. Theory Ser. A 102 (2003), 241–254, DOI 10.1016/S0097-3165(03)00004-9. Cited only for the general homogeneous-poset one-point-extension background.
4. P. J. Cameron and D. C. Lockett, *Posets, homomorphisms and homogeneity*, Discrete Math. 310 (2010), 604–613, DOI 10.1016/j.disc.2009.04.027. Background on homogeneity notions.
