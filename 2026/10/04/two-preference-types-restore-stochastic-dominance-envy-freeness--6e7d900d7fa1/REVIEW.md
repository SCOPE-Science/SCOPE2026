# Same-model scientific review

## Correctness
**PASS.** The all-\(n\) proof is symbolic. For every agent and every top-\(k\) set, being among the first \(k\) priority positions guarantees receipt of a top-\(k\) object, giving probability at least \(k/n\). With two preference types of multiplicities \(r,s\), equal treatment of equals gives lotteries \(x^A,x^B\), while bistochastic feasibility gives \(r x^A(T)+s x^B(T)=k\) for each \(k\)-object top set \(T\). Combining these identities yields \(x^A(T)\ge x^B(T)\), and symmetrically for type \(B\). This proves stochastic-dominance envy-freeness. The embedded verifier separately confirms the sharp three-agent witness, the complete \(n=3\) census, the symmetry quotient, and \(4{,}166\) normalized two-type test profiles through \(n=6\).

Risk: the finite replay is only a consistency check for the infinite theorem, not its proof. No independent external audit has been performed.

## Originality
**PASS.** Bogomolnaia--Moulin prove that Random Priority is weakly envy-free but can fail full stochastic-dominance envy-freeness for \(n\ge3\). Hosseini--Larson--Cohen explicitly give the three-agent failure profile and empirically investigate how RSD envy depends on preference structure. The inspected material does not state the two-distinct-preference-order domain theorem, and targeted published-finding corpus/web searches by “two preference types,” “two rankings,” stochastic-dominance envy, and the exact \(72\)-profile boundary did not locate an equivalent statement.

Risk: search failure is not proof of novelty; an unindexed thesis, note, exercise, or software table may contain the same argument or census. The three-agent witness itself is prior work and is not claimed as novel.

## Value
**PASS.** The theorem identifies a natural, interpretable preference-heterogeneity boundary at which the canonical strategyproof random-priority mechanism recovers the strong fairness property it lacks in general. The restriction is sharp already in the smallest possible square market, and the exact boundary census separates the structural theorem from a one-off example. This directly refines the classical fairness comparison between Random Priority and Probabilistic Serial.

Same-model review: passed. Independent audit: not yet performed.
