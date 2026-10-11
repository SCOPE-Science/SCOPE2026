# Independent mathematical audit

## correctness

PASS

The proof was reconstructed directly. For a nonempty complement \(T\), restrained domination requires \(T\) to meet both bipartition sides. Let \(a\) be the least \(A\)-class met by \(T\) and \(b\) the greatest \(B\)-class met by \(T\). Nesting of neighborhoods makes the condition on every \(T\cap A\) vertex equivalent to the prefix \(B_1\cup\cdots\cup B_a\) containing at least one vertex of \(T\) and at least one of \(S\); dually, every \(T\cap B\) vertex is handled exactly by the corresponding suffix \(A_b\cup\cdots\cup A_p\). These are necessary and sufficient. Once \((a,b)\) is fixed, the two side choices are independent and the three relative-order cases \(b<a\), \(b=a\), \(a<b\) give exactly the stated \(E_m\) and \(P_m\) factors without double counting. I independently replayed exhaustive definition-versus-formula checking for all canonical profiles with \(p\le4\), class sizes in \(\{1,2,3\}\), and total order at most 11: 540 profiles and 687,124 subsets with no mismatch. The finite replay is supplementary only.

## originality

PASS

Pandey--Panda's primary arXiv paper was inspected at its public full bibliographic/abstract material: it gives polynomial-time algorithms for the minimum restrained-dominating-set problem on chain graphs, so the minimum parameter is prior art. The 2019 restrained-domination-polynomial paper's accessible abstract lists complete graphs, complete bipartite graphs, paths, cycles, and certain \(K_2\)-products; the complete-bipartite case is the \(p=1\) specialization and is treated as prior. No checked source or Resultary record gives the all-set prefix/suffix classification or full polynomial for arbitrary chain graphs. Open routes did not expose the 2019 full body; one authorized institutional retrieval attempt returned an operational error and was not retried or bypassed, leaving an explicit bibliographic risk rather than causing failure.

## value

PASS

The result upgrades a known minimum-optimization problem to a complete structural classification and full polynomial for a natural hereditary bipartite class. The prefix/suffix boundary description is reusable, and the formula gives every cardinality count, the minimum, and the number of minimum sets. This is a natural complete enumerative classification rather than an isolated coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
