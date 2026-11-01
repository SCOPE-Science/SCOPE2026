# Review of the complete-bipartite rendezvous result

## Correctness (C): PASS

The exact expression follows by solving an explicit three-type killed transition system, whose entries are independently checked by full-state rational enumeration. Differentiation after the odds substitution produces a degree-six numerator with exactly one coefficient sign change for all positive part sizes; its signs at zero and infinity force a unique global minimizer, and its value at one bounds that minimizer by one half. A uniform remainder estimate relative to the harmonic-size scale proves the cube-root optimizer and its additive-order-one optimum, including unbalanced growth. Direct passage to the star limit proves the distinct constant optimizer. The standalone checker passed 793 exact/algebraic assertions and three numerical diagnostics; they complement the proof, not replace it. Boundary cases \(K_{1,1}\), part size one, and nonmeeting at zero holding probability are explicitly included.

## Originality (O): PASS, subject to historical priority uncertainty

The 2015 full open-access article by Ohwa already contains the general two-walker Markov-chain recurrence and continuous-time star calculations; these are credited rather than rebranded. Its graph-specific sections treat stars, cycles and complete graphs, not the explicit opposite-start \(K_{a,b}\) synchronous discrete-time optimized-laziness law. The full arXiv text of Kanade–Mallmann-Trenn–Sauerwald (2016) concerns coalescence bounds and star orders; the full arXiv text of van Belle–Klimovsky (2024) gives spectral representations without this global optimization or the cube-root/constant transition. The present claim is thus not established by the statements inspected in the closest accessible primary works. The general recurrences can generate the finite expectation algebraically, but they neither state nor immediately imply the unique optimizer and its sharp asymptotics. The 2023 Warwick thesis had an inaccessible full PDF, so no claim about its uninspected contents is made. The possibility of a separate earlier exact biclique result is a residual literature risk.

## Value (V): PASS

This supplies a complete parameter-level optimization rather than an isolated small-graph computation. Bipartite periodicity makes zero laziness fail to produce any meeting, yet imposing conventional one-half holding loses one-quarter of leading efficiency on balanced bicliques. The sharp cube-root law explains the nontrivial optimal amount of aperiodicization as both parts grow, while the star limit demonstrates that one small part changes the mechanism. The graph family and invariant are natural for independent-search rendezvous; the conclusion could guide synchronous search and mixing protocols without asserting a universal graph theorem.

## Scientific limitations and comparison risk

The walkers must be independent, identically lazy, synchronous and initially in opposite parts; only vertex coincidences count. No adaptive or continuous-time optimization is asserted. The general product-chain recursion is prior art, and some plausible further literature may not be indexed or accessible.

Self-review: passed. Independent audit: not yet performed.
