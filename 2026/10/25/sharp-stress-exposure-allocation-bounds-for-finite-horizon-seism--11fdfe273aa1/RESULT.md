# Sharp stress-exposure allocation bounds for finite-horizon seismicity

## Finding

For the constant-normal-stress, spatially homogeneous Dieterich seismicity law, fix a prediction horizon \(T>0\), aftershock relaxation time \(a>0\), background earthquake-production rate \(r>0\), maximum dimensionless positive stress perturbation \(H>0\), and cumulative stress-exposure budget \(0<B<HT\). Admit measurable stress histories \(s:[0,T]\to[0,H]\) satisfying \(\int_0^T s(t)\,dt=B\). Expected cumulative earthquake production \(N_s(T)\) has **unique maximizer** (up to equality almost everywhere)
\[
s_{\max}(t)=H\mathbf1_{(T-B/H,T)}(t),
\]
and **unique minimizer**
\[
s_{\min}(t)=\min\{H,\max\{0,C-t/a\}\}.
\]
Here the constant \(C\in(0,H+T/a)\) is the unique solution of
\[
\frac Ba=\frac12\left[C^2-(C-T/a)_+^2-(C-H)_+^2+(C-H-T/a)_+^2\right],
\qquad u_+=\max\{u,0\}.
\]
Thus the maximal expected count is produced by a late, full-amplitude rectangular perturbation, whereas the minimal count is produced by an early, linearly declining stress perturbation with possible amplitude and zero-stress plateaus. These conclusions hold for all indicated positive parameter values and all admissible histories, not only finite-block protocols.

Writing \(q=T/a\), \(b=B/a\), \(u=\min\{q,\max\{0,C-H\}\}\), and \(v=\min\{q,\max\{0,C\}\}\), their exact values are
\[
N_{\min}=ra\log\!\left(1+e^H(e^u-1)+e^C(v-u)+e^q-e^v\right),
\]
\[
N_{\max}=ra\log\!\left(e^q+(e^H-1)(e^q-e^{q-b/H})\right).
\]
Both optimizers are unique modulo changes on a set of zero time measure. The boundary cases \(B=0\) and \(B=HT\) reduce to the single constant history and are excluded from the strict theorem.

## Assumptions and scope

The background fault population has constant reference seismicity rate \(r\) and constant positive background shear stressing rate. Effective normal stress is time-invariant, all candidate sources respond to the same dimensionless shear-stress deviation \(s(t)=\Delta\tau(t)/(A\sigma)\), and the source-population evolution is represented by the classical Dieterich rate-and-state constitutive law. Its characteristic time is \(a=A\sigma/\dot\tau_{\mathrm{ref}}>0\). There are no source-to-source triggering interactions, variable fault properties, magnitude effects, or delayed poroelastic transfer in this idealized statement.

The controls are **stress perturbations themselves**, not injection rates or production schedules. An admissible history may have jumps, treated as idealized stress steps. For measurable histories, the standard positive integral formula is used as the definition of cumulative expected events; for piecewise absolutely continuous histories it agrees with the normalized seismicity-state differential equation and its multiplicative stress-step updates. Endpoints and individual times have no effect on the time integral. The budget is \(\int s=B\), an imposed stress-time exposure constraint, not a claim that this quantity is an injection-volume, energy, or financial budget.

## Proof

**1. Exact reduction of expected counts.** Let the normalized state be \(\Gamma=a\dot\tau_{\mathrm{ref}}\gamma/(A\sigma)=\dot\tau_{\mathrm{ref}}\gamma\), normalized so \(\Gamma(0^-)=1\). At differentiable times, the original Dieterich law with constant \(\sigma\) is
\[
\dot\Gamma=(1-\Gamma)/a-\Gamma\dot s,
\qquad R(t)=r/\Gamma(t).
\]
Stress steps multiply \(\Gamma\) by \(e^{-\Delta s}\). An integrating factor gives
\[
\Gamma(t)=e^{-t/a-s(t)}D(t),\qquad
D(t)=1+\frac1a\int_0^t e^{u/a+s(u)}\,du.
\]
Consequently, for almost all \(t\), \(R(t)=raD'(t)/D(t)\); since \(D(0)=1\),
\[
N_s(T)=\int_0^T R(t)\,dt=ra\log D(T).
\]
This is the constant-normal-stress specialization of the cumulative-count integral in Heimisson and Segall (2018), equation (18), and can be checked directly from Dieterich's constitutive equation. Since the logarithm is strictly increasing, extremizing \(N_s(T)\) is equivalent to extremizing
\[
J(s)=\int_0^T e^{t/a+s(t)}\,dt.
\]

**2. Unique maximum.** Strict convexity gives the chord bound, with equality only at \(z=0\) or \(z=H\):
\[
e^z\le 1+\frac{e^H-1}{H}z,\quad 0\le z\le H.
\]
Hence
\[
J(s)\le a(e^{T/a}-1)+\frac{e^H-1}{H}\int_0^T e^{t/a}s(t)\,dt.
\]
For \(0\le s\le H\) and \(\int s=B\), the increasing weight \(e^{t/a}\) uniquely maximizes the last integral by putting \(s=H\) on the final interval of length \(B/H\) and zero elsewhere (the strict-weight bathtub/rearrangement argument). This history also attains equality in the chord bound. Both equalities are strict for any other admissible history up to null sets, proving the unique maximum and its displayed formula.

**3. Unique minimum.** Introduce dimensionless time \(x=t/a\in[0,q]\), stress \(z(x)=s(ax)\), and budget \(b=B/a\). For any real \(C\), the strictly convex function \(z\mapsto e^{x+z}-e^Cz\) on \([0,H]\) has the unique minimizer
\[
z_C(x)=\min\{H,\max\{0,C-x\}\}.
\]
Its integrated budget \(\Phi(C)=\int_0^q z_C(x)\,dx\) is exactly the four-square positive-part expression in the finding. It is continuous and strictly increasing for \(0<C<H+q\), tending from \(0\) to \(Hq\) at the two ends; therefore a unique \(C\) satisfies \(\Phi(C)=b\). Integrating the pointwise minimizing inequality for any other admissible \(z\), the linear term \(e^C\int z\) cancels because both histories have budget \(b\), leaving \(J(s)\ge J(s_{\min})\). Strict convexity forces equality only when \(z=z_C\) almost everywhere. On \([0,u]\), \([u,v]\), and \([v,q]\), the minimizing integrand \(e^{x+z_C(x)}\) respectively equals \(e^{x+H}\), \(e^C\), and \(e^x\), giving the displayed exact minimum.

## Verification

The independent algebraic route through the seismicity-state equation gives the same cumulative kernel. A standalone standard-library script `verify.py` evaluates both closed bounds, propagates the exact piecewise-constant state equation with instantaneous stress-step updates, and checks \(600\) randomly generated stress profiles satisfying their budget to numerical tolerance. Random checks are diagnostics only: the proof above covers the whole measurable-control class.

For \(a=r=1\), \(T=2\), \(H=3/2\), \(B=2\), the minimizer has \(C=7/2-\sqrt2\) and is at full amplitude until \(t=2-\sqrt2\), then decreases linearly to a positive terminal perturbation. Numerically
\[
N_{\min}\approx2.76976928170860,
\qquad N_{\max}\approx3.27086268884977,
\]
compared with \(N_0=rT=2\) for zero perturbation. These are illustrative nondimensional parameters, not field calibration.

## Relationship to prior work

Dieterich (1994) develops the constitutive relationship for seismicity following stress perturbations. Ziv (2003), section 2.2, analyzes rectangular stress pulses and post-pulse seismicity. Heimisson and Segall (2018), equations (18) and (20), derive the general temporal kernel and cumulative-count formula, **which are prior results, not claimed here**. The present result solves a separate sharp constrained extremal problem: all bounded stress histories with equal peak cap and equal integrated exposure, including an exactly characterized declining-ramp minimum and a late full-height maximum.

Candela et al. (2022) perform numerical optimization of well injection rates under a seismicity-rate constraint in a coupled hydromechanical model. That control variable and objective differ from the analytical stress-exposure budget and cumulative-count extremum studied here. More recent feedback-control studies likewise address coupled reservoir operational controls rather than the exact constrained stress-history envelope. An equivalent convex-allocation theorem from a wider mathematical literature could apply after reduction, so the claim is to a model-specific, explicit characterization rather than to inventing convex duality or rearrangement principles.

## Limitations

This is an idealized constitutive-model theorem, not an observed earthquake forecast or a policy recommendation for subsurface injection. Real stress histories may not be independently designable; stress diffusion, normal stress variation, finite stress slew rate, fault heterogeneity, spontaneous events and interactions can invalidate the reduction or make the step maximizer infeasible. Only cumulative *expected* counts at one fixed horizon are optimized; instantaneous peak rate, spatial earthquake hazard, event magnitudes, exceedance probability, and horizons after the control period are not optimized. The original 1994 paper's publisher abstract was available, but its full text could not be accessed during the comparison; an unpublished or differently phrased equivalent extremal theorem remains a literature risk. No independent audit has been performed.

## References

- J. H. Dieterich (1994), *A constitutive law for rate of earthquake production and its application to earthquake clustering*, Journal of Geophysical Research 99(B2), 2601–2618, doi:10.1029/93JB02581. First online/public publication listed by the publisher: 1994-02-10.
- A. Ziv (2003), *Foreshocks, aftershocks, and remote triggering in quasi-static fault models*, Journal of Geophysical Research 108(B10), doi:10.1029/2002JB002318.
- E. R. Heimisson and P. Segall (2018), *Constitutive Law for Earthquake Production Based on Rate-and-State Friction: Dieterich 1994 Revisited*, Journal of Geophysical Research 123, 4141–4156, doi:10.1029/2018JB015656.
- T. Candela et al. (2022), *A physics-informed optimization workflow to manage injection while constraining induced seismicity: The Oklahoma case*, Frontiers in Earth Science, doi:10.3389/feart.2022.1053951.
