# A sharp minimum for nonlinear period softening along the Gray–Scott Hopf curve

## Finding
Consider the spatially homogeneous Gray–Scott kinetics
\[
\dot u=F(1-u)-uv^2,\qquad \dot v=uv^2-(F+k)v,\qquad F,k>0.
\]
Every positive-equilibrium Hopf point with nonzero imaginary eigenvalues has the unique parameterization
\[
 k_t=\frac{t^2}{(1+t)^4},\quad F_t=\frac{t^3}{(1+t)^4},\quad
 (u_t,v_t)=\left(\frac{t}{1+t},\frac{t}{(1+t)^2}\right),\quad 0<t<1.
\]
Consider *any* family of nonconstant small periodic orbits whose parameters tend to \((F_t,k_t)\) and whose orbits shrink to the positive equilibrium. At the actual parameters of each orbit, let \(\omega_{\mathrm{lin}}>0\) be the absolute imaginary part of the eigenvalues of the Jacobian at the nearby positive equilibrium, let \(T\) be the orbit's least period, and let \(a\) be the modulus of the first temporal Fourier harmonic of \(v-v_{\mathrm{eq}}\):
\[
 a=\sqrt{\left(\frac2T\int_0^T(v(s)-v_{\mathrm{eq}})\cos(2\pi s/T)\,ds\right)^2+
\left(\frac2T\int_0^T(v(s)-v_{\mathrm{eq}})\sin(2\pi s/T)\,ds\right)^2}.
\]
Then, as \(a\to0\),
\[
\boxed{\frac{T\omega_{\mathrm{lin}}}{2\pi}-1=C(t)a^2+o(a^2),\qquad
 C(t)=\frac{(9t^2+6t+5)(1+t)^3}{24t^2(1-t)^2}.}
\]
The coefficient is positive at **every** Hopf point, including the generalized-Hopf point \(t=1/3\), and has a **unique sharp global minimum** on \((0,1)\). Precisely,
\[
 C(t)\ge C(t_* )=15.796641246067701\ldots,
 \quad t_*=0.300154330325167\ldots,
\]
where \(t_*\) is the unique root in \((0,1)\) of
\[
9t^4-45t^3-35t^2-19t+10=0.
\]
Equality occurs exactly at \(t=t_*\). At the known generalized-Hopf parameter \(t=1/3\), the coefficient is exactly \(C(1/3)=16\). The coefficient is relative to the *linearized frequency at the same parameters*; it is not a claim that absolute period increases along every path in parameter space.

## Assumptions and scope
The physical time and dimensionless concentrations are those of the displayed homogeneous Gray–Scott ODE, without time reparameterization. All parameters are positive. The limiting Hopf equilibrium is the positive nonsaddle equilibrium, not the always-stable boundary equilibrium. The nearby periodic orbits may be attracting or repelling; existence of small cycles off the generalized-Hopf point follows from the ordinary Hopf theorem, while existence of nearby cycles at the generalized-Hopf point is part of established Bautin theory for this model. The assertion is pointwise for each fixed \(t\in(0,1)\) and for all sequences of such cycles approaching its Hopf point. It does not require a chosen one-parameter unfolding. The Fourier amplitude \(a\) is invariant under shifting time origin.

## Proof
**1. Exact Hopf curve.** At a positive equilibrium,
\[
uv=F+k,\qquad F(1-u)=(F+k)v,
\]
and the Jacobian has trace \(k-v^2\) and determinant \((F+k)(v^2-F)\). Pure imaginary nonzero eigenvalues require \(v^2=k>F\). Eliminating the equilibrium variables gives \(F\sqrt{k}=(F+k)^2\). With \(t=F/k\in(0,1)\), this gives the asserted formulas, and
\[
 \omega^2=(F+k)(k-F)=k^2-F^2>0.
\]
Conversely, all the displayed points satisfy the positive equilibrium and Hopf conditions. Along the Hopf curve \(\omega=k\sqrt{1-t^2}\).

**2. Time-preserving canonical coordinates.** Fix such a Hopf point and write \(c=F+k\), \(s=v_{\mathrm{eq}}=\sqrt{k}\), \(X=v-v_{\mathrm{eq}}\), and \(Y=(u-u_{\mathrm{eq}})+X\). Define \(x=X\) and \(y=(F X+kY)/\omega\). A direct polynomial expansion, without altering time, yields
\[
 \dot x=\omega y+N(x,y),\qquad
 \dot y=-\omega x+\frac{F}{\omega}N(x,y),
\]
with
\[
 N=Ax^2+Bxy+Cx^3+Dx^2y,\qquad
 A=-\frac{F+k}{s},\quad B=\frac{2\omega}{s},\quad
 C=-\frac{F+k}{k},\quad D=\frac{\omega}{k}.
\]
Thus, for \(z=x+iy\), the equation is \(\dot z=-i\omega z+P_2(z,\bar z)+P_3(z,\bar z)\), where \(P_j=(1+iF/\omega)N_j\) and \(N_j\) is the homogeneous degree-\(j\) part of \(N\).

**3. Cubic resonant coefficient.** Eliminate quadratic terms by the unique quadratic near-identity substitution \(z=w+H_2(w,\bar w)+O(|w|^3)\), where, writing \(\lambda=-i\omega\),
\[
 (H_2)_{j,2-j}=\frac{(P_2)_{j,2-j}}{(j-1)\lambda+(2-j)\bar\lambda},\qquad j=0,1,2.
\]
All denominators are nonzero. The coefficient of \(w^2\bar w\) after quadratic elimination is the coefficient of that monomial in
\[
 P_3+(\partial_zP_2)H_2+(\partial_{\bar z}P_2)\overline{H_2}.
\]
Expansion, followed by \(s^2=k\) and \(\omega^2=k^2-F^2\), gives the **physical-time** cubic resonant coefficient
\[
 \boxed{G=G_R+iG_I,\qquad
 G_R=\frac{3F-k}{8(k-F)},\quad
 G_I=\frac{9F^2+6Fk+5k^2}{24\omega(k-F)}.}
\]
These are exact algebraic identities, rechecked directly in `check_symbolic.py`. In particular, \(G_I>0\) throughout the Hopf curve, even though \(G_R\) changes sign at \(F/k=1/3\). The known Bautin degeneracy is the zero of the real, not imaginary, cubic part.

**4. Period of nearby cycles.** Carry the time-preserving polynomial normal-form transformation out smoothly in parameters near the fixed Hopf point. For parameters sufficiently close, the linear eigenvalues are \(\sigma\pm i\omega_{\mathrm{lin}}\) and the Hopf normal form is
\[
 \dot w=(\sigma-i\omega_{\mathrm{lin}})w+[G+o(1)]w|w|^2+O(|w|^4),
\]
where the \(o(1)\) depends on parameter displacement. On any shrinking periodic orbit, standard angular averaging therefore gives angular frequency \(\omega_{\mathrm{lin}}-G_Ir^2+o(r^2)\), with \(r\) the leading complex normal-form radius. The quadratic substitution produces only the zero and second Fourier harmonics in \(x=v-v_{\mathrm{eq}}\), so the *first* harmonic satisfies \(a=r+O(r^2)\). This yields
\[
 \frac{T\omega_{\mathrm{lin}}}{2\pi}-1=\frac{G_I}{\omega}a^2+o(a^2).
\]
Substitute \(F=tk\), \(k=t^2/(1+t)^4\), and \(\omega^2=k^2(1-t^2)\) to obtain the displayed \(C(t)\). The argument uses actual periodic orbits and neither treats trajectories at the Hopf point as periodic nor interprets finite numerics as existence proofs.

**5. Sharp minimization.** The exact derivative is
\[
 C'(t)=\frac{(1+t)^2[9t^4-45t^3-35t^2-19t+10]}{24t^3(t-1)^3}.
\]
The quartic \(P\) in brackets satisfies \(P(0)=10\), \(P(1)=-80\), and
\[
P'(t)=36t^3-135t^2-70t-19<0\quad(0<t<1),
\]
because \(36t^3<36t^2\). Hence it has exactly one zero \(t_*\in(0,1)\). Since the derivative denominator is negative, \(C\) decreases before and increases after \(t_*\). The limits at both endpoints are infinite, making the minimum strict and global. Direct substitution gives \(C(1/3)=16\).

## Verification
Running `python check_symbolic.py` with SymPy checks the original equilibrium and Hopf conditions, the quadratic homological elimination, the complex cubic coefficient, the period coefficient, and the unique-minimum algebra with exact symbolic identities. Running `python check_shooting.py` with NumPy and SciPy performs optional high-accuracy periodic-orbit shooting on both sides of the generalized-Hopf point. For \(t=1/4\), the predicted coefficient is \(16.34837963\ldots\); for \(t=1/2\) it is \(23.0625\). The observed normalized period quotients tend to these predictions as the prescribed concentration excursion decreases. This numerical agreement corroborates but is not needed for the universal proof.

## Relationship to prior work
Gray and Scott's cubic-autocatalysis studies introduced the chemical-oscillator setting and described the onset, period, and amplitude behavior of sustained oscillations. Delgado, Hernández-Martínez, and Pérez-López analyzed precisely the homogeneous two-parameter Gray–Scott ODE and proved its Takens–Bogdanov and generalized-Hopf points, including \((k,F)=(9/256,3/256)\) and the change in sign of the real first Lyapunov coefficient. Their bifurcation normal form uses an angular equation normalized to unit speed; such an orbital/time normalization does **not** imply a coefficient for the physical-time period compared at the same parameters. Nor does a period trend along a residence-time path imply the asserted path-independent first-harmonic period residual and its sharp minimizer. The result concerns this remaining physical-time period invariant, not rediscovery of the Hopf or Bautin thresholds.

## Limitations
The result is local to shrinking periodic orbits of the homogeneous ODE; it makes no claim about global cycle periods, their uniqueness far from Hopf, heterogeneous reaction-diffusion patterns, or monotonically varying absolute period along arbitrary parameter paths. The limit is taken at each fixed \(0<t<1\), with no assertion uniform as the zero-frequency endpoint is approached. At \(t=1/3\), the leading radial cubic coefficient vanishes, but the angular coefficient remains nonzero; small-cycle existence there depends on the established two-parameter Bautin unfolding. Full text of a relevant 1984 historical article was not available for direct inspection, leaving a publication-priority risk despite comparison with its indexed abstract. The index date of the historical foundational article may have been normalized to the first day of its publication year. No independent audit has been performed.

## References
1. P. Gray and S. K. Scott, "Autocatalytic reactions in the isothermal, continuous stirred tank reactor: oscillations and instabilities in the system A + 2B → 3B; B → C," *Chemical Engineering Science* 39 (1984), 1087–1097. DOI: `10.1016/0009-2509(84)87017-7`.
2. J. Delgado, L. I. Hernández-Martínez and J. Pérez-López, "Global bifurcation map of the homogeneous states in the Gray–Scott model," *International Journal of Bifurcation and Chaos* 27 (2017), 1730024. DOI: `10.1142/S0218127417300245`; lawful public preprint `arXiv:1702.03353v1` (2017-02-10).
3. P. Gray and S. K. Scott, "Autocatalytic reactions in the isothermal, continuous stirred tank reactor: isolas and other forms of multistability," *Chemical Engineering Science* 38 (1983), 29–43. DOI: `10.1016/0009-2509(83)80132-8`. Background on the earlier cubic-autocatalysis scheme, not itself the full later catalyst-decay model.
