# Scientific review: order-five de Bruijn circular attractors

## Correctness

PASS. The proof establishes a universal lower bound of seven by counting the \(32\) unique length-five windows and five windows per selected position. Every cyclic order-five de Bruijn word is represented exactly once by a depth-first enumeration of Hamiltonian cycles of five-bit windows anchored at the unique all-zero vertex. All seven-position candidates that can cover the unique length-five windows are precisely the \(384\) circular-gap-bounded seven-subsets. Exact short-factor incidence masks give a necessary-and-sufficient test for covering every remaining factor, and any longer factor is automatically crossed after the length-five test. The executable finite certificate exhausts all \(2048\) words, reproduces the six numerical census claims, and independently checks all factor lengths for all candidate subsets on the six extreme words. It does not infer statements about arbitrary orders.

## Originality

PASS within the examined literature. The primary 2026 small-attractor classifications address linear Fibonacci and period-doubling words. Mantaci et al. (2021, Section 6.2, Proposition 41) give linear de Bruijn asymptotic estimates, not this circular finite census. Romana (2023) gives general decision algorithms; Whittington (2024, Section 5, Theorem 5.22) proves a prime-order result only for one specially constructed and unfolded Lyndon de Bruijn sequence, leaving general de Bruijn behavior as an explicit question. The exact order-five circular all-cycle conclusion and especially the optimizer-count distribution do not follow from those results. Searches for equivalent formulations and published finite tables found no covering assertion, but possible unindexed tabulations or older equivalent descriptions remain a priority risk.

## Value

PASS. This is a complete exact cutoff on a canonical, mathematically closed finite class of \(2048\) nonisomorphic-by-rotation universal cycles. The fifth order is the first sizeable odd-prime order beyond the smallest de Bruijn examples; every sequence meets the sharp information-theoretic lower bound even though the number of optimal position sets varies substantially, from \(216\) to \(368\). That variation is important when evaluating rigidity and abundance of optimal attractors and is not captured by the minimal size alone. The finding is finite and self-contained, not an arbitrary sample or a claim of broad asymptotic progress.

## Closest work and residual uncertainty

See the four primary works listed in RESULT.md. A different, unpublished or unindexed classification of the exact finite family is not excluded. All numerical claims were reproduced from the standalone checker, not a reference table.

Self-review: passed. Independent audit: not yet performed.
