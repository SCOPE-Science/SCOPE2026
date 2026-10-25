# The first covariance-sign reversals for fixed points and consecutive patterns

## Finding
Let \(\Pi\) be uniform on the symmetric group \(S_n\), and let \(F=\#\{i:\Pi(i)=i\}\). For a pattern \(\tau\in S_k\), let \(N_\tau\) be its number of *consecutive* occurrences: the number of windows \((\Pi(s),\ldots,\Pi(s+k-1))\), \(1\le s\le n-k+1\), whose relative rank order is \(\tau\).

For every \(n\ge k\ge2\), an exact boundary identity gives \(\operatorname{Cov}(F,N_\tau)\). For every \(n\ge4\) and \(\tau\in S_4\), the covariance is
\[
\boxed{\operatorname{Cov}(F,N_\tau)=\frac{P_\tau(n)}{6n(n-1)(n-2)}},
\]
where the **complete** list of \(24\) quadratic numerators \(P_\tau\) is given below.

Exactly three patterns of length four change from a strictly negative to a strictly positive covariance, or vice versa, as the permutation size increases:
\[
\begin{aligned}
P_{2143}(n)&=(n-5)(n+2),\\
P_{3142}(n)&=n^2-21n+62,\\
P_{4231}(n)&=-3(n-6)(n-3).
\end{aligned}
\]
Thus \(2143\) is negative at \(n=4\), zero at \(n=5\), and positive for \(n\ge6\); \(3142\) is negative for \(4\le n\le17\) and positive for \(n\ge18\); and \(4231\) is positive at \(n=4,5\), zero at \(n=6\), and negative for \(n\ge7\). The other twenty-one length-four patterns never exhibit both strict signs. No length-two or length-three pattern has a sign reversal for admissible sizes. Therefore **four is the smallest consecutive-pattern length allowing a fixed-point covariance-sign reversal**.

The three reversing patterns all have descent set \(\{1,3\}\), but their thresholds are different. This shows that descent-set information alone does not specify the fixed-point response of an individual consecutive-pattern count.

## Assumptions and scope
A permutation is uniform on *all* of \(S_n\), not restricted to derangements, avoidance classes, or involutions. A fixed point refers to equality between position and value. A consecutive occurrence is a rank pattern of \(k\) adjacent **positions**; occurrences may overlap. All assertions are finite-sample, including \(n=k\), and \(n\) ranges over integers.

The covariance measures the response to the natural one-parameter fixed-point tilt \(\mathbb P_h(\pi)\propto e^{hF(\pi)}\):
\[
\left.\frac{d}{dh}\mathbb E_h[N_\tau]\right|_{h=0}=\operatorname{Cov}(F,N_\tau).
\]
A sign reversal therefore means a change in the *first-order response* to rewarding fixed points, not a reversal of stochastic dominance.

Write \((a)_b=a(a-1)\cdots(a-b+1)\) for a falling factorial, and adopt \(\binom ab=0\) whenever \(b<0\), \(b>a\), or \(a<0\), with integer arguments. For \(1\le r,t\le k\) define the boundary contribution
\[
b_{r,t}(n)=
\sum_{j=1}^{r-1}\binom{j-1}{t-1}\binom{n-j}{k-t}
+\sum_{j=n-k+r+1}^{n}\binom{j-1}{t-1}\binom{n-j}{k-t},
\]
and \(B_{n,k}(\tau)=\sum_{r=1}^{k}b_{r,\tau_r}(n)\). Empty sums are zero.

## Proof
**1. Local conditioning.** Put \(I_j=\mathbf1_{\{\Pi(j)=j\}}\). For a consecutive window beginning at \(s\) let \(X_{s,\tau}\) indicate pattern \(\tau\). Then \(\mathbb P(I_j=1)=1/n\) and \(\mathbb E X_{s,\tau}=1/k!\). If \(j\notin\{s,\ldots,s+k-1\}\), conditioning on \(I_j=1\) leaves the window entries exchangeable, so \(\mathbb E[X_{s,\tau}\mid I_j=1]=1/k!\), and their covariance is zero.

If \(j=s+r-1\), the fixed value \(j\) must be the \(t=\tau_r\)-th smallest of the window. The other \(k-1\) values must include \(t-1\) values less than \(j\) and \(k-t\) values greater than \(j\). For each such unordered choice there is exactly one ordering matching \(\tau\). Consequently,
\[
\mathbb P(X_{s,\tau}=1\mid I_j=1)
=\frac{\binom{j-1}{t-1}\binom{n-j}{k-t}}{(n-1)_{k-1}}.
\]
Summing the covariances over every fixed-point index and every window gives the unabridged exact identity
\[
\operatorname{Cov}(F,N_\tau)=\frac1n\sum_{s=1}^{n-k+1}\sum_{r=1}^{k}
\left[\frac{\binom{s+r-2}{\tau_r-1}\binom{n-s-r+1}{k-\tau_r}}{(n-1)_{k-1}}-\frac1{k!}\right].
\tag{1}
\]

**2. Cancellation to the boundaries.** For every fixed rank \(t\), the elementary order-statistic Vandermonde identity is
\[
\sum_{j=1}^{n}\binom{j-1}{t-1}\binom{n-j}{k-t}=\binom nk.
\]
Here \(j\) is the value of the \(t\)-th smallest member of a selected \(k\)-subset. For each window coordinate \(r\), the admissible fixed point position ranges from \(j=r\) to \(j=n-k+r\); its omitted terms are exactly \(b_{r,\tau_r}(n)\). Since \(\binom nk/(n-1)_{k-1}=n/k!\), identity (1) simplifies to the universal **boundary identity**
\[
\boxed{
\operatorname{Cov}(F,N_\tau)
=\frac1n\left[\frac1{(k-2)!}-\frac{B_{n,k}(\tau)}{(n-1)_{k-1}}\right]},
\qquad n\ge k\ge2.
\tag{2}
\]
Nothing in this derivation assumes that windows are independent. Their overlaps are irrelevant to a covariance with \(F\) because expectation is linear.

**3. Complete length-four reduction.** When \(k=4\), every term in \(B_{n,4}(\tau)\) has an index within three units of an endpoint. The terms \(\binom{n-j}{4-\tau_r}\) in the left boundary and \(\binom{j-1}{\tau_r-1}\) in the right boundary are polynomials in \(n\) of degree at most three. Thus \(B_{n,4}(\tau)\) is a polynomial of degree at most three. Elementary expansion yields, for each of the twenty-four patterns,
\[
6B_{n,4}(\tau)=(n-3)\left[3(n-1)(n-2)-P_\tau(n)\right].
\tag{3}
\]
Here is the complete table, grouped solely for legibility:

| \(\tau\) | \(P_\tau(n)\) | \(\tau\) | \(P_\tau(n)\) |
|---|---|---|---|
| \(1234\) | \(3(n-2)(n-1)\) | \(1243\) | \(2(n^2-3n-1)\) |
| \(1324\) | \(3(n-3)(n-2)\) | \(1342\) | \(2(n-5)(n-4)\) |
| \(1423\) | \((n-4)(n+1)\) | \(1432\) | \(n^2-9n+26\) |
| \(2134\) | \(2(n^2-3n-1)\) | \(2143\) | \((n-5)(n+2)\) |
| \(2314\) | \((n-4)(n+1)\) | \(2341\) | \(-n^2+9n-26\) |
| \(2413\) | \(-n^2+9n-26\) | \(2431\) | \(-2(n-5)(n-4)\) |
| \(3124\) | \(2(n-5)(n-4)\) | \(3142\) | \(n^2-21n+62\) |
| \(3214\) | \(n^2-9n+26\) | \(3241\) | \(-(n-4)(n+1)\) |
| \(3412\) | \(-n^2-9n+46\) | \(3421\) | \(-2(n^2-3n-1)\) |
| \(4123\) | \(-n^2+9n-26\) | \(4132\) | \(-(n-4)(n+1)\) |
| \(4213\) | \(-2(n-5)(n-4)\) | \(4231\) | \(-3(n-6)(n-3)\) |
| \(4312\) | \(-2(n^2-3n-1)\) | \(4321\) | \(-3(n^2-7n+14)\) |

For a finite, exact symbolic certificate of the table, note that both sides of (3) have degree at most three. Evaluating the binomial boundary sums on the left and the printed polynomials on the right at four distinct points \(n=4,5,6,7\) therefore proves each of the twenty-four polynomial identities **for all real \(n\)** by the root bound for a nonzero cubic. The bundled checker performs all \(96\) exact integer tests. This finite calculation is a proof of polynomial identities because the degree bound is proved independently; the exhaustive permutation experiments below are only supplementary. Substitution into (2) proves the length-four covariance formula for all integers \(n\ge4\).

**4. Sign classification and minimality.** The denominator \(6n(n-1)(n-2)\) is positive for \(n\ge4\). Every row of the table except \(2143\), \(3142\), and \(4231\) has a fixed weak sign over that range. For the three exceptions the displayed factors, together with \(\frac{21+\sqrt{193}}2\in(17,18)\), give the exact integer thresholds stated in the Finding.

For \(k=2\), direct substitution into (2) gives \(\operatorname{Cov}(F,N_{12})=1/n\) and \(\operatorname{Cov}(F,N_{21})=-1/n\). For \(k=3\) it gives \(\operatorname{Cov}(F,N_{123})=1/n\), \(\operatorname{Cov}(F,N_{132})=\operatorname{Cov}(F,N_{213})=(n-3)/(2n(n-1))\), \(\operatorname{Cov}(F,N_{231})=\operatorname{Cov}(F,N_{312})=-1/(2n)\), and \(\operatorname{Cov}(F,N_{321})=-(n-3)/(n(n-1))\). None reverses sign for \(n\ge k\), establishing minimality.

## Verification
Run `python3 verify.py` with Python's standard library. It checks the \(96\) exact evaluations proving the length-four polynomial table; evaluates the universal boundary identity against every closed expression for \(2\le k\le4\) over \(k\le n\le80\); and independently exhausts all \(409112\) permutations with \(2\le n\le9\), comparing \(202\) joint moments against the derived formulas using exact rational arithmetic. It also tests the stated sharp sign thresholds. The program's expected terminus starts with `VERIFY_OK`; its actual run succeeded.

The unrestricted proof is the conditional counting argument plus degree-bounded polynomial identity, **not** an extrapolation from exhaustive enumeration through \(n=9\) or tests through \(n=80\).

## Relationship to prior work
Diaconis, Evans, and Graham [1] study random fixed-point sets and their equivalence with unseparated value successions in uniform permutations. That probabilistic theorem neither conditions on consecutive *rank patterns* nor computes their fixed-point mixed moments. Eriksen, Freij, and Wästlund [2] count derangements with prescribed descents; Désarménien and Wachs [4] refine descent-class enumeration by fixed-point count. Their descent specifications aggregate different rank patterns. For example, \(2143\), \(3142\), and \(4231\) all have descents at positions \(\{1,3\}\) but have different covariance profiles, so none of the three formulas follows merely by extracting a fixed-point/descent-class total.

Elizalde and Noy [3] develop generating functions and cluster enumeration for consecutive-pattern occurrence counts, including the length-four patterns \(1423\) and \(2143\). Their generating functions track occurrences but not the fixed-point count. The previously published exact fixed-point/descent covariance law [5] is the \(k=2\) boundary case; it does not imply the length-four quadratic numerators or their sign reversals. A previously published fourth consecutive-pattern frequency-polytope census [6] studies long-run feasible frequencies, not their finite random-permutation covariance with fixed points.

## Limitations
The result concerns only **first mixed moments**, not joint generating functions, stochastic domination, the law conditional on a specified number of fixed points, or higher-order fixed-point tilt responses. The closed sign census is for pattern lengths at most four; identity (2) applies to every \(k\), but it does not classify signs for all \(k\). The sign reversal is a first-order statement at the *uniform* permutation distribution. The earlier descent-class results may hide other equivalent formulations, and additional unpublished or differently indexed mixed-pattern formulas are a remaining historical priority risk. No independent audit is claimed.

## References
[1] P. Diaconis, S. N. Evans, R. Graham, “Unseparated pairs and fixed points in random permutations,” arXiv:1308.5459, first publicly posted 2013-08-25; *Advances in Applied Mathematics* 61 (2014), 102–124. Primary MSC 60C05. https://mathweb.ucsd.edu/~ronspubs/14_05_pairs.pdf

[2] N. Eriksen, R. Freij, J. Wästlund, “Enumeration of derangements with descents in prescribed positions,” arXiv:0811.1925v1, first publicly posted 2008-11-12; *Electronic Journal of Combinatorics* 16 (2009), R32. https://arxiv.org/abs/0811.1925

[3] S. Elizalde, M. Noy, “Clusters, generating functions and asymptotics for consecutive patterns in permutations,” arXiv:1210.6061v1, first publicly posted 2012-10-22; *Advances in Applied Mathematics* 49 (2012), 351–374. https://arxiv.org/abs/1210.6061

[4] J. Désarménien, M. L. Wachs, “Descent classes of permutations with a given number of fixed points,” *Journal of Combinatorial Theory, Series A* 64 (1993), 311–328. DOI:10.1016/0097-3165(93)90100-M. Full text examined, especially §5 Theorem 5.1 on fixed-point/descent-class enumeration and §6 Theorem 6.2 on fixed-point monotonicity within descent classes; neither refines to individual consecutive rank patterns.

[5] “Boundary localization of fixed-point–descent dependence in a uniform permutation,” 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-boundary-localization-of-fixed-point-descent-dependence-in-a-uni--6e228e1e9495 .

[6] “Complete local graph-degree spectrum of the fourth consecutive-pattern polytope,” 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-local-graph-degree-spectrum-of-the-fourth-consecutive-p--5a78dd8e7c56 .
