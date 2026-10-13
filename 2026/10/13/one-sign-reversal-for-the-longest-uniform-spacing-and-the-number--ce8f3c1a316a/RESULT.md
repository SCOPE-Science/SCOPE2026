# One sign reversal for the longest uniform spacing and the number of long spacings

## Finding
For every integer \(m\ge2\), let \(D=(D_1,\ldots,D_m)\sim\operatorname{Dirichlet}(1,\ldots,1)\). Define the longest spacing \(M_m=\max_iD_i\) and the number of threshold-exceeding spacings \(K_m(t)=\sum_i\mathbf1\{D_i>t\}\), for \(0<t<1\). These are the spacings obtained from \(m-1\) iid uniform points on the unit interval, including the two boundary gaps.

There is a unique crossover \(t_m\in(0,1)\) with
\[
\operatorname{Cov}(M_m,K_m(t))<0\ (0<t<t_m),\qquad
\operatorname{Cov}(M_m,K_m(t_m))=0,\qquad
\operatorname{Cov}(M_m,K_m(t))>0\ (t_m<t<1).
\]
For \(m=2\), \(t_2=1/2\). For \(m\ge3\), \(1/m<t_m<1/2\). With all logarithms natural,
\[
\boxed{m t_m=\log\log m+\log\log\log m+o(1)}\qquad(m\to\infty).
\]
An exact finite identity for all \(m\ge2\) and \(0<t<1\) is
\[
\operatorname{Cov}(M_m,K_m(t))
=(1-t)^{m-1}\bigl(1+(m-1)t-H_m\bigr)
+\sum_{j=1}^{m-1}\frac{(-1)^{j+1}}{j(j+1)}\binom{m-1}{j}
\bigl(1-(j+1)t\bigr)_+^m,
\]
where \(H_m=\sum_{j=1}^m1/j\) and \(u_+=\max\{0,u\}\).

## Assumptions and scope
The simplex distribution is uniform, with all Dirichlet shape parameters equal to one; no corresponding assertion is made for unequal or nonunit shape parameters. The threshold is deterministic and strictly between zero and one. The number of spacings \(m\) is finite in the sign theorem and tends to infinity in the location law. We use strict exceedances; ties have probability zero in the nontrivial interior.

## Proof
**1. Conditional shifting identity.** By exchangeability and the standard uniform-simplex section law, conditional on \(D_1>t\), the vector \(D\) is distributed as
\[
(t+(1-t)B_1,(1-t)B_2,\ldots,(1-t)B_m),
\]
where \(B\) is an independent uniform point on the same simplex. Put \(\mu=\mathbb E M_m=H_m/m\), \(\delta=t/(1-t)\),
\[
\Phi_m(s)=\mathbb E\max\{B_1+s,B_2,\ldots,B_m\},\quad
p_m(s)=\mathbb P\{B_1+s>\max_{2\le j\le m}B_j\}.
\]
The function \(\Phi_m\) is absolutely continuous and \(\Phi_m(\delta)=\mu+\int_0^\delta p_m(s)\,ds\). As \(\mathbb P(D_1>t)=(1-t)^{m-1}\),
\[
\begin{aligned}
C_m(t)&:=\operatorname{Cov}(M_m,K_m(t))\\
&=m(1-t)^m\left(\int_0^\delta p_m(s)\,ds-\mu\delta\right)\\
&=mt(1-t)^{m-1}\left(\frac1\delta\int_0^\delta p_m(s)\,ds-\mu\right).
\end{aligned}
\]
Thus the covariance sign equals the sign of the averaged win probability relative to \(\mu\).

**2. Exactly one change of sign.** The event defining \(p_m(s)\) increases with \(s\). For every \(0<a<b<1\) it increases with *strictly positive* probability: the continuous simplex law gives positive probability that \(\max_{j\ge2}B_j-B_1\in(a,b)\). Hence \(p_m\) is strictly increasing on \((0,1)\); it equals one for \(s\ge1\), and \(p_m(0)=1/m\). Its running average
\[
R_m(\delta)=\delta^{-1}\int_0^\delta p_m(s)\,ds
\]
is strictly increasing for all \(\delta>0\), because \(p_m\) is nonconstant on every initial interval and \(R_m'(\delta)=[p_m(\delta)-R_m(\delta)]/\delta>0\). Its limiting values are \(1/m\) and one. Because \(1/m<H_m/m<1\) for \(m\ge2\), the intermediate value theorem gives exactly one \(\delta_m>0\) with \(R_m(\delta_m)=H_m/m\). Set \(t_m=\delta_m/(1+\delta_m)\).

For \(m=2\), direct evaluation gives \(t_2=1/2\). For \(0<t\le1/m\), a remaining coordinate is always at least as large as \(D_1=t\), and direct beta conditioning yields
\[
C_m(t)=\frac1m-(1-t)^{m-1}\left(\frac1m+H_{m-1}t\right).
\]
At \(t=1/m\) this is negative for every \(m\ge3\): for \(m=3,4\) directly, and for \(m\ge5\) using \((1-1/m)^{m-1}>e^{-1}\) and \(1+H_{m-1}\ge1+H_4>e\). Thus \(t_m>1/m\). At \(t=1/2\), the count is \(K_m(t)=\mathbf1\{M_m>t\}\) almost surely. For \(m\ge3\), this event is nondegenerate and monotone in \(M_m\), giving strictly positive covariance. Hence \(t_m<1/2\).

**3. Exact identity.** Inclusion–exclusion for the simplex gives the exact win probability
\[
p_m(s)=\sum_{j=0}^{m-1}\frac{(-1)^j}{j+1}\binom{m-1}{j}(1-js)_+^{m-1},\qquad s\ge0.
\]
Integrating each term gives
\[
\int_0^\delta p_m(s)\,ds=\delta+
\sum_{j=1}^{m-1}\frac{(-1)^j}{mj(j+1)}\binom{m-1}{j}\bigl[1-(1-j\delta)_+^m\bigr].
\]
Equivalently, direct integration over \(D_1>t\) of the usual inclusion–exclusion maximum formula yields the displayed exact finite covariance formula. Both independent exact expressions are included in the standalone checker.

**4. Double-logarithmic crossover.** Write \(B_i=E_i/S\), where the \(E_i\) are independent unit exponentials and \(S=\sum_iE_i\). For any \(s\ge0\),
\[
p_m(s/m)=\mathbb P\{E_1+(s/m)S>\max_{j\ge2}E_j\}.
\]
For deterministic \(y\ge0\), elementary integration gives
\[
a_m(y)=\mathbb P\{E_1+y>\max_{j\ge2}E_j\}
=\frac{e^y}{m}\left[1-(1-e^{-y})^m\right].
\]
Let \(\epsilon_m=m^{-1/3}\). A Gamma concentration bound gives \(\mathbb P\{|S/m-1|>\epsilon_m\}\le2e^{-c m^{1/3}}\) for a universal \(c>0\). The above events are sandwiched between those defining \(a_m(s(1-\epsilon_m))\) and \(a_m(s(1+\epsilon_m))\), up to this exponentially small probability. Since \(m e^{-3\log\log m} =m/(\log m)^3\to\infty\), uniformly for \(0\le s\le3\log\log m\),
\[
p_m(s/m)=\frac{e^s}{m}(1+o(1)).
\]
Consequently, uniformly at \(s=\log\log m+\log\log\log m+O(1)\),
\[
R_m(s/m)=\frac{e^s-1}{ms}(1+o(1)).
\]
For fixed \(\eta>0\), substituting \(s_\pm=\log\log m+\log\log\log m\pm\eta\) gives \(R_m(s_\pm/m)/(H_m/m)\to e^{\pm\eta}\), since \(H_m=\log m+O(1)\). Strict monotonicity brackets \(m\delta_m\) between \(s_-\) and \(s_+\) for large \(m\). Sending \(\eta\downarrow0\) gives \(m\delta_m=\log\log m+\log\log\log m+o(1)\). Finally \(t_m=\delta_m/(1+\delta_m)\) and \(m\delta_m^2\to0\), yielding the asserted law.

## Verification
Run `python3 verify.py` with Python 3 and no external dependencies. The script evaluates the exact covariance in two algebraically independent forms using rational arithmetic for \(m=2,\ldots,12\), at the 99 rational thresholds \(t=1/100,\ldots,99/100\), a total of 1,089 exact identities, plus exact endpoint and threshold-region sign checks. This finite test corroborates the algebra and does not certify universal signs or the asymptotic rate; those follow from the proof above.

## Relationship to prior work
Bairamov, Berred, and Stepanov (first published online 10 April 2008) analyze ordered uniform spacings, the largest spacing, and exceedance statistics of distinct constructions, supplying classical background for the object and marginal maximum. Their article was examined, including the ordered-spacing formulas and its later exceedance theorems; it does not state the same-sample longest-spacing/threshold-count covariance or its unique crossover. Kochar's review surveys stochastic orderings of spacings but does not state this mixed-covariance classification. Pyke (1965) and Huffer (1988) give broader classical spacing and joint-distribution methods, creating an acknowledged possibility of implicit derivation; their complete texts were not obtained in this examination. Thus the novelty assessment concerns the particular global one-crossing law and double-logarithmic location, not foundational spacing identities.

## Limitations
No comparable result is established for nonsymmetric Dirichlet laws, for other powers of the longest spacing, or for dependent/nonuniform spacings. The expansion is an additive \(o(1)\) statement after multiplication by \(m\), and no explicit finite-\(m\) error bound is claimed. The novelty assessment is based on accessible literature and does not establish exhaustive historical priority. Independent validation has not been performed.

## References
1. I. Bairamov, A. Berred, and A. Stepanov, “Limit results for ordered uniform spacings,” *Statistical Papers* 51 (2010), 227–240, first published online 10 April 2008, DOI: 10.1007/s00362-008-0134-3.
2. S. Kochar, “Stochastic Comparisons of Order Statistics and Spacings: A Review,” *ISRN Probability and Statistics* (2012), Article 839473, DOI: 10.5402/2012/839473.
3. R. Pyke, “Spacings,” *Journal of the Royal Statistical Society, Series B* 27 (1965), 395–436, DOI: 10.1111/j.2517-6161.1965.tb00602.x.
4. F. W. Huffer, “Divided differences and the joint distribution of linear combinations of spacings,” *Journal of Applied Probability* 25 (1988), 346–354, DOI: 10.2307/3214442.
