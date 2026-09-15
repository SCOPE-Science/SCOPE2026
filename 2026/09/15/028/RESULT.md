# Axis-Centered Scale Dichotomy and Ring-Escape Obstruction for Gamma-Bounded Axisymmetric Navier-Stokes Blowup

## Context

The admitted target asked for an unconditional axisymmetric critical-element extraction: every finite-time axisymmetric Navier-Stokes blowup with uniformly bounded critical swirl
M = sup_t ||r v_theta(t)||_oo should produce, via axis-centered profile decomposition with scales lambda_k -> 0 and cores on the symmetry axis, a non-trivial bounded axisymmetric ancient mild solution retaining the Gamma bound. The submitted emergent finding arose while honestly closing each step of that route: on-axis Gamma algebra, Type-I compactness, and Type-II backward-window exhaustion all verified, but the Type-II amplitude-renormalization step did not close. This record states the resulting proved obstruction lemma.

## Definitions

Work in cylindrical coordinates (r,theta,z) on R^3. A field is axisymmetric if its cylindrical components are theta-independent. Define Gamma := r v_theta and M := sup_{0<t<T*} ||Gamma(t)||_oo. Navier-Stokes scaling about z0=(x0,T*) is v^lambda(y,s) := lambda v(x0+lambda y, T*+lambda^2 s). For amplitude renormalization at peak points x_k with M_k := |v(x_k,t_k)| -> oo, set mu_k := 1/M_k and u_k(z,s) := mu_k v(x_k+mu_k z, t_k+mu_k^2 s). For a blowup ring of radius r_k := r(x_k) -> 0 define the dimensionless normalized peak distance d_k := r_k M_k = r_k/mu_k.

## Result

Theorem (Axis-centered scale dichotomy and ring-escape criterion). Let v be axisymmetric. (A) Navier-Stokes rescaling about x0 preserves axisymmetry about the global z-axis for all lambda>0 iff x0 lies on the axis. (B) If x0 is on the axis, Gamma^lambda(y,s)=Gamma(x,t) identically, so ||Gamma^lambda(s)||_oo = ||Gamma(t)||_oo <= M exactly; off-axis centering instead gives Gamma^lambda -> 0 pointwise. (C) For axis-projected amplitude renormalization centered at the on-axis projection of a peak ring, the normalized peak sits at distance d_k from the origin; if d_k -> oo along a subsequence, the peak eventually leaves every fixed ball, so no subsequence converges locally uniformly on compacts to a limit carrying the peak normalization, while if d_k stays bounded the peaks remain in a fixed ball and compactness can in principle proceed. (D) Under a Type-II model rate ||v(t)||_oo=(T*-t)^{-alpha} with alpha>1/2, the rescaled backward time window exhausts (-oo,0], so the obstruction in (C) is spatial escape rather than lack of ancient time. (E) For arbitrary r_k>0 and M_k<oo there exists a smooth compactly supported axisymmetric divergence-free field with Gamma=0 and max|v|=M_k at radius r_k, so M<oo imposes no constraint on (r_k,M_k) or d_k. Corollary (conditional form): unconditional axis-centered extraction needs, beyond M<oo, a non-escape bound limsup_k d_k<oo, equivalently a poloidal Type-I rate bound that M does not control; under such a bound plus standard CKN/Aubin-Lions compactness, axis-centered extraction can proceed.

## Proof and evidence

(A) follows from R(x0+lambda y)=Rx0+lambda Ry for z-rotations R: equality with x0+lambda Ry for all y holds iff Rx0=x0. (B) is direct algebra: on axis r_x=lambda rho, v_theta=Gamma/r_x, hence (v^lambda)_theta=lambda Gamma/(lambda rho) and rho times it equals Gamma; verified symbolically in scaling_check.py part (a); part (b) gives the off-axis collapse formula. (C) is the identity that the on-axis projection sits at physical distance r_k, i.e. r_k/mu_k=d_k in rescaled variables, plus point-set compactness: unbounded d_k defeats uniform convergence on compacts carrying |u_k|=1 at the peak, while bounded d_k permits Bolzano-Weierstrass extraction of peak positions. (D) is the exponent computation (T*-t_k)/mu_k^2=(T*-t_k)^{1-2alpha}->+oo for alpha>1/2, confirmed numerically for alpha in {0.6,1.0}. (E) uses a prototype poloidal divergence-free bump W supported near (r,z)=(1,0) with max|W|=1, W_theta=0, scaled as v^{(k)}(r,z)=M_k W(r/r_k,z/r_k), preserving the axisymmetric divergence condition d_r(r v_r)+d_z(r v_z)=0 while attaining amplitude M_k at radius r_k with M=0; e.g. r_k=1/k, M_k=k^2 gives d_k=k->oo. The script also tabulates escape cases (r_k,M_k) in {(1e-2,1e3),(1e-3,1e5),(1e-4,1e8)} with d_k in {10,100,10000}.

## Limitations

Proved: identities (A)-(D), kinematic realizability (E), and computed verification. Not proved and not claimed: that Navier-Stokes dynamics realize the escape regime (test fields are kinematic, not solutions); that the target dichotomy is false (this obstructs the prescribed axis-centered method, not the statement); the full conditional extraction under bounded d_k (stated as a corollary direction, not a closed theorem). No regularity breakthrough is claimed.

## Reproducibility

Run python3 output/artifacts/scaling_check.py (requires sympy): part (a) asserts on-axis Gamma invariance symbolically; part (b) prints the off-axis formula; part (c) prints window exponents; part (d) prints the ring-escape table. Full self-contained proofs are in the draft sections 2-3 with a proved-versus-unproved separation.

## References

Caffarelli-Kohn-Nirenberg partial regularity and epsilon-regularity; Kenig-Koch concentration-compactness/rigidity for Navier-Stokes critical elements; Gerard/Gallagher-Koch-Planchon L^3 profile decomposition; Seregin-type local regularity away from the axis; Aubin-Lions compactness and Duhamel mild-solution passage. Nearest priors inspected and found non-covering: Chen-Strain-Tsai-Yau (2008) blow-up rate; Gallagher-Koch-Planchon (2012) profile decomposition; Kenig-Koch (2010) critical spaces; Hou (2025) generalized axisymmetric blowup; Shahmurov (2026) swirl critical structure.
