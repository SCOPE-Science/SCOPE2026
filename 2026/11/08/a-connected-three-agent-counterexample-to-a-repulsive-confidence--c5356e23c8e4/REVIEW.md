# Scientific assessment

## Correctness — PASS

The source update is transcribed with self-weight \(A_{ii}=1\) and strictly receptive edges \(|x_j-x_i|<c\). In the connected signed path, the sole initially receptive nonloop edge is repulsive, so its two endpoints update to \((a-1)c/2\) and \((a+1)c/2\), while the isolated-in-receptivity third endpoint remains at \(bc\). The repulsive gap then equals \(c\) and the attractive gap exceeds \(c\); both edges stay inactive forever. The exact final width and strict excess follow algebraically. The numeric witness is checked in two independent exact-rational implementations; the infinite family is supported by the proof, not merely tests. The two-agent minimality invokes Proposition 4.1 of the source. No claim is made about general convergence.

## Originality — PASS (best-knowledge priority assessment)

Kann and Feng, arXiv:2301.02210v1, equations (3.1)–(3.2), Proposition 4.1 and page 14 proposed Theorem 4.11 were read. The text explicitly calls the mixed-sign theorem numerically suspected, and the printed inequality is universally quantified in graphs, without initial receptive-connectivity assumptions. The present path is an actual counterexample, not a numerical observation or a rewording of their proved complete-repulsive theorem. Searches for the exact conjecture, its diameter inequality, mixed-sign three-agent counterexamples and equivalent width bounds did not identify a covering prior statement. Related signed opinion models use different update mechanisms. A 2021 signed bounded-confidence paper was only accessible at abstract/bibliographic level and could not be compared in full; this and unindexed literature are residual publication-priority risks. Unsuccessful searches alone are not treated as proof of novelty.

## Value — PASS

The result resolves the truth value of the explicit, motivated general mixed-sign diameter conjecture with the smallest possible connected graph, an exact rational witness, a genuine open set of initial conditions, and the exact amount of excess within that set. It isolates how an initially nonreceptive attractive edge coexists with an active repulsive edge to defeat an edge-count width barrier. This is a substantive boundary to a mathematical assertion, not an arbitrary parameter slice or a small numerical improvement. A revised conjecture requiring initial receptive connectivity remains untested.

## Closest literature and limits

Primary: C. Kann and M. Feng, *Repulsive Bounded-Confidence Model of Opinion Dynamics in Polarized Communities*, arXiv:2301.02210v1 (2023), model equations (3.1)–(3.2), two-agent Proposition 4.1, and conjectural Theorem 4.11 on page 14. Related but distinct: C. Bernardo et al., *Bounded confidence opinion dynamics: A survey*, Automatica 159 (2024), 111302, DOI:10.1016/j.automatica.2023.111302; discrete-time signed bounded-confidence article, Neurocomputing DOI:10.1016/j.neucom.2019.12.061, abstract only. Full independent priority review has not been conducted. The counterexample does not address general convergence and assumes the source's strict confidence rule.

Self-review: passed. Independent audit: not yet performed.
