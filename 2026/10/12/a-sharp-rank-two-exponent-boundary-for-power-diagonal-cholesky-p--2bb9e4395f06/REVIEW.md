# Independent mathematical audit

## correctness

PASS

Write r_i=(A²)_ii and d_i=A_ii. Expanding the PSD rank-one downdate and spectral Cauchy yields S−||B_i||²=2(A³)_ii/d_i−r_i²/d_i² ≥r_i²/d_i². Weighted Cauchy yields expected gain ≥S²/[∑d_i^β∑d_i^(2−β)]. For 0≤β≤2, AM–GM pairwise gives denominator≤n∑d_i²≤nS. Scalar identity attains equality. For A_{m,t}=diag(t,J_m), exact gain Gβ=(t^(β+2)+m³)/(t^β+m), S=t²+m². β=4 gap is m[y³−my²−y+m³]/[(m+1)(y²+m)]>0 for y=t² by case y≥m and 0≤y≤m; monotonic in β depending on t/m reduces every β∈[0,4] to endpoint 0 or 4. For β>4 choose 2/β<a<1/2 and t=m^a giving Gβ=o(m)<S/(m+1)~m. Continuity gives SPD examples. Independently reproduced β=5,m=100,t=8 expected residual 9102400/913, target 1006400/101, excess 499200/92213; tested polynomial positivity rationally for 336 m,y cases.

## originality

PASS

Steinerberger (2024) already establishes β=2 one-step Frobenius contraction and uses Gibbs/diagonal-power pivot distributions; Chen–Epperly–Tropp–Webber (2022) covers the β=1 randomized Cholesky and trace bounds. The new differentiated claims are the full β∈[0,2] sufficient interval and sharp rank-two cluster phase β=4, not the sampler, pivot identity or known β2 theorem.

## value

PASS

Choosing power β trades information exploitation against redundant-cluster blindness in randomized PSD approximation. The naturally motivated isolated coordinate plus repeated-column rank-two model has a sharp actual exponent threshold and witnesses strict over-greedy failure for every β>4. This is a substantive boundary despite general β∈(2,4] remaining open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
