# Independent mathematical audit

## correctness

PASS

The skew saddle gradient is J(x,y)=(-y,x), also the matrix used by the frozen checker; some row separators in the prose are malformed but do not change the identified update. The original RCOG formula realizes it by η_i=t, γ_i=g and p_i=1/2 in the paper's notation (its γ_i is a ratio). Expanding conditionally and using E P_i=I/2 gives the four-moment recurrence. For an independent elimination, scale the cross moment c by 1/t and use U,V,W,B for the normalized generating functions of u,v,w,c/t. Then W=1+zU, B=z(−U+gV), (1−sg²z²)V=1+(z−sgz²)U; substituting these into the u recurrence gives the stated N and D, with D the reversed characteristic polynomial. Independently verified by exact rational arithmetic: the five scaled Cayley coefficients and both scaled Hurwitz determinants have nonnegative polynomial coefficients and are strictly positive for r>0; their leading coefficients at the critical s are positive except for the constant Cayley term, which vanishes there. Hence at s=s₀ the transformed polynomial has a simple zero at w=0 and a strictly Hurwitz remaining cubic; the leading Cayley coefficient excludes λ=−1. A 7×7 Sylvester determinant of degree at most fourteen in s matches the displayed resultant at fifteen exact points, proving the polynomial identity. For s>s₀, D(0)>0>D(1), and the resultant excludes cancellation of a root in (0,1); Cauchy–Hadamard then gives a root limsup >1. At equality, the simple-pole contribution is −N(1)/D′(1)=1089/3217 and other modes decay. At t=3/4 the two exact complex Schur inequalities hold; 9/16>s₀. Normalization removes dependence on the direction of each nonzero deterministic cold start.

## originality

PASS

The algorithm, standard moment-lift/Schur tools, and the general phenomenon of mean versus second-moment separation are not new. The supported distinct claim is the evaluated sharp frontier, nonzero boundary residue for the algorithm's initialization, and exact separation witness in this particular iid coordinate saddle dynamics.

## value

PASS

A smallest two-block skew saddle is a natural test of whether deterministic mean dynamics diagnoses second-moment behavior of optimistic randomized coordination. The explicit parameter witness makes that diagnosis fail even with the prescribed cold start; evaluating the whole step frontier at that ratio and its boundary bias in the second moment supplies a sharp calibration for convergence analyses rather than a single numerical eigenvalue estimate. The motivation is the stability distinction and transition, not the intrinsic significance of the rational numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
