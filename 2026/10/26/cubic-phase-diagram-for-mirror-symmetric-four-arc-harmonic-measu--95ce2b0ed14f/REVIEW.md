# Independent mathematical audit

## correctness

PASS

For each reflected pair of arcs, integrating the Fourier coefficient of the indicator gives analytic derivative (4/π)Σ_{n≥1} sin(nδ)cos(nθ)z^(n−1). Summing the geometric series gives numerator Nθ=cosθ(1+z²)−2cz over Qθ, the product of the two quadratic endpoint factors, with the stated prefactor. Adding the pairs gives P=N_a Q_b+N_b Q_a. At an endpoint of the θ-pair, Nθ=−2z sinθ sin(θ±δ)≠0, while Q for the other pair is nonzero. At any non-endpoint boundary point with value 0, the Poisson integral divided by 1−r on the radial approach tends to a strictly positive integral of 2/|e^{iφ}−e^{iθ}|² over the arcs (with normalized angular measure); where the boundary value is 1 use 1−u and the complement instead. Thus there is no unit-circle root of P. The reciprocal identity z⁶P(1/z)=P(z) implies exactly three interior zeros with multiplicity, even when there is a zero at the origin: if its order is m, the degree is 6−m and the remaining 6−2m zeros pair by inversion. Substituting t=z+1/z reduces Qθ/z² to t²−4c cosθ t+4(cos²θ+c²−1) and Nθ/z to cosθ t−2c. The resulting cubic is exactly H. When A+B≠0 there is no zero at the origin and every t outside [−2,2] has a unique inverse strictly inside the disk with nonzero derivative of the forward map. A root in [−2,2] would produce a circle root. Therefore the ordinary real discriminant gives precisely the claimed real versus conjugate-pair alternatives and a real repeated root at zero discriminant. Independent exact integer discriminants: 500H has coefficients (25,360,83,−2961) and (25,−612,110,−1017) for the two witnesses. Dividing their discriminants by 500⁴ gives respectively 14626551073/2500000000 and −914716481579/62500000000. Along A=1/20−B, 3/5≤B≤4/5, the gap a−b increases with B, while b>δ and a<π−δ throughout. At its minimum cos(a−b)=−0.33+0.8√0.6975<0.62=cos(2δ). Hence the sign-changing segment remains admissible and nonantipodal. For a+b=π the boundary indicator is the pullback via w=z² of the two arcs centered at ±2b with half-width 2δ; uniqueness of the harmonic extension gives the same pullback inside. The two-arc derivative has one interior zero solving cos(2b)(1+w²)=2 cos(2δ)w, with |cos(2b)|<cos(2δ). The small root has the stated magnitude and sign; z²=w lifts it and differentiation adds a zero at 0. At b=π/4 that root is simple at w=0 and the pullback derivative has order three at z=0. Thus the imaginary-axis transition applies only to the antipodal subfamily. Replay: RESULT.md lines 29–75 and the scaled integral cubics above. check.py and check_output.txt were inspected, not executed; the Fourier tests use one interior location in two geometries, not two distinct points. Those checks illustrate the formulas rather than replace the proof.

## originality

PASS

Best-of-knowledge pass for the explicit equal-width reflected four-arc phase diagram: reduction to a cubic in the geometric parameters, discrimination of real and nonreal phases with a verified nonantipodal collision, and a separate exact antipodal formula. The ordinary Poisson derivative, reciprocal root counting and general critical-point location framework are not credited as new. The leading-coefficient exception must not be evaluated by the cubic test. The inaccessible Walsh texts leave a specific historical risk, not affirmative coverage or clearance.

## value

PASS

For the natural equal-width symmetric family the exact classification identifies when all interior saddles remain on the reflection diameter, when a conjugate pair leaves it, and how collisions can occur. The discriminant has realizable strict phases with a collision in the nondegenerate admissible region, rather than merely giving a generic upper bound on the number of critical points. The antipodal formula gives an exact benchmark and isolates a width-independent triple collision. These are useful geometry and decision criteria, not a claim about all level sets or general nonsymmetric four-arc configurations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
