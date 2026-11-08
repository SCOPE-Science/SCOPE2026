# Independent mathematical audit

## correctness

PASS

For unit Fock kernels at z_j=√(ρN)exp(2πij/N), direct Fourier transform of their normalized circulant Gram gives exactly λ_{N,k}=N P(Poisson(ρN)≡k mod N), which is positive. The maximum is √(N/(2πρ))(1+O_ρ(1/N)) by Poisson local Stirling and exponential separation. For 0<ρ≤e^-1, unimodality and endpoint ratio p_0/p_{N−1}∼ρ√(2πN)exp[N(−1−logρ)] show unique minimizing Fourier residue N−1 even at threshold, giving λ_min=√N/(ρ√(2π)) exp(−N(ρ−1−logρ))(1+O_ρ(1/N)). For ρ>e^-1, the strictly increasing φ(u)=(u+1)log(u+1)−u logu gives unique u>0 satisfying φ(u)=1+logρ, so I_ρ(u)=I_ρ(u+1)=H>0, u<ρ<u+1. Convexity localizes globally least residues to integers Nu+O_ρ(1); two Poisson aliases at Nu+δ and N(u+1)+δ have prefactor a^δ/√u + b^δ/√(u+1), δ∈Z−{Nu}; strict convexity reduces D_N minimization to two nearby integers. Uniform Stirling and remote-alias exponential gaps yield stated O_ρ(1/N) and squared κ. Independent log-sum-exp Poisson-residue comparisons for N=80,160,320 and ρ∈{0.2,e^-1,0.45,1,2} gave log-asymptotic discrepancies ≤0.0042. Finite checks corroborate, do not prove all N.

## originality

PASS

Horoshko–De Bièvre–Kolobov–Patera (2016) already establishes the exact Poisson-residue spectrum and this is NOT claimed as new. The distinctive result is sharp joint-N all-residue minimization with pinned critical N−1 mode and oscillatory two-alias prefactor. Reviewed prior sections focus on circular coherent-state entanglement and average photon number rather than this interpolation-conditioning asymptotic. Luo–Tang–Zhang 2024 full text unavailable after OA attempt and Oxford VPN block; residual risk documented.

## value

PASS

The ratio of eigenvalues of a normalized kernel Gram is canonical interpolation stability; scaling squared radius ρN balances node count and physical occupation number naturally. Identifying one-tail versus two-alias worst-mode mechanisms, sharp ρ=e^-1 boundary and fractional-part-dependent leading amplitude provides nontrivial precise guidance beyond an already known exact but infinite series.

The dated certificate retains the supplied scientific assessment, sources and limitations.
