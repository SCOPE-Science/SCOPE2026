# Independent mathematical audit

## correctness

PASS

The exact finite-n Gaussian cell mass is q_c(z)=∫_{z+(2c−1)/√n}^{z+(2c+1)/√n}φ(u)du. Shifting s=z+2c/√n gives ∂²_s log q_c=−1+Var_s(T)<0 because T has nondegenerate tilted support [−1/√n,1/√n], so the binomial expectation of −log q_c is strictly convex; binomial reflection makes it even, hence c=0 is uniquely optimal for all n≥1. Independently checking the log interval Taylor coefficients through n^−2, EZ²=1, EZ⁴=3−2/n, EZ⁶=15−30/n+16/n² and the symmetric-binomial entropy H(S_n)=.5 log(π e n/2)−1/(12n²)+o(n^−2) yields D_n(c)=2c²/n+[1/9−(2/3)c²]/n²+o(n^−2) for fixed c. Central-window Taylor bounds and Chernoff-controlled tails justify the expectation. An independent numerical summation for n=200,800,3200 recovers limiting n²D_n(0)→1/9 and nD_n(1/2)→1/2; finite checks alone are not an asymptotic proof.

## originality

PASS

The exact all-n phase optimizer and full fixed-phase KL coefficients are stronger than Gavalakis–Kontoyiannis qualitative quantized-normal entropic CLT and not implied by the independent binomial entropy expansion alone. Best-of-knowledge novelty; older refined continuity corrections remain a named risk.

## value

PASS

The discrete entropic CLT normally uses a boundary-aligned cell comparator; the exact midpoint optimizer removes the entire n−1 KL term, improving to the sharp n−2 order. This is a motivated quantitative normalization effect with a rigorously identified optimum, not merely a routine entropy coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
