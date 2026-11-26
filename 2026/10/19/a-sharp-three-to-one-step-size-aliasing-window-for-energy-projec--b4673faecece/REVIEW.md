# Independent mathematical audit

## correctness

PASS

Identify the plane with C. The step is multiplication by P_m(iz)/|P_m(iz)|; the stage-chain weights telescope to Taylor's coefficients, and stages one and two span the plane for m≥2. For m=1,2 the imaginary part is positive; at the only positive imaginary-part zero for m=3,4 the real parts are −2 and −1/2; for m=5 the imaginary part is z[(z²−10)²+20]/120. The continuous phase derivative numerator is Re(conj(P_m(iz))P_(m−1)(iz)); independent rational convolution in /workspace/check_frozen_math.py reproduces all five polynomials. For m=4 the minimum of x³−6x²+144 on x≥0 is 112, so all phases up to degree four are strictly increasing and their limits are at most 2π, never attained. For degree five F'(x)=4x²(x−12), and the two disjoint exact brackets (6,7) and (15,16) give the only positive phase turning points. The real part is respectively negative and positive there; the upper-half-plane phase tends to 0 at zero and π/2 from below at infinity. The three open monotonicity intervals have phase images (0,max), (min,max), and (min,π/2). Adding each finite critical step once gives the claimed counts, including two (not three) at π/2. Multiplication by a unit complex number preserves energy, and within (0,π) identical rotations entail identical angles. The frozen support was inspected, not executed; the independent script checks finite algebra and diagnostics, not the universal conclusion by sampling.

## originality

PASS

The known projection and phase-lag frameworks already give the normalized-amplification interpretation and the conservation mechanism. The supported distinction is the sharp all-positive-step inverse-multiplicity law for the Taylor polynomials, including the degree cutoff. The closest retrieved projection/dispersion paper uses different projection directions and a local dispersion-order question, despite using a Taylor cubic predictor for one method.

## value

PASS

The step-size identification question is intrinsic to exactly energy-normalized oscillator propagation. Degree five is the first failure and permits three distinct finite steps for the same projected map without any phase wrapping. The entire interval, turning points and boundary counts form a useful exact benchmark separating invariant preservation from phase identifiability. The independently useful feature is the global classification, not the textbook unit-modulus projection identity, and it need not promise accurate elapsed-time integration at those unrestricted steps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
