# Independent mathematical audit

## correctness

PASS

For Haar-uniform sphere normals the axial dot product is uniform on [−1,1], so its absolute value t is uniform. Independently from the projected convex-hull derivation, the Cauchy surface integral gives normalized brightness πt/2 + (1/4)∫_0^{2π}|t+k√(1−t²)cosφ| dφ: the base contributes the first term and the side normal has axial component 1/√(1+k²), radial component k/√(1+k²), and uniform azimuthal area. For t≥t₀ the integrand is nonnegative before taking the absolute value; otherwise the negative azimuthal interval has length 2β. Evaluating gives exactly πt+√(k²−(1+k²)t²)−tβ, and the endpoint values are k and π. Differentiation gives B′=π−β−(k²/2)sin(2β), approaching π at the join. The zero condition is H(β)=k² with H=2(π−β)/sin(2β), decreasing up to π/4 and diverging at both ends. Beyond π/4, its only stationary point solves tan(2β)+2(π−β)=0, whose left and right limits are −∞ and π and whose derivative is 2tan²(2β)>0. The minimum is unique and nondegenerate: at the threshold, B′=B″=0 and D=B‴=2k_*²sin(2β_*)[β′(t_c)]²>0. Independent bisection gives k_*=2.145539290889752. Thus monotonicity persists at the cusp, and the two supercritical simple critical coordinates have sign pattern +,−,+, yielding distinct critical values. Uniform input and branchwise change of variable give the cubic density coefficient (6/D)^(1/3)/3 on both sides and the quadratic coefficient √(2/|B″|) on the locally attained side. Other regular branches contribute bounded terms even if an area equals an endpoint value. The cusp is an interior value; a supercritical local extremum may be at the edge of the full support, and its local formula still applies on its attained side. The two roots count inclination coordinates, not viewing normals. No atoms arise from the finite strictly monotone branches. The polygon/quadrature checker was inspected, not run, and the calculation does not claim full numerical or formal certification.

## originality

PASS

The projected-area formula is classical and excluded from the new claim, as are the generic Taylor inversion exponents in isolation. The supported distinct result is the global sharp threshold analysis for this cone profile and its Haar-pushforward density classification. The closest indexed record repeats the exact lower threshold and onset but is dated October 25, after the frozen October 18 record, and uses that threshold as background for a different global-maximizer switch. Its uncited reference to existing work does not resolve the antecedent. The older Pennell–Deignan paper is the main plausible priority risk: retrieval did not give its full text, so absence of the bifurcation in it has not been established. The pass is limited to the distinct content supported by the actual comparisons.

## value

PASS

The profile is a natural geometric observation with a precise change from a globally invertible inclination statistic to a multibranch one. Determining when this happens for all aspects and resolving the change in singularity from a cubic cusp to two quadratic folds are useful exact distributional information. This is not merely rederiving an area formula or its mean; no noisy-data inference or general cone theorem is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
