# Independent audit — 2026-10-01

## Final claim

Every 4-existentially closed graph is super geometric dominant; consequently every prime-order Paley graph \(P(p)\) with \(p\equiv1\pmod4\) and \(p\ge193\) is super geometric dominant, while \(P(17)\) is an exact checked smaller example that is not 4-existentially closed.

## Correctness — PASS

In a diameter-two graph, a third vertex lies on the metric line through two endpoints exactly when the induced triple has two edges. The 4-e.c. property realizes the explicit adjacency patterns needed to witness both directions of incomparability for any two lines, two closed neighborhoods, and a line versus a closed neighborhood, so the transfer theorem is valid. For Paley graphs the four-pattern character expansion gives \(16N\ge p-38-11\sqrt p\), positive at and above \(193\). A fresh exact replay of \(P(17)\) checked diameter two, all 136 line comparisons, all neighborhood comparisons and every line/neighborhood comparison, with line sizes \(6\) and \(10\) occurring 68 times each; the finite check supports only the small proposition.

Checked sources:
- Chen, Huzhang, Miao and Yang, Graph metric with no proper inclusion between lines, Discrete Applied Mathematics 185 (2015), complete accessible text inspected.
- Blass, Exoo and Harary, Paley graphs satisfy all first-order adjacency axioms, J. Graph Theory 5 (1981).
- Ananchuen and Caccetta, On the adjacency properties of Paley graphs, Networks 23 (1993).
- Cameron and Stark, A Prolific Construction of Strongly Regular Graphs with the n-e.c. Property, EJC 9 (2002).
- Resultary semantic search for existential closure, Paley graphs and super geometric dominance.
- Assigned P(17) verifier and independent exact replay.

Residual risks:
- The general Paley theorem rests on the character-sum bound, not on the finite P(17) computation.

## Originality — PASS

Best-of-knowledge originality passes. The 2015 primary source defines super geometric dominance, proves randomized existence, and explicitly says no constructive family without randomness was known. Classical Paley adjacency results give eventual existential-closure properties but predate the metric-line notion. The searched literature did not state the transfer from 4-e.c. to super geometric dominance or its deterministic Paley consequence.

### Equivalent formulations

Searches:
- Resultary query: 4-existentially closed graphs super geometric dominant Paley graph metric lines neighborhoods antichain
- Web query: super geometric dominant existentially closed; super geometric dominant Paley

Evidence:
- The assigned record was the only exact Resultary hit.
- The 2015 paper contains no occurrence of an existential-closure transfer and explicitly records the constructive-family gap.

Reasoning: The aliases are 4-e.c./four-extension property and the antichain of generated metric lines plus closed neighborhoods; no equivalent bridge was found.

### Broader coverage

Searches:
- Chen--Huzhang--Miao--Yang 2015 full text
- Classical Paley adjacency-property papers

Evidence:
- The 2015 source is broader on super geometric dominant graphs but uses random constructions.
- Classical Paley papers are broader on adjacency-extension axioms but predate and do not discuss super geometric dominance.

Reasoning: Neither side alone mechanically yields the cross-theory transfer without the tight-triple argument.

### Exact database or table

Searches:
- Resultary search for Paley super geometric dominant examples
- Assigned exact P(17) replay

Evidence:
- No prior exact Paley table was located.
- The P(17) computation verifies the small example but is not treated as novelty proof.

Reasoning: The main claim is an infinite structural implication; no database lookup subsumes it.

### Claim versus prior implication

Searches:
- 2015 Definition 4 and Discussion Question 2 versus the audited theorem
- Cameron--Stark/Paley n-e.c. results

Evidence:
- The 2015 discussion explicitly says no constructive family avoiding randomness was known.
- Paley n-e.c. gives the input property but not the metric-line conclusion.

Reasoning: Composing the two literatures still requires proving that 4-e.c. realizes every antichain witness; that implication is the substantive new bridge.

### Source inspections

- **Graph metric with no proper inclusion between lines** — Does not cover the transfer; it explicitly records a constructive-family gap. Material read: Complete accessible article text, including Definition 4, Theorems 5--6, and the discussion questions Method: Primary full-text web inspection Evidence: The discussion says no constructive family of super geometric dominant graphs without random process was known.
- **A Prolific Construction of Strongly Regular Graphs with the n-e.c. Property** — Provides adjacency-extension examples but not the metric-line antichain theorem. Material read: Primary bibliographic/theorem-level material relevant to the n-e.c. property Method: Primary-source comparison Evidence: Its subject is the n-e.c. property of strongly regular graphs, not super geometric dominance.

Checked sources:
- Chen, Huzhang, Miao and Yang, Graph metric with no proper inclusion between lines, Discrete Applied Mathematics 185 (2015), complete accessible text inspected.
- Blass, Exoo and Harary, Paley graphs satisfy all first-order adjacency axioms, J. Graph Theory 5 (1981).
- Ananchuen and Caccetta, On the adjacency properties of Paley graphs, Networks 23 (1993).
- Cameron and Stark, A Prolific Construction of Strongly Regular Graphs with the n-e.c. Property, EJC 9 (2002).
- Resultary semantic search for existential closure, Paley graphs and super geometric dominance.
- Assigned P(17) verifier and independent exact replay.

Residual risks:
- The threshold \(193\) is only sufficient and is not claimed optimal.
- Differently indexed post-2015 work could contain the same transfer, although no such statement was located in the searches performed.

## Scientific value — PASS

The transfer theorem converts a standard adjacency-extension property into the complete metric-line/closed-neighborhood antichain condition and immediately supplies an explicit deterministic infinite family answering a gap stated in the defining 2015 paper. The exact \(P(17)\) example also shows the sufficient hypothesis is not necessary.

Checked sources:
- Chen, Huzhang, Miao and Yang, Graph metric with no proper inclusion between lines, Discrete Applied Mathematics 185 (2015), complete accessible text inspected.
- Blass, Exoo and Harary, Paley graphs satisfy all first-order adjacency axioms, J. Graph Theory 5 (1981).
- Ananchuen and Caccetta, On the adjacency properties of Paley graphs, Networks 23 (1993).
- Cameron and Stark, A Prolific Construction of Strongly Regular Graphs with the n-e.c. Property, EJC 9 (2002).
- Resultary semantic search for existential closure, Paley graphs and super geometric dominance.
- Assigned P(17) verifier and independent exact replay.

Residual risks:
- The threshold \(193\) is only sufficient and is not claimed optimal.
- Differently indexed post-2015 work could contain the same transfer, although no such statement was located in the searches performed.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
