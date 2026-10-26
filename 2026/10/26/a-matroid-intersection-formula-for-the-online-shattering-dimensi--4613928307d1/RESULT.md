# A matroid-intersection formula for the online shattering dimension of basis indicators

## Finding
Let \(M=(E,\mathcal I)\) be any **finite matroid**, \(r\) its rank function, \(M^*\) its dual, and \(\mathcal H(M)=\{h_B:B\in\mathcal B(M)\}\) its class of basis-incidence functions, with \(h_B(e)=1\) precisely when \(e\in B\). The query domain is \(E\). Then
\[
\boxed{\operatorname{Ldim}(\mathcal H(M))
=\operatorname{VCdim}(\mathcal H(M))
=\max\{|F|:F\in\mathcal I(M)\cap\mathcal I(M^*)\}}
\]
and these quantities equal both rank min–max expressions
\[
\boxed{\min_{A\subseteq E}\bigl(r(A)+r^*(E\setminus A)\bigr)
=|E|-r(E)+\min_{A\subseteq E}\bigl(2r(A)-|A|\bigr).}
\]

Moreover, if \(e\in E\) is neither a loop nor a coloop, the two nonempty version spaces obtained after querying \(e\) are identified with the basis classes of \(M\setminus e\) and \(M/e\), and their dimensions satisfy the **exact one-step dichotomy**
\[
\boxed{\min\{\operatorname{Ldim}(\mathcal H(M\setminus e)),
\operatorname{Ldim}(\mathcal H(M/e))\}
=\operatorname{Ldim}(\mathcal H(M))-1.}
\]
In particular, choosing a prediction whose consistent version space has larger dimension gives an optimal worst-case realizable online mistake bound; the bound is computable by matroid intersection without listing all bases.

For the graphic matroid of a finite connected graph \(G\), the common value is the greatest cardinality of an edge set \(F\) that is **a forest and whose deletion leaves \(G\) connected**. Thus the worst-case online mistake complexity of an unknown spanning tree, under individual edge-membership examples, equals this forest-with-connected-complement maximum.

## Assumptions and scope
A finite matroid is given by its hereditary and augmentation axioms on a finite set \(E\). The dual matroid \(M^*\) has bases \(E\setminus B\) for bases \(B\) of \(M\). Loops, coloops, parallel elements, disconnected matroids, rank-zero matroids, and the empty ground set are allowed.

VC dimension is the largest cardinality of a fixed coordinate set on which all binary assignments are realized by concepts in \(\mathcal H(M)\). Littlestone dimension is the greatest depth of a complete binary *adaptive* coordinate-query tree for which every labeled root-to-leaf path is realized by some concept. In the depth-zero case, a nonempty singleton concept class has dimension zero. All queries ask membership of an element of \(E\); no independence, rank, equivalence, noisy, or randomized query is part of the claim.

Write \(m=|E|\), \(R=r(E)\), and, for \(A\subseteq E\), put \(\phi(A)=2r(A)-|A|\). The statement is uniform over all finite matroids, without representability or simplicity assumptions.

## Proof
**1. Exact static shattering criterion.** A coordinate set \(F\subseteq E\) is VC-shattered by the basis indicators if and only if it is independent in both \(M\) and \(M^*\). Indeed, the all-one assignment requires a basis containing \(F\), so \(F\) is independent in \(M\). The all-zero assignment requires a basis disjoint from \(F\), equivalently \(F\) is independent in \(M^*\).

Conversely, suppose both conditions hold. Choose a basis \(B_0\) disjoint from \(F\), which exists by dual independence. Given any requested one-set \(I\subseteq F\), \(I\) is independent in \(M\). The restriction of \(M\) to \(B_0\cup I\) has full rank because it contains \(B_0\). The matroid augmentation axiom therefore extends \(I\) to a basis \(B\subseteq B_0\cup I\). This basis intersects \(F\) in exactly \(I\). Every assignment to \(F\) is realized, proving the converse.

Consequently the VC dimension is the maximum cardinality of a common independent set of \(M\) and \(M^*\). Edmonds' matroid-intersection min–max theorem supplies
\[
\nu(M):=\operatorname{VCdim}(\mathcal H(M))
=\min_{A\subseteq E}\bigl(r(A)+r^*(E\setminus A)\bigr).
\]
The dual-rank identity \(r^*(E\setminus A)=m-|A|-R+r(A)\) yields
\[
\nu(M)=m-R+\min_{A\subseteq E}\phi(A).
\]
These identities hold for all boundary cases because the basis family is always nonempty.

**2. Exact minor split for the static invariant.** Fix an element \(e\) that is neither a loop nor a coloop. Then \(M\setminus e\) has ground size \(m-1\) and rank \(R\), while \(M/e\) has ground size \(m-1\) and rank \(R-1\). For every \(B\subseteq E\setminus\{e\}\),
\[
r_{M\setminus e}(B)=r(B),\qquad r_{M/e}(B)=r(B\cup\{e\})-1.
\]
Applying the preceding rank formula separately to the two minors gives
\[
\begin{aligned}
\nu(M\setminus e)
&=m-R-1+\min_{\substack{A\subseteq E\\e\notin A}}\phi(A),\\
\nu(M/e)
&=m-R-1+\min_{\substack{A\subseteq E\\e\in A}}\phi(A).
\end{aligned}
\]
The two optimization domains partition \(2^E\); hence
\[
\min\{\nu(M\setminus e),\nu(M/e)\}=\nu(M)-1.\tag{1}
\]
No minimizer needs to be unique and this equality holds for *every* nonconstant coordinate \(e\).

**3. Adaptive upper bound by induction.** Induct on \(m\) to show \(\operatorname{Ldim}(\mathcal H(M))\le\nu(M)\). If no coordinate is nonconstant across the basis family, the family is a singleton, and both dimensions are zero. This includes the empty ground set.

Otherwise a depth-positive shattered tree has a root query \(e\) that is neither a loop nor a coloop. Its zero-labeled branch is the class of bases of \(M\setminus e\), and its one-labeled branch, after deleting the fixed coordinate \(e\), is the class of bases of \(M/e\). For a shattered tree of depth \(d\), both branches must have Littlestone dimension at least \(d-1\). By the induction hypothesis and (1),
\[
d-1\le \min\{\nu(M\setminus e),\nu(M/e)\}=\nu(M)-1,
\]
so \(d\le\nu(M)\). Since any fixed VC-shattered coordinate set also gives a complete adaptive tree (use its coordinates in a fixed order), \(\operatorname{Ldim}\ge\operatorname{VCdim}=\nu(M)\). Equality follows. Substituting the established equality into (1) gives the asserted exact one-step dichotomy.

**4. Graphic specialization and computability.** In a connected graph, the graphic matroid's bases are spanning trees. Independence of \(F\) in that matroid means \(F\) is a forest. Independence of \(F\) in the dual means some spanning tree avoids \(F\), equivalently the graph obtained by deleting \(F\) remains connected. The general theorem therefore gives the stated graphic formula.

With an independence oracle for \(M\), dual independence of \(F\) can be checked by computing whether \(r(E\setminus F)=R\), using greedy rank evaluation. Thus ordinary polynomial-time matroid intersection on \(M\) and \(M^*\) computes the common dimension without enumerating the, potentially exponentially many, bases. After any consistent history, the remaining basis family is a minor's basis family, up to already-fixed coordinates. Predicting the label of larger minor dimension ensures that each mistake reduces the integer-valued dimension by at least one. The lower bound from static shattering proves worst-case optimality.

## Verification
The supplementary standalone Python program `verify_matroid.py` enumerates every nonempty constant-cardinality family of subsets on ground sets of sizes zero through five, retains exactly those satisfying the basis-exchange axiom, and independently computes (i) static shattering by direct projection, (ii) adaptive shattering by a version-space recursion, (iii) the rank-minimum formula by all-subset minimization, and (iv) the maximum common-independent-set size. It also verifies equation (1) on every nonconstant coordinate of each resulting matroid.

Its complete counts of labeled basis families that are matroids, by ground-set size \(0,1,2,3,4,5\), are \(1,2,5,16,68,406\). All 498 cases pass all four equalities and the minor-split check. An additional 336 deterministically seeded random binary-representable matroids of ground size four through ten pass the same comparisons. The accompanying `verification_output.txt` is actual captured program output. These finite tests corroborate, but do not replace, the unrestricted induction and the standard matroid-intersection theorem.

## Relationship to prior work
The classical matroid-intersection min–max theorem is explicitly used, not claimed as new. Chakrabarty, Lee, Sidford, Singla, and Wong (2019, arXiv:1911.10765v1, Introduction, rank-oracle section) give its rank formula and algorithms for finding common independent sets, without identifying the VC or Littlestone dimensions of a matroid's basis-incidence class.

Merino, Mütze, and Williams (2022) prove greedy Gray-code enumeration of the bases of any matroid and study the independence/coindependence-oracle implementation. Their stated results concern listing bases under exchanges, rather than shattering adaptive membership-query trees or equating two learning dimensions.

Chase, Freitag, and Reyzin (2023) analyze Littlestone dimension in query learning and compression, including general principles for how dimensions change under labeled examples, but do not specialize to matroid bases or derive the exact dual-matroid rank minimum. Guingona, Kolesnikov, Nierwinski, and Soucy (2021) establish equal VC and Littlestone dimensions for zero sets of linear combinations, which is a distinct class construction: basis-incidence concepts of arbitrary, possibly nonrepresentable matroids are not covered by their hypothesis.

The new mathematical ingredient here is the *partition of the matroid-intersection minimizer by any queried element*, turning the static min–max theorem into the exact two-branch adaptive rank identity (1). This connection is not supplied by the general dimension inequality alone or by algorithms enumerating matroid bases.

## Limitations
The theorem concerns finite matroids and deterministic realizable binary element-membership prediction only. It does not assert that arbitrary constant-cardinality set families are matroids or that their VC and Littlestone dimensions coincide. The polynomial statement concerns the dimension and the abstract oracle model, not an implementation-specific end-to-end running time for online prediction. The cited matroid-intersection theorem and the two dimension definitions are standard inputs. Searches of the consulted literature found no equivalent matroid-basis learning theorem, but historical priority beyond those sources remains uncertain; this work has not been independently audited.

## References
1. D. Chakrabarty, Y. T. Lee, A. Sidford, S. Singla, and S. C.-w. Wong, *Faster Matroid Intersection*, arXiv:1911.10765v1, first posted 2019-11-25. In particular, Introduction §1, rank-oracle discussion, states the Edmonds matroid-intersection minimum formula. https://arxiv.org/html/1911.10765v1
2. A. Merino, T. Mütze, and A. Williams, *All Your bases Are Belong to Us: Listing All Bases of a Matroid by Greedy Exchanges*, FUN 2022, DOI:10.4230/LIPIcs.FUN.2022.22, published 2022-05-23. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FUN.2022.22
3. H. Chase, J. Freitag, and L. Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812v1, posted 2023-10-07. https://arxiv.org/html/2310.04812v1
4. V. Guingona, A. Kolesnikov, J. Nierwinski, and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1, posted 2021-09-10. https://arxiv.org/abs/2109.04805
