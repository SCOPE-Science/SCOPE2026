# Scientific review

## Correctness

**PASS.** The directed-edge recurrence counts each infected person once, includes the probability of a failed contact back to the already infected parent, and terminates on a finite tree. The center-rooted canonical parenthesis representation gives one representative per tree isomorphism class; attaching all possible leaves generates all trees inductively. Exact rational arithmetic checked all \(1301\) unlabelled trees at order \(13\) and all lower orders. Independent weighted-path summation checked the exact \(14\)-vertex witness vector and its positive \(1/576\) gap.

## Originality

**PASS, with discovery risk.** The one-contact infection chain is equivalent to a simple random walk stopped just before its first attempted vertex revisit. Tishby, Biham and Katzav (arXiv:1606.01560) study precisely that stopping mechanism for randomly seeded Erdős–Rényi ensembles. Their ensemble distribution does not establish the fixed-tree, vertex-specific leaf-optimality boundary. Kenah and Robins supply general SIR outbreak-network theory; Gómez and colleagues use reinfecting one-contact dynamics and stationary outcomes; Enright and Kao study a different exact outbreak-size computation on time-expanded DAGs. None of the inspected primary full texts gives or implies the sharp order-14 classification. Equivalent unindexed fixed-tree results remain a residual possibility.

## Value

**PASS.** Maximizing spread from one deliberately chosen seed is a natural centrality/epidemic-control question. A strict internal optimum appears at a precisely identified first network order even though every smaller tree has some optimal leaf. The margin is small but the existence and sharp minimum order are qualitative structural facts, and the exact enumeration rules out smaller counterexamples. No applied impact claim is made.

## Scope and limitations

Connected simple unweighted trees; one randomly chosen neighbor per infected individual, one infectious attempt, permanent removal, and a deterministic initial seed. This is not a theorem about general cyclic graphs, classical multi-contact SIR, or non-backtracking walks. Verification uses complete finite enumeration for the lower bound and an analytic recurrence plus explicit exact instance for the upper bound; no infinite census is asserted. Independent review is outstanding.

Self-review: passed. Independent audit: not yet performed.
