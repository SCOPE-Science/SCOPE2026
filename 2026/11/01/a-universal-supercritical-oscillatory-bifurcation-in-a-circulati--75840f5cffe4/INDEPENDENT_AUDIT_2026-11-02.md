# Independent mathematical audit

## correctness

PASS

For every fixed c>0, the clipped cyclic logistic map is analytic near interior homogeneous fixed point q=1-1/r. Fourier diagonalization gives multipliers 1-t and 1-t±iκt (κ=sqrt(3)c,t=r-1), unit-circle crossing exactly at r_c=1+2/(1+κ²)<3, transverse outward derivative one, and a third multiplier strictly within unit disk at r_c. The exact quadratic Fourier equations give center-manifold U=-(2r_c/t_c)|Z|²+O(|Z|³); outside resonances c=1/3,1/sqrt(3), eliminating the conjugate-square term with p=β/(barλ²-λ) yields l1=Re(barλ[γ+2βbar p])=-(κ²+3)^3/(1+κ²)^2<0. Independent SymPy algebra recomputed p, l1 and c=1 value -27/2; numerical crossing and exact Fourier substitution checks from the inspected package were distinguished from proof. The nonresonant Neimark–Sacker theorem and transverse contraction then give a nearby attracting invariant Jordan curve for sufficiently small r-r_c>0. Clipping is inactive near onset; no global basin or resonant circle assertion.

## originality

PASS

Best-of-knowledge PASS: the source logistic-map models are not equivalent under natural parameter substitution: the inspected 2020 study uses two symmetric coupled maps and a symmetry-broken fixed-point Neimark–Sacker event, the 2014 three-map paper has additive linear unidirectional coupling, and the 2026 disordered-map work gives broader instability motivation but no identified theorem fixing the exact cubic coefficient for this multiplicatively circulating three-site family. Unindexed directed cyclic competition work remains priority risk.

## value

PASS

A balanced three-site directed logistic ring is the smallest circulation network with a nontrivial oscillatory Fourier pair. The exact onset before the scalar flip and universally negative first Lyapunov coefficient across every positive nonresonant coupling resolve the nonlinear bifurcation type rather than just reporting linear instability. The sharp all-coupling sign and attracting-circle conclusion constitute a motivated structural dynamical classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
