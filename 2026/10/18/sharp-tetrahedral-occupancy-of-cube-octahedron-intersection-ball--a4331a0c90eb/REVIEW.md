# Scientific review: cube–octahedron tetrahedral occupancy

## Correctness — PASS
The polytope vertices are determined by intersections of the active coordinate and absolute-sum supporting planes. Multiaffinity reduces maximal four-point determinants to vertex quadruples. The exact standard-library checker reconstructs all \(10626\) quadruples in each open chamber and verifies **every** candidate bound on an entire real parameter interval through nonnegative rational Bernstein coefficients. Three explicit quadruples attain the bounds. The formula for full-body volume is independently established by inclusion–exclusion. The difference between the claimed maximal tetrahedron volume and one sixth of the full-body volume factors into expressions nonnegative on each interval, with a unique zero at \(c=3/2\). There is no extrapolation of finite numerical samples.

## Originality — PASS (self-review)
The nearest same-object source, Deza–Hiriart-Urruty–Pournin (arXiv:2011.05607), explicitly describes the polar cube–cross-polytope intersection and derives full-body volume, not the maximum-volume *contained tetrahedron*. Di Summa et al. (arXiv:1406.3512) provide general complexity/approximation results. Akopyan–Glazyrin (DOI:10.1007/s10998-014-0051-2) discuss maximal simplices of prisms/parallelotopes and center containment, without this intersection family or its determinant phase diagram. Two indexed results on this same family give illumination counts and integer-parameter graph distances, distinct from the claimed invariant. Priority under unsearched terminology or older optimization literature remains a risk.

## Value — PASS
This is the exact sharp contained-simplex approximation profile for a canonical continuous interpolation connecting three standard Archimedean solids with the cube and octahedron. The transition at \(c=3/2\) separates genuinely different winning tetrahedral shapes and is simultaneously the **unique global worst tetrahedral occupancy**, namely \(1/6\). The extra transition at \(c=2\) gives a complete three-regime classification, beyond endpoint values, a known volume formula, or a routine single-shape calculation. Multiplicities specify the vertices realizing each branch; the classification makes no unsupported claim about all nonvertex optimizers.

## Limitations and supporting sources
The theorem concerns this 3D family only. The exact computations remain available in `verify.py`, and their mathematical completeness is justified by determinant multilinearity and Bernstein positivity. Full text of the same-body Deza et al. paper and of the 2014 Akopyan–Glazyrin paper was inspected for stronger coverage; arXiv:1406.3512 was examined for general MVS results. The two closest indexed related records were read at their published `RESULT.md` documents. An independent audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
