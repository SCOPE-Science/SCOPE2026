# Independent mathematical audit

## correctness

PASS

In the eigenbasis the normalized Gaussian direction has uniform angle and z=d/λ=cos(2θ), with arcsine law. A²=λ²I gives normalized squared loss 2−z²+(w−z)² for w=λψ, including the oracle unique almost surely with mean 3/2. With w=z/(z²+x²), tangent substitution gives J=E[(z²+x²)⁻¹]=1/(x√(1+x²)); the linear term uses 1−x²J, and the quadratic term J+xJ′/2 (differentiate locally for x>0). The resulting derivative has numerator 4x⁴−1 and strictly positive denominator 2x²(1+x²)^(5/2); x=1/√2 is the unique global minimum, giving 8√3/9. For cutoff the retained loss is z⁻² versus rejection loss 2. Pointwise choice gives the threshold 1/√2 and the continuous positive density on |z|∈(0,1) makes it unique even when allowing thresholds ≥1. Arcsine integration gives 1+2/π, strictly above the ridge optimum. Without regularization the error is λ/|z|, giving the stated survival law even at t=λ and exactly the finite positive moments p<1. All risk values scale by λ². The frozen verifier was inspected, not executed; quadrature is confirmatory and its five tail checks test only the formula's range, not the law.

## originality

PASS

The distinct contribution is the exact normalized, balanced indefinite scalar-core squared-loss tradeoff and the resulting optimal ridge versus optimal hard cutoff comparison. The deterministic indefinite blow-up mechanism is prior, and the angular law and quadratic completion are classical ingredients.

## value

PASS

This is a natural minimal indefinite example with a singular scalar core, rather than an arbitrary tuning slice. Under the same one-column information, it locates the best finite-risk choices and separates ridge, hard cutoff, the scalar oracle, and the infinite-risk plain inverse. The quantitative gap is useful as a benchmark for handling this singularity, not a stability, confidence, or dominance guarantee for general sketches or matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
