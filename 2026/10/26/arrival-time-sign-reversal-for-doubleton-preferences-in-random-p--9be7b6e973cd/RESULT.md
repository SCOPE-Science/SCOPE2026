# Arrival-time sign reversal for doubleton preferences in random parking functions

## Finding

For a uniform classical parking function on \(n\ge2\) spaces, let \(L_i\) be the indicator that arrival \(i\) receives its preferred spot. For \(1\le r\le n\), let \(U_r\) count distinct preferred spot labels occurring exactly \(r\) times among the \(n\) preferences. Write \(N=n+1\) and
\[
b_m(s)=\begin{cases}\binom ms N^{-s}(1-N^{-1})^{m-s},&0\le s\le m,\\0,&\text{otherwise}.\end{cases}
\]
Then, for all \(1\le i,r\le n\),
\[
\operatorname{Cov}(L_i,U_r)=\frac{N-i+1}{N}\big[b_{n-i}(r-1)-b_{n-i}(r)-b_{n-1}(r-1)+b_{n-1}(r)\big].\tag{1}
\]
In particular, the first car has zero covariance with all preference multiplicity counts. For \(2\le i\le n\), the covariance is strictly positive when \(r=1\), and strictly negative for every \(3\le r\le n\).

For \(r=2\), if \(2\le n\le4\), the covariance is strictly negative for all \(i\ge2\). If \(n\ge5\), its nonzero signs in arrival order \(i=2,3,\ldots,n\) switch exactly once from positive to negative. At most one arrival can have exactly zero covariance. Thus doubleton preferences are the only frequency class exhibiting an arrival-time covariance transition.

The distinct-preference count \(K=\sum_{r\ge1}U_r\) also has an exact strictly positive covariance for \(i\ge2\):
\[
\operatorname{Cov}(L_i,K)=\frac{N-i+1}{N}\left[(1-N^{-1})^{n-i}-(1-N^{-1})^{n-1}\right].\tag{2}
\]

For \(i/n\to\alpha\in(0,1)\), define \(g(t)=e^{-t}(t-t^2/2)\). Then
\[
\operatorname{Cov}(L_i,U_2)\longrightarrow (1-\alpha)[g(1-\alpha)-g(1)].\tag{3}
\]
There is one critical fraction \(\alpha_*=1-\lambda_*\approx0.714556384743\), with \(\lambda_*\in(0,2-\sqrt2)\) the unique solution of \(g(\lambda_*)=g(1)\). The limiting covariance is positive for \(0<\alpha<\alpha_*\) and negative for \(\alpha_*<\alpha<1\).

## Assumptions and scope

A preference list \(a_1,\dots,a_n\in\{1,\dots,n\}\) is a classical parking function if cars arrive in order, each occupying the first still-free spot at or after its preference, and all successfully park. The distribution is uniform on the \((n+1)^{n-1}\) such lists. In \(U_r\), preference multiplicity is counted **before** displacement: it is not the multiplicity of realized parking positions, which is always one. All claims hold for the indicated finite integer ranges, with exact zero convention for out-of-range binomial probabilities. They concern covariance, not stochastic dominance or causal effects.

## Proof

**Circular reduction.** Place the \(N=n+1\) spots on a circle and choose the \(n\) preferences independently and uniformly from the circular sites. The parking algorithm always fills \(n\) sites and leaves one vacant. Shifting all preferences modulo \(N\) also shifts the final hole, while preserving every \(L_i\) and every multiplicity count \(U_r\). Each shift orbit contains exactly one list with final hole at site \(N\), and that representative is an ordinary linear parking function. Therefore the complete joint distribution of \((L_i,U_1,\dots,U_n)\) under the uniform linear model equals that under the independent circular preference model. This uses the classical circular argument, but transfers the **joint** marked observable rather than only its marginals.

**Exact cross-covariance.** Fix arrival \(i\) and condition on all earlier preferences and circular parking choices, denoted \(\mathcal H_{i-1}\). Precisely \(i-1\) sites are occupied, and each site previously preferred by any car is occupied (the car either parked there or found it already occupied). Thus all \(N-i+1\) free sites have received zero earlier preferences. Since \(a_i\) is uniform and independent of the past,
\[
p_i:=\Pr(L_i=1\mid\mathcal H_{i-1})=\frac{N-i+1}{N}.\tag{4}
\]
Let \(c_v\) be the number of earlier preferences equal to site \(v\). Later preferences are independent uniforms; for any site \(v\), their count \(Y_v\) has the marginal \(\mathrm{Bin}(n-i,1/N)\). Temporarily delete draw \(i\), leaving earlier and later preferences. Inserting draw \(i\) at site \(v\) changes the final frequency-\(r\) count, in conditional expectation, by
\[
\Delta_r(c_v)=\Pr(c_v+1+Y_v=r)-\Pr(c_v+Y_v=r).
\]
Conditioning on \(L_i=1\), site \(v\) must be free and hence \(c_v=0\). Therefore the conditional covariance between \(L_i\) and \(U_r\), given \(\mathcal H_{i-1}\), equals
\[
p_i\left[\Delta_r(0)-\frac1N\sum_{v=1}^{N}\Delta_r(c_v)\right].\tag{5}
\]
The conditional mean of \(L_i\) is the constant \(p_i\), so taking expectations in (5) produces the unconditional covariance without an additional between-history term. The first term equals \(b_{n-i}(r-1)-b_{n-i}(r)\). For any fixed site, the earlier count \(c_v\sim\mathrm{Bin}(i-1,1/N)\); adding its independent later count gives \(\mathrm{Bin}(n-1,1/N)\). Hence the expected site average in (5) equals \(b_{n-1}(r-1)-b_{n-1}(r)\), proving (1). Replacing frequency-\(r\) counts by the distinct-site count gives (2), since inserting at a new site changes distinctness exactly when the later count there is zero.

**Single and high multiplicities.** Put \(h_m(r)=b_m(r-1)-b_m(r)\). From the Bernoulli convolution recurrence,
\[
h_{m+1}(r)-h_m(r)=\frac1N\big[b_m(r-2)-2b_m(r-1)+b_m(r)\big].\tag{6}
\]
For \(r=1\) and \(0\le m\le n-2\), this difference is strictly negative, because \(b_m(1)/b_m(0)=m/(N-1)<1\). Equation (1), comparing \(h_{n-i}(1)\) and \(h_{n-1}(1)\), is therefore strictly positive for \(i\ge2\). For \(r\ge3\), the right side of (6) is nonnegative for every \(0\le m\le n-2\), and is strictly positive once \(m\ge r-2\): indeed, for \(m\ge r-1\),
\[
\frac{b_m(r-2)}{b_m(r-1)}=\frac{(r-1)(N-1)}{m-r+2}>2,
\]
while for \(m=r-2\) the first term in (6) is positive and the other two vanish. Since \(r\le n\), the interval from \(n-i\) to \(n-1\) contains at least one strict increment. Thus (1) is strictly negative for every \(i\ge2\) and \(3\le r\le n\).

**Doubleton transition.** For \(r=2\), the sign of the first difference in (6) equals the sign of
\[
H_n(m)=1-\frac{2m}{n}+\frac{m(m-1)}{2n^2},\qquad 0\le m\le n-2,\tag{7}
\]
because \(N-1=n\) and \(b_m(0)>0\). This quadratic is strictly decreasing over the indicated interval, so \(m\mapsto h_m(2)\) is unimodal: it increases and then decreases, with at most one flat step. Its initial value is \(h_0(2)=0\) and \(h_{n-1}(2)>0\). Moreover
\[
2n^2H_n(n-2)=-n^2+3n+6,\tag{8}
\]
which is positive for \(n\le4\) and negative for \(n\ge5\). Consequently, for \(n\le4\), \(h_m(2)<h_{n-1}(2)\) for all \(m<n-1\), giving negative covariance. For \(n\ge5\), \(h_{n-2}(2)>h_{n-1}(2)>h_0(2)\). By unimodality, as \(m=n-i\) decreases from \(n-2\) to zero, the sign of \(h_m(2)-h_{n-1}(2)\) changes from positive to negative exactly once, with at most one equality, as claimed.

**Asymptotic location.** For any integers \(m=m_n\) with \(m/n\to t\in[0,1]\), elementary binomial-to-Poisson convergence gives \(h_m(2)\to g(t)\). The prefactor in (1) tends to \(1-\alpha\), giving (3). Since \(g'(t)=e^{-t}(1-2t+t^2/2)\), \(g\) is strictly increasing on \((0,2-\sqrt2)\) and strictly decreasing on \((2-\sqrt2,1)\). The value \(g(1)=e^{-1}/2\) lies strictly between \(g(0)=0\) and the unique maximum, yielding exactly one additional root \(\lambda_*\in(0,2-\sqrt2)\) and the stated signs. Numerical bisection gives \(\alpha_*\approx0.714556384743\).

## Verification

The standalone file `verify.py` exhaustively enumerates all classical parking functions for \(2\le n\le7\), independently computes each exact rational \(\operatorname{Cov}(L_i,U_r)\), and checks (1) across all valid \(i,r\). It also checks the sign classification and the distinct-preference covariance (2) for \(2\le n\le200\), and the doubleton transition profile for all those values. Run `python3 verify.py` from the directory containing the script. Finite enumeration corroborates, but does not replace, the all-\(n\) proof above.

## Relationship to prior work

The circular parking-function construction and the marginal distribution of the lucky count are classical. Diaconis and Hicks explicitly identify preference *species* (multiplicity counts) with the iid occupancy model through rotation and summarize the corresponding marginal laws; Kenyon and Yin give the fixed-root forest connection, the lucky-car product generating function, and coordinate covariances. Harris and Martinez enumerate prescribed lucky subsets, while Butler et al. develop the lucky-car and lucky-spot perspectives. None of the inspected relevant treatments states the cross-covariance (1), the all-frequency sign trichotomy, or the sharp doubleton arrival threshold; separate lucky-set and species marginals do not imply the mixed statistic. The argument here combines established ingredients with a new joint insertion calculation. Exhaustive claims of historical priority are not made: an equivalent marked-enumeration formula in classical hashing/linear-probing literature remains possible.

## Limitations

The theorem treats **uniform classical** parking functions and a single lucky indicator versus a global preference-frequency count. It does not establish stochastic ordering, higher joint moments, a multivariate central limit theorem, or extend directly to nonuniform preferences or other parking protocols. The asymptotic sign rule assumes a fixed interior arrival fraction. The finite numerical implementation checks only bounded sizes; the proof of all-size validity is analytic. Earlier equivalent mixed-moment results in linear probing or parking-function enumerators remain a historical-priority risk.

## References

1. P. Diaconis and A. Hicks, *Probabilizing Parking Functions*, arXiv:1611.09821, first public 2016-11-29, especially Sections 3–4 (lucky count and preference species).
2. R. Kenyon and M. Yin, *Parking functions: From combinatorics to probability*, arXiv:2103.17180, first public 2021-03-31, especially Sections 2.1, 2.4 and 3.
3. P. E. Harris and L. Martinez, *Parking functions with a fixed set of lucky cars*, arXiv:2410.08057, first public 2024-10-10, especially Section 2.
4. S. Butler, K. Hadaway, V. Lenius, P. Martens and M. Moats, *Lucky cars and lucky spots in parking functions*, arXiv:2412.07873, first public 2024-12-10, especially Sections 2–3.
5. J. Riordan, *Ballots and trees* (1969), for Pollak's classical circular parking argument (historical attribution through references above).
