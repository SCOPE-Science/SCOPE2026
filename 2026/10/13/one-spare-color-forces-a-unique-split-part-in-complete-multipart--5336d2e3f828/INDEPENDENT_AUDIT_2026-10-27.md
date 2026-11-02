# Independent mathematical audit

## correctness

PASS

A full proper coloring of K_{n1,...,nr} with r+1 labelled colors has r disjoint nonempty part palettes, so either every part is monochromatic (one unused color), or exactly one part j has two colors, and all others are monochromatic. In the first case every blank sees at most r−1 neighbor colors forever, so forcing implies a total initial coloring. In the second case every vertex of the split part sees at most r−1 external colors and thus must be seeded; if >=2 nonsplit parts are completely blank, no first force sees r colors. Conversely, a fully seeded split part with both colors, all other parts seeded except at most one, forces the missing part then forces all remaining blanks. The r+1 colors can be chosen as an unordered pair for j and bijection on other parts in (r+1)!/2 ways; surjective two-color assignments on j number 2^{n_j}−2, and nonempty/blank seed choices give the exact H_G coefficient factor. Independent vertex weighting p,q gives FC. The minimum seed domain m+r−2 and its multiplicity follow by taking one blank nonsplit part and one selected vertex from every other nonsplit part. The all-singleton case is r! times choice of unused color. An independently written exhaustive enumerator verified all states for seven profiles (r=3 or 4 and singleton boundary), 89,557 initial assignments total, with exact polynomial coefficients and minimum counts. The universal theorem rests on the analytic dichotomy, not the finite checks.

## originality

PASS

The exact all-profile r>=3 one-spare-palette formula and split-part characterization were compared against the 2024 primary definition, the published complete-multipartite λ=r theorem, the published bipartite λ=3 theorem, and maximum-degree-two results. The 2024 source gives only the general forcing indicator sum and a stall criterion. The two strongest later records cover complementary boundary cases; neither directly proves the new all-r condition or all-coefficient polynomial. Three semantic Resultary searches and targeted open literature searches found no decisive covering statement. The 2026 Farr preprint full text could not be independently retrieved in this run; that substantial uncertainty is expressly retained rather than pretending full-text exclusion.

## value

PASS

The first color count above the chromatic number is a natural threshold in Farr’s recently introduced forced-colouring invariant. For arbitrary r>=3 and arbitrary positive part sizes, the exact successful-seed classification changes qualitatively from λ=r: propagation requires a wholly seeded two-color part and all but at most one other part seeded. This yields every coefficient, a probability polynomial and exact extremal seed number/count; it gives a benchmark for a natural graph class with unbounded sizes. Though the proof uses elementary counting and parallels the r=2 boundary, the complete r>=3 λ=r+1 invariant is not mechanically obtained by direct specialization of the inspected prior theorems. The result does not address larger palettes or arbitrary graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
