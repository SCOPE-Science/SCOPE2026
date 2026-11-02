# A sharp one-step Riccati barrier and physical-energy defect in scaled-field SAV particle integration

## Finding

In the one-cell periodic, one-particle homogeneous mode of the charge- and modified-energy-preserving VA-II Strang PIC method of Fan, Crouseilles and Hu, the cold-start step has an **exact maximal positive-auxiliary existence interval**, even though the particle velocity and auxiliary energy stay bounded up to its boundary. At initial electric field \(e\ne0\), auxiliary offset \(C_0>0\), and \(R=\sqrt{C_0+e^2/2}\), define
\[
 y=\frac{h^2 e^2}{8R^2},\qquad h_*=\sqrt{\frac83}\,\frac{R}{|e|}.
\]
For every \(0<h<h_*\), all five stages of one full VA-II step exist in the positive-\(r\) domain, and its final velocity, auxiliary variable and physical grid field are
\[
 v_1=\frac{he}{1+y},\qquad r_1=R\frac{1-y}{1+y},\qquad E_1=e-\frac{h v_1}{2}.
\]
The physical energy **strictly increases** by the exact amount
\[
 \frac{v_1^2+E_1^2-e^2}{2}=
 \frac{C_0e^2h^4}{8R^2(1+y)^2}>0,
\]
while the modified total energy is conserved exactly:
\[
 \frac{v_1^2}{2}+r_1^2-C_0=\frac{e^2}{2}.
\]
The final scaled-field consistency error is exactly
\[
 r_1g_1-E_1=\frac{4ey^2}{(1+y)(1-3y)}.
\]
Consequently \(g_1\) diverges as \(h\uparrow h_*\), while \(v_1,r_1,E_1\) have finite limits. At \(h=h_*\), the final Riccati half-stage reaches its finite-time pole exactly at the endpoint; for \(h_*<h<\sqrt8R/|e|\) it reaches the pole before the endpoint. Hence \((0,h_*)\) is the **sharp interval connected to zero** of positive-\(r\), finite, real one-step VA-II execution for these cold-start data.

## Assumptions and scope

Use a unit-length periodic one-dimensional spatial domain, one periodic grid cell of width \(1\), one particle of weight \(1\), and periodized cardinal B-spline deposition satisfying the partition-of-unity property. The current deposited on this one-cell homogeneous mode is therefore the particle velocity. When depositing the full-step charge-conserving current, use the usual unwrapped (winding-aware) particle displacement, so the full-step integrated current equals the displacement. Take initial velocity \(v_0=0\), arbitrary initial position, spatially constant physical electric field \(E_0=e\in\mathbb R\setminus\{0\}\), auxiliary offset \(C_0>0\), auxiliary variable \(r_0=R=\sqrt{C_0+e^2/2}\), and scaled field \(g_0=e/R\).

The field is a permitted **nonzero constant/harmonic mode of the periodic Gauss-law constraint** (density \(\rho=1\), field gradient zero). The additional zero-mean potential-based Poisson initialization specified in the source paper would set this homogeneous field to zero; the present benchmark exercises admissible Gauss-law initial data with a nonzero mean field instead. It does not claim to arise from that particular zero-mean initialization.

The numerical method is specifically the source's VA-II scheme, equations (2.31)--(2.46): first half-step particle advection and scaled-field current subtraction, first half-step exact scalar Riccati evolution, a full velocity/auxiliary-variable implicit-midpoint step, a second half-step Riccati evolution, and final half-step advection/current subtraction. The physical \(E\) is updated independently by the full-step charge-conserving current. The theorem does not address VA-I, arbitrary multi-cell modes, other branches after leaving the positive-\(r\) domain, or unwrapped versus incorrectly wrapped deposition implementations.

## Proof

Write \(g=g_0=e/R\). During the first advection/current half-step the particle has zero velocity, so the current and displacement vanish and \(g,r,v\) do not change. The first Riccati half-step also acts trivially since its current is zero.

During the middle velocity/auxiliary step, the one-cell normalized discrete midpoint equations (source equations (2.40)--(2.43)) are
\[
 v_1=hg\frac{R+r_1}{2},\qquad
 r_1-R=-\frac{hg}{2}\frac{v_1}{2}.
\]
Consequently, with \(r_{\rm mid}=(R+r_1)/2\),
\[
 r_{\rm mid}=\frac{R}{1+h^2g^2/8}=\frac{R}{1+y},\quad
 v_1=\frac{he}{1+y},\quad
 r_1=\frac{R(1-y)}{1+y}.
\]
These equations also immediately show \(\frac12v_1^2+r_1^2=R^2\): expand the squared midpoint equations, or multiply the first by the midpoint velocity and the second by twice the midpoint auxiliary variable and add. For \(0<y<1\), both \(r_1\) and \(r_{\rm mid}\) are positive.

In the second Riccati half-step, the velocity is frozen at \(v_1\), the auxiliary variable at \(r_1\), and the scalar scaled field satisfies \(\dot g=(v_1/(2r_1))g^2\). Its exact solution from \(g(0)=e/R\) is
\[
 g(\tau)=\frac{e/R}{1-\tau(e/R)v_1/(2r_1)}.
\]
At \(\tau=h/2\), direct substitution gives \(h(e/R)v_1/(4r_1)=h^2e^2/[4R^2(1-y)]=2y/(1-y)\) and hence the exact endpoint denominator
\[
 \boxed{\Delta_2=1-\frac{h(e/R)v_1}{4r_1}=\frac{1-3y}{1-y}.}
\]
In particular, the Riccati half-step exists for its full positive time interval exactly when \(y<1/3\) within \(0<y<1\). For \(1/3\le y<1\), its finite-time singularity occurs at \(\tau_*=2r_1/((e/R)v_1)\le h/2\), while \(r_1>0\). The sharp step threshold is therefore \(h_*=\sqrt{8/3}\,R/|e|\); the pole cannot be avoided by the later advection stage.

For \(0<y<1/3\), the scaled field immediately after the second Riccati stage is
\[
 g_{\rm Ric}=\frac{e}{R}\frac{1-y}{1-3y}.
\]
The final advection half-step moves the particle by \(h v_1/2\) and subtracts its deposited current divided by \(r_1\), giving
\[
 g_1=\frac{e}{R}\frac{1-y}{1-3y}-\frac{h v_1}{2r_1}.
\]
In one periodic cell, the accumulated charge-conserving current over both half-advective stages equals the net (unwrapped) displacement \(h v_1/2\); the independent Ampère update is therefore
\[
 E_1=e-\frac{h v_1}{2}.
\]
Substitution of these three exact updates and \(h^2e^2=8R^2y\) gives
\[
 r_1g_1-E_1
 =e\left[\frac{(1-y)^2}{(1+y)(1-3y)}-1\right]
 =\frac{4ey^2}{(1+y)(1-3y)}.
\]
Finally, direct expansion of \((v_1^2+E_1^2-e^2)/2\), followed by \(R^2-e^2/2=C_0\), gives
\[
 \frac{v_1^2+E_1^2-e^2}{2}
 =\frac{C_0e^2h^4}{8R^2(1+y)^2}.
\]
This is positive for all stipulated data and steps. As \(y\uparrow1/3\), the last Riccati denominator tends to zero while \(r_1=R/2\), \(v_1=3he/4\), and \(E_1\) remain finite. Because the Riccati field has nonzero initial value and strictly positive growth coefficient \((e/R)v_1/(2r_1)>0\), its divergence is genuine, not removable by cancellation.

## Verification

Run `python3 verify.py` from the directory containing the supplied checker. The standalone checker independently constructs the midpoint updates, solves the Riccati endpoint denominator, evaluates the independent Ampère update and verifies all closed-form identities with Python exact rational arithmetic. It also checks that the Riccati pole time lies inside the second half-step when \(1/3\le y<1\). It includes fixed examples and seeded rational data. These finite checks support the algebra but cannot establish the continuous-parameter theorem by themselves.

## Relationship to prior work

Fan, Crouseilles and Hu (2026, arXiv:2610.16028v1), Section 2.3, introduce VA-II and give its exact Riccati subflow (2.39), midpoint update (2.43), symmetric composition (2.44), and separate physical field update (2.45)--(2.46). Their Proposition 2.2 proves modified-energy and charge preservation. This finding **does not claim** those formulas, the method, or preservation as new. It composes them on a cold homogeneous Gauss-law mode to identify a **sharp complete-step singularity threshold**, and obtains the exact physical-energy and scaled-field consistency defects, which are not stated in that source.

Crouseilles, Liu and Yue (2026), *Semi-Lagrangian SAV method for Vlasov--Maxwell equations*, study an earlier SAV Vlasov framework and its conservation properties with a different semi-Lagrangian update. Its Gauss/energy balance does not directly imply this VA-II PIC composition formula or the exact cold-start Riccati pole. General SAV literature already distinguishes modified from physical energies; the contribution here is the explicit positive defect and resonance in this precise five-stage map, not that general distinction. Historical priority beyond the inspected sources remains uncertain.

## Limitations

This is a one-step exact-arithmetic result in the one-cell, one-particle homogeneous invariant sector, with nonzero mean electric field and winding-aware periodic deposition. It is a rigorous counterexample to unconditional positive-domain well-posedness of that scheme, **not** a claim of blow-up in the underlying Vlasov--Ampère dynamics. No instability or physical-energy growth rate beyond one step is asserted. The threshold concerns the branch connected to sufficiently small positive timesteps; possible nonphysical signed-auxiliary algebraic continuations are not classified. The source's zero-mean potential-based initialization cannot produce the chosen nonzero constant field. Uniform spatial tests with nonzero constant-field mean are necessary to exercise this benchmark. An independent mathematical audit has not been conducted.

## References

1. C. Fan, N. Crouseilles and J. Hu, *Explicit charge-conserving and modified energy-conserving PIC methods using the SAV approach*, arXiv:2610.16028v1, first posted 2026-10-12, Sections 2.1 and 2.3, especially equations (2.31)--(2.46). https://arxiv.org/abs/2610.16028
2. N. Crouseilles, X. Liu and X. Yue, *Semi-Lagrangian SAV method for Vlasov--Maxwell equations*, Journal of Computational Physics (2026), available author manuscript, Sections 2.2--2.3. https://lirias.kuleuven.be/retrieve/50e8d678-ecc1-4287-b2ad-6c7dbd5a27e8
