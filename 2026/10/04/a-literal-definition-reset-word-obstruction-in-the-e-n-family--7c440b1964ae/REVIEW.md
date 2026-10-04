# Same-model review

## Correctness
**PASS.** The claim is limited to the literal transition table. The interval-image proof explicitly reconstructs the action of \(a^2b^{n-2}\), handles parity, proves the universal reset word, and compares its length with \(n^2-3n+2\). Exact power-automaton breadth-first search for \(4\le n\le12\) independently verifies the finite instances but is not used as an infinite proof.

## Originality
**PASS.** The primary arXiv v2 full text was inspected at the exact definition, Figure 6, and Theorem 4 proof. The 2010 precursor announces the threshold family but does not define \(E_n\). Searches over the family name, threshold, proof identities, transition-table language, and erratum/correction aliases found no indexed statement that implies the universal literal-table obstruction. The residual risk is an informal or non-indexed correction, and the claim is accordingly limited to the public arXiv v2 presentation.

## Value
**PASS.** A literal implementation of the displayed table yields an explicit reset word of asymptotic length about half the claimed threshold for every \(n\ge5\). The discrepancy therefore materially affects reproducibility and benchmarking for a named slowly synchronizing family. Figure 6 and the proof resolve which semantics the theorem intended.

## Closest literature and limitations
The closest source is the defining 2013 paper itself; its intended Figure-6 automaton is not challenged. The 2010 precursor does not contain the problematic definition. The exact universal reset threshold of the literal cyclic-table automaton is not claimed here.

Same-model review: passed. Independent audit: not yet performed.
