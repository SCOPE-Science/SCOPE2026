# A flat left-endpoint covariance kernel for permutation records and inversions

## Finding
Let \(\pi\) be uniform on \(S_n\), let \(R_k\) indicate that the value at position \(k\) is a new left-to-right maximum, and let \(X_{ij}\) indicate that the pair of positions \(i<j\) is inverted. The *complete cross-covariance kernel* is

\[
\operatorname{Cov}(R_k,X_{ij})=
\begin{cases}
\dfrac{k-1}{2k(k+1)},&k=i,\\
-\dfrac1{2k(k+1)},&i<k<j,\\
-\dfrac1{2k},&k=j,\\
0,&\text{otherwise}.
\end{cases}
\]

Writing \(R=\sum_{k=1}^nR_k\), summation gives a striking *right-endpoint-flat* covariance:

\[
\boxed{\operatorname{Cov}(R,X_{ij})=-\frac{1}{2i(i+1)}\quad(1\le i<j\le n).}
\]

For any deterministic real array \(w=(w_{ij})_{i<j}\), define its weighted inversion statistic \(I_w=\sum_{i<j}w_{ij}X_{ij}\). Then

\[
\operatorname{Cov}(R,I_w)=-\frac12\sum_{i<j}\frac{w_{ij}}{i(i+1)}.
\]

It is strictly negative for every nonzero nonnegative weight array. In particular, writing \(H_n=\sum_{k=1}^n1/k\) and \(I=\sum_{i<j}X_{ij}\), one recovers \(\operatorname{Cov}(R,I)=-(n-H_n)/2\). The aggregate covariance is contextual; the new assertion is the full local kernel and its right-endpoint independence.

## Assumptions and scope
All indices are integers, \(n\ge2\), \(1\le k\le n\), \(1\le i<j\le n\). The permutation is uniformly random. By rank invariance, the same conclusions hold when \(\pi\) is obtained by ranking any \(n\) independent observations from a common atomless distribution. The inversion comparison is *strict*. The weighted identity permits arbitrary real deterministic weights; the strict sign assertion requires nonnegative weights with at least one strictly positive entry. No asymptotic assumption is used.

## Proof
Write \(A_k=\{R_k=1\}\). Because the maximum of the first \(k\) relative ranks is equally likely at any of their positions, \(\mathbb P(A_k)=1/k\). For each \(i<j\), symmetry gives \(\mathbb P(X_{ij}=1)=1/2\); hence

\[
\operatorname{Cov}(R_k,X_{ij})=\frac1k\left(\mathbb P(X_{ij}=1\mid A_k)-\frac12\right).
\]

If \(k=i\), the largest of the first \(k+1\) relative ranks belongs to position \(k\) rather than position \(j\) with conditional probability \(k/(k+1)\): among the \(k\) prefix positions, position \(k\) is known to carry the prefix maximum, and position \(j\) lies outside that prefix. More formally, conditioning on the relative order in the first \(k\) positions makes the event that their maximum exceeds \(\pi(j)\) have probability \(k/(k+1)\). Therefore the covariance is \((k-1)/(2k(k+1))\).

If \(k=j\), then \(A_k\) forces \(\pi(j)>\pi(i)\), so the conditional inversion probability is zero and the covariance is \(-1/(2k)\).

If \(i<k<j\), the event \(A_k\) is independent of the unordered set of values occupying the first \(k\) sites together with position \(j\). Therefore the *sum* of the conditional probabilities of the \(k\) comparisons \(\pi(a)>\pi(j)\), for \(1\le a\le k\), equals \(k/2\). The comparison with site \(k\) has conditional probability \(k/(k+1)\). Exchangeability of the other \(k-1\) prefix positions gives, for each \(i<k\),

\[
\mathbb P(\pi(i)>\pi(j)\mid A_k)
=\frac{k/2-k/(k+1)}{k-1}
=\frac{k}{2(k+1)}.
\]

Hence the covariance is \(-1/(2k(k+1))\). Finally, if \(k<i\), the two positions \(i,j\) remain exchangeable conditional on \(A_k\), and if \(k>j\), the ordering of the first \(k-1\) positions remains uniform conditional on \(A_k\). Both yield conditional comparison probability \(1/2\), establishing the zero cases.

Summing the nonzero cases over \(k\) (an empty intermediate sum is interpreted as zero) yields

\[
\begin{aligned}
\operatorname{Cov}(R,X_{ij})
&=\frac{i-1}{2i(i+1)}
-\frac12\sum_{k=i+1}^{j-1}\frac1{k(k+1)}
-\frac1{2j}\\
&=\frac{i-1}{2i(i+1)}
-\frac12\left(\frac1{i+1}-\frac1j\right)
-\frac1{2j}\\
&=-\frac1{2i(i+1)}.
\end{aligned}
\]

This cancellation removes every dependence on \(j\). Linearity of covariance proves the weighted identity. In the unweighted case, summing over \(i<j\) gives \(-\frac12\sum_{i=1}^{n-1}(n-i)/(i(i+1))=-(n-H_n)/2\). All statements follow.

## Verification
The accompanying standalone Python checker `verify.py` uses exhaustive enumeration of \(S_n\) for every \(2\le n\le8\), computing exact rational means and covariances *directly* from each permutation rather than from conditional-probability arguments. It verifies each local cross-covariance, every right-endpoint-flat row, and an independent nonconstant pair-weight identity: **644 exact assertions passed**. Run `python verify.py` in the directory containing the extracted file. This finite check supplements, but does not replace, the preceding all-order proof.

## Relationship to prior work
Katzenbeisser (1988, 1990) studied the **joint distribution of aggregate record and inversion counts**; Chao, Chen and Cheng (2003) studied asymptotic joint normality. Their aggregate focus differs from the present position-resolved \(n\)-by-\(\binom n2\) cross-covariance kernel. The scalar aggregate moment follows by summation and is **not** claimed to be new. Gnedin and Gorin (arXiv:1202.3680, first submitted February 16, 2012) analyze record-dependent permutation laws, rather than the local inversion kernel. Existing local record–descent dependence corresponds to the adjacent subfamily \(j=i+1\), but does not imply the independence from right endpoint for all nonadjacent \(j\). The new statement is the complete nonadjacent kernel and cancellation.

## Limitations
The 1988 and 1990 Katzenbeisser full texts were not available for full-text inspection; comparisons to them use publisher abstracts and bibliographic descriptions, leaving possible implicit earlier appearance of the position-resolved identity as a historical-priority risk. The 2003 paper was inspected through its public abstract. No claim of priority, independent audit, or statistical model beyond uniform ranks is made. The covariance is a second-order statement only; it does not imply independence or a sign for weighted sums with mixed-sign coefficients.

## References
- W. Katzenbeisser, “On the joint distribution of the random variables ‘number of inversions’ and ‘number of outstanding variables’ in a randomly arranged sequence,” *Statistical Papers* **29** (1988), 133–141. https://doi.org/10.1007/BF02924518
- W. Katzenbeisser, “On the joint distribution of the number of upper and lower records and the number of inversions in a random sequence,” *Advances in Applied Probability* **22** (1990), 957–960. https://doi.org/10.2307/1427570
- C.-C. Chao, Y.-L. Chen, and W.-H. Cheng, “The asymptotic joint normality of the numbers of upper records, lower records and inversions in a random sequence,” *Journal of Applied Probability* **40** (2003), 257–263. https://doi.org/10.1239/jap/1044476839
- A. Gnedin and V. Gorin, “Record-dependent measures on the symmetric groups,” arXiv:1202.3680 (first public submission 2012-02-16). https://arxiv.org/abs/1202.3680
