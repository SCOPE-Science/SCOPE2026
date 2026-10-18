# Independent mathematical audit

## correctness

PASS

For every integer k>=1, C_k(u,v)=uv+(1/8k)u(1-u)[4v(1-v)]^k has uniform margins and c_k=1+eps(1-2u)f'_k with |f'_k|<=4k; consequently c_k lies in [1/2,3/2]. The conditional CDF v+eps(1-2u)f_k(v) decreases in u for interior v, establishing strict stochastic increase, while C-uv>=0 yields PQD. Directly integrating its squared conditional-CDF deviation gives xi(C_k)=2 eps^2 I_k, I_k=4^(2k)((2k)!)^2/(4k+1)!. Four actual quadrant masses [[(1+eps)/4,(1-eps)/4],[(1-eps)/4,(1+eps)/4]] yield a piecewise-linear checkerboard conditional CDF and xi(B_k)=eps^2/2. Hence the exact ratio 1/(4I_k) diverges like sqrt(k/(2*pi)); dominated convergence supplies the infinite result. Independently evaluated rational beta integrals, checkerboard matrix and k=5,6 threshold; I5=262144/969969, I6=4194304/16900975. k6 ratio=16900975/16777216. These finite calculations do not replace the asymptotic proof; absolute inflation tends to zero.

## originality

PASS

Best-of-knowledge original quantitative divergence at one fixed 2x2 coarse grid inside smooth SI and PQD copulas with density bounded above and away from zero. Rockel (2026) has the already known twofold SI checkerboard inflation example (2x4 down to 2x2), along with a reverse inequality under stronger TP2 density. Both prior facts are correctly credited. Neither finite ratio two, positive TP2 bound, nor Ansari–Fuchs fixed-input continuity entails arbitrarily large relative ratios across varying k. Focused Resultary and web comparisons did not reveal dominating statement; unsuccessful searches are not novelty proof.

## value

PASS

A structural instability/boundary of a widely used fixed-grid directional rank-dependence approximation is substantively motivated: no uniform multiplicative fidelity constant even for polynomial strictly SI copulas with uniformly bounded positive densities, despite the TP2 lower bound and fixed-C refinement convergence. The explicit k=6 first crossing and asymptotic growth give interpretable sharp family behavior. Distinct from merely showing one coarse-grid counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
