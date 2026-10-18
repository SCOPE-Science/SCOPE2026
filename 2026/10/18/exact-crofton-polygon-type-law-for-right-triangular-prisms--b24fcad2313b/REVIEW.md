# Scientific review: Exact Crofton polygon-type law for right triangular prisms

## Correctness — PASS

The single final claim is the complete three-atom law for all nondegenerate right triangular prisms, with its perimeter-only triangle–pentagon gap. A generic plane cuts exactly the prism edges whose signed endpoint heights differ. Sorting the three bottom heights gives an exact interval of cutting offsets for pentagons; the upper and lower hemispheres reduce its invariant measure to an explicit trigonometric integral. Its elementary evaluation is obtained on the six angular order chambers. Cauchy's width identity fixes the normalizing constant and the edge-crossing integral independently establishes the mean number of vertices. These give the identity \(\Pr(N=3)-\Pr(N=5)=2h/(L+2h)\) without extrapolating a finite sample.

The included `verify.py` passes **32** independent integral comparisons, **3,600** direction-by-direction offset checks against all nine prism edges, and **180,000** uniform-normal/uniform-unconditional-offset random-plane trials, with 78,827 hitting planes in the reproducible seeded test. Sampling rejects nonintersecting planes rather than biasing the normal orientation. Computations are corroboration, not an infinite proof.

## Originality — PASS relative to inspected materials, with genuine historical risks

Searches of published records covered triangle/prism/Crofton aliases, the exact perimeter gap, equivalent statistics, broader stereological families and earlier tables. The closest previously available same-measure geometric record treats **right rectangular pyramids**, which have a different vertex/edge graph and do not imply the all-triangular-prism family. A published regular-prism mean-square **width** result is also a different observable. Wang, *Determining All Universal Tilers* (2011, arXiv:1110.1715), proves section tilability rather than probabilities. Voss, *Frequencies of n-polygons in planar sections of polyhedrons* (1982), treats the exact general observable; its accessible abstract identifies an integral-geometric method and examples of unspecified families, so possible direct overlap cannot be excluded. Ohser–Mücklich, *Stereology for some classes of polyhedrons* (1995), concerns regular-prism size/shape inversion with numerical kernels; the accessible abstract does not state this law. Both full texts, and the Wasén–Warren 1991 stereological catalog, require future priority inspection. Search absence is not a novelty proof; the PASS assessment is explicitly bounded by these material-access risks.

## Mathematical value — PASS

A finite elementary-arctangent formula for all three section frequencies across **every triangular base geometry** is a complete, motivated convex-geometric classification, not an arbitrary slice or numerical recomputation. Its universal gap is geometrically substantive: one statistic depends only on base perimeter and height even though the full distribution retains shape information. The exact law is a natural test case for integral stereology of pentahedra.

## Scope and limitations

Only right triangular prisms, generic affine planes and section side counts are covered; oblique prisms, central-plane sampling, shadows and section-area laws are not established. The full texts of the two most threatening earlier papers were inaccessible and historical priority is not certified. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
