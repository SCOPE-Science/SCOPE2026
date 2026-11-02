# Scientific review

## Correctness — PASS
The proof derives the exact \(K_{a,n}\) SI transition generator from independent exponential passage times, realizes infections through independent threshold maxima, uses a uniform empirical bound, and proves that the difference between accumulated exposures at completion of the second part tends to \(\lambda\). The flooding-time rate bound controls the full horizon, and the vanishing post-saturation susceptible-time integral is explicit. The balance identity follows from part-exchange symmetry after the first forced cross-part infection. All 3,468 finite exact checker assertions passed. Finite checks do not establish the infinite result.

## Originality — PASS, with priority risks
Compared the assertion to the motivating 2023 exponential-FPP complete-graph flooding theorem, a 2017 discrete-time infection takeover model, a 2012 inhomogeneous-graph typical-path theorem, and 2018 sparse-graph flooding bounds. Their graph families, marked observables, generators, or asymptotic precision do not imply the present dense-bipartite last-class logistic window. Public research-record and primary-literature queries found no equivalent statement. Possible older multitype epidemic and marked extreme-value results remain a genuine unexcluded risk. A relevant 2023 finite-birth epidemic paper was not fully inspected owing to limited source access.

## Value — PASS
Knowing which community contains the final infected vertex is a natural property of spatial epidemic completion that cannot be read from the leading scalar flooding time. The theorem identifies the \(n/\log n\) imbalance scale, its entire fixed-parameter crossover, and an exact all-size balance law. The proof also isolates an asymptotic accumulated-exposure displacement that is reusable for studying marked terminal events.

## Limits and closest literature
The result is restricted to fixed \(\lambda\), independent rate-one exponential edges, complete bipartite graphs, and one initially infected root. No joint centered flooding-time law or independent historical-priority certification is claimed. Closest material read: van der Hofstad–Lodewijks (arXiv:2311.16088, 2023), Ottino-Löffler–Scott–Strogatz (arXiv:1702.00881, 2017), Kolossváry–Komjáthy (arXiv:1201.3137, 2012), Leskelä–Ngo (arXiv:1806.09568, 2018). The structured scientific comparison and specific risks are in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
