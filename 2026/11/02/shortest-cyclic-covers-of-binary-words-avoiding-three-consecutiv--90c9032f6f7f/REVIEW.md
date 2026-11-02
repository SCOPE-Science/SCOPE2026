# Scientific review

## Correctness — PASS

The claim fixes linear target factors avoiding \(000\), while permitting arbitrary cyclic covering words. The full de Bruijn graph includes forbidden arcs, so the dual lower bound applies to every possible competitor. Every required arc has multiplicity at least one in a cover, and subtracting its indicator leaves a nonnegative balancing flow. The exact potential inequalities give a lower bound on its total mass. `CERT.json` and `verify.py` check that an explicit balancing flow attains that lower bound at each of the fourteen orders, while the explicit cyclic witnesses have exactly the prescribed edge multiplicities. The check returned `VERIFY_OK`, including independent direct enumeration for the two smallest orders. No infinite-order statement is made.

## Originality — PASS, with priority qualifications

The closest prior mathematical frameworks are the universal-pattern cycles of Burstein and Kitaev (2003), the lexicographically least restricted-language cycles of Moreno and Matamala (2004/2007), and the maximum-distinct-window RLL sequences of Chee et al. (2024). Full-text comparisons show different families or opposite optimization objectives: in particular, the linear \(000\)-free target family is not the cyclic-closed admissible necklace family. Targeted public literature and mathematical-result-record queries for the exact profile and its equivalent circulation formulation disclosed no established values or stronger theorem implying this fourteen-order minimum-length result. This search does not establish universal historical priority. The most significant residual concern is an unindexed table or a general shortest-superstring algorithm already used to compute precisely these values.

## Value — PASS

The invariant is the shortest cyclic superstring of an entire natural finite-type binary language, not an arbitrary slice or isolated numerical curiosity. The target family has tribonacci growth and nonbalanced overlap arcs, so unlike a conventional de Bruijn cycle an exact-once traversal fails from order four onward. The exact profile through sixteen measures the synchronization/overcoverage penalty and shows, unexpectedly, that forbidden extra windows do not improve the optimum at any of these orders. Integer dual certificates plus complete witnesses make all fourteen optima reusable as benchmarks for constrained universal cycle and shortest-superstring studies. This is a finite exact classification of one optimization profile, not a claim about all orders.

## Closest sources and limitations

Burstein–Kitaev, arXiv:math/0311399v1, focuses on pattern graphs (especially Section 3, Theorem 3.8 and Corollary 3.11). Moreno–Matamala, arXiv:0711.1695v1 and WG 2004 preprint, defines “minimal” lexicographically and uses periodic language constraints. Chee et al., arXiv:2403.01454v2, analyzes maximum-length sequences of distinct run-limited windows. Results above order sixteen and other forbidden factors remain open here; independent publication-priority investigation is not complete.

Self-review: passed. Independent audit: not yet performed.
