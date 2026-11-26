# Independent mathematical audit

## correctness

PASS

Translate by the fixed center and write the periodic displacement as u. For β>0 the filtered position z_β is C¹ and periodic, and z′_β=u−βz_β by integration by parts and boundedness. Integrating u·z′_β over a period therefore gives ∫|z′_β|²; if this vanishes then z_β is constant and u=βz_β is constant. The exchange with μ is valid already on the mixed product, bounded after time integration by T‖u‖∞‖u′‖∞/β; no unstated β^{-2} integrability is needed. For a nonconstant trajectory each μ-integrand after period averaging is strictly positive and μ is nonzero. The chord contribution has pointwise radial product |u(t)−u(t−s)|²/2 because the radii agree, so nonnegative κ,w,a make it nonnegative (and a is bounded on the chord range). The left hand side has zero radial product, ruling out the periodic trajectory, including arbitrary speed or plane of motion. For the witness, e^{-iτ}=(-1+3i)/sqrt(10), giving i m̂(i)=(-2+i)/5; 4(∫w−ŵ(i))=(2+4i)/5, so the net coefficient is i. The delayed mass sqrt(10)/5 is strictly between zero and one. The flat splice at r=1 gives a smooth a, with Gaussian-scale decay at infinity; near the origin Φ is a constant minus |z|²/2. The profile is positive and strictly radially decreasing and its outward negative gradient is a(|z|)z. For every 0<R≤1/2 all chords use a=1, so these are exact full-history circles; at R=0 only the constant solution occurs. Replay: RESULT.md lines 43–90, with checks/check.py and VERIFICATION.md inspected but not executed. No statement about orbital stability, arbitrary periodic orbits off a fixed sphere, or state-adaptive age weights is proved.

## originality

PASS

The supported distinction is the whole-fixed-sphere rigidity versus explicit positive delayed-kernel circle in the prescribed subclass. The model and generic filter positivity have antecedents; the comparison does not assign priority for either. Inspected relevant statements do not give the coupled spherical theorem or the witness with this first-order unconfined model.

## value

PASS

The result gives an invariant-set obstruction for arbitrary periodic motion on a sphere, not just for a harmonic ansatz. The explicit full-history witness shows the obstruction can disappear under a positive, subunit-mass kernel when the shape changes, with a smooth bounded strictly decreasing potential and an entire interval of circular radii. This is a motivated boundary on admissible memory classes, independent of numerical orbit detection or any unproved stability claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
