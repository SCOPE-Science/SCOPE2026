# Universal persistence law for long wet-spell occurrence

## Finding

For each integer \(k\ge3\), consider a stationary binary daily wet/dry Markov chain with wet probability \(1/2\), with common probability \(q\in(0,1)\) of repeating the previous day's wet/dry state. Let \(S_{n,k}(q)\) be the probability that the first \(n\) days contain **no** stretch of \(k\) consecutive wet days, and define its asymptotic survival factor

\[
\lambda_k(q)=\lim_{n\to\infty} S_{n,k}(q)^{1/n}.
\]

There is **exactly one** persistence parameter \(q_k\in(0,1)\) maximizing the long-window exponential occurrence rate \(-\log\lambda_k(q)\). It is specified without optimizing a matrix numerically as follows. Put \(m=k-1\), and let \(r_m\in(0,1)\) be the unique solution of

\[
\frac{2r_m\sum_{j=0}^{m-1}r_m^j}{1+\sqrt{1-r_m^m}}=m.
\]

Then

\[
q_k=\frac{r_m}{r_m+(1-r_m)/\sqrt{1-r_m^m}},\qquad
\lambda_k(q_k)=\frac{1}{r_m+(1-r_m)/\sqrt{1-r_m^m}}.
\]

Furthermore, let \(c\in(0,2)\) be the unique positive solution of

\[
c=\frac{2(1-e^{-c})}{1+\sqrt{1-e^{-c}}}.
\]

The optimal persistence and avoidance eigenvalue obey the **universal large-spell laws**

\[
\lim_{k\to\infty}(k-1)(1-q_k)
=\frac{c}{\sqrt{1-e^{-c}}}\approx0.75430126082451,
\]

\[
\lim_{k\to\infty}(k-1)\bigl(1-\lambda_k(q_k)\bigr)
=c\left(\frac{1}{\sqrt{1-e^{-c}}}-1\right)\approx0.29755327337930.
\]

Consequently the optimal exponential occurrence rate is asymptotic to \(0.29755327337930/(k-1)\), with the long-window limit taken first at each fixed spell length. For \(k=3\), \(q_3\approx0.73953495433966\). The already-known \(k=2\) calibration yields \(q_2=3/5\); no originality is claimed for that special case.

## Assumptions and scope

The process is a time-homogeneous, first-order binary Markov chain in stationary equilibrium. Days are identically classified as wet or dry; the transition probabilities are \(\Pr(1\to1)=\Pr(0\to0)=q\), with complements \(1-q\), ensuring wet marginal \(1/2\). The result concerns the probability of **at least one** specified-length wet run in a long observation window, not the expected number of runs, the probability of a run in a specified finite window, total precipitation or flooding. Each fixed \(k\ge3\) is optimized over \(0<q<1\); limits in \(k\) are taken only after obtaining the long-window exponential decay for each fixed \(k\). The endpoints \(q=0,1\) are not admissible irreducible aperiodic chains and do not attain the interior optimum.

## Proof

**1. Killed-chain Perron factor.** Index the transient states by the current wet-run length \(j\in\{0,1,\ldots,k-1\}\), with state \(0\) meaning the most recent day was dry. From state \(0\) the next day gives state \(0\) with probability \(q\) or state \(1\) with probability \(1-q\). From a state \(j\ge1\), a dry day leads to state \(0\) with probability \(1-q\), while a wet day leads to state \(j+1\) with probability \(q\), except that from \(j=k-1\) this wet transition kills the path. The resulting matrix \(Q_k(q)\) is primitive for \(0<q<1\) and is strictly substochastic in at least one row. The stationary initial streak vector after day one is \(\alpha=(1/2,1/2,0,\ldots,0)\). Therefore

\[
S_{n,k}(q)=\alpha Q_k(q)^{n-1}{\bf 1},\qquad
\lambda_k(q)=\rho(Q_k(q))\in(0,1),
\]

by Perron–Frobenius theory. The right Perron eigenvector \(v\) has strictly positive components, with \(\lambda v_0=qv_0+(1-q)v_1\) and \(\lambda v_j=(1-q)v_0+qv_{j+1}\) for \(1\le j<k-1\), ending with \(\lambda v_{k-1}=(1-q)v_0\). Unwinding from the last state yields

\[
\lambda^{k-1}(\lambda-q)
=(1-q)^2\sum_{j=0}^{k-2}q^j\lambda^{k-2-j}.
\]

In particular \(\lambda>q\), allowing the change of variables below.

**2. Exact parametrization.** Put \(m=k-1\), \(r=q/\lambda\in(0,1)\), \(t=(1-q)/\lambda>0\) and \(A_m(r)=\sum_{j=0}^{m-1}r^j\). Dividing the preceding equation by \(\lambda^{m+1}\) gives \(1-r=t^2A_m(r)\). Hence

\[
t=\sqrt{\frac{1-r}{A_m(r)}}=\frac{1-r}{\sqrt{1-r^m}},\quad
h_m(r)=r+t=\frac1\lambda,\quad
q=\frac{r}{h_m(r)}.
\]

The function \(t(r)\) is strictly decreasing since its squared numerator \(1-r\) strictly decreases while \(A_m(r)\) strictly increases. Thus \(r/(r+t(r))\) increases strictly and continuously from \(0\) to \(1\), and this substitution parametrizes every admissible \(q\). Conversely, the positive eigenvector recurrences above construct a positive eigenvector for the resulting \(\lambda=1/h_m(r)\), so the parametrized eigenvalue is necessarily Perron's eigenvalue. Maximizing the exponential rate is equivalent to maximizing \(h_m(r)\).

**3. Unique optimum for every spell length.** With \(z=\sqrt{1-r^m}\), direct differentiation gives

\[
h_m'(r)=\frac{(1-r)r^{m-1}}{2(1-r^m)^{3/2}}
\left[m-\frac{2rA_m(r)}{1+\sqrt{1-r^m}}\right].
\]

The prefactor is positive. The function \(G_m(r)=2rA_m(r)/(1+\sqrt{1-r^m})\) is strictly increasing: its numerator increases, its positive denominator decreases, and its endpoint limits are \(0\) and \(2m\). Therefore \(G_m(r)=m\) has exactly one solution \(r_m\in(0,1)\), at which \(h_m\) changes from increasing to decreasing. Since \(h_m(0)=\lim_{r\uparrow1}h_m(r)=1\), this is the unique global maximum. The stated formulas follow.

**4. The large-length scaling.** The optimality condition implies

\[
m(1-r_m)\le2r_m\le2,
\]

because \(A_m(r)\le1/(1-r)\) and the denominator of \(G_m\) is at least \(1\). Thus \(r_m\to1\), and \(c_m=-m\log r_m\) is bounded. If a subsequence had \(c_m\to0\), then the optimality equation divided by \(m\) would yield \(1=2\), a contradiction. Any positive subsequential limit \(c\) therefore satisfies

\[
1=\frac{2(1-e^{-c})}{c(1+\sqrt{1-e^{-c}})}.
\]

The right-hand side is strictly decreasing from \(2\) to \(0\) on \((0,\infty)\): \((1-e^{-c})/c\) decreases strictly, as does \(1/(1+\sqrt{1-e^{-c}})\). Hence there is a unique \(c>0\), and the full sequence \(c_m\to c\). Moreover \(c<2\) from the finite bound, so the specified root lies in \((0,2)\). Finally

\[
m(1-r_m)\to c,\quad 1-r_m^m\to1-e^{-c},\quad
h_m(r_m)=1+(1-r_m)\left(\frac1{\sqrt{1-r_m^m}}-1\right).
\]

Applying \(q_k=r_m/h_m(r_m)\) and \(\lambda_k=1/h_m(r_m)\) yields the two displayed asymptotic constants. Because \(-\log\lambda\sim1-\lambda\) as \(\lambda\uparrow1\), the exponential-rate asymptotic follows. This completes the proof.

## Verification

The standalone `check.py` uses only Python's standard library and can be run with `python3 check.py`. It verifies exact rational weather-path enumerations against a killed-chain recurrence, compares characteristic identities at rational parameters by exact fraction-preserving Gaussian elimination, checks the spectral optimizer against independent Perron power iterations for several spell lengths, and checks large-length numerical scaling. Its current replay reports `VERIFY_OK assertions= 387`. These finite tests are regression checks; the preceding proof supplies the quantifiers over every \(k\ge3\) and every \(q\in(0,1)\).

## Relationship to prior work

Caskey (1963) and Weiss (1964) motivate Markov wet/dry occurrence and spell modeling. Fu, Wang and Lou (2003), especially Sections 2 and 4–6, already establish general finite-state embedding and Perron-rate treatments of two-state longest runs. Those ingredients are acknowledged, not claimed as new. In the inspected full text, transition parameters are inputs rather than decision variables; the paper does not state the unique optimal equal-marginal persistence law or the large-spell universal constant. Sen, Mohan and Agarwal (2013) likewise develop Markov waiting-time pattern generating functions rather than this parameter optimization. A previously established two-wet-day result covers \(k=2\), not the simultaneous all-\(k\ge3\) optimization and high-\(k\) scaling proved here. Koutras (1997), Lou (1996), and Samarova (1982) address related runs, waiting times or longest-run asymptotics; comparison is qualified by incomplete access where indicated below.

## Limitations

This result describes a stylized symmetric, stationary, first-order model, not nonstationary rainfall, the depth or intensity of precipitation, an empirical forecast, or the optimal persistence for any fixed finite observation length. The two limits (long window then large spell length) cannot be interchanged without additional uniform analysis. The precise optimization theorem has not been independently validated. Earlier equivalent optimization results in older run-reliability or meteorology literature cannot be excluded absolutely, especially where the complete manuscript was not accessible.

## References

- J. E. Caskey Jr. (1963), *A Markov Chain Model for the Probability of Precipitation Occurrence in Intervals of Various Length*, Monthly Weather Review 91, 298–301, DOI 10.1175/1520-0493(1963)091<0298:AMCMFT>2.3.CO;2. First public date: 1963-06-01.
- L. L. Weiss (1964), *Sequences of Wet or Dry Days Described by a Markov Chain Probability Model*, Monthly Weather Review 92, 169–176, DOI 10.1175/1520-0493(1964)092<0169:SOWODD>2.3.CO;2.
- J. C. Fu, L. Wang and W. Y. W. Lou (2003), *On exact and large deviation approximation for the distribution of the longest run in a sequence of two-state Markov dependent trials*, Journal of Applied Probability 40, 346–360, DOI 10.1239/jap/1053003548.
- M. V. Koutras (1997), *Waiting Time Distributions Associated with Runs of Fixed Length in Two-State Markov Chains*, Annals of the Institute of Statistical Mathematics 49, 123–139, DOI 10.1023/A:1003118807148.
- W. Y. W. Lou (1996), *On Runs and Longest Run Tests*, Journal of the American Statistical Association 91, 1595–1601, DOI 10.1080/01621459.1996.10476727.
- K. Sen, A. Mohan and R. Agarwal (2013), *Distributions of Patterns of Pair of Successes Separated by Failure Runs ... Markov Dependent Trials: GERT Approach*, DOI 10.1155/2013/494976.
- S. S. Samarova (1982), *On the Length of the Longest Head-Run for a Markov Chain with Two States*, Theory of Probability and Its Applications 26, 498–509, DOI 10.1137/1126056.
