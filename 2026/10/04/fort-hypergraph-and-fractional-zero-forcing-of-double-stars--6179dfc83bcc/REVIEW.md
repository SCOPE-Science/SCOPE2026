# Review of Fort hypergraph and fractional zero forcing of double stars

## Correctness
PASS. Any minimal fort cannot contain a center, because including a center forces all leaves on that side into the fort and therefore contains a proper two-leaf fort. With both centers outside, each same-side leaf count must avoid one; minimality therefore leaves exactly two leaves on one side. The fort hypergraph is consequently \(K_a\sqcup K_b\). Standard matching, fractional vertex-cover, and vertex-cover calculations then give the fort number, fractional zero forcing number, optimizer classification, and ordinary zero forcing number. Exhaustive fort enumeration, direct color-change simulation, and LP face checks agree for all \(2\le a,b\le6\).

## Originality
PASS. The primary 2023 source introduces the fort hypergraph and LP fractional zero forcing, proves the general tree upper bound \(Z^*(T)\le\ell(T)/2\), and characterizes equality with the integral zero forcing number, but targeted full-text searches found no double-star or bistar theorem. Later IP-model work provides computational methods and experiments, not this closed structural formula. Semantic and exact-phrase searches found no equivalent double-star fort-hypergraph classification or optimizer theorem.

## Value
PASS. Double stars are the canonical diameter-three trees with two branching vertices. The result makes the general tree upper bound sharp throughout this family while the integral zero forcing number can be almost twice as large, yielding a transparent near-factor-two integrality gap on a very simple tree class. The full optimizer classification and exact fort hypergraph also explain the mechanism rather than merely reporting a scalar value.

Same-model review: passed. Independent audit: not yet performed.
