# Review: The asymmetrical eight-vertex Klein bottle has mod-two cosystolic profile \(5,6,6\)

## Correctness
**PASS.** Exact face-equation reduction gives \(\dim Z^1=9\), vertex coboundaries give \(\dim B^1=7\), and the resulting \(512\) cocycles split into four classes of \(128\) representatives. Every cocycle is exhaustively classified by support weight and cup-square bit. The minimum data for the three nonzero classes are exactly \((5,1,1),(6,5,0),(6,3,1)\). The explicit weight-five cocycle is replayed from the facet data, and every minimum support is checked to be one simple cycle in the dual graph. The checker also reconstructs the closed connected surface and independently confirms trivial simplicial automorphism group.

Risk: the numerical multiplicities rely on a finite exhaustive checker. This is appropriate here because all \(2^9=512\) cocycles are enumerated, the linear-algebra dimensions are independently checked, and the supplied code is self-contained.

## Originality
**PASS.** Cervone's exact-object source gives the 1133 triangulation, uniqueness, asymmetry, and nearby mod-two homology context, but not a classwise cocycle support spectrum. Full-text inspection and targeted term searches found no cocycle, cohomology, or systolic statement. Lutz's survey supplies minimality and classification context, not the cochain metric. Focused semantic searches under exact-object, dual-cycle, cosystole, and cohomology-code aliases found no covering result.

The closest same-object comparison is a primal homology-cycle census. It does not imply this claim: the present invariant is shortest support in cohomology, equivalently a dual-cell one-cycle problem under Poincaré duality, and additionally records classwise multiplicities and cup-square type. No prior statement inspected dominates those data.

Residual risk: an older unindexed computation may describe the dual cubic map's shortest nonseparating cycles without using cohomology language.

## Value
**PASS.** The 1133 complex is a canonical vertex-minimal Klein-bottle triangulation, and mod-two one-cosystole is a natural discrete systolic and cohomological-code invariant. The full profile reveals a genuine class distinction invisible from the abstract group \(H^1\cong\mathbf F_2^2\): one square-nonzero class has a unique five-edge dual representative, the unique square-zero class first appears at six edges with five minimizers, and the remaining square-nonzero class also begins at six edges but with three minimizers. This is a complete natural finite classification, not a single arbitrary support calculation.

## Closest literature and limitations
The checked exact-object source is Cervone, DOI 10.1007/BF01265307, with the archived public snapshot `webarchive:20040309191227:vmkb.pdf`. Lutz, arXiv:math/0506372v1, supplies the vertex-minimal manifold context. The theorem is restricted to the fixed 1133 triangulation and mod-two cohomology; no claim is made about other triangulations or coefficients.

Same-model review: passed. Independent audit: not yet performed.
