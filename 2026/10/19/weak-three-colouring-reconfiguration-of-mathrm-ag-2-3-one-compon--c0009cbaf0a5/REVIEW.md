# Scientific review of the nine-point affine-plane recolouring classification

## Correctness

**PASS.** The exact domain is all assignments of three named colours to nine indexed affine points with each of twelve three-point lines nonmonochromatic, and an edge is one legal site recolouring. The proof bounds every colour class by four using an incidence contradiction, excludes two-colour assignments by \(r^2-9r+24=0\), and identifies strict bicolorings by the rainbow-line pair identity. The nonstandard finite metric claims rest on complete independent constructions of all \(3762\) states, \(16848\) edges, and all \(3762\) breadth-first eccentricities using the included `verify_coordinates.py` and `verify_arcs.py`; both files are readable standalone stdlib programs. The recorded outputs match exactly and contain canonical graph fingerprints. The proof does not infer infinite statements from a finite experiment.

## Originality

**PASS under presently accessible comparisons; residual historical-priority risk remains.** Colbourn–Dinitz–Rosa (1999) give the order-nine \((4,4,1)\) strict bicolouring split but no state-transition graph. The affine-plane arc-colouring work arXiv:2601.19043 establishes optimal colour numbers and investigates a different plane's colourings, not this graph's distances. Cardinal et al. arXiv:1805.04055 address two-colour NAE reconfiguration hardness on varying instances. Searches under Hesse configuration, \(\mathrm{AG}(2,3)\), Steiner triple system of order nine, weak recolouring, and the numerical state/edge counts did not disclose equivalent covering results. Neither the known bicolouring split nor the known chromatic number is represented as new. Unindexed or differently termed equivalent results remain possible.

## Value

**PASS.** This is a natural smallest odd-order affine-plane instance of the general problem of reconfiguring minimum-palette proper weak hypergraph colourings. It precisely answers reachability and worst-case transformations and exhibits a sharp phenomenon: the class of strict bicolorings is wholly frozen internally, but its states become mutually accessible after merely relaxing the requirement that *every line* use exactly two colours, while preserving three colours and excluding monochromatic lines. Exact radius, diameter, degree and distance distributions make the answer usable as a benchmark for enumeration and sampling.

## Limitations and nearest literature

The claim is finite and computer assisted. The checked source text for Colbourn–Dinitz–Rosa (1999) explicitly covers existence of a strict bicolouring with split \((4,4,1)\); the 2026 affine-plane arc-colouring work gives more general palette bounds but no state graph; the Boolean NAE reconfiguration paper has a different palette and variable-instance complexity focus. Searches alone do not prove publication priority. Independent external mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
