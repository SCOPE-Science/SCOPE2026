# Disproof of the uniform cusp-modulus band for diagonal double fillings of the magic manifold

## Context

Let `M = s776` be the magic manifold with cusps `(E0,E1,E2)` in SnapPy's
standard meridian-longitude framing. For integer `n` with `|n| >= 6`, let
`N_n` be the simultaneous `(1,n)` filling on `E1,E2`, leaving `E0` complete.
The target band was

`1.30 <= Im(theta_n) <= 2.00` and `|Re(theta_n)| <= 0.35`,

where `theta_n` is the meridian-longitude cusp modulus of the unfilled cusp.
The modulus is scale invariant, so maximal-horoball rescaling does not change it.

## Result

The band is false. For `n=6`, `N_6` has a certified positive solution of the
complete logarithmic gluing equations and hence is hyperbolic. Its remaining
cusp satisfies the rigorous enclosure

- `0.4654775688468905 < Re(theta_6) < 0.4654775688495280`,
- `1.1939928091790021 < Im(theta_6) < 1.1939928091826787`.

Thus `Re(theta_6) > 0.35` and `Im(theta_6) < 1.30`, each by more than `0.1`.

## Certification

The six-tetrahedron SnapPy triangulation supplies six independent rectangular
gluing equations. The recorded Krawczyk computation uses `mpmath.iv` at
50 decimal digits and stores the original box `X` and the Krawczyk image
`K(X)`. Direct comparison of the saved decimal endpoints gives strict
coordinate-wise inclusion `K(X) subset int(X)`; the smallest saved boundary
margin is greater than `9.99997e-9`. All imaginary parts of `X` are positive.
The recorded verifier also checks the independent log lifts and all ten
logarithmic edge/completeness/filling rows with error far below the `0.1`
branch-separation threshold.

For the cusp modulus, the complex cusp cross-section is developed from the
certified Krawczyk boxes using the exact face pairings and peripheral-curve
integers transferred from the SnapPy kernel. The repaired verifier parses the
saved decimal interval endpoints directly into `mpmath.iv`; it does not pass
them through binary64 `float`. An independent reconstruction from
`lane1841_n6_snapshot.json` reproduces the enclosure above.

The earlier verifier version converted saved interval endpoints to binary64
before rebuilding the interval boxes. The numerical effect was about machine
epsilon and did not change the conclusion, but that conversion was not suitable
for a formal enclosure claim. `artifacts/lane1841_cusp.py` and its JSON
certificate are therefore repaired to preserve a conservative enclosure.

## Slope identification and literature context

SnapPy coefficients `(1,n)` represent the stated `1/n` filling family in this
record's fixed framing. Martelli-Petronio's classification of fillings of the
magic manifold is consistent with the hyperbolic `n=6` member but does not give
this cusp-modulus enclosure. Purcell's work on cusp shapes under cone
deformation supplies general background rather than this explicit value.

## Limitations

Only `n=6` is certified; no claim is made about the other members of the
family. The interval proof uses `mpmath.iv` as its interval implementation and
has not been cross-checked with a second interval library. The slope convention
is the standard SnapPy framing used by the stored triangulation.

## Reproducibility

From the record directory run:

`python3 artifacts/lane1841_krawczyk.py`

then

`python3 artifacts/lane1841_cusp.py`

The certificate and topology files are
`artifacts/lane1841_krawczyk.json`,
`artifacts/lane1841_cusp.json`, and
`artifacts/lane1841_n6_snapshot.json`.

## References

- B. Martelli and C. Petronio, *Dehn filling of the magic 3-manifold*,
  arXiv:math/0204228.
- J. S. Purcell, *Cusp shapes under cone deformation*,
  arXiv:math/0410233.
- SnapPy documentation and source for the gluing-equation and complex
  cusp-cross-section machinery.
