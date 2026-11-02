# Scientific review: exact finite-sweep phase diagram for directed-ring best responses

## Correctness — PASS

The theorem states an explicit finite-player model, all strategy bounds, heterogeneity, positive weights, and a single repeated revision order. The proof derives the full-sweep scalar map with a clipping-composition identity, not a heuristic linearization. Its critical cases include the unit gain and plateau boundaries. For gain above one, the exact finite-settling lemma proves eventual exact stationarity for the orientation-preserving return map, which applies directly to even rings and to the squared map for odd rings. For gain below one, the ordinary contraction argument gives a unique equilibrium and quantitative convergence. The result that odd rings have at most one primitive two-cycle follows from the at-most-three fixed points of the squared clipped-affine map and the unique fixed point of the decreasing first return. Deterministic exact-rational tests in `VERIFY.py` independently compute the individual responses and compare the derived recurrence. The tests corroborate but do not replace the proof.

## Originality — PASS, with residual priority risk

The closest full inspected source, Bayer, Kozics and Szőke, *Best-response dynamics in directed network games* (https://arxiv.org/abs/2101.03863), specifically discusses the directed-cycle construction in Section 3, a contractive directed cycle in Section 5 and the general sufficient spectral condition for convergence. The known subcritical result is acknowledged and not claimed as new. The combined arbitrary-gain, arbitrary-target clipped-return classification with finite-time supercritical outcomes and uniqueness of primitive two-cycles is not contained in those inspected propositions or cycle examples. Olszewski's monotone-iteration convergence result (https://doi.org/10.1287/moor.2021.1210), inspected at the available abstract level, is relevant but is not a full-document exclusion check; an unspecified specialized equivalence remains a priority risk. A literature and comparable-claim search did not identify such an equivalence, which alone does not constitute a uniqueness proof.

## Value — PASS

The known directed-network theory makes weak-influence convergence and the possibility of cycles clear, but does not give an all-parameter answer on weighted one-way rings. This theorem identifies an exact feedback-gain threshold, a parity dichotomy, supercritical *finite-time* rather than merely asymptotic convergence for even rings, and a limit of one supercritical two-cycle for odd rings, with an explicit linear-time-in-players reduction to a scalar return map. The object is a natural family of directed local-public-goods games, not an arbitrarily selected parameter slice. Although the interval-map argument is elementary, the resulting full game-dynamics classification is useful for interpreting the boundary between stable Nash equilibrium adjustment and persistent nonconvergence.

## Scope and remaining risks

This is a theorem about exact periodic best responses and one predecessor per player, not random or arbitrary fair schedules, simultaneous updating, or signed network weights. First public source attribution uses the 2020-01-13 working-paper listing, not a 2023 publication date. The earlier working-paper PDF itself was not accessible in one retrieval attempt; a later full open version of the same work was examined. Any unidentified equivalent result in other specialized literature would change the originality assessment. No independent audit or external proof verification has been performed.

Self-review: passed. Independent audit: not yet performed.
