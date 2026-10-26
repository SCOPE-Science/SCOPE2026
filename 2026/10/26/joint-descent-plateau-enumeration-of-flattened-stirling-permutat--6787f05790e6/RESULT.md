# Joint descent–plateau enumeration of flattened Stirling permutations

## Finding

Let \(\mathcal F_n\) be the set of flattened Stirling permutations of order \(n\). For internal descents \(d(w)\) and internal plateaux \(p(w)\), define
\[
H_n(t,u)=\sum_{w\in\mathcal F_n}t^{d(w)}u^{p(w)}.
\]
For every \(n\ge1\), the complete joint distribution is specified by the exact bivariate exponential generating function
\[
\boxed{\sum_{n\ge1}H_n(t,u)\frac{x^{n-1}}{(n-1)!}=Z(x;t,u)\exp W(x;t,u)}
\]
where
\[
Z(x;t,u)=u+t(e^{ux}-1),
\]
\[
W(x;t,u)=ux+\sum_{s\ge2}\left[t\left(u^{s-1}+u^s\right)+\left(2^{s-1}-2\right)t^2u^{s-1}\right]\frac{x^s}{s!}.
\]
The displayed expressions are formal series in \(x\) over \(\mathbb Z[t,u]\). In particular, no division by \(u\) or limiting convention is needed. They determine the complete joint ascent–plateau distribution as well: because all \(2n-1\) internal comparisons are ascents, descents, or plateaux, the three-variable polynomial is \(v^{2n-1}H_n(t/v,u/v)\), with \(v\) marking ascents and \(t,u\) marking descents and plateaux.

For example,
\[
H_2(t,u)=u^2+tu,\qquad H_3(t,u)=u^3+4tu^2+tu^3,
\]
\[
H_4(t,u)=u^4+11tu^3+4tu^4+3t^2u^2+5t^2u^3.
\]

## Assumptions and scope

A Stirling permutation of order \(n\) is a word containing each of \(1,2,\ldots,n\) twice, such that every entry strictly between the two copies of \(i\) exceeds \(i\). A run is a maximal weakly increasing contiguous subword. A word is *flattened* when its successive run-starting values are weakly increasing. The statistics \(d(w)=\#\{i<2n:w_i>w_{i+1}\}\) and \(p(w)=\#\{i<2n:w_i=w_{i+1}\}\) count only internal positions; no artificial first or last letters are appended. The result covers all positive integers \(n\), with no asymptotic assumption. The source family and bijection have verified primary MSC \(05A05\).

## Proof

Use the bijection between \(\mathcal F_n\) and type-B set partitions on \(\{0,\pm1,\ldots,\pm(n-1)\}\), established in Buck–Elder–Figueroa–Harris–Harry–Simpson (2023). A type-B partition consists of a zero block fixed by negation, containing \(0\), and a set of unordered opposite pairs of nonzero blocks. One representative of each nonzero pair is chosen to contain its smallest absolute label positively. The labels of size \(n-1\) below are the absolute labels distinct from zero.

For a nonzero block-pair of total absolute size \(s\), put \(p\ge1\) positive entries (including the smallest absolute element) and \(q\ge0\) negative entries, with \(p+q=s\). In the explicit bijection, the block-pair contributes a concatenation \(f(N)g(P)\), where \(f(N)\) is the word of the doubled negative-class labels in increasing absolute order and \(g(P)\) consists of the smallest positive-class label, followed by the other doubled positive-class labels in increasing order, then that smallest positive-class label again. When \(p=1\), \(g(P)\) is simply that doubled smallest label. Every absolute label is shifted by one in the resulting permutation.

Within this block word the number of descents is \(\mathbf1_{q>0}+\mathbf1_{p>1}\). Its number of plateaux is \(q+p-1=s-1\) if \(p>1\), and \(q+1=s\) if \(p=1\). These are exhaustive: descents occur only at the join \(f(N)|g(P)\) (if \(q>0\)) and at the final return to the smallest positive label (if \(p>1\)); all other adjacent comparisons are increases or equalities. For \(s=1\), the weight is \(u\). For \(s\ge2\), there are precisely three disjoint cases:

* \(q=0\), with weight \(t u^{s-1}\);
* \(q=s-1\), with weight \(t u^s\);
* \(1\le q\le s-2\), with \(\binom{s-1}{q}\) sign allocations each of weight \(t^2u^{s-1}\).

The last case sums to \((2^{s-1}-2)t^2u^{s-1}\). Thus the exponential weight of one nonzero block-pair, summed over its nonempty absolute label set, is exactly \(W(x;t,u)\).

The zero block has \(z\ge0\) nonzero absolute labels besides \(0\). Its output word \(g(P_0)\) has \(p_0=z+1\) positive labels including the special smallest one. If \(z=0\) it gives one plateau and no descent, with weight \(u\). If \(z\ge1\) it gives one descent and exactly \(z\) plateaux, with weight \(tu^z\). Hence the zero-block exponential series is exactly \(Z(x;t,u)\).

Finally the canonical ordering of nonzero block-pairs by their least absolute element makes the boundary between successive block words an ascent, because the final letter of a block word is its least positive label and the first letter of the next block has a strictly larger least label; the zero-block word begins with the globally least letter and ends with that letter. Thus no descent or plateau is omitted at the joins. All weights factor across the distinguished zero block and an arbitrary *set* of nonzero block-pairs. The labeled exponential formula therefore yields \(Z\exp W\), and the bijection transfers exactly these weights to \(\mathcal F_n\). The coefficient of \(x^{n-1}/(n-1)!\) proves the theorem for every \(n\ge1\).

## Verification

The embedded `verify.py` independently constructs \(H_n(t,u)\) by a block-size recurrence (equivalent to extracting coefficients of \(Z\exp W\)), and generates all Stirling permutations by adjacent insertion of the new greatest doubled label. It then filters by the run-start condition and measures adjacent descents and plateaux directly. Complete coefficient tables agree for \(1\le n\le8\), with flattened totals \(1,2,6,24,116,648,4088,28640\). The direct enumeration uses all \( (2n-1)!!\) Stirling permutations before filtering at each tested order, not a partial sample. The infinite conclusion rests on the bijection and block-weight proof, not this finite check.

Two additional independent specializations follow directly: setting \(u=1\) gives exactly the descent EGF of Shankar (2023), Corollary 10; setting \(t=u=1\) yields \(\exp(x+(e^{2x}-1)/2)\), the known Dowling-number EGF. These comparisons check the normalization but do not imply the joint refinement.

## Relationship to prior work

Buck et al. (2023) supply the type-B partition bijection, and Shankar (2023), Theorem 8 and Corollary 10, already establish the *descent-only* EGF. Consequently the specialization \(u=1\) is **not** claimed as new. Shankar's Section 7, question 4, asks for the joint statistics of ascents and plateaux on flattened \(k\)-Stirling permutations. The present all-order bivariate formula answers that question for the original \(k=2\) case. Ma–Ma–Yeh (2019) analyze statistics on all Stirling permutations without the flattening restriction. Ma–Liu–Yeh–Yeh (2025) study a distinct restricted family in which the smallest letter occurs once; their full text does not identify the flattened class or this EGF. The present claim is a joint refinement on a strictly specified subset, not a restatement of the unrestricted Eulerian distributions.

## Limitations

Only the \(k=2\) case is proved; nothing is asserted for general \(k>2\), for joint limiting laws, or for closed-form individual coefficients beyond coefficient extraction. A paper or table not indexed in the inspected sources could predate this refinement. The formula itself does not establish priority beyond the explicit literature comparisons.

## References

1. A. Buck, J. Elder, A. A. Figueroa, P. E. Harris, K. Harry, A. Simpson, *Flattened Stirling Permutations*, arXiv:2306.13034 (first public 2023-06-22), https://arxiv.org/abs/2306.13034 . Section 3 and its type-B bijection.
2. U. Shankar, *Enumeration of flattened \(k\)-Stirling permutations with respect to descents*, arXiv:2307.07730 (first public 2023-07-15), https://arxiv.org/abs/2307.07730 . Theorem 8, Corollary 10, Section 7 question 4.
3. S.-M. Ma, J. Ma, Y.-N. Yeh, *The Ascent-Plateau Statistics on Stirling Permutations*, arXiv:1801.08056 (2018; published 2019), https://arxiv.org/abs/1801.08056 .
4. S.-M. Ma, J.-Y. Liu, J. Yeh, Y.-N. Yeh, *Eulerian-type polynomials over Stirling permutations and box sorting algorithm*, arXiv:2506.16438 (2025), https://arxiv.org/abs/2506.16438 . Section 3.2.
