# Independent mathematical audit

## correctness

PASS

For a binary order-n de Bruijn cycle, the feedback permutation has 2^(n-1) entries with two fixed endpoint bits. Cross-joining two full cycles exchanges successors in two conjugate-state pairs and toggles exactly two interior feedback bits. Relative to any clique vertex, the pairs toggled to all other vertices form a pairwise-intersecting family of 2-subsets of q=2^(n-1)-2 coordinates. Such a family is either a star (size <=q-1) or a triangle of at most three edges; hence omega<=q for every n>=4. For n=5, independently enumerated all 2^16=65536 feedback masks by their exact 32-state successor orbits, obtaining 2048 full cycles. Every 14-clique must be a rooted star: 224 valid (mask,common-coordinate) witnesses were enumerated, and each clique is counted exactly fourteen times, so exactly 16 distinct K14. At n=4, 16 valid masks and 24 rooted witnesses give 4 K6. A separate 6-mer-factor intersection check verified all pairs in the 16 constructed order-5 cliques. Finite exhaustive n=4,5 enumeration verifies only those orders; the universal n>=4 bound follows from the 2-subset lemma.

## originality

PASS

Connectivity and Hamiltonicity are not equivalent to or sufficient for the maximum complete-subgraph count. The feedback-coordinate star classification is a stricter invariant. Broader generality in connectivity and local perturbation degree does not dominate the global clique number and exact 16-subset census; degrees do not determine all common-neighbor intersections. The statement omega=14 and 16 K14 subgraphs is a finite natural exact invariant; no inspected existing exact table supplies this number. Lack of matching database is not proof of novelty. Prior structural ingredients can motivate the proof; they do not in the cited theorems establish the new all-n bound or exact order-five clique count. Best-of-knowledge PASS with specifically identified historical-priority risks; an unsuccessful search is not proof of novelty.

## value

PASS

The graph of cross-joins is a natural object for nonlinear-feedback sequence generation. Its general clique bound and complete small-order extremal classification supply exact simultaneous cross-join structure not recovered from connectivity, degrees, or pairwise perturbation counts. The order-five census covers all 2048 cycles and is mathematically motivated rather than an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
