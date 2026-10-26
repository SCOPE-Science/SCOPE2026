# Parity-alternating endpoint vacancies in finite Page–Rényi parking

## Finding
For every integer \(n\ge3\), the two endpoint-vacancy indicators in the uniform random-order greedy dimer parking process on the path of \(n\) sites have covariance whose sign is exactly \((-1)^n\). At \(n=2\) their covariance is zero. Moreover,
\[
\operatorname{Cov}(L_n,R_n)\sim (-1)^n\frac{2^{n-2}}{(n-1)!}\qquad(n\to\infty).
\]
Thus a positive association at even sizes and a negative association at odd sizes alternate for every admissible length, but decay at a factorial rate.

## Assumptions and scope
Let the sites be \(1,\ldots,n\) with \(n\ge2\). Give each adjacent bond \((i,i+1)\), \(1\le i<n\), an independent continuous priority, equivalently process all bonds in a uniformly random order. When processing a bond, occupy both sites if both are unoccupied, otherwise do nothing. After all bonds, let \(L_n\) and \(R_n\) indicate vacancies at sites \(1\) and \(n\), respectively. For recursion purposes, the empty path has vacancy probability \(a_0=0\), and the single-site path has \(a_1=1\). Define \(a_n=\Pr(L_n=1)=\Pr(R_n=1)\) and \(b_n=\Pr(L_n=R_n=1)\). We use covariance of Bernoulli indicators, not conditional covariance.

## Proof
**First-split recurrence.** The earliest-priority bond is uniform among the \(n-1\) bonds. If this bond is \((i,i+1)\), it parks and leaves independent greedy parking processes on the left subpath with \(i-1\) sites and the right subpath with \(n-i-1\) sites. Thus, for all \(n\ge2\),
\[
 a_n=\frac1{n-1}\sum_{j=0}^{n-2}a_j,\qquad
 b_n=\frac1{n-1}\sum_{j=0}^{n-2}a_j a_{n-2-j}.
\]
The second identity also holds when one subpath is empty because \(a_0=0\). These identities are exact, with \(b_2=b_3=0\).

**One-point solution.** Subtracting successive equations gives \(a_n-a_{n-1}=(-1)^{n-1}/(n-1)!\), as checked inductively from \(a_1=1\). Hence
\[
 a_n=\sum_{r=0}^{n-1}\frac{(-1)^r}{r!},\quad
 A(z)=\sum_{n\ge0}a_nz^n=\frac{ze^{-z}}{1-z}.
\]
Taylor's integral remainder yields
\[
 a_n=e^{-1}-(-1)^n R_n,\qquad
 R_n=\frac1{(n-1)!}\int_0^1(1-u)^{n-1}e^{-u}\,du>0.
\]
In particular \(0<R_n\le 1/n!\).

**Joint solution.** The convolution recurrence gives, for \(n\ge4\),
\[
 b_n=\frac1{n-1}[z^{n-2}]A(z)^2
 =\frac1{n-1}[z^{n-4}]\frac{e^{-2z}}{(1-z)^2}
 =\frac1{n-1}\sum_{r=0}^{n-4}\frac{(n-3-r)(-2)^r}{r!}.
\]
Writing \(q=n-4\) and \(P_q(t)=\sum_{r=0}^{q}t^r/r!\), this also reads
\[
 b_n=P_q(-2)+\frac{(-2)^{q+1}}{(q+3)q!}.
\]
Apply Taylor's integral remainder to \(e^{-2}\), then substitute \(1/(q+3)=\int_0^1(1-u)^{q+2}\,du\), to obtain
\[
 b_n=e^{-2}+(-1)^n B_n,\qquad
 B_n=\frac{2^{n-3}}{(n-4)!}\int_0^1(1-u)^{n-4}
 \bigl(e^{-2u}-(1-u)^2\bigr)\,du.
\]
For \(0<u\le1\), \(e^{-u}>1-u\), so \(B_n>0\).

**All signs and the sharp asymptotic.** For even \(n\ge4\), \(a_n<e^{-1}\) and \(b_n>e^{-2}\), hence \(b_n-a_n^2>0\). For odd \(n\ge5\), \(a_n>e^{-1}\) and \(b_n<e^{-2}\), hence \(b_n-a_n^2<0\). Directly \(b_3=0\) and \(a_3=1/2\), giving covariance \(-1/4\); \(n=2\) gives zero. Finally \(e^{-2u}-(1-u)^2=u^2+O(u^3)\) near zero. Integrating against \((1-u)^{n-4}\) and using beta integrals gives
\[
 B_n=\frac{2^{n-3}}{(n-4)!}\left(\frac{2(n-4)!}{(n-1)!}(1+O(n^{-1}))\right)
 =\frac{2^{n-2}}{(n-1)!}(1+O(n^{-1})).
\]
Since \(R_n=O(1/n!)\), the correction \(a_n^2-e^{-2}=O(1/n!)\) is negligible relative to \(B_n\), proving the stated asymptotic. \(\square\)

## Verification
The supplied self-contained `verify.py` recomputes the first-split recursion using exact rational arithmetic through \(n=79\), checks the alternating covariance sign and closed marginal formulas, and independently enumerates all \((n-1)!\) bond-processing permutations for \(2\le n\le9\). The leading small-size covariance values are \(-1/4,\ 2/9,\ -9/64,\ 59/900\) for \(n=3,4,5,6\) respectively. All infinite claims are proved analytically; finite enumeration is only a cross-check.

## Relationship to prior work
The discrete Page–Rényi parking model, random-priority construction and first-split method are classical. Gerin's full-text treatment gives the matching model, endpoint probability recursion in the history of the problem, bulk density, and infinite-line local statistics, but does not state this full finite-endpoint two-point covariance sign law or its sharp factorial amplitude. Prior random sequential adsorption work includes more general multisite correlations; the finite-boundary consequence may be implicit in broader formulas, so independent historical-priority verification remains warranted. No novelty is claimed for the elementary first-split recurrence by itself.

## Limitations
This is a finite path with open boundary conditions and uniformly randomized bond priorities; it does not assert the same result on cycles, heterogeneous priority laws, or longer cars. A published general multisite-correlation formula could potentially subsume the result without mentioning finite endpoints. Independent validation has not been performed.

## References
1. L. Gerin, *The Page–Rényi parking process*, arXiv:1411.8002 (first public version November 28, 2014); *Electronic Journal of Combinatorics* 22 (2015), P4.4, doi:10.37236/5150.
2. E. S. Page, *The distribution of vacancies on a line*, *Journal of the Royal Statistical Society, Series B* 21 (1959), 364–374, as cited in Gerin.
3. L. A. Fan and J. K. Percus, *Asymptotic coverage in random sequential adsorption on a lattice*, *Physical Review A* 44 (1991), 5099–5103; broader multisite-correlation historical-priority risk.
