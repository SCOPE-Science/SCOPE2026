# An exact incidence-only oscillation window in exponential-transmission SIR

## Finding

In a closed susceptible–infectious–removed epidemic with exponentially growing transmission, the existence of repeated *incidence* peaks has an exact threshold strictly below the threshold for repeated *infectious-prevalence* peaks. Consequently there is a nonempty, explicitly computable parameter regime in which incidence has infinitely many strict local maxima and minima, although the number of infectious individuals decreases strictly at all times. The distinction survives in the elementary two-parameter transmission family \(\beta(t)=\beta_0e^{rt}\), without oscillatory forcing or replenishment of susceptibles.

Fix \(0<r<\gamma\), and put \(a=\gamma-r>0\). For a physical initial state \(S_0,I_0>0\), \(R_0=N-S_0-I_0\ge0\), \(N>0\), \(\beta_0>0\), set
\[
X_0=\frac{\beta_0S_0}{N},\qquad Y_0=\frac{\beta_0I_0}{N},\qquad h=\Phi(X_0,Y_0),
\]
where
\[
\Phi(X,Y)=X-a-a\log(X/a)+Y-r-r\log(Y/r).
\]
Define the strictly positive thresholds
\[
 x_*=\frac{3a+r+\sqrt{a^2+6ar+r^2}}4,\quad
 y_*=x_*-a,\quad
 h_{\rm inc}=\Phi(x_*,y_*),\quad
 h_{\rm prev}=\Phi(\gamma,r)=r-a\log(\gamma/a).
\]
Then \(0<h_{\rm inc}<h_{\rm prev}\), and the following **complete phase classification** holds for every such physical initial state:

1. If \(0\le h\le h_{\rm inc}\), both infection incidence and infectious prevalence decrease strictly on \([0,\infty)\) (with at most an isolated horizontal tangent at equality).
2. If \(h_{\rm inc}<h\le h_{\rm prev}\), incidence has exactly one strict local maximum and exactly one strict local minimum in every transformed orbit period, while infectious prevalence decreases strictly on \([0,\infty)\).
3. If \(h>h_{\rm prev}\), each of incidence and prevalence has exactly one strict local maximum and one strict local minimum in each transformed orbit period.

At every nonzero energy level the transformed orbit is periodic. Hence all asserted positive-peak regimes contain infinitely many strict maxima over the infinite time axis. Successive corresponding incidence and prevalence values shrink by the geometric factor \(e^{-rP(h)}\); there is no persistent positive epidemic intensity. No claim is made about clinical significance or peaks exceeding a fixed prominence threshold.

## Assumptions and scope

The deterministic closed SIR equations are
\[
 \dot S=-\beta(t)SI/N,\qquad
 \dot I=\beta(t)SI/N-\gamma I,\qquad
 \dot R=\gamma I,\qquad
 \beta(t)=\beta_0e^{rt}.
\]
Time is continuous, \(N=S+I+R\) is conserved, \(\beta_0,\gamma,N>0\), and this theorem requires \(0<r<\gamma\). Incidence means the instantaneous **flow of new infections** \(c(t)=\beta(t)S(t)I(t)/N\); prevalence means the state variable \(I(t)\). Strict decrease means \(f(t_2)<f(t_1)\) whenever \(t_2>t_1\); it does not require \(\dot f<0\) at every isolated tangency. A full orbit period refers to the period of the scaled variables, not to a period of incidence or prevalence itself.

## Proof

**1. Conservation and periodicity of scaled contact states.** Define \(X=\beta S/N\) and \(Y=\beta I/N\). Direct differentiation gives exactly
\[
 \dot X=X(r-Y),\qquad \dot Y=Y(X-a),\qquad a=\gamma-r.
\]
The derivative of \(\Phi\) along this vector field vanishes:
\[
 \dot\Phi=(1-a/X)X(r-Y)+(1-r/Y)Y(X-a)
          =(X-a)(r-Y)+(Y-r)(X-a)=0.
\]
Moreover \(\Phi\) is strictly convex with Hessian \(\operatorname{diag}(a/X^2,r/Y^2)\), tends to infinity at each boundary of the positive quadrant, and has its unique minimum \(0\) at \((a,r)\). Thus every positive level \(\Phi=h>0\) is a compact smooth strictly convex simple closed curve enclosing \((a,r)\). The vector field has no stationary point on such a level. Its trajectory traverses that curve periodically with some \(P(h)>0\). The zero level is the equilibrium \((a,r)\).

The actual epidemiological observables are
\[
 I(t)=\frac{N}{\beta_0}e^{-rt}Y(t),\qquad
 c(t)=\frac{N}{\beta_0}e^{-rt}X(t)Y(t).
\]
These formulae imply exponential damping along each period, although \(X,Y\) are periodic.

**2. Sharp onset of incidence oscillation.** Logarithmic differentiation of \(c\) gives
\[
 \frac{\dot c}{c}=\frac{\dot\beta}{\beta}+\frac{\dot S}{S}+\frac{\dot I}{I}
 =r-Y+X-\gamma=X-a-Y.
\]
Thus incidence stationary points on a positive-energy orbit are intersections with the open ray \(Y=X-a>0\), parameterized by \(X=x>a\). Restrict \(\Phi\) to this ray:
\[
 \psi(x)=\Phi(x,x-a),\qquad
 \psi'(x)=2-\frac ax-\frac r{x-a},\qquad
 \psi''(x)=\frac a{x^2}+\frac r{(x-a)^2}>0.
\]
We have \(\psi(x)\to\infty\) as \(x\downarrow a\) and as \(x\to\infty\). Its unique critical point is the larger root of \(2x^2-(3a+r)x+a^2=0\), namely \(x_*\) above; the other algebraic root lies below \(a\). The minimum is \(h_{\rm inc}>0\): the center \((a,r)\) does not lie on the ray.

When \(h<h_{\rm inc}\), the closed level cannot intersect the stationary ray. Since the orbit surrounds the center, where \(X-a-Y=-r<0\), the incidence derivative is strictly negative throughout. At equality, the ray is tangent to the level at precisely \((x_*,y_*)\), so the logarithmic derivative vanishes at one phase but never changes sign: incidence remains strictly decreasing. When \(h>h_{\rm inc}\), strict convexity and endpoint divergence of \(\psi\) give precisely two transverse intersections with the level per orbit; on the arcs between them the logarithmic derivative has alternating signs. There is exactly one strict incidence maximum and one strict incidence minimum per orbit, with no other critical points.

**3. Independent threshold for prevalence.** The other logarithmic derivative is
\[
 \frac{\dot I}{I}=X-\gamma.
\]
A level intersects the vertical line \(X=\gamma\) only when \(h\) exceeds the minimum of \(Y\mapsto\Phi(\gamma,Y)\), attained uniquely at \(Y=r\) with value \(h_{\rm prev}=\Phi(\gamma,r)\). Below that value \(X<\gamma\) throughout every orbit; at equality the only contact is tangential, with no sign change; above it there are exactly two transverse intersections and therefore exactly one strict prevalence maximum and minimum per orbit. This proves the prevalence classification, including the equality case.

**4. Strict separation of the thresholds and admissibility.** Since \((\gamma,r)=(a+r,r)\) belongs to the incidence-stationary ray, \(h_{\rm inc}\le h_{\rm prev}\). Strictness follows because the derivative of \(\psi\) at \(x=\gamma\) is \(\psi'(\gamma)=r/(a+r)>0\), so \((\gamma,r)\) is not its minimizer. Any desired positive energy can be realized by positive \(X_0,Y_0\) on the corresponding level, followed by a sufficiently large choice \(\beta_0\ge X_0+Y_0\) and \(S_0=NX_0/\beta_0\), \(I_0=NY_0/\beta_0\), \(R_0=N-S_0-I_0\ge0\). Hence the intermediate regime is nonempty for physical epidemics. Combining steps 1–4 proves the claim. \(\square\)

## Verification

An exact reproducibility checker `verify.py` symbolically reconstructs the two transformed derivatives, the first-integral identity, the stationary-ray quadratic, and the strict threshold inequality. It then integrates a physical example and verifies multiple incidence maxima but strictly decreasing prevalence in sampled output; finite numerical sampling is supplementary, not proof.

For \(N=1\), \(r=1\), \(\gamma=2\), \(\beta_0=4\), take \((S_0,I_0,R_0)=(19/40,1/4,11/40)\), giving \((X_0,Y_0)=(19/10,1)\). Here
\[
 h=\frac9{10}-\log(19/10),\quad
 h_{\rm inc}\approx0.2259871559<h\approx0.2581461138
 <h_{\rm prev}=1-\log2\approx0.3068528194.
\]
Therefore the theorem proves infinitely many incidence peaks even though \(I(t)\) strictly decreases, without relying on the numerical verifier.

## Relationship to prior work

Rabajante (2026) establishes general SIR incidence/prevalence peak-crossing conditions for arbitrary time-varying transmission and develops a knot-based peak-complexity framework. In particular, its incidence identity supplies the necessary stationary-ray equation after substituting exponential transmission; it does **not** give the sharp global energy minimum on that ray, the distinct prevalence energy threshold, or the resulting exact incidence-only oscillation window. These identities are explicitly treated as prior inputs, not new discoveries.

Maheshwari, Shetty, Bannur and Merugu (2020/2021) derive a Lotka–Volterra representation for a different SIR **feedback-control** transmission policy, using susceptible contacts and infectious prevalence as predator–prey variables. Its periodic active-infection result does not imply the classification here for externally fixed exponential transmission and exponentially decaying prevalence. Classical Lotka–Volterra periodicity and convexity facts are likewise acknowledged as established; the contribution here is the comparison between the two distinct *observable-specific* thresholds for the fixed exponential-transmission SIR family.

## Limitations

The exponential transmission path is unbounded and may be epidemiologically unrealistic over long horizons. All infinitely many strict oscillations shrink geometrically and eventually fall below any fixed absolute reporting or prominence threshold; this theorem is not a prediction of infinitely many detectable outbreaks. The model excludes replenishment of susceptible individuals, changes in removal rate, spatial mixing, and stochastic extinction. The claim does not establish statistical identifiability of exponential forcing. Although the closest available full text and indexed prior models were checked, a previously unknown analytic treatment of the exact observable thresholds could subsume this calculation. Independent mathematical audit has not been performed.

## References

1. J. F. Rabajante, *How Simple Models Can Reproduce Multiple Epidemic Waves: Peak Topology, Minimal Dynamic Complexity, and Inference for Time-Varying Transmission*, arXiv:2610.05556v1 (first public October 4, 2026), https://arxiv.org/abs/2610.05556.
2. H. Maheshwari, S. Shetty, N. Bannur, S. Merugu, *CoSIR: Optimal control of SIR epidemic dynamics by mapping to Lotka-Volterra System*, medRxiv doi:10.1101/2020.11.10.20211995 (2020 preprint; updated 2021), https://doi.org/10.1101/2020.11.10.20211995.
3. A. J. Lotka, *Elements of Physical Biology* (1925); V. Volterra, *Variazioni e fluttuazioni del numero d'individui in specie animali conviventi* (1926): standard conservative predator–prey dynamics.
