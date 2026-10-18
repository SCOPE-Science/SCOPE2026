# Exact signed Roman domination and extremal rigidity in two-subset Kneser graphs

## Finding
For every integer \(n\ge9\), the signed Roman domination number of the two-subset Kneser graph is
\[
\gamma_{\mathrm{sR}}(K(n,2))=\begin{cases}3,&n\text{ odd},\\4,&n\text{ even}.\end{cases}
\]
All minimum signed Roman dominating functions for odd \(n\ge9\) admit the following complete classification. Partition \([n]=A\sqcup B\), where \(|A|=(n-3)/2\) and \(|B|=(n+3)/2\). Give every cross-pair label \(-1\), every pair within \(B\) label \(1\), and label the pairs within \(A\) from \(\{-1,1,2\}\) so that the sum of labels on the \(|A|-1\) pairs incident with each \(a\in A\) is exactly \(|A|+1\), and such that every internal pair labeled \(-1\) is disjoint from at least one internal pair labeled \(2\). Every such labeling is minimum, and every minimum labeling arises uniquely this way. In particular, the respective numbers of labeled minimum functions at \(n=9,11,13\) are \(84,990,15444\).

## Assumptions and scope
The graph \(K(n,2)\) has one vertex for each two-element subset of \([n]=\{1,\ldots,n\}\); two such graph vertices are adjacent precisely when the subsets are disjoint. A signed Roman dominating function is a map \(f:\binom{[n]}2\to\{-1,1,2\}\) such that (i) the sum of \(f\) over each closed graph neighborhood is at least \(1\), and (ii) each vertex labeled \(-1\) has a graph neighbor labeled \(2\). Its weight \(W\) is the sum of all labels; \(\gamma_{\mathrm{sR}}\) minimizes \(W\). All graphs and labels in the theorem are finite; graph vertices are labeled by their underlying two-subsets. This is not ordinary signed domination, nor Roman domination with labels \(\{0,1,2\}\).

## Proof
**1. Incidence identity and universal lower bound.** Regard \(f\) as labels on the edges of the complete graph on \([n]\). For \(i\in[n]\) put \(s_i=\sum_{j\ne i}f(\{i,j\})\), so \(\sum_i s_i=2W\). For \(i\ne j\), let \(T_{ij}\) be the sum on the closed neighborhood of the Kneser vertex \(\{i,j\}\). Since the open neighbors are exactly the pairs disjoint from \(\{i,j\}\),
\[
T_{ij}=W-s_i-s_j+2f(\{i,j\})\ge1.\tag{1}
\]
Summing (1) over \(j\ne i\) gives the exact star identity
\[
\sum_{j\ne i}T_{ij}=(n-3)W-(n-4)s_i.\tag{2}
\]
Also every label occurs in exactly \(1+\binom{n-2}2\) closed neighborhoods. Since each neighborhood sum is at least \(1\),
\[
\left(1+\binom{n-2}2\right)W\ge\binom n2.\tag{3}
\]
For \(n\ge9\), the right-to-left ratio is strictly greater than \(1\); because \(W\) is an integer, \(W\ge2\). If \(W=2\), then (2) implies \((n-4)s_i\le n-5\) for every \(i\), so \(s_i\le0\); this contradicts \(\sum_i s_i=4\). Thus \(W\ge3\).

**2. Weight-three rigidity.** Suppose \(W=3\). From (2), for each \(i\),
\[
(n-4)s_i\le2(n-4),\qquad s_i\le2.\tag{4}
\]
We first prove that some \(s_i=2\). If instead all \(s_i\le1\), let \(p\) be the number with \(s_i=1\), \(z\) the number with \(s_i=0\), and \(h\) the number with negative \(s_i\). The identity \(\sum_i s_i=6\) implies \(p\ge6\) and that the sum of the absolute values of the negative \(s_i\)'s is \(p-6\), whence \(h\le p-6\). Choose \(i\) with \(s_i=1\). Its total neighborhood-sum slack from (2) is
\[
\sum_{j\ne i}(T_{ij}-1)=n-4.\tag{5}
\]
For another \(j\) with \(s_j=1\), condition (1) forces \(f(\{i,j\})\in\{1,2\}\) and hence \(T_{ij}-1\ge2\). If \(s_j=0\), the slack is at least \(3\). If \(s_j=-r\) with \(r\ge1\), it is at least \(r-1\). Consequently
\[
n-4\ge2(p-1)+3z+(p-6-h)=4(p+z)-n-8,
\]
so \(n\ge2(p+z)-2\). But \(n=p+z+h\le2p+z-6\), which would imply \(z\le-4\), absurd. Therefore some \(s_i=2\).

For this \(i\), (2) and \(W=3\) give \(\sum_{j\ne i}T_{ij}=n-1\). Because every \(T_{ij}\ge1\), all of them equal \(1\). Equation (1) therefore yields \(s_j=2f(\{i,j\})\) for all \(j\ne i\). In view of (4), no such pair has label \(2\); thus all other \(s_j\) lie in \(\{-2,2\}\). The same holds for \(s_i\). Writing \(B=\{i:s_i=2\}\) and \(A=\{i:s_i=-2\}\), the equation \(\sum_i s_i=6\) implies \(|B|-|A|=3\), so \(n\) is odd and the displayed part sizes are forced.

For every \(b\in B\), the preceding saturation argument applies, and gives \(f(\{b,j\})=s_j/2\) for all \(j\ne b\). Hence the cross-pairs are \(-1\), pairs inside \(B\) are \(1\), and each \(a\in A\) has internal label sum \(s_a+|B|=-2+|B|=|A|+1\). This proves necessity of the claimed characterization and proves \(W\ge4\) whenever \(n\) is even.

**3. Sufficiency and odd-order upper bound.** Conversely, suppose \(n\ge9\) is odd and the stated partition and internal degree-sum conditions hold. They give \(s_a=-2\) for \(a\in A\), \(s_b=2\) for \(b\in B\), and therefore \(W=3\). Equation (1) gives closed-neighborhood sums exactly \(1\) on cross-pairs and within \(B\), while on pairs within \(A\) they equal \(7+2f(\{a,a'\})\ge5\).

It remains to check the Roman defense condition. At each \(a\in A\), write \(d_2(a)\) and \(d_{-1}(a)\) for its numbers of incident internal pairs labeled \(2\) and \(-1\). The internal sum equation is equivalent to
\[
d_2(a)-2d_{-1}(a)=2,\tag{6}
\]
so \(d_2(a)\ge2\). The graph of internal label-\(2\) edges thus has minimum degree at least \(2\), hence at least \(|A|\) edges, more than the at most \(|A|-1\) incident with any one \(a\). Every cross-pair \(\{a,b\}\), the only type with label \(-1\) outside \(A\), therefore has a disjoint label-\(2\) pair in \(A\). The additional disjointness condition in the statement supplies the required defender for every internal pair labeled \(-1\). Hence the two defining requirements are satisfied for all pairs.

For the existence statement it suffices to take all internal labels in \(A\) equal to \(1\) except the edges of a Hamiltonian cycle, which are labeled \(2\). Then every internal sum is \(|A|+1\), there are no negative internal edges, and every negative cross-pair has a disjoint cycle edge because \(|A|\ge3\). Hence a weight-three signed Roman dominating function exists for every odd \(n\ge9\).

**4. Even-order upper bound.** Let \(n\ge10\) be even, put \(a=n/2-1\), \(b=n/2+1\), and partition \([n]=A\sqcup B\) accordingly. Label each cross-pair \(-1\), each internal pair \(1\), then upgrade a Hamiltonian cycle on \(A\) and three pairwise disjoint pairs on \(B\) to label \(2\). The total weight is
\[
\binom a2+\binom b2-ab+a+3=4.
\]
Every \(a\in A\) has \(s_a=-1\); vertices in \(B\) have \(s_b=1\) or \(2\). Equation (1) gives \(T_{ij}\ge8\) on pairs within \(A\), \(T_{ij}\ge2\) within \(B\), and \(T_{ij}=3-s_b\ge1\) on cross-pairs. For each negative cross-pair \(\{a,b\}\), a label-\(2\) cycle edge in \(A\) avoids \(a\), since \(|A|\ge4\). This proves the upper bound \(4\) and hence the parity formula.

**5. First optimal-function counts.** For \(n=9,11,13\), the set \(A\) has \(a=3,4,5\) vertices. From (6) and \(d_2+d_{-1}\le a-1\), one obtains \(2+3d_{-1}\le a-1\), which forces \(d_{-1}=0\). The label-\(2\) edges are therefore a 2-regular spanning graph on \(A\), necessarily a Hamiltonian cycle for \(a\le5\). There are respectively \(1,3,12\) such cycles, giving \(\binom93\), \(3\binom{11}4\), and \(12\binom{13}5\) labeled functions.

## Verification
The standalone file `verify.py` constructs and checks signed Roman dominating functions for all \(72\) orders \(9\le n\le80\), evaluating every graph vertex's closed-neighborhood sum and explicit defense condition, and checking both weighted-degree identities. It also exhaustively counts allowed internal edge labelings for \(|A|=3,4,5\) (respectively \(1,3,12\)). Run `python3 verify.py`; the recorded stdout is in `verify_output.txt`. These checks test the constructions and small counts; the infinite lower bounds and structural arguments are mathematical proofs, not finite extrapolations.

## Relationship to prior work
Zec and Grbić, *Several Roman domination graph invariants on Kneser graphs* (arXiv:2204.05664, 2022; DMTCS 25:1, 2023), Theorem 3, give \(2\le\gamma_{\mathrm{sR}}(K(n,2))\le3\) for odd \(n\) and \(2\le\gamma_{\mathrm{sR}}(K(n,2))\le5\) for even \(n\) at sufficiently large orders; their Remark 3 supplies exact isolated cases \(n=9,10,11\). The present parity formula supplies the missing lower bounds, improves the even upper bound by a uniform construction, and characterizes the weight-three labelings by a degree-sum identity. The earlier odd cycle construction and isolated values are not claimed as new. A subsequent survey, *Varieties of Roman domination IV*, repeats the earlier Kneser bounds in its indexed text; comprehensive full-text comparison was not possible for that survey. No novelty conclusion is inferred merely from search absence.

## Limitations
The formula is established for \(n\ge9\) only. Smaller values are not newly analyzed here. The internal disjointness clause in the characterization is essential: local incident-sum equalities alone need not defend an internal label-\(-1\) pair. The classification does not enumerate optimizers for even \(n\). The verifier checks finite orders, not the unbounded proof. Independently established mathematical priority is not claimed, and unindexed equivalent work remains possible.

## References
1. T. Zec and M. Grbić, *Several Roman domination graph invariants on Kneser graphs*, arXiv:2204.05664 (first public version 12 April 2022), *Discrete Mathematics & Theoretical Computer Science* 25:1, article 14 (2023), DOI: 10.46298/dmtcs.10506. Full text: https://arxiv.org/pdf/2204.05664 .
2. M. Chellali, N. Jafari Rad, S. M. Sheikholeslami, and L. Volkmann, *Varieties of Roman domination IV*, DOI: 10.1080/09728600.2025.2598772 (2026).
