# Self-review

## Correctness — PASS

For the exact domain of simple wheels with at least three rim sites and synchronous loopless neighbor-XOR over \(\mathbb F_2\), the polynomial representation of the update is explicit. The odd-ring injectivity argument uses the simple \(z+1\) factor and nonzero augmentation of the all-ones polynomial. For even rings, the Chinese remainder decomposition separates the invertible complementary factor from the hub-coupled primary factor; the latter has exact power ranks \((3,2,1,0)\) when \(e=2\), \((5,2,1,0)\) when \(e=4\), and \(e+1,e-2,e-4,e-6,\ldots,0\) when \(e\ge8\). Those ranks fix every nilpotent Jordan length and thus every first-entry shell. Matrix-rank checks at \(3\le n\le128\) and exhaustive trajectories for \(3\le n\le16\) corroborate the claim with separately implemented methods, but are not used as an infinite proof. All boundaries and quantifiers are specified in `RESULT.md`.

## Originality — PASS, with residual risk

No checked previous finding or targeted mathematical-research search established the wheel-specific characteristic-two nilpotent Jordan partition and complete first-entry distribution. The nearest analogous records concern parity automata on distance-two Boolean cubes, complete multipartite graphs, and modular Laplacian boundary dynamics, whose exact mathematical claims do not imply the wheel result. Rowland–Yassawi studies infinite cellular-automaton column sequences, not the present finite-wheel dynamics. Abu-Jeib's integer wheel determinant **does imply** invertibility on odd-rim wheels after reduction modulo two; this is explicitly treated as an established implication, not a separate novel observation. The full Abu-Jeib spectrum concerns characteristic zero and does not itself state characteristic-two elementary divisors. Fran–Saputri–Kiftiah studies when modular-two adjacency products are graphical, not full powers or stopping-time counts. A historical treatment of modular wheel Jordan forms could still subsume the theorem; literature-index incompleteness and indirect algebraic implications remain residual risks.

## Mathematical value — PASS

The family \(K_1\vee C_n\) naturally probes how a single universal coupling vertex changes the arithmetic of linear cellular-automaton relaxation. The full nilpotent partition, rather than merely determinant or kernel dimension, identifies the sharp first-entry time and every initial-state shell. The surprising transition at the first two dyadic valuations—one length-three block for \(e=2\), three blocks for \(e=4\), and two equal long blocks plus a singleton for \(e\ge8\)—is a complete classification for an infinite graph family and yields a parameter-universal probability law for fixed dyadic part. This is more than a normal-form restatement, a tiny numerical improvement, or a finite census.

## Closest literature and limits

Rowland and Yassawi (arXiv:1209.6008) supplies a general finite-field cellular-automaton context. Abu-Jeib (2006, DOI 10.35834/2006/1802142) supplies previously known wheel integer determinant and real spectrum. Fran, Saputri and Kiftiah (2021, DOI 10.34312/jjom.v3i2.10468) supplies directly related modular wheel matrix products. None of the checked full-text results states the new partition or cumulative first-entry law. The eventual periods in the invertible primary component are not classified, and the new result remains subject to independent historical and mathematical audit.

Self-review: passed. Independent audit: not yet performed.
