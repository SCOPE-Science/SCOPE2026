# A sharp three-radius design for joint seismic depth, wave-speed and origin-time recovery

## Finding

Consider an ideal seismic impulse in a homogeneous isotropic half-space, and noiseless direct-wave arrival times at surface receivers. Both source origin time and propagation speed are unknown, as are the two epicentral coordinates and positive hypocentral depth. A ring-based receiver layout has a sharp radial-diversity boundary:

1. **One circle is intrinsically ambiguous.** Arbitrarily many receivers on one circle cannot uniquely determine source position, depth, wave speed and origin time. Even for an off-centre source there is a nonconstant one-parameter family preserving every direct arrival. The same ambiguity persists when several seismic phases are available but all their speeds are uncalibrated.
2. **Two radii are insufficient for universal recovery.** Any array consisting of arbitrarily many receivers on one circle and receivers only at one additional distance from its centre fails to identify sources directly beneath the centre, even if there are arbitrarily many receivers at both radii.
3. **Seven explicit stations suffice globally.** Five *distinct* stations anywhere on a circle of positive radius, together with one station at each of two distinct, different radii from that circle's centre, uniquely identify all five parameters for **every** source with positive depth. No generic-position exception, prior speed calibration or known origin time is needed. Reconstruction is a five-unknown linear solve followed by elementary algebra.

The sharpness is within this ring-based geometry: two radial levels never suffice globally, whereas three levels with five azimuthally distinct stations at one radius always suffice. No claim is made that seven is the global minimum over every possible planar array.

## Assumptions and scope

Translate the ring centre to the origin. Let the surface station locations be \(s_i=(s_{i1},s_{i2})\in\mathbb R^2\), and let the subsurface point source be \((x_1,x_2,-h)\), with \(h>0\). The homogeneous constant wave speed \(v>0\) and origin time \(\tau\in\mathbb R\) are unknown. The observed first-arrival time is exactly

\[
t_i=\tau+\frac{\sqrt{\lVert s_i-x\rVert^2+h^2}}{v},\qquad x=(x_1,x_2).
\]

No refraction, multiple ray paths, phase-picking noise, anisotropy, finite-fault effects or station clock offsets are included. Source depths are strictly positive, and receiver positions are known in fixed distance units. The theorem is global *structural* identifiability from exact times, not a claim of numerical stability for noisy observations.

For the seven-station sufficiency statement, take any five distinct points on \(\lVert s\rVert=R>0\) and any two more points with respective radii \(R_1,R_2\ge0\), satisfying \(R_1\ne R_2\), \(R_1\ne R\), \(R_2\ne R\). The two extra azimuths are arbitrary. For example, one valid layout is

\[
(1,0),(0,1),(-1,0),(0,-1),(3/5,4/5),(0,0),(2,0).
\]

## Proof

**Step 1: exact linearization.** Set \(A=v^{-2}\), \(B=-2Ax\in\mathbb R^2\), and \(D=A(\lVert x\rVert^2+h^2)-\tau^2\). Squaring the arrival formula and rearranging yields the **linear** equation

\[
t_i^2=(2\tau)t_i+A\lVert s_i\rVert^2+B\cdot s_i+D.
\]

Thus the design matrix has rows

\[
\bigl(2t_i,\ \lVert s_i\rVert^2,\ s_{i1},\ s_{i2},\ 1\bigr).
\]

If this matrix has column rank five, its unique solution determines \(\tau,A,B,D\), followed by

\[
v=A^{-1/2},\qquad x=-\frac{B}{2A},\qquad h=\sqrt{\frac{D+\tau^2}{A}-\lVert x\rVert^2}.
\]

The positive square root is forced by \(h>0\).

**Step 2: the five-circle lemma.** Suppose a function of the form \(g(s)=\tau+v^{-1}\sqrt{C-2x\cdot s}\), with the radicand strictly positive on the radius-\(R\) circle, agreed with an affine function \(a+b\cdot s\) at five distinct points of that circle. Parametrize \(s=R(\cos\theta,\sin\theta)\) and square the alleged equality. The resulting difference is a real trigonometric polynomial of degree at most two, with at least five distinct zeros, hence is identically zero: multiplying by \(e^{2i\theta}\) produces an ordinary polynomial of degree at most four. The degree-two Fourier harmonics contributed by \((b\cdot s)^2\) vanish only when \(b=0\). Its first harmonics then force \(x=0\). Therefore, **for every noncentral hypocentre \(x\ne0\)**, its five circular arrival times cannot agree with *any* affine function of the surface position.

**Step 3: full rank for every noncentral source.** The columns \(1,s_{i1},s_{i2},\lVert s_i\rVert^2\) already have rank four: a linear combination vanishing at five points on a common circle first forces both coordinate coefficients to vanish and then, using an off-circle point, forces the remaining coefficients to vanish. If the arrival-time column belonged to their span, then on the five circular points it would be affine in \(s\), contrary to Step 2 when \(x\ne0\). Hence the full design has rank five.

**Step 4: the central source.** If \(x=0\), the time depends only on squared station radius \(z=\lVert s\rVert^2\) through \(\tau+v^{-1}\sqrt{z+h^2}\). Were the time column in the span of the four purely geometric columns, the five circular stations would force the coordinate coefficients to be zero. The data at the three distinct squared radii would then lie on a single affine line in \(z\). This is impossible because \(z\mapsto\sqrt{z+h^2}\) is *strictly concave* for \(h>0\). The full design therefore also has rank five at central sources. Steps 1–4 prove global uniqueness and reconstruction.

**Step 5: sharp two-radius obstruction.** Consider the central source \(x=0\). Every station at radius \(r\) has the same arrival time \(t(r)=\tau+v^{-1}\sqrt{h^2+r^2}\). If the array has only two distinct radii \(r_a\ne r_b\), the data supply only \(t(r_a)\) and \(t(r_b)\). Given any alternative \(h'>0\), the two equations determine a unique positive alternative slowness \(v'^{-1}\) and an alternative \(\tau'\), since \(\sqrt{h'^2+r_a^2}-\sqrt{h'^2+r_b^2}\) has the same nonzero sign as the observed time difference. Varying \(h'\) yields infinitely many indistinguishable parameter triples. With one radius, ambiguity is still greater.

**Step 6: the complete-ring gauge.** On \(\lVert s\rVert=R\), write \(u=v^{-1}\) and \(M=R^2+\lVert x\rVert^2+h^2\). For any \(\lambda>0\) sufficiently close to one, put

\[
u'=\lambda u,\quad x'=x/\lambda^2,\quad
h'^2=\frac{M}{\lambda^2}-R^2-\frac{\lVert x\rVert^2}{\lambda^4},\quad\tau'=\tau.
\]

Continuity and \(h>0\) ensure \(h'^2>0\) near \(\lambda=1\), and direct expansion gives

\[
u'^2\bigl(\lVert s-x'\rVert^2+h'^2\bigr)=u^2\bigl(\lVert s-x\rVert^2+h^2\bigr)
\]

for **every** point on the circle. For any collection of phases with unknown positive slownesses, multiply every phase slowness by the same \(\lambda\) and use the same \(x',h',\tau\); the complete multi-phase arrival records still agree. As an explicit noncentral witness on the unit circle, \((x,h,u) = ((1,0),2,1)\) and \((x',h',u')=((4,0),\sqrt7,1/2)\) yield the identical travel-time square \(6-2s_1\) at all positions.

## Verification

The accompanying standard-library script `check_ring_geometry.py` evaluates the two noncentral gauge configurations at 720 ring angles, inverts the exact five-parameter linearization for 1,500 seeded randomly generated positive-depth cases, and checks 15 central cases. It reports 8,296 successful consistency assertions. The finite tests do **not** prove global uniqueness; that rests on the five-zero trigonometric-polynomial lemma and strict concavity in the proof above. The explicit stations have exact rational surface coordinates and three distinct radii.

Run with `python3 check_ring_geometry.py` in a directory containing the script. No data files, external packages, stochastic inputs or network requests are needed.

## Relationship to prior work

Classic exact arrival-time localization methods, including Militello and Buenafuente (2007) and Buenafuente and Militello (2011), consider a calibrated, constant propagation speed and discuss receiver geometry. Annibale and Rabenstein (2012) investigate estimating propagation speed jointly with source location from time differences of arrival. Poliannikov and collaborators (2013) examine microseismic location with uncertainty in the velocity model, including unknown event origin times, while Valentine and Woodhouse (2010) examine joint seismic source/structure inversion.

The result here is a global noiseless **geometry-specific** statement for the simultaneous unknown depth, horizontal epicentre, origin time and absolute wave speed. Its distinguishing content is the exact noncentral circular gauge, a sharp two-versus-three-radial-level obstruction, and a finite **seven-station** design whose identifiability has no exceptional hypocentres. Neither the familiar linearization alone nor parameter counting gives this universal array guarantee. The cited literature motivates the inverse problem but historical priority for a possible equivalent specialized array theorem is not independently established.

## Limitations

Identifiability here is exact and noiseless; the condition number can deteriorate when source geometry approaches degeneracy or observation arrays cluster. No error bounds, Cramér–Rao performance, or robustness guarantee for real heterogeneous Earth structure is established. Station clock errors, unknown receiver coordinates, anisotropic or depth-dependent speeds, wave scattering and multipath arrivals fall outside the theorem. No claim is made that seven stations are necessary among arbitrary planar geometries. Prior work on sound-source localization with jointly estimated propagation speed may contain an equivalent specialized statement not retrievable in full text in this comparison.

## References

- C. Militello and S. R. Buenafuente, *An exact noniterative linear method for locating sources based on measuring receiver arrival times*, Journal of the Acoustical Society of America **121** (2007), 3595–3601. DOI: 10.1121/1.2724241.
- S. R. Buenafuente and C. M. Militello, *The Linear Method for Acoustical Source Localization (Constant Speed Localization Method): A Discussion of Receptor Geometries and Time Delay Accuracy for Robust Localization*, Advances in Sound Localization (2011), publicly dated 11 April 2011. DOI: 10.5772/14663.
- P. Annibale and R. Rabenstein, *Speed of sound and air temperature estimation using the TDOA-based localization framework*, ICASSP (2012), 229–232. DOI: 10.1109/ICASSP.2012.6287859.
- O. V. Poliannikov, M. Prange, A. Malcolm and H. Djikpesse, *A unified Bayesian framework for relative microseismic location*, Geophysical Journal International **194** (2013), 557–571, online 19 April 2013. DOI: 10.1093/gji/ggt119.
- A. P. Valentine and J. H. Woodhouse, *Reducing errors in seismic tomography: combined inversion for sources and structure*, Geophysical Journal International **180** (2010), 847–857, online 1 February 2010. DOI: 10.1111/j.1365-246X.2009.04452.x.
