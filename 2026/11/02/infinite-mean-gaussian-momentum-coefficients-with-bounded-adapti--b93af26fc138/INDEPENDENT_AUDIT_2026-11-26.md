# Independent mathematical audit

## correctness

PASS

Algorithm 2 initialized with relaxation one gives x¹=(I−P_s)x⁰; Algorithm 3 uses uncapped Eq. (17) at k=1. For n≥2, d=x¹−x⁰ and x¹ are nonzero a.s.; conditionally on s, the second sketch z has nonzero component along x¹ and nonzero projection off d a.s., so the algorithm does not reject and its Gram determinant is nonzero. In the frame e=d/||d||, v=x¹/||x¹|| write z=Ze+W, U=W·v, R=||W||. Minimizing ||x¹−αg+βd||² first over β cancels the e-component, and then minimizing off e gives α=1/R² and β=(||x¹||/||d||)ZU/R². Conditionally on s the scalar law of (Z,R,T=U/R) is fixed, with independent Gaussian, chi_(n−1), and sphere-coordinate factors. These scalars, not necessarily the embedded vector W, are independent of the first-sketch ratio; this is the precise moving-frame reading needed for RESULT.md line 75. That ratio is χ_(n−1)/|G₀| for independent factors. The gamma-density integral for R^-2p gives the stated step moments, finite exactly for p<(n−1)/2. In the β moment multiply the chi moment and inverse-chi moment with the sphere-coordinate moment and the two one-dimensional normal moments: the powers of two and Γ((n−1+p)/2) cancel, leaving exactly the stated gamma quotient. Tonelli gives divergence for p≥1 from |G₀|^−p and symmetry gives no signed mean. For n=2 the two absolute Cauchy ratios are independent and each has square-root moment √2. Finally the remaining update is projection off W after projection off s; their orthogonality gives the two-plane complement. The mean of its rotationally invariant projector has trace n−2 and equals (n−2)I/n. Independent basic projections multiply the squared-error factor (n−1)/n twice, giving the difference ||x⁰||²/n². This was checked analytically; the supplied simulation is not evidence for divergent moments or numerical stability.

## originality

PASS

The exact coefficient laws and integrability thresholds for the published two-step adaptive update are the distinct claim on the inspected evidence. The projection interpretation and general error comparison are already in the original method paper; the exact two-step Gaussian error is a specialization, not an independent novelty claim.

## value

PASS

The exact laws give separate diagnostic thresholds for coefficients of a real adaptive algorithm, rather than an arbitrary scalar statistic. A raw momentum average is not integrable at any dimension despite an exactly bounded improving iterate. The first-sketch denominator and cancellation explain why iterate-error guarantees alone cannot control coefficient moments. This does not demonstrate finite-precision instability or a long-run effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
