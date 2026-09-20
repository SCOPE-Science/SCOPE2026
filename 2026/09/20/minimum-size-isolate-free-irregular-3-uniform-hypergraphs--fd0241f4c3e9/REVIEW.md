# Review: minimum size of isolate-free irregular 3-uniform hypergraphs

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The lower bound is forced by two exact facts: an isolate-free irregular hypergraph has n distinct positive degrees, whose sum is at least n(n+1)/2, and a 3-uniform hypergraph has total degree 3|E|.

The construction was checked algebraically case by case modulo 6. In each induction step a new vertex x is added and a simple graph F on old vertices is used as its link, so every edge uv of F creates exactly one new triple xuv. This preserves 3-uniformity and simplicity. The number of new triples is exactly M_n-M_{n-1}. The specified F-degrees transform D_{n-1} into D_n, including the two divisibility-correction residue classes n = 1,4 mod 6. The special path-plus-matching construction is valid already at n=7, its smallest case. No vertex is isolated because every target degree is positive.

A standalone construction checker verifies all orders n=6,...,200 and checks the exact degree set, simplicity, number of vertices, edge count, and degree-sum identity. The proof is general and does not depend on this finite computation.

Adversarial checks considered duplicate triples, collision of the new degree with old degrees, insufficient vertices for the matchings, the n=7 boundary case, and the maximum-degree feasibility of n+1 in the corrected degree set. None produces an exception.

## Originality

**PASS, to the best of our knowledge.**

The main older source checked was Gyárfás–Jacobson–Kinch–Lehel–Schelp (1992). It defines irregular hypergraphs, exhibits the six-vertex seven-edge 3-uniform example, proves existence for r >= 3 and n >= r+3, and explicitly notes that its inductive construction may have one isolated vertex but can be altered to remove it. The checked construction/existence section does not give a fixed-order minimum-edge theorem for isolate-free irregular 3-graphs.

Behrens et al. (2013) was checked as broader degree-sequence context. Its stated problems and main early results concern characterizations and sufficient conditions for k-graphic sequences and edge exchanges, not the present fixed-order sparse extremum. Li–Miklós studies dense irregular 3-uniform degree sequences, with degrees on the quadratic scale in n, rather than the sparse linear-scale sequences here.

Searches used exact and synonymous formulations including irregular 3-uniform hypergraph, irregular 3-graph, minimum size/number of edges, no isolated vertices/isolate-free, degree sequence 1,...,n, the corrected degree sequence 1,...,n-2,n,n+1, and the candidate formula ceil(n(n+1)/6). No equivalent statement or stronger theorem implying the exact fixed-order minimum was located. The current SCOPE archive was also checked by object and claim family before publication.

Residual originality risk remains because older degree-sequence and set-system literature is fragmented, and an equivalent sparse realizability statement could appear without the word "irregular". The claim is therefore explicitly limited to the best of our knowledge.

## Value

**PASS.**

The result turns the unavoidable degree-sum lower bound into an exact formula for every admissible order and supplies a uniform recursive realization. The construction also identifies a clean modular phenomenon: four residue classes realize the consecutive positive degree set exactly, while the two obstructed classes require only a two-unit correction to the degree sum. The link-graph induction is elementary and reusable for related prescribed-degree constructions.

## Scientific limitations

- Isolated vertices are excluded; allowing them changes the extremal problem and is not addressed.
- All minimum-size isomorphism classes are not classified.
- No analogue for arbitrary uniformity r is claimed.
- Originality remains subject to the possibility of an equivalent result in older or differently indexed hypergraph degree-sequence literature.

## Sources checked

- Gyárfás, Jacobson, Kinch, Lehel, Schelp (1992), *Irregularity Strength of Uniform Hypergraphs*, especially the direct construction section and Theorem 3.3.
- Behrens et al. (2013), *New Results on Degree Sequences of Uniform Hypergraphs*, introduction and degree-sequence framework.
- Li and Miklós, *Dense, irregular, yet always graphic 3-uniform hypergraph degree sequences*, abstract and stated main regime.
