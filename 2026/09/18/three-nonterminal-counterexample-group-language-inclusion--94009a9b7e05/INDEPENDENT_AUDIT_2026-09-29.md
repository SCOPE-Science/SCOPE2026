# Independent audit — A three-nonterminal counterexample to a context-free group-inclusion criterion

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/18/three-nonterminal-counterexample-group-language-inclusion--94009a9b7e05`  
**Audited tree:** `582ebe72ce6b5eb54da9e4112d75b3a59f43e130`

## Disposition

**PASSED.** All three required axes pass. Publication may remain in the validated record set.

## Correctness

**PASS.** The counterexample is correct under Yordzhev's published definitions. The source defines U=Σ*×T, so its unit is the literal pair <ε,e>, not a pair whose first coordinate merely represents the identity in G. For the grammar A1→A2A3, A2→x1, A3→x1', the generated language is the singleton {x1x1'}, which is the identity word in the free group after free reduction. The published dynamic recurrence nevertheless places <x1x1',e> in g^4_{14}; this is nonidentity in U and triggers Algorithm 4.4's rejection branch. The same example separates condition (i) from condition (iv) of Theorem 4.3.

## Originality

**PASS.** The published Filomat paper and its arXiv posting were checked directly, including Theorem 2.1, Definition 3.1, Theorem 4.3, and Algorithm 4.4. Targeted searches by title, DOI, arXiv identifier, theorem/algorithm numbers, and correction/erratum/counterexample terminology did not locate a prior published correction or this three-nonterminal example. The claim is therefore appropriately qualified to the best of the searched literature.

## Scientific Value

**PASS.** This is a compact falsification of a stated theorem and algorithm in a peer-reviewed paper, with a minimal-looking three-nonterminal grammar and a transparent diagnosis of the literal-word/group-value mismatch. It has direct corrective value even though it does not settle the underlying inclusion problem.

## Independent checks

- Read the source paper's Definition 3.1: U=Σ*×T with componentwise multiplication and 1_U=<ε,e>.
- Read Theorem 2.1: the earlier criterion uses W1⊆L(G), whereas Theorem 4.3 replaces the corresponding condition by W1={ε}.
- Read Algorithm 4.4: its line-7 test rejects when g^{n+1}_{1,n+1} is nonempty and differs from {<ε,e>}.
- Recomputed the four relevant arcs and the K^k recurrence: k=2 yields <x1,A3> in g^2_{14}, k=3 yields <x1',A3'> in g^3_{44}, and k=4 yields <x1x1',e> in g^4_{14}.
- Independently reduced x1x1' in the free group to the identity while retaining it as a nonempty word in Σ*.

## Literature and prior-art boundary

- https://doi.org/10.2298/FIL2412157Y — Yordzhev, Filomat 38:12 (2024), the published theorem and algorithm being corrected.
- https://arxiv.org/abs/2602.18305 — Author-posted arXiv version of the same work; targeted searches found no erratum or prior counterexample.

## Limitations

- The conclusion is only about Theorem 4.3 and Algorithm 4.4 under the published algebra U=Σ*×T and literal comparison with <ε,e>.
- It does not imply undecidability of the language-inclusion problem and does not validate any proposed quotient-by-G repair.
- An informal or poorly indexed observation could predate this record; no such source was located in the targeted search.

## Repository identity

The assigned source-tree SHA `582ebe72ce6b5eb54da9e4112d75b3a59f43e130` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
