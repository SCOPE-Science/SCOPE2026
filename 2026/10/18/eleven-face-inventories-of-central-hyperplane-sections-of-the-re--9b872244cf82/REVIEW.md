# Self-review

## Correctness — PASS

The stated \(120\) exact vertices form an \(H_4\) root system of circumradius \(2\). The proposed four simple roots have the \(5,3,3\) Coxeter Gram matrix, and their reflection orbit exhausts the displayed vertices. Every central hyperplane normal is congruent to one of the relative interiors of the fifteen nonzero fundamental-chamber faces, since signs of all roots depend only on which simple-root inequalities vanish. The exact checker enumerates 720 edges, 1200 triangles, and 600 tetrahedral facets; for each chamber face it recovers section vertices from intersected edges, facets from intersected tetrahedra, and section edges from intersected triangles. Every row satisfies Euler's equation and polygon-edge incidence, with exactly eleven inventories. A separate numerical convex-hull implementation reproduces all fifteen row counts. The mathematical Coxeter-chamber argument, not numerical experiments, proves exhaustiveness.

## Originality — PASS relative to inspected evidence

The nearest established works concern vertex-deletion cuts of the 600-cell (Dutour Sikirić–Myrvold 2007), root matroid flats and automorphisms (Bao and colleagues 2010), and special inscribed 24-cell structures (Denney and colleagues 2019). General section bounds do not determine the claimed fifteen chamber cases. Previously recorded 600-cell maximal-simplex determinant data concern a different invariant, while the previously recorded seven-inventory central-section theorem concerns the \(D_4\) regular 24-cell, not the \(H_4\) 600-cell. The eleven-section inventory census is not implied by those results. Classical sections in selected symmetry directions, including possible 1973 Coxeter tables, remain an explicit historical-priority risk, and definitive priority certification is not asserted.

## Value — PASS

This is a complete finite classification of a natural geometric object in exceptional four-dimensional regular-polytope geometry, including the nonsmooth normals generally omitted by generic counts. It yields sharp minimum and maximum section-vertex counts \(42\) and \(144\), the single generic inventory, and two distinct non-generic section types with the same vertex count \(124\) but different edge–facet counts. The calculation has mathematical content beyond isolated coordinate evaluations because Coxeter chamber symmetry proves exhaustiveness.

## Limits

No combinatorial isomorphism classification beyond face inventories is established. Historical priority and external scholarly review remain open. One successful finite verification is not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
