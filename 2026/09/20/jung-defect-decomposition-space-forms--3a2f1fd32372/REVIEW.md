# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof reduces to two exact identities. First-order optimality of a minimum enclosing ball provides active unit tangent directions with positive weights summing to an equilibrium, \(\sum_i\lambda_i u_i=0\), and Carathéodory reduces to at most \(n+1\) active directions. The constant-curvature cosine laws then give
\[
\Phi_\kappa(d_{ij})=\Psi_\kappa(R)(1-\langle u_i,u_j\rangle).
\]
Expanding the equilibrium condition gives
\[
\sum_{i<j}\lambda_i\lambda_j(1-\langle u_i,u_j\rangle)=1/2,
\]
which proves the support identity exactly.

The Jung-defect decomposition is obtained by adding and subtracting the diameter value. After zero-padding the weight vector to \(n+1\) coordinates,
\[
\sum_i\lambda_i^2-1/(n+1)=\sum_i(\lambda_i-1/(n+1))^2,
\]
so every displayed term is nonnegative. Equality therefore forces all \(n+1\) weights to be equal and every active edge to have diameter length; conversely a regular \(n\)-simplex realizes equality.

The support-cardinality hierarchy follows from \(\sum_{i=1}^m\lambda_i^2\ge1/m\) and is sharp for regular lower-dimensional simplices. The componentwise weight bound uses the zero-sum condition on deviations and Cauchy--Schwarz. The individual edge estimate follows because every summand in the weighted edge deficit is nonnegative.

The spherical restriction lies below \(\pi\), and the elementary bound \(R\le D\) therefore rules out antipodal active points, which is enough for the first-order support argument. The classical spherical Jung theorem additionally gives \(R<\pi/2\) in the stated regime, but that fact is not used to derive the support identity.

Supplementary symbolic/numerical spot checks of the cosine-law identity and the defect decomposition were performed for regular and non-regular equilibrium configurations; these checks support but are not used in place of the proof.

## Originality

**PASS, to the best of our knowledge.**

The classical claims are explicitly excluded. Jung's Euclidean bound is classical. Dekster established spherical and hyperbolic Jung theorems with regular-simplex equality. Lang--Schroeder gave a much more general Jung theorem for Alexandrov/CAT spaces with curvature bounded above. A 2024 hyperbolic convex-geometry paper restates the hyperbolic circum-support theorem and the regular-simplex equality case. Schneider's 2009 paper gives a genuine stability result for Jung-type inequalities in Minkowski spaces, but its conclusion is Banach--Mazur closeness of a convex body to a simplex and its mechanism is Minkowski asymmetry; it does not state the active-support defect identity here. Euclidean minimum-enclosing-ball duality also contains closely related weighted variance identities, so no novelty is claimed for the Euclidean weighted identity by itself.

Searches covered exact and synonymous formulations: “Jung theorem stability,” “quantitative Jung inequality,” “minimum enclosing ball support weights,” “Chebyshev center support points,” “spherical Jung defect,” “hyperbolic Jung defect,” “circumradius diameter stability,” and combinations with regular simplex, barycentric weights, cosh/cosine, and support cardinality. No located source states the unified space-form identity, the exact split into weight variance plus weighted edge deficit, or the sharp formula converting normalized Jung deficit into the minimum required number of active support points.

The strongest residual originality risk is B. V. Dekster, *The Jung theorem for spherical and hyperbolic spaces* (Acta Math. Hungar. 67, 1995, 315--331, DOI 10.1007/BF01874495). Bibliographic data, later theorem statements, and equality characterizations were checked, but the primary paper itself was not available here as directly inspectable full text; its proof could contain part of the cosine-law calculation implicitly. A second residual-risk source is Lang--Schroeder 1997: its theorem and bibliographic scope were checked, but no exact constant-curvature defect decomposition was located. Because the present proof is short once an equilibrium support is chosen, equivalent folklore in minimum-enclosing-ball or classical simplex literature remains possible.

## Value

**PASS.**

The result refines an extremal radius--diameter theorem into an exact, termwise nonnegative certificate. It distinguishes two independent causes of Jung deficit—unbalanced circum-support and non-diametral active edges—and converts a single scalar deficit into a sharp discrete conclusion about support dimension. The threshold hierarchy is global, dimension-explicit, and simultaneously valid in Euclidean, spherical, and hyperbolic model spaces. It also yields direct quantitative control of active weights and every active edge near equality.

## Limitations

- The spherical statement is restricted to the non-antipodal Jung regime.
- The result controls an active minimum-enclosing-ball support, not the whole set in Hausdorff or Banach--Mazur distance.
- No exact extension is claimed to general CAT\((\kappa)\) spaces, where the cosine-law equality is replaced by comparison inequalities.
- The Euclidean weighted support identity is not claimed as new by itself.
- Originality remains to the best of our knowledge, with material residual risk from older constant-curvature Jung proofs and MEB folklore.

## Sources checked

- H. Jung, *Über die kleinste Kugel, die eine räumliche Figur einschliesst*, J. Reine Angew. Math. 123 (1901), 241--257.
- B. V. Dekster, *The Jung theorem for spherical and hyperbolic spaces*, Acta Math. Hungar. 67 (1995), 315--331. https://doi.org/10.1007/BF01874495
- U. Lang, V. Schroeder, *Jung's theorem for Alexandrov spaces of curvature bounded above*, Ann. Global Anal. Geom. 15 (1997), 263--275. https://doi.org/10.1023/A:1006574402955
- R. Schneider, *Stability for Some Extremal Properties of the Simplex*, J. Geom. 96 (2009), 135--148. https://doi.org/10.1007/s00022-010-0028-0
- F. Nielsen, G. Hadjeres, *Approximating Covering and Minimum Enclosing Balls in Hyperbolic Geometry*, GSI 2015, LNCS 9389, 586--594. https://doi.org/10.1007/978-3-319-25040-3_63
- H. Hirai, *On a manifold formulation of self-concordant functions*, arXiv:2212.10981.
- K. J. Böröczky, A. Csépai, Á. Sagmeister, *Hyperbolic width functions and characterizations of bodies of constant width in the hyperbolic space*, J. Geom. 115 (2024), 15. https://doi.org/10.1007/s00022-024-00714-9
