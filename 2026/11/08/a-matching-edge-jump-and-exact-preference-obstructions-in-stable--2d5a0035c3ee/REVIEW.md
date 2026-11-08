# Scientific review

**Correctness: PASS.** The finite simple graph, named palette and preference cycle definitions are explicit. A matching orientation reaches at most four vertices, or three without matching edges. Every larger member contains the five-vertex obstruction with a fixed three-colour ranking profile; the \(12\) proper assignments each have a specifically identified mutually envying edge. The Grundy-number argument separately caps first-fit colours at three. The exact \(624/576/48\) breakdown was exhaustively computed with two independent directed-cycle tests and explicitly stated enumeration bounds. The verifier was replayed from the final package.

**Originality: PASS (priority provisional).** Koana--Oh--Yoneda, *Graph Coloring with Color Preferences* (arXiv:2609.00569, first public 2026-09-01), gives the base \(K_{2,n}\) case and general upper/lower tools, not the matching-edge jump, explicit five-vertex obstruction, or exact profile count. The closest semantically indexed record treats preference-stability of \(K_{2,3,3}\), a non-isomorphic complete tripartite graph, rather than the matching-augmented bipartite family. Related preferential-colouring definitions require care; no stronger matching-family coverage was found in the inspected sources. Full priority and broad literature exhaustiveness cannot be certified.

**Mathematical value: PASS.** Adding a single edge to the \(K_{2,n}\) side raises the stable chromatic requirement sharply while leaving its usual Grundy lower bound unchanged; the universal 5-vertex obstruction and uniform sharp orientation explain this gap throughout an infinite family. The exact five-vertex profile census distinguishes 2-cycle obstructions from genuinely longer blocking cycles, which is relevant to stability recognition.

The structural theorem is confined to an explicit graph family, and the \(7776\)-profile census is confined to a single labelled graph and three named colours. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
