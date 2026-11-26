# Independent mathematical audit

## correctness

PASS

The antipodal matching contributes g(I−Sⁿ), not 2g(I−Sⁿ). Fourier diagonalization reduces λ_k to 2−2cos(πk/n)+g(1−(−1)^k). Representatives 0 and n are single, the others pair with 2n−k; monotonicity on k=0,…,n forbids within-parity collisions, and g>0 excludes the endpoint 0 and collision with an odd endpoint n. Thus C₄ and C₃ count distinct spectral blocks, even if their rates coincide. Spectral projections are polynomials of degree less than 2n in L, so the reachable space is the direct sum of their input projections. Consecutive coordinate restrictions are Vandermonde on distinct Fourier roots, rank min(q,m) for block dimension m, with no change after complexification. This proves both the fixed-pair deficit and multiplicity lower bound with attaining consecutive inputs; k=1 guarantees a double mode in the absence of collisions. For each allowed even e the least collision rate is attained uniquely at o=e−1, with rate 2sin((e−½)π/n)sin(π/2n). For even n, e=n is uniquely closest to an endpoint in this sine comparison, including n=2. For odd n the two extremal allowed indices e=2 and e=n−1 are equally close and give distinct fourfold blocks unless n=3 where they are the same. No non-neighbor odd representative can tie the overall minimum since its own adjacent rate is strictly smaller. The deficits at the first resonance are consequently 1, 2, 4 for even n, n=3, and odd n≥5 respectively. Replay: RESULT.md Fourier/PBH and extremal-sine proof; VERIFICATION.md and verify.py were inspected, not executed. The recorded checks use numerical tolerances except for three rational examples, and cannot settle equality for arbitrary real g.

## originality

PASS

Credit existing maximum-multiplicity and weighted-circulant minimum-leader results. The supported distinct contribution is the explicit conductance-dependent loss for the fixed adjacent pair, and the first positive rate with the exact parity-dependent multiplicity of simultaneous losses. Comparing actual analogous ladder and wheel findings does not yield those thresholds for this antipodally matched cycle.

## value

PASS

For one natural weighted graph family the result predicts every exact rank loss of a specified control placement. It distinguishes coincident losses at different eigenvalues from maximum multiplicity; the first conductance at which two controls fail can cost four dimensions although only four controls in total are necessary. The even/odd threshold and exceptional six-vertex case are structural, not fitted examples. It gives neither robustness near resonances nor bounds on control energy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
