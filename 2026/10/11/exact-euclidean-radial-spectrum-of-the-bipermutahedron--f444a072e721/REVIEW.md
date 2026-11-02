# Mathematical assessment

## Correctness — PASS

For Ardila's standard realization of the bipermutahedron in the inherited Euclidean metric, the vertex formula gives
\[
\|v_B\|^2=\frac{2n(4n^2-1)}3+2(2A-n^2)^2+4(2A-n^2),
\]
where \(A\) is the Dyck-area statistic of first-occurrence positions. Each integer \(0\le A\le n(n-1)/2\) occurs, and the formula is strictly decreasing with \(A\). The unique circumball center is the origin by simultaneous permutation symmetry. The radius and outer contact count are
\[
R=\sqrt{\frac{2n(n-1)(3n^2+7n+1)}3},
\qquad
N_{\mathrm{outer}}=n((n-1)!)^2.
\]
An independent exact enumeration of all 116,016 labeled bipermutations in dimensions \(n=2,3,4,5\) corroborates the general argument.

## Originality — PASS, best of knowledge

Ardila's *The bipermutahedron* (arXiv:2008.02295, Definition 2.4 and Proposition 7.2) supplies the coordinates and symmetry, and its Theorem 9.4 concerns a Minkowski quotient. Neither this paper nor Nabijou's subsequent fan-theoretic study states the exact radial spectrum.

The separately established bipermutahedron inball theorem concerns facet distances, rather than an enclosing sphere determined by vertices. The harmonic-polytope shell theorem applies to a different realization and has only \(n\) shells. The bipermutahedron reversal-distance theorem studies the one-skeleton graph metric. None of these inspected statements implies the present Euclidean vertex-shell classification. An unindexed equivalent calculation remains a residual priority risk.

## Mathematical value — PASS

The bipermutahedron is a canonical non-vertex-transitive polytope motivated by matroid geometry. Its entire set of distinct Euclidean vertex radii is organized by one Dyck statistic in every dimension. The radius of its unique circumsphere and the precise outer contact set give reusable metric information not established by the inspected combinatorial or fan classifications.

## Scope and verification boundaries

The result is specific to the standard integral realization and its Euclidean metric; it does not classify shell multiplicities away from the outermost shell or other deformations. Numerical and combinatorial tests are supplementary and do not substitute for the arbitrary-dimension proof. No Lean proof or external expert attestation is asserted.

## Primary references

Federico Ardila, *The bipermutahedron*, arXiv:2008.02295 (2020), Combinatorial Theory 2(3) (2022), DOI 10.5070/C62359149.

Navid Nabijou, *Toric configuration spaces: the bipermutahedron and beyond*, arXiv:2306.03215; Mathematische Zeitschrift 308 (2024), 57.

Federico Ardila and Laura Escobar, *The harmonic polytope*, arXiv:2006.03078; Selecta Mathematica 27 (2021), 91.
