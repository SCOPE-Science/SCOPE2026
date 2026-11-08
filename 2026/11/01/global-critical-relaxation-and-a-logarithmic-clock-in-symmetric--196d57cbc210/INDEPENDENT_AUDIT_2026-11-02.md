# Independent mathematical audit

## correctness

PASS

Fix 0<γ<1, positive x,y, symmetric Ricker map at r=s=2. The previously proved global convergence-to-a-fixed-point theorem of Baigent–Hou–Elaydi–Balreira–Luís applies at endpoint; coordinate growth near origin and missing-species invasion factor exp[2(1−γ)]>1 at each axial equilibrium rule out noncoexistence limits for positive orbits. For q=(1+γ)(x+y)/2−2 and w=(1+γ)(x−y)/2, exact update qʹ=e^(−q)[(2+q)cosh(κw)−w sinh(κw)]−2, wʹ=e^(−q)[w cosh(κw)−(2+q)sinh(κw)], κ=(1−γ)/(1+γ), η=1−2κ=(3γ−1)/(1+γ), |η|<1. Transverse w contracts exponentially on late tails. Inverting the scalar map f(q)=(2+q)e^(−q)−2 and solving weighted backward errors via a contraction with Lipschitz Lρ²<1 yields local C³ scalar phase π(q,w)=q+O(w²), invariant strong-stable phase-zero curve and exponentially small scalar shadowing. Analytic nonzero Jacobian off a measure-zero critical locus implies countable backward preimages of this C³ curve remain null. Independent exact symbolic composition gives f²(z)=z−z³/3+z⁵/30+z⁶/72+O(z⁷) and inverse-square step U_{n+1}−U_n=2/3+(4/15)U_n^−1+O(U_n^−3/2). Summation yields U_n=(2/3)n+(2/5)log n+C+o(1); exponential shadowing transfers the constant-level asymptotic to every nonexceptional planar orbit. Eigenvalue and exchange symmetry give even ψ(w) with curvature −γ(1−γ)/(1−2γ+5γ²). Finite trajectory samples do not prove global convergence.

## originality

PASS

Baigent et al. 2023 prove global convergence but not a two-term critical rate or exceptional preimage geometry. Kulakov et al. 2022 analyze dynamic modes; older Balreira et al. 2014 and Jiang–Rogers 1987 address stability/competition but full relevant texts were inaccessible in this review (Balreira repository PDF returned 403). Similar published Resultary logarithmic clocks concern different rational/flow systems and do not reduce to this Ricker map; prior spectral Floquet reduction covers synchronous cycles, not the nonhyperbolic coexistence fixed point. Best-of-knowledge originality with named risks.

## value

PASS

At the exact flip boundary r=s=2 of a globally convergent ecological discrete map, this gives an all-positive-initial-state rate classification beyond convergence: a universal logarithmically corrected algebraic clock, signed √3 amplitude, null exponentially fast exceptional family, and explicit coupling-dependent curvature. The boundary and invariant are natural, and the logarithmic coefficient is not forced by linear stability or a routine hyperbolic estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
