# Strict likelihood-ratio ordering of first quota winners in unequal-probability sampling

## Finding
Fix integers \(m\ge 2\) and \(r\ge 2\). Draw independently from \(m\) categories with fixed positive probabilities \(p_1,\ldots,p_m\), summing to one. Let \(T\) be the first draw at which any category has been observed \(r\) times and let \(L\) be that category. If \(p_i<p_j\), then for **every** integer \(r\le t<m(r-1)+1\),
\[
\Pr(T=t+1,L=i)\Pr(T=t,L=j)
>\Pr(T=t,L=i)\Pr(T=t+1,L=j).
\]
Equivalently, the conditional odds \(\Pr(L=i\mid T=t)/\Pr(L=j\mid T=t)\) strictly increase throughout the entire support of \(T\). In particular, \(T\mid L=i\) is larger than \(T\mid L=j\) in strict monotone likelihood-ratio order. The odds have the sharp endpoints
\[
\frac{\Pr(L=i\mid T=r)}{\Pr(L=j\mid T=r)}
=\left(\frac{p_i}{p_j}\right)^r,
\qquad
\frac{\Pr(L=i\mid T=m(r-1)+1)}{\Pr(L=j\mid T=m(r-1)+1)}
=\frac{p_i}{p_j}.
\]
If \(p_i=p_j\), the two conditional time laws and corresponding odds coincide, by symmetry. Thus the winner and completion time are independent when all category probabilities are equal; unequal probabilities yield nontrivial marked-time dependence.

## Assumptions and scope
Sampling is independent, with replacement, over a finite set of \(m\ge2\) categories, with time-homogeneous strictly positive probabilities summing to one. All categories have the **same integer quota** \(r\ge2\). The stopping time is the first quota *completion*, not the time all categories complete or the first time a quota is met by a specified category. Its support is exactly the integers from \(r\) to \(m(r-1)+1\), since a prefix before the first completion contains at most \(r-1\) occurrences of each category. Every pair \((T=t,L=i)\) in this range has positive probability.

Define the truncated exponential polynomial
\[
E_{r-1}(u)=\sum_{a=0}^{r-1}\frac{u^a}{a!}.
\]
For each category \(i\), with \(k=t-r\), exact counting gives
\[
W_i(t):=\Pr(T=t,L=i)
=\frac{(t-1)!}{(r-1)!}\,p_i^r\,[z^{k}]\prod_{h\ne i}E_{r-1}(p_hz).
\tag{1}
\]
The comparison is about the full *marked* completion-time distribution, not only its marginal waiting-time law or its probability of a given winner.

## Proof
**Exact joint mass.** On \(\{T=t,L=i\}\), the first \(t-1\) draws contain exactly \(r-1\) occurrences of type \(i\) and at most \(r-1\) of every other type, after which the last draw is of type \(i\). Expanding the multinomial weight of all admissible prefixes proves (1), including its endpoints and full positive support.

**A strict convolution lemma.** A finite sequence \((a_0,\ldots,a_A)\) is strictly positive and strictly log-concave on its support if every \(a_u>0\) and \(a_u^2>a_{u-1}a_{u+1}\), using zeros outside the support. The Toeplitz kernel \(H_a(k,s)=a_{k-s}\), extended by zero, has nonnegative minors of order two: log-concavity makes the ratios of consecutive positive terms nonincreasing, which is equivalent to the total positivity of order two of this kernel.

If \(a\) and \(b\) have this property with supports \([0,A]\) and \([0,B]\), their convolution \(c=a*b\) does also. Indeed, \(H_c=H_aH_b\), so the Cauchy–Binet formula makes every order-two minor nonnegative. For the adjacent minor determining strict log-concavity of \(c\) at any \(0\le k<A+B\), choose intermediate columns \(s,s+1\), where \(s=\max\{0,k-A\}\). Then \(0\le s\le B-1\) and \(0\le u=k-s\le A\); the corresponding Cauchy–Binet summand is
\[
\bigl(a_u^2-a_{u-1}a_{u+1}\bigr)
\bigl(b_s^2-b_{s-1}b_{s+1}\bigr)>0.
\]
At \(k=A+B\) strictness follows from \(c_{A+B}>0\) and \(c_{A+B+1}=0\). This proves strict log-concavity for arbitrary finite convolutions of such sequences; the unit point mass at zero is an admissible identity factor. In particular, \((p^s/s!)_{0\le s\le r-1}\) is strictly positive and strictly log-concave for every \(p>0\), and so is any product's coefficient sequence.

**Likelihood-ratio determinant.** Fix \(i\ne j\). Set
\[
q_u=[z^u]\prod_{h\notin\{i,j\}}E_{r-1}(p_hz),
\qquad
B_x(k)=\sum_{s=0}^{r-1}q_{k-s}\frac{x^s}{s!},
\]
with zero coefficients outside their nonnegative support. Here \(q\) has full support \([0,Q]\), where \(Q=(m-2)(r-1)\), and is strictly log-concave (including the unit-point-mass case \(m=2\)). Formula (1) becomes
\[
\frac{W_i(t)}{W_j(t)}
=\left(\frac{p_i}{p_j}\right)^r
\frac{B_{p_j}(t-r)}{B_{p_i}(t-r)}.
\tag{2}
\]
For \(0<x<y\) and \(0\le k<(m-1)(r-1)\), apply the order-two Cauchy–Binet formula to the product of the Toeplitz kernel \(q_{k-s}\) and the two-column matrix \(a_s(x)=x^s/s!\), \(a_s(y)=y^s/s!\). All contributing summands are nonnegative. One is strictly positive: take \(s=\max\{0,k-Q\}\), which satisfies \(0\le s\le r-2\) and \(u=k-s\in[0,Q]\). Its two determinants are
\[
q_u^2-q_{u-1}q_{u+1}>0
\quad\text{and}\quad
\frac{x^sy^s(y-x)}{s!(s+1)!}>0.
\]
Consequently
\[
B_x(k)B_y(k+1)-B_y(k)B_x(k+1)>0.
\tag{3}
\]
Taking \(x=p_i\), \(y=p_j\) in (2) and (3) proves the asserted strict increase for all consecutive feasible completion times. Multiplying rows or columns by positive normalizing factors preserves the likelihood-ratio inequality, so the conditional law \(T\mid L=i\) is strictly larger in monotone likelihood-ratio order when \(p_i<p_j\).

Finally, at \(k=0\), all \(B_x(0)=1\); at \(k=(m-1)(r-1)\), \(B_x(k)\) is proportional to \(x^{r-1}\). Substitution in (2) gives the two exact endpoint odds. Symmetry under exchanging equal-probability labels proves the equality case. The proof covers every finite \(m,r\) and all positive, not necessarily rational, probabilities.

## Verification
An independent exact-rational program, `verify_quota.py`, builds the joint marked-time law two ways: by coefficient extraction in (1), and by an absorbing occupancy-state dynamic program. It exhaustively compares all cells and the strict neighboring inequalities for \(m\in\{2,3,4,5\}\), \(r\in\{2,3,4\}\), and all positive integer probability-weight profiles with entries in \(\{1,2,3,4\}\) for \(m\le4\) or \(\{1,2,3\}\) for \(m=5\). This comprises 1,737 exact-arithmetic profiles. A third independent full-word enumeration also checks small parameters. All checks passed.

For example, at \((p_1,p_2,p_3)=(1/2,1/3,1/6)\), the odds of type three versus type one at quota \(r=3\), for \(t=3,4,5,6,7\), are respectively \(1/27,5/81,25/243,5/27,1/3\), all strictly increasing. The code and captured output are included alongside this result. Finite exact calculations **illustrate** the all-parameter statement; the proof above, rather than enumeration, establishes it.

## Relationship to prior work
Camarri and Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities* (Berkeley Technical Report 523, publicly dated 1 June 1998; *Electronic Journal of Probability* 5, 2000), derive marginal repeat-time formulas and random-tree relations. Their equations (1)–(2) and Section 3.1 concern first-repeat times and observed sets, not an all-time monotone likelihood-ratio comparison of the winning repeated category. Camarri, *Asymptotics for k-fold repeats in the birthday problem with unequal probabilities* (Berkeley Technical Report 524, publicly dated 1 July 1998), extends repeat-time asymptotics and point-process structure to multiple hits, but the full text examined does not state the finite marked-winner ordering established here.

Aston and Martin, *Waiting time distributions of competing patterns in higher-order Markovian sequences* (*Journal of Applied Probability* 42, 2005), Section 3.3, supply a broad finite-state method for time-dependent absorption probabilities of competing patterns, which can numerically express the present joint law. Their formula (3.3) does not establish, or imply without a separate inequality argument, strict likelihood-ratio monotonicity uniformly over positive sampling probabilities, categories and quotas. Anderson, Sobel and Uppuluri, *Quota fulfillment times* (*Canadian Journal of Statistics* 10, 1982), address exact/asymptotic quota waiting-time distributions; its full text was not accessible during this review. Its potential bearing on priority is therefore a specifically disclosed risk, not a claim of full-text noncoverage.

The new assertion is the universal **strict two-parameter determinant sign** for the pair \((T,L)\), with exact endpoints. Ordinary formulas for \(\Pr(T=t)\), marginal winner probabilities, or finite-state transition matrices do not themselves give this strong order. Similar-sounding complete coupon collection is a different stopping rule: there one waits for **every** category, rather than the **first** category reaching a fixed quota.

## Limitations
The result assumes independent identically distributed categorical trials, finitely many strictly positive category probabilities, and equal quotas. No claim is made for category-specific unequal quotas, dependent trials, sampling without replacement, infinitely supported distributions, or larger/secondary orderings beyond the proved pairwise likelihood-ratio relation. The original-history assessment is conditional on the sources inspected: inaccessible full text of Anderson–Sobel–Uppuluri (1982) and any undiscovered stronger results remain historical-priority risks. No independent scientific audit or certification has been performed.

## References
1. M. Camarri and J. Pitman (1998), *Limit distributions and random trees derived from the birthday problem with unequal probabilities*, Berkeley Technical Report 523 (publicly dated 1 June 1998); *Electronic Journal of Probability* 5 (2000), Paper 2. https://statistics.berkeley.edu/tech-reports/523 ; https://doi.org/10.1214/EJP.v5-58
2. M. Camarri (1998), *Asymptotics for k-fold repeats in the birthday problem with unequal probabilities*, Berkeley Technical Report 524 (publicly dated 1 July 1998); *Random Structures & Algorithms* 15 (1999), 176–195. https://statistics.berkeley.edu/tech-reports/524
3. J. A. D. Aston and D. E. K. Martin (2005), *Waiting time distributions of competing patterns in higher-order Markovian sequences*, *Journal of Applied Probability* 42, 977–988. https://doi.org/10.1239/jap/1134587810
4. K. Anderson, M. Sobel and V. R. R. Uppuluri (1982), *Quota fulfillment times*, *Canadian Journal of Statistics* 10, 73–88. https://doi.org/10.2307/3314900
