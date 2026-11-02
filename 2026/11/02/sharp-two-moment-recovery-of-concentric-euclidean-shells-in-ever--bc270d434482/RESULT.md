# Sharp two-moment recovery of concentric Euclidean shells in every dimension

## Finding
Fix an integer \(d\ge2\). For radii \(0\le a<b<\infty\), let
\[
S(a,b)=\{x\in\mathbb R^d:a\le\|x\|\le b\}.
\]
Choose \(X,Y\) independently from normalized \(d\)-dimensional Lebesgue measure on \(S(a,b)\), and put \(D=\|X-Y\|\), \(M_2=\mathbb E[D^2]\), \(M_4=\mathbb E[D^4]\), and \(q=a/b\). For \(0\le q<1\),
\[
M_2=\frac{2d}{d+2}b^2\frac{1-q^{d+2}}{1-q^d},\qquad
\frac{M_4}{M_2^2}=\frac{d+2}{2d}+\frac{(d+2)^2}{2d(d+4)}\frac{(1-q^{d})(1-q^{d+4})}{(1-q^{d+2})^2}.
\]
The dimensionless ratio \(Q_d(q)=M_4/M_2^2\) is **strictly decreasing** in \(q\), and maps \([0,1)\) bijectively onto
\[
\left(1+\frac1d,\,\frac{(d+2)(d+3)}{d(d+4)}\right].
\]
Hence the pair \((M_2,M_4)\) reconstructs both radii uniquely, including \(a=0\), by solving the displayed strictly monotone scalar equation and then setting
\[
b=\left(\frac{M_2(d+2)(1-q^d)}{2d(1-q^{d+2})}\right)^{1/2},\qquad a=qb.
\]
Conversely these conditions on \(M_2>0\) and \(M_4/M_2^2\) are necessary and sufficient for realization by a nonempty solid shell with \(0\le a<b\). If the central hole must have positive radius, the upper bound is strict. The lower endpoint is a limiting zero-thickness sphere, not an admissible volume-uniform solid shell. One even-distance moment cannot recover two radii because varying \(q\) and adjusting \(b\) as above leaves \(M_2\) fixed.

The two inverse-conditioning boundaries have **different sharp orders**. As \(q\downarrow0\),
\[
Q_d(0)-Q_d(q)=\frac{(d+2)^2}{2d(d+4)}q^d+O_d(q^{d+2}),
\]
and as \(q\uparrow1\),
\[
Q_d(q)-\left(1+\frac1d\right)=\frac{(1-q)^2}{6}+O_d((1-q)^3).
\]
On each compact positive scale range \(0<m\le M_2\le M<\infty\), the inverse from \((M_2,Q_d)\) to the ordered pair \((a,b)\), extended to the zero-thickness endpoint by continuity, is uniformly Hölder with exponent \(1/d\). No exponent greater than \(1/d\) works uniformly in a neighborhood of the solid-ball endpoint. In the thin-shell regime the optimal exponent is \(1/2\). These stability assertions concern deterministic errors in exact population moments, not statistical sampling rates.

## Assumptions and scope
The ambient dimension \(d\ge2\) is known. The shell is concentric and Euclidean, with normalized volume sampling (not boundary-surface sampling); \(a=0\) denotes a complete ball, and \(a=b\) is excluded from the volume-model domain. Both points are independent. The second and fourth powers are powers of their **ordinary Euclidean** separation, not intrinsic paths constrained to the shell. The inverse is unique only within this two-parameter family; arbitrary radial densities and eccentric/off-center cavities are not covered. All formulas are valid for every permitted dimension, radius and scale without a genericity assumption.

## Proof
**1. Radial and angular moments.** Rotational symmetry gives \(\mathbb E[X]=0\) and \(\mathbb E[XX^\mathsf T]=(\mu_2/d)I_d\), where \(\mu_{2j}=\mathbb E\|X\|^{2j}\). The radial density is \(dr^{d-1}/(b^d-a^d)\) multiplied by \(d\) on \([a,b]\). Direct integration, with \(q=a/b\), gives
\[
\mu_{2j}=b^{2j}\frac{d}{d+2j}\frac{1-q^{d+2j}}{1-q^d}\quad(j=1,2).
\]
Expand \(D^2=\|X\|^2+\|Y\|^2-2X\cdot Y\). Independence, centering and isotropy give
\[
M_2=2\mu_2,\qquad
M_4=2\mu_4+2\mu_2^2+4\mathbb E[(X\cdot Y)^2]
=2\mu_4+\left(2+\frac4d\right)\mu_2^2.
\]
Substitution proves both boxed formulas in the Finding. Notice that the angular identity uses only \(\mathbb E[XX^\mathsf T]\); it does not require fourth angular moments or assume coordinate independence.

**2. Strict monotonicity.** Put \(q=e^{-t}\) with \(t>0\), and let
\[
F_d(q)=\frac{(1-q^{d})(1-q^{d+4})}{(1-q^{d+2})^2}.
\]
Differentiating with respect to \(t\) gives
\[
\frac{d}{dt}\log F_d(e^{-t})=g_t(d)+g_t(d+4)-2g_t(d+2),\qquad
 g_t(s)=\frac{s}{e^{st}-1}.
\]
For every \(t>0\), the function \(s\mapsto g_t(s)\) is strictly convex for \(s>0\). Indeed for \(z=st\), writing \(h(z)=z/(e^z-1)\),
\[
h''(z)=\frac{e^z((z-2)e^z+z+2)}{(e^z-1)^3}>0\quad(z>0).
\]
For \(\psi(z)=(z-2)e^z+z+2\), one has \(\psi(0)=\psi'(0)=0\), \(\psi''(z)=ze^z>0\), proving positivity. Since the three arguments are equally spaced, strict convexity makes the derivative of \(\log F_d(e^{-t})\) positive. Thus \(F_d(q)\), and therefore \(Q_d(q)\), strictly **decreases** as \(q\) increases. There are no unproved exceptional dimensions.

**3. Endpoint values, inverse and realizability.** At \(q=0\), \(F_d(0)=1\). As \(q\uparrow1\), first-order expansions give \(F_d(q)\to d(d+4)/(d+2)^2\). The corresponding values are \((d+2)(d+3)/(d(d+4))\) and \(1+1/d\). Continuity and strict monotonicity give precisely the asserted range and unique \(q\). The positive formula for \(b\), and \(a=qb\), give a valid shell for every admissible measurement pair, establishing sufficiency. For any fixed \(M_2>0\), every \(q\in[0,1)\) can be paired with the displayed positive \(b\), showing failure of one-moment reconstruction.

**4. Sharp boundary expansions.** For small \(q\), elementary geometric-series expansion yields \(F_d(q)=1-q^d+O_d(q^{d+2})\), because \(d\ge2\). This gives the exact leading ball coefficient. At the opposite endpoint write \(q=1-\varepsilon\) and let \(U=\|X\|^2/b^2\). The radial coordinate is \(1-\varepsilon T\), where the density of \(T\in[0,1]\) tends uniformly to \(1\) as \(\varepsilon\downarrow0\), with \(O_d(\varepsilon)\) error. Therefore \(U=1-2\varepsilon T+O(\varepsilon^2)\),
\[
\operatorname{Var}(U)=\frac{\varepsilon^2}{3}+O_d(\varepsilon^3),\qquad \mathbb E U=1+O_d(\varepsilon).
\]
Since \(Q_d=(d+2)/(2d)+(\mathbb E U^2)/(2(\mathbb E U)^2)\), the variance identity yields the universal coefficient \(1/6\). The estimates can alternatively be derived by Taylor expansion of the exact rational expression.

**5. Uniform and optimal inverse regularity.** On \(0<q<1\) the derivative is negative. The two preceding expansions show that
\[
\frac{-Q_d'(q)}{q^{d-1}(1-q)}
\]
extends to a strictly positive continuous function on \([0,1]\), with endpoint values \(d(d+2)^2/[2d(d+4)]\) and \(1/3\), respectively. Consequently it is bounded below by \(c_d>0\). For any \(0\le u<v\le1\), splitting the interval at \(1/2\) if necessary gives
\[
Q_d(u)-Q_d(v)\ge c_d\int_u^v s^{d-1}(1-s)\,ds\ge c'_d(v-u)^d,
\]
where the last inequality follows from the lower bounds \(\int_I s^{d-1}ds\ge |I|^d/d\) on the left half and \(\int_I(1-s)ds\ge |I|^2/2\ge |I|^d/2\) on the right half (at least one subinterval has length at least \((v-u)/2\)). Thus \(|u-v|\le C_d|Q_d(u)-Q_d(v)|^{1/d}\). The formula for \(b\) is smooth with bounded first derivatives in \((M_2,q)\) when \(M_2\) lies in a fixed compact positive interval and \(q\in[0,1]\); it extends smoothly at \(q=1\). The same Hölder modulus follows for \((a,b)\). For sharpness, keep \(M_2\) fixed and let \(q\downarrow0\). The outer radius approaches a positive constant while \(a=qb\) differs from zero by order \(q\), but the measured ratio differs from its ball value only by order \(q^d\). This rules out all uniform Hölder exponents greater than \(1/d\). At the thin-shell endpoint, the exact quadratic expansion similarly gives local exponent \(1/2\), and rules out a larger exponent uniformly near that boundary.

## Verification
The standalone, standard-library-only program `verify_shell_moments.py` performs exact rational comparisons of both independent moment formulas in dimensions \(2\) through \(12\), verifies strict ordering on rational shape grids, independently generates Gaussian-normalized directions with exact radial-CDF sampling and compares simulated moments with the formulas, and checks both sharp endpoint coefficients through high-precision rational evaluations. Execute `python verify_shell_moments.py` in the directory containing the file. Successful output ends in `ALL_CHECKS_PASSED`. The analytic argument above, not finite grids or Monte Carlo trials, proves the infinite-dimensional-parametric statements.

## Relationship to prior work
Tu and Fischbach (2002) derived **forward** distance-density formulas for arbitrary radial density distributions in balls; their Sections III, IV and V.3 explicitly encompass layered spherical models, and Section V.1 gives moment formulas for uniform full balls. This prior forward theory encompasses shell geometry as a special sampling density but does **not** state the finite two-moment injectivity, the sharp observable interval, or the two optimal inverse-conditioning exponents proved here. Bonnet, Gusakova, Thäle and Zaporozhets (arXiv first posted 2020-10-07) proved sharp bounds for the **mean first distance** of convex bodies, rather than the inverse higher-even-moment map for nonconvex shells. The published result “Exact visibility laws for concentric spherical shells in odd dimensions” studies the probability that an interpoint **segment stays inside** its shell; its one-probability inversion concerns another observable, and it does not imply the present second/fourth Euclidean-distance-moment injectivity. Relevant existing exact forward moments of inertia for spherical shells likewise cannot be confused with an inverse distance-moment classification. Exhaustive historical priority is not established by search.

## Limitations
These results concern exact population moments and the concentric, uniform-volume model. They do not provide a finite-sample statistical estimator, noise confidence bounds or reconstruction under unknown radial density. The Hölder exponent is a deterministic worst-case inverse modulus; good statistical rates cannot be read from it without an observation model. The limiting infinitely thin shell is not an admissible volume body. The prior literature's general forward density formulas remain stronger for computing the full distance distribution, while the present result is specifically a sharp **finite-data inverse** statement. Independent mathematical validation has not been performed.

## References
1. G. Bonnet, A. Gusakova, C. Thäle and D. Zaporozhets, “Sharp inequalities for the mean distance of random points in convex bodies,” arXiv:2010.03351v1, first publicly posted 2020-10-07, later *Advances in Mathematics* 386 (2021), 107813. https://arxiv.org/abs/2010.03351
2. S.-J. Tu and E. Fischbach, “Random Distance Distribution for Spherical Objects: General Theory and Applications to n-Dimensional Physics,” arXiv:math-ph/0201046v1, first posted 2002-01-22. https://arxiv.org/html/math-ph/0201046v1
3. S.-I. Hong and S.-C. Hong, “Moments of inertia of spheres without integration in arbitrary dimensions,” *European Journal of Physics* 35 (2014), 025003. https://doi.org/10.1088/0143-0807/35/2/025003
4. “Exact visibility laws for concentric spherical shells in odd dimensions,” published-finding corpus published research, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-visibility-laws-for-concentric-spherical-shells-in-odd-dim--611519ee4958
