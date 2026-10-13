# Full-branching rigidity and rank spectra of uniquely retractable finite ultrametrics

## Finding

Let \((X,d)\) be a nonempty finite ultrametric space. A retraction onto \(\varnothing\ne Y\subseteq X\) is a map \(r:X\to Y\) with \(r|_Y=\mathrm{id}_Y\). It is **nonexpansive** if \(d(r(x),r(x'))\le d(x,x')\) for all \(x,x'\in X\). Every nonempty subset admits at least one such retraction; the question is when it is **unique**.

**Full-branching rigidity theorem.** A nonempty subset \(Y\subseteq X\) admits exactly one nonexpansive retraction if and only if, for every non-singleton closed ball \(B\) in the canonical hierarchy with \(|Y\cap B|\ge2\), every immediate child ball of \(B\) contains at least one point of \(Y\).

Let \(P_B(z)\) count these uniquely retractable nonempty subsets of each hierarchy ball \(B\) by their cardinalities. If \(B\) is a singleton, \(P_B(z)=z\). If \(B\) has immediate child balls \(B_1,\ldots,B_s\), where \(s\ge2\), then
\[
\boxed{P_B(z)=|B|z+\prod_{i=1}^{s}P_{B_i}(z).}
\]
This is a complete effective rank spectrum for every finite ultrametric, not merely the existence of retractions.

For the regular \(q\)-ary leaf ultrametric \(X_{q,h}=[q]^h\), with \(q\ge2\) and \(h\ge0\), let \(P_{q,h}(z)\) be its polynomial and \(U_{q,h}=P_{q,h}(1)\). Then
\[
P_{q,0}(z)=z,\quad P_{q,h}(z)=q^h z+P_{q,h-1}(z)^q,\qquad
U_{q,0}=1,\quad U_{q,h}=q^h+U_{q,h-1}^q.
\]
The support is **sharp**:
\[
\boxed{[z^k]P_{q,h}(z)>0\ \Longleftrightarrow\ 1\le k\le q^h\text{ and }k\equiv1\pmod{q-1}.}
\]
In particular, binary ultrametrics have uniquely retractable subsets of every rank, while larger branching arities exclude all other congruence classes.

For each fixed \(q\ge2\), the finite positive limit
\[
 c_q=\lim_{h\to\infty}\frac{\log U_{q,h}}{q^h}
\]
exists and satisfies \(0<c_q<\log2\). A uniformly chosen nonempty subset is therefore uniquely retractable with probability
\[
\boxed{\frac{U_{q,h}}{2^{q^h}-1}
=\exp\bigl(-[\log2-c_q+o(1)]q^h\bigr).}
\]
Thus retraction uniqueness is exponentially rare in the number of leaves, despite the fact that every nonempty subset is retractable.

## Assumptions and scope

All metric spaces in the theorem are finite and nonempty, distances are genuine ultrametric distances, and the maps are \(1\)-Lipschitz (not necessarily isometric). The canonical ball hierarchy is obtained recursively by partitioning any non-singleton ball \(B\) into equivalence classes for \(d(x,x')<\operatorname{diam}(B)\); these are its maximal proper child balls. The children are disjoint, exhaust \(B\), and number at least two. All cross-child distances equal \(\operatorname{diam}(B)\). For regular \(X_{q,h}\), points are words of length \(h\), and distance depends only on the longest common prefix; any strictly decreasing sequence of positive scale values gives the same nonexpansive maps.

A **uniquely retractable image** means a *concrete* nonempty subset \(Y\) with precisely one idempotent nonexpansive endomorphism having image \(Y\). This is stronger than saying that \(Y\) is a retract, and different subsets are counted separately. The results do not concern arbitrary metric spaces, infinite ultrametrics, or arbitrary Lipschitz constants.

## Proof

**Step 1: existence for all nonempty subsets.** Induct on the hierarchy. If a ball \(B\) meets \(Y\) in a single point, take the constant retraction there. Otherwise, choose any occupied child balls and recursively retract each occupied child onto its part of \(Y\). On each unoccupied child use a constant value in \(Y\). Within occupied children nonexpansiveness is inductive; across different children every original distance is \(\operatorname{diam}(B)\), an upper bound for all image distances. This defines a retraction. This existence is consistent with the prior finite-ultrametric retraction theorem of Al-Sabti and earlier polymorphism-homogeneity results; existence itself is not claimed as new.

**Step 2: root dichotomy and necessity.** If \(|Y|=1\), the constant map is the only possible retraction. Suppose \(|Y|\ge2\) and an immediate child \(C\) of \(B\) misses \(Y\). Fix any retractions on occupied children using Step 1 and any constant maps on other unoccupied children. On \(C\), choose either of two distinct points of \(Y\) as its constant image. Both extensions are nonexpansive because cross-child distances in the source equal \(\operatorname{diam}(B)\); they are distinct retractions. Hence uniqueness forces every child of \(B\) to meet \(Y\) whenever \(|Y\cap B|\ge2\).

**Step 3: sufficiency and recursive independence.** If every child \(B_i\) meets \(Y\), then any nonexpansive retraction must carry \(B_i\) into itself: choose \(y_i\in B_i\cap Y\); for any \(x\in B_i\), the inequality \(d(r(x),y_i)\le d(x,y_i)<\operatorname{diam}(B)\) forces \(r(x)\in B_i\). Its restrictions are exactly independent nonexpansive retractions \(B_i\to Y\cap B_i\). Induction therefore proves the stated criterion and the polynomial product term. All singletons in \(B\) contribute the separate term \(|B|z\). This gives the exact recursion for arbitrary finite ultrametrics.

**Step 4: regular rank support.** In the regular \(q\)-ary case the recursion is \(P_{q,h}(z)=q^h z+P_{q,h-1}(z)^q\). Inductively the exponent support of \(P_{q,h-1}\) is every integer \(1+(q-1)t\) with \(0\le t\le(q^{h-1}-1)/(q-1)\). Every sum of \(q\) such integers occurs, and these sums are exactly the integers \(q+(q-1)t\) for \(0\le t\le q(q^{h-1}-1)/(q-1)\). Adjoining exponent one gives every permissible exponent through \(q^h\) and no others.

**Step 5: strict entropy bounds.** The recurrence implies \(U_{q,h}\ge U_{q,h-1}^q\); hence \(q^{-h}\log U_{q,h}\) increases and is bounded by \(\log2\), since there are fewer than \(2^{q^h}\) nonempty subsets. Its limit is positive, at least \(q^{-1}\log(q+1)\). To make the upper bound strict, observe that every bottom ball of \(q\) leaves in a globally uniquely retractable subset has intersection either empty, a singleton, or the entire bottom ball. For \(q\ge3\), there are only \(q+2<2^q\) possibilities; disjoint bottom balls imply \(U_{q,h}\le(q+2)^{q^{h-1}}\). For \(q=2\), each bottom two-level ball of four leaves has \(1+U_{2,2}=14<16\) allowed intersections, so \(U_{2,h}\le14^{2^{h-2}}\) when \(h\ge2\). Consequently \(c_q\le\log(q+2)/q<\log2\) for \(q\ge3\) and \(c_2\le\log14/4<\log2\). Subtracting the logarithm of the total \(2^{q^h}-1\) subsets gives the probability asymptotic.

## Verification

The standalone file `verify.py` constructs every unordered rooted branching hierarchy with at most five leaves, forms an explicit ultrametric, exhaustively enumerates all self-maps, and identifies the nonexpansive idempotents by direct pairwise distance and idempotence tests. It then compares, for **every nonempty concrete image subset**, the actual number of retractions to the full-branching criterion and independently checks each hierarchy's rank polynomial. Three additional direct cases and regular recurrences for \(q=2,3,4,5\), \(h\le4\), were tested. Running `python3 verify.py` yielded:

`VERIFY_OK 24 finite ultrametric shapes; 550 image-subset tests; 85778 total map candidates; 1887 idempotent maps; regular rank recurrences q=2..5,d=1..4`

These finite tests are not substitutes for Steps 1–5; no formal proof assistant or external mathematical certification was used.

## Relationship to prior work

Al-Sabti (2024) proves existence of nonexpansive retractions onto arbitrary nonempty subsets of finite-spectrum ultrametrics and studies homomorphism extension and dense locally finite endomorphism submonoids. Pantić and Pech (2022) independently establish finite-ultrametric homomorphism-homogeneity. Neither existence result by itself determines whether a given retract has **one** nonexpansive projection, its complete rank polynomial, the regular-arity congruence support, or its asymptotic frequency.

Dolinka and East (2014/2016), especially their Propositions 3.1–3.2, enumerate idempotents of transformations preserving **one** uniform partition. Their formulas encompass a shallow special case of the hierarchical phenomenon, so no novelty is claimed for simple one-partition idempotent enumeration. The claim here is the **arbitrary canonical ball-tree uniqueness characterization** and its rank/entropy consequences, including nonuniform finite hierarchies and unrestricted depth. The polynomial recursion resembles classical full-branching tree enumeration, whose elementary multiplication principle is not claimed as new in isolation.

## Limitations

The originality comparison checked the full Al-Sabti text as mirrored openly, Dolinka–East's full arXiv HTML version, available descriptions of Pantić–Pech, exact-phrase/alias searches, and a mathematical results index. Earlier unindexed work on tree endomorphisms or unique Lipschitz projections could imply an equivalent criterion. Pantić–Pech's full text was not openly accessible during this review, so its theorem-level uniqueness coverage was not established; its indexed abstract addresses existence and polymorphism-homogeneity rather than counting. The asymptotic constant \(c_q\) is defined as a convergent limit; no closed form is asserted. The rank polynomial counts concrete image subsets, not isometry types. Independent mathematical audit has not been performed.

## References

1. K. Al-Sabti, *On the Endomorphism Monoid of Certain Ultrametric Speces*, Contemporary Mathematics **5** (2024), 2983–2989, first published 2024-08-08, DOI: 10.37256/cm.5320243750. Publisher record: https://ojs.wiserpub.com/index.php/CM/article/view/3750 . Open full-text reproduction: https://www.researchgate.net/publication/383026717_On_the_Endomorphism_Monoid_of_Certain_Ultrametric_Speces .
2. B. Pantić and M. Pech, *Towards the Classification of Polymorphism-homogeneous Metric Spaces*, Journal of Multiple-Valued Logic and Soft Computing **38** (2022), 153–182. https://www.researchgate.net/publication/361582217_Towards_the_Classification_of_Polymorphism-homogeneous_Metric_Spaces .
3. I. Dolinka and J. East, *Idempotent Generation in the Endomorphism Monoid of a Uniform Partition*, Communications in Algebra **44** (2016), 5179–5198, arXiv:1407.3312 (first posted 2014-07-11), https://arxiv.org/html/1407.3312v2 .
