# Interior Chebyshev reflection resonances create unbounded stochastic descent variance

## Finding
For the undamped first-order \(s\)-stage Runge–Kutta–Chebyshev stochastic-descent method, with one fresh equally likely sample selected per outer step and *reused across all internal stages*, two strongly convex scalar quadratic samples can produce unbounded mean-square iterates at interior points of the deterministic Chebyshev stability interval. The mechanism is classified exactly by simultaneous negative Chebyshev extrema. A five-stage example has linearly growing stochastic variance although the corresponding full-gradient iteration is a strict contraction. Its nearby stationary variance has an exact quadratic pole.

In particular, put \(s=5\), \(h=25\), and let the independent equiprobable samples at successive outer steps have gradients \(g_i(x)=\lambda_i(x-c_i)\), where
\[
\lambda_- = \frac{3-\sqrt5}{4},\quad c_-=-1,\qquad
\lambda_+ = \frac{3+\sqrt5}{4},\quad c_+=1.
\]
Both curvatures are positive, and both normalized arguments lie strictly between the Chebyshev stability endpoints. Each sampled five-stage update is nevertheless the exact reflection \(X_{n+1}=-X_n+2c_{\xi_n}\). For \(X_0=0\),
\[
\mathbb E X_n=0,\qquad \operatorname{Var}(X_n)=4n,\qquad
\mathbb E[F(X_n)-F(x_*)]=\frac32n+\frac5{24},
\]
where \(F=(f_-+f_+)/2\) and \(x_*=\sqrt5/3\). In contrast, the deterministic five-stage update using the full gradient has the exact distance multiplier \(61/64\) and converges geometrically to \(x_*\).

For the same sample problem with variable \(h\) sufficiently close to, but different from, \(25\), there is a unique finite-variance invariant distribution \(\pi_h\), and
\[
\lim_{h\to25,\ h\ne25}(h-25)^2\operatorname{Var}_{\pi_h}(X)=100.
\]

## Assumptions and scope
All computations are in exact real arithmetic. Fix an integer \(s\ge2\) and a constant outer step \(h>0\). At each outer step sample independently and uniformly from the two scalar component gradients \(g_i(x)=\lambda_i(x-c_i)\), with \(\lambda_i>0\), and retain that same sample for all \(s\) internal stages. The stage coefficients are those of the *undamped* first-order RKC method (damping parameter \(\epsilon=0\)). Assume \(0<h\lambda_i<2s^2\) for both components; thus no sampled scalar curvature lies outside the open deterministic stability interval. The full objective is \(F=(f_1+f_2)/2\), where \(f_i(x)=\lambda_i(x-c_i)^2/2\); it is strongly convex, and the sampled gradients are unbiased.

Write
\[
r_i(h)=T_s\!\left(1-\frac{h\lambda_i}{s^2}\right),\qquad
q(h)=\frac{r_1(h)^2+r_2(h)^2}{2},
\]
where \(T_s(\cos\theta)=\cos(s\theta)\). For arbitrary distinct centers, the general statements below classify second-moment behavior at *simultaneous* interior extrema; the explicit variance formula and pole use centers \((-1,1)\) and the parameters in the Finding.

## Proof
**Exact affine reduction.** With a fixed component sample \((\lambda,c)\) throughout one outer step, let \(Y_0=x\), \(Y_1=x-(h\lambda/s^2)(x-c)\), and
\[
Y_j=2Y_{j-1}-Y_{j-2}-\frac{2h\lambda}{s^2}(Y_{j-1}-c),\qquad 2\le j\le s.
\]
These are the undamped first-order RKC coefficients. Subtracting \(c\) gives the Chebyshev three-term recurrence, including its two initial conditions. Consequently,
\[
Y_s=c+T_s\!\left(1-\frac{h\lambda}{s^2}\right)(x-c).
\]
Thus the stochastic outer update, exactly rather than asymptotically, is \(X_{n+1}=r_{\xi_n}X_n+(1-r_{\xi_n})c_{\xi_n}\).

**Sharp reflection criterion.** The open stability interval implies \(|r_i|\le1\), so \(q\le1\). Equality holds precisely when both component arguments are Chebyshev extrema, namely when integers \(j_i\in\{1,\dots,s-1\}\) satisfy
\[
h\lambda_i=s^2\left(1-\cos\frac{j_i\pi}{s}\right),\qquad r_i=(-1)^{j_i}.
\]
If at least one \(j_i\) is even, the corresponding outer map is the identity, and any other map is either the identity or a single reflection, so every deterministic-start trajectory has at most two states. If both indices are odd, both maps are reflections. When their centers coincide the orbit still has at most two states. When their centers differ, for independent equiprobable samples and deterministic \(X_0\),
\[
X_n=(-1)^nX_0+2\sum_{k=0}^{n-1}(-1)^{n-1-k}c_{\xi_k},\qquad
\operatorname{Var}(X_n)=n(c_1-c_2)^2.
\]
This is the complete dichotomy at interior simultaneous extrema. Off their intersection, \(q<1\); synchronous coupling satisfies \(\mathbb E|X_n-\widetilde X_n|^2=q^n|X_0-\widetilde X_0|^2\). The affine random series therefore yields a unique invariant law with finite second moment.

**Five-stage instance.** At \(h=25\), the two Chebyshev arguments equal \(\cos(\pi/5)\) and \(\cos(3\pi/5)\), respectively; hence both multipliers equal \(-1\). Both positions are interior because the indices are \(1,3\in\{1,2,3,4\}\). For centers \((-1,1)\), the foregoing variance identity gives \(4n\), and symmetric sampling gives zero mean from \(X_0=0\). The full objective has curvature \(\bar\lambda=3/4\) and minimizer \(x_*=\sqrt5/3\), while the full-gradient Chebyshev argument is \(1-h\bar\lambda/25=1/4\), yielding \(T_5(1/4)=61/64\). Finally \(F(x)-F(x_*)=(3/8)(x-x_*)^2\), which gives the asserted objective expectation.

**Exact stationary variance pole.** Put \(a=r_-(h)\), \(b=r_+(h)\), \(A=1-a\), \(B=1-b\). Whenever \(q=(a^2+b^2)/2<1\), the stationary mean \(m\) and variance \(V\) obey
\[
m=\frac{a-b}{2-a-b},\qquad
V=\frac{4A^2B^2}{(A+B)^2(1-q)}.
\]
Indeed, stationary first moments give the formula for \(m\), and the centered recursion gives \(V=qV+[A^2(-1-m)^2+B^2(1-m)^2]/2\); substitution reduces the numerator to \(4A^2B^2/(A+B)^2\).

Both multipliers are stationary at \(h=25\). Direct differentiation of \(T_5\), or the Chebyshev differential equation, gives the *positive* quadratic coefficients
\[
a=-1+\left(\frac1{50}-\frac{\sqrt5}{125}\right)(h-25)^2+O((h-25)^3),\quad
b=-1+\left(\frac1{50}+\frac{\sqrt5}{125}\right)(h-25)^2+O((h-25)^3).
\]
Their coefficient sum is \(1/25\), hence \(1-q=(h-25)^2/25+O((h-25)^3)\). The numerator of \(V\) tends to \(4\). Therefore \(V\sim100/(h-25)^2\), proving the limit and strict nearby contraction.

## Verification
The standalone `verify.py` (run with `python verify.py`, requiring SymPy) checks the generic five-stage recurrence, both exact Chebyshev reflections, their double contact, the full-gradient multiplier, the full-objective minimizer, all sample paths through eleven steps, the invariant-variance algebra, the exact quadratic coefficients, and nearby numerical values. It produces a PASS count when run. Exhaustive finite-horizon checks corroborate, but do not replace, the analytical all-horizon and asymptotic arguments above.

## Relationship to prior work
Stillfjord and Williamson (2022 preprint, 2023 journal) introduce SRKCD, its same-sample-across-stages formulation and decreasing-step convergence results. Eftekhari, Vandereycken, Vilmart and Zygalakis (2020 online publication) develop deterministic RKCD and Chebyshev stability polynomial theory. The Chebyshev polynomial recurrence, affine stochastic-recursion moment identities and general stochastic stability theory are established techniques, not claimed here as new. The contribution is the precise *joint negative-extremum criterion* for this stochastic optimization map, the algebraic five-stage counterexample in which the full gradient strictly contracts, and its exact near-resonance stationary-variance pole. Some later closely related stochastic stabilized-gradient articles were accessible only through public summaries; their priority relevance remains a risk.

## Limitations
The divergence requires exact undamped Chebyshev extrema, one shared sample within each outer step, fresh independent samples between outer steps, a constant step size, and differing component minimizers. It does not claim divergence for the damped parameters employed in numerical experiments, for sampling afresh within stages, or for the source's diminishing-step convergence theorem. The stationary-variance limit concerns a punctured neighborhood of one exact resonance, not uniform guarantees for general objectives. It does not quantify floating-point robustness; numerical damping can remove the exact degeneracy. Independence of publication priority is not established.

## References
1. T. Stillfjord and M. Williamson, *SRKCD: a stabilized Runge-Kutta method for stochastic optimization*, arXiv:2201.12782 (first posted January 30, 2022), subsequently *Journal of Computational and Applied Mathematics* **417** (2023), 114575, doi:10.1016/j.cam.2022.114575.
2. A. Eftekhari, B. Vandereycken, G. Vilmart and K. C. Zygalakis, *Explicit stabilised gradient descent for faster strongly convex optimisation*, *BIT Numerical Mathematics* **61** (2021), 119–139; first online July 4, 2020, doi:10.1007/s10543-020-00819-y.
3. A. Abdulle and S. Cirilli, *S-ROCK: Chebyshev methods for stiff stochastic differential equations*, *SIAM Journal on Scientific Computing* **30** (2008), 997–1014, doi:10.1137/070679375 (distinct SDE setting).
