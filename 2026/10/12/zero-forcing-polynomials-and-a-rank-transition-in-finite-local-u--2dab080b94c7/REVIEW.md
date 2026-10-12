# Review

## Correctness

PASS. Unit status in a finite local ring is detected modulo the maximal ideal, yielding equal residue fibers of size \(s\). In residue characteristic \(2\) the graph is complete \(q\)-partite; in odd residue characteristic its complement is one clique together with \((q-1)/2\) complete bipartite components. Every fiber is a twin class, so two white vertices in one fiber are impossible in a zero forcing complement. Three white fibers stall immediately in both parity regimes, while every pair of white fibers has an explicit first force. This proves the complete three-term polynomial. The parameter inversion is exact. The real rank witnesses are explicit; the only nontrivial lower bound, for even \(q\ge4\), follows because each part would require a distinct isotropic line in a rank-two bilinear model, while a real nondegenerate symmetric form in dimension two has at most two such lines.

The packaged verifier independently constructs four representative rings, exhaustively checks the full polynomial, replays all rank witnesses with exact rational row reduction, and tests the parameter inversion.

## Originality

PASS for the strengthened combined claim. The 2010 and 2014 unit-graph papers supply the graph and classical structural invariants but not zero forcing or minimum rank. The 2018 zero-forcing-polynomial paper already gives the complete multipartite formula, so the characteristic-two polynomial specialization is prior and is not counted as standalone novelty. The 2004 rank-two classification broadly covers the low-rank graph structure. A recent dominant-metric paper gives the residue-fiber decomposition and a different deletion theorem, with no zero-forcing or minimum-rank statement.

The searched literature and semantic database did not locate the local-ring-wide standard zero forcing classification, the exact parameter recovery from this polynomial, or the sharp transition \(Z=M\) versus \(Z=M+1\) at even residue-field orders at least \(4\).

## Value

PASS. The theorem gives a complete forcing census for a standard algebraic graph class and proves that the polynomial is a complete graph invariant within finite local nonfields. The fact that the polynomial has the same form across residue parity while minimum rank changes exactly in one arithmetic regime isolates a genuine boundary between forcing and inverse-eigenvalue behavior rather than merely recomputing a known graph invariant.

Self-review: passed. Independent audit: not yet performed.
