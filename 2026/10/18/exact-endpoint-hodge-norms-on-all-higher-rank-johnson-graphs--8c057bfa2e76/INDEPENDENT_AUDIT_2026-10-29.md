# Independent mathematical audit

## correctness

PASS

For integers n≥6, 3≤k≤floor(n/2), graph J(n,k) with degree k(n−k), unit conductances, real counting-measure edge ℓ1/ℓ∞ spaces, and Q=D^T L^+D, C=I−Q. Fix an oriented adjacent pair (U+a,U+b), |U|=k−1. Source antisymmetry forces h=0 when both/neither a,b occur and opposite potentials ±p_i when exactly one occurs, i=|S∩U|. Counting swaps yields w_i=C(k−1,i)C(n−k−1,k−1−i), u_i=(k−1−i)^2, d_i=i(n−2k+i), and (n+u_i+d_i)p_i−u_i p_(i+1)−d_i p_(i−1)=1_{i=k−1}. This tridiagonal matrix has positive inverse because diagonal exceeds off-diagonal sum by n; irreducible nearest-neighbor rates prove p_i>0. For Δ_i=p_(i+1)−p_i the subtracted system has row margin exactly 2(n−1)>0 and positive irreducible inverse; hence strict Δ_i>0. Weighted detailed balance w_i u_i=w_(i+1)d_(i+1) yields S0=Σw_i p_i=1/n and S1=Σi w_i p_i=((k−1)+(k−1)^2/n)/(2(n−1)). Each positive vertex has n−2 zero-potential neighbors and exactly one negative neighbor; same-sign adjacent levels contribute 2Σw_i d_i Δ_(i−1). Thus absolute transfer-current column sum 2[(n−1)S0+(n−2)S1−(k−1)^2 S0] simplifies exactly to ((k+1)n²−(k²+3)n+2)/(n(n−1)). Edge-transitivity and Q=Q^T make every column and row equal. Since graph edges number Nk(n−k)/2 and rank(Q)=N−1, diagonal effective resistance R=2(1−N^{-1})/[k(n−k)], and column C has norm 1+norm Q−2R. For k(n−k)≥9, C>Q. Difference of Q at successive ranks (n−2k−1)/(n−1)>0 before balanced k, proving strict rank ordering. At fixed rank n→∞, norms tend k+1,k+2; balanced rank gives n/4+5/4+O(1/n) and n/4+9/4+O(1/n). Independently reconstructed Git tree hash, symbolic row margins/moment reductions/rank differences, two exact full Laplacian rational cases J(6,3),J(7,3), and 84 exact tridiagonal tests (6≤n≤22 plus three larger n). Verified SOURCE formulas and expected endpoint values; no claim that finite checks prove all parameters.

## originality

PASS

Best-of-knowledge all-rank originality after statement-level comparison: the published 2024 cycle-space projection paper derives exact Hamming-cube endpoint norms, not Johnson J(n,k) edge-gradient norms; 2017/2026 electrical-flow papers bound transfer-current absolute norms for general graphs without the proposed rank formula or sign-ordered Green kernel. Two published Johnson-scheme results were read in full: one evaluates the degree-two primitive idempotent on vertex functions, the other a two-coordinate-face low-pass concentration operator; neither acts on oriented edges nor implies the proposed cut-column absolute-current formula. The rank-two triangular-graph formula is recovered but is expressly excluded. The new higher-rank result has a k-state positivity and moment proof. Unindexed equivalent or stronger results cannot be ruled out completely.

## value

PASS

The Johnson graph is a standard and structurally central two-parameter distance-regular family, and the canonical edge cut/cycle Hodge ℓ1/ℓ∞ projection norms measure worst-case unit-current path length and Banach-space complementability. A complete exact n,k law for k≥3 is mathematically natural rather than a contrived finite slice. The nontrivial strict ordering of edge-rooted potential levels and two weighted Green moments give conceptual insight into why absolute values collapse to a rational expression. The exact extremal rank comparison reveals a transition from bounded norms at fixed k to n/4 growth at balanced ranks, and C−Q→1. This is a worthwhile self-contained structural invariant even without claiming optimal arbitrary projection norms, a general electrical-routing theorem, or a broader paper-sized result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
