# Independent mathematical audit

## correctness

PASS

For the precisely defined pair of 16-vertex SRG(16,6,2,2) graphs, CF3(G) consists of ALL vertex masks excluding every induced triangle. I independently enumerated each graph and 32 triangular masks, all 2^16 subsets: augmented face totals 8951 (Shrikhande) and 7343 (rook), including the empty simplex. The deterministic 0..15 toggle matches 4466/3658 pairs; an independently constructed oriented Hasse DAG topological sort exhausts all 8951/7343 vertices, proving acyclicity. Critical counts are 5 dimension-five and 14 dimension-six cells for Shrikhande, 21 dimension-five and 6 dimension-six for rook, plus the critical vertex after discarding the empty vertex pair. Independent exact Morse boundary elimination gives an integer 5x14 matrix with a +1 rank-five minor and 21x6 with -1 rank-six minor, respectively; primitive integral Smith factors give free reduced homology Z^9 in degree6 and Z^15 in degree5. A one-vertex CW model with cells only dimensions five/six has attaching classes classified by their integral degree vectors (pi5 wedge S5=Z^r) and unimodular cancellations, yielding the claimed wedges of spheres. The scope excludes other SRGs and equivariance.

## originality

PASS

The CF3 triangle-exclusion complex is strictly distinct from the ordinary independence complex CF2. Primary clique-free shellability results are conditional on chordality/diamond-freeness or clique attachments and do not give either 16-vertex homotopy type. The paired exact six-vs-five dimensional homotopy classification appears new at best knowledge, while related published ordinary independence values do not imply it.

## value

PASS

A natural controlled counterexample to the idea that equal strongly regular parameters or equal triangle totals determine higher clique-free topology: these two classical nonisomorphic graphs have identical (16,6,2,2), 32 triangles and face counts through dimension2, but sphere-wedge homotopy lives in different dimensions. The exact finite two-object classification is mathematically motivated and reusable, not an arbitrary cut of an infinite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
