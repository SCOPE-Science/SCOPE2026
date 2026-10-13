# Sharp predator invasion and all-delay extinction barriers in a delayed eco-epidemic model

## Finding

Consider the positive-parameter eco-epidemic system
\[
\begin{aligned}
\dot x(t)&=rx(t)\left(1-\frac{x(t)+y(t)}{K}\right)
-\frac{\beta x(t)y(t)}{\alpha+y(t)}
-\frac{mx(t)z(t)}{(a+x(t))(b+z(t))},\\
\dot y(t)&=\frac{\beta x(t)y(t)}{\alpha+y(t)}
-\frac{ny(t)z(t)}{cz(t)+y(t)}-\nu y(t),\\
\dot z(t)&=\frac{e_1mx(t-\tau)z(t-\tau)}{(a+x(t-\tau))(b+z(t-\tau))}
+\frac{e_2ny(t-\tau)z(t-\tau)}{cz(t-\tau)+y(t-\tau)}-hz(t).
\end{aligned}
\]
All parameters are positive and the gestation delay \(\tau\) is any finite nonnegative number. We distinguish an exact **local** invasion threshold from an explicit **global** extinction guarantee.

If \(\beta K>\alpha\nu\), the unique predator-free endemic equilibrium is
\[
E=(x_*,y_*,0),\qquad
x_*=\frac{\nu(\alpha+y_*)}{\beta},
\]
where \(y_*\) is the unique positive root of
\[
r(\alpha+y)[\beta K-\alpha\nu-(\beta+\nu)y]-\beta^2Ky=0.
\]
The equilibrium identity is used only as a checked algebraic premise and is not asserted as novel.

Set
\[
p=\frac{e_1m x_*}{b(a+x_*)}+e_2n.
\]
Then for **every** finite delay \(\tau\ge0\), the full predator-free equilibrium is linearly asymptotically stable if \(p<h\), unstable if \(p>h\), and nonhyperbolic with exactly one simple zero characteristic root if \(p=h\). At equality, every other root has strictly negative real part.

When \(p>h\), instability is present even before delay is introduced: one positive real root persists for every delay. With
\[
\omega=\sqrt{p^2-h^2},\qquad
\theta=\arccos(h/p),
\]
the complete sequence of nonzero imaginary-root events is
\[
\boxed{\tau_j=\frac{2\pi(j+1)-\theta}{\omega},\quad j=0,1,2,\ldots.}
\]
All such pairs cross **left to right**. For the number of unstable roots, counted with algebraic multiplicity,
\[
N_+(\tau)=1\quad(0\le\tau<\tau_0)
\]
and
\[
N_+(\tau)=2j+3\quad(\tau_j<\tau<\tau_{j+1}).
\]
At \(\tau_j\) there are \(2j+1\) right-half-plane roots and one simple imaginary conjugate pair. A mathematical small-amplitude periodic orbit bifurcating at such a delay is unstable because the equilibrium's positive real root induces a transverse Floquet multiplier greater than one. Indeed, **no nontrivial nonnegative periodic predator orbit can remain close to this equilibrium when \(p>h\)**: such a physical periodic orbit would have to violate the integrated predator birth–death balance. Any mathematical Hopf offspring must have predator density of both signs.

Finally set
\[
H_{\mathrm{all}}=\frac{e_1mK}{b(a+K)}+e_2n.
\]
For arbitrary infection parameters, if \(h>H_{\mathrm{all}}\), then **every solution from histories with positive susceptible and infected prey and nonnegative predators has exponential predator extinction**:
\[
z(t)=O(e^{-\eta t})\quad\text{for some }\eta>0.
\]
This sufficient global bound is generally larger than the sharp local threshold \(p\) because \(x_*<K\). It does not imply the converse for harvest values between the two thresholds.

## Assumptions and scope

Assume all parameters appearing in the displayed equations are strictly positive and the initial history is continuous on \([-\tau,0]\) with \(x(s)>0\), \(y(s)>0\) and \(z(s)\ge0\) throughout that interval. This ensures that the ratio-dependent predator recruitment term is well-defined even when the predator is absent; merely nonnegative histories could otherwise reach an indeterminate \(0/0\) at a delayed time. Along solutions, \(y'(t)\ge-(\nu+n/c)y(t)\), so \(y(t)>0\) for all finite times, while \(x(t)>0\) follows from its multiplicative equation. The logistic bound on \(x\), the bound \(y'\le\beta x-\nu y\), and at-most-linear delayed growth of \(z\) rule out finite-time blow-up. The proof below also supplies the comparison estimates for exponential predator extinction.

The local equilibrium classification requires \(\beta K>\alpha\nu\). The global sufficient harvest condition does not. Delay is arbitrary but finite. For \(\tau=0\), interpret history terms as values at the present time.

At \(p=h\), linear nonhyperbolicity is the only asserted conclusion: nonlinear center dynamics are not classified. The all-delay instability statement is linear. Its small-periodic-orbit corollary applies to branches that actually exist near the stated crossing; it makes no assertion that each crossing produces such a branch.

## Proof

**1. Endemic prey block.** Setting \(z=0\), the two prey equations are
\[
\dot x=rx(1-(x+y)/K)-\frac{\beta xy}{\alpha+y},
\qquad
\dot y=y\left(\frac{\beta x}{\alpha+y}-\nu\right).
\]
At any positive equilibrium, \(\beta x_*/(\alpha+y_*)=\nu\) and
\[
r\left(1-\frac{x_*+y_*}{K}\right)
=\frac{\beta y_*}{\alpha+y_*}.
\]
These yield the equilibrium equation above. Its left-hand side is a concave quadratic with strictly positive value at \(y=0\) and strictly negative leading coefficient. Therefore exactly one root is positive when \(\beta K>\alpha\nu\).

The linearization of the prey block at \((x_*,y_*)\) is
\[
A=\begin{pmatrix}
-rx_*/K & -rx_*/K-\beta\alpha x_*/(\alpha+y_*)^2\\
\beta y_*/(\alpha+y_*) & -\nu y_*/(\alpha+y_*)
\end{pmatrix}.
\]
Both diagonal entries are strictly negative; the off-diagonal entries have opposite signs. Thus
\[
\operatorname{tr}A<0,\qquad \det A>0,
\]
so both prey eigenvalues have negative real parts for every admissible positive parameter choice. There is no extra prey stability inequality to verify.

**2. Triangular delayed linearization.** The predator birth terms are products of past predator density with functions of past prey densities. At the predator-free equilibrium, their partial derivatives in the prey directions therefore vanish. The predator equation linearizes autonomously as
\[
\dot u(t)=p u(t-\tau)-h u(t).
\]
The full characteristic equation factorizes as
\[
\det(\lambda I-A)\,[\lambda+h-pe^{-\lambda\tau}]=0.
\]
If \(p<h\) and \(\Re\lambda\ge0\), then
\[
|\lambda+h|\ge h>p\ge |pe^{-\lambda\tau}|,
\]
a contradiction. If \(p=h\), equality in this estimate is possible only at \(\lambda=0\); the root is simple because the derivative of the scalar factor there is \(1+h\tau>0\). All other roots lie strictly in the left half-plane.

If \(p>h\), the strictly increasing real function
\[
F(s)=s+h-pe^{-s\tau}\quad(s\ge0)
\]
is negative at zero and tends to infinity. It has a unique positive real zero for every delay. Thus the equilibrium is always unstable in this regime.

**3. Exact imaginary-root ladder.** A nonzero imaginary scalar root \(\lambda=i\omega\) requires
\[
h+i\omega=pe^{-i\omega\tau}.
\]
The modulus gives the unique positive frequency
\[
\omega=\sqrt{p^2-h^2}.
\]
Separating real and imaginary parts gives
\[
\cos(\omega\tau)=h/p,\qquad
\sin(\omega\tau)=-\omega/p.
\]
Hence every nonnegative delay with an imaginary pair is precisely
\[
\tau_j=\frac{2\pi(j+1)-\arccos(h/p)}{\omega}.
\]
The scalar characteristic derivative is
\[
\partial_\lambda F=1+p\tau e^{-\lambda\tau}
=1+\tau(h+i\omega)
\]
at crossing, so each root is simple. Implicit differentiation yields
\[
\lambda'(\tau)
=-\frac{\lambda(\lambda+h)}{1+\tau(\lambda+h)}.
\]
At \(\lambda=i\omega\),
\[
\Re\lambda'(\tau_j)
=\frac{\omega^2}{(1+h\tau_j)^2+(\omega\tau_j)^2}>0.
\]
For a retarded differential equation, the unstable-root count is finite and locally constant except at imaginary-axis crossings. At zero delay the predator factor has precisely one unstable eigenvalue \(p-h\); the prey eigenvalues are stable. Every subsequent simple conjugate crossing adds two unstable roots, proving the full ladder.

At every crossing, the persistent positive real characteristic root gives a spectral multiplier \(e^{s_+T}>1\) over the positive period \(T\) of a nearby Hopf orbit. Continuity of the variational monodromy spectrum at a nondegenerate small-amplitude branch preserves an unstable multiplier, so no sufficiently small bifurcating periodic orbit can be orbitally asymptotically stable.

There is a stronger positive-cone obstruction. Write
\[
q(t)=\frac{e_1m x(t)}{(a+x(t))(b+z(t))}
+\frac{e_2n y(t)}{cz(t)+y(t)}.
\]
For all trajectories sufficiently near \(E\), this continuous function satisfies \(q(t)>h\) because its equilibrium value is \(p>h\). If a nontrivial periodic trajectory of period \(T>0\) had \(z(t)\ge0\), integration of
\[
\dot z(t)=q(t-\tau)z(t-\tau)-hz(t)
\]
over a full period (and periodic shifting of the delayed term) would give
\[
0=\int_0^T[q(t)-h]z(t)\,dt>0,
\]
a contradiction. The same integral is strictly negative if the predator density is nonpositive but not identically zero. Therefore every sufficiently small nontrivial mathematical periodic orbit near \(E\), if it exists, must have predator density of both signs: it is not a biological periodic solution. This argument does not presume nonlinear Hopf existence or a computed Lyapunov coefficient.

**4. Global predator extinction.** The susceptible equation gives
\[
\dot x\le rx(1-x/K).
\]
Comparison with the logistic equation shows
\[
\limsup_{t\to\infty}x(t)\le K.
\]
For arbitrary \(\varepsilon>0\), eventually \(x(t)\le K+\varepsilon\). The predator birth terms are bounded by
\[
\dot z(t)\le q_\varepsilon z(t-\tau)-hz(t),
\]
where
\[
q_\varepsilon
=\frac{e_1m(K+\varepsilon)}{b(a+K+\varepsilon)}+e_2n.
\]
Indeed, the susceptible-prey birth contribution uses \(b+z\ge b\), and the infected-prey contribution uses \(y/(cz+y)\le1\). If \(h>H_{\mathrm{all}}\), choose \(\varepsilon\) such that \(q_\varepsilon<h\). For any fixed finite \(\tau\), choose \(\eta>0\) so that
\[
\eta+q_\varepsilon e^{\eta\tau}<h.
\]
A sufficiently large multiple of \(e^{-\eta t}\) is then a supersolution for the scalar delayed comparison equation on the eventual history window. Standard scalar comparison proves
\[
z(t)=O(e^{-\eta t}).
\]
No restriction on the infection reproduction number or gestation delay is needed for this sufficient nonlinear extinction criterion.

## Verification

For the rational parameters
\[
r=5/3,\quad K=5,\quad\alpha=\nu=a=b=m=n=e_1=e_2=1,\quad\beta=2,
\]
substitution gives \((x_*,y_*)=(1,1)\), and the prey Jacobian and its characteristic polynomial are
\[
A=\begin{pmatrix}-1/3&-5/6\\1&-1/2\end{pmatrix},
\qquad
\det(\lambda I-A)=\lambda^2+\frac56\lambda+1.
\]
The predator recruitment factor and the uniform all-state envelope are exactly
\[
p=3/2,\qquad H_{\mathrm{all}}=11/6.
\]
At \(h=2\), the global extinction criterion applies for every finite delay. At \(h=1\), the unique positive imaginary frequency is \(\sqrt5/2\), and the complete critical-delay ladder and positive crossing derivatives follow by the closed formulas.

The bundled standalone checker verifies the exact equilibrium and Jacobian entries with rational arithmetic, checks the strict local/global inequalities, and evaluates the first six imaginary characteristic residuals and crossing-direction derivatives. It is corroboration; the proofs are analytic.

## Relationship to prior work

Sarwardi and coauthors derive the predator-free invasion coefficient (their \(A_1\)), provide no-delay local stability conditions, and discuss an imaginary-frequency condition when \(A_1>h\) in their Theorem 1. Their analysis does not state the all-delay stability trichotomy, the permanent positive real eigenvalue for \(A_1>h\), the exact unstable-root counts, the instability of nearby periodic branches, or a nonlinear harvesting guarantee ensuring predator extinction for every gestation delay.

The scalar retarded stability inequality and the comparison argument are classical general techniques and are not presented as new methods. The contribution here is a complete spectral and biologically interpretable invasion classification for the actual three-population model, combined with a concrete nonlinear harvest intervention bound that does not require proximity to equilibrium. The sharp local threshold and sufficient global threshold are expressly distinguished.

The corrected algebraic existence/uniqueness classification of the predator-free endemic equilibrium is treated as background, not as part of the new contribution. The present result concerns its delay spectrum and nonlinear global predator extinction.

Earlier delay-predator literature studies global attraction for other functional responses and different locations of disease. A closer 2019 predecessor with infected prey and both Crowley–Martin functional responses introduces two delays; its abstract was compared, but full-text access was unavailable, so no decisive whole-paper novelty exclusion is claimed. These works motivate the comparison, but their equations do not imply the exact invasion factor or intervention bounds for the present mixed Crowley–Martin and ratio-dependent eco-epidemic system.

## Limitations

The critical case \(p=h\) is spectrally nonhyperbolic; nonlinear attraction or repulsion on its center manifold is not established.

The global bound \(h>H_{\mathrm{all}}\) is sufficient, not necessary, and does not claim that all prey compartments converge to a specified endemic state. It guarantees exponential extinction only of predators. No uniform decay exponent independent of delay is claimed.

For \(p>h\), small Hopf offspring, if present, are unstable; existence and nonlinear criticality of each branch are not computed. Exact spectral counts rely on standard retarded-delay root continuity and do not apply unchanged to neutral delay equations.

Nonnegative periodic predator orbits are locally excluded in the invasion regime; sign-changing mathematical solutions of the Hopf normal form may still exist. A particularly close 2019 two-delay infected-prey predecessor remained inaccessible in full text, and an equivalent statement under different notation remains a residual novelty risk. Relevant older general delayed predator–prey papers were not all available in full text for complete comparison.

## References

1. S. Sarwardi, H. Mollah, A. A. Raezah, F. Al Basir, “Direction and stability of Hopf bifurcation in an eco-epidemic model with disease in prey and predator gestation delay using Crowley-Martin functional response,” AIMS Mathematics 9 (2024), 27930–27954. DOI: 10.3934/math.20241356.
2. D. Das, S. Chakraborty, “A brief discussion about a predator-prey model including disease in predators with the delay effect,” Numerical Algebra, Control and Optimization 15 (2025), 357–385; early access September 5, 2023. DOI: 10.3934/naco.2023018.
3. S. G. Mortoja, P. Panja, S. K. Mondal, “Dynamics of a predator-prey model with nonlinear incidence rate, Crowley-Martin type functional response and disease in prey population,” Ecological Genetics and Genomics 10 (2019), 100035. DOI: 10.1016/j.egg.2018.100035.
4. Y. Cao, H. I. Freedman, “Global attractivity in time-delayed predator-prey systems,” Journal of the Australian Mathematical Society Series B 38 (1996), 149–162. DOI: 10.1017/S0334270000000540.
