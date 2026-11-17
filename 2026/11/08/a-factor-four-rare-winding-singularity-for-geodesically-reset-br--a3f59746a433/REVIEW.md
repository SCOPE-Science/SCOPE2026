# Independent mathematical audit

## correctness

PASS

From the frozen RESULT.md the two-zone backward equations D u″-(r+s)u+r u(0)=0 on (0,L/2) and D u″-(r+s)u+r=0 on (L/2,L), plus Neumann at 0, Dirichlet at L, give H_r(s)=(r cosh z+s)/(r cosh z+s cosh 2z), z=L sqrt((r+s)/D)/2. Fair independent renewal marks yield the exact pole equation H_r(Λ)cosh k=1; nonlattice renewal limits and differentiable steep SCGF justify the LDP. For r>0, H~(r/s)e^{-z}, so z+log(s/r)=|k|-log2+o(1) and the -2log|k| correction; Legendre transform gives coefficient L²/(16D). r=0 directly yields Λ=D k²/L², I_0=L² j²/(4D). Independent mpmath roots at (r,k)=(0.01,40),(0.01,160),(0.5,40),(0.5,160) show normalized Λ/(4Dk²/L²) increasing toward 1 and logarithm correction error decaying; this is finite corroboration, not proof. The standalone CHECK.py BVP discretization, renewal root and finite perturbations were inspected, not accepted solely from its marker.

## originality

PASS

Grange reports renewal turns, moments and related transform but the examined full-text sections do not state the r>0 singular large-current comparison; the published r=0 law cannot imply it by r→0 continuity since limits do not commute. No decisive earlier explicit matching theorem found. Broader stochastic-reset machinery and an earlier same-geometry Laplace transform explain the method, not explicitly the logarithmically corrected factor-four high-current theorem. This is a substantial implicit-derivability priority risk.

## value

PASS

The singular noncommuting rare-current and small-reset limits are a natural qualitative boundary for topological winding under resetting; the quarter-cost is a sharp, nontrivial observable distinction from ordinary effective diffusion, and the explicit correction localizes crossover. Motivated by comparing geodesic return protocols, not arbitrary parameter numerology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
