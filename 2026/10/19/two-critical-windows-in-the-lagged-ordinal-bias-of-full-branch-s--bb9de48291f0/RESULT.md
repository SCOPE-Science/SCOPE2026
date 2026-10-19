# Two critical windows in the lagged ordinal bias of full-branch skew tent maps

## Finding
For \(0<p<1\), consider the Lebesgue-preserving skew tent map
\[
T_p(x)=\begin{cases}x/p,&0\le x\le p,\\ (1-x)/(1-p),&p\le x\le1.\end{cases}
\]
Let \(X\) be uniformly distributed on \([0,1]\), and for every integer \(n\ge1\) define the lagged **ordinal bias**
\[
W_n(p)=\Pr\{X<T_p^n(X)\}-\frac12.
\]
Equalities in this comparison form a finite set and have Lebesgue probability zero. Set
\[
q=1-p,\quad \alpha=2p-1,\quad \beta=p^3+q^3,
\quad \eta=p^4-q^4,\quad \sigma=p^4+q^4.
\]
For every \(p\in(0,1)\) and \(n\ge1\),
\[
\boxed{W_n(p)=\tfrac12\alpha^n+q^2\sum_{j=0}^{n-1}\alpha^{n-1-j}\beta^j
-q^3\sum_{j=0}^{n-1}\beta^{n-1-j}\eta^j+R_n(p),}
\]
with the **explicit uniform-in-time remainder**
\[
\boxed{|R_n(p)|\le \frac{nq^4}{p}\sigma^{n-1}.}
\]
In particular, away from \(p=2/3\),
\[
\boxed{W_n(p)=\frac{p}{2(3p-2)}\alpha^n+
\frac{p^2q}{(2-3p)(4p^2-5p+2)}\beta^n+
O_p(n\sigma^{n-1}).}
\]
The error also includes the exactly known term \(q^3\eta^n/(\beta-\eta)\), bounded by a constant times \(\sigma^n\).

The leading behavior has **two distinct transition parameters**:

* For \(0<p<1/3\), the leading term is \(\frac{p}{2(3p-2)}(2p-1)^n\), which alternates in sign with \(n\).
* At \(p=1/3\),
\[
W_n(1/3)=3^{-n}\left(\frac2{21}-\frac{(-1)^n}{6}\right)+O(n(17/81)^{n-1}).
\]
* For \(1/3<p<2/3\), the leading term is the positive \(\beta^n\)-term displayed above.
* At \(p=2/3\), the two positive modes merge; the following finite-time estimate holds:
\[
\boxed{\left|W_n(2/3)-\left(\frac n3+\frac14\right)3^{-n}-\frac14(5/27)^n\right|
\le \frac n{54}(17/81)^{n-1}.}
\]
* For \(2/3<p<1\), the leading term is the positive \(\frac{p}{2(3p-2)}(2p-1)^n\).

Both transitions have an explicit **inverse-lag parameter window**. For each fixed real \(\lambda\), with parameters understood only for sufficiently large \(n\),
\[
\boxed{3^nW_n\!\left(\frac13+\frac\lambda n\right)
-\frac2{21}e^{-3\lambda}+\frac{(-1)^n}{6}e^{-6\lambda}\longrightarrow0,}
\]
so the sign of the even-lag leading coefficient switches at \(\lambda=(\log(7/4))/3\); odd-lag coefficients remain positive. At the second transition,
\[
\boxed{\frac{3^n}{n}W_n\!\left(\frac23+\frac\lambda n\right)
\longrightarrow\begin{cases}\frac{e^{6\lambda}-e^{3\lambda}}{9\lambda},&\lambda\ne0,\\ \frac13,&\lambda=0.\end{cases}}
\]
Finally, the symmetric map admits the exact formula
\[
\boxed{W_n(1/2)=\frac1{2(4^n-1)}}\qquad(n\ge1).
\]

## Assumptions and scope
The parameter is fixed in \((0,1)\) for all one-parameter estimates. The parameter-window limits are taken with fixed \(\lambda\in\mathbb R\) and integers \(n\to\infty\); no claim of uniformity in unbounded \(\lambda\) is made. The observable compares two points of the same deterministic stationary orbit, not independent random draws. The phase diagram describes asymptotic signs and rates at fixed \(p\), except for the separately stated critical-window limits.

## Proof
**Step 1: exact inverse-cylinder integration.** The two inverse branches are
\[
\phi_0(y)=py,\qquad\phi_1(y)=1-qy,
\]
with signed slopes \(s_0=p\), \(s_1=-q\), absolute branch weights \(u_0=p\), \(u_1=q\), and offsets \(a_0=0\), \(a_1=1\). For each binary word \(w=(w_1,\ldots,w_n)\), the composition \(\phi_{w_1}\circ\cdots\circ\phi_{w_n}\) is \(a_w+s_wy\), where \(|s_w|=\prod_i u_{w_i}\). Its unique fixed point \(r_w=a_w/(1-s_w)\) lies in \([0,1]\). Indeed, the affine branch maps \([0,1]\) into itself and \(|s_w|<1\). On this cylinder, \(X<T_p^n X\) is equivalent to \(y>r_w\), since \(1-s_w>0\). The uniform measure of that event is therefore \(|s_w|(1-r_w)\). Summing over the \(2^n\) cylinders gives
\[
\Pr\{X<T_p^nX\}=1-\sum_w |s_w|\frac{a_w}{1-s_w}.
\]

**Step 2: exact inverse-branch mode expansion.** The affine offset is
\[
a_w=\sum_{j=1}^n a_{w_j}\prod_{i<j}s_{w_i}.
\]
Expand the geometric denominator \((1-s_w)^{-1}=\sum_{k\ge0}s_w^k\). For fixed \(n\) the expansion is absolutely summable because every \(|s_w|<1\). Introduce
\[
A_k=\sum_{b\in\{0,1\}}u_b s_b^k=p^{k+1}+(-1)^kq^{k+1},\qquad
B_k=\sum_bu_ba_b s_b^k=(-1)^kq^{k+1}.
\]
Factorizing the independent choices in each word at each index yields, for every integer \(n\ge1\),
\[
\Pr\{X<T_p^nX\}=1-\sum_{k=0}^{\infty}B_k
\sum_{j=0}^{n-1}A_k^{n-1-j}A_{k+1}^{j}.
\]
Here \(A_0=1\), \(A_1=\alpha\), \(A_2=\beta\), and \(A_3=\eta\). The \(k=0\) term is \(q(1-\alpha^n)/(1-\alpha)=(1-\alpha^n)/2\), giving the displayed three-mode identity for \(W_n\) after retaining \(k=1,2\). For every \(k\ge3\),
\[
|A_k|,|A_{k+1}|\le\sigma<1,
\qquad \sum_{k\ge3}|B_k|=\frac{q^4}{p};
\]
so each inner \(n\)-term sum has modulus at most \(n\sigma^{n-1}\), proving the stated bound. The same reasoning bounds the tail of the full series after \(K\) terms by \(nq^{K+1}/p\) for any \(K\ge0\).

**Step 3: isolate the modes and their exact coefficients.** For \(u\ne v\), the geometric convolution equals \((v^n-u^n)/(v-u)\). The identities
\[
\beta-\alpha=q(2-3p),\qquad
\beta-\eta=q(4p^2-5p+2)
\]
then give, when \(p\ne2/3\),
\[
W_n(p)=d_1(p)\alpha^n+d_2(p)\beta^n+d_3(p)\eta^n+R_n(p),
\]
where
\[
d_1=\frac{p}{2(3p-2)},\quad
 d_2=\frac{p^2q}{(2-3p)(4p^2-5p+2)},\quad
 d_3=\frac{q^2}{4p^2-5p+2}.
\]
The quadratic denominator is positive on \((0,1)\). Moreover \(\sigma<\beta\) and \(|\eta|\le\sigma\). Direct factorization shows that \(|\alpha|>\beta\) exactly for \(0<p<1/3\) or \(2/3<p<1\), while \(\beta>|\alpha|\) for \(1/3<p<2/3\). The coefficient of the dominant mode never vanishes in its stated open range. Since \(\sigma<\max\{|\alpha|,\beta\}\), the remainder is exponentially smaller. At \(p=1/3\) the two dominant moduli agree with opposite signs; substituting \(d_1=-1/6\), \(d_2=2/21\) gives the stated alternating profile. At \(p=2/3\), the two equal positive bases in the convolution give \(n3^{-(n-1)}\), and direct substitution into the three-mode identity gives the exact displayed resonance estimate.

**Step 4: resolve the two transition windows.** If \(p_n=1/3+\lambda/n\), the leading bases satisfy
\[
3^n\alpha(p_n)^n=(-1)^ne^{-6\lambda}+o(1),\quad
3^n\beta(p_n)^n=e^{-3\lambda}+o(1).
\]
The coefficients converge to their values at \(1/3\), and the \(\eta\)-mode plus remainder are uniformly negligible for a fixed \(\lambda\). This proves the first window. At \(p_n=2/3+\lambda/n\), the two positive bases satisfy
\[
3^n\alpha(p_n)^n\to e^{6\lambda},\quad
3^n\beta(p_n)^n\to e^{3\lambda},\quad
n(\beta(p_n)-\alpha(p_n))\to-\lambda.
\]
For \(\lambda\ne0\) divide the convolution by \(n\); at \(\lambda=0\) it is exactly \(n(1/3)^{n-1}\). The other terms divided by \(n3^{-n}\) vanish, proving the second window by continuity. The first window's even-lag zero is obtained by solving \(2e^{-3\lambda}/21=e^{-6\lambda}/6\).

**Step 5: symmetric benchmark.** For \(p=q=1/2\), \(A_{2j}=4^{-j}\) and \(A_{2j+1}=0\). Substituting in the absolutely convergent full series and grouping consecutive even/odd indices gives \(W_n=[2(4^n-1)]^{-1}\) for \(n\ge2\). At \(n=1\), the event interval ends at \(1/(2-p)=2/3\), yielding the same expression.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to enumerate inverse cylinders independently of the power-series derivation. It compares the direct order probabilities with the rigorous three-mode error bound for six rational parameters and nine positive lags each. Further comparisons test independently truncated power series, the symmetric closed formula, and the resonant finite-time bound. Running `python verify.py` returned:

`VERIFY_OK: 54 exact rational cylinder-to-three-mode bounds; 36 independent finite-k power-series estimates; symmetric exact probabilities and resonant inequalities`

The checker is finite corroboration only. The estimates, sign classification, and limit assertions follow analytically from Steps 1–5, not from finite enumeration.

## Relationship to prior work
Arroyo, Alvarez and Amigó (2008) introduced parameter-dependent order-pattern distributions for the **same full-branch skew tent family**, giving in particular an exact length-four *consecutive* increasing-pattern probability. Their analytic example and distribution plots do not evaluate the **two-time comparison at arbitrary lag**, its asymptotic spectrum, the two transition values \(1/3\) and \(2/3\), or the critical windows. Abrams, Babson, Landau, Landau and Pommersheim (2010) study sets of realizable ordinal-pattern distributions across interval maps; their general framework does not state these evaluated parametric lagged probabilities. Unakafov and Keller (2014) treat conditional ordinal-pattern entropy, not the two-time bias spectrum. General inverse-cylinder and expanding-map constructions are background tools, not new contributions here.

## Limitations
The formulas require the full-branch map with Lebesgue stationary initial state; they are not asserted for non-full-branch tent maps, noisy dynamics, or alternative invariant distributions. In critical windows the parameter perturbation is \(O(1/n)\) with fixed window coordinate. At the even-lag leading-zero point in the first window, determining the sign from a smaller-order term would require an additional expansion; no such sign is claimed. The literature comparison is a best-knowledge assessment, not a proof of historical priority. A relevant 2022 paper on periodic points of skew tent maps has an accessible abstract but its full text could not be inspected; its methods could implicitly subsume aspects of the inverse-cylinder enumeration.

## References
1. D. Arroyo, G. Alvarez, J. M. Amigó, *Estimation of the control parameter from symbolic sequences: Unimodal maps with variable critical point*, arXiv:0812.2331v1 (first public 2008-12-12), https://arxiv.org/pdf/0812.2331.
2. A. Abrams, E. Babson, H. Landau, Z. Landau, J. Pommersheim, *Distributions of order patterns of interval maps*, arXiv:1003.5561v1 (first public 2010-03-29), https://arxiv.org/pdf/1003.5561.
3. A. M. Unakafov, K. Keller, *Conditional entropy of ordinal patterns*, arXiv:1407.5390v1 (first public 2014-07-21), https://arxiv.org/pdf/1407.5390.
4. K. Chen, Y.-G. Shi, B. Xu, *Periodic Points of Skew Tent Maps*, Journal of Dynamics and Differential Equations (2022), DOI:10.1007/s10883-022-09594-1 (abstract only inspected).
