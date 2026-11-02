# Independent mathematical audit

## correctness

PASS

For synchronous binary open-neighbour majority with lazy ties on K_a+single bridge+K_b, a,b>=3, separately reconstruct update of one clique from x one-bits among n-1 nondistinguished vertices, bridge bit w and opposite bridge bit e. For odd n=2p+1, all nondistinguished vertices move to majority immediately and only x=p pivotal cases cause one-step bridge discrepancy, entire clique constant by time 2. For even n=2p, unbalanced total s=x+w becomes permanent unanimous state; at s=p nondistinguished bits complement and bridge adopts e, staying balanced for next step iff bridge bits oppose. These exact case rules yield all recurrent states: four fixed, primitive 2-cycles only if both sizes even, all 2D_aD_b 2-periodic states with D_n=binom(n-1,n/2-1), and none entered after time zero. Inclusion-exclusion of odd pivotal events yields max T=2 and N2=2^b C_a+2^a C_b-2 C_aC_b with C_odd=binom(n-1,(n-1)/2). If both even, one balanced side and one strict majority yields max T=4 and N4=2[D_a(2^{b-2}-D_b)+D_b(2^{a-2}-D_a)]. If mixed parity, odd pivotal bridge prolongs balanced even side until t=5 and N5=binom(a-1,(a-1)/2)binom(b,b/2) for odd a; switched analog. Central binomial Stirling gives N5/2^{a+b}~1/(pi sqrt(ab)). Independent checker built neighbour masks anew and exactly enumerated all states for 25 pairs 3<=a,b<=7, verifying upper bounds, sharp populations, four fixed, primitive 2-cycles, and absence of late 2-cycle entry. Proof remains all-size, not extrapolated finite data.

## originality

PASS

Goles–Olivos establishes eventual at-most-two periods for symmetric threshold maps, not the sharp 2/4/5 transient times, full explicit critical labelled populations or no-entry-after-time-zero on this graph. Kaaser–Mallmann-Trenn–Natale gives broad upper bounds/contraction methods but not the exact barbell counts. A previous Resultary bridge-barbell polynomial is a zero-forcing invariant, not majority dynamics; complete split graphs or clique windmills have different edge sets. A prior specialization might exist under threshold automata nomenclature, so qualified O PASS for exact bridge-resonance classification and strata.

## value

PASS

Two highly cohesive communities connected by one bridge form a standard model for majority-consensus bottlenecks. The theorem gives a complete natural parity boundary for longest transients and a precise labelled count of each worst-case stratum, including when two-cycles can exist and the unexpected fact that they never acquire a positive transient. These are unknown nontrivial graph-dynamical invariants, not implied by generic period-two convergence. The single-bridge/majority/lazy-tie assumptions are explicit and necessary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
