# A sign-definite second-harmonic threshold and exact escape clock for seventh-degree equivariant flows

## Finding
Consider the fourfold-equivariant real planar homogeneous polynomial system, written in complex coordinates,
\[
\dot z=(-a+i\omega)z|z|^6+bz^2\overline z^{\,5}+c\overline z^{\,7}.
\]
Let \(b>0\), \(c,a\in\mathbb R\), and suppose the angular rotation condition
\[
\omega>M(b,c):=\max_{u\in[0,2\pi]}|b\sin u+c\sin(2u)|
\]
holds. Define the positive integral
\[
J=\int_0^{2\pi}\frac{du}{\omega-b\sin u-c\sin(2u)},
\]
and the sharp damping threshold
\[
a_*=-\frac cJ\int_0^{2\pi}\frac{\cos(2u)}{\omega-b\sin u-c\sin(2u)}\,du.
\]
Then \(a_*\) has **exactly the sign of \(c\)** (and is zero exactly when \(c=0\)). More quantitatively,
\[
|a_*|\ge\frac{|c|b^2(\omega-M(b,c))}{4\omega^3}.
\]
The global dynamics have an exhaustive three-way classification:

* For \(a>a_*\), the origin is globally asymptotically stable, and every nonzero trajectory has radius \(r(t)=\Theta(t^{-1/6})\) as physical time tends to infinity.
* For \(a=a_*\), the origin is Lyapunov stable but not attracting, and every nonzero trajectory is periodic; its physical period scales inversely with the sixth power of its initial radius at fixed initial angle.
* For \(a<a_*\), the origin is unstable, and every nonzero trajectory escapes to infinity in finite positive physical time \(T\), with \(r(t)=\Theta((T-t)^{-1/6})\).

For fixed \(\omega>b>0\), \(a_*(b,c,\omega)\) is odd and real-analytic near \(c=0\), and its exact first variation is
\[
a_*(b,c,\omega)=\left(\frac b{\omega+\sqrt{\omega^2-b^2}}\right)^2c+O(c^3).
\]
Thus adding the second angular harmonic creates, for every admissible \(c>0\), a **positive-damping interval \(0<a<a_*\)** in which every nonzero orbit blows up. For \(c<0\), there is conversely an interval \(a_*<a<0\) in which the system is globally attracting despite a negative isotropic damping coefficient.

The original-time escape clock is exact, not merely asymptotic. Set
\[
f(\theta)=-a+b\cos(4\theta)+c\cos(8\theta),\qquad
g(\theta)=\omega-b\sin(4\theta)-c\sin(8\theta).
\]
For an initial state \(z(0)=r_0e^{i\theta_0}\ne0\), define
\[
I=J(a_*-a),\quad
K(a,\theta_0)=\int_0^{2\pi}\frac{\exp\left[-6\int_0^s\frac{f(\theta_0+v)}{g(\theta_0+v)}\,dv\right]}{g(\theta_0+s)}\,ds.
\]
When \(a<a_*\), the finite blow-up time satisfies
\[
T=\frac{r_0^{-6}K(a,\theta_0)}{1-e^{-6I}}.
\]
With \(b,c,\omega,r_0,\theta_0\) fixed, let \(K_*(\theta_0)=K(a_*,\theta_0)\). The sharp critical slowdown is
\[
\lim_{a\uparrow a_*}(a_*-a)T
=\frac{r_0^{-6}K_*(\theta_0)}{6J}>0.
\]

## Assumptions and scope
The variables \(z=x+iy\) and physical time \(t\) are real-planar and real, respectively. All coefficients \(a,b,c,\omega\) are real. The only restrictions are \(b>0\) and the strict rotation inequality above; in particular \(c\) need not be small. The origin is an equilibrium of polynomial degree seven, and the theorem quantifies all nonzero initial data, not merely small-amplitude trajectories. Big-Theta bounds have positive constants depending on the fixed coefficients and initial state. The analytic expansion near \(c=0\) assumes \(\omega>b>0\) fixed; it is not asserted to be uniform as \(\omega\downarrow b\).

## Proof
**1. Polar reduction and return map.** Writing \(z=re^{i\theta}\), direct substitution of the three degree-seven monomials gives
\[
\dot r=r^7f(\theta),\qquad \dot\theta=r^6g(\theta).
\]
The hypothesis on \(\omega\) implies \(g(\theta)>0\) for all \(\theta\), so nonzero trajectories have a strictly increasing angular coordinate. Consequently
\[
\frac{d\log r}{d\theta}=\frac{f(\theta)}{g(\theta)}.
\]
As \(f,g\) have angular period \(\pi/2\), integrating over a full \(2\pi\) turn and substituting \(u=4\theta\) gives the exact logarithmic multiplier
\[
I=\int_0^{2\pi}\frac{f(\theta)}{g(\theta)}\,d\theta
=-aJ+N=J(a_*-a),
\]
where
\[
N=\int_0^{2\pi}\frac{b\cos u+c\cos(2u)}{\omega-b\sin u-c\sin(2u)}\,du.
\]
Because the derivative of the denominator is \(-b\cos u-2c\cos(2u)\), a full-period logarithmic derivative integrates to zero. Hence
\[
N=-cL,\qquad L=\int_0^{2\pi}\frac{\cos(2u)}{\omega-b\sin u-c\sin(2u)}\,du.
\]
This proves the stated formula for \(a_*\). The exact radial return map at fixed angle is \(r\mapsto e^Ir\).

**2. Strict Fourier sign, valid throughout the rotating sector.** Put \(X(u)=b\sin u+c\sin(2u)\) and \(M=\max_u|X(u)|\). Since \(X\) is odd, pairing \(u\) and \(-u\) yields
\[
L=\omega\int_0^{2\pi}\frac{\cos(2u)}{\omega^2-X(u)^2}\,du
=\frac1\omega\sum_{n=0}^{\infty}\frac{1}{\omega^{2n}}
\int_0^{2\pi}\cos(2u)X(u)^{2n}\,du.
\]
The series converges uniformly because \(M<\omega\). Expand \(X(u)^{2n}=\sin^{2n}u\,(b+2c\cos u)^{2n}\). Terms with an odd power of \(\cos u\) integrate to zero under \(u\mapsto\pi-u\). The remaining terms are nonnegative coefficients multiplying
\[
A_{n,j}:=\int_0^{2\pi}\cos(2u)\sin^{2n}u\cos^{2j}u\,du,
\qquad 0\le j\le n.
\]
The beta-function recurrence, or one integration by parts, gives exactly
\[
A_{n,j}=\frac{j-n}{n+j+1}
\int_0^{2\pi}\sin^{2n}u\cos^{2j}u\,du\le0.
\]
At \(n=1,j=0\), the coefficient is \(b^2>0\) and \(A_{1,0}=-\pi/2\). Thus every other surviving summand is nonpositive and
\[
L\le-\frac{\pi b^2}{2\omega^3}<0.
\]
Since \(J>0\), this proves \(\operatorname{sgn}(a_*)=\operatorname{sgn}(c)\). Moreover \(J\le 2\pi/(\omega-M)\), which gives the displayed quantitative lower bound on \(|a_*|\).

**3. Exact symmetry and small-harmonic slope.** Under \(u\mapsto\pi-u\), both \(J\) and \(L\) are even in \(c\). For \(\omega>b\), their denominators stay uniformly positive for all sufficiently small \(|c|\), so both integrals and their quotient are real-analytic. Thus \(a_*=-cL/J\) is odd. Put
\[
q=\frac b{\omega+\sqrt{\omega^2-b^2}},\qquad 0<q<1.
\]
The absolutely convergent Poisson expansion is
\[
\frac1{\omega-b\sin u}=
\frac1{\sqrt{\omega^2-b^2}}
\left(1+2\sum_{k=1}^{\infty}q^k\cos(k(u-\pi/2))\right).
\]
Its second cosine moment is \(L(b,0,\omega)=-J(b,0,\omega)q^2\). Differentiating \(-cL/J\) at zero and using oddness therefore gives \(a_*=q^2c+O(c^3)\).

**4. Global trichotomy and physical-time completeness.** In any angular turn the radius changes by the factor \(e^I\). Within each turn, the ratio of radius to its value at the beginning stays between two strictly positive uniform constants because \(f/g\) is continuous and periodic. If \(I<0\), radii contract geometrically, the physical time needed for later turns increases geometrically, and the radius remains bounded and tends to zero. Uniform within-turn bounds imply Lyapunov stability and \(r(t)=\Theta(t^{-1/6})\); the solution exists for all \(t\ge0\). If \(I=0\), the radius returns after one turn, providing a closed nonconstant orbit through every nonzero state; the same uniform bound gives Lyapunov stability but no attraction. If \(I>0\), radii grow geometrically and the physical flight times form a convergent geometric series: every nonzero orbit blows up at a finite physical time and the origin is unstable. The periodic within-turn factor also gives \(r(t)=\Theta((T-t)^{-1/6})\). These arguments cover all initial radii and angular phases, and exclude any other recurrent regime under \(g>0\).

**5. Exact escape-clock summation.** Along one angular turn starting from \((r_0,\theta_0)\), solve the logarithmic-radius equation exactly:
\[
r(\theta_0+s)=r_0\exp\left(\int_0^s\frac{f(\theta_0+v)}{g(\theta_0+v)}\,dv\right).
\]
Because \(dt/d\theta=1/(r^6g)\), its physical duration is exactly \(r_0^{-6}K(a,\theta_0)\). Every subsequent angular turn begins with its radius multiplied by \(e^I\), so the corresponding duration is multiplied by \(e^{-6I}\). Summation gives \(T=r_0^{-6}K/(1-e^{-6I})\) when \(I>0\). Since \(K\) depends continuously on \(a\) near \(a_*\) and \(I=J(a_*-a)\), multiplication by \(a_*-a\) and passage to the limit yield the asserted exact critical coefficient.

## Verification
The accompanying standalone script `verify.py` rederives the complex-monomial angular exponents symbolically; checks the beta-integral sign identities for finitely many indices; compares direct high-precision quadrature with the integration-by-parts identity for positive and negative second harmonics, including angularly near-critical parameters; checks the threshold slope and odd symmetry numerically; and independently integrates the angular flight equation to compare its return drift and physical-time geometric clock. It checks diagnostics only; the universal sign and trichotomy follow from the analytical argument above. Run the script with Python 3 and the `sympy`, `mpmath`, `numpy`-compatible SciPy installation via `python verify.py`.

## Relationship to prior work
The angular return-map idea and the general center criterion are classical. Giné, Llibre and Valls (2017, Lemma 1) state that a planar homogeneous system with nonvanishing angular speed is a center precisely when its radial/angular quotient has vanishing angular integral; their degree-seven classification specifically concerns nonhomogeneous weight-homogeneous systems. Shevchenko, Liu and Liu (2026, Section 3) prove a general invariant-average criterion for global asymptotic stability and discuss the planar decidability background. Thus the use of an angular integral to test stability or a center, by itself, is **not** a new result. The present finding is the all-parameter strict sign evaluation for a minimal two-harmonic fourfold-equivariant septic class, the resulting positive-damping/negative-damping reversal, its explicit threshold slope and quantitative finite-time blow-up clock.

The classical two-dimensional homogeneous stability framework of Samardžija (1983) is relevant but its complete text was not available for direct priority comparison. Work on fourfold-equivariant cubic centers (Du, Liu and Liu, 2013) concerns another degree and equilibrium structure. These distinctions are mathematical scope comparisons, not a claim of exhaustive bibliographic priority.

## Limitations
All conclusions require strictly nonvanishing angular speed; no behavior is asserted on or beyond the angular-locking boundary \(\omega=M(b,c)\). The analytic expansion is for fixed \(\omega>b>0\) as \(c\to0\), and the escape-clock pole fixes \(b,c,\omega,r_0,\theta_0\). The exact duration depends on initial angle and radius. The theorem neither asserts perturbation robustness nor resolves broader homogeneous-vector-field stability decision problems. Literature priority remains subject to additional specialist verification; in particular the complete 1983 stability paper was not inspected. Independent validation has not been performed.

## References
1. I. O. Shevchenko, J. Liu, X. Liu, *Global asymptotic stability of homogeneous polynomial vector fields is undecidable*, arXiv:2610.12434v1 (first posted 2026-10-08), especially Section 3. https://arxiv.org/abs/2610.12434
2. J. Giné, J. Llibre, C. Valls, *Centers of weight-homogeneous polynomial vector fields on the plane*, Proceedings of the American Mathematical Society 145 (2017), 2539–2555, Lemma 1 and the degree-seven distinction. https://doi.org/10.1090/proc/13393 ; author preprint: https://ddd.uab.cat/pub/artpub/2017/gsduab_4239/proamematsoc_a2017v145n6p2539preprint.pdf
3. N. Samardžija, *Stability properties of autonomous homogeneous polynomial differential systems*, Journal of Differential Equations 48 (1983), 60–70. https://doi.org/10.1016/0022-0396(83)90059-1
4. C. Du, Y. Liu, C. Liu, *Weak center problem and bifurcation of critical periods for a Z4-equivariant cubic system*, Advances in Difference Equations 2013, 197. https://doi.org/10.1186/1687-1847-2013-197
5. J. Giné, J. Llibre, C. Valls, *Simultaneity of centres in Zq-equivariant systems*, Proceedings of the Royal Society A 474 (2018), 20170811. https://doi.org/10.1098/rspa.2017.0811
