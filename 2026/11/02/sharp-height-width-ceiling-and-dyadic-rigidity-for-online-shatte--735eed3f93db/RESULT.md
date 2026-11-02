# Sharp height–width ceiling and dyadic rigidity for online shattering of poset ideals

## Finding
Let \(P\) be any nonempty finite partially ordered set of height \(h\) and width \(w\), where height and width mean the maximum numbers of elements in a chain and an antichain, respectively. Let \(\mathcal J(P)\) contain the characteristic functions of all lower order ideals, including the empty ideal, on the domain \(P\); each query names one element and requests its membership bit. Then
\[
\operatorname{VCdim}(\mathcal J(P))=w,\qquad
w\le\operatorname{Ldim}(\mathcal J(P))\le w\left\lfloor\log_2(h+1)\right\rfloor.
\]
The upper bound is the **exact maximum** for each prescribed pair of positive integers \((h,w)\): the disjoint union of \(w\) chains, each of length \(h\), attains it.

There is a rigid equality characterization at every dyadic height. Whenever \(h+1=2^r\) for an integer \(r\ge1\), equality \(\operatorname{Ldim}(\mathcal J(P))=rw\) holds **if and only if** \(P\) is the disjoint union of \(w\) chains, each of length \(h\).

In particular, every poset of height at most two has \(\operatorname{Ldim}=\operatorname{VCdim}=w\). Height three is the first possible height permitting an adaptive–static difference: for every height-three poset, \(0\le\operatorname{Ldim}-\operatorname{VCdim}\le w\), and equality at the upper endpoint occurs exactly for a disjoint union of \(w\) three-element chains.

## Assumptions and scope
A *lower ideal* \(I\subseteq P\) satisfies \(y\in I\) and \(x\le y\) only if \(x\in I\). All ideals, including \(\varnothing\) and \(P\), are present. One concept is one ideal, with Boolean response \(\mathbf 1[x\in I]\) to the query \(x\in P\). The VC dimension is the largest number of fixed queries shattered by all Boolean response patterns. The Littlestone dimension is the maximum depth of a complete binary query tree for which every root-to-leaf sequence of answers is realized by some ideal, with queries allowed to depend on earlier answers. Distinct root-to-leaf sequences must have distinct witness concepts. Only finite posets are considered. The empty poset, excluded from the displayed theorem, has both dimensions zero.

No restrictions on comparabilities other than being a partial order are imposed. The dyadic equality statement requires the actual height \(h\), not an arbitrary loose height upper bound.

## Proof
**1. VC dimension is width.** If \(x<y\) are both in a fixed query support, the pattern accepting \(y\) but rejecting \(x\) is impossible for a lower ideal. Every VC-shattered support is therefore an antichain, of cardinality at most \(w\). Conversely, fix a maximum antichain \(A\). For each \(B\subseteq A\), take its down-closure \(\downarrow B=\{x\in P:x\le b\text{ for some }b\in B\}\). Antichain incomparability gives \((\downarrow B)\cap A=B\), so every pattern on \(A\) occurs. Hence \(\operatorname{VCdim}=w\), and \(\operatorname{Ldim}\ge w\) by using a fixed shattered support along every level of a query tree.

**2. Disjoint-domain additivity.** Suppose two finite nonempty binary concept classes \(H\) and \(K\) are defined on disjoint query domains, and \(H\times K\) consists of their independent combinations. Then
\[
\operatorname{Ldim}(H\times K)=\operatorname{Ldim}(H)+\operatorname{Ldim}(K).
\]
The lower bound concatenates complete shattered trees for the two classes. For the upper bound, put \(a=\operatorname{Ldim}(H)\), \(b=\operatorname{Ldim}(K)\) and induct on \(a+b\). A query in the first domain cannot split \(H\) into two nonempty branches both having dimension at least \(a\), since that would shatter a tree of depth \(a+1\). Hence at least one branch has dimension at most \(a-1\), and by induction its product with \(K\) has dimension at most \(a+b-1\). The same argument applies to queries in the second domain. Therefore no depth-\(a+b+1\) tree exists. If one factor has dimension zero, it contains only one distinct concept and adds no depth.

**3. Chain upper bound.** A chain of \(\ell\) elements has exactly \(\ell+1\) lower ideals, namely its prefixes. By hypothesis counting the Littlestone dimension is at most \(\lfloor\log_2(\ell+1)\rfloor\); repeatedly querying a position that bisects the remaining possible prefix lengths constructs a complete tree of that depth. Thus equality holds for the chain.

By Dilworth's chain-partition theorem, partition \(P\) into exactly \(w\) nonempty chains \(C_1,\ldots,C_w\), with lengths \(\ell_i\le h\). Every ideal restricts to a prefix on each chain. Its vector of restrictions is an injective representation within the unrestricted Cartesian product of the chain-prefix families. Inclusion of concept classes cannot increase Littlestone dimension. By Step 2,
\[
\operatorname{Ldim}(\mathcal J(P))
\le\sum_{i=1}^{w}\left\lfloor\log_2(\ell_i+1)\right\rfloor
\le w\left\lfloor\log_2(h+1)\right\rfloor.
\]
For a disjoint union of \(w\) chains of length \(h\), there are no cross-chain restrictions, so both inequalities are equalities. This also proves the claimed exact extremal maximum for every \((h,w)\).

**4. Dyadic rigidity.** Now assume \(h+1=2^r\) and \(\operatorname{Ldim}(\mathcal J(P))=rw\). A shattered depth-\(rw\) binary tree has \(2^{rw}\) distinct leaf witnesses. On the other hand, the chain partition gives
\[
2^{rw}\le|\mathcal J(P)|\le\prod_{i=1}^{w}(\ell_i+1)
\le(h+1)^w=2^{rw}.
\]
Every inequality is an equality. The final product equality forces \(\ell_i=h\) for every chain. Equality in the injection into all prefix vectors says every tuple of independent chain prefixes is an ideal. If there were a cross-chain comparability \(a<b\) with \(a\in C_i\), \(b\in C_j\) and \(i\ne j\), the prefix containing \(b\) on \(C_j\) together with the empty prefix on \(C_i\) would not be an ideal, a contradiction. Thus there are no comparabilities between different chains and \(P\) is the stated disjoint union. The converse was proved in Step 3.

**5. Low-height boundary.** At \(h=1\) or \(h=2\), \(\lfloor\log_2(h+1)\rfloor=1\), so the lower and upper bounds coincide at \(w\). At \(h=3\), the coefficient is two. The rigidity argument with \(r=2\) identifies precisely the posets attaining \(2w\), and disjoint unions of three-element chains supply such posets. This yields both the sharp height-three gap and the earliest height with any gap.

## Verification
A standalone Python program, `verify.py`, independently enumerates the ideals of each finite poset with a fixed natural-label linear extension, and computes its Littlestone dimension by exact version-space recursion. It checks 5,231 distinct naturally labeled partial orders on up to six elements (one through six elements respectively: 1, 2, 7, 40, 357, 4,824). Every one satisfies the height–width bound; every height-at-most-two instance has dimension equal to width; and the tested height-three equality cases are exactly the disjoint unions of three-element chains. Further explicit tests check products of two-, three- and seven-element chains. Execute `python3 verify.py` using only the standard Python library. The final success marker is `HEIGHT_WIDTH_SHATTERING_ALL_CHECKS_PASS 5231`. These finite tests are corroboration, not substitutes for Steps 1–5.

## Relationship to prior work
Iams, Johnston and Muth study membership queries for ideals under a bound on the number of positive answers, optimizing the worst-case **total number of queries**. That minimax identification objective is not the maximum complete binary shattering depth here. Ghazi, Golowich, Kumar and Manurangsi give general closure bounds for Littlestone dimension under Boolean aggregation on a common domain; they do not determine this poset-specific sharp width–height extremum. Elizalde, Plante, Roby and Sagan study the ideal lattices of fences through rowmotion, orbit structure and homomesy, rather than online shattering. The present claim is a separate exact classification and sharp extremal rigidity theorem. No claim is made that the underlying ingredients—Dilworth's theorem, chain-prefix thresholds, and disjoint-domain rank additivity—are themselves new.

## Limitations
The upper bound can be strict for general posets of height greater than two, and the theorem does not determine the Littlestone dimension of each individual poset of arbitrary height. The equality characterization is asserted only when \(h+1\) is a power of two; no converse characterization is claimed at other heights. A distinct theorem under the language of monotone online classification, thicket rank, or chain-cover learning could conceivably predate this formulation; exhaustive historical-priority verification is not claimed. No independent scientific audit is included.

## References
1. A. Iams, H. Johnston and R. Muth, *Searching for quicksand ideals in partially ordered sets*, first arXiv version dated 2020-09-15, arXiv:2009.07348, https://arxiv.org/abs/2009.07348.
2. B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, Algorithmic Learning Theory, PMLR 132 (2021), https://proceedings.mlr.press/v132/ghazi21a.html.
3. S. Elizalde, M. Plante, T. Roby and B. E. Sagan, *Rowmotion on fences*, arXiv:2108.12443 (first version 2021-08-27), Algebraic Combinatorics 6 (2023), https://arxiv.org/abs/2108.12443.
4. R. P. Dilworth, *A Decomposition Theorem for Partially Ordered Sets*, Annals of Mathematics 51 (1950), 161–166 (the classical chain-partition theorem used in the proof).
