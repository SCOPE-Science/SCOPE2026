# Opposite predator-invasion shifts under zero-mean seasonal harvesting

## Finding
Consider the harvested predator–prey model
\[
\dot x=r x(1-x/K)-m p(x)y-h_0-s(t),\qquad
\dot y=y\{C p(x)-d\},\qquad C=cm>0,
\]
with positive \(r,K,m,c,d\) and a positive response \(p\) on the relevant prey-density interval. A nonconstant continuous periodic variation \(s\) with zero time mean changes the transverse predator-invasion threshold of the predator-free periodic orbit even though the mean harvest remains \(h_0\). On the high-density branch, the shift has a universal sign: it is positive for a convex response whose derivative at the static equilibrium is negative (a group-defense regime), and negative for a concave response whose derivative there is positive (an ordinary saturation regime). The assertion holds for every forcing period and every admissible waveform, not merely in a small-amplitude or high-frequency limit.

Specifically, write \(d_s=C\overline{p(x_s)}\) for the predator mortality at which the transverse Floquet multiplier of the forced predator-free orbit equals one and \(d_0=Cp(X_+)\) for the constant-harvest threshold. Define the strictly positive prey variance \(V=\overline{(x_s-\bar x_s)^2}\). Under the assumptions below, with \(\Delta=2X_+-K\):

* If \(p''\geq0\) on the trapping interval and \(p'(X_+)<0\), then
\[
d_s-d_0\geq C[-p'(X_+)]\frac{\Delta-\sqrt{\Delta^2-4V}}2
>\frac{C[-p'(X_+)]}{\Delta}V>0.
\]
* If \(p''\leq0\) on the trapping interval and \(p'(X_+)>0\), then
\[
d_s-d_0\leq-Cp'(X_+)\frac{\Delta-\sqrt{\Delta^2-4V}}2
<-\frac{Cp'(X_+)}{\Delta}V<0.
\]

Consequently, whenever \(d\) lies strictly between \(d_0\) and \(d_s\), the constant-harvest predator-free equilibrium and the forced predator-free periodic solution have **opposite local stability in the predator direction**, despite having identical mean harvesting. The prey direction is attracting in both cases. The result concerns local invasion and does not assert persistence or a positive coexistence cycle.

## Assumptions and scope
Fix \(r,K>0\) and \(0<h_0<rK/4\). Put \(f(x)=rx(1-x/K)\) and let \(X_+\in(K/2,K)\) be its larger solution of \(f(X_+)=h_0\). Take numbers \(K/2<u<X_+<v<K\) and \(\eta>0\) satisfying
\[
f(u)>h_0+\eta,\qquad f(v)<h_0-\eta.
\]
Let \(T>0\) be arbitrary and let \(s:\mathbb R\to\mathbb R\) be continuous, nonconstant, \(T\)-periodic, and satisfy \(\overline s=T^{-1}\int_0^Ts(t)\,dt=0\) and \(\|s\|_\infty<\eta\). Let \(p\in C^2([u,v])\) be strictly positive. Either of the two curvature/slope cases stated above is assumed, independently. One can use \(p(x)=x^2/(a x^2+b x+1)\) with \(a>0\) and positive denominator throughout \([u,v]\); the theorem is not restricted to this rational form.

The predator-free equation \(\dot x=f(x)-h_0-s(t)\) has a unique periodic solution \(x_s(t)\) taking values in \([u,v]\); uniqueness means among solutions wholly contained in that interval. A bar denotes the time average over one full period of this orbit. Write \(\mu=\bar x_s\), \(V=\overline{(x_s-\mu)^2}\), and \(\Delta=2X_+-K>0\).

## Proof
**1. A uniquely attracting high-density periodic prey state.** At \(u\) the time-dependent scalar vector field is strictly positive, and at \(v\) it is strictly negative, so \([u,v]\) is forward invariant. On this interval, \(f'(x)=r(1-2x/K)\le r(1-2u/K)<0\). The period-\(T\) map therefore carries \([u,v]\) into itself and has Lipschitz constant at most \(\exp\{r(1-2u/K)T\}<1\). Its unique fixed point generates \(x_s(t)\). The same contraction proves exponential attraction within the interval. If \(x_s\) were constant, the scalar equation would force \(s\) to be constant; this contradicts the assumptions, so \(V>0\).

**2. Exact mean–variance shell.** Integrate the scalar equation over one period. Since \(\bar s=0\),
\[
r\mu(1-\mu/K)-\frac rK V=h_0=f(X_+).
\]
Because \(\mu\in[u,v]\subset(K/2,K)\) and \(f\) is strictly decreasing there, \(\mu<X_+\). Set \(\delta=X_+-\mu\), which satisfies \(0<\delta<\Delta/2\) because \(\mu>K/2\). Expanding the quadratic identity gives
\[
V=\delta(\Delta-\delta),\qquad
\delta=\frac{\Delta-\sqrt{\Delta^2-4V}}2
=\frac{2V}{\Delta+\sqrt{\Delta^2-4V}}>\frac V\Delta.
\]
The square root is real and the lower branch is fixed by the strict inequality \(\delta<\Delta/2\). No perturbative approximation was used.

**3. Curvature turns the mean deficit into a signed invasion shift.** For convex \(p\), its tangent at \(X_+\) lies below its graph, hence
\[
\overline{p(x_s)}-p(X_+)\ge p'(X_+)(\mu-X_+)=[-p'(X_+)]\delta>0.
\]
For concave \(p\), the tangent lies above its graph, giving
\[
\overline{p(x_s)}-p(X_+)\le-p'(X_+)\delta<0.
\]
Substitute the exact expression for \(\delta\) from step 2 to obtain both strict variance-controlled bounds.

**4. Exact local Floquet interpretation.** At the predator-free periodic orbit \((x_s(t),0)\), the planar variational equation is upper triangular, with diagonal entries \(f'(x_s(t))\) and \(Cp(x_s(t))-d\). Its multipliers are therefore
\[
\rho_x=\exp\left(\int_0^T f'(x_s(t))\,dt\right)\in(0,1),\qquad
\rho_y=\exp\{T(d_s-d)\}.
\]
For constant harvest, replace \(x_s\) by the equilibrium \(X_+\), yielding threshold \(d_0\). Choosing \(d\) strictly between \(d_s\) and \(d_0\) gives opposite signs of the corresponding transverse exponents, while the prey exponents remain strictly negative. This proves the stated local stability reversal. At equality \(d=d_s\) or \(d=d_0\), a transverse multiplier equals one and no nonlinear classification is claimed.

**5. Two concrete, nonempty open response regimes.** Set \(r=1\), \(K=2\), \(h_0=3/8\), \(u=7/5\), \(v=8/5\), \(\eta=1/25\), and \(C=1\). Then \(X_+=3/2\), \(\Delta=1\), \(f(u)-h_0=9/200\), and \(h_0-f(v)=11/200\). Every continuous nonconstant zero-mean periodic \(s\) with \(\|s\|_\infty<1/25\) is admissible.

For strong group defense, choose \(p_g(x)=x^2/((11/10)x^2-2x+1)\), whose denominator is strictly positive everywhere, whose derivative is negative on \([7/5,8/5]\), and whose second derivative is strictly positive there. In fact, writing \(D_g=(11/10)x^2-2x+1\),
\[
p_g''(x)=\frac{2(1+(11/5)x^3-(33/10)x^2)}{D_g(x)^3}>0,
\]
because \(22x^3-33x^2+10\) is increasing for \(x>1\) and equals \(711/125>0\) at \(7/5\). Thus \(p_g(X_+)=90/19\), \(p_g'(X_+)=-2400/361\), and \(d_s-90/19>(2400/361)V\).

For ordinary saturation, choose \(p_m(x)=x^2/(1+x^2)\), strictly increasing and strictly concave on the same interval: \(p_m'(x)=2x/(1+x^2)^2\) and \(p_m''(x)=-2(3x^2-1)/(1+x^2)^3<0\). Here \(p_m(X_+)=9/13\), \(p_m'(X_+)=48/169\), and \(d_s-9/13<-(48/169)V\). The strict inequalities persist for small parameter changes retaining the trapping and curvature assumptions.

## Verification
The self-contained analytical proof above requires no numerical calculation. The included `checks/verify.py` (dependencies listed in `checks/requirements.txt`) checks exact symbolic endpoint identities and response derivatives, then integrates the high-density prey equation for three distinct mean-zero periodic waveforms. In each case it verifies the exact mean–variance identity to numerical tolerance and confirms the opposite strict response-average inequalities. Its output for the first forcing includes \(V\approx0.00036008618\), \(\overline{p_g(x_s)}-p_g(X_+)\approx0.0057611461\), and \(\overline{p_m(x_s)}-p_m(X_+)\approx-0.0001626754\). These finite checks are corroboration, not proof for all forcing waveforms.

To rerun, install the three Python dependencies from the requirements file and execute `python checks/verify.py` from this package's root. The analytic inequalities hold for any \(T>0\), not just the tested \(T=2\pi\).

## Relationship to prior work
Etoua and Rousseau (2010) established the autonomous generalized Gause model and studied its equilibrium and global bifurcation geometry under *constant* prey harvest. El Khateeb, Akter, Kottegoda, and Abou Hasan (2026) examined the negative-denominator-coefficient group-defense regime and constant-harvest bifurcations; their boundary predator-invasion thresholds are equilibrium thresholds. Banerjee and Das (2016) treated seasonal perturbations of prey growth and predator mortality with impulsive interventions in a different two-prey system. Song et al. (2019) considered time-dependent parameters and nonlinear harvesting for a Leslie–Gower predator equation, deriving permanence and existence of periodic coexistence solutions. None of these inspected results states the waveform-uniform *signed difference* between constant-harvest and seasonal-harvest predator-free Floquet thresholds for the present system. The proof combines an exact forced-logistic variance identity with supporting-line inequalities; these component techniques themselves are classical. No general or unconditional historical-priority claim is made.

## Limitations
The theorem assumes a trapping interval strictly above the logistic maximum, bounded seasonal harvest fluctuations, and response curvature and slope of the stated signs. It does not classify larger forcing that leaves the interval, the lower prey branch, non-periodic harvest, mixed-curvature responses, predator persistence away from the boundary, nonlinear neutral cases, or global positive dynamics. A response change between group-defense and ordinary-saturation examples is an explicit comparison of two functional regimes, not an assertion that one biological population switches responses. Source comparisons cannot exclude all unindexed prior results; independent audit has not been performed.

## References
1. W. El Khateeb, F. Akter, C. Kottegoda, and M. M. Abou Hasan, *Dynamics of a Harvested Predator-Prey Model with a Generalized Holling Type III Response Capturing Group Defense*, arXiv:2610.32306v1, first posted 2026-10-23. https://arxiv.org/abs/2610.32306
2. R. M. Etoua and C. Rousseau, *Bifurcation analysis of a generalized Gause model with prey harvesting and a generalized Holling response function of type III*, Journal of Differential Equations 249 (2010), 2316–2356. Author-accessible preprint: https://dms.umontreal.ca/~rousseac/Etoua_Rousseau_eng.pdf ; DOI: 10.1016/j.jde.2010.06.021.
3. C. Banerjee and P. Das, *Impulsive Control on Seasonally Perturbed General Holling Type Two-Prey One-Predator Model*, Discrete Dynamics in Nature and Society (2016), 9268257. https://doi.org/10.1155/2016/9268257
4. J. Song, Y. Xia, Y. Bai, Y. Cai, and D. O'Regan, *A non-autonomous Leslie–Gower model with Holling type IV functional response and harvesting complexity*, Advances in Difference Equations (2019), article 299. https://doi.org/10.1186/s13662-019-2203-4
