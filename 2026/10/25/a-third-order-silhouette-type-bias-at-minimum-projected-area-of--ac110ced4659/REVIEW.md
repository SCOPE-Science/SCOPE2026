# Review of the type-resolved minimum-brightness law

## Correctness — PASS
The public proof specifies the tetrahedron, Haar measure, projection-area normalization, triangular/quadrilateral boundary, all twelve minimizers, chart, spherical Jacobian, and two exact angular integrals. The critical equal-leading/unequal-third-order coefficients follow from uniform inversion of the exact local area formula and elementary integrations. A separately implemented planar convex-hull calculation tests both area and vertex count, and deterministic radial quadrature checks each coefficient and the conditional limit. The `verify_projection.py` package runs and has no external data dependencies beyond NumPy and SciPy. These finite tests are not substituted for the general analytical argument.

## Originality — PASS relative to inspected material
Feldman–Klain's theorem gives the unconditional triangular-shadow probability. Finch gives unconditional projected-area moments, unconditional type probabilities, and angular formulas for area and perimeter; the new conclusion is a **joint endpoint law sorted by silhouette type**, including the nonzero linear conditional bias. The published tetrahedral area-weighted moment formulas give finite conditional moments, not endpoint asymptotic coefficients. Searches by the exact area threshold, silhouette type, aliases, and third-order coefficients found no equivalent statement. Vickers–Brown's older paper could not be inspected beyond available abstract/bibliography; overlap remains a risk, and global novelty is not certified.

## Value — PASS
The lower area endpoint lies exactly on the boundary between triangular and quadrilateral shadows. Its two adjacent geometric strata are equally likely at leading order but measurably different at next order, a sharp orientation/shape-selection effect inaccessible from unconditional silhouette frequencies and a useful local diagnostic of geometric projection bias. Both the exact cubic coefficient split and the sign and value of its conditional linear bias are intrinsic to the natural threshold problem, rather than an arbitrary numerical slice.

## Residual limitations
The statement concerns the explicitly normalized regular tetrahedron and only the near-minimal-area joint distribution. It is not a global distribution, not a general-tetrahedron theorem, and not an independently certified priority claim. Source inspection limits include the inaccessible full text of Vickers–Brown (2001).

Self-review: passed. Independent audit: not yet performed.
