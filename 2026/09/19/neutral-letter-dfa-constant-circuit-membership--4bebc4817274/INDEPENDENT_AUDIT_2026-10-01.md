# Independent mathematical audit — SCOPE-20260919-4bebc4817274

Final disposition: **PASS**.

## Correctness
**PASS** — For a language with an identity neutral letter, the source characterization reduces constant circuit complexity to alphabeticity. Alphabeticity is equivalent to idempotence and commutation of letter actions modulo right-language equivalence at every reachable state: the forward direction is immediate from support invariance, and adjacent swaps plus duplicate deletion generate the free semilattice congruence for the converse. A violation has an NL witness consisting of a reachable context and a product-automaton path to an accepting/nonaccepting pair. Hardness is sound: in the fixed ternary construction, unreachable t gives the empty alphabetic language, while a first-hit path word w is accepted and ww, with identical support, is rejected. Complement reachability is NL-complete because NL=coNL.

## Originality
**PASS** — The directly relevant 2026 source states the neutral-letter characterization and NFA PSPACE-completeness but no arbitrary-DFA complexity classification in the accessible primary material. Masopust's prior work gives NL-completeness for general piecewise-testability recognition from DFAs and higher-k results, while the special 1-piecewise/alphabetic local criterion cited in the literature is for minimal DFAs. Targeted searches found no prior NL-completeness theorem for 1-piecewise/alphabetic recognition from arbitrary nonminimal DFAs, especially with an explicit identity letter and fixed ternary alphabet. Full text of the 2026 source remained inaccessible, so this is best-of-knowledge.

### Equivalent formulations
The equivalent language-variety formulations were searched, not only the circuit-complexity wording.

### Broader coverage
Neither broader result mechanically supplies the exact arbitrary-DFA 1-piecewise classification.

### Exact database or table
No finite database is relevant; this was a prior-theorem search.

### Claim versus prior implication
The final claim fills a nontrivial implication gap between two known endpoints.

## Value
**PASS** — The theorem isolates a genuine representation-complexity boundary for a natural regular-language class: minimal presentations admit a very low-complexity local test, arbitrary deterministic presentations require NL-complete semantic quotienting, and nondeterministic presentations reach PSPACE. Fixed alphabet and syntactic neutrality make the separation robust rather than encoding-driven.

## Source inspections
- **Rational Reductions and Regular Languages of Constant Circuit Complexity** (https://arxiv.org/abs/2609.18484): primary abstract and bibliographic material; open and authorized full-text attempts returned no verified PDF Assessment: ACCESS_LIMITATION_WITH_RESIDUAL_OVERLAP_RISK. Evidence: Accessible material supports the neutral-letter characterization/NFA context but cannot rule out an internal DFA remark.
- **Piecewise Testable Languages and Nondeterministic Automata** (https://doi.org/10.4230/LIPIcs.MFCS.2016.67): primary abstract and indexed theorem statements Assessment: RELATED_GENERAL_DFA_RESULT_NOT_LEVEL_ONE_COVERAGE. Evidence: The paper states general DFA piecewise-testability recognition is NL-complete; its k-piecewise complexity statements do not give the arbitrary-DFA k=1 theorem.

## Residual risks
- The 2026 neutral-letter source could not be inspected in full, so an unindexed deterministic special-case remark remains possible.
- Because the proof is short once right-language equivalence is used, folklore prior knowledge is a material originality risk.
