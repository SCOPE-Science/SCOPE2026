# A directional moment-determinacy boundary for shear diffusion under resetting

## Finding

Consider isotropic planar Brownian diffusion in a linear shear, with both coordinates reset to the origin at independent Poisson times. There is an exact dichotomy in the stationary *one-dimensional projection laws*: the direction orthogonal to the shear velocity has a Laplace law and is Hamburger moment-determinate, whereas every direction with a nonzero component along the shear is Hamburger moment-indeterminate when the shear is nonzero. The latter laws have a sharp, parameter-dependent stretched-exponential density asymptotic, including the complete leading prefactor.

For a unit direction \((u,v)\), write \(Z=uX+vY\) for the stationary projection. For \(\gamma u\ne0\), put
\[
\ell=\left(\frac{9}{4D\gamma^2u^2r}\right)^{1/4},\qquad
B=\frac{4r\ell}{3},\qquad
K=\frac{\sqrt r}{2\ell\sqrt{2D\gamma^2u^2/3}}\exp\left(\frac{rv}{\gamma u}\right).
\]
Then the strictly positive even density \(f_{u,v}\) of \(Z\) satisfies
\[
f_{u,v}(z)\sim K|z|^{-1/2}\exp(-B\sqrt{|z|})\qquad (|z|\to\infty).
\]
All absolute moments exist, but the law is *not* uniquely determined by its complete sequence of moments. If \(\gamma u=0\), instead,
\[
f_{u,v}(z)=\frac12\sqrt{\frac rD}\exp\left(-|z|\sqrt{\frac rD}\right),
\]
which has a finite moment-generating function in a neighborhood of zero and is therefore Hamburger moment-determinate. For fixed nonzero \(\gamma\), the only determinate unit projection directions are \((u,v)=(0,\pm1)\).

## Assumptions and scope

Fix arbitrary \(D>0\), \(r>0\), and real shear rate \(\gamma\). Between Poisson resets of rate \(r\), start both coordinates at zero and solve
\[
dX_t=\gamma Y_t\,dt+\sqrt{2D}\,dW_t^{(1)},\qquad
dY_t=\sqrt{2D}\,dW_t^{(2)},
\]
where the two Brownian motions and the Poisson process are independent. At each reset both coordinates are simultaneously set to \((0,0)\); the dynamics resume with independent Brownian increments. The stationary law exists uniquely by regeneration. The coordinates \((X,Y)\) and the projection \(Z=uX+vY\) always refer to that stationary law, with \(u^2+v^2=1\). This theorem is about full resets and does not cover the different operation of resetting only the horizontal coordinate.

## Proof

**1. Exact stationary Gaussian mixture.** The elapsed time \(T\) since the last reset in stationarity is exponential of rate \(r\), independent of the Brownian increments in that renewal cycle. For a cycle of age \(t\), stochastic Fubini gives
\[
X_t=\sqrt{2D}\left(W_t^{(1)}+\gamma\int_0^t(t-s)\,dW_s^{(2)}\right),\qquad
Y_t=\sqrt{2D}\,W_t^{(2)}.
\]
Thus \(Z\) conditional on \(T=t\) is centered Gaussian with variance
\[
V(t)=2D\left[t+\gamma uv\,t^2+\frac{\gamma^2u^2}{3}t^3\right],
\]
where the coefficient of \(t\) uses the unit-direction normalization. It is positive for every \(t>0\), since
\[
V(t)=2D\int_0^t\left[u^2+\bigl(v+\gamma u(t-s)\bigr)^2\right]ds.
\]
The stationary projection density is the exact normalized mixture
\[
f_{u,v}(z)=r\int_0^\infty\frac{\exp\left[-rt-z^2/(2V(t))\right]}{\sqrt{2\pi V(t)}}\,dt.
\]
Positivity and evenness are immediate. Continuity and finiteness follow from \(V(t)\sim2Dt\) near zero and the exponential age factor for large \(t\). In particular \(f_{u,v}(0)>0\).

**2. The exceptional Laplace case.** If \(\gamma u=0\), then \(V(t)=2Dt\). The elementary inverse-Gaussian-type integral
\[
r\int_0^\infty(4\pi Dt)^{-1/2}\exp\left(-rt-\frac{z^2}{4Dt}\right)dt
=\frac12\sqrt{\frac rD}\,e^{-|z|\sqrt{r/D}}
\]
yields the claimed Laplace density. Its moment-generating function equals \(r/(r-D\theta^2)\) for \(|\theta|<\sqrt{r/D}\). Uniqueness of a law possessing a moment-generating function near zero proves Hamburger determinacy.

**3. Sharp tails for every shear-sensitive direction.** Assume \(\gamma u\ne0\), and abbreviate
\[
c_3=\frac{2D\gamma^2u^2}{3}>0,\qquad c_2=2D\gamma uv,\qquad c_1=2D,
\]
so \(V(t)=c_3t^3+c_2t^2+c_1t\). Write \(q=|z|\), \(a=\ell\sqrt q\), \(t=as\), and \(\Lambda=ra\). The choice of \(\ell\) makes \(q^2/(2c_3a^3)=\Lambda/3\). Uniformly on every compact interval of \(0<s<\infty\), expansion of the exact exponent gives
\[
rt+\frac{q^2}{2V(t)}
=\Lambda\left(s+\frac{1}{3s^3}\right)
-\frac{rc_2}{3c_3s^4}+O(\Lambda^{-1}),
\]
and \(V(as)^{-1/2}=(c_3a^3s^3)^{-1/2}(1+O(a^{-1}))\). The leading action \(F(s)=s+1/(3s^3)\) has its unique minimum at \(s=1\), with \(F(1)=4/3\) and \(F''(1)=4\). Laplace's method therefore gives
\[
\begin{aligned}
f_{u,v}(q)
&\sim\frac{ra}{\sqrt{2\pi c_3a^3}}
 e^{rc_2/(3c_3)}e^{-4\Lambda/3}
\sqrt{\frac{2\pi}{4\Lambda}}\\
&=\frac{\sqrt r}{2\sqrt{c_3}\,a}
 e^{rc_2/(3c_3)}e^{-4ra/3}.
\end{aligned}
\]
The compact-saddle calculation controls the full integral rigorously. Choose a fixed large \(t_0\) so that \(V(t)\le(1+\varepsilon)c_3t^3\) for all \(t\ge t_0\). On \(t_0\le t\le\delta a\), the displacement action satisfies \(q^2/(2V(t))\ge\Lambda/[3(1+\varepsilon)\delta^3]\), which exceeds the saddle action by a fixed positive fraction of \(\Lambda\) if \(\delta>0\) is small. On \(0<t<t_0\), the same action is at least \(q^2/[2\max_{0\le t\le t_0}V(t)]\), of higher order than \(\Lambda\). On \(t\ge Ra\), the age factor has action at least \(R\Lambda\), which exceeds \(4\Lambda/3\) for \(R>4/3\). On the remaining compact interval \(\delta\le s\le R\), excluding any fixed neighborhood of \(s=1\), the action \(F(s)\) exceeds its unique minimum. Polynomial prefactors cannot overcome these exponential separations. Since \(c_2/(3c_3)=v/(\gamma u)\), substituting \(a=\ell\sqrt q\) proves exactly the displayed \(K\), \(B\) and power \(q^{-1/2}\). Symmetry covers negative \(z\).

**4. Moment classification and exponential-moment boundary.** For every \(k>0\), the Gaussian absolute-moment formula and polynomial growth \(V(t)=O(1+t^3)\) imply
\[
\mathbb E|Z|^k=C_k\,\mathbb E[V(T)^{k/2}]<\infty.
\]
If \(\gamma u\ne0\), conditional Gaussian integration shows for each \(\theta\ne0\)
\[
\mathbb E[e^{\theta Z}]
=r\int_0^\infty\exp\left(-rt+\frac{\theta^2V(t)}2\right)dt=\infty,
\]
as the positive cubic term dominates. The positive continuous density has \(-\log f(z)=B\sqrt{|z|}+\tfrac12\log|z|-\log K+o(1)\) as \(|z|\to\infty\). Consequently its Hamburger Krein logarithmic integral satisfies
\[
\int_{-\infty}^{\infty}\frac{-\log f_{u,v}(z)}{1+z^2}\,dz<\infty.
\]
The integral is finite on compact sets by positivity and continuity, and in both tails because \(\sqrt{|z|}/z^2\) is integrable. Krein's sufficient criterion for Hamburger indeterminacy (as stated in Lin, 2017) now implies that infinitely many distinct distributions share all the moments of this projection. Together with step 2 this proves the exact directional dichotomy.

## Verification

A standalone script, `check.py`, reproduces the exact variance polynomial, integrates the positive stationary Gaussian mixture by quadrature, and independently evaluates the saddle-point constants. Across nine parameter/direction combinations and three displacement scales each, its density/asymptotic ratios approach unity; it also tests independent horizontal and vertical moment identities. Executing `python check.py` using NumPy and SciPy yields `PASS 31 numeric and exact moment checks`. These computations check the analytic formulas in finite examples; the infinite claims follow from the above proof, not from numerical limits.

## Relationship to prior work

Abdoli, Olsen and Löwen (arXiv:2410.10333v1) introduced this shear-diffusion/reset model, derived the Gaussian propagator and last-reset stationary mixture, and studied stationary moments, anisotropy, skewness, energetic cost, and partial-reset nonstationarity. The present contribution is the all-direction sharp asymptotic, its shear-tilt prefactor, and the *complete directional moment-(in)determinacy classification*. The source's reference to especially heavy tails concerns a distinct partial-reset, nonstationary experiment rather than this full-reset projection theorem.

Santra, Basu and Sabhapandit (arXiv:2205.00549v1) found a square-root stretched-exponential stationary tail in a distinct Brownian model with a stochastic diffusion coefficient that resets along with position. Thus a half-power exponent is not asserted to be new in stochastic resetting generally; their stochastic-diffusivity process does not imply the present shear-dependent directional constants or axis-specific determinacy boundary. Lin (2017), and Lin and Stoyanov (arXiv:1406.1654), provide general established criteria and product examples for moment indeterminacy, which are applied rather than reinvented here.

## Limitations

The formula assumes Gaussian isotropic diffusion, a linear shear, full simultaneous Poisson resets to a fixed origin, and stationary observation. It does not concern coordinate-wise partial resetting, nonlinear flow, correlated noises, non-Poisson renewal tails, or a multidimensional moment problem for the *joint* stationary law. For \(\gamma u\ne0\), lack of a moment-generating function alone does not prove indeterminacy; the separate Krein-integral argument is essential. The derived asymptotic is for each fixed direction and nonzero effective shear, without uniformity as \(\gamma u\to0\). The transition at zero effective shear is a tail/moment-property distinction, not a thermodynamic phase transition.

## References

1. I. Abdoli, K. S. Olsen, and H. Löwen, *Shear-Driven Diffusion with Stochastic Resetting*, arXiv:2410.10333v1, publicly posted 14 October 2024. https://arxiv.org/html/2410.10333v1
2. I. Santra, U. Basu, and S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient*, arXiv:2205.00549v1 (2022). https://arxiv.org/html/2205.00549v1
3. G. D. Lin, *Recent developments on the moment problem*, Journal of Statistical Distributions and Applications **4**, 5 (2017), DOI: 10.1186/s40488-017-0059-2. https://link.springer.com/article/10.1186/s40488-017-0059-2
4. G. D. Lin and J. Stoyanov, *On the Moment Determinacy of Products of Non-identically Distributed Random Variables*, arXiv:1406.1654 (2014). https://arxiv.org/abs/1406.1654
