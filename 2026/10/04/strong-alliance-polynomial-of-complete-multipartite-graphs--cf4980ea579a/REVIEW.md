# Independent mathematical audit

## correctness

PASS

For a selected vertex in part \(V_i\), the exact internal and external neighbor counts are \(s-s_i\) and \((N-n_i)-(s-s_i)\); the strong defensive condition is therefore exactly \(s-s_i\ge\lceil(N-n_i)/2\rceil\). Summing over occupied parts yields the half-order lower bound. Adding one vertex can only preserve or improve every relevant cross-part count, proving upper closure. Under deletion from part \(k\), every other occupied-part slack falls by one while the surviving \(k\)-part slack is unchanged; requiring every deletion to fail is therefore equivalent to at least two tight occupied parts. For fixed size \(s\), the criterion is precisely the stated partwise capacity bound, giving the coefficient-extraction formula. Evaluating capacities at half order gives the parity law for the minimum. Double counting cover relations in the upper ideal gives the normalized level-density inequality. I independently brute-forced the literal adjacency criterion against the capacity criterion on several nontrivial multipartite profiles; the inspected package verifier exhausts all ordered profiles through total order nine and separately checks the known complete-bipartite specialization.

## originality

PASS

The complete foundational strong-alliance-polynomial preprint was inspected. It defines the invariant and computes paths, cycles, complete graphs, stars, complete bipartite graphs and double stars; Theorem 3.3 gives the exact complete-bipartite factorization. It does not treat arbitrary complete multipartite graphs. The submitted theorem recovers that two-part boundary case but adds an all-part capacity classification, complete polynomial, inclusion-minimal characterization and parity minimum law. Targeted Resultary search returned the audited arbitrary-multipartite result as the exact hit and no earlier equivalent theorem.

## value

PASS

Complete multipartite graphs are a canonical graph family, and the strong alliance polynomial is the defining all-cardinality refinement of the minimum alliance number. The theorem classifies every contributing set, every inclusion-minimal set and the exact minimum across arbitrary part profiles, while strictly extending the foundational complete-bipartite formula. That is a natural complete classification rather than an arbitrary finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
