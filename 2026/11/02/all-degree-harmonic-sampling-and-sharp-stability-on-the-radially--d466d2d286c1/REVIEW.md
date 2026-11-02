# Self-review

## Correctness — PASS

The addition theorem gives the Gram/evaluation rank correspondence with antipodal parity. The explicit corner/axis decomposition is derived directly from the seven representative coordinates, with separate even and odd Legendre sectors. Every low-degree rank and the strict competing condition-number inequalities for degrees below 120 use exact rational recurrences and exact arithmetic in the supplied standalone checker. The unique degree-seven maximum is supported by explicit algebraic eigenvalues and integer isolating bounds. The infinite tail is covered independently by the published Bernstein inequality and Gershgorin diagonal dominance. The finite geometry cross-check constructs the original seven-by-seven matrix from coordinates. Scientific risk: the 120-degree finite certificate is computational and should be replayed; the proof does not assert that finite testing alone proves an infinite statement.

## Originality — PASS under bounded comparison

Compared direct statements and implications for spherical-harmonic interpolation, harmonic-index designs, the exact rhombic-dodecahedron point set, and related spherical grids. Marzo (arXiv:math/0611503) treats increasing-degree, growing-node sampling and interpolation densities; Bannai–Okuda–Tagami (arXiv:1308.5101v1) treat vanishing unweighted harmonic moments and design bounds; neither inspected source supplies the complete seven-point Gram spectrum or the unique degree-seven global condition number. A polyhedral-grid paper names the same underlying polyhedron but its accessible abstract concerns PDE grids, and its inaccessible full text remains an explicit residual risk. Searches of related published mathematical records did not show a covering theorem. Residual risks: an older octahedral association-scheme, spherical-cubature, or representation-theory treatment could provide equivalent results; search absence is not novelty proof.

## Mathematical value — PASS

The two-radius fourteen-vertex rhombic dodecahedron is a classical non-vertex-transitive configuration whose radial projection leads to a natural finite harmonic sampling problem. Determining its exact-degree interpolation threshold and the isolated rank losses at degrees eight, ten, and fourteen resolves the full infinite-degree rank question, while the unique global worst condition number supplies sharp quantitative interpolation stability beyond a rank computation. The strict competing-degree bound identifies a meaningful stability gap. The exact results are specific to this canonical configuration, not arbitrary slices of a parameter table.

## Closest work and scientific limitations

J. Marzo (2006), *Marcinkiewicz–Zygmund inequalities and interpolation by spherical harmonics*; E. Bannai, T. Okuda, and M. Tagami (2013), *Spherical designs of harmonic index t*; W. Gautschi and C. Giordano (2008), Bernstein's inequality in equation (56); D. Oldham, J. Davies, and T. Phillips (2012), polyhedral spherical grids (abstract only). The supplied exact checker is a necessary part of the finite proof, with all higher degrees handled analytically. No independent review has been conducted.

Self-review: passed. Independent audit: not yet performed.
