# Independent mathematical audit

## correctness

PASS

For symmetric nearest-neighbor voter copying rate1 on each ring N>=3, and independent rate r>0 resets to original frozen iid fair xi (M) or fresh fair spins (F), the stationary annealed cross moment H_n=E[S_i xi_(i+n)] solves L_r H=r delta_0 for L_r=(1+r)I-(T+T^-1)/2. The positive discrete Green inverse G gives H=rG, F_n=(G*G)_n=-partial_r G_n, C^F_n=G_n/G_0 and C^M_n=r^2F_n+(1-r^2F_0)G_n/G_0 for n!=0, normalized C_0=1. Therefore C^M_n-C^F_n=-r^2G_n partial_r log(G_n/G_0)>0, since G_n/G_0=cosh(a(h-min(n,N-n)))/cosh(ah), cosh a=1+r, h=N/2 and t->t*tanh(at) strictly increases for t>=0. The proof handles odd N (half-integer h), N=3 and all r>0. At r= lambda/N^2 the exact a expansion gives same leading continuum profile, positive O(1/N) macroscopic memory correction and strictly positive limit N^2(rho_F-rho_M)=(lambda/4)(1+2s/sinh(2s)), s=sqrt(lambda/2). Independently checked normalized finite-cycle resolvents/convolutions, strict signs in 18 N/r choices, and exact moment recurrence form; symbolic asymptotic expansions, not finite samples, prove N->infty.

## originality

PASS

Grange provides original-opinion stochastic resetting and infinite lattice two-point equations. Pymar–Rivera treat fresh-noisy voter finite graphs and cycle transition. The all-N all-r strict comparison of these different matched protocols and exact finite-size subleading wall coefficient are not stated in inspected primary statements; O PASS best-of-knowledge with a real risk that a broader killed-walk comparison implies it.

## value

PASS

Keeping original opinions versus refreshing independent fair opinions are meaningful competing stochastic interventions with matched clocks. Showing a strict sign for every finite size, positive rate and pair separation and calculating the first observable N^-2 domain-wall separation after the leading continuum profiles coincide is a natural exact finite-volume comparison and sharp correction, not just an algebraic relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
