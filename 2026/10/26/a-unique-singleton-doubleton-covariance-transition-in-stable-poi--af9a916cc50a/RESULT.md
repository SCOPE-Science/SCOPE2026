# A unique singleton–doubleton covariance transition in stable Poisson–Dirichlet partitions

## Finding
Let \(M_{1,n}\) and \(M_{2,n}\) count blocks of sizes one and two in a sample of size \(n\) from the stable Poisson–Dirichlet partition \(\mathrm{PD}(\alpha,0)\), where \(n\ge3\) and \(0<\alpha<1\). For each such \(n\) there is exactly one \(\alpha_n\in(0,1)\) for which
\[\operatorname{Cov}(M_{1,n},M_{2,n})=0.\]
The covariance is strictly positive for \(0<\alpha<\alpha_n\) and strictly negative for \(\alpha_n<\alpha<1\). The thresholds strictly increase, and satisfy
\[\alpha_3=\frac{\sqrt{11/3}-1}{2},\qquad \alpha_3<\alpha_4<\cdots<1,\qquad \lim_{n\to\infty}n(1-\alpha_n)=2.\]
Equivalently, the exact covariance-sign ratio is
\[R_n(\alpha)=\frac{n-2}{n}\frac{\alpha\,(n-1)!\,(2\alpha)_{n-3}}{(\alpha)_{n-1}(\alpha)_{n-2}},\qquad\operatorname{sgn}\operatorname{Cov}(M_{1,n},M_{2,n})=\operatorname{sgn}(R_n(\alpha)-1),\]
with \((z)_k=z(z+1)\cdots(z+k-1)\), \((z)_0=1\).

## Assumptions and scope
The partition of \([n]\) follows the exchangeable Chinese restaurant process with discount \(0<\alpha<1\) and strength zero: start with one table; when \(m\) customers occupy \(k\) tables of sizes \(s_1,\ldots,s_k\), customer \(m+1\) joins table \(i\) with probability \((s_i-\alpha)/m\), or starts a table with probability \(k\alpha/m\). Only unconditional covariance of the two block-count statistics at finite \(n\) is considered. The discount parameter does not vary within the construction for a fixed \(n\), though the threshold sequence varies with \(n\).

## Proof
**Marked block events.** Exchangeability and the restaurant transition probabilities imply, for one designated vertex \(v\), one designated pair \(\{u,w\}\), and a disjoint designated singleton and pair, respectively,
\[\begin{aligned}
\Pr(\{v\}\text{ is a block})&=\frac{(\alpha)_{n-1}}{(n-1)!},\\
\Pr(\{u,w\}\text{ is a block})&=\frac{(1-\alpha)(\alpha)_{n-2}}{(n-1)!},\\
\Pr(\{v\}\text{ and }\{u,w\}\text{ are blocks})&=\frac{\alpha(1-\alpha)(2\alpha)_{n-3}}{(n-1)!}.
\end{aligned}\]
For instance, the last probability equals \(\alpha(1-\alpha)/2\) for the first three guests with respective membership patterns \(\{1\},\{2,3\}\), multiplied by \(\prod_{m=3}^{n-1}(m-3+2\alpha)/m\) to prevent later arrivals joining either marked table. There are \(n\) choices of singleton, \(\binom n2\) choices of pair, and \(n\binom{n-1}{2}\) choices of disjoint singleton and pair. Hence
\[\begin{aligned}
\mathbb E M_{1,n}&=\frac{n(\alpha)_{n-1}}{(n-1)!},\\
\mathbb E M_{2,n}&=\frac{\binom n2(1-\alpha)(\alpha)_{n-2}}{(n-1)!},\\
\mathbb E(M_{1,n}M_{2,n})&=\frac{n\binom{n-1}{2}\alpha(1-\alpha)(2\alpha)_{n-3}}{(n-1)!}.
\end{aligned}\]
The means are strictly positive, and their ratio with the product moment is precisely \(R_n(\alpha)\), establishing the sign equivalence.

**Exactly one zero.** Directly \(R_3(\alpha)=2/[3\alpha(1+\alpha)]\). For \(n\ge4\), canceling the factors with index zero yields
\[R_n(\alpha)=\frac{2(n-2)(n-1)!}{n}\,\frac{\prod_{j=1}^{n-4}(j+2\alpha)}{(n-2+\alpha)\prod_{j=1}^{n-3}(j+\alpha)^2}.\]
Every factor \((j+2\alpha)/(j+\alpha)^2\) is strictly decreasing for \(j\ge1\) because its logarithmic derivative is \(2/(j+2\alpha)-2/(j+\alpha)<0\); the remaining denominator terms also increase. Thus \(R_n\) strictly decreases on \((0,1)\). Its right endpoint is \(R_n(1)=(n-2)/n<1\); at the left endpoint \(R_3(0+)=\infty\), and for \(n\ge4\), \(R_n(0+)=2(n-1)(n-2)/[n(n-3)]>1\). The intermediate value theorem proves a unique threshold and the stated signs. Solving \(R_3(\alpha_3)=1\) gives the explicit \(\alpha_3\).

**Strict threshold ordering.** Elementary cancellation yields for every \(n\ge3\),
\[Q_n(\alpha):=\frac{R_{n+1}(\alpha)}{R_n(\alpha)}=\frac{n^2(n-1)(n-3+2\alpha)}{(n+1)(n-2)(n-1+\alpha)(n-2+\alpha)}.\]
This expression strictly increases with \(\alpha\in(0,1)\): its logarithmic derivative is \(2/(n-3+2\alpha)-1/(n-1+\alpha)-1/(n-2+\alpha)>0\). At \(\alpha=2/5\), exact factorization gives
\[Q_n(2/5)-1=\frac{2(13n^2-43n+24)}{(n-2)(n+1)(5n-8)(5n-3)}>0\quad(n\ge3).\]
Since \(\alpha_3>2/5\), induction shows that \(Q_n(\alpha_n)>1\) and hence \(R_{n+1}(\alpha_n)>1\); strict decrease of \(R_{n+1}\) forces \(\alpha_{n+1}>\alpha_n\).

**Limit and sharp scaling.** The gamma-ratio rule, for every fixed \(\alpha\in(0,1)\), gives
\[\lim_{n\to\infty}R_n(\alpha)=\frac{\alpha\Gamma(\alpha)^2}{\Gamma(2\alpha)}=\alpha B(\alpha,\alpha)>1.\]
The last strict inequality follows by integrating \((1-t)^{\alpha-1}>1\) against \(\alpha t^{\alpha-1}\) on \((0,1)\). Since \(R_n\) is decreasing in \(\alpha\), the thresholds eventually exceed every fixed \(\alpha<1\), proving \(\alpha_n\uparrow1\). Set \(F_n=\log R_n\). We have \(F_n(\alpha_n)=0\), \(F_n(1)=\log(1-2/n)=-2/n+O(n^{-2})\), and direct differentiation of the product formula yields \(F_n'(1)=-1-1/(n-1)\). Furthermore \(\sup_{n\ge3,\,1/2\le\alpha\le1}|F_n''(\alpha)|<\infty\): after differentiating, all index-dependent terms are dominated by convergent series of reciprocal squares; the \(n=3\) case is explicit. Since \(\alpha_n\to1\), the mean value theorem gives \(0=F_n(1)+F_n'(\xi_n)(\alpha_n-1)\) for some \(\xi_n\in(\alpha_n,1)\), with \(F_n'(\xi_n)\to-1\). Consequently \(n(1-\alpha_n)\to2\).

## Verification
The standalone standard-library script `verify.py` enumerates exact rational restaurant-state distributions for \(n=3,\ldots,9\) and five rational discounts; all three moment expressions agree exactly with their enumerated values. Independent numerical bisection checks the threshold ordering through \(n=1000\) and its asymptotic trend. These finite tests corroborate algebra but are not used to prove the universal statements, which are proved above. To reproduce: run `python verify.py` under Python 3.

## Relationship to prior work
Maller and Shemehsavar (2023), arXiv:2309.00815v1, define the frequency-of-frequencies vector and analyze its large-sample joint laws. Their Section 4.2, Theorem 4.2 and equation (4.16) give the two-parameter partition sampling formula and an asymptotic law, rather than the finite-sample zero of the singleton–doubleton covariance or its moving-discount boundary. The exact marked-block moments here are compatible with that known sampling formula, but the strict threshold, its monotonicity in sample size, and \(n(1-\alpha_n)\to2\) are additional comparisons derived here. Gnedin and Stark (2022), arXiv:2209.12781v1, treat Ewens-permutation cycle-count dynamics (an unrelated \(\alpha=0\), positive-strength regime). Searches for equivalent finite-discount phase diagrams found no matching statement; this is evidence-limited, not proof of priority.

## Limitations
The result concerns only strength-zero stable partitions, two particular block sizes, and unconditional covariance. It does not characterize other block-count pairs, conditional dependence, statistical estimators, or concentration. The limiting case \(\alpha=1\) is not a nondegenerate member of the model. The primary sampling formula is classical; neither the moment identities alone nor an unsuccessful literature search certify historical novelty. Earlier or unindexed treatments of the sign transition remain a residual priority risk. Independent verification beyond the stated reproducible finite checks is not claimed.

## References
1. R. Maller and S. Shemehsavar, *Limiting Behaviour of Poisson-Dirichlet and Generalised Poisson-Dirichlet Distributions*, arXiv:2309.00815v1 (2023-09-02), Sections 3 and 4.2, especially Theorem 4.2 and Eq. (4.16). https://arxiv.org/pdf/2309.00815
2. A. Gnedin and D. Stark, *Random Permutations and Queues*, arXiv:2209.12781v1 (2022-09-26), Sections 1–2. https://arxiv.org/pdf/2209.12781
3. J. Pitman and M. Yor, *The two-parameter Poisson–Dirichlet distribution derived from a stable subordinator*, Annals of Probability 25 (1997), 855–900, Section A.2, as cited by Maller and Shemehsavar.
