# Same-model review

## Correctness

PASS. In the source normalization, roots have squared length \(2\) and are exactly the Voronoi facet vectors. Therefore every facet lies at distance \(1/\sqrt2\), and the pyramid identity gives
\[
\mathcal I_d(V_\Lambda)
=
d\sqrt2\,\operatorname{covol}(\Lambda)^{1/d}.
\]
The ADE Cartan determinants reduce the problem to integer determinant products. The periodic lower-bound function
\[
(1,2,3,4,4,4,3,2)
\]
is multiplicatively compatible modulo \(8\), with equality only when one residue is zero. This proves both the all-rank bound and the equality classification. The bundled exact checker independently confirms the residue table and dynamic-programming minima through rank \(256\).

## Originality

PASS. Novaga--Song's theorem is local under nearby metric and affine perturbations. It neither compares all root lattices of a fixed rank nor gives a global equality list. Targeted searches for the exact modulo-\(8\) isoperimetric classification and its determinant formulation found no covering result.

## Value

PASS. The result completely solves the natural global discrete counterpart to the source's local root-lattice analysis. It gives an exact closed constant in every rank and explains the recurring role of \(E_8\) by a sharp determinant-product law. The contrast between discrete global optimality and continuous local instability is structurally informative.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Novaga--Song, arXiv:2610.01653v1, whose Section 9 gives the local root-lattice classification. Classical ADE references provide the determinant table but do not state the fixed-rank Voronoi isoperimetric theorem.

The result applies only to root lattices. It does not identify the global minimizer among arbitrary lattices or parallelohedra. Older lattice literature may contain the determinant optimization implicitly under another formulation; this is the main residual bibliographic risk.
