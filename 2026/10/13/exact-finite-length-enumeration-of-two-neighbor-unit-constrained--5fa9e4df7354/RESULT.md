# Exact finite-length enumeration of two-neighbor unit-constrained permutations
## Finding
For every integer \(n\ge2\), let \(\mathcal A_n\) consist of the permutations \(\sigma\) of \(\{1,\ldots,n\}\) such that for every interior position \(2\le i\le n-1\), at least one of \(|\sigma(i)-\sigma(i-1)|=1\) or \(|\sigma(i+1)-\sigma(i)|=1\) holds. This is the symmetric two-neighbor rank constraint with tolerance one introduced in the cited rank-modulation literature.

Define polynomials \(P_m(u)\), for \(m\ge1\), by
\[
P_1(u)=1,\qquad P_2(u)=4u-2u^2,\qquad P_3(u)=2u+4u^2-2u^3,
\]
and, for every \(m\ge4\),
\[
P_m(u)=uP_{m-1}(u)+(2u-u^2)P_{m-2}(u).
\]
Then the exact number of admissible permutations of every length is
\[
\boxed{|\mathcal A_n|=\sum_{j=0}^{n-1}[u^j]P_{n-1}(u)\,(n-j)!}.\tag{1}
\]
Equivalently, the auxiliary polynomials have the rational bivariate generating function
\[
\boxed{\sum_{m\ge1}P_m(u)z^m=\frac{z\big(1+(3u-2u^2)z+u^2z^2\big)}{1-uz-(2u-u^2)z^2}.}\tag{2}
\]
Formula (1) is evaluable with \(O(n^2)\) integer-arithmetic operations when all coefficients are retained; this is an arithmetic-operation count, not a claim of quadratic bit complexity. Exact values at lengths \(n=2,3,\ldots,14\) are \(2,6,18,52,170,550,1972,6998,27106,104052,430458,1769046,7752020\).

## Assumptions and scope
The symbols are all distinct and occupy the linearly ordered positions \(1,\ldots,n\). Differences refer to ordinary integers, not circular distances. Endpoints impose no separate condition. The condition uses an inclusive tolerance of one and an OR between the two neighboring absolute differences. No additional minimum-distance or error-correction restriction is imposed. Our claimed result is the all-length exact cardinality and recurrence, not the previously known asymptotic capacity of this constrained alphabet.

## Proof
Put \(m=n-1\). For each permutation \(\sigma\), define the set of *good edges*
\[
G(\sigma)=\{i\in\{1,\ldots,m\}:|\sigma(i+1)-\sigma(i)|=1\}.
\]
An interior position satisfies the constraint precisely when its two incident edges are not both bad. Therefore \(\sigma\in\mathcal A_n\) if and only if the complement of \(G(\sigma)\) contains no consecutive integers.

**Forcing an arbitrary set of good edges.** Fix \(S\subseteq\{1,\ldots,m\}\), and let \(r(S)\) be the number of nonempty runs of consecutive edges in \(S\). Each run of length \(\ell\ge1\) requires its \(\ell+1\) consecutive positional symbols to be pairwise consecutive integers, with each successive difference equal to \(+1\) or \(-1\). Since no integer can be visited twice, all differences along one such run must have the same sign. Hence the values on that entire positional block are monotone, with exactly two possible orientations. Every unselected-edge separator determines a boundary between blocks. There are exactly \(b=n-|S|\) positional blocks, with distinguishable sizes and positions; allocating the ordered interval \(\{1,\ldots,n\}\) as \(b\) consecutive value intervals in an arbitrarily chosen block order gives \(b!\) assignments. For each positive-edge run there are two orientations. Consequently, the number of permutations for which \(S\subseteq G(\sigma)\) is exactly
\[
F_n(S)=2^{r(S)}(n-|S|)! .\tag{3}
\]
The positional blocks are fixed and labeled by position; no permutation of identically sized blocks is being quotiented out. Additional unforced good edges are allowed, as is required for (3).

**Möbius expansion of the condition.** Let \(f(T)\) be one when \(\{1,\ldots,m\}\setminus T\) has no consecutive integers, zero otherwise. On subsets define
\[
h_m(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}f(T).
\]
Boolean-lattice Möbius inversion gives \(f(G)=\sum_{S\subseteq G}h_m(S)\) for every \(G\). Sum this identity over all permutations, interchange the finite sums and apply (3):
\[
|\mathcal A_n|=\sum_{S\subseteq[m]}h_m(S)\,2^{r(S)}(n-|S|)! .\tag{4}
\]
Set \(P_m(u)=\sum_{S\subseteq[m]}h_m(S)2^{r(S)}u^{|S|}\). Grouping (4) by \(|S|\) proves equation (1) for these polynomials.

**A three-state transfer calculation.** In the preceding double sum over \(T\subseteq S\), at an edge position record the pair \((s,t)\) of membership indicators for \(S,T\). Only \((0,0),(1,0),(1,1)\) are possible. The condition \(f(T)=1\) forbids consecutive positions with \(t=0\). The local weight at the current site is \((-1)^{s-t}u^s2^{s(1-s_{\rm old})}\), so the factor two occurs exactly when a new nonempty run of \(S\) begins. Ordering the three states as just listed, the first-position row and transition matrix are
\[
v=(1,-2u,2u),\qquad M=\begin{pmatrix}0&0&2u\\0&0&u\\1&-u&u\end{pmatrix}.
\]
Thus for every \(m\ge1\),
\[
P_m(u)=vM^{m-1}\begin{pmatrix}1\\1\\1\end{pmatrix}.
\]
Inverting \(I-zM\) as a matrix of formal power series gives precisely (2). Its first three coefficients are \(1\), \(4u-2u^2\) and \(2u+4u^2-2u^3\); multiplying by the denominator yields the stated order-two recurrence for all \(m\ge4\). This completes the proof for every \(n\ge2\).

## Verification
Run `python verify_recurrence.py` using Python 3 standard library. This computes the recurrence, directly enumerates all \(n!\) permutations for \(2\le n\le10\), and independently checks the count by a used-symbol-mask dynamic program for \(2\le n\le14\). It also computes exact values through length \(100\); those longer calculations are demonstrations, not substitutes for the proof. Run `python transfer_check.py` from the same directory to check the independent three-state transfer implementation against the polynomial recurrence for \(1\le m\le59\), and the original double Möbius sum for \(1\le m\le9\). Both programs use only Python 3 standard library modules. Successful outputs include `VERIFIED unit two-neighbor formula via brute and subset DP` and `TRANSFER_OK m=1..59, MOBIUS_OK m=1..9`.

## Relationship to prior work
Buzaglo and Yaakobi introduced the two-neighbor constraint in their preprint (January 17, 2014) and expanded the analysis in a 2016 journal article. Their Definition 2 is precisely the condition used here with tolerance one. Their Theorems 13 and 15 and Lemma 14 establish asymptotic capacity and bounds, including \(C(1)=1/2\), but they do not state the all-length exact count, the displayed recurrence or the generating function. Their Construction 11 gives one large *subset* of admissible permutations, not an enumeration of the entire constrained alphabet.

Reilly and Tanny (1979) count permutations with a prescribed number of *increasing* successions, without imposing the positional exclusion of adjacent bad edges; their published abstract describes a univariate succession statistic. Such totals do not themselves determine the positional pattern of absolute \(\pm1\) successions required here. The full 1979 article was not accessible for complete comparison, so a more general underlying enumeration theorem remains a bibliographic risk. The proof presented above is self-contained and does not assume novelty merely from failed database searches.

## Limitations
The exact count concerns the *symmetric* two-neighbor tolerance-one constraint only; it does not give a complete exact enumeration for higher tolerances, asymmetric two-neighbor constraints, or codes with additional distance restrictions. The recurrence counts admissible rankings; it does not provide an efficient optimal rank/unrank encoder. Its \(O(n^2)\) bound counts integer-arithmetic operations rather than bit complexity. Originality is subject to residual risk from unindexed or incompletely accessible historical succession-enumeration literature. No independent external validation or audit is claimed.

## References
1. S. Buzaglo and E. Yaakobi, *Constrained Codes for Rank Modulation*, arXiv:1401.4484v1, first posted 2014-01-17, https://arxiv.org/abs/1401.4484.
2. S. Buzaglo and E. Yaakobi, *On the Capacity of Constrained Permutation Codes for Rank Modulation*, IEEE Transactions on Information Theory 62(4), 1649–1666 (2016), DOI:10.1109/TIT.2016.2519400; author-hosted full text: https://yaakobi.net.technion.ac.il/files/2016/04/20_RM_Capacity_IT16.pdf.
3. J. W. Reilly and S. M. Tanny, *Counting Successions in Permutations*, Studies in Applied Mathematics 61, 73–81 (1979), DOI:10.1002/sapm197961173 (abstract accessible; complete text not inspected).
