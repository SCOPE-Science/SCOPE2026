# Scientific review

## Correctness

PASS. The fixed Euler face and edge counts make facet-uniform then side-uniform sampling equivalent to edge-uniform sampling. The cited spherical Blaschke–Petkantschin intensity yields the beta radial factor through an explicit two-branch change of variables; the angular integral is performed independently, with both inverse-sine branches and a normalized density. The second moment follows by direct trigonometric integration. At \(n=4\), the entire numerical CDF agrees with the independently known two-point chord law. Convex-hull reconstruction checks additional sample sizes. The analytical proof, not numerical experiments, covers the full infinite integer range.

## Originality

PASS, with residual historical priority uncertainty. Akopyan–Edelsbrunner–Nikitenko, arXiv:2007.07783v1, Section 4 and Theorem 15, give the generic decomposition and first edge-length expectation but not the explicit normalised chord-density or the exact quadratic-edge energy. Bonnet–O'Reilly gives facet-height information and does not evaluate the angle law. The related planar Poisson–Voronoi edge law concerns a different graph statistic. Actual semantic search comparisons and accessible prior finding claims did not reveal a statement implying the full new claim. This does not establish global historical uniqueness.

## Mathematical value

PASS. A complete finite-sample chord distribution is a natural statistic of a randomly triangulated sphere, and it provides all edge moments and a nondegenerate local scaling law. The squared-length sum is a standard mesh-energy diagnostic. Its exact ratio \(15/\pi\) to expected surface area, and its fixed multiplicative gap from the sharp equilateral-triangle benchmark, offer a concrete and sample-size-independent measure of mean mesh quality; this is not merely another unsupported numerical constant.

## Limits and closest work

The essential decomposition and surface-area formula are due to [1], and the typical-facet height theory to [2]. Only the extra evaluated law and consequences are assessed here. The model does not address realization-wise ratios, edge-length weighting, nonuniform samples or other dimensions. Bibliographic priority is provisional, particularly for older tessellation literature indexed under Delaunay rather than spherical convex hulls.

Self-review: passed. Independent audit: not yet performed.
