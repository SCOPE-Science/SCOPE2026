# Independent mathematical audit

## correctness

PASS

The two endpoint-count state is complete because consecutive length-three windows overlap in exactly one endpoint bit. For read symbols zero through three, the four transitions are respectively \((p,0)\), \((p+q,p)\), \((q,p+q)\), and \((0,q)\). With \(S=p+q\) and \(M=\max(p,q)\), induction gives \(S\le F_{j+3}\) and \(M\le F_{j+2}\). Equality excludes symbols zero and three; after the first one or two, every later equality step must add the currently larger coordinate, forcing the read vector to remain constantly one or constantly two. Fresh exhaustive reconstruction through \(m=7\) reproduced maxima \(3,5,8,13,21,34,55\) and exactly those two maximizers. The all-length theorem rests on the induction and equality analysis.

## originality

PASS

The primary transverse-read paper introduces exactly the \((3,2)\) model and explicitly draws the nondeterministic two-state machine underlying the shared endpoint bit. It then determinizes that machine to count distinct valid read vectors and derive capacity. Counting outputs once loses source-path multiplicity, so that capacity result does not determine the largest fiber. The audited label-specific multiplicity recurrence and its sharp Fibonacci optimization therefore answer a different natural invariant of the same channel. Current Resultary searches for maximum fiber, preimage multiplicity, ambiguity, and the exact Fibonacci law returned no covering theorem.

## value

PASS

Worst-case ambiguity is the natural zero-error list-size counterpart of output capacity for a many-to-one read channel. The theorem gives its exact all-blocklength law and unique maximizers in the first nontrivial odd-window model, providing a reusable benchmark for decoding ambiguity rather than a small finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
