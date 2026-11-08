# Self-review

## Correctness — PASS

The finite Markov generator yields exact drifts LZ=epsilon(1/2-Z), LD=-(1+c)D and quadratic variation Gamma(Z)=s H/4 with H=epsilon/2+c(X+Y-2XY). The stationary L(D^2) identity gives E(D^2)<=s/[2(1+c)] and a transient exponential bound. For epsilon/s tending to a finite lambda, Taylor remainders after time acceleration by 1/s are O(max(1/a,1/b)); integrated D^2 vanishes, implying tightness and convergence to the unique Jacobi martingale problem. Stationarity and its unique Beta(2lambda,2lambda) invariant give the critical joint limit. At zero and infinite ratios the exact two-spin covariance equation and stationary variance give the endpoints. Exact rational Markov generator checks replayed 2664 assertions for all part sizes 1..4 and refresh fractions 1/2,1/3,2/3; those are supplementary to the infinite proof.

## Originality — PASS (qualified)

Inspected general unnoised voter-density diffusion limits (Chen–Choi–Cox 2013; Blythe 2010), noisy-voter ordered and disordered regimes (Pymar–Rivera first posted 2021), complete-graph noisy-voter Wright–Fisher equilibration (Aljovin–Jara–Xiang 2024), and a distinct multi-agent-per-node network model (Mori–Hisakado–Nakayama 2018). None of their examined statements implies the specific all-imbalance K_{a,b} noisy-bipartite process and its diagonal critical stationary Beta law with exact finite correlation identities. Previously recorded mathematical findings include synchronous bipartite independent-Beta limits and a fixed-core star Beta limit; both differ materially in update rule or growth regime. Scientific-record searches found no stronger/equivalent covering result. Residual risk: general diffusion reduction/mutation extensions could independently yield the conclusion, and priority is not independently certified.

## Value — PASS

In a bipartite network with two diverging but arbitrarily unequal populations, this identifies the exact critical mutation scale s=1/a+1/b, the full path-level Wright–Fisher limit, a shared (rather than independent) critical Beta opinion density, and two endpoint regimes; it quantifies the change caused by asynchronous versus synchronous updating. This is a natural stochastic-process scaling problem; the explicit finite pair correlations supply nonasymptotic checks and identify effective population size. It does not rely on arbitrary slices or small numerical gains.

## Prior literature and scope limitations

The nearest sources are Pymar–Rivera, arXiv:2112.01478; Chen–Choi–Cox, arXiv:1311.5786; Aljovin–Jara–Xiang, arXiv:2409.05722; Mori–Hisakado–Nakayama, arXiv:1810.05643; and Blythe, arXiv:1006.1557. All employ relevant copying or diffusion machinery, but their inspected statements do not simultaneously cover the claimed graph, noise scaling, diagonal joint law, and arbitrary part imbalance. The mathematically important unresolved risk is independent derivability via a general mutation-extended diffusion reduction. The finite checker establishes no infinite theorem by itself.

Self-review: passed. Independent audit: not yet performed.
