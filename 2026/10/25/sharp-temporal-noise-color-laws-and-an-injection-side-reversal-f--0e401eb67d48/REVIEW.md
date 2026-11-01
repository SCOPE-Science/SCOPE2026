# Independent mathematical audit

## correctness

PASS

Projection onto invariant constraint kernel diagonalizes the midpoint map with multipliers μ_i=(1−hλ_i/2)/(1+hλ_i/2). Stationary variance of each mode follows by summing lag covariance Σ_{j,k≥0} μ^{j+k}h⁵qg²ρ^{|j−k|} = h⁵qg²(1+μρ)/[(1−μ²)(1−μρ)]; the injection-side gain is g=1 post-step versus g=(1+hλ/2)^{−1} in the midpoint residual. Differentiation yields R''=4h⁵Σ qg² μ²/[(1−μ²)(1−μρ)³]>0 unless all μ=0, giving exact endpoint derivative criterion, unique 2-mode optimum ρ*=(β−α)/(αv+βu). Symbolic independent moment recurrence and algebra verified the exact two sign-opposite examples at h=1, λ=(1,10), μ=(1/3,−2/3), with post-step optimum 9√5−39/2>0 and pre-solve (9√5−33)/19<0 plus exact risk values. Finite-horizon RMS O(h²) follows from Toeplitz lag covariance norm ≤(1+|ρ|)/(1−|ρ|) and deterministic midpoint O(h²); no uniform ρ→±1 assertion.

## originality

PASS

Altmann–Moradi's original randomized midpoint PDAE construction and O(h²) iid perturbation rate are already prior; its Section 4.2 Eq.(4.3) explicitly inserts iid η into the equation RHS. Classical linear-filter transfer/covariance formulas also predate this claim. The contribution is a sharp stationary AR(1) time-correlation convexity classification for two input conventions and the explicit SAME constrained model with opposite best correlation signs. The full Altmann–Moradi OA article examined in its relevant section considers i.i.d. independent input, not optimally colored AR(1) numerical forcing. Broader linear filtering work may encode the covariance calculus; significance lies in the injection-side sign reversal and order retention, not the generic geometric series.

## value

PASS

Separates a design choice of probabilistic numerical methods—where noise is injected—from the choice of its temporal correlation. Opposite optimal correlation signs on the same nontrivial constrained SPD dynamics and preservation of second-order RMS for fixed color form an interpretable structural counterexample; the general all-eigenmode strict-convexity criterion and exact two-mode formula make it more than a tiny parameter calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
