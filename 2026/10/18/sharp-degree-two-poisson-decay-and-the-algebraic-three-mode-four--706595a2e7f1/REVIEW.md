# Independent mathematical audit

## correctness

PASS

For bandwidth two the normalized operator is the convex combination with weights (1+r)/2 and (1−r)/2 of the identity and the negative half-turn; the first characters give equality, even for p=1 and infinity. For the cubic, multiply by ζ and write w=ζ², t=r². The coefficients of (1+w−εt w²)^2 are 1, 2, 1−2εt, −2εt, ε²t²; their squared norms give exactly the difference (1−t)[4ε−8ε²(1+t)−ε⁴(1+t+t²+t³)], bracket ≥599/2500 for ε=1/10. For the limiting projection, Parseval of the square shows the sole phase term is 4 Re(ac conjugate(b)^2). Any zero coefficient gives ratio ≤1, and compactness on a coefficient sphere plus the witness yields an interior optimum. At fixed magnitudes the maximizing phase is antialignment; scale and rotation give xζ⁻¹+ζ−yζ³ with x,y>0. Independent elimination replay: put u=y² and w=x/y. With N=x⁴+4x²+1 and Δ=D−N, divide the x stationarity equation (Δ_x N−Δ N_x) by 4y. After substitution it is B=u³(−2w⁵−w³)+u²(3w⁴−4w³−2w)+u(4w²−6w)−1=0; the y derivative is A=2uw²−w+u+2=0. Exact division of B by A in w gives remainder −(Cw+E)/(4u), with C=4u³+20u²+2u−1 and E=−2u³−2u²+9u+2. Substitute w=−E/C into A: its cleared numerator is 4u times the stated sextic. The sextic is strictly increasing for u>0, and evaluations at 49/1000 and 51/1000 have opposite signs. On this bracket C<0, so existence and the necessary conditions identify the unique magnitudes. Independent evaluation gives u≈0.04995333523717872, x≈0.6429606224569812, y≈0.2235024278104798 and K≈1.02744398345308878024. The finite-radius error in operator norm is at most r² by the norm-one Fourier coefficient bound on probability-normalized Haar measure. The frozen checker was inspected, not run.

## originality

PASS

The distinct contribution supported is the sharp L4-to-L4 bandwidth boundary with an all-radius witness, and the exact three-character restricted projection norm including its phase orbit. Closest sources use an L∞ or coefficient L2 input, an unnormalized sharp frequency cutoff, or a different extremand on the same progression. The fourth-moment collision formula is standard and is not itself new.

## value

PASS

A proposed stronger spectral-gap route to the complex Poisson fourth-norm endpoint has a smallest possible bandwidth at which it breaks. The all-radius witness demonstrates that this is not just an endpoint artifact. The arithmetic progression supporting the first cubic cancellation gives a natural finite subproblem; the sharp algebraic size and complete extremal phase orbit separate qualitative failure from its exact magnitude there.

The dated certificate retains the supplied scientific assessment, sources and limitations.
