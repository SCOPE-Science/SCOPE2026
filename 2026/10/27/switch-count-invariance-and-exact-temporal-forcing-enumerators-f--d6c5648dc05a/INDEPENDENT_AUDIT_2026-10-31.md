# Independent mathematical audit

## correctness

PASS

For a matching M, its one-step infection closure F_M is union-preserving and idempotent. Thus collapsing repeated identical snapshots leaves the final set unchanged; an alternating sequence of two perfect matchings is specified by the first color and r=1+#switches. On a 2m-vertex alternating-cycle component, the first occupied matching edge i infects a contiguous 2r-vertex interval after r compressed snapshots (capped at 2m). A union of these intervals covers the component iff the cyclic gaps between nonempty first-matching edges are all ≤r. Counting occupied edge sets by marking one edge and distributing m as s gaps of sizes 1..r yields C_{m,r}(s)=m/s[x^{m-s}](1+...+x^{r−1})^s; the three nonempty seed patterns per occupied matching edge contribute 2z+z², hence the product all-cardinality polynomial. The minimum successful number is Σ ceil(m_j/r), with minimum-count Π 2^{s_j}C_{m_j,r}(s_j); shared matching edges (m=1), r≥m, and zero snapshots are handled distinctly. Under independent initial vertex infection, each first-matching edge is occupied with probability q=1−(1−p)², and the maximal vacant run has asymptotic length log(m)/(−log(1−q)) by disjoint blocks and union bound. Independent simulation of all 2^(2m) initial sets for m=1..5 across multiple schedules reproduced every full final set, success criterion and polynomial coefficient, without substituting finite tests for the general proof.

## originality

PASS

Best-of-knowledge original contribution as delimited by the final assigned theorem, not novelty of its foundational method. Direct original statements and implications were compared against the checked primary results and the published-finding search. Highly relevant inaccessible works remain named as residual priority risks; no failed search or abstract alone proves whole-document noncoverage.

## value

PASS

A natural family of temporal propagation graphs collapses from arbitrarily long schedules to the initial matching and a single switch-count statistic. The theorem goes beyond minimum-size zero forcing, giving a factored all-cardinality enumerator, precise extremizer multiplicities and a probability asymptotic. Those are independently useful exact invariants for temporal infection and controllability questions, and the restriction to two fixed perfect matchings is motivated by their decomposable alternating-cycle geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
