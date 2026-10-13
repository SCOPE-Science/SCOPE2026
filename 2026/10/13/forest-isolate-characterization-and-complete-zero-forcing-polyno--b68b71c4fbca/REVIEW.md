# Scientific review: zero forcing of triangular graphs

## Correctness — PASS

The identification of line-graph vertices with edges of the complete graph is exact. For any black edge \(uv\), its still-white neighbors are precisely the remaining white edges incident to \(u\) or \(v\), counted without overlap. A legal force therefore removes a leaf edge in the white-edge graph using an isolated vertex as an anchor. The first-move obstruction and the impossibility of deleting the first edge of a cycle prove necessity. Repeated leaf deletion with a fixed isolated anchor proves sufficiency for every size and order. Cayley's formula and the labeled exponential formula yield all coefficients; the extremal cases are counted without asymptotic assumptions. A separately implemented direct forcing check agrees with a disjoint-set forest test and exact forest enumeration on every one of 33864 configurations for orders 3–6. These computations corroborate, but are not the infinite proof.

## Originality — PASS, with specified residual uncertainty

The closest direct earlier statement, Eroh–Kang–Yi (arXiv:1207.6127, Proposition 3.5), supplies the scalar \(Z(L(K_n))\) from the 2008 foundational paper, not an all-set characterization. The 2016 Fallat–Soltani theorem on Hamiltonian-path line graphs is **broader in graph class but only a minimum-number statement**, so its implication to the present scalar minimum is acknowledged, not treated as novelty. The 2015 compressed-cliques paper determines a positive-semidefinite forcing minimum of \(J(n,2)\), whose color-change rule is different. The inspected 2018 zero-forcing polynomial paper treats the polynomial generally and lists several other evaluated families, without a triangular-graph enumeration in its relevant theorem sections. Actual searches included names \(T_n\), \(L(K_n)\), \(J(n,2)\), triangular graphs, spanning forests, isolated vertices, and the zero-forcing polynomial. The complete 2008 foundational article was inspected via a public copy: Proposition 4.9 proves a minimum-rank equality and the corresponding scalar, not the forest-isolate membership test. Earlier or later equivalences under alternative vocabulary remain a residual risk. Absence from a search index is not proof of novelty.

## Value — PASS

Instead of giving another extremal scalar already covered by the literature, the result classifies **every** forcing initial condition in a classical distance-regular graph family by an easily testable combinatorial property. It evaluates the entire size enumerator via Cayley trees and supplies the exact number of optimal initial sets. The same characterization determines the largest failed initial sets and all mixed forcing/nonforcing cardinalities; their count is unbounded across this natural family. This structural and enumerative information is not entailed by previously established minimum cardinality formulas.

## Scope and status

The classification assumes ordinary forcing and \(n\ge3\). A differently indexed published or unpublished equivalent enumeration cannot be entirely ruled out. No claims are made about positive-semidefinite, skew or connected zero forcing, or forcing times.

Self-review: passed. Independent audit: not yet performed.
