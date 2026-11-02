# Self-review

## Correctness: PASS

The state equation is an exact piecewise-linear mass balance. Telescoping the square of pollutant load provides the global objective identity; a weighted Cauchy--Schwarz inequality bounds it sharply for every \(k\ge1\) and \(0<\eta\le1\). The equality conditions determine every upstream pre-filter load, and their strictly positive unique gaps realize the bound. In the separate integer-site model, direct influence accounting proves the objective identity; an exact completion of squares yields an integer center and gap problem. Successive gap differences have rational thresholds, whose strict order gives global optimality and every tie. No approximation or finite test establishes the infinite scope. Boundary \(\eta=1\) and \(n=2\) are handled; \(\eta=0\) is deliberately excluded because there is no unique placement.

The included standard-library checker passed 7,193 exact-rational assertions for sampled rational efficiencies, independent recurrence implementations, all site pairs over small integer ranges, and exact equality cases. It supplements the proof only. A field-calibrated result is not claimed.

## Originality: PASS within checked evidence; priority not certified

The full author-uploaded Weller--Jordan--Correll (1998) article was inspected through its model, results and discussion; its fixed-fraction buffer cells are organized in transverse land-to-stream columns and its conclusions concern width variability and aggregate discharge, not longitudinal placement or \(\int C\) minimization. The full Voß et al. (2012) open manuscript supplies a relevant distributed-source transport equation but no filter-location extremizer. The Liu et al. (2019) MIT abstract demonstrates genuine real-world importance of in-series filter spacing, but the model concerns hydrodynamic residence and number of islands per reach, not the fixed-count, constant-per-filter transmission problem. The Brand--Ostfeld (2011) abstract concerns genetic-algorithm wastewater network design; full text remained unavailable and is a residual risk, not evidence of noncoverage.

published-finding corpus semantic searches for the continuous all-\(k\) formula, integer efficacy staircases, aliases and transport optimization yielded unrelated Fourier filters, sensor spacing and numerical optimization findings; none of the retrieved claims implies the result. The accessible prior research records was consulted only for overlap and supplied no matching result. Search absence does not prove novelty; future domain scholarship may uncover an equivalent cascade theorem.

## Value: PASS

The all-filter-count inequality and unique placements quantify the otherwise nontrivial tradeoff between placing filters early to treat more downstream distance and placing them later to remove larger incident loads. The optimal internal/end-gap ratio equals exactly \(\eta\), rather than always requiring uniform spacing. For fixed integer locations, rational threshold ties give a reproducible design classification with explicit efficacy sensitivity. These exact reference cases are useful for benchmarking multi-location water-quality optimizers and for detecting grid artifacts in simplified transfer models, without pretending to make hydraulic or cost recommendations. The discrete staircase is part of the same spatial-placement claim, rather than a separate unrelated result.

## Limitations and closest sources

Weller, Jordan and Correll (1998), doi:10.1890/1051-0761(1998)008[1156:HMFMDF]2.0.CO;2 (full article inspected); Voß et al. (2012), doi:10.1002/hyp.9445 (full manuscript, reach equations and scope inspected); Brand and Ostfeld (2011), doi:10.2175/106143010X12780288628219 (abstract only); Liu et al. (2019), doi:10.1016/j.advwatres.2019.05.011 (abstract/record only). Unindexed process-design equivalences and inaccessible full texts remain priority risks. The result assumes a constant removal fraction, homogeneous sources and no decay or hydraulic coupling.

Self-review: passed. Independent audit: not yet performed.
