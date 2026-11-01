# Scientific review

## Correctness — PASS

The all-parameter nullity identity is proved by expressing the complemented 2-factor operator as \(F=J+B\), with \(B=I+A_H\), and reducing each deleted cycle block of \(B\) to multiplication by \(x^{-1}(x^2+x+1)\) in the cyclic quotient. The exact gcd degree is \(2\min(t,2^{\nu_2(n)})\) if the cycle length is divisible by three and zero otherwise. Since \(BJ=JB=J\), even total order gives the invertible factor \(I+J\) and odd total order gives one extra zero mode on the all-ones line. Fitting decomposition then supplies the exact first-periodic-entry counts, while the specialization to two length-\(3\cdot2^s\) cycles proves the linear sharp transient and its exact final-layer fraction.

The source programs in `verify/rank_verifier.py` and `verify/orbit_verifier.py` were replayed from their packaged locations. They checked 2,094 graph-parameter multisets by independent GF(2) rank computations and 83,136 binary labelled states by direct graph iteration, respectively. The tested finite ranges do not substitute for the analytic proof. No assumption of finite exhaustive tests proving an infinite family is made.

## Originality — PASS, with historical-priority risk

Martin, Odlyzko and Wolfram (1984) develop the older polynomial-factorization theory of additive dynamics on cyclic rings; the individual \(x^2+x+1\) resonance is therefore not asserted to be newly discovered. Ciandrini et al. (arXiv:0809.1526v1, 2008) analyze graph XOR dynamics and feedback loops. Ogihara and Uchizawa (2020) study reachability, cycle-length complexity and predecessors for general XOR networks. The relevant inspected sections and results do not give the complete kernel-power ranks and first-entry populations for arbitrary complements of spanning disjoint cycles. Standard power-rank and Fitting facts are prior mathematical tools, not the claimed new contribution.

The claimed gap is the explicit evaluation of the densely coupled family, including a rank-one coupling invariant and sharp linear delay attained by a fixed proportion of initial states in asymptotically complete graphs. A general arbitrary-matrix algorithm is not an explicit classification of this graph family. No equivalent or stronger covering formula was identified in the considered sources or available similarity comparisons. An unindexed or inaccessible equivalent classification, or a stronger result under a different name, remains possible. This is a self-review, not a priority certificate.

## Mathematical value — PASS

The object is the natural complement of a spanning 2-factor; the observable is the exact time for arbitrary initial states to enter a periodic orbit under elementary synchronous parity evolution. The structural law depends on only a cubic-root divisibility condition and powers of two, and it describes the complete preperiod census for any component lengths. A striking counterfamily deletes only a vanishing fraction of the complete graph's edges yet changes an everywhere-periodic invertible map into one with a sharp transient of \(N/6\) steps experienced by \(15/16\) of binary initial states. This identifies a concrete boundary for connectivity- or density-only heuristics and supplies a useful exact benchmark for graph-coupled linear dynamics.

## Scope and closest comparisons

The theorem is limited to characteristic two, the stated graph family, synchronous self-exclusive unweighted neighbor summation, and first-entry rather than exact eventual primitive periods. The closest generic literature does not by itself certify historical novelty; source-inspection extent and unresolved priority risks are documented in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
