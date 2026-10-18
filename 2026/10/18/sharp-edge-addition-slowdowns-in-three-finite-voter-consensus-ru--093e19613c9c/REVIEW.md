# Scientific review

## Correctness — PASS

The claim defines the three update probabilities, the fair independent initial law, and a unit cost for every update attempt. Absorption follows from connectivity. The exact finite chain formula \(T_R(G)=2^{-n}\boldsymbol 1^{\mathsf T}(I-Q_R(G))^{-1}\boldsymbol 1\) follows by first-step analysis. Recomputing each transition and solving the rational linear system reproduces every table entry. The accompanying stand-alone verifier enumerates **all** labelled graphs through four vertices and groups source graph plus added nonedge under every permutation: there are zero, one, and six edge-addition orbits at orders two, three, and four. A rational five-vertex star calculation provides the LD upper witness. This proves the stated sharp finite thresholds and no larger-graph classification.

## Originality — PASS (best-knowledge assessment)

Closest full-text research is Iwamasa–Masuda (arXiv:1404.6360), which explicitly illustrates the same four-vertex paw and finite absorbing-chain method but optimizes large-graph consensus at fixed edge count, with balanced initial configurations. It does not tabulate all local single-edge comparisons at four vertices or give the sharp rule-dependent five-vertex threshold. Sood–Antal–Redner (arXiv:0712.4288) establish the different update rules; Masuda (arXiv:1403.4763) works on two-clique bridge families; Cooper–Dyer–Frieze–Rivera (arXiv:1604.06884) use discordant-only updates. Searches for edge augmentation, graph insertion monotonicity, consensus absorption time, voter/invasion/link dynamics, and Braess-type effects located no encompassing theorem or exact table. Those broader observations and techniques are acknowledged; the distinctive contribution is the complete exact first onset and comparison of three protocols. Residual risk remains that a less easily located finite graph enumeration contains the same table.

## Value — PASS

Whether strengthening a social connection speeds binary agreement is a natural network-design question. The sharp minimal network order and *entire* four-agent insertion classification are interpretable obstructions to an intuitive monotonicity hypothesis. They exhibit the same edge producing opposite effects under two canonical update rules, while the third rule first fails at a different order. The result is a finite exact structural boundary, not a restatement of general consensus existence or a marginal decimal improvement.

## Boundaries and evidence

The calculation uses fair independent initial opinions, attempted-update time, and static connected simple graphs. It does not infer an infinite-size theorem or five-agent census. The scientific comparison rests on the source articles, explicit model normalization, and verified finite rational computations; literature-search incompleteness is a remaining risk. Independent external validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
