# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The Crelle triangle has side lengths
\(x=AB\cdot CD\), \(y=AC\cdot BD\), \(z=AD\cdot BC\) and area \(6RV\).
Factored Heron gives
\[
L\sigma_x\sigma_y\sigma_z=576R^2V^2,
\qquad
\sigma_x+\sigma_y+\sigma_z=L,
\]
so the normalized slacks are a positive probability vector with the
stated product.

The converse construction was checked algebraically. For arbitrary
positive \(p_1+p_2+p_3=1\), the four displayed disphenoid coordinates
give the opposite-edge products
\((1-p_1)/2,(1-p_2)/2,(1-p_3)/2\), hence slacks
\(p_1,p_2,p_3\). Its circumradius is \(1/(2\sqrt2)\) and its volume is
\(8u_1u_2u_3/3\), which reproduces
\(\eta=4p_1p_2p_3\).

At fixed \(\eta\), prescribing one component \(t\) leaves two positive
components with sum \(1-t\) and product \(\eta/(4t)\). The discriminant
condition is exactly \(t(1-t)^2\ge\eta\), giving the two sharp roots
\(\alpha,\beta\); the same disphenoid construction realizes every
admissible \(t\), not only the endpoints.

For the defect identity, the centroid-circumcenter relation
\(16R^2=\sum e^2+16OG^2\) and the exact pairing
\(\sum e^2=2L+E\) imply
\(8R^2/L=1+(E+16OG^2)/(2L)\). Substitution into the
Crelle-Heron product identity yields equation (9) with no inequality
step. Random numerical tetrahedra and the explicit disphenoid family
were also used as consistency checks; the proof itself is exact.

Potential edge cases were checked: nondegeneracy makes all Crelle slacks
strictly positive; \(\eta=4/27\) is the unique product maximum for the
normalized slack vector and collapses both profile roots to \(1/3\);
degeneration corresponds to \(\eta\downarrow0\).

## Originality

**PASS, to the best of our knowledge.**

The review excludes the classical Crelle theorem, the factored Heron
identity, and the known \(d_3\ge72V^2\) inequality from the novelty claim.
Mazur--Petrenko (2011) explicitly define the Crelle-triangle
\(d_3\) product and relate it to tetrahedra. Mazur (2018) proves the
volume inequality and its equivalent circumradius bound. Minculete--
Piscoran (2022) transfers several triangle inequalities to the Crelle
triangle. Gomez--Memoli (2024) studies Ptolemy's inequality in a broader
four-point/metric setting.

The literature checked did not locate the normalized slack map as a
surjection onto the open probability simplex, the constructive
disphenoid realization of every slack vector, the complete
componentwise interval at fixed \(\eta\) with realization of every point
of that interval, or the exact defect identity in equation (9).

Residual originality risk is significant because all of these statements
are elementary consequences of classical identities once the normalized
slack variables are introduced. Equivalent formulations may exist in
older solid-geometry, triangle-inequality, or tetrahedral-inequality
literature. The originality claim is therefore deliberately limited to
the best of our knowledge.

## Value

**PASS.**

The result turns qualitative strictness of the three-dimensional
Ptolemy inequalities into a complete quantitative profile governed by a
single scale-invariant volume/circumradius parameter. The converse
construction shows that the profile has no hidden tetrahedral
realizability gap: every normalized slack vector and every admissible
component value is already realized by a concrete disphenoid. The exact
defect identity also separates the classical volume-inequality gap into
opposite-edge mismatch and circumcenter-centroid displacement.

## Limitations

- Nondegenerate Euclidean tetrahedra only; degenerate cases are limiting.
- The profile concerns products of opposite edges, not six individual
  edge lengths or geometric distance to a model tetrahedron.
- The parameter uses \(R,V,L\); no universality for other shape
  normalizations is claimed.
- Residual folklore risk remains because the derivation is elementary.

## Sources checked

- A. L. Crelle, *Einige Bemerkungen uber die dreiseitige Pyramide*
  (1821), 105--132.
  https://archive.org/details/sammlungmathemat01crel
- M. Mazur and B. V. Petrenko, *On the conjectures of Atiyah and
  Sutcliffe*, arXiv:1102.4662v2 (2011).
  https://arxiv.org/abs/1102.4662
- M. Mazur, *An Inequality for the Volume of a Tetrahedron*,
  Amer. Math. Monthly 125 (2018), 273--275.
  https://doi.org/10.1080/00029890.2018.1411741
- N. Minculete and L.-I. Piscoran, *Vectorial and metrical relations in
  tetrahedron*, J. Math. Inequal. 16 (2022), 687--706.
  https://doi.org/10.7153/jmi-2022-16-49
- M. Gomez and F. Memoli, *The Four Point Condition: An Elementary
  Tropicalization of Ptolemy's Inequality*, Amer. Math. Monthly 131
  (2024), 187--203.
  https://doi.org/10.1080/00029890.2023.2285695
