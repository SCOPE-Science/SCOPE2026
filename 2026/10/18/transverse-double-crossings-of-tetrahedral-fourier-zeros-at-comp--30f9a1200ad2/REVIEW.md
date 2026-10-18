# Scientific review: transverse tetrahedral Fourier-zero crossings

## Correctness — PASS

The exact exponential-simplex identity [1, Corollary 12] fixes the Fourier convention and normalization. At pairwise-distinct integral phase nodes, the four exponential factors coincide, giving a zero by Lagrange interpolation. The real first jet has rank one. The imaginary second jet on its two-dimensional kernel has explicitly negative determinant, since the product of four interpolation denominators is a positive squared Vandermonde product. Real-analytic Morse reduction then proves **exactly two transverse, embedded nodal branches** near each node. The affine extension follows from a nonvanishing multiplier and a linear change of frequency. The result is local, not a global zero-locus classification. Independent exact-algebra and high-precision checks are documented in VERIFICATION.md.

## Originality — PASS, with qualification

Baldoni–Berline–De Loera–Köppe–Vergne [1, Section 3.2] prove the general exponential simplex integral; the present finding claims no originality for that formula. Gallatin [2, Sections 2 and 4] gives a polyhedral Fourier-transform method. Both were read in relevant complete-text sections. The tetrahedral form-factor documentation [3] also states the transform and handles removable singularities of its rational representation. Their statements do not identify the local real zero set at complete reciprocal nodes, the two explicit tangent directions, or the universal negative saddle determinant. Comparisons with discrete finite-field simplex Fourier supports and planar triangle fold bifurcations are inapplicable to the specified real three-dimensional local topology. Exact publication priority is not independently certified; older optical form-factor literature may contain equivalent nodal observations, and only abstract-level material could be checked for the 2023 polyhedral form-factor paper [4].

## Mathematical value — PASS

The zero set of a three-dimensional Fourier transform is generally a real curve; identifying its singularities requires information not supplied merely by the transform's pointwise value. The theorem classifies every completely phase-aligned reciprocal node of any tetrahedron, proves that each is an ordinary transverse double point, and gives computable directions of its two incident Fourier-zero curves. The invariant sign from a four-point Vandermonde product is a structural statement across an infinite lattice and all invertible affine tetrahedra, not a selected numerical example.

Self-review: passed. Independent audit: not yet performed.

## References

[1] V. Baldoni et al., *How to Integrate a Polynomial over a Simplex*, arXiv:0809.2083 (2008), Section 3.2.

[2] G. M. Gallatin, *Fourier, Gauss, Fraunhofer, Porod and the Shape from Moments Problem*, arXiv:1109.5262 (2011), Sections 2 and 4.

[3] SasView, *truncated_tetrahedron* documentation, tetrahedral form factor and removable expression singularities: https://www.sasview.org/docs/user/models/truncated_tetrahedron.html

[4] T. Yang et al., *Form factor of any polyhedron and its singularities derived from a projection method*, *J. Appl. Crystallogr.* 56 (2023), 167–177, DOI 10.1107/S160057672201130X (abstract inspected; complete text not inspected).
