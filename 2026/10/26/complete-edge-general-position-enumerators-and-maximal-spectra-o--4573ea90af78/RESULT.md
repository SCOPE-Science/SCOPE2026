# Complete edge-general-position enumerators and maximal spectra of cycles

## Finding

Let \(C_n\) be a simple cycle on \(n\ge3\) edges. An *edge-general-position set* \(S\subseteq E(C_n)\) contains at most two edges of every shortest vertex-to-vertex path. Define \(P_n(z)=\sum_{S\text{ legal}}z^{|S|}\) and \(M_n(z)=\sum_{S\text{ inclusion-maximal legal}}z^{|S|}\). The empty set is counted in \(P_n\).

For \(3\le n\le5\),
\[
P_n(z)=(1+z)^n,\qquad M_n(z)=z^n.
\]
For all \(n\ge6\), write \(m=\lfloor n/2\rfloor\), \(b=\lceil n/2\rceil\), and
\[
A_n=\frac n3\left(\binom{n-1}{2}-3\binom{m-1}{2}\right),\qquad
B_n=\begin{cases}\binom m2&n=2m,\\n(m-1)&n=2m+1.\end{cases}
\]
Then
\[
P_n(z)=1+nz+\binom n2z^2+A_nz^3+B_nz^4.
\]
The complete polynomial for inclusion-maximal sets is
\[
M_n(z)=\begin{cases}
\dfrac{m(m-1)(m-2)}{3}z^3+\binom m2z^4,&n=2m,\\[4pt]
\dfrac{n(m-2)(m-3)}{6}z^3+n(m-1)z^4,&n=2m+1.
\end{cases}
\]
For \(n\ge6\), every maximal set has cardinality three or four; both occur when \(n=6\) or \(n\ge8\), while \(n=7\) has only maximal four-sets. Together with the small cycles, the independence system of legal sets is pure exactly for \(3\le n\le5\) and for \(n=7\).

## Assumptions and scope

All graphs are finite, simple, unweighted cycles. Shortest paths are vertex-to-vertex geodesics in the original graph, not arbitrary paths. Label the edges cyclically by integers \(0,1,\ldots,n-1\), interpreted modulo \(n\). If selected positions in cyclic order are \(e_1,\ldots,e_k\), define their positive cyclic gaps \(g_i=e_{i+1}-e_i\pmod n\), with \(e_{k+1}=e_1\) and \(\sum_i g_i=n\). These are *differences of edge indices*, not counts of unselected edges. A zero-, one-, or two-edge subset is automatically legal. Inclusion-maximal means not properly contained in another legal subset and differs from maximum cardinality.

## Proof

**Gap criterion.** A shortest path in \(C_n\) consists of a consecutive arc of at most \(m=\lfloor n/2\rfloor\) edges; conversely every such arc is shortest between its endpoints. Three specified edges lie in such an arc if and only if one of the three intervening cyclic gaps is at least \(n-m+1=b+1\): the complementary arc includes the three edges and occupies \(n-g+1\) consecutive edge positions. Consequently a triple is legal exactly when its three cyclic gaps are at most \(b\). A set is legal precisely when all its triples are legal.

**Four and five edges.** Let four edges have successive positive gaps \(g_1,g_2,g_3,g_4\). Among their four triples, each replaces exactly one adjacent pair of gaps by its sum; the triple criterion is therefore equivalent to \(g_i+g_{i+1}\le b\) for every cyclic index \(i\). In a hypothetical legal five-set, select each triple of three consecutive selected edges. The complementary cyclic gap for that triple equals the sum of three consecutive gaps of the five-set, so all five cyclic three-gap sums are at most \(b\). Summing gives \(3n\le5b\), impossible for every \(n\ge6\): for even \(n\), \(3n-5b=n/2>0\); for odd \(n\ge7\), \(3n-5b=(n-5)/2>0\). Hence no larger subset is legal either.

**Enumerating triples.** The number of ordered triples of positive gaps summing to \(n\) is \(\binom{n-1}{2}\). The number with one specified gap at least \(b+1\) is \(\binom{n-b-1}{2}=\binom{m-1}{2}\). Two distinct gaps cannot both exceed \(b\), because \(2(b+1)>n\). Thus the number of valid ordered gap triples is \(\binom{n-1}{2}-3\binom{m-1}{2}\). Choosing an initial edge among \(n\) positions and dividing by the three choices of selected initial edge gives \(A_n\). The cases of fewer than three edges give the first three coefficients of \(P_n\).

**Enumerating four-sets.** Suppose \(n=2m\). Summing four adjacent-pair inequalities gives \(2n=4m\), so all inequalities are equalities. Thus the gaps alternate \((a,m-a,a,m-a)\), with \(1\le a\le m-1\). There are \(m-1\) ordered gap quadruples, hence \(n(m-1)/4=\binom m2\) unmarked four-sets.

If \(n=2m+1\), each of the two opposite adjacent-pair sums partitions \(n\) into two positive integers each at most \(m+1\); their values are \(m\) and \(m+1\), in one of two orders. Choosing independently the order of the two opposite pairs gives four alternatives. Each leaves exactly \(m-1\) positive choices for one gap, with the others determined and positive, yielding \(4(m-1)\) ordered quadruples. Dividing \(n\cdot4(m-1)\) by four gives \(B_n=n(m-1)\).

**Classifying maximal triples.** Every legal triple with gaps \(x,y,g\) is extendable to a legal four-set if and only if some gap \(g\) is at least \(m\). Necessity: after inserting a fourth edge into the gap \(g\), the two other original gaps \(x,y\) must remain adjacent in the four-set, and hence \(x+y=n-g\le b\), so \(g\ge m\). Sufficiency: let \(m\le g\le b\), and write \(g=a+(g-a)\) with positive integer \(a\). The four cyclic adjacent-pair constraints for \((x,y,a,g-a)\) reduce to
\[
\max(1,g+x-b)\le a\le\min(g-1,b-y).
\]
Since \(x+y=n-g\), \(x,y\ge1\), and \(n\le2b\), the interval is nonempty: \(x,y\le b-1\), while \(g+x-b\le b-y\) follows from \(n\le2b\). Every legal four-set is maximal since five-sets are impossible. Thus a legal triple is maximal exactly when all its gaps lie in \([1,m-1]\).

The number of positive ordered triples summing to \(2m\) with parts at most \(m-1\) is \(\binom{2m-1}{2}-3\binom m2=(m-1)(m-2)/2\). For \(2m+1\) it is \(\binom{2m}{2}-3\binom{m+1}{2}+3=(m-2)(m-3)/2\), where the last inclusion-exclusion term arises from pairs of gaps at least \(m\). Multiply these counts by \(n/3\) to obtain the cubic coefficients of \(M_n\).

No legal set of size at most two is maximal: each pair of edges lies in some legal four-set. Indeed, cyclically rotate the pair to positions \(0,d\) with \(1\le d\le m\). For \(d<m\), use \(\{0,d,m,m+d\}\); for \(d=m\), use \(\{0,1,m,m+1\}\). Their gaps satisfy the four-set criterion for both parities; any singleton or empty set extends as well. Thus the maximal-set formula is exhaustive.

Finally, for \(n\le5\), every shortest path has at most two edges, so every edge subset is legal. For odd \(n=2m+1\ge7\), the maximal triple count vanishes precisely at \(m=3\), namely \(n=7\); for even \(n\ge6\), it is positive. This establishes the purity statement. \(\square\)

## Verification

The accompanying Python 3 standard-library file `verify.py` implements legal sets directly from all original shortest arc masks, **independently of the gap formula**, and computes inclusion-maximality by testing each possible edge extension. It exhaustively compares all cardinality coefficients, all legal triples and quartets against the gap characterizations, and the maximal-set polynomial for every \(3\le n\le16\). The total number of checked subsets is \(\sum_{n=3}^{16}2^n=131064\). Execute `python3 verify.py`; the captured exact output is `verification_output.txt`. Finite checks corroborate, but do not establish, the infinite formulas.

## Relationship to prior work

Manuel, Prabha and Klavžar, *The Edge General Position Problem* (arXiv:2105.04292), established the maximum edge-general-position cardinality of cycles: \(n\) for \(n\le5\) and four otherwise. Tian, Klavžar and Tan (arXiv:2302.01587) recall the same extremal result. **Neither extremal fact is claimed here.**

There is a precise prior-theory reduction: edge-general-position subsets of \(C_n\) correspond to general \(d\)-position vertex subsets of the line graph \(L(C_n)\cong C_n\), with \(d=\lfloor n/2\rfloor-1\), since a shortest path containing \(\ell\) consecutive edges corresponds to a vertex path containing their \(\ell\) line-graph vertices. Klavžar, Rall and Yero, *General \(d\)-position sets* (arXiv:2005.08095), Proposition 3.3 already determines the maximum size from this perspective and Theorem 4.1 provides an abstract structural criterion. These pre-existing results are not claimed as new; the complete cyclic-gap enumeration and inclusion-maximal size distribution are the results evaluated here.

Iršič, Klavžar, Rus and Tuite, *General Position Polynomials* (arXiv:2401.05696), Proposition 2.1 enumerates **ordinary vertex general-position** sets of cycles (maximum degree at most three), a different problem from the present edge enumeration (degree four for \(n\ge6\)).

## Limitations

The formula applies to unweighted simple cycles, not to all graphs, all \(d\)-position variants or graphs with parallel edges. The known maximum edge-general-position number is not new. The enumerator may admit equivalent formulations in unindexed literature; exhaustive bibliographic priority is not guaranteed. Reproducibility checks cover finite sizes only. Independent mathematical validation has not been performed.

## References

1. S. Klavžar, D. F. Rall, I. G. Yero, *General \(d\)-position sets*, arXiv:2005.08095v1 (16 May 2020), https://arxiv.org/abs/2005.08095.
2. P. D. Manuel, S. Prabha, S. Klavžar, *The Edge General Position Problem*, arXiv:2105.04292 (10 May 2021), https://arxiv.org/abs/2105.04292.
3. J. Tian, S. Klavžar, E. Tan, *Extremal Edge General Position Sets in Some Graphs*, arXiv:2302.01587 (3 February 2023), https://arxiv.org/abs/2302.01587.
4. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (2024), https://arxiv.org/abs/2401.05696, DOI:10.1007/s00025-024-02133-3.
