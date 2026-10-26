# Subexponential-list stability of rank-conditioned decoding reliability

## Finding

Consider a uniformly random codebook of size \(M_n=2^{\lfloor nR\rfloor}\) in \(\mathbb F_2^n\), with fixed rate \(R\in(0,1)\). Let additive-noise patterns be ranked as \(z_{n,1},\ldots,z_{n,2^n}\) in nonincreasing order of likelihood, and write \(p_{n,j}=\Pr[N^n=z_{n,j}]\). For the top \(L_n\) codeword candidates, let their noise ranks be \(q_{1,n}<\cdots<q_{L_n,n}\), where \(2\le L_n<M_n\) and \(\log_2 L_n=o(n)\).

Assume the same guesswork large-deviation hypotheses used for the fixed-list rank-conditioned reliability theorem. In particular, at the relevant points, let \(I(y)\) be the rate function for \(n^{-1}\log_2 G(N^n)\), let \(g(y)=I(y)+y\) be the point-rank exponent, and suppose
\[
\frac1n\log_2 q_{1,n}\to y_1,\qquad
\frac1n\log_2 q_{2,n}\to y_2,\qquad
\frac1n\log_2 q_{L_n,n}\to y_L<1.
\]
Define
\[
\Delta=\min\left\{g(y_2),\,1-R+\inf_{x\ge y_L}I(x)\right\}-g(y_1).
\]
Then, whenever \(\Delta\ne0\), the posterior probability \(S_n\) that the first list entry is the transmitted codeword has the same first-order reliability boundary as in the fixed-list theorem:

- If \(\Delta>0\), then \(S_n\to1\) and \(-n^{-1}\log_2(1-S_n)\to\Delta\).
- If \(\Delta<0\), then \(S_n\to0\) and \(-n^{-1}\log_2 S_n\to-\Delta\).

Thus polynomial-size lists, and more generally any subexponential-size lists, do not change the first-order rank-conditioned reliability decision away from \(\Delta=0\); only the first, second, and last rank exponents enter the boundary.

## Assumptions and scope

The codebook is uniformly sampled without replacement from \(\mathbb F_2^n\), the transmitted codeword is uniform in the codebook, and the additive noise is independent of the codeword. The likelihood ranking and the large-deviation regularity assumptions are those of Struss, Médard, and Duffy's fixed-list analysis. The result requires \(R>0\), \(L_n=2^{o(n)}\), and a last-rank exponent \(y_L<1\), so that \(2^n-q_{L_n,n}\) has exponent one. It makes no claim at the critical boundary \(\Delta=0\), for exponentially growing list sizes, or for arbitrary fixed codebooks.

## Proof

For a uniform random codebook, conditioning on the observed top-list ranks gives the exact posterior expression
\[
S_n=\frac{p_{n,q_{1,n}}}{p_{n,q_{1,n}}+A_n+B_n},
\]
where
\[
A_n=\sum_{i=2}^{L_n}p_{n,q_{i,n}},\qquad
B_n=\frac{M_n-L_n}{2^n-q_{L_n,n}}\sum_{j=q_{L_n,n}+1}^{2^n}p_{n,j}.
\]
The factor in \(B_n\) is the conditional inclusion probability for each unlisted rank: among the \(2^n-q_{L_n,n}\) ranks beyond the list, exactly \(M_n-L_n\) are selected as remaining codewords on average.

Because the rank probabilities are nonincreasing and \(q_{i,n}\ge q_{2,n}\) for every \(i\ge2\),
\[
p_{n,q_{2,n}}\le A_n\le L_n p_{n,q_{2,n}}.
\]
Taking \(-n^{-1}\log_2\) and using \(n^{-1}\log_2 L_n\to0\) shows that \(A_n\) has the same exponential rate \(g(y_2)\) as \(p_{n,q_{2,n}}\). This is the only step that needs more than fixed list size.

Next, \(M_n-L_n=2^{nR+o(n)}\) because \(R>0\) and \(L_n=2^{o(n)}\). Since \(y_L<1\),
\[
2^n-q_{L_n,n}=2^{n+o(n)}.
\]
The tail large-deviation limit therefore gives the exponential rate \(1-R+\inf_{x\ge y_L}I(x)\) for \(B_n\). The numerator \(p_{n,q_{1,n}}\) has rate \(g(y_1)\). Consequently, the ratio \((A_n+B_n)/p_{n,q_{1,n}}\) has exponential rate \(-\Delta\).

If \(\Delta>0\), that ratio tends to zero exponentially, so \(S_n\to1\), with error exponent \(\Delta\). If \(\Delta<0\), the ratio diverges exponentially, so \(S_n\to0\), with exponent \(-\Delta\). At \(\Delta=0\), exponential-rate information alone cannot decide the limit. This proves the claim.

## Verification

The proof uses the exact conditional posterior formula from the random-codebook model, the monotonicity of likelihood-ranked probabilities, the subexponential bound \(A_n\le L_n p_{n,q_{2,n}}\), and the same tail large-deviation limit as the fixed-list theorem. No finite simulation is used as an infinite proof. The boundary case \(\Delta=0\) is excluded explicitly.

## Relationship to prior work

Struss, Médard, and Duffy, arXiv:2610.02458, derive the exact rank-conditioned posterior formula and the decision function for a **fixed** list size; their paper explicitly states that it considers fixed \(L\). The present extension supplies the missing uniformity argument for \(L_n=2^{o(n)}\): the aggregate contribution of all intermediate list entries is exponentially equivalent to the second entry because the list-size factor has zero exponential rate.

Tavakoli, arXiv:2607.00205, proves that subexponential lists do not change a first-order **guesswork-moment exponent**. That is related context, but it is not the posterior probability of the first list entry conditioned on the complete list-rank tuple, and it does not establish the decision boundary above. The result here does not claim a new guesswork-moment theorem.

## Limitations

The theorem is conditional on the large-deviation and point-rank limits in the fixed-list framework. It is an asymptotic statement for the uniform random-codebook model, not a guarantee for every structured code. It does not resolve the critical surface \(\Delta=0\), and the argument does not extend unchanged to exponentially growing lists, for which \(n^{-1}\log_2 L_n\) need not vanish. Independent review has not been performed.

## References

1. C. Struss, M. Médard, and K. R. Duffy, “Conditional Correctness in List Decoding: How a Late Second Codeword Can Rescue Confidence in the First,” arXiv:2610.02458, first posted 2026-10-01. https://arxiv.org/abs/2610.02458
2. H. Tavakoli, “Guesswork Under Linear Constraints: Exact Exponent for Coset Decoding,” arXiv:2607.00205, first posted 2026-06-30. https://arxiv.org/abs/2607.00205
