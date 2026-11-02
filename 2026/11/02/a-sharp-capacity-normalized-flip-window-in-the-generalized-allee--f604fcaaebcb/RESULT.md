# A sharp capacity-normalized flip window in the generalized Allee–logistic map

## Finding
For the generalized Allee–logistic (GAL) family
\[
f_{r,m,h}(x)=r x(1-x)\bigl[1-m(1+h-x)\bigr],\qquad 0\le x\le1,
\]
let \(h\in[0,1]\), \(0\le m\le1/(1+h)\), and \(r>0\). Define \(A=1-m(1+h)\) and \(g(x)=x(1-x)(A+mx)\). Let \(c\) be the unique maximizer of \(g\) on \([0,1]\), and set
\[
r_{\mathrm{cap}}=\frac1{g(c)}.
\]
Then the map preserves \([0,1]\) **exactly** when \(0<r\le r_{\mathrm{cap}}\). The upper positive fixed-point branch undergoes its unique generic supercritical period-doubling (flip) at
\[
r_{\mathrm{flip}}=\frac1{(1-u)(A+mu)},
\]
where
\[
(c,u)=\left(\tfrac12,\tfrac23\right)\quad\text{when }m=0,
\]
and, when \(m>0\),
\[
c=\frac{m-A+\sqrt{(m-A)^2+3mA}}{3m},\qquad
u=\frac{3(m-A)+\sqrt{9(m-A)^2+32mA}}{8m}.
\]
The first-flip location, normalized by the maximum biologically admissible reproduction parameter, obeys the **sharp universal inequalities**
\[
\boxed{\frac34\le\frac{r_{\mathrm{flip}}}{r_{\mathrm{cap}}}\le\frac{64}{81}<1.}
\]
Equality on the left holds only for \(m=0\), and on the right only for \(A=0\). At fixed \(h\), the ratio increases strictly with \(m\) in the interior of its permitted range, as does the unnormalized \(r_{\mathrm{flip}}\). More intrinsically, the ratio is a strictly increasing function of \(s=m/(A+m)\in[0,1]\), independent of the absolute scale \(A+m\). Consequently, a genuine positive-branch flip always occurs **before** the GAL map loses the invariant population interval, and the two extremal shape limits give exact fractions \(3/4\) and \(64/81\) of the entire admissible reproduction range.

## Assumptions and scope
The conditions \(0\le m\le1/(1+h)\) guarantee \(A\ge0\), \(m\ge0\), and \(A+m>0\). They are a nonnegative-growth subfamily of the source's model, not a claim covering the full range of model parameters. Here “first flip” means the first multiplier \(-1\) event of the **upper positive fixed-point branch**, not the first chaotic parameter or necessarily a global change in extinction basins. Near that flip the fixed point is in \((0,1)\) and the newly created attracting two-cycle is local; coexistence with the extinction attractor is allowed. No claim is made about subsequent period doublings or global attracting sets.

## Proof
**1. Exact capacity.** Because \(g(x)\ge0\) and \(g(0)=g(1)=0\), interval invariance is equivalent to \(r\max_{[0,1]}g\le1\). The derivative is
\[
g'(x)=A(1-2x)+mx(2-3x).
\]
It has precisely one interior zero \(c\in[1/2,2/3]\) (strictly interior for \(A,m>0\)), with \(g\) increasing before \(c\) and decreasing afterward. Solving this quadratic gives the formula for \(c\) above and proves the capacity formula.

**2. Upper fixed point and unique flip.** Every positive fixed point solves
\[
rq(x)=1,\qquad q(x)=(1-x)(A+mx).
\]
Let the upper branch mean the positive solution with \(q'(x)<0\); for \(m=0\), this is the unique positive branch, and at the saddle-node or extinction boundary the statement is interpreted one-sided. On this branch, \(q\) strictly decreases and thus \(x\) strictly increases with \(r\). Its multiplier is
\[
\lambda(x)=f'_{r,m,h}(x)=1+x\frac{q'(x)}{q(x)}.
\]
Here \(q'/q<0\) and
\[
\frac{d}{dx}\frac{q'}q=-\frac1{(1-x)^2}-\frac{m^2}{(A+mx)^2}<0,
\]
so \(\lambda\) decreases strictly from \(+1\) at branch birth toward values below \(-1\). The equation \(\lambda(u)=-1\) is
\[
A(2-3u)+mu(3-4u)=0,
\]
which has exactly one solution \(u\in[2/3,3/4]\), given by the displayed formula. The multiplier crosses \(-1\) transversely as \(r\) increases; the upper branch is locally attracting after its birth and before this crossing, and locally repelling immediately after it.

Write the local map at the flip as \(z\mapsto-z+a_2z^2+a_3z^3\). Its coefficients satisfy
\[
a_2=-r_{\mathrm{flip}}[A+m(3u-1)],\qquad a_3=-r_{\mathrm{flip}}m.
\]
Because \(u\ge2/3\), \(A+m(3u-1)\ge A+m\), while \((1-u)(A+mu)\le(A+m)/3\) implies \(r_{\mathrm{flip}}(A+m)\ge3\). Hence
\[
a_2^2+a_3\ge r_{\mathrm{flip}}[3(A+m)-m]>0.
\]
The cubic term of the second iterate is \(-2(a_2^2+a_3)z^3\), so the nondegenerate, transverse flip is supercritical and creates a locally attracting primitive two-cycle for parameters just above \(r_{\mathrm{flip}}\).

**3. Sharp universal monotonicity.** Set \(s=m/(A+m)\) and \(K_s(x)=1-s+sx\). Common scaling by \(A+m\) cancels from the ratio
\[
R(s)=\frac{r_{\mathrm{flip}}}{r_{\mathrm{cap}}}
=\frac{c(1-c)K_s(c)}{(1-u)K_s(u)}.
\]
The maximizing and flip equations give two strictly increasing coordinate parametrizations
\[
s=\frac{2c-1}{4c-3c^2-1},\qquad
s=\frac{3u-2}{2(2u-1)(1-u)},
\]
with \(1/2\le c\le2/3\) and \(2/3\le u\le3/4\). Differentiating the second relation yields
\[
u'(s)=\frac{2(1-u)^2(2u-1)^2}{6u^2-8u+3}>0.
\]
Using the stationarity of the maximum at \(c\), and \(u q'(u)/q(u)=-2\), logarithmic differentiation simplifies to
\[
\frac{d}{ds}\log R
=\frac{2(2u-1)(3u^2-3u+1)}{u(6u^2-8u+3)K_s(c)}\left[c-\frac{u^2(2u-1)}{3u^2-3u+1}\right].
\]
Every factor before the square bracket is positive. Put
\[
T(u)=\frac{u^2(2u-1)}{3u^2-3u+1}.
\]
The function \(T\) increases from \(4/9\) to \(9/14\) on \([2/3,3/4]\); its derivative is \(u(6u^3-12u^2+9u-2)/(3u^2-3u+1)^2>0\). The increasing function \(s_c(z)=(2z-1)/(4z-3z^2-1)\) is well-defined on \([4/9,2/3]\), with derivative
\[
s_c'(z)=\frac{2(3z^2-3z+1)}{(z-1)^2(3z-1)^2}>0.
\]
Direct algebra shows
\[
s_u(u)-s_c(T(u))=
\frac{u\bigl(12u^4-24u^3+22u^2-12u+3\bigr)}
{2(2u-1)(2u^2-2u+1)(6u^3-6u^2+3u-1)}>0.
\]
Indeed, with \(v=u-2/3\in[0,1/12]\), the numerator's quartic factor is
\[
12v^4+8v^3+6v^2-\frac49v+\frac1{27}>0;
\]
its last two terms have nonnegative sum throughout this interval, and the remaining positive terms prevent equality. All denominators above are positive on the stated ranges. Since \(s_u(u)=s_c(c)\), strict monotonicity of \(s_c\) implies \(c>T(u)\). Therefore \(R'(s)>0\) for \(0<s<1\).

At \(s=0\), one has \(c=1/2\), \(u=2/3\), giving \(R(0)=(1/4)/(1/3)=3/4\). At \(s=1\), one has \(c=2/3\), \(u=3/4\), giving \(R(1)=(4/27)/(3/16)=64/81\). The strict interior inequalities and equality cases follow. At fixed \(h\), \(s(m)=m/(1-mh)\) is strictly increasing. Finally \(r_{\mathrm{flip}}=1/q_m(u(m))\): the factor \(q_m(x)=(1-x)[1-m(1+h-x)]\) decreases strictly as \(m\) increases at each \(0<x<1\), while \(q_m(u)\) decreases with \(u\) on the upper branch and \(u(m)\) is increasing. Thus \(r_{\mathrm{flip}}\) also strictly increases with \(m\). This completes the proof.

## Verification
Run \(\texttt{python verify.py}\) with SymPy available. The standalone script checks the polynomial derivatives, the two shape-coordinate relations, the exact quartic identity underlying the monotonicity proof, and both rational endpoint ratios. It also evaluates five algebraic sample shapes and runs 999 numerical diagnostics solely as supplementary checks. The global result and strict inequalities are proved analytically above, not inferred from finite evaluation.

## Relationship to prior work
Pires, Andrade Jr., and Herrmann introduced the same GAL map, derived its stationary branches and tricriticality, and numerically studied the impact of Allee strength on chaotic transitions. The formula for the GAL map, the existence of equilibria, and the qualitative observation that the Allee effect delays chaotic behavior are **not new**. The present claim instead concerns the exact first **fixed-point flip** and its capacity-normalized monotonic universal window; the source's accessible complete text does not state this result. The logistic endpoint and the pure cubic endpoint have classical or previously documented fixed-point bifurcation thresholds; novelty is **not** asserted for those isolated cases. The new assertion is the uniform, strict inequality and monotonic interpolation for the whole nonnegative GAL shape family.

Rocha and Taha (2019) classify fixed-point stability for a four-parameter family of generalized Allee-logistic maps, but their complete text could not be accessed for a decisive comparison of all possible reductions. Their abstract alone does not establish or exclude the present shape-normalized inequality. Rak and Rak (2015) study \(r x^p(1-x^q)\), which overlaps endpoint shapes but not this affine Allee interpolation in general.

## Limitations
The theorem requires \(A=1-m(1+h)\ge0\); it does not cover all parameters discussed in the motivating source, especially configurations for which the Allee factor becomes negative at small densities. It analyzes local upper-branch period doubling rather than global chaos onset. At or after the flip, no global basin classification is claimed. Some related older literature was not available in full, so historical priority is provisional and no independent audit has been carried out.

## References
1. M. A. Pires, J. S. Andrade Jr., and H. J. Herrmann, *Tricriticality and chaos in a generalized Allee-logistic map*, arXiv:2606.05351v1 (submitted June 3, 2026), https://arxiv.org/abs/2606.05351 . Full public text inspected at https://www.researchgate.net/publication/406059459_Tricriticality_and_chaos_in_a_generalized_Allee-logistic_map .
2. J. Leonel Rocha and A.-K. Taha, *Allee's Effect Bifurcation in Generalized Logistic Maps*, International Journal of Bifurcation and Chaos **29** (2019), article 1950039, https://doi.org/10.1142/S0218127419500391 . Abstract inspected; complete text inaccessible.
3. R. Rak and E. Rak, *Route to chaos in generalized logistic map*, arXiv:1502.00248 (2015), https://arxiv.org/abs/1502.00248 . Different power-law family.
