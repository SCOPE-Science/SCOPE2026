# Independent mathematical audit

## correctness

PASS

Define R=q(q+1)/2 length-two necklaces and H=q(q−1)/2 two-cycles in the order-two de Bruijn directed graph. The explicit pivot/star ordering begins at (0,0), covers q singleton loops and H ordered 2-cycles exactly once, and consecutive classes have one-way connector triples. For arbitrary positive traversal counts t_i, each class cycle is traversed δ_i+ℓ_i t_i before its unique exit connector. Any word with identical length≤3 factor counts starts in the same length-two vertex and traverses the same edge multiset: the directed acyclic ordering of connector classes forces exhaustion before exit; each necklace cycle has unique internal successor, hence a unique Euler trail and 3-abelian singleton. Injectivity in t_i follows from cycle-edge multiplicities. Σδ_i=binom(q−1,2), Σℓ_i=q², giving n0=2q²−q+2 and subfamily generating function z^n0/[(1−z)^q(1−z²)^H]. Near z=1 pole order R dominates any z=−1 pole (order H<R), yielding coefficient n^(R−1)/(2^H(R−1)!)+O_q(n^(R−2)). Karhumäki et al Theorem 6.1 independently supplies O_q(n^(R−1)) for ALL singleton words, so Θ fixed q≥2. Independent separately coded necklace-connector graph and saturated Euler trail recursion verified q=2,3,4; minima lengths 8,17,30 and offsets 0,1,3. This is neither an exact total count nor an all-k theorem.

## originality

PASS

Best-of-knowledge PASS: a constructive lower bound resolving the sharp exponent for fixed factor length k=3 and every fixed alphabet q≥2, using the published upper bound. Conjecture 7.8 of Karhumäki et al explicitly proposes the missing sharp growth generally; the submitted all-q length-two necklace chain and enumerated singleton subfamily contribute the missing half at k=3.

## value

PASS

This supplies the all-alphabet case k=3 of an explicit published sharp-growth conjecture via a mathematically transparent family of uniquely reconstructable words. The independent necklace traversal parameters create the exact exponent and a reusable generating function; that is substantially more than reusing the known upper bound or tabulating a few words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
