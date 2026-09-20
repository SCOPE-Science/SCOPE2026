# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The claim separates into three exact steps.

First, every entry in Mizhaev's published coordinate table is divisible by 3, so uniform scaling by 1/3 gives an integer realization of the same embedded polyhedral surface. The normalized coordinate ranges are exactly 200, 200, and 156.

Second, the normalized vertex differences generate the full ambient lattice. Relative to vertex 1, two explicit 3-by-3 minors are -8 and 1325. Since these are coprime, the index of the difference lattice divides 1 and is therefore 1. Thus any affine map taking every normalized vertex to an integer point has an integer linear part.

Third, two vertex differences are exactly (0,200,0) and (200,0,0). Consequently every integer covector with a nonzero x- or y-component has width at least 200, whereas a nonzero vertical integer covector has width at least 156. The three rows of an invertible integer linear part are independent, so at least two are nonvertical. This proves the sorted lower bound (156,200,200), which the displayed coordinates attain.

The exact arithmetic in `artifacts/verify.py` reproduces the determinant certificates, coordinate ranges, forcing differences, and attained box-volume product. The script was executed successfully with the output implied by the assertions.

Adversarial checks included allowing arbitrary real affine maps rather than assuming unimodularity: saturation of the difference lattice forces their linear parts to be integral as soon as all image vertices are integral. The proof therefore covers integer matrices of any nonzero determinant, not only GL(3,Z). Translation does not affect widths.

## Originality

**PASS, to the best of our knowledge.** Mizhaev's arXiv:2609.17700v1 was inspected through its coordinate table, theorem, symmetry statement, and reproducibility/limitations section. The paper explicitly states that its certificate does not establish coordinate minimality or optimal aspect ratios; it does not discuss divisibility by 3, the saturated difference lattice, lattice width, or affine-integral bounding-box optimality.

Literature checks using the exact paper title and combinations of `integer coordinates`, `minimal coordinates`, `lattice width`, `integral affine`, `bounding box`, and `equivelar octahedron` did not locate the theorem above. Hougardy--Lutz--Zelke (2006) proves small-coordinate results for different genus-3 triangulations by enumeration in cubes; it does not cover this 24-vertex eight-nonagon realization or its affine orbit. The current SCOPE archive was also checked by the source identifier, author name, object name, lattice-width terminology, and integer-coordinate terminology, with no matching record found.

The factor-three rescaling by itself is elementary and is not presented as the principal contribution. The claimed contribution is the sharp affine-orbit theorem: after primitive normalization, every affine image that remains integral has sorted coordinate-span profile at least (156,200,200), with equality attained.

The most relevant source not inspected in full is Mizhaev's 2020 precursor, *Equivelar octahedron of genus 3 in 3-space* (DOI 10.31219/osf.io/hvtey). Available bibliographic and abstract material was checked, and exact-coordinate/lattice-width searches did not reveal the present statement, but an earlier differently phrased observation cannot be excluded. The 2026 preprint is also very recent, so later revisions could overlap.

## Value

**PASS.** The source paper's purpose is to provide a compact exact integer certificate, yet its displayed coordinates are nonprimitive by a factor of 3. The normalized certificate reduces each linear coordinate scale by 3 and the axis-aligned box-volume product by 27. More importantly, the lattice argument proves this normalized certificate is not merely smaller: within the entire affine orbit subject to integrality, the full sorted span profile (156,200,200) is sharp. This turns a numerical simplification into an exact rigidity statement and gives a canonical primitive lattice normalization for reuse in enumeration or CAD computations.

The result is deliberately narrower than global coordinate minimality. It does not compare against non-affinely-equivalent realizations of the same combinatorial map, so the broader minimization problem remains open.

## Limitations

- The optimality theorem is restricted to affine images of the published realization that keep all vertices integral.
- It does not establish a global minimum among all geometric realizations of the same equivelar map.
- It does not optimize Euclidean aspect ratio under arbitrary non-affine deformation.
- The full text of the 2020 precursor was not inspected, leaving a residual historical-priority risk.
- The motivating 2026 preprint is recent, so later revisions or unindexed parallel observations may overlap.
- Independent audit has not been performed.
