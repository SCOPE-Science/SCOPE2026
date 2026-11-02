# Independent mathematical audit

## correctness

PASS

Reconstructed the minimization for all γ,w>0 and K≥1. With q_i=p_i/p_{i+1}, the weighted symmetric part is -γI+(w/2)T where T is a 4-path with squared off-diagonal weights q_i. Perron strict monotonicity forces p1=min p=1 and p4=max p=K at K>1; for fixed s=p3/p2 the product q1q3=s/K and q2=1/s are fixed. Characteristic polynomial λ⁴−(q1+q2+q3)λ²+q1q3 makes minimizing λ equivalent to minimizing q1+q3 at fixed product; AM–GM forces q1=q3=√(s/K), achievable by p2=√(K/s), p3=√(Ks). Put r=q1=q3 in [1/K,1], q2=1/(Kr²). The Perron root is L=(1/(√K r)+√(1/(Kr²)+4r))/2. Symbolic differentiation independently confirmed sign(L′)=sign(2Kr³−1−√(4Kr³+1)), negative until Kr³=2, positive afterward. Thus r*=1 for K≤2, and (2/K)^{1/3} for K≥2, unique, yielding exactly both branches R(K) and P*(K). Standard logarithmic norm derivative at t=0 proves semigroup nonexpansion iff μ≤0; monotonic inversion yields Kcrit in all c regimes including boundaries c=1/√2 and c=(1+√5)/4. The exact rational certificate was independently verified as det(xP−(G^TP+PG))=256x(x+1)(x+3)(x+4), with G=-I+2N and P=diag(1,2,8,16). No finite scan is treated as all-K proof.

## originality

PASS

Best-of-knowledge original constrained spectral optimization: Mason–Shorten (2006) Theorem 4.2 characterizes existence of a common diagonal quadratic Lyapunov function for two Hurwitz Metzler matrices via a matrix-pencil condition; it neither imposes a finite condition budget nor identifies an optimal diagonal metric. Mason (2012) Theorem 3.1 concerns diagonal Riccati solution existence for positive delay systems. Bhatia–Kahan–Li (2002), in its accessible full abstract, compares norms of scaled triangular matrices under monotone diagonal similarities, but that published assertion does not imply the minimax weighted symmetric-part eigenvalue or the exact K=2 phase. Published related SCOPE weighted-shift and Jordan results concern distinct norm objectives. No inspected complete primary text yielded the sharp K-dependent profile, inverse-sixth-power threshold, or the all-diagonal-metrics necessity. An older differently parameterized general optimization theorem could still cover the claim; see residual risks.

## value

PASS

The spectral condition number κ(P) measures the distortion cost of a positive diagonal quadratic Lyapunov metric. Determining the least cost for a stable positive cascade to be nonexpansive is a natural finite-dimensional control/spectral optimization, not merely restating Hurwitz stability or a cheap negative test. Four stages are the first chain with interacting outer and central link allocations. The exact K=2 phase switch between two plateaus and unique nongeometric graded weights, the exact Kcrit(c) for all damping ratios, and sixth-power divergence as γ/w→0 quantify a nontrivial tradeoff; the exact rational threshold K=16 is a motivated sharp boundary. It is narrow but offers an independently useful all-parameter structural classification and witness. The conclusion is about optimal weighted log norm, not a claim about exact Euclidean transient maxima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
