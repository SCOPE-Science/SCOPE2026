# Scientific assessment: coextinction-profile nonidentifiability

## Correctness — PASS

The observation is fully defined by the integer histogram of viable-plant counts under every uniformly sampled set of surviving pollinators. The equivalence with independent-retention laws follows from independence of the Bernstein polynomial basis. Pollinator degrees are observed at single-pollinator retention, and plant degrees follow from the displayed triangular binomial inversion; all endpoints and multiplicities are accounted for. The four-by-four witness is certified by direct enumeration of all sixteen pollinator survivor subsets and has opposite four-cycle counts, so equality of laws cannot be a disguised graph isomorphism.

The sharp minimum is certified by an exhaustive graph enumeration: every allowed simple incidence matrix is a sorted tuple of distinct nonzero plant-neighborhood masks, connectedness and distinct column-neighborhood constraints filter exactly the required class, and a complete pollinator-permutation canonicalization identifies precisely the side-preserving isomorphism classes. The checked counts through seven total vertices are 28 nonisomorphic candidates, with no equal-signature pair within a fixed guild-size stratum. The packaged pure-Python checker and exact integer JSON certificate reproduce the entire finite enumeration; a separate deletion enumeration verifies the witness profile.

Residual correctness limits: no general identification claim is made for larger networks; a finite computer-assisted census is not an abstract theorem about all graph orders. All dependencies of the computational claim are embedded.

## Originality — PASS, qualified by source access

Memmott, Waser and Price (2004; doi:10.1098/rspb.2004.2909) introduced and studied the precise one-way pollinator-removal/coextinction mechanism, including random removal; their complete paper does not provide the present inverse-data classification. Bane, Pocock and James (2018; doi:10.1002/ece3.4529) studied robustness under alternative knockout rules and variable extinction sequences, but do not compare entire survivor-count distributions for network reconstruction. Bergold, Hochstättler and Mayer (2022; doi:10.46298/dmtcs.8388) study common-neighbor subset counts, whereas the new invariant records the size of *unions* of neighborhoods at each pollinator subset cardinality. Equality of graph degrees, the mean removal curve, and the stochastic count law are not equivalent statements; the proposed witness satisfies the strongest of these.

The 2008 paper of Boros, Gurvich and Zverovich (doi:10.1002/jgt.20293) concerns graph realization of full neighborhood hypergraphs. Its abstract does not imply the sharp collision result for marginal survivor-count laws, but full text was inaccessible; a reformulation in hypergraph or graph-polynomial language is a residual bibliographic risk. The searches did not establish novelty by absence alone, and an independent full bibliographic check remains required.

## Mathematical value — PASS

The main ecological motivation is the inverse problem underlying randomized species knockouts: can exact, complete extinction-count data identify the interaction network? The theorem proves a sharp answer in the smallest nontrivial connected twin-free setting, and shows that a biologically meaningful motif (a four-cycle representing shared partner redundancy) can be absent or present despite indistinguishable complete random-removal response laws and identical degrees. The degree-recovery lemma specifies what *is* identifiable without any graph-size bound. A result limited to a mean profile would be weaker; this collision survives all conditional distributions and all independent retention probabilities. Scope includes only the binary, unweighted, one-way, uniform-removal mechanism; empirical detectability with finite noisy data is not asserted.

Self-review: passed. Independent audit: not yet performed.
