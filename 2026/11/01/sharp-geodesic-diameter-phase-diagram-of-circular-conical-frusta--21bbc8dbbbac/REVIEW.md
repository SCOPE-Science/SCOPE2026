# Scientific review: intrinsic diameter of circular conical frusta

## Correctness — PASS

The claim fixes the lateral surface only, specifies the generator radii, and correctly converts physical azimuth to developed angular period. The proof covers every real radius ratio in \((0,1)\) and every physical half-apex angle in \((0,\pi/2)\). The shortest-path formula is established from planar annular-obstacle geometry, including boundary-following routes and competing winding classes. Convexity of distance in each radial coordinate reduces global diameter to two specific rim combinations; an exact comparison yields the three exhaustive branches. Both contact transitions and claimed derivatives follow algebraically. The included executable reproduces 810,000 random checks and 20 exhaustive radial grids of 8,281 points each, with no positive diameter violation. This finite evidence is ancillary, not an infinite proof. Nonstandard lemmas needing independent checking are the annular-obstacle geodesic representation and its radial convexity; both have explicit proofs in RESULT.md.

## Originality — PASS (best-knowledge assessment)

Compared exact claims and implications rather than titles: classical local straightening of cone geodesics, general polyhedral geodesic algorithms, related geometric cone invariants, and independently published geodesic-diameter work on a different discrete family. Charitos–Papadoperakis–Tsapogas (2013) study complete closed Euclidean cone surfaces and do not present frustum boundaries or diameter optimization. Chen (2017) classifies local cone geodesics but omits the boundary-following minimizers essential here. The 1987 polyhedral shortest-path paper has a broad algorithmic abstract, but its full text could not be inspected; it is not evidence either way for a smooth conical-frustum formula. Relevant indexed records concern other metrics, surfaces, or extrinsic cone quantities; no explicit formula with both specified transition loci was found. This is a scoped positive novelty assessment, not an assertion of exhaustive historical priority. The main residual risk is an unlocated classical treatment of annulus obstacle shortest paths that might already draw the global-diameter corollary.

## Value — PASS

The geometric problem is canonical: determine the intrinsic diameter and farthest pairs of every circular conical frustum. The answer has a nontrivial contact switch at \(q=2\cos\phi-1\) in one angular regime, a separate boundary-grazing geodesic transition at \(q=\cos(\phi/2)\), and distinct differentiability signatures. The theorem treats all aspect ratios, recovers the sharp intact-cone and cylinder limits, and supplies an explicit global classification rather than a single sampled value. Exact metric diameters and farthest pairs are usable benchmark invariants for intrinsic surface-distance algorithms. The contribution is elementary and may be derivable by familiar planar geometry, but the classification and transitions are not a mere change of variables or numerical exercise.

## Closest literature and limits

- Charitos, Papadoperakis and Tsapogas, *The geometry of Euclidean surfaces with conical singularities*, arXiv:1306.1759 (2013), exact public submission date 2013-06-07: the local conical metric is shared, but the global problem concerns closed surfaces without annular boundary.
- Chen, *Rectifying curves and geodesics on a cone in the Euclidean 3-space* (2017), DOI:10.5556/j.tkjm.48.2.2017.2382: full paper's introduction and principal proofs establish local geodesic structure, not shortest paths allowed to follow truncated cone rims.
- Mitchell, Mount and Papadimitriou, *The discrete geodesic problem* (1987), DOI:10.1137/0216045: publisher abstract only; polyhedral-surface method, not verified as excluding this different smooth-surface special case.

All correctness evidence comes from the explicit derivation and separately runnable numerical checks. Neither independent audit nor independent historical-priority review has been performed; no such certification is claimed.

Self-review: passed. Independent audit: not yet performed.
