# Independent mathematical audit

## correctness

PASS

For the specified degree-four graph the flip cost is 4J(k−2) with k opposite neighbors. Equality is allowed for weak stability but not for strict freezing. Each triangle has an equal edge and each horizontal edge belongs to only one triangle, so strict freezing forces both rows to alternate, giving four states for even n, none for odd. Independently, order the vertices as (i,0),(i+1,1),(i+1,0),… to obtain C_(2n)^2, then stagger spins to give the periodic ANNNI Hamiltonian −JΣτ_jτ_(j+1)+JΣτ_jτ_(j+2). The corresponding wall word has even weight and two spin lifts. With m walls and a adjacent wall pairs, F=2n−m+2a. For m>n, a≥2m−2n and m−2a≤n−3; for m≤n, m−2a≤m, with equality exactly for isolated walls. Thus the optimum uses n isolated walls when n is even (two alternating wall words), and n−1 when n is odd. The count of cyclic independent (n−1)-subsets is (2n/(n+1)) binom(n+1,n−1)=n², giving 2n² spin configurations. In the original 16-state transfer, the four displayed neighbor entries must be counted as four slots, not as a set of distinct spin values; the physical-neighbor condition and the supplied code both specify that intended count. A separate replay reconstructed the graph and counted all spin configurations at n=4,…,8, matching the graded weak ensemble and the parity and ground formulas. Independent trace computation at n=4,…,11 yielded 62,172,450,1276,3550,9782,27256,75616. Rebuilding the marked transfer gave the exact P and Q factorization and a strictly positive fifth power on the 14-state core. Thus the isolated simple Perron root gives the stated entropy and analytic log moment-generating function near u=1. The spectral gap persists in a small complex neighborhood, so the exponentially small remainder in the log trace can be differentiated there; the variance is O(n). The positive root and derivative give α≈2.776562146292835 and μ≈1.464073732677484. As a different replay, in ANNNI wall bits weak stability excludes precisely 1100,1110,1111,0111,0011; shift overlapping triples and mark each transition by u^(b+1{b=c}) for the middle two bits. The wall transfer gives R(z,u)=z^5−uz^3−(u^3+u^2)z²−u³z−u⁴ as its Perron factor; P(z²,u)=−R(z,u)R(−z,u). The original graph proof and marked transfer establish the all-length results, while the bounded replays corroborate them. The frozen verify.py was inspected, not executed. There is no assertion about time scales or hitting distributions for dynamics.

## originality

PASS

The graph is an exact reparametrization of the classical κ=1 periodic ANNNI chain, and the commensurate fourfold antiphase ground state is prior. The distinct supported contribution is the parity-resolved finite count together with the exact marked enumeration and energy law of the uniform weak one-spin-stable ensemble, contrasted with strict absorbing states. No novelty is credited to the Hamiltonian, the commensurate antiphase, the existence of ties, or the Glauber dynamics of this model.

## value

PASS

At the marginal dynamical coupling of a standard frustrated chain, the exact weak-minimum entropy and marked energy density quantify how an exponentially large set of local minima can lie an extensive energy above equilibrium even when strict absorbing states are absent or number only four. The parity formulas also distinguish geometric frustration from tie-induced local stability. The result is a static comparison, not a claim of dynamical metastable lifetimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
