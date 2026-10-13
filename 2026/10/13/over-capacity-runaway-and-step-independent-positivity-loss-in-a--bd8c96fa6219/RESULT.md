# Over-capacity runaway and step-independent positivity loss in a Smith predator–prey model

## Finding

In the published Smith-growth model, the predator carrying-capacity surface is also a qualitative separator. When predator density is above carrying capacity and prey is below the conversion threshold, the continuous model accelerates predator growth instead of suppressing it. Every initial state in the open region below exhibits predator runaway with an exact exponential rate and prey extinction on a faster-than-exponential scale. For the **same** initial state, the paper's forward-Euler model exits the nonnegative ecological state space in finitely many steps, no matter how small the positive time step is.

Specifically, put \(A=r-b\), \(K=k_2\), and
\[
\mathcal W=\{(u,v):0<u<f/e,\quad v>\max\{K,A/a\}\}.
\]
For any continuous solution starting from \((u_0,v_0)\in\mathcal W\), there is a constant \(C(u_0,v_0)>0\) such that
\[
\lim_{t\to\infty}v(t)e^{-cf t/d}=C(u_0,v_0),\qquad
\lim_{t\to\infty}\frac{-\log u(t)}{v(t)}=\frac{ad}{cf}.
\]
For every forward-Euler step \(h>0\), define
\[
\eta=f-eu_0,\quad q=1+hc\eta\frac{v_0-K}{K+dv_0}>1,\quad
T=\max\!\left\{v_0,\frac{A+1/h}{a}\right\}.
\]
Then the first Euler iterate with nonpositive prey density has index at most
\[
N=1+\left\lceil\frac{\log(T/v_0)}{\log q}\right\rceil.
\]
These statements hold for all strictly positive parameters and all initial states in \(\mathcal W\); the step-size conclusion also applies under the motivating paper's \(0<ha<1\) and \(0<hb<1\) restrictions.

## Assumptions and scope

Gao's continuous equations (6), with positive rates \(r,b,k_1,a,K,c,d,e,f\), are
\[
\dot u=u(A-rk_1u-av),\qquad
\dot v=cv\frac{K-v}{K+dv}(eu-f).
\]
Its forward-Euler equations (7), indexed by nonnegative integers, are
\[
\begin{aligned}
u_{n+1}&=u_n[1+h(A-rk_1u_n-av_n)],\\
v_{n+1}&=v_n\left[1+hc\frac{K-v_n}{K+dv_n}(eu_n-f)\right].
\end{aligned}
\]
Here \(K\) is predator carrying capacity, not an imposed hard state constraint. The theorem concerns the open domain \(\mathcal W\), which is nonempty for any positive parameter set; it does **not** claim that all positive solutions leave the nonnegative region. The original paper also considers the parameter conventions \(0<a,b<1\) in continuous time and \(0<ha,hb<1\) in discrete time, and the exact example below satisfies all of these.

## Proof

Let \(g(v)=(v-K)/(K+dv)\) for \(v>K\). It is strictly increasing because
\[
g'(v)=\frac{K(1+d)}{(K+dv)^2}>0,
\qquad 0<g(v)<1/d.
\]
For a continuous solution starting in \(\mathcal W\), we have \(\dot u/u=A-rk_1u-av<0\), whereas \(\dot v/v=c(f-eu)g(v)>0\). Both strict signs persist: decreasing \(u\) stays below \(f/e\); increasing \(v\) stays above \(\max\{K,A/a\}\). With \(\delta=av_0-A>0\) and \(\eta=f-eu_0>0\), comparison gives
\[
0<u(t)\le u_0e^{-\delta t},\qquad
v(t)\ge v_0e^{\theta t},\qquad
\theta=c\eta g(v_0)>0.
\]
Also \(\dot v/v<c f/d\). This upper bound excludes finite-time blow-up; the bounds show that every solution exists globally, \(u(t)\to0\), and \(v(t)\to\infty\).

Writing \(\rho=cf/d\), direct subtraction yields the exact nonnegative rate deficit
\[
\rho-\frac{\dot v}{v}=ce\,u\,g(v)
+\frac{cfK(1+d)}{d(K+dv)}.
\]
Both right-hand terms have finite time integrals by the exponential bounds for \(u\) and \(1/v\). Thus \(\log[v(t)e^{-\rho t}]\) has a finite real limit. Consequently \(v(t)e^{-\rho t}\to C\) for some **strictly positive finite** \(C\). Since \(-\log u(t)\to\infty\), differentiation of its ratio with the increasing function \(v(t)\) gives
\[
\lim_{t\to\infty}\frac{d[-\log u(t)]/dt}{dv(t)/dt}
=\lim_{t\to\infty}\frac{av(t)+rk_1u(t)-A}{cv(t)(f-eu(t))g(v(t))}
=\frac{ad}{cf}.
\]
L'Hôpital's rule proves \(-\log u(t)/v(t)\to ad/(cf)\). This is a superexponential prey-decay law, not a finite-time extinction statement.

Now consider the Euler map from the same state. Suppose for contradiction its prey coordinates remain positive indefinitely. Its prey multiplier is strictly less than one whenever the state lies in \(\mathcal W\), so \(0<u_{n+1}<u_n<f/e\). The predator multiplier is at least
\[
1+hc(f-eu_0)g(v_0)=q>1,
\]
since \(g\) is increasing. Inductively, \(v_n\ge v_0q^n\) and the whole orbit remains in \(\mathcal W\). For \(n=\lceil\log(T/v_0)/\log q\rceil\), one has \(v_n\ge T\), whence
\[
1+h(A-rk_1u_n-av_n)\le1+h(A-av_n)\le0.
\]
This contradicts positivity of \(u_{n+1}\). Therefore the first nonpositive prey iterate occurs by the claimed bound. The argument uses no condition forcing \(h\) to be large.

An exact admissible witness has
\[
(r,b,k_1,a,K,c,d,e,f,h)=
(3/2,1/2,1/2,1/2,3,1,1,1,1,1/4),
\quad (u_0,v_0)=(1/2,4).
\]
Here \(0<a,b<1\), \(ha=hb=1/8\), the first iterates are \((u_1,v_1)=(21/64,57/14)\), and the geometric lower factor is exactly \(q=57/56\). The theorem's explicit bound is \(N=1+\lceil\log(5/2)/\log(57/56)\rceil=53\); direct high-precision simulation first obtains nonpositive prey at index \(16\). The theorem rests on the inequalities proved above, not that finite simulation.

## Verification

Run `python verify.py` with Python 3; it uses only the standard library. It checks the positive rate constraints, exact rational first-step identities, geometric lower factor, and the announced finite-step upper bound, then reports the sample exit index using 65-digit decimal arithmetic. Expected first line: `VERIFY_OK`. The symbolic monotonicity identity and the asymptotic rate-deficit formula are independently derived in the proof above; the script's finite run is not a proof of asymptotic limits or universal finite exit.

## Relationship to prior work

Gao (2026), equations (6)–(7), gives exactly the two vector fields analyzed. Its Sections 2–4 derive equilibrium/local bifurcation criteria and examine trajectories near specific equilibria; they do not derive the open overcapacity runaway wedge, the sharp continuous-time asymptotics, or an all-step failure of positivity for the same initial data. The result is **not** a contradiction to local stability calculations for selected equilibria or finite-time simulations within a restricted domain.

Bai–Zheng–Kang (2024) study a continuous Smith-growth model **with a different additive predation construction and Holling-II term**; their abstract concerns global equilibria, heteroclinic loops and limit cycles, not the Euler equation (7) or the multiplicative sign reversal \((K-v)(eu-f)\). Their full text was not accessible in the consulted source, so broader special-case coverage cannot be excluded by full-text comparison alone. Elsadany et al. (2026) analyze Smith-type **prey** growth with a Monod–Haldane functional response; the ecological mechanism and update law differ.

## Limitations

No ecological realism or empirical validity of above-capacity predator runaway is asserted. The theorem says neither that below-capacity initial states exhibit runaway nor that equilibria calculated in the motivating article are incorrect. Asymptotics are specific to the continuous equations with \(d>0\), and the finite-iterate exit conclusion is specific to the forward-Euler discretization. The discrete model is not continued physically after prey density becomes nonpositive. No global basin classification, stochastic robustness, or comparison with independent software implementations is claimed.

## References

1. De-Bao Gao, *Dynamical Study of a Discrete Predator–Prey Model Incorporating Smith Growth and Linear Functional Response*, Journal of Mathematics (2026), article 9152254, first published 23 August 2026. DOI: https://doi.org/10.1155/jom/9152254.
2. D. Bai, J. Zheng, and Y. Kang, *Global dynamics of a predator-prey model with a Smith growth function and the additive predation in prey*, Discrete and Continuous Dynamical Systems B **29** (2024), 1923–1960. DOI: https://doi.org/10.3934/dcdsb.2023161.
3. A. A. Elsadany, A. Almaslokh, B. Alreshidi, and I. M. E. Abdelstar, *Bifurcation analysis and Control in a Discrete-Time Predator-Prey Model with Smith-Type Growth and Monod-Haldane Response*, International Journal of Analysis and Applications **24** (2026), 165. DOI: https://doi.org/10.28924/2291-8639-24-2026-165.
