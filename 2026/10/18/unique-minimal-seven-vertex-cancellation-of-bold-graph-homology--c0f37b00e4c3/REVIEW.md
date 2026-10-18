# Scientific review: sharp seven-vertex bold-homology cutoff

## Correctness — PASS

The claim is a *finite* statement about all connected graphs of order at most seven, not a heuristic extrapolation. The 2,097,152 labeled seven-vertex edge masks are visited exhaustively; 1,866,256 are connected. An exact integer alternating count identifies 1,691,767 zero-Euler instances. Exact mod-two simplicial boundary reductions yield 252 labeled nontrivial cancellations, each checked to have exactly the graph-suspension structure. The orbit count \(7!/20=252\) matches. Independently, 1,253 standard unlabeled atlas entries are scanned using direct connected-domination cochain matrices; the unique positive is `G1212` with two unit Betti numbers. The bad-subset complex admits an explicit five-collapse model \(S^1\sqcup\{\mathrm{pt}\}\), certifying the witness cohomology even integrally. Included source and observed outputs permit replay. Residual: external packages and C toolchain should be checked by the reproducer; no formal machine-checked proof or independent audit is asserted.

## Originality — PASS

The **already-known** Caputi–Celoria–Collari 2022 connected-domination theorem identifies the cochains and Euler characteristic, and the authors pose the cancellation question (Question 5.11). More decisively, their 2023 suspension theorem (Theorem 5.8) already implies the *existence* of the particular cycle-suspension example with the two nonzero cohomology groups. Therefore these components have **no novelty claim**. The claim being assessed is instead the *first possible graph order and uniqueness among all connected seven-vertex isomorphism types*, which does not follow from the construction of examples or from their homology formulas. Inspection of those papers and related überhomology work, plus targeted searches of the published mathematical-record database for equivalent formulations and seven-vertex graph catalogues, yielded no encompassing classification. Similar small-order publications concern distinct matching, neighborhood, and domination-number complexes. The 2023 theorem is explicitly recorded as a genuine strong predecessor rather than dismissed. Residual: an unindexed or differently named exhaustive census could cover the exact minimum and uniqueness.

## Mathematical value — PASS

The natural invariant under study answers the smallest-counterexample question suggested by the explicit 2022 cancellation problem, which the later suspension construction answers only at the level of existence. Locating the *sharp universal cutoff* and classifying its *sole extremizer* are mathematically interpretable facts, not an arbitrary graph selected after a computation. The dual independently reproducible census provides a useful minimal test for bold-cohomology algorithms. Its value is a natural finite extremal classification, not a general structural theory of all graphs.

## Closest sources and scope

- Caputi, Celoria, Collari, *Categorifying connected domination via graph überhomology* (2022), arXiv:2201.00721v1, Theorems 1.2–1.3 and Question 5.11.
- Caputi, Celoria, Collari, *From the Mayer–Vietoris spectral sequence to überhomology* (2023), arXiv:2304.10134, Theorem 5.8; prior coverage of suspension witness existence and groups, **not the sharp cutoff**.
- NetworkX Read–Wilson graph atlas documentation, `graph_atlas_g`, for independent isomorphism-class coverage.
- Unindexed equivalent census remains a possible limitation; no claim about all integral coefficients or graphs above seven vertices.

Self-review: passed. Independent audit: not yet performed.
