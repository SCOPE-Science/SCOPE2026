# Finite-sample two-switch law for long-run counts in Bernoulli trials

## Finding
Let \(X_1,\ldots,X_n\) be independent Bernoulli\((p)\) variables, with \(0<p<1\), and let \(n\ge k\ge2\). A **success run** is a maximal consecutive block of ones. Write \(R_n\) for the number of all success runs and \(T_{n,k}\) for the number of success runs of length at least \(k\). Put \(q=1-p\).

For \(n=k\), the covariance is
\[
\operatorname{Cov}(R_n,T_{n,k})=p^kq[1-(k-1)p].
\]
For \(n\ge k+1\), writing \(s=n-k\), the exact finite-sample covariance is
\[
\operatorname{Cov}(R_n,T_{n,k})=p^kq H_{s,k}(p),\qquad
H_{s,k}(p)=(s+1)-[(k+2)s+k-1]p+[(k+2)s-2]p^2.
\]
Its sign admits a complete classification:

1. For \(k\ge3\) and \(n=k\), the single interior sign switch is \(p=1/(k-1)\). For \(k\ge3\) and \(n\ge k+1\), \(H_{s,k}\) has two positive real roots \(p_-<1/2<p_+\). There is always exactly one interior switch \(p_-\). A **second** interior switch occurs if and only if \(n>2k\): in that case \(p_+<1\), and covariance has signs positive, negative, positive in the intervals determined by \(p_-\) and \(p_+\). If \(n=2k\) then \(p_+=1\); if \(k+1\le n<2k\), then \(p_+>1\), and the covariance stays negative from \(p_-\) to \(1\).
2. For \(k=2\), the case \(n=2\) has strictly positive covariance. For every \(n\ge3\), \(p_-=1/2\) is an interior root. A second interior root occurs exactly for \(n\ge5\) and equals \(p_+=(n-1)/(2n-5)\). For \(n=4\) the second root is \(1\), and for \(n=3\) it is \(2\). Signs are positive before \(1/2\), negative just after \(1/2\), and (when the second interior root exists) positive beyond it.

For fixed \(k\ge3\), the two roots converge as \(n\to\infty\) to
\[
\frac{1\pm\sqrt{1-4/(k+2)}}{2}.
\]
For \(k=2\), by contrast, the width of the negative-covariance interval is exactly \(3/(4n-10)\), which tends to zero. The threshold \(n=2k+1\) is the first word length that can contain **two** success runs each of length at least \(k\), separated by a zero.

## Assumptions and scope
The trials are mutually independent with a **common** success probability \(p\). Runs are maximal blocks, counted once each even if longer than \(k\); no circular wrap-around is used. The entire classification holds for the finite word, with no asymptotic or approximation assumptions. Only positive integer parameters \(n\ge k\ge2\) and \(0<p<1\) are asserted. Roots at \(p=1\) are boundary values, not interior sign switches. When \(n<k\), \(T_{n,k}=0\) identically, outside the nontrivial claim.

## Proof
Define the start-of-run indicators
\[
A_i=\mathbf1\{X_i=1,\ i=1\text{ or }X_{i-1}=0\},\quad 1\le i\le n,
\]
and the long-run start indicators
\[
B_j=\mathbf1\{X_j=\cdots=X_{j+k-1}=1,\ j=1\text{ or }X_{j-1}=0\},\quad1\le j\le n-k+1.
\]
Then \(R_n=\sum_i A_i\), \(T_{n,k}=\sum_j B_j\), \(\mathbb EA_1=p\), \(\mathbb EA_i=pq\) for \(i\ge2\), \(\mathbb EB_1=p^k\), and \(\mathbb EB_j=qp^k\) for \(j\ge2\). In particular
\[
\mathbb ER_n=p+(n-1)pq,\qquad \mathbb ET_{n,k}=p^k[1+(n-k)q].
\]

Fix \(j\) and put \(F_j=[j-1,j+k]\cap[1,n]\), with the left endpoint replaced by \(1\) when \(j=1\). If \(i=j\), then \(A_iB_j=B_j\). For each other \(i\in F_j\), a required zero for \(A_i\) contradicts one of the bits fixed by \(B_j\), so \(A_iB_j=0\). For \(i\notin F_j\), the respective events use disjoint sets of independent bits, and \(A_i\) and \(B_j\) are independent. Therefore
\[
\operatorname{Cov}(R_n,B_j)
=\mathbb EB_j\left(1-\sum_{i\in F_j}\mathbb EA_i\right).
\]
This identity includes both endpoints of the word. Summing over the \(n-k+1\) eligible long-run starting positions, using the four boundary cases \(j=1\), \(j=2\), \(3\le j\le n-k\), and \(j=n-k+1\) (empty ranges omitted), yields, when \(n\ge k+1\),
\[
\begin{aligned}
\operatorname{Cov}(R_n,T_{n,k})
&=p^kq\bigl((s+1)-[(k+2)s+k-1]p\\
&\hspace{32mm}+[(k+2)s-2]p^2\bigr).
\end{aligned}
\]
The overlap formula may be checked directly in the shortest case \(n=k+1\), where there are just two positions \(j\). When \(n=k\), only \(j=1\) is possible; substituting \(F_1=[1,k]\) gives the separate formula \(p^kq[1-(k-1)p]\).

For \(n\ge k+1\), the quadratic's leading coefficient \((k+2)s-2\) is strictly positive, while
\[
H_{s,k}(0)=s+1>0,\qquad H_{s,k}(1)=s-k=n-2k,\qquad H_{s,k}(1/2)=-\frac{(k-2)(s+2)}4.
\]
For \(k\ge3\), its value at \(1/2\) is strictly negative; hence one root lies in \((0,1/2)\), the other lies above \(1/2\), and the sign and position of \(H_{s,k}(1)\) determine whether the latter lies below, at, or above \(1\). The sign pattern follows because the parabola opens upward. The case \(n=k\) is immediate from its linear factor. For \(k=2\) a direct factorization is
\[
H_{s,2}(p)=(1-2p)[(s+1)-(2s-1)p].
\]
Consequently the roots are \(1/2\) and \((s+1)/(2s-1)\), with their placement exactly as stated. Finally, dividing the quadratic by \(s\) proves convergence of the two roots for fixed \(k\ge3\), and direct subtraction gives the \(k=2\) interval width.

## Verification
The standalone `verify.py` uses only the Python standard library. It enumerates all binary words through length 12 with exact rational weights, independently computing the three moments \(\mathbb ER_n\), \(\mathbb ET_{n,k}\), and \(\mathbb E(R_nT_{n,k})\). It checks equality with the claimed formulas at three rational success probabilities for all \(2\le k\le n\le12\) (198 exact checks). It also checks the root placements for 3,002 parameter pairs and compares 37 limiting-root predictions with large finite samples. Run `python3 verify.py` in a directory containing this file. The exact proof above, not the finite tests, establishes the universal result.

## Relationship to prior work
Makri and Psillakis, *On Success Runs of Length Exceeded a Threshold* (first available online July 18, 2009), investigate the distribution, mean and variance of the count of runs exceeding a fixed threshold, including Bernoulli words. The present result does **not** claim this marginal law, its moments, or run-indicator technology as new. Stefanov (2000) and Mytalas–Zazanis (2013) provide multivariate asymptotic laws and covariance machinery for several run-counting conventions; the leading \(n\)-order coefficient here is consistent with and obtainable from that general literature. The assessed contribution is the **explicit finite-word two-root classification**, including the exact finite feasibility boundary \(n>2k\), the boundary cases, and the shrinking exceptional \(k=2\) phase. This is not a new CLT or a new marginal distribution.

## Limitations
This is an analytic finite-sample identity and sign classification, not a new independence statement, stochastic-order result, or extension to dependent or nonidentically distributed observations. General earlier joint-distribution machinery can in principle imply finite moments. A prior work deriving the same finite covariance polynomial or the same two-root classification would cover this result; available comparisons did not reveal such a derivation, but no exhaustive claim of novelty is made. The all-runs count means **success runs only**, not success plus failure runs. Independent validation and independent scientific audit have not been performed.

## References
- F. S. Makri and Z. M. Psillakis, *On Success Runs of Length Exceeded a Threshold*, Methodology and Computing in Applied Probability 13 (2011), 269–305, DOI 10.1007/s11009-009-9147-1. The primary text states “Published online: 18 July 2009.” https://www.researchgate.net/publication/225145624_On_Success_Runs_of_Length_Exceeded_a_Threshold
- V. T. Stefanov, *On run statistics for binary trials*, Journal of Statistical Planning and Inference 87 (2000), 177–185, DOI 10.1016/S0378-3758(99)00191-3. https://www.researchgate.net/publication/223159926_On_run_statistics_for_binary_trials
- G. C. Mytalas and M. A. Zazanis, *Central Limit Theorem approximations for the number of runs in Markov-dependent binary sequences*, Journal of Statistical Planning and Inference 143 (2013), 321–333, DOI 10.1016/j.jspi.2012.07.014. https://www.researchgate.net/publication/257199413_Central_Limit_Theorem_approximations_for_the_number_of_runs_in_Markov-dependent_binary_sequences
- J. C. Fu, *Distribution Theory of Runs and Patterns of Multi-state Trials*, Statistica Sinica 6 (1996), 957–974. https://www3.stat.sinica.edu.tw/statistica/password.asp?art=10&num=4&vol=6
