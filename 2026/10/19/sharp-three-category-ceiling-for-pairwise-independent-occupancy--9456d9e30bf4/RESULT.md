# Sharp three-category ceiling for pairwise-independent occupancy parities

## Finding

Suppose \(n\ge1\) independent trials each fall into one of \(m\ge2\) distinguished categories with probabilities \(p_1,\ldots,p_m>0\) and \(\sum_i p_i\le1\). There is one possible untracked residual category of probability \(p_0=1-\sum_i p_i\ge0\). Let \(N_i\) be the number of trials assigned to category \(i\) and \(B_i=\mathbf1_{\{N_i\text{ is odd}\}}\).

For distinct \(i,j\), the exact parity covariance is
\[
\boxed{\operatorname{Cov}(B_i,B_j)=\frac{(1-2p_i-2p_j)^n-[(1-2p_i)(1-2p_j)]^n}{4}.}
\tag{1}
\]
For **odd** \(n\), every such covariance is strictly negative. For **even** \(n\), its sign is exactly the sign of
\[
\boxed{p_i+p_j-p_ip_j-\tfrac12.}
\tag{2}
\]
Because the variables are Bernoulli, \(B_i\) and \(B_j\) are independent precisely when their covariance vanishes. Thus for even \(n\), pairwise independence occurs precisely when
\[
\boxed{(1-p_i)(1-p_j)=\tfrac12.}
\tag{3}
\]

If **three or more** indicators are pairwise independent, necessarily \(n\) is even, exactly three categories are distinguished, and their probabilities are uniquely
\[
\boxed{p_1=p_2=p_3=1-1/\sqrt2,\qquad p_0=3/\sqrt2-2>0.}
\tag{4}
\]
Conversely, (4) produces pairwise independent \(B_1,B_2,B_3\) for **every** positive even \(n\); they are **never jointly independent**.

There is also a sharp dimension obstruction to nonnegative dependence: if \(m\ge4\), at least one pair has strictly negative covariance for **every** \(n\), regardless of the positive probabilities. This bound is sharp, since for \(m=3\) and even \(n\), the uniform probabilities \(p_1=p_2=p_3=1/3\) produce three strictly positive pairwise covariances.

## Assumptions and scope

The number \(n\) of trials is an arbitrary positive integer, all distinguished probabilities are positive, and their sum is at most one; no positivity is required of \(p_0\). All trials have the same category probabilities and are independent. The \(B_i\) indicate parity of **counts**, not whether a category has ever appeared. The pairwise independence statement includes any number of distinguished categories, while its explicit three-category conclusion is conditional on \(m\ge3\). No independence of the underlying occupancy counts is asserted.

## Proof

For any subset \(S\subseteq\{1,\ldots,m\}\), one trial flips the parity of \(\sum_{i\in S}N_i\) with probability \(\sum_{i\in S}p_i\). Independence of trials gives the character identity
\[
\mathbb E\left[(-1)^{\sum_{i\in S}N_i}\right]
=\left(1-2\sum_{i\in S}p_i\right)^n.
\tag{5}
\]
Set \(Z_i=(-1)^{N_i}=1-2B_i\). Since \(\operatorname{Cov}(B_i,B_j)=\operatorname{Cov}(Z_i,Z_j)/4\), equation (5) for \(S=\{i\},\{j\},\{i,j\}\) yields (1).

Put \(a=1-2(p_i+p_j)\) and \(b=(1-2p_i)(1-2p_j)=a+4p_ip_j\). Because \(p_ip_j>0\), we have \(a<b\), so for odd \(n\), \(a^n<b^n\), proving strict negative covariance. For even \(n\), the sign of \(a^n-b^n\) equals that of \(a^2-b^2\), because \(u\mapsto u^{n/2}\) is strictly increasing on nonnegative numbers. Direct factorization yields
\[
a^2-b^2=16p_ip_j\left(p_i+p_j-p_ip_j-\tfrac12\right).
\tag{6}
\]
This establishes the even-case sign law. Two Bernoulli random variables are independent if and only if they are uncorrelated: their joint table is determined by the two marginal probabilities and the probability of the joint \((1,1)\) event. Therefore (3) follows.

Suppose \(m\ge3\) and every pair is independent. All pairs satisfy (3), hence for any three distinct indices \(i,j,k\),
\[
(1-p_i)(1-p_j)=(1-p_i)(1-p_k)=\tfrac12.
\]
Since \(1-p_i>0\), this forces \(p_j=p_k\); varying the indices forces all \(p_i\) equal to a common \(p\). The only admissible root of \((1-p)^2=1/2\) is \(p=1-1/\sqrt2\). But \(4p>1\), whereas \(3p<1\). Consequently at most three categories fit the probability simplex, and the three-category solution has exactly the residual probability displayed in (4). This also establishes existence of pairwise independence for any even \(n\).

The triple is not independent. At (4), write \(s=1-2p=\sqrt2-1>0\). From (5),
\[
\mathbb E[Z_1Z_2Z_3]=(1-6p)^n=(3\sqrt2-5)^n,
\quad
\prod_{i=1}^3\mathbb E[Z_i]=s^{3n}.
\]
For positive even \(n\), the first expression is \((5-3\sqrt2)^n\) and the second is \((5\sqrt2-7)^n\). Their positive bases are distinct, since
\[
5-3\sqrt2>5\sqrt2-7>0
\quad\Longleftrightarrow\quad 3>2\sqrt2.
\]
Therefore the product moment cannot factor, ruling out joint independence.

For the nonnegative-covariance dimension ceiling, order the weights as \(p_1\le p_2\le\cdots\le p_m\). For \(m\ge4\), the sum of the two smallest weights satisfies \(p_1+p_2\le2\sum_i p_i/m\le2/m\le1/2\). Since \(p_1p_2>0\), we have \(p_1+p_2-p_1p_2<1/2\); equation (2) gives a strictly negative pair covariance for every even \(n\), while every odd \(n\) is already resolved. For sharpness choose \(m=3\), \(p_i=1/3\) and even \(n\). Then \(p_i+p_j-p_ip_j=5/9>1/2\), making all three pair covariances positive.

For completeness, when \(m=2\), the nondegenerate independence locus for even \(n\) is exactly
\[
0<p_1<\tfrac12,\qquad p_2=\frac{1/2-p_1}{1-p_1},
\]
with the remaining probability positive. This follows by solving (3) under \(p_1,p_2>0\). Thus (3) is a complete classification also at the two-category boundary.

## Verification

The accompanying standalone Python verifier independently enumerates all sequences of draws, with exact rational weights, for two-, three-, and four-category examples over sample sizes one through six. It checks (1) against direct joint Bernoulli moments and checks every predicted sign. Separately it carries out symbolic algebra with the irrational parameter in (4) for positive even sizes through 200, checking pairwise zero covariances and a nonzero third-order product defect. It includes exact sign and independence-boundary examples. Finite tests complement rather than replace the unrestricted character proof (5)--(6).

## Relationship to prior work

Joag-Dev and Proschan established negative association of multinomial count vectors; Dubhashi and Ranjan developed negative association and regression for independent balls-and-bins allocations, including their empty-bin indicator theorem. These results constrain covariance of **monotone** transforms and do not impose negative association on the nonmonotone count-parity map. Bartroff and Goldstein study normal approximation for fixed-occupancy counts in the classical urn model, a different collection of indicators. A published occupancy-indicator precision result similarly concerns the events of being occupied at least once, rather than being occupied an odd number of times.

The formulas here concern a precise parity-character dependence regime, including the sharp three-category independence ceiling and its pairwise-but-not-mutual witness. Standard multinomial probability-generating-function identities supply the character-moment starting point, but a general transform formula alone does not state the feasibility and triple-dependence classification. Targeted comparisons found no explicit equivalent classification. The literature and source-access limits are described in the companion review.

## Limitations

This theorem assumes iid categorical draws with one fixed distribution. It makes no claim about stopping times, dependent trials, arbitrary moduli other than two, or nonidentical per-trial categorical vectors. Pairwise independence is not mutual independence; indeed the unique three-category pairwise-independent configuration is explicitly non-independent jointly. An implicit version of these elementary Fourier-character deductions could appear in earlier probability literature; priority has not been independently established.

## References

- K. Joag-Dev and F. Proschan, “Negative Association of Random Variables with Applications,” *Annals of Statistics* **11** (1983), 286–295. DOI: 10.1214/aos/1176346079.
- D. Dubhashi and D. Ranjan, “Balls and Bins: A Study in Negative Dependence,” *BRICS Report Series* **3** (1996), no. 25. DOI: 10.7146/brics.v3i25.20006; openly accessible full report at https://www.brics.dk/RS/96/25/BRICS-RS-96-25.pdf.
- J. Bartroff and L. Goldstein, “A Berry-Esseen bound for the uniform multinomial occupancy model,” arXiv:1202.0909, first public 2012-02-04.
