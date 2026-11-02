# Scientific review: girth from spherical overlap cumulants

## Correctness — PASS

The definitions specify independent uniform spherical spins, a finite simple graph, deterministic weights, analytic cumulants, and a normalized baseline using independent edge variables. On every forest, leaf stripping proves mutual independence of the actual edge inner products, not just uncorrelatedness. A simple cycle's ordered edge-product moment is \(p^{1-j}\), and proper cycle subsets have zero centered product moments. Cumulant multilinearity and vanishing on independent blocks then force the entire first difference to occur at the girth and give the exact \(g!\) multiplicity. The positivity condition rules out cancellations for the girth-identification conclusion. The qubit Bloch identity and fourth/fifth joint-cumulant calculations yield the stated low-order formulas. The complete proof is analytical; 213 exact-rational checks on independent tensors are supporting finite evidence only. Neither infinite graph results nor finite-sample reconstruction is asserted.

## Originality — PASS, with historical-priority qualification

The closest directly relevant source, Zhang (arXiv:2610.25196v1), evaluates moments of cyclic Bargmann invariants and random-state overlaps, not total edge-fidelity sums on arbitrary graphs or the first cumulant defect identifying shortest cycles. Peled–Spinka (arXiv:1708.00058, Section 2.4) gives the **general spin partition function and an exact high-temperature subset expansion**, so there is important established formalism; its inspected formulas do not evaluate the shortest-cycle coefficient, compare the partition function with independent edge factors, or give the inverse-girth statement. Stanley's 1967 classical-Heisenberg expansion is a relevant earlier diagrammatic approach, but the accessible abstract focuses on spin correlations and regular lattices and is insufficient to exclude implicit coverage in the full paper. A mathematical-record search also located an LKJ-correlation-matrix triangle cumulant; that is a different dependent-matrix model and does not imply the spherical-edge claim. The mathematical comparison is of implications, not title overlap. A full systematic priority audit of older spin-cluster literature remains outstanding, but no decisive covered theorem was found in the inspected material.

## Mathematical value — PASS

Graph girth and shortest-cycle multiplicity are natural structural invariants. The result shows exactly when dependence first becomes statistically visible in a single graph-wide sum of random quantum-state overlaps. The leading defect is nonzero for every positive-weight cycle and is dimension-explicit; thus the theorem is an all-order structural identification, not a finite sample count, a renaming of a known parameter, or an arbitrary low-dimensional example. The explicit third through fifth cumulants additionally recover three standard short-cycle counts for general graphs with triangles and overlapping cycles. It does not claim complete graph reconstruction or a finite-sample optimal estimator.

## Closest literature and limits

- Lin Zhang, *Exact probability laws of random inner products*, arXiv:2610.25196v1, especially Sections 4 and 6.5 (full HTML inspected).
- Ron Peled and Yinon Spinka, *Lectures on the Spin and Loop \(O(n)\) Models*, arXiv:1708.00058, Sections 2.1 and 2.4, including PDF page 16 equation (15) (full relevant sections inspected).
- H. E. Stanley, *High-Temperature Expansions for the Classical Heisenberg Model. I*, Phys. Rev. 158 (1967), 537, abstract inspected; full-text historical overlap unresolved.

Limitations: signed-weight shortest-cycle contributions can cancel; independent states and finite simple graphs are essential; the result provides population-law identities, not error bounds for sampled cumulants. The broad classical linked-cluster literature presents residual historical-priority risk.

Self-review: passed. Independent audit: not yet performed.
