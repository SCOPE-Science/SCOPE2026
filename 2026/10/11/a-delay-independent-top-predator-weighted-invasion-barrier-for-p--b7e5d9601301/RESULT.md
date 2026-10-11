# A delay-independent top-predator-weighted invasion barrier for positive cycles
## Finding
Consider the Wang–Shao–Chai delayed three-species food-chain model
\[
\dot x_1(t)=\frac{r x_1(t)}{1+kx_2(t)}-b x_1(t)-a x_1(t)^2-\frac{\alpha x_1(t)x_2(t)}{x_1(t)+m x_2(t)},
\]
\[
\dot x_2(t)=\frac{\beta x_1(t-\tau_1)x_2(t-\tau_1)}{x_1(t-\tau_1)+m x_2(t-\tau_1)}-d x_2(t)-\frac{\theta x_2(t)x_3(t)}{v+p x_2(t)+q x_3(t)},
\]
\[
\dot x_3(t)=\frac{\eta x_2(t-\tau_2)x_3(t-\tau_2)}{v+p x_2(t-\tau_2)+q x_3(t-\tau_2)}-e x_3(t),
\]
with all displayed biological parameters positive and \(\tau_1,\tau_2\ge0\).

Let \((x_1,x_2,x_3)\) be any strictly positive \(T\)-periodic solution. Define the top-predator-weighted mean intermediate-predator density
\[
M_3=\frac{\int_0^T x_2(t)x_3(t)\,dt}{\int_0^T x_3(t)\,dt}.
\]
Then existence of such a positive cycle forces
\[
\eta>pe,
\]
and every such cycle obeys the strict finite-amplitude barrier
\[
\boxed{M_3>\frac{ve}{\eta-pe}}.
\]
If the top-predator gestation delay vanishes, \(\tau_2=0\), then the ordinary time mean satisfies the stronger statement
\[
\boxed{\frac1T\int_0^T x_2(t)\,dt>\frac{ve}{\eta-pe}}.
\]

The threshold is not ad hoc. In the source, the interior equilibrium satisfies
\[
x_3^*=\frac{\eta-pe}{qe}x_2^*-\frac vq,
\]
so a positive interior equilibrium requires \(x_2^*>ve/(\eta-pe)\). The same quantity appears in the source's local top-predator-invasion condition at the top-predator-free equilibrium. The result above therefore extends that local/static threshold to a finite-amplitude constraint on every positive periodic state.

For the source's numerical parameters \(v=3.1\), \(p=1.14\), \(\eta=2.2\), and \(e=0.2\), the barrier is
\[
\frac{ve}{\eta-pe}=\frac{155}{493}=0.3144016227\ldots.
\]

## Assumptions and scope
All biological parameters in the displayed system are positive. The solution is assumed strictly positive and \(T\)-periodic for some \(T>0\). No small-amplitude assumption is made. The weighted bound holds for arbitrary nonnegative delays \(\tau_1\) and \(\tau_2\). The ordinary unweighted mean bound is proved only on the slice \(\tau_2=0\); no unweighted mean claim is made for general positive \(\tau_2\).

The result is conditional on existence of a positive periodic solution. It does not prove that a Hopf branch exists for every parameter set, nor does it establish stability or uniqueness of any cycle. It gives a necessary constraint on any such cycle.

## Proof
Integrate the third equation over one period. Since \(x_2\) and \(x_3\) are \(T\)-periodic, shifting the integration variable by \(\tau_2\) leaves the integral unchanged. Hence
\[
0=\eta\int_0^T\frac{x_2(t)x_3(t)}{v+p x_2(t)+q x_3(t)}\,dt-e\int_0^T x_3(t)\,dt.
\]
Because \(x_3(t)>0\), define the probability measure on one period
\[
d\nu(t)=\frac{x_3(t)\,dt}{\int_0^T x_3(s)\,ds}.
\]
Then
\[
\frac e\eta=\int\frac{x_2}{v+p x_2+q x_3}\,d\nu.
\]
Strict positivity of \(q x_3\) gives
\[
\frac e\eta<\int\frac{x_2}{v+p x_2}\,d\nu.
\]
Set \(f(u)=u/(v+pu)\). For \(u>0\),
\[
f''(u)=-\frac{2pv}{(v+pu)^3}<0,
\]
so \(f\) is strictly concave. Jensen's inequality yields
\[
\frac e\eta<\int f(x_2)\,d\nu\le f\!\left(\int x_2\,d\nu\right)=\frac{M_3}{v+pM_3}.
\]
The right side is strictly below \(1/p\), so necessarily \(e/\eta<1/p\), equivalently \(\eta>pe\). With this positive denominator,
\[
\frac e\eta<\frac{M_3}{v+pM_3}
\]
is algebraically equivalent to
\[
M_3>\frac{ve}{\eta-pe}.
\]

Now assume \(\tau_2=0\). Dividing the third equation by the positive function \(x_3(t)\) gives
\[
\frac{d}{dt}\log x_3(t)=\eta\frac{x_2(t)}{v+p x_2(t)+q x_3(t)}-e.
\]
Its period average is zero, hence
\[
\frac e\eta=\frac1T\int_0^T\frac{x_2(t)}{v+p x_2(t)+q x_3(t)}\,dt.
\]
Repeating the same strict denominator comparison and Jensen argument, now with ordinary normalized time measure, gives
\[
\frac1T\int_0^T x_2(t)\,dt>\frac{ve}{\eta-pe}.
\]
This completes both assertions.

## Verification
The proof is exact and analytic. The packaged checker `verify.py` uses rational arithmetic to verify the algebraic threshold rearrangement and the source's printed numerical specialization. It is not used as a substitute for the period-integral argument.

Two boundary checks are important. First, the strict inequality uses \(q>0\) and \(x_3(t)>0\); if the top predator vanishes, strictness can fail and the claimed positive-cycle setting is lost. Second, for \(\tau_2>0\), the birth term contains \(x_3(t-\tau_2)\) while mortality contains \(x_3(t)\), so dividing by \(x_3(t)\) does not produce the ordinary-time identity. This is why the general-delay theorem uses the weighted mean \(M_3\), and why the ordinary mean statement is restricted to \(\tau_2=0\).

## Relationship to prior work
The 2023 source introduces the displayed delayed model, proves positivity and boundedness, derives the interior-equilibrium relation
\[
x_3^*=\frac{\eta-pe}{qe}x_2^*-\frac vq,
\]
and gives the local top-predator-free stability condition involving \(x_2<ve/(\eta-pe)\). It then studies delay-driven Hopf bifurcations, including the slice \(\tau_2=0\), and numerically exhibits oscillatory states. It does not state an exact finite-amplitude weighted-mean or ordinary-mean barrier for periodic solutions.

Related open literature on tritrophic food chains with gestation delays studies Hopf thresholds, stabilization/destabilization, periodic solutions, and chaos for different functional responses. The inspected related works do not imply the present source-specific weighted identity or its exact alignment with \(ve/(\eta-pe)\). Searches of published mathematical findings for the source title, the threshold, weighted means, and equivalent periodic-orbit formulations likewise returned only results for different systems.

## Limitations
The theorem is only a necessary condition for strictly positive periodic solutions. It does not prove existence, uniqueness, orbital stability, or attraction of a cycle. For \(\tau_2>0\), only the top-predator-weighted mean is controlled; an ordinary unweighted mean lower bound has not been proved here. Analogous weighted-average arguments may exist for other predator-prey systems, so the originality claim is source-specific: the exact statement for this delayed Beddington-DeAngelis food chain and its coincidence with the paper's local invasion threshold.

## References
1. Y. Wang, Y. Shao, and C. Chai, “Dynamics of a predator-prey model with fear effects and gestation delays,” AIMS Mathematics 8 (2023), 7535–7559. DOI: 10.3934/math.2023378. Published 17 January 2023.
2. R. K. Upadhyay, S. Mishra, Y. Dong, and Y. Takeuchi, “Exploring the dynamics of a tritrophic food chain model with multiple gestation periods,” Mathematical Biosciences and Engineering 16 (2019), 4660–4691. DOI: 10.3934/mbe.2019234.
3. S. Vinoth et al., “Dynamical analysis of a delayed food chain model with additive Allee effect,” Advances in Difference Equations (2021), Article 38. DOI: 10.1186/s13662-021-03216-z.
4. D. Jana, R. Agrawal, and R. K. Upadhyay, “Top-predator interference and gestation delay as determinants of the dynamics of a realistic model food chain,” Chaos, Solitons & Fractals 69 (2014), 50–63. DOI: 10.1016/j.chaos.2014.09.001.
