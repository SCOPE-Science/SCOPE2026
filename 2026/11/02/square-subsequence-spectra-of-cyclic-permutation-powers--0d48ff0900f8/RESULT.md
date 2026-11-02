# Square-subsequence spectra of cyclic permutation powers

## Finding
Fix an ordered alphabet \(\Sigma_q=\{0,1,\ldots,q-1\}\) with \(q\ge2\). For \(k\ge1\), let
\[
W_{q,k}=(0\,1\,\cdots\,(q-1))^k.
\]
For \(m\ge1\), let \(S_q(k,m)\) be the number of **distinct** words \(u\in\Sigma_q^m\) for which the concatenated square \(uu\) is a scattered subsequence of \(W_{q,k}\). A scattered subsequence preserves increasing index order; it need not occupy adjacent positions. Different index embeddings of the same word \(uu\) are counted once.

**Complete membership criterion.** For \(u=u_1\cdots u_m\), put
\[
r(u)=\sum_{i=1}^{m-1}\mathbf1_{\{u_{i+1}\le u_i\}},\qquad s(u)=\mathbf1_{\{u_1\le u_m\}}.
\]
Then, for all \(q\ge2\), \(k,m\ge1\), and \(u\in\Sigma_q^m\),
\[
\boxed{uu\preccurlyeq W_{q,k}\quad\Longleftrightarrow\quad 1+2r(u)+s(u)\le k.}
\]
Here \(\preccurlyeq\) denotes scattered-subsequence containment.

**Exact length-spectrum generating function.** Set \(H_q(x)=\sum_{j=0}^{q-1}\binom q{j+1}x^j\). In the formal power-series ring \(\mathbb Q[[z,v]]\), where \(z\) marks *whole permutation periods* and \(v\) marks *half the square length*, one has
\[
\boxed{\begin{aligned}
\mathcal F_q(z,v)&=\sum_{k\ge1}\sum_{m\ge1}S_q(k,m)z^k v^m\\
&=\frac{zv}{1-z}\,
\frac{zH_q(x)+(1-z)v z^2H_q'(x)}{1-vz^2H_q(x)},
\qquad x=v(1-z^2).
\end{aligned}}
\]
Thus every length-specific count is an explicit integer coefficient of a rational function, for every alphabet size and every host power. For example, when \(q=3\) and \(k=4\), the nonzero values \((S_3(4,1),\ldots,S_3(4,6))\) are \((3,9,17,15,6,1)\).

**Sharp longest-square classification.** Writing \(h=\lfloor k/2\rfloor\), the longest such square has length \(2qh\). If \(k=1\), no nonempty square occurs. If \(k=2h\ge2\), the unique longest square is \((0\,1\,\cdots\,(q-1))^{2h}\) (its root is \((0\,1\,\cdots\,(q-1))^h\)). If \(k=2h+1\ge3\), there are exactly \(q\) longest squares; their roots are the \(q\) cyclic rotations of \((0\,1\,\cdots\,(q-1))^h\).

## Assumptions and scope
The order on \(\Sigma_q\) is the usual numerical order, and all copies of the permutation period are identical, without an incomplete final block. The parameters \(q,k,m\) are positive integers with \(q\ge2\). A square means an exactly concatenated word \(uu\), not an Abelian square, shuffle square, or a square occurring contiguously in the host. The maximum-length statement concerns distinct square **strings**, not distinct embeddings. The generating function includes no empty-root term.

## Proof
**1. Greedy period cost.** To test a target \(a_1\cdots a_L\) against the infinite word \((0\,1\,\cdots\,(q-1))^\infty\), match each letter at its earliest position following the previous match. The next target symbol fits in the same period precisely when it is strictly larger than the preceding symbol; when it is equal or smaller, one additional full period is necessary and sufficient. Therefore the target requires exactly
\[
1+\sum_{i=1}^{L-1}\mathbf1_{\{a_{i+1}\le a_i\}}
\]
periods. Greedy matching is optimal because choosing any later occurrence cannot make any later target symbol match earlier. For \(a_1\cdots a_{2m}=uu\), the internal weak-descents of \(u\) occur twice, and the join between copies contributes \(s(u)\). This proves the stated necessary-and-sufficient criterion, including equality and boundary cases.

**2. Weighted transfer matrix.** Define the \(q\times q\) matrix \(M_q(t)\), with indices \(0,\ldots,q-1\), by
\[
(M_q(t))_{ij}=\begin{cases}1&i<j,\\t&i\ge j.\end{cases}
\]
For any \(m\ge1\), expansion of a matrix trace along the \(m\) cyclicly linked symbols of a root gives
\[
P_{q,m}(t):=\sum_{u\in\Sigma_q^m}t^{2r(u)+s(u)}
=\operatorname{tr}\!\left(M_q(t^2)^{m-1}M_q(t)\right).
\]
This identity holds also for \(m=1\): both sides equal \(qt\). For any exponent \(e\ge0\), \(\sum_{k\ge1,\,k\ge e+1}z^k=z^{e+1}/(1-z)\). Using the membership criterion and summing first over periods and then over root lengths yields
\[
\mathcal F_q(z,v)=\frac{zv}{1-z}\operatorname{tr}\left[(I-vM_q(z^2))^{-1}M_q(z)\right].
\]
All inverses are valid formal power series in \(v\).

**3. Evaluate the trace for all \(q\).** Write \(U\) for the strictly upper triangular all-ones matrix and \(J=\mathbf1\mathbf1^\top\) for the all-ones matrix. Then \(M_q(t)=(1-t)U+tJ\). Put \(x=v(1-z^2)\) and \(B=I-xU-vz^2J\). Since \(U\) is nilpotent,
\[
\mathbf1^\top(I-xU)^{-1}\mathbf1
=\sum_{j=0}^{q-1}\binom q{j+1}x^j=H_q(x).
\]
Indeed, the coefficient of \(x^j\) counts strictly increasing chains of \(j+1\) distinct indices in \(\Sigma_q\). The rank-one determinant lemma, together with \(\det(I-xU)=1\), gives \(\det B=1-vz^2H_q(x)\). The rank-one inverse formula implies
\[
\operatorname{tr}(B^{-1}J)
=\frac{H_q(x)}{1-vz^2H_q(x)}.
\]
Differentiating \(\log\det B\) in \(x\), holding \(vz^2\) fixed and using \(\partial_xB=-U\), gives
\[
\operatorname{tr}(B^{-1}U)
=\frac{vz^2H_q'(x)}{1-vz^2H_q(x)}.
\]
Substitute \(M_q(z)=(1-z)U+zJ\) into the trace from step 2 to obtain the displayed rational generating function. This is an identity of formal series; it does not rely on numerical matrix inversion or analytic convergence.

**4. Maximum length and its complete set of roots.** Each alphabet symbol occurs exactly \(k\) times in \(W_{q,k}\). A square \(uu\) therefore uses each symbol an even number of times, at most \(k\), so its root contains at most \(h=\lfloor k/2\rfloor\) copies of each symbol. Hence \(|u|\le qh\). The root consisting of \(h\) full ordered periods attains this bound for \(k\ge2\), proving the longest-square length; for \(k=1\) the bound forces absence.

To classify equality, take \(|u|=qh\) with \(h\ge1\), and let \(d=r(u)+s(u)\), the number of weak descents in the **cyclic** list \(u_1,\ldots,u_m,u_1\). Between two consecutive cyclic weak descents lies a strictly increasing run of length at most \(q\). Consequently \(d\ge h\). Since the membership criterion reads \(1+2d-s(u)\le k\), for \(k=2h\) or \(2h+1\) it forces \(d=h\). Equality in the run-length bound then forces each of the \(h\) cyclic increasing runs to contain all \(q\) letters in their only strictly increasing order. Thus \(u\) is a cyclic rotation of \((0\,1\,\cdots\,(q-1))^h\). Exactly one rotation starts at \(0\), and it has \(s(u)=1\); the other \(q-1\) rotations have \(s(u)=0\). At \(k=2h\), only the first passes \(1+2h-s(u)\le2h\); at \(k=2h+1\), all \(q\) pass. This proves uniqueness and multiplicities without assuming an exhaustive computer search.

## Verification
The accompanying standalone \`verify.py\` implements two genuinely different finite methods. First, for 24 selected host parameter pairs through \(q=8\), it enumerates **indexed** subsequences of the literal host, deduplicates square roots, and compares those sets to roots obtained by the weak-descent criterion. This checks 861 distinct appearing square roots and independently tests the longest-square multiplicities. Second, a transfer-state count of the weak-descent cost checks 780 integer coefficient identities of the cross-multiplied rational generating function across \(q=2,\ldots,7\), including boundary exponents and empty coefficient positions. The exact command and observed output are in \`VERIFICATION.md\`. These finite checks support but do not replace the all-parameter proof above.

## Relationship to prior work
Inoue, Inenaga, Hyyrö, Bannai, and Takeda (CPM 2018) analyze algorithms and hardness for longest **common** square subsequences of arbitrary strings. Inoue, Inenaga, and Bannai (2020) revisit the longest-square-subsequence problem with efficient general-input algorithms. Bannai, I, and Köppl (2022 preprint, journal title *Longest bordered and periodic subsequences*) give general procedures for finding longest periodic subsequences. These results concern optimization or algorithms on arbitrary inputs and do not state the distinct-square membership or root-length enumerator of the special host \(W_{q,k}\). He, Huang, Nam, and Thaper (2021 preprint) enumerate **shuffle squares**, whose defining predicate is the partition of a word into two interleaved identical subsequences; this is not the requirement that the sequentially concatenated square \(uu\) be a subsequence of a specified host. Prior cyclic-permutation results for minimally absent or palindromic subsequences examine other predicates, not the distinct-square spectrum. The present claim is the explicit root classification and rational bivariate spectrum, not the already-known existence of general square-subsequence algorithms.

## Limitations
This result counts distinct square strings, not their embedding multiplicity, and requires complete copies of a fixed permutation period. The formula does not automatically extend to unequal run lengths, incomplete last periods, interleaved shuffle squares, or general source words. Relevant prior results were checked by statement and by available main-text sections; an unlocated equivalent specialization remains a genuine originality risk. The correctness proof is mathematical; independent external validation has not been performed.

## References
1. T. Inoue, S. Inenaga, H. Hyyrö, H. Bannai, M. Takeda, *Computing longest common square subsequences*, CPM 2018, doi:10.4230/LIPIcs.CPM.2018.15, first public date used: 2018-05-18. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2018.15
2. H. Bannai, T. I, D. Köppl, *Longest (Sub-)Periodic Subsequence*, arXiv:2202.07189, initial public date: 2022-02-15. https://arxiv.org/abs/2202.07189
3. X. He, E. Huang, I. Nam, R. Thaper, *Shuffle Squares and Reverse Shuffle Squares*, arXiv:2109.12455, initial public date: 2021-09-25. https://arxiv.org/abs/2109.12455
4. T. Inoue, S. Inenaga, H. Bannai, *Longest Square Subsequence Problem Revisited*, arXiv:2006.00216, initial public date: 2020-05-30. https://arxiv.org/abs/2006.00216
