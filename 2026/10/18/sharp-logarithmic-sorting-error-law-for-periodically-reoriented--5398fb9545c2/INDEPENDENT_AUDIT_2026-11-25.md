# Independent mathematical audit

## correctness

PASS

A constant factor with angular column (h/√c,√c) and translational columns (√κ I,0) has the same Gram matrix as the symmetric mobility square root and differs by a constant orthogonal noise rotation. The angular term is d(Rφu) in Stratonovich form, since Ju=h/c. The independent translational noise integral has zero quadratic covariation correction; conditional on the angular path it is Gaussian with deterministic covariance τI before rescaling, hence independent of that path. Increments on disjoint reset cycles are iid. Integrating the endpoint e-projection gives cos Θ−1, and tilting yields Λ(q)=εq²+log A_z(q) with A_z=e^−qB_z from the wrapped-normal Fourier coefficients. Λ′(0)<0, Λ″≥2ε>0 and Λ′ eventually positive since the angular variable is bounded. The optimal Chernoff upper bound is matched by tilting to zero mean: the tilted CLT gives nonvanishing probability for a sample mean in [0,δ], and undoing the tilt costs at most q*δ in the per-cycle exponent. For fixed z, scaling θ=v/√q in the wrapped integral and in its first derivative gives A_z∼H_z/√(2πq) and −A_z′/A_z∼1/(2q). Gaussian domination follows from 1−cos θ≥2θ²/π² on the integration interval; an even Taylor expansion of w_z and the phase gives the stated relative O_z(q^−1) corrections. The optimizer escapes every compact interval as ε→0 because −A_z′/A_z is strictly positive there, and 2εq*=−A_z′/A_z gives εq*²→1/4. Substitution yields 1/4 log(1/ε)−1/4−log(H_z/√π) per cycle, divided by τ per unit time. Opposite h reflects the full law, the moment identities follow from E cos(kΘ)=exp(−k²z), and at ε=0 the wrong-sign event has probability zero for n≥1 because each cosine equals one with probability zero. These arguments are analytical (RESULT.md Eqs. (6)–(12)); no uploaded script executed. They do not imply a joint-limit estimate, a rate for an anisotropic Schur complement, or an optimal decision rule beyond the specified displacement sign.

## originality

PASS

The distinct finding taken for this pass is the exact sign-error rate and its sharp fixed-z small-residual-noise asymptotic, including the optimizer and constant. Credit the parent model and mean drift, and do not count the standalone endpoint factorization as a new mechanism: it is a specialization of a broader exact decomposition in a distinct catalogue result, and is also directly obtainable from the parent dynamics. No inspected comparison supplies the model-specific rate and logarithmic asymptotic. This is a bounded assessment, not a priority assertion.

## value

PASS

The useful new quantity is the speed of decay of the misclassification probability for a specified protocol, which an average drift or effective diffusivity cannot predict. The logarithmic rather than inverse-noise rate, and its explicit constant, resolve the behavior near the one-sided noiseless boundary. The result is an idealized model guarantee, not an experimental design validation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
