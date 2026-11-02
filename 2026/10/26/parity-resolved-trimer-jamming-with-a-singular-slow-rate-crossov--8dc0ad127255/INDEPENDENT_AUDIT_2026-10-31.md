# Independent mathematical audit

## correctness

PASS

For each vacant length n>=3 interval, the loss equation has n-2 internal triple starts and exactly four starts crossing its boundaries; all four extensions have lengths n+1 or n+2. The candidate E_{i,n}=exp(-t sum_{j=i}^{i+n-3}r_j) u_parity(i)u_parity(i+n-1) with the two displayed u0,u1 ODEs satisfies each equation. The bounded linear hierarchy uniqueness follows from Duhamel/Gronwall after factoring negative diagonal terms; the probability solution is bounded, so the ansatz is the correct infinite-lattice vacancy probability. Successful triple arrival rates are a exp(-at)u0^2 and b exp(-bt)u1^2; counting two even/one odd, or reverse, yields C0=2J0+J1, C1=J0+2J1. For b=eps->0, on compact fast time u0,u1->exp(-(1-e^{-at})), yielding J0->(1-e^-2)/2. Uniform tail bounds give u1(s/eps)->e^-1 for each s>0; changing variable v=eps t and dominated convergence gives J1(s/eps)->e^-2(1-e^-s), including s=infinity. This proves exact singular jump in mean 3e^-2/2 between b downarrow0 after jamming vs b=0 initially. Independently checked 44 vacancy hierarchy equations at each of four times for rates (1,1),(1,.2),(2,3),(.1,1) with fresh SciPy ODE integration and independently formed residuals.

## originality

PASS

Best-of-knowledge PASS, with particularly serious named priority risk. Classical 1D homogeneous trimer RSA and empty-interval techniques are prior. Lebovka et al. arXiv:1109.3271 full primary discusses two-dimensional orientation anisotropy and uniform 1D baseline, not alternating 1D start positions in its inspected model. The highly plausible 1994 de Oliveira–Tomé paper *Inhomogeneous random sequential adsorption on bipartite lattices* states exact time-dependent 1D sublattice coverage under inhomogeneous adsorption, but its abstract does NOT specify the exclusion footprint or whether its full result implies this trimer ODE and singular limit. arXiv and lawful OA access attempts were unsuccessful, and authorized Oxford returned vpn_disconnected (no bypass). Abstract-only access is not taken as whole-document NOT_COVERING. There is no demonstrated exact implication; its unresolved priority remains an explicit material risk.

## value

PASS

Parity-dependent deposition rates are a natural kinetic perturbation in irreversible hard-segment adsorption. The complete finite-time two-component infinite-volume closure is an exact tractable inhomogeneous RSA model; the slow b->0 limit yields a noncommutation of jamming and parameter limit with an explicit nonzero coverage jump 3e^-2/2 and a universal exponential slow-time profile. Both the object and invariant are physically/mathematically motivated, and the result is not a finite simulation or a trivial homogeneous parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
