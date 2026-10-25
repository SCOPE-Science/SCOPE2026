# One-atom modal probability distortion: sharp branching rigidity and the five-world cutoff

## Finding

Let \(W\) be a labelled set of \(n\ge4\) worlds. For an arbitrary accessibility relation \(R\subseteq W\times W\), define its normal additive possibility operator by
\[
\Diamond_R A=\{x\in W:\exists y\in A\ (xRy)\},\qquad A\subseteq W.
\]
Equip \(W\) with uniform probability \(\mu(A)=|A|/n\), and define the **one-step modal probability distortion**
\[
\Delta(R)=\max_{A\subseteq W}\left|\mu(\Diamond_R A)-\mu(A)\right|.
\]

**Theorem (sharp one-atom extremizers).** For every integer \(n\ge4\):

1. Among all relations satisfying \(\Delta(R)\le 1/n\), the maximum number of ordered accessibility pairs is exactly \(2n\).
2. If \(n\ge5\), a relation attains \(2n\) pairs under this distortion bound **if and only if** there is a unique world \(c\in W\) and a function \(f:W\to W\setminus\{c\}\) with \(|f(W)|\ge n-2\) such that
   \[
   \Diamond_R A=\{c\}\cup f(A)\quad(A\ne\varnothing),\qquad \Diamond_R\varnothing=\varnothing.
   \]
   Equivalently, every target world \(y\) has precisely the two predecessors \(c\) and \(f(y)\). All \(n\ge5\) extremizers have a universal predecessor \(c\), and their number on a fixed labelled \(W\) is exactly
   \[
   \boxed{n!\left(\binom n2+\binom n3+3\binom n4\right)}.
   \]
3. The bound \(n\ge5\) in this rigidity statement is sharp. At \(n=4\) there are exactly **456** labelled extremizers, of which **312** have the common-predecessor form in (2) and **144** do not. The exceptional 144 are obtained by choosing a three-element subset of \(W\), then assigning the four target worlds surjectively to its three distinct two-element subsets, interpreted as their predecessor sets.

For contrast, exact probability preservation \(\Delta(R)=0\) forces \(R\) to be a permutation graph, with exactly \(n!\) choices. Thus permitting one atom's probability error uniformly over **all** propositions changes the sharp accessibility density from \(n\) to \(2n\), yet forces a unique universal predecessor at maximal density for \(n\ge5\).

## Assumptions and scope

The frame is finite, labelled, and unrestricted: reflexive pairs are permitted, and neither seriality nor transitivity is assumed. Every subset of \(W\) is an admissible valuation of a propositional variable. The operator is the standard Kripke **existential predecessor** modality, not a stochastic transition kernel: the probabilities of input and output sets are compared under the same uniform atomic measure. No independence or random sampling hypothesis is used.

The distortion bound \(1/n\) means exactly one probability atom under this measure. It is required for every proposition, not merely for singleton or designated valuations. If \(R\) is oriented as \(xRy\), its column at \(y\) is the predecessor set \(P_y=\Diamond_R\{y\}\). Reversing the orientation throughout gives the dual statement for an existential successor operator.

## Proof

**Step 1: upper bound and its attainment.** From the bound on the singleton \(\{y\}\) we obtain
\[
\left||P_y|-1\right|\le1,
\]
so \(|P_y|\le2\) for every \(y\). Since \(|R|=\sum_{y\in W}|P_y|\), necessarily \(|R|\le2n\).

This is attained for all \(n\ge4\). Choose \(c\in W\), and any function \(f:W\to W\setminus\{c\}\) whose image contains at least \(n-2\) worlds; such functions exist because the codomain has \(n-1\) elements. Define \(P_y=\{c,f(y)\}\). For nonempty \(A\), let \(m=|A|\) and \(d=|f(A)|\). The number \(m-d\) of repeated values within \(A\) lies between \(0\) and \(n-|f(W)|\le2\). Consequently
\[
|\Diamond_R A|-|A|=1+d-m=1-(m-d)\in\{-1,0,1\}.
\]
The empty set has zero distortion. Hence \(\Delta(R)\le1/n\), and every column has two pairs, giving \(2n\) pairs.

**Step 2: intersection rigidity.** Any extremizer has \(|P_y|=2\) for all \(y\). For two distinct target worlds \(y,z\), the same distortion bound on \(\{y,z\}\) implies
\[
|P_y\cup P_z|\le3.
\]
Therefore all two-element predecessor sets intersect pairwise. We use the following elementary lemma, including repeated members: a pairwise-intersecting collection of two-element subsets either has a point common to every member or all its members lie among the three edges of one triangle. To prove it, take distinct members \(\{a,b\}\) and \(\{a,d\}\) with \(b\ne d\). If their common point \(a\) is not common to the collection, a member avoiding \(a\) must be \(\{b,d\}\); any two-element set intersecting all three is necessarily one of these same three edges. The degenerate case of only one distinct member has an obvious common point.

But \(A=W\) gives \(|\Diamond_R W|\ge n-1\). When \(n\ge5\), a triangle would supply at most three output worlds, contradicting \(n-1\ge4\). Thus there is a common predecessor \(c\) and \(P_y=\{c,f(y)\}\) with \(f(y)\ne c\) for every \(y\). Applying the lower distortion bound to \(A=W\), we have
\[
1+|f(W)|\ge n-1,
\]
so \(|f(W)|\ge n-2\). Conversely Step 1 proves this condition sufficient. As the image contains at least two distinct leaves, the common point is unique.

**Step 3: count the common-predecessor extremizers.** For \(n\ge4\), each common-predecessor extremizer has a unique \(c\), so we count functions \(f:W\to W\setminus\{c\}\) with image size \(n-1\) or \(n-2\). Write \(S(n,k)\) for a Stirling number of the second kind. For each choice of \(c\), the number is
\[
(n-1)!S(n,n-1)+(n-1)(n-2)!S(n,n-2).
\]
The partition identities
\[
S(n,n-1)=\binom n2,\qquad S(n,n-2)=\binom n3+3\binom n4
\]
follow by identifying a single merged pair, respectively one triple or two disjoint pairs. Multiplication by the \(n\) choices of \(c\) gives the stated \(n!\)-formula.

**Step 4: exact four-world exception.** For \(n=4\), the same intersection lemma permits a second case: no common predecessor, so the predecessor pairs are drawn from the three edges of a triangle. All three edge types must occur; otherwise the pairs have a common endpoint. Four targets assigned to three edge types must therefore have multiplicities \((2,1,1)\). Every one-target union has size two; a two-target union has size two or three; any three-target union has size three; and the all-target union has size three. Each differs from the target-set cardinality by at most one. Conversely these are the only non-common-predecessor extremizers by Step 2. Choose the three output worlds in \(\binom43=4\) ways, and surjectively assign four labelled targets to the three edges in \(3!S(4,3)=36\) ways. This gives \(144\) exceptions. The common-predecessor formula at \(n=4\) gives \(4!(6+4+3)=312\), for a total \(456\).

**Step 5: exact-preservation boundary.** If \(\Delta(R)=0\), all singleton predecessor sets have size one. All pairwise unions must have size two; hence the singleton predecessors are distinct, so the relation is a permutation graph. Conversely each permutation preserves the cardinality of all inverse images and has zero distortion. This last elementary boundary is background context, not a separate priority claim.

## Verification

The standalone `checker.py` directly implements \(\Diamond_R\) and its distortion over every input subset. It independently exhausts **every** binary relation on one, two, three and four labelled worlds (respectively \(2,16,512,65536\) relations), and finds the expected maximum edge counts and permutation counts at exact zero distortion. At four worlds there are exactly \(456\) eight-edge relations under the one-atom bound.

It further exhausts all assignments of two-element predecessor sets at four and five worlds (respectively \(6^4=1296\) and \(10^5=100000\) possibilities), checking the bound on every subset. At four worlds it finds \(312\) star and \(144\) non-star extremizers; at five worlds it finds exactly \(4200\), all with a unique common predecessor, agreeing with the closed formula. A separately programmed Stirling recurrence checks the symbolic enumeration identity through twelve worlds. Execution prints `ALL_CHECKS_OK`.

The unrestricted theorem follows from the mathematical proof. Finite enumeration alone is not used to infer the five-world cutoff or the general enumeration formula.

## Relationship to prior work

Bezhanishvili, de Groot and Moss (2026) study normal additive modal operators on measurable algebras and marked measurable frames, including measure-preserving dynamical-system examples. Their modal Loomis–Sikorski theorem concerns representation and countable-join preservation; it does not assert a sharp all-proposition numerical probability-distortion bound. A subsequent mathematical note on finite marked-modal-measurable quotients identifies a partial-functional relation under **meet preservation**. That stronger algebraic hypothesis rules out the branching \(2n\)-edge extremizers here; it cannot subsume the present near-preservation classification.

Cosyns (October 2026) develops qualitative links between probability-zero/probability-one events and modal readings in Stone probability spaces. The present theorem asks a distinct quantitative question about the probability **difference** between a proposition and its Kripke possibility image, uniformly over all propositions in the finite atomic setting. Neither inspected source contains the sharp five-world star/triangle threshold or its complete labelled census.

The elementary lemma about intersecting two-element sets and the Stirling identities are standard tools and are **not** claimed as new. The claimed contribution is their exact quantitative modal-probability extremal synthesis, including the sharp exceptional four-world layer and the closed labelled count. Indexed searches for numerical modal distortion, almost measure-preserving relations, relational neighbourhood discrepancy and equivalent union-size formulations did not locate a directly covering theorem. This does not constitute a proof of absolute priority.

## Limitations

The classification is for the extremal number of pairs at one specific uniform error tolerance, not a characterization of every near-preserving relation. It does not extend the count automatically to nonuniform atomic probabilities, infinite spaces, countable-additive Markov kernels or the marked-modal-measurable quotient semantics. The sources motivate the compatibility question but the theorem is not asserted as a consequence within their more specialized model classes.

The result uses a known two-uniform intersection lemma; closely related set-system results could express the same extremal classification under different terminology. That is the main residual priority risk. A previously published mathematical note on finite marked modal quotients and several classical neighbourhood-hypergraph sources were considered; no identified implication settles the present quantitative extremizers. Independent external validation has not been performed.

## References

1. N. Bezhanishvili, J. de Groot, L. S. Moss, *Modal Measurable Logics via a Modal Loomis-Sikorski Representation Theorem*, Electronic Proceedings in Theoretical Computer Science 447 (2026), 158–172; arXiv:2606.31862, first public posting 2026-06-30. https://arxiv.org/abs/2606.31862
2. L. Cosyns, *On the foundations of logic and probability, II. Modal probability spaces*, arXiv:2610.17049v2 (2026); first public posting 2026-10-12. https://arxiv.org/html/2610.17049v2
3. E. Boros, V. Gurvich, I. Zverovich, *Neighborhood hypergraphs of bipartite graphs*, Journal of Graph Theory 58 (2008), 69–95, DOI:10.1002/jgt.20293. The available abstract concerns neighbourhood-hypergraph recognition, not numerical probability distortion.
