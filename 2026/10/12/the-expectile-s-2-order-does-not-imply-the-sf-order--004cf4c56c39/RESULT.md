# The expectile \(s_2\)-order does not imply the \(sf\)-order
## Finding
Eberl and Klar define
\[
s_{2,X}(\alpha)
=
\frac{1}{1-2\alpha}
\frac{e_X(1-\alpha)+e_X(\alpha)-2\mu_X}
{e_X(1-\alpha)-e_X(\alpha)},
\qquad 0<\alpha<\frac12,
\]
and write \(X\le_{s_2}Y\) if this quantity for \(X\) does not exceed that for \(Y\) at every \(\alpha\). They also define
\[
\widetilde S_X(t)=S_X(td_X),
\qquad
S_X(u)=\frac{\pi_X(\mu_X+u)-\pi_X(\mu_X-u)}{u}+1,
\]
where \(d_X=E|X-\mu_X|\) and \(\pi_X(z)=E(X-z)_+\), and write \(X\le_{sf}Y\) when
\[
\widetilde S_X(t)\le \widetilde S_Y(t)
\qquad\text{for every }t>0.
\]

The implication
\[
X\le_{s_2}Y\Longrightarrow X\le_{sf}Y
\]
is false even within the atomless interval-support setting of that work.

An exact finite-support seed is
\[
P_X=\frac35\delta_{-83/100}+\frac3{10}\delta_{123/100}+\frac1{10}\delta_{135/100},
\tag{1}
\]
\[
P_Y=\frac3{20}\delta_{-9/5}+\frac{27}{50}\delta_{-2/5}+\frac14\delta_{9/10}+\frac3{50}\delta_5.
\tag{2}
\]
For these two laws,
\[
s_{2,X}(\alpha)<s_{2,Y}(\alpha)
\qquad\text{for every }0<\alpha<\frac12,
\tag{3}
\]
but after mean/MAD standardization,
\[
\widetilde S_X\!\left(\frac45\right)=\frac15
>
\frac{73441}{569900}
=
\widetilde S_Y\!\left(\frac45\right).
\tag{4}
\]
Hence the seed satisfies \(X<_{s_2}Y\) while violating \(X\le_{sf}Y\).

The strict inequalities persist after a small explicit smoothing. For a seed law \(P\) with support endpoints \(\ell<u\), let \(K_\varepsilon\) have triangular density
\[
k_\varepsilon(x)
=
\frac{(\varepsilon^2-|x|)_+}{\varepsilon^4},
\]
and put
\[
P^{(\varepsilon)}
=
(1-\varepsilon)(P*K_\varepsilon)
+
\varepsilon U[\ell-\varepsilon,u+\varepsilon].
\tag{5}
\]
For every sufficiently small \(\varepsilon>0\), the two laws obtained from (1) and (2) have atomless interval supports and strictly positive densities throughout those intervals, and they still satisfy (3) and (4). Thus the failure of the implication is not an artifact of atoms.

## Assumptions and scope
The order definitions are exactly those in Eberl and Klar. The final counterexample consists of bounded atomless distributions with interval support, strictly increasing continuous cdf, and finite moments of all orders.

The result disproves only the direction
\[
\le_{s_2}\Longrightarrow\le_{sf}.
\]
It does not decide whether \(\le_{sf}\) implies \(\le_{s_2}\).

The finite-support pair is used as a transparent algebraic seed. The smoothing step is part of the proof and is needed to return to the standing atomless interval-support assumptions of the motivating paper.

## Proof
For a finite law supported at \(x_1<\cdots<x_m\) with probabilities \(p_i\), its \(\alpha\)-expectile is the unique solution of
\[
\alpha E(X-e)_+=(1-\alpha)E(e-X)_+.
\tag{6}
\]
On any interval \(x_j<e<x_{j+1}\), (6) is linear in \(e\), so the expectile is a rational function of \(\alpha\).

For (1), the only break relevant to \(s_2\) occurs at \(\alpha=1/104\), and direct substitution into (6) gives
\[
s_{2,X}(\alpha)=
\begin{cases}
\displaystyle
\frac{1784\alpha-127}{5(2\alpha-1)(312\alpha+109)},
&0<\alpha<\frac1{104},\\[3mm]
\displaystyle\frac15,
&\frac1{104}\le\alpha<\frac12.
\end{cases}
\tag{7}
\]
For (2), the relevant breaks are \(2/11\) and \(210/859\), and
\[
s_{2,Y}(\alpha)=
\begin{cases}
\displaystyle
\frac{5731\alpha-4683}{5(2\alpha-1)(15037\alpha+2040)},
&0<\alpha<\frac2{11},\\[3mm]
\displaystyle
-\frac{28246\alpha-953}{10(2\alpha-1)(5154\alpha+1805)},
&\frac2{11}\le\alpha<\frac{210}{859},\\[3mm]
\displaystyle\frac{19}{50},
&\frac{210}{859}\le\alpha<\frac12.
\end{cases}
\tag{8}
\]

Subtracting (7) from (8) and splitting at all breakpoints gives four expressions. On
\[
0<\alpha<\frac1{104},
\]
the difference is
\[
-\frac{25037936\alpha^2+2566078\alpha+251367}
{5(2\alpha-1)(312\alpha+109)(15037\alpha+2040)}>0,
\tag{9}
\]
because all factors except \(2\alpha-1\) have positive sign. On
\[
\frac1{104}\le\alpha<\frac2{11},
\]
the difference is
\[
-\frac{30074\alpha^2-16688\alpha+2643}
{5(2\alpha-1)(15037\alpha+2040)}>0.
\tag{10}
\]
The numerator quadratic in (10) is strictly positive because its discriminant is
\[
-39452984<0.
\]
On
\[
\frac2{11}\le\alpha<\frac{210}{859},
\]
the difference is
\[
-\frac{3(6872\alpha^2+8386\alpha-1521)}
{10(2\alpha-1)(5154\alpha+1805)}>0.
\tag{11}
\]
The polynomial in parentheses is strictly increasing for positive \(\alpha\) and at \(2/11\) equals
\[
\frac{27939}{121}>0.
\]
Finally, on
\[
\frac{210}{859}\le\alpha<\frac12,
\]
the difference is exactly
\[
\frac9{50}>0.
\tag{12}
\]
Equations (9)--(12) prove (3).

For the \(sf\)-comparison, the seed means and MADs are
\[
\mu_X=\frac3{500},
\qquad
d_X=\frac{627}{625},
\]
\[
\mu_Y=\frac{39}{1000},
\qquad
d_Y=\frac{51291}{50000}.
\]
Thus the mean/MAD standardized supports are
\[
\left\{-\frac56,\frac{255}{209},\frac{280}{209}\right\}
\]
for \(X\), and
\[
\left\{-\frac{30650}{17097},-\frac{21950}{51291},
\frac{350}{417},\frac{6050}{1251}\right\}
\]
for \(Y\), with the original probabilities. Evaluating the stop-loss transforms at \(t=4/5\) yields exactly (4). Hence \(X\not\le_{sf}Y\).

It remains to justify atomless interval-support counterexamples. We use the smoothing family (5). The uniform component gives every \(P^{(\varepsilon)}\) a strictly positive density on the full interval \([\ell-\varepsilon,u+\varepsilon]\), while
\[
P^{(\varepsilon)}\to P
\]
in \(1\)-Wasserstein distance as \(\varepsilon\downarrow0\).

We need stability uniformly over the whole expectile-skewness profile. For a bounded law \(P\), the expectile is the unique zero of
\[
G_{P,\alpha}(z)
=
\alpha E_P(X-z)_+-(1-\alpha)E_P(z-X)_+.
\tag{13}
\]
On compact support, (13) is jointly continuous in \(P,\alpha,z\) under \(1\)-Wasserstein convergence and is strictly decreasing in \(z\). Hence the expectile curves converge uniformly on every closed subinterval of \((0,1)\).

For the endpoints of the normalized profile, bounded laws with no atom at their mean have the continuous extensions
\[
\overline s_{2,P}(0)
=
\frac{u+\ell-2\mu_P}{u-\ell},
\tag{14}
\]
and
\[
\overline s_{2,P}\!\left(\frac12\right)
=
2F_P(\mu_P)-1.
\tag{15}
\]
Formula (14) follows from the expectiles tending to the support endpoints. To prove (15), rewrite (6) exactly as
\[
e_P(\alpha)-\mu_P
=
(2\alpha-1)E|X-e_P(\alpha)|.
\tag{16}
\]
Expanding the absolute-deviation function at the mean, whose derivative is \(2F_P(\mu_P)-1\) when there is no atom at the mean, gives (15).

For the two seed laws the means lie in gaps between atoms. In the explicit family (5), those gaps remain free of the narrow triangular bumps for all small \(\varepsilon\); only the uniform background contributes there. Consequently the endpoint expansions (14)--(16) are uniform as \(\varepsilon\downarrow0\). Near \(\alpha=0\), the fixed positive mass in the lowest and highest bumps gives the same uniform endpoint control directly from (13). Combining those two endpoint neighborhoods with interior uniform convergence gives
\[
\overline s_{2,P_X^{(\varepsilon)}}
\longrightarrow
\overline s_{2,P_X},
\qquad
\overline s_{2,P_Y^{(\varepsilon)}}
\longrightarrow
\overline s_{2,P_Y}
\]
uniformly on \([0,1/2]\).

The seed difference extends continuously to that compact interval. Its endpoint values are
\[
\frac{83789}{370600}>0
\quad\text{at }\alpha=0,
\qquad
\frac9{50}>0
\quad\text{at }\alpha=\frac12,
\]
and (9)--(12) show that it is positive everywhere in between. It therefore has a positive minimum. Uniform convergence preserves the strict \(s_2\)-ordering for every sufficiently small \(\varepsilon\).

Finally, mean, MAD, and stop-loss transforms are continuous under bounded \(1\)-Wasserstein perturbations. The strict seed gap
\[
\widetilde S_X(4/5)-\widetilde S_Y(4/5)
=
\frac{40539}{569900}>0
\]
therefore persists for all sufficiently small \(\varepsilon\). This proves the atomless interval-support counterexample.

## Verification
The bundled `verify.py` uses exact rational arithmetic to recompute the two seed means and MADs, the standardized support points, the expectile breakpoint locations, the four sign certificates in (9)--(12), and the exact \(sf\)-violation at \(t=4/5\). It also evaluates the finite-support expectile equation directly at deterministic rational \(\alpha\)-values on every algebraic piece and compares it to (7)--(8).

A successful run ends with
`VERIFY_OK breaks=1/104,2/11,210/859 sf_gap=40539/569900`.

The checker does not replace the smoothing argument. Existence of continuous counterexamples follows analytically from the strict compact profile margin and the stability lemma proved above.

## Relationship to prior work
Eberl and Klar introduced the normalized expectile-skewness profile \(s_2\), the mean/MAD-standardized \(sf\)-order, and in Remark 6 explicitly asked whether \(\le_{s_2}\) implies \(\le_{sf}\) or conversely. Their paper proves both orders are implied by stronger skewness orders but does not compare these two weak orders directly.

The same paper uses a discrete construction in its expectile-dispersive section and explicitly notes that the statement persists under sufficiently close continuous approximation. The smoothing step above is analogous in spirit but includes an explicit uniform-profile stability argument because \(\le_{s_2}\) quantifies over every \(\alpha\in(0,1/2)\).

Eberl's 2022 dissertation gives a later full treatment of both families of expectile-based skewness measures. It proves that, for a single distribution, nonnegativity of the entire \(s_2\)-family is equivalent to nonnegativity of the entire integrated-cdf family, and that both families characterize symmetry. Those are sign comparisons against zero, not pairwise order implications between two arbitrary distributions; the inspected section does not state a result covering the counterexample here.

Arab, Lando, and Oliveira show that the standardized expectile order is a skewness order and thereby support the stronger chain leading to \(sf\). Their result likewise does not imply a pairwise comparison between the \(s_2\)- and \(sf\)-orders.

Targeted searches for the exact order symbols, the open-question wording, expectile-skewness aliases, the rational seed, and the exact \(sf\)-gap did not locate a published resolution of this implication.

## Limitations
Only one direction of the open comparison is resolved:
\[
\le_{s_2}\not\Rightarrow\le_{sf}.
\]
The reverse implication \(\le_{sf}\Rightarrow\le_{s_2}\) remains unproved here.

The atomless counterexamples are established by a sufficiently-small smoothing parameter rather than by a closed numerical upper bound on that parameter. The finite-support seed is exact and fully algebraic, while the persistence step is qualitative but analytic.

Bibliographic searches cannot rule out an independently discovered counterexample under different notation or terminology.

## References
1. A. Eberl and B. Klar, “Stochastic orders and measures of skewness and dispersion based on expectiles,” arXiv:2108.06138v1, 13 August 2021; *Statistical Papers* 64 (2023), 509–527. DOI: 10.1007/s00362-022-01331-x.
2. A. Eberl, *Quantification of Location, Dispersion, Skewness and Kurtosis*, doctoral dissertation, Karlsruhe Institute of Technology, 2022. DOI: 10.5445/IR/1000148810.
3. I. Arab, T. Lando, and P. E. Oliveira, “Comparison of Lp-quantiles and related skewness measures,” *Statistics & Probability Letters* 183 (2022), 109339. DOI: 10.1016/j.spl.2021.109339.
