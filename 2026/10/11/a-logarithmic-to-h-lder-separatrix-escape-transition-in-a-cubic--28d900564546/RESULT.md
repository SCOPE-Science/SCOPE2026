# A logarithmic-to-Hölder separatrix escape transition in a cubic Darboux flow
## Finding
For the cubic polynomial flow
\[
\dot x=x-x^2y+pxy^2+y^3,\qquad \dot y=y+py^3,
\]
with real parameter \(p\), fix \(b>0\) and initial conditions \((x(0),y(0))=(-(1+\varepsilon)b,b)\), where \(\varepsilon>0\). Put \(K=(2+\varepsilon)/\varepsilon\). The first forward singularity always occurs at a finite time \(T_p(\varepsilon;b)\), given in **original physical time** by
\[
T_p(\varepsilon;b)=
\begin{cases}
\frac12\log\!\left(1+\frac{1-K^{-p}}{pb^2}\right),&p\ne0,\\[3pt]
\frac12\log\!\left(1+\frac{\log K}{b^2}\right),&p=0.
\end{cases}
\]
For fixed \(\varepsilon>0\), \(y(t)\) has a strictly positive, finite limit \(Y=y(T_p)\), with
\[
Y^2=\begin{cases}(b^2+p^{-1})K^p-p^{-1},&p\ne0,\\ b^2+\log K,&p=0,\end{cases}
\qquad x(t)\sim-\frac{1}{Y(T_p-t)}\quad(t\uparrow T_p).
\]
The time-to-escape has a sharp, parameter-dependent singular transition as the initial point approaches the invariant line \(x=-y\) from its escaping side:
\[
\begin{array}{ll}
p<0:&T_p=\frac{-p}{2}\log\frac{2}{\varepsilon}-\frac12\log((-p)b^2)+o(1),\\
p=0:&T_0=\frac12\log\log\frac{2}{\varepsilon}-\log b+o(1),\\
p>0:&t_b-T_p\sim \frac{2^{-p-1}}{1+pb^2}\varepsilon^p,
\quad t_b=\frac12\log\!\left(1+\frac1{pb^2}\right).
\end{array}
\]
Thus the approach produces logarithmic delay, double-logarithmic delay, or a finite limit with a fractional power cusp, respectively. The one-sided extension \(T_p(0;b)=t_b\) is analytic in \(\varepsilon\) when \(p\) is a positive integer, and is exactly \(C^{\lfloor p\rfloor}\) but not \(C^{\lceil p\rceil}\) at zero when \(p>0\) is not an integer.

These three regimes admit a **uniform critical crossover**. As \(\varepsilon\downarrow0\), write \(\ell=\log K\) and allow \(p=\delta/\ell\), with \(\delta\) in any fixed compact real interval. Define the positive continuous function \(F(\delta)=(1-e^{-\delta})/\delta\) for \(\delta\ne0\), \(F(0)=1\). Then, uniformly in that interval,
\[
T_{\delta/\ell}(\varepsilon;b)=\frac12\log\ell-\log b+\frac12\log F(\delta)+O(\ell^{-1}).
\]
Finally, on the exact separating trajectory \(x=-y\), the dynamics are global for \(p\le0\), but for \(p>0\) they terminate at \(t_b\) with the different singularity \(x(t)=-y(t)\sim-[2p(t_b-t)]^{-1/2}\). The escaping side always has the order-one pole above, so the normal blow-up exponent changes at the separatrix.

## Assumptions and scope
All statements concern the autonomous real ODE with ordinary physical time \(t\), real \(p\), \(b>0\), and \(\varepsilon>0\). The singular time is the maximal forward existence time of the classical solution. The symbols \(\sim\) and \(o(1)\) refer to the specifically stated one-variable limits, with \(b,p\) fixed unless a joint limit is explicitly given. The crossover error is uniform for \(\delta\) in each compact real interval, with \(b\) fixed. No claim is made about complex trajectories, arbitrary perturbations, or asymptotics uniform over all \(p\in\mathbb R\).

For completeness, with the same fixed \(y(0)=b>0\), initial data \(x(0)<-b\) exhibit finite-time \(x\)-escape for every \(p\); initial data \(x(0)\ge-b\) are forward complete when \(p\le0\), whereas when \(p>0\) they reach their first singularity at \(t_b\) through divergence of \(y\). This is an exact initial-data threshold, not a perturbative linearization.

## Proof
**1. Reduction and exact clock.** Since \(y(0)=b>0\), the scalar equation \(\dot y=y(1+py^2)\) preserves positivity until its maximal time. Put \(r=x/y\); direct differentiation and cancellation give
\[
\dot r=\frac{\dot x y-x\dot y}{y^2}=y^2(1-r^2).
\]
Set \(I(t)=\int_0^t y(s)^2\,ds\). Solving the scalar equation gives
\[
y(t)^2=\frac{b^2e^{2t}}{1-pb^2(e^{2t}-1)},\qquad
I(t)=\begin{cases}
-\frac{1}{2p}\log[1-pb^2(e^{2t}-1)],&p\ne0,\\
\frac{b^2}{2}(e^{2t}-1),&p=0.
\end{cases}
\]
For \(p>0\), the scalar existence endpoint is \(t_b\) as in the statement; for \(p\le0\) it is infinity. In all cases \(I\) increases strictly from zero to infinity on its scalar interval.

For \(r(0)=-1-\varepsilon\), separation yields
\[
\frac{r(t)-1}{r(t)+1}=K e^{-2I(t)},\qquad
r(t)=\frac{1+K e^{-2I(t)}}{1-K e^{-2I(t)}}.
\]
Because \(K>1\), there is one and only one time before the scalar endpoint when the denominator vanishes, namely \(I(T_p)=\frac12\log K\). Solving this equality with the formula for \(I\) yields the two exact expressions for \(T_p\). For all real nonzero \(p\), the logarithm's argument is strictly greater than one; hence \(0<T_p<t_b\) if \(p>0\), and \(T_p<\infty\) if \(p\le0\). The scalar solution is finite there. Substitution into its square gives the asserted formula for \(Y\), which is positive (this positivity also follows directly from the scalar solution).

Since \(I'(T_p)=Y^2>0\), the denominator \(1-Ke^{-2I(t)}\) is \(-2Y^2(T_p-t)+o(T_p-t)\) as \(t\uparrow T_p\), while its numerator tends to 2. Thus \(r(t)\sim-1/[Y^2(T_p-t)]\) and \(x=yr\sim-1/[Y(T_p-t)]\). Standard local existence for polynomial vector fields excludes an earlier singularity because both \(y\) and \(r\) are finite on each compact interval before \(T_p\).

**2. Singular asymptotics.** For \(p<0\), the identity \(K^{-p}\to\infty\) and the exact clock give
\[
2T_p=(-p)\log K-\log((-p)b^2)+o(1).
\]
For \(p=0\), \(2T_0=\log\log K-2\log b+o(1)\). Since \(\log K=\log(2/\varepsilon)+o(1)\), these are the first two expansions stated. For \(p>0\), elementary rearrangement yields the **exact gap**
\[
t_b-T_p=-\frac12\log\left(1-\frac{K^{-p}}{1+pb^2}\right).
\]
Taylor expansion and \(K^{-p}=(\varepsilon/(2+\varepsilon))^p\) prove the positive-parameter constant and the regularity assertion. To verify sharp noninteger regularity, use the positive analytic factor \((2+\varepsilon)^{-p}/(1+pb^2)\) and the nonzero leading coefficient of \(\varepsilon^p\); all lower-order analytic terms vanish in the gap. For integer \(p>0\), the exact gap is analytic near zero.

**3. Uniform crossover.** Setting \(\ell=\log K\), \(p=\delta/\ell\) directly in the exact clock, including its continuous extension at \(\delta=0\), yields the identity
\[
T_p=\frac12\log\left(1+\frac{\ell}{b^2}F(\delta)\right).
\]
On every compact set of \(\delta\), \(F\) has a strictly positive lower bound and a finite upper bound. Factoring \(\ell F(\delta)/b^2\) from the logarithm gives the claimed expansion, with an \(O(\ell^{-1})\) remainder uniformly in that compact set.

**4. Separatrix and threshold.** At \(r(0)=-1\), uniqueness for \(\dot r=y^2(1-r^2)\) forces \(r\equiv-1\); hence \(x=-y\). If \(p>0\), the scalar formula gives \(y(t)\sim[2p(t_b-t)]^{-1/2}\). For \(p\le0\) the scalar solution is global. For \(r(0)>-1\), the scalar-time equation has no pole and \(r(t)\) tends to 1 as \(I\to\infty\); this proves the remaining initial-data dichotomy.

## Verification
The accompanying `check.py` uses symbolic cancellation to confirm the exact ratio equation and arbitrary-precision numerical checks of the clock, endpoint amplitude, fixed-parameter limits and joint critical crossover. With the dependencies in `requirements.txt`, run `python check.py`; its successful diagnostic is `CHECK_OK`. The proof above is analytic and independent of numerical enumeration. For each concrete initial condition, equations in the proof provide a direct reproducible evaluation without numerical ODE integration.

## Relationship to prior work
Volokitin (arXiv:2306.10706v1) introduced precisely this cubic family and established its global phase portraits, invariant lines and Darboux first integrals. Those results are NOT claimed as new. In particular, its line \(x=-y\) and the cases \(p<0\), \(p=0\), \(p>0\) motivate the escape-side comparison. Its theorem concerns phase portraits and integrability, not an original-physical-time formula for the off-line blow-up clock, the sharp one-sided clock regularity or the uniform parameter-distance crossover shown here. The general star-node classification of Alarcón, Castro and Labouriau (arXiv:2106.07516) is at the level of orbital equivalence and does not preserve original flight times. Their contracting-homogeneity result (arXiv:2307.16020) assumes strict contraction of the homogeneous field in every direction; this cubic field vanishes along \(y=0\), so its theorem is not a stronger covering case. Earlier Volokitin–Cheresiz qualitative classification articles were identified bibliographically; their full texts could not be compared.

## Limitations
The theorem addresses a specifically integrable cubic family and its natural invariant line; it does not establish corresponding scaling laws under generic perturbations. The proof yields only the stated compact-\(\delta\) uniform crossover, not uniformity for unbounded \(\delta\). Prior textual comparisons cannot guarantee absolute publication priority. Numerical checker outputs are finite diagnostics, not independent mathematical verification or certificates.

## References
1. E. P. Volokitin, *The cubic Darboux systems with a non-elementary singular point at the Poincaré equator* (2023), arXiv:2306.10706v1. https://arxiv.org/abs/2306.10706
2. B. Alarcón, S. B. S. D. Castro, I. S. Labouriau, *Qualitative planar dynamics with star nodes and homogeneous nonlinearities: beyond Hilbert's 16th problem* (initial preprint 2021), arXiv:2106.07516. https://arxiv.org/abs/2106.07516
3. B. Alarcón, S. B. S. D. Castro, I. S. Labouriau, *Global planar dynamics with a star node and contracting nonlinearity* (2023), arXiv:2307.16020. https://arxiv.org/abs/2307.16020
4. E. P. Volokitin, V. M. Cheresiz, *Qualitative investigation of plane polynomial Darboux-type systems* (2016), Siberian Electronic Mathematical Reports 13, 1170–1186; DOI:10.17377/semi.2016.13.092.
5. E. P. Volokitin, V. M. Cheresiz, *Dynamics of cubic Darboux systems* (2017), Siberian Electronic Mathematical Reports 14, 889–902; DOI:10.17377/semi.2017.14.075.
