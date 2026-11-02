# Scientific review of the matching-deletion NOR basin theorem

## Correctness — PASS

The proof specifies the entire graph and update rule and reduces the dynamics to the pair of maps from each side of the bipartition to the other. The critical fact is that each side has only \(k+2\) possible one-step output subsets: the empty set, the whole part and the \(k\) matched singletons. Their interchange makes the recurrent image an involution. Direct counts give \(k+2\) fixed points and \(\binom{k+2}{2}\) primitive two-cycle orbits. The preimage fibers have sizes \(2^p-k-1\) and \(2^q-k-1\) in the only non-singleton cases; adding fibers over each cycle proves all individual basin sizes. The basin total is exactly \(2^{p+q}\), and the unique zero-transient boundary is checked. Two separately implemented exhaustive programs, inspecting 86,384 and 804,208 configurations across the stated ranges, corroborate the formulas. Their finite scope is explicitly separated from the all-parameter proof.

## Originality — PASS, with residual literature risk

The 2011 fixed-point paper of Veliz-Cuba and Laubenbacher concerns AND-NOT networks and maximal independent sets, while the 2015 survey by Aledo, Martínez and Valverde and the 2020 periodic-point paper of Aledo and collaborators provide general maxterm/minterm context. The latter two full-text accounts were examined for mathematical implication, including differences between open-neighbor and self-inclusive conventions. The known one-step NOR periodicity and the complete-bipartite no-deletion case are expressly treated as antecedents. The new assertion is the explicit matching-defect-dependent orbit and **individual basin** classification. No covering exact family theorem was identified in the actual searches. A full extraction of the 2011 paper was unavailable, and an unindexed older result could overlap; the originality judgment is qualified by these limitations rather than stated as a guarantee of historical priority.

## Mathematical value — PASS

The theorem resolves the full finite dynamical classification for a natural infinite family containing the crown graphs and all partial missing matchings. Removing \(k\) independent edges creates \(k\) stationary states but \(k(k+3)/2\) new primitive two-cycles, a meaningful divergence in recurrence complexity. Simultaneously, a single specified oscillation attracts an asymptotic fraction one of random initial states, uniformly even when the missing matching is as large as possible. This exact coexistence of quadratic attractor proliferation and macroscopic basin concentration is a natural dynamical invariant with value independent of the code and verification alone.

## Boundaries and remaining uncertainty

The result does not cover overlapping deleted edges, other local Boolean rules, stochastic updates or nonuniform initial distributions. The research compares accessible earlier statements by implication and does not assert uniqueness from an unsuccessful search. It is a self-contained mathematical proof with finite computational corroboration; there has been no independent external audit.

Self-review: passed. Independent audit: not yet performed.
