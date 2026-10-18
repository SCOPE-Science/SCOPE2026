# Sharp capped-susceptibility epidemic envelopes from two moments

## Finding

**Theorem (sharp attainable epidemic-pressure interval with fixed first two susceptibility moments).** In the heterogeneous-susceptibility SIR fluid-limit model of [1], assume the individual susceptibility \(X\) is supported in \([0,L]\), has mean \(m\) and variance \(v\), where \(0<m<L\) and \(0<v<m(L-m)\). Set
\[
b=m+\frac vm,\qquad c=m-\frac{v}{L-m},
\]
and define the two distinct admissible susceptibility laws
\[
F_{\mathrm{lo}}=\frac{v}{m^2+v}\delta_0+\frac{m^2}{m^2+v}\delta_b,
\qquad
F_{\mathrm{hi}}=\frac{(L-m)^2}{(L-m)^2+v}\delta_c+\frac{v}{(L-m)^2+v}\delta_L.
\]
For every admissible law \(F\), let \(A_F(t)\) be its cumulative infection pressure and \(r_F(t)\) its removed proportion. With common \(s_0>0\), \(i_0>0\), \(r_0\ge0\), \(s_0+i_0+r_0=1\) and common \(\tau,\gamma>0\), the **exact** all-time bounds are
\[
 A_{F_{\mathrm{lo}}}(t)\le A_F(t)\le A_{F_{\mathrm{hi}}}(t),\qquad
 r_{F_{\mathrm{lo}}}(t)\le r_F(t)\le r_{F_{\mathrm{hi}}}(t)
 \quad(t\ge0).
\]
For every \(t>0\), equality at either endpoint holds only for that endpoint susceptibility law. The same conclusions hold at \(t=\infty\); at any prescribed positive finite time, and also at the terminal time, **every value of each closed interval is attained** by a law supported in \([0,L]\) and having exactly the stipulated mean and variance. The endpoint laws are common extremizers simultaneously at all times, not time-dependent optimizing distributions.

The uncertainty interval first opens at fourth order:
\[
 A_{F_{\mathrm{hi}}}(t)-A_{F_{\mathrm{lo}}}(t)
 =\frac{\tau^4s_0 i_0^3}{24}\,
 vL\left(1-\frac{v}{m(L-m)}\right)t^4+O(t^5)
 \quad(t\downarrow0).
\]
The removed-proportion interval has this leading coefficient multiplied by \(\gamma/\tau\). For positive variance, the capped upper endpoint is strictly below the homogeneous, same-mean epidemic at every positive time; as \(L\to\infty\) with \(m,v\) fixed, the capped upper endpoint approaches the homogeneous trajectory and terminal size. This explains why the positive upper improvement needs a finite cap, in light of [2].

## Assumptions and scope

Here \(F\) is an arbitrary Borel probability measure on the full closed interval \([0,L]\), possibly discrete or with a zero-susceptibility atom. The moments are \(\int x\,dF(x)=m\) and \(\int (x-m)^2\,dF(x)=v\). The strict interior variance condition makes \(0<c<m<b<L\), giving strictly positive masses in both endpoint laws. The homogeneous benchmark uses the law \(\delta_m\), which has a different variance and is used only for comparison, never as an admissible positive-variance extremizer.

The deterministic pressure/removed equations inherited from [1] are
\[
 G_F(a)=\int_{[0,L]}e^{-ax}\,dF(x),\quad
 \dot A_F(t)=\tau\{i_0+s_0[1-G_F(A_F(t))]\}-\gamma A_F(t),
 \quad A_F(0)=0,\quad
 r_F(t)=r_0+\frac\gamma\tau A_F(t),\qquad s_F(t)=s_0G_F(A_F(t)).
\]
The final newly infected susceptible proportion is \(s_0-s_F(\infty)=r_F(\infty)-r_0-i_0\). Thus the theorem also supplies its precise attainable bounds, after subtracting the common initial infection \(i_0\).

No population-size-uniform finite stochastic epidemic claim, incidence-peak ordering, infected-proportion ordering, or variation outside the indicated support/moment class is asserted. Degenerate variances \(v=0\) and \(v=m(L-m)\) are outside the nondegenerate theorem; both collapse to unique two-moment laws by direct limiting arguments.

## Proof

**Step 1: admissible endpoint laws and strict Laplace order.** The displayed masses are positive, sum to one, and give exactly the moments \(m\) and \(m^2+v\). Their support nodes are ordered as above. Fix any \(a>0\), and put \(f(x)=e^{-ax}\); then \(f'''(x)=-a^3e^{-ax}<0\). Let \(P_{\mathrm{lo}}\) be the unique quadratic Hermite interpolant of \(f\) with one node at \(0\) and a repeated node at \(b\): \(P_{\mathrm{lo}}(0)=f(0)\), \(P_{\mathrm{lo}}(b)=f(b)\), \(P'_{\mathrm{lo}}(b)=f'(b)\). The Hermite interpolation error at any \(x\in[0,L]\) has the sign of
\[
 f'''(\xi)x(x-b)^2/6\le0,
\]
including when \(x\) lies outside the interpolation nodes; at nodes the error vanishes by continuity. Hence \(f(x)\le P_{\mathrm{lo}}(x)\), with strict inequality away from \(\{0,b\}\). All laws in the moment class integrate any quadratic to the same value. Consequently
\[
 G_F(a)\le\int P_{\mathrm{lo}}\,dF
 =\int P_{\mathrm{lo}}\,dF_{\mathrm{lo}}
 =G_{F_{\mathrm{lo}}}(a),
\]
with equality iff \(F\) is supported on \(\{0,b\}\), hence iff \(F=F_{\mathrm{lo}}\).

Similarly, let \(P_{\mathrm{hi}}\) interpolate \(f\) with a repeated node \(c\) and a single node \(L\). The error now has sign
\[
 f'''(\eta)(x-c)^2(x-L)/6\ge0,
\]
so \(P_{\mathrm{hi}}(x)\le f(x)\) on \([0,L]\), with equality only at \(\{c,L\}\). Integrating gives
\[
 G_{F_{\mathrm{hi}}}(a)\le G_F(a)\le G_{F_{\mathrm{lo}}}(a)
 \qquad(a\ge0).
\]
At every strictly positive argument the inequalities are strict unless the indicated endpoint law is used. This elementary Hermite proof is a specialization of classical fixed-moment extremal principles; the distribution-free lower attack-size comparison is already known in [2].

**Step 2: dynamical transfer, sharpness, complete interval.** For fixed \(F\), the pressure vector field \(H_F(a)=\tau\{i_0+s_0[1-G_F(a)]\}-\gamma a\) is globally Lipschitz on \([0,\infty)\). It has \(H_F(0)=\tau i_0>0\), tends to \(-\infty\), and is strictly concave because
\[
H_F''(a)=-\tau s_0\int x^2e^{-ax}\,dF(x)<0.
\]
It therefore has exactly one positive root \(a_F\), and the solution increases from zero to \(a_F\). The Laplace inequalities imply the pointwise vector-field bounds \(H_{F_{\mathrm{lo}}}\le H_F\le H_{F_{\mathrm{hi}}}\). Scalar ODE comparison proves the pressure ordering at all times. Strict inequalities at every positive pressure give strict comparisons for every positive time and at the equilibrium roots unless \(F\) is the corresponding extremal distribution. The affine identity for \(r_F\) immediately transfers the bounds, and convergence to the roots proves the terminal statement.

For \(0\le\theta\le1\), the mixture \(F_\theta=(1-\theta)F_{\mathrm{lo}}+\theta F_{\mathrm{hi}}\) remains admissible. Its transform and vector field vary continuously with \(\theta\) and strictly monotonically for positive pressure, so \(\theta\mapsto A_{F_\theta}(t)\) is continuous and strictly increasing for every \(t>0\). The unique positive equilibrium also varies continuously and strictly monotonically, by the strict crossing of each vector field. The intermediate-value theorem fills the entire attainable pressure/removed interval at every positive observation time and at infinity.

**Step 3: first nonzero onset separation.** Expanding the scalar vector field at \(a=0\) gives
\[
 H_F(a)=\tau i_0+(\tau s_0m-\gamma)a
 -\frac{\tau s_0(m^2+v)}2 a^2
 +\frac{\tau s_0\mathbb E_F[X^3]}6 a^3+O(a^4).
\]
All admissible laws share the first three resulting Taylor coefficients of the solution \(A_F(t)\); the difference between their fourth Taylor coefficients is \(\tau^4s_0i_0^3\Delta_3/24\), where direct expansion of the two endpoint laws yields
\[
\Delta_3=\mathbb E_{F_{\mathrm{hi}}}[X^3]
 -\mathbb E_{F_{\mathrm{lo}}}[X^3]
 =vL\left(1-\frac{v}{m(L-m)}\right)>0.
\]
Compact support permits all needed Taylor derivatives and a fifth-order remainder, proving the stated asymptotic. Multiplying by \(\gamma/\tau\) handles removed proportion.

**Step 4: why a finite cap matters.** By Jensen, \(G_F(a)>e^{-ma}\) for every \(a>0\) whenever \(v>0\), so the homogeneous law \(\delta_m\) strictly dominates the capped upper endpoint in pressure and eventual removals. For fixed \(m,v\), as \(L\to\infty\), \(c=m-v/(L-m)\to m\), the mass of \(F_{\mathrm{hi}}\) at \(L\) tends to zero, and \(G_{F_{\mathrm{hi}}}(a)\to e^{-ma}\) on every bounded interval. Continuous dependence of the scalar ODE and its strictly crossed positive equilibrium gives convergence to the homogeneous comparison. No uniform strict upper improvement can follow from first two moments alone if the susceptibility cap is dropped, consistent with [2].

## Verification

Run the standalone standard-library checker `python3 verify.py`. It evaluates 27 exact rational pairs of admissible endpoint distributions, checks their first two moments and strictly positive third-moment difference, tests Laplace inequalities for intermediate mixtures, compares five positive-time trajectories using fourth-order Runge–Kutta, and independently brackets positive final-pressure roots. The exact benchmark \(m=1\), \(L=3\), \(v=1\), \(s_0=0.9\), \(i_0=0.1\), \(r_0=0\), \(\tau=3\), \(\gamma=1\) gives terminal removed intervals approximately \([0.531448376117,0.774523533215]\) and early pressure-width coefficient exactly \(729/160000\). The common initial effective reproduction number is \(2.7\). These checks are finite examples; the preceding interpolation and ODE arguments, not numerical experiments, establish the unrestricted theorem.

## Relationship to prior work

[1] establishes the mixed-Sellke fluid-limit equation, arbitrary initial susceptibility laws, and a Jensen-based same-mean homogeneous comparison. [2] had already proved the sharp lower final-size bound from mean and coefficient of variation, identifying precisely the zero-and-positive-atom law \(F_{\mathrm{lo}}\), and proved that no nontrivial improvement of the homogeneous upper bound is possible from two moments **without** a support cap. Those claims are not presented as new. The contribution here is the cap-dependent, attained upper endpoint \(F_{\mathrm{hi}}\), the simultaneous complete all-time identified range in the new initial-infected fluid-limit formulation, and the explicit fourth-order onset gap. The endpoint-distribution construction is consistent with classical Markov–Krein moment extremality [3], which is acknowledged rather than attributed to this result. [4] studies gamma-versus-lognormal distributional misspecification with matched mean and coefficient of variation in a different SEIR setting, without the bounded-support minimax interval derived here.

## Limitations

The assertion is deterministic and applies to susceptibility-only heterogeneity under fixed contact and recovery parameters with a strictly positive initial infectious proportion. It does not cover heterogeneous infectiousness, transmission networks, finite-population stochastic outbreaks, peak incidence or peak prevalence. The known two-moment lower endpoint is prior mathematics. The novel upper endpoint requires a trusted finite cap; if it is an empirical estimate rather than an enforced upper bound, the theorem is not a valid worst-case guarantee. A specialized publication applying the general moment problem to exactly these epidemic trajectories could subsume this contribution; no claim of an exhaustive worldwide novelty proof is made. The positive-variance and nonmaximal-variance boundaries are excluded from the strict theorem, with unique-law limiting interpretations only.

## References

[1] O. Izyumtseva, W. R. KhudaBukhsh, M. G. M. Gomes, G. A. Rempala, *From Individual-Based Stochastic Epidemics to Heterogeneous SIR Equations*, arXiv:2608.22122v1 (22 August 2026), especially Theorem 1, Proposition 3, and Section 4.4. https://arxiv.org/html/2608.22122v1

[2] G. Katriel, *The size of epidemics in populations with heterogeneous susceptibility*, Journal of Mathematical Biology 65 (2012), 237–262, especially Theorems 3 and 6 and discussion following Theorem 6. DOI: 10.1007/s00285-011-0460-2. https://doi.org/10.1007/s00285-011-0460-2

[3] S. Karlin and W. J. Studden, *Tchebycheff Systems: With Applications in Analysis and Statistics*, Interscience (1966); general classical moment extremality. Relevant interpolation inequalities are proved explicitly here.

[4] I. Mohammed, C. Robertson, M. G. M. Gomes, *An exploration into how susceptibility distribution misspecifications impact epidemic forecasting*, arXiv:2606.08693v1 (7 June 2026). https://arxiv.org/abs/2606.08693
