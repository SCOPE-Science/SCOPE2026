# Independent mathematical audit

## correctness

PASS

Reconstructed the exact stages after setting U=(sqrt(r),0) by rotational equivariance. With t=h(a+br), q=br/(a+br), and s=t^2, the normalized second-stage frequency is B=1+qs/4 and the third-stage coordinates are (1-sB/2,-tB). Its normalized frequency is C=1+q[-sB+sB^2+s^2B^2/4]. Expanding X=1-sB(1+C)/4 and -Y/t=(1+2B+C(1-sB/2))/4 in X^2+Y^2 gives zero coefficients at s,s^2; the s^3,s^4,s^5 coefficients are (q+1)^2/64, -q(q+1)(2q+1)/128, q(9q+8)/1024. Evenness follows directly from X even and Y odd in t. Thus the generic r-increment is r(a+br)^4(a+2br)^2 h^6/64, and its unique nonstationary positive-radius cancellation q=-1 leaves r_star H^10/1024. Energy is r/2, so actual energy defects are half the radial increments; these are local errors of orders five and nine in the stated convention, not orders of the full state method. If a+br=0 all stages vanish. In the bounded layer r/r_star=1+H^2 y the three displayed polynomial coefficients contribute H^10 times y^2/16, y/64, 1/1024, respectively; omitted terms are uniformly O(H^12) since the denominator stays away from zero. Dividing by H^2 gives an Euler recurrence of step H^8 with O(H^10) residual. The exact Riccati solution is tau/(1024-8 tau); on every compact pre-pole interval the bounded Lipschitz Euler comparison accumulates O_T(H^2) and closes the bounded-layer bootstrap. Physical time scales as h^-7, with no claim of a discrete blow-up or accuracy at the pole. Inspected frozen verify.py and VERIFICATION.md but did not run the submitted code; the coefficient and uniform-error reasoning were checked analytically, not inferred from the floating-point demonstrations.

## originality

PASS

Best-of-knowledge pass for the unique nonstationary higher-order cancellation and the proved slow-time limit. The same tableau, general amplitude-dependent nonlinear setting, and generic fifth-order energy analysis were already in Liu–Brio v2, dated 2026-05-10 UTC by its arXiv version record; v1 dated 2024-05-08 UTC is linear. A specific cubic example in v2 is also prior; the residual claim goes beyond all of these, not merely to a new application of the same tableau.

## value

PASS

The radius is selected by an intrinsic zero of the generic drift, not an arbitrary convenient test amplitude. At that zero the order gain and its lifetime are different questions: the error drives the orbit off the exceptional amplitude, and the matched detuning law gives a quantitative duration and shape of that departure. This is a meaningful invariant-accuracy diagnostic for a known integrator and a natural oscillator, beyond recomputing a generic order coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
