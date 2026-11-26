# Subexponential-list stability of rank-conditioned decoding reliability

## Finding

Let a codebook be sampled uniformly without replacement from \(\mathbb F_2^n\), with size \(M_n=2^{\lfloor nR\rfloor}\) for fixed \(0<R<1\). The transmitted codeword is uniform in the codebook and the additive noise \(N^n\) is independent of both the codebook and the transmitted word. Rank the noise patterns in nonincreasing order of likelihood, breaking ties in a fixed order. Write \(p_{n,j}\) for the probability of the pattern of rank \(j\), and \(I\) for the large-deviation rate function (in base two) of \(n^{-1}\log_2 G(N^n)\), where \(G\) is the noise rank.

Let \(2\le L_n<M_n\), \(\log_2 L_n=o(n)\), and consider top-list tuples \(q_{1,n}<\cdots<q_{L_n,n}\) of ranks. Suppose \(n^{-1}\log_2 q_{1,n}\to y_1\), \(n^{-1}\log_2 q_{2,n}\to y_2\), and \(n^{-1}\log_2 q_{L_n,n}\to y_L<1\). Set \(g(y)=I(y)+y\). Assume the following limits along these **actual rank sequences**:
\[
\begin{aligned}
-\frac1n\log_2 p_{n,q_{1,n}}&\longrightarrow g(y_1)<\infty,\\
-\frac1n\log_2 p_{n,q_{2,n}}&\longrightarrow g(y_2)<\infty,\\
-\frac1n\log_2\Pr\{G(N^n)>q_{L_n,n}\}&\longrightarrow \inf_{x\ge y_L}I(x).
\end{aligned}
\]
The tail is **strict**, may have infinite decay rate, and its limit does not follow from the support endpoint or from an LDP alone. Under the guesswork regularity of Struss, Médard, and Duffy [1], the above estimates apply when \(0\le y_1\le y_2\le y_L<H_0\), where \(H_0\) is the upper endpoint of the limiting guesswork support in their notation. This provides a sufficient interior regime that does not require distinct limiting rank exponents.

Define
\[
\Delta=\min\left\{g(y_2),\,1-R+\inf_{x\ge y_L}I(x)\right\}-g(y_1).
\]
Let \(S_n\) be the posterior probability that the first list entry is the transmitted codeword, conditioned on the top-list rank tuple in the random-codebook model. Then:

- If \(\Delta>0\), then \(S_n\to1\) and \(-n^{-1}\log_2(1-S_n)\to\Delta\).
- If \(\Delta<0\), then \(S_n\to0\) and \(-n^{-1}\log_2 S_n\to-\Delta\).

Thus the fixed-list formula for the strict-sign boundary still applies with subexponential list sizes. Only the first, second, and last limiting rank exponents enter the formula. If a different list length changes those exponents (in particular the last one), the formula need not give the same decision.

## Proof

Fix a received word. Translating the codebook by this word gives a set of distinct ranks. Among rank sets with the specified top-list tuple, there are \(\binom{2^n-q_{L_n,n}}{M_n-L_n}\) possible completions. For a putative transmitted rank equal to any listed rank, every completion is allowed. For a given unlisted rank beyond \(q_{L_n,n}\), the fraction of completions allowing it is \((M_n-L_n)/(2^n-q_{L_n,n})\); no other transmitted ranks are possible. In the joint probability that the received word and tuple occur and that a particular rank was transmitted, each allowed completion contributes the same common codebook and codeword factor times \(p_{n,j}\). This proves, also after summing over the received word, the exact posterior formula
\[
 S_n=\frac{p_{n,q_{1,n}}}{p_{n,q_{1,n}}+A_n+B_n},\qquad
 A_n=\sum_{i=2}^{L_n}p_{n,q_{i,n}},\qquad
 B_n=\frac{M_n-L_n}{2^n-q_{L_n,n}}\Pr\{G(N^n)>q_{L_n,n}\}.
\]
The combinatorial feasibility condition \(q_{L_n,n}\le 2^n-M_n+L_n\) holds eventually since \(R<1\) and \(y_L<1\). The finite point-rate assumption at the first rank gives positive likelihood eventually, so the conditioning event then has positive probability.

By the rank ordering,
\[
 p_{n,q_{2,n}}\le A_n\le (L_n-1)p_{n,q_{2,n}}.
\]
The factor \(L_n-1\) has zero exponential rate. Thus \(-n^{-1}\log_2 A_n\to g(y_2)\). Also \(M_n-L_n=2^{nR+o(n)}\) and \(2^n-q_{L_n,n}=2^{n+o(n)}\). By the strict-tail hypothesis, \(B_n\) has decay rate \(1-R+\inf_{x\ge y_L}I(x)\); this includes the convention \(-\log_2 0=+\infty\). Consequently \(D_n=(A_n+B_n)/p_{n,q_{1,n}}\) satisfies \(-n^{-1}\log_2 D_n\to\Delta\). If \(\Delta>0\), \(D_n\to0\) and \(1-S_n=D_n/(1+D_n)\) has decay rate \(\Delta\). If \(\Delta<0\), \(D_n\) diverges and \(S_n=1/(1+D_n)\) has decay rate \(-\Delta\).

## Why the strict-tail hypothesis matters

The point-mass window estimate in [1, Lemma 2] applies to moving ranks whose log-rank exponent converges to a point below \(H_0\). For the tail, use [1, Lemma 5] at fixed exponents \(y_L-\epsilon\) and \(y_L+\epsilon\) in that regime and squeeze by the ordering of the thresholds. Continuity of the tail rate there gives the moving-threshold limit. At \(y_L=0<H_0\), the upper bound on the probability is one, and the lower bound from a fixed positive exponent tending to zero gives rate zero. This argument does not supply a strict-tail estimate at \(H_0\) even when \(H_0<1\).

For example, let the noise be uniform on a binary subspace of dimension \(\lfloor hn\rfloor\), where \(0<h<1\), and put \(K_n=2^{\lfloor hn\rfloor}\). Its rank is uniform on \(\{1,\ldots,K_n\}\), and the rate function is \(I(x)=h-x\) for \(0\le x\le h\) and \(+\infty\) elsewhere. Choose \(L_n=n\) for large \(n\), \(q_{i,n}=i\) for \(i<n\), and \(q_{L_n,n}=K_n\). Then \(y_L=h<1\), but the strict tail is zero and \(\inf_{x\ge h}I(x)=0\). The exact posterior is \(S_n=1/n\). Substitution of the closed-set rate into the boundary formula without the tail hypothesis would instead predict a strictly positive success-decay exponent for \(R>1-h\).

## Verification, relationship to prior work, and limits

The proof is analytic: the finite posterior is a counting identity, and the exponential comparison uses the monotonicity of likelihood ranks and the three stated limits. The endpoint example is exact and illustrates the need for the tail condition; it is not used as evidence for the general positive result.

Struss, Médard, and Duffy [1, Propositions 1–2] give the finite posterior identity and analyze the boundary for fixed list size at fixed distinct interior rank exponents. Here the subexponential bound controls the aggregate over a growing list, with no alignment or separation assumption on its limiting exponents. Tavakoli [2, Definition 2 and Theorem 8] studies subexponential lists in a different quantity, the constrained-guesswork moment, rather than this posterior given the entire rank tuple.

The claim says nothing about \(\Delta=0\), exponential list growth, or a fixed structured codebook. It does not apply at a support endpoint unless the two point limits and the strict-tail limit are independently justified there.

## References

1. C. Struss, M. Médard, and K. R. Duffy, “Conditional Correctness in List Decoding: How a Late Second Codeword Can Rescue Confidence in the First,” arXiv:2610.02458v1. https://arxiv.org/abs/2610.02458v1
2. H. Tavakoli, “Guesswork Under Linear Constraints: Exact Exponent for Coset Decoding,” arXiv:2607.00205v2. https://arxiv.org/abs/2607.00205v2
