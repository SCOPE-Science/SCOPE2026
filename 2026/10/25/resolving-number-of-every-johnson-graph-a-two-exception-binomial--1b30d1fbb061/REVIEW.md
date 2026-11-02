# Independent mathematical audit

## correctness

PASS

For pair distance r in J(n,k), an equidistant witness W must choose equal counts from disjoint r-sets, so E_r=Σ_j C(r,j)^2 C(n-2r,k-2j). The all-subsets threshold is 1+max_r E_r. The coefficientwise D_r(z)=(1+z)^{2r-1}(1+z²)−(1+z)Σ C(r,j)^2 z^{2j} is nonnegative by Vandermonde central/near-central term comparisons; hence E1≥Er whenever n≥2r+1. The only remaining n=2r case forces n=2k=r*2; for even k=2h, Ek=C(2h,h)^2 and E1=2 C(4h-2,2h-2). Vandermonde yields E1≥Ek for h≥3; h=1,2 have strict antipodal excess. Odd k antipodal count zero. Complement J(n,k)≅J(n,n-k) handles entire domain. Independent integer code checked 484 admissible n,k pairs and 8,370 coefficient signs through r=90. Finite checks corroborate the analytical proof, not infinity.

## originality

PASS

The generic resolving-number/equal-distance obstruction identity was established by Garijo–González–Márquez (2013), and Johnson/Kneser metric resolving-set constructions are older. The present claim maximizes all Johnson equalizer counts and isolates two antipodal exceptions; the cited predecessors do not state that universal maximization in examined material. Similar binomial identities in constant-weight coding or older distance-equalizer research are a residual priority risk.

## value

PASS

The resolving number is the natural sharp threshold at which every landmark choice resolves a vertex-transitive coding-theoretic graph; its complete two-exception closed formula settles all Johnson parameters and identifies the structural antipodal exceptions. It is not a textbook minimum-metric-dimension deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
