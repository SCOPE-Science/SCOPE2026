# Hidden propulsion transition in a historical-velocity-reset active walker

## Finding
Consider the one-dimensional active walker of Boyer and Majumdar [1] with signed velocity \(v\sigma_t\), where \(v,\gamma,r>0\). Intrinsic Poisson tumbling of rate \(\gamma\) reverses \(\sigma_t\in\{-1,1\}\); at an independent Poisson event of rate \(r\), the walker copies **both** the position and velocity sign it held at a time sampled uniformly from \([0,t]\). Start with an unbiased sign and position zero. The *cumulative signed propulsion* is the continuously accumulated quantity
\[
Y_t=v\int_0^t\sigma_s\,ds,
\]
not the physical position \(X_t\), which jumps at relocation events. Put \(B(t)=\operatorname{Var}(Y_t)/v^2\), \(\lambda=2\gamma+r\), and \(\nu=2r/\lambda\in(0,2)\).

For every \(t>0\) and \(r\ne2\gamma\), its exact finite-time mean square is
\[
\boxed{B(t)=\frac{2t}{2\gamma-r}\left[1-{}_1F_1\!\left(1-\nu;2;-\lambda t\right)\right].}
\]
At the critical rate \(r=2\gamma\), the removable limit is
\[
\boxed{B(t)=\frac{t}{2\gamma}\left[\log(4\gamma t)+\gamma_E-1+E_1(4\gamma t)+\frac{1-e^{-4\gamma t}}{4\gamma t}\right].}
\]
Here \({}_1F_1\) is the confluent hypergeometric function, \(E_1(z)=\int_z^\infty e^{-u}du/u\), and \(\gamma_E\) is Euler's constant. The sharp mean-square regimes are
\[
B(t)\sim\begin{cases}
\dfrac{2t}{2\gamma-r},&0<r<2\gamma,\\[4pt]
\dfrac{t\log(4\gamma t)}{2\gamma},&r=2\gamma,\\[4pt]
\dfrac{2\lambda^{\nu-1}}{(r-2\gamma)\Gamma(1+\nu)}\,t^{\nu},&r>2\gamma.
\end{cases}
\]
Thus copying historical orientation changes *unwrapped signed propulsion* from diffusive variance to critical \(t\log t\) growth and then genuinely superlinear variance at exactly \(r=2\gamma\), despite the physical resetting position having logarithmic variance in [1]. These claims concern only second moments, not a central limit theorem or a limiting distribution.

## Assumptions and scope
All parameters \(v,\gamma,r\) are fixed and strictly positive. Poisson clocks and uniform sampling at each relocation are independent of previous random draws conditional on the recorded path. Ties among event times have probability zero. The initial velocity sign has probabilities \(1/2,1/2\); sign symmetry makes \(\mathbb E Y_t=0\). Since there are finitely many events on bounded time intervals and \(|Y_t|\le vt\), all expectations below are finite. The physical path decomposes exactly as \(X_t=Y_t+\sum_{\tau_j\le t}(X_{U_j}-X_{\tau_j-})\), emphasizing that no equality between \(X_t\) and \(Y_t\) is asserted after a relocation.

## Proof
Set \(A_t=Y_t/v=\int_0^t\sigma_s\,ds\), \(K(t)=\mathbb E[A_t\sigma_t]\), and \(B(t)=\mathbb E[A_t^2]\). At intrinsic flips \(\sigma\mapsto-\sigma\), giving the contribution \(-2\gamma K\). At a relocation time \(t>0\), \(\sigma_t\mapsto\sigma_U\) with \(U\) uniform on \([0,t]\), while the already accumulated \(A_t\) is unchanged; its drift in \(K\) is consequently
\[
r\left(\mathbb E\left[A_t\frac1t\int_0^t\sigma_s ds\right]-K\right)=r\left(\frac{B(t)}t-K(t)\right).
\]
Between events \(dA_t=\sigma_tdt\) and \(\sigma_t^2=1\). Hence for \(t>0\)
\[
B'(t)=2K(t),\qquad K'(t)=1-(2\gamma+r)K(t)+\frac r tB(t).
\]
The initial conditions are \(B(0)=B'(0)=0\), and the Volterra dynamics select the regular solution. Eliminating \(K\) gives
\[
tB''(t)+\lambda t B'(t)-2r B(t)=2t.
\]
Write \(B(t)=tF(t)\). Then
\[
tF''+(2+\lambda t)F'+(\lambda-2r)F=2,\qquad F(0)=0.
\]
When \(\lambda\ne2r\), \(F_p=2/(\lambda-2r)\) is a particular solution; its regular homogeneous companion is \({}_1F_1(1-2r/\lambda;2;-\lambda t)\), whose value at zero is one. The displayed formula is the unique regular combination with \(F(0)=0\). When \(\lambda=2r\), integrate the first-order equation for \(F'\), obtaining
\[
F'(t)=\frac{2(\lambda t-1+e^{-\lambda t})}{\lambda^2t^2};
\]
integration from zero and \(\lambda=4\gamma\) yield the critical formula.

For \(z\to+\infty\), Kummer's transformation and standard positive-argument asymptotics give
\[
{}_1F_1(1-\nu;2;-z)\sim\frac{z^{\nu-1}}{\Gamma(1+\nu)}.
\]
For \(\nu<1\) this decays and yields the linear regime; for \(\nu>1\) it dominates the constant and yields the superlinear regime, with positive coefficient because \(r-2\gamma>0\). At \(r=2\gamma\), \(E_1(z)=O(e^{-z}/z)\) gives the stated logarithmic regime. A regular Taylor solution has
\[
B(t)=t^2-\frac{2\gamma}{3}t^3+\frac{\gamma(6\gamma+r)}{18}t^4+O(t^5),
\]
which also fixes the initial normalization.

## Verification
The standalone Python program `check_moments.py` implements three separate checks: the hypergeometric formula against numerical integration of the moment ODE; a direct event-driven simulation of uniform-past sign copying against the predicted second moment with standard errors; and large-time leading-coefficient ratios in all three regimes. In the provided run, the exact and ODE results agreed to the displayed nine decimals at parameter triples \((\gamma,r,t)=(1,0.5,5),(1,2,5),(1,5,5),(2,6,3)\). Monte Carlo with 16,000 paths per case was consistent within approximately 1.4 standard errors. Long-time ratios for \((\gamma,r)=(1,0.5),(1,2),(1,4)\), evaluated at \(t=10^{10}\), were about 0.99999935, 1.00000000, and 0.99969587. These computations independently check arithmetic and simulation, but the infinite-time conclusions follow from the analytic proof.

## Relationship to prior work
Boyer and Majumdar [1] formulate exactly this joint historical position-and-velocity copying protocol and determine the one-time physical-position Fourier law and its logarithmic variance. Their displayed one-time analysis does not give the cumulative signed propulsion law here: this is a different path functional, requiring correlations of orientations at distinct times. The Kummer function also appears in their one-time calculation, but their position-variance law is not the equation for \(\mathbb E[(\int_0^t\sigma_sds)^2]\). Schütz and Trimper [2], and Coletti, Gava and Schütz [3], establish an analogous diffusive/critical/superdiffusive trichotomy for the **discrete-step** elephant walk. Their steps copy or reverse uniformly selected previous *increments* and do not coincide with the continuous-time model with separate Poisson flip/copy clocks and duration-weighted past sampling. Thus the critical exponent pattern is antecedent, whereas the present continuous-time finite-time formula, threshold in physical rates, and coefficients are not supplied by those results. These comparisons do not amount to a claim of exhaustive bibliographic novelty.

## Limitations
The theorem gives second moments only. It does not establish a central limit theorem, tightness of rescaled paths, higher moment asymptotics, or independence of trajectory correlations. The cumulative signed propulsion is not the relocated position; treating the latter as the integral would be incorrect. Analogous moment formulas might occur in less easily indexed reinforced-telegraph literature; this is the principal remaining literature risk. The derivation and supporting computational tests are not independent external validation.

## References
[1] D. Boyer and S. N. Majumdar, *Active particle in one dimension subjected to resetting with memory*, arXiv:2312.13439, first publicly posted 2023-12-20, https://arxiv.org/abs/2312.13439 .

[2] G. M. Schütz and S. Trimper, *Elephants can always remember: Exact long-range memory effects in a non-Markovian random walk*, Phys. Rev. E 70 (2004) 045101, arXiv:cond-mat/0406593, https://arxiv.org/abs/cond-mat/0406593 .

[3] C. F. Coletti, R. Gava and G. M. Schütz, *Central limit theorem for the elephant random walk*, J. Math. Phys. 58 (2017) 053303, arXiv:1608.01662, https://arxiv.org/abs/1608.01662 .
