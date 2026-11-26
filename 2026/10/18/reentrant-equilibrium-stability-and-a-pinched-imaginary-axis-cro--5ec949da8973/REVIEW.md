# Independent mathematical audit

## correctness

PASS

The frozen Finding item 3 incorrectly assigned two positive-real-part eigenvalues to all points outside the open stable interval, including its two endpoints. For a=3,b=c=1, k=-6 gives (λ+2)(λ²+9) and k=-3/2 gives (λ+3)(λ²+3), each with unstable index zero. The proof and subsequent endpoint sentence already supported the correction. The complete corrected RESULT.md and SLOGAN.txt under /workspace/repairs/2 now separate strict exterior points, the marginal endpoints, and the collapsed a=2c case. Re-audit: xy=b fixes y=b/x; solving the remaining equations gives x²=b(a−ck)/a, so existence and symmetry are as stated. The independently computed cubic has Q=c+a²/(a−ck)>0 and S=2b(a−ck)>0 in the existence region. The first Routh column (1,Q,Δ/Q,S) gives index zero or two for Δ positive or negative; at Δ=0, R=S/Q and the exact cubic splits as (λ+Q)(λ²+R). The two linear factors of Δ divide the admissible k values exactly as stated: k_B lies beyond a/c when a<c, disappears when a=c, and meets k_A only at a=2c when a>c. Implicit differentiation at λ=i√R gives real-part speed −Δ'/(2(Q²+R)); the quadratic correction at the pinch is positive. Independent replay /workspace/branches/replay_2.py reconstructed the cubic from the differential equations, tested both exact endpoint factors, and solved orders one and two directly in the pinched cubic, confirming bc/[64(b+c²)]. The equality cases do not classify nonlinear Lyapunov stability or imply a nonlinear Hopf bifurcation.

## originality

PASS

For the corrected claim, credit Dong with the general equilibrium/Jacobian formulas and fixed-parameter analysis and classical Routh–Hurwitz with the criterion. The exact sign partition and the degeneracy with its quadratic coefficient are not already stated or supplied by a stronger inspected spectral theorem. They are derived from the known Jacobian; the claim is the exact all-parameter analysis, not novelty of the flow, equilibrium count, or algebraic method.

## value

PASS

The corrected local result makes the role of the control parameter explicit: changing it can create and then destroy simultaneous exponential stability of the symmetric pair, independently of forcing b. The stable window collapses at a distinguished ratio; the exact positive contact coefficient explains why varying k there cannot cross onto a stable side. Distinguishing marginal equality from index-two instability matters for interpreting bifurcation diagrams and is not a claim about global attractors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
