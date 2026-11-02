# Review of the cuboctahedral Fourier-support classification

## Correctness

PASS. The type-\(A_3\) root-polytope identification is proved by mass transport between positive and negative coordinates. Exactly eight candidate integer translates per unit-cube point are reduced to a three-case arithmetic count, giving the two-level periodization almost everywhere. The Laplace inversion at integer frequency yields all residue multiplicity patterns without loss at repeated poles. Every nonzero case is a nonvanishing rational multiple of \(\pi^{-2}\). The resulting support count is a direct exhaustive combinatorial count, valid even at \(N=0\). A standalone checker independently corroborates the arithmetic formula.

## Originality

PASS within bounded source coverage. Montagard–Ressayre, arXiv:math/0609809, and Ardila–Beck–Hoşten–Pfeifle–Seashore, arXiv:0809.5123, address root-polytope geometry and explicit type-\(A_n\) triangulations, not lattice-frequency Fourier support. Diaz–Le–Robins, arXiv:1602.08593, gives general Stokes/face-poset Fourier formulas and distinguishes nongeneric frequencies, but does not state the cuboctahedral periodization, nonvanishing table, or exact count. Searches including cuboctahedral integer Fourier coefficients, type-\(A_3\) root-polytope periodization, and Fourier support collision hyperplanes did not identify a statement entailing the result. This is a bounded comparison, not proof of global uniqueness; older specialized tiling or spline literature may contain an equivalent formula.

## Mathematical value

PASS. The cuboctahedron is the first three-dimensional root polytope with triangular faces, unlike lattice-zonotope multi-tiles whose nonzero lattice Fourier support can collapse. The theorem identifies its exact translation-multiplicity defect and the entire nonzero integer Fourier support, including a closed polynomial count for every box. This is a natural harmonic invariant relevant to lattice periodization and spectral/tiling questions, not a numerical sample or an artificially selected subfamily.

## Scope and limits

The result uses the root-lattice coordinate normalization, and covers only this specific three-dimensional polytope at integer frequencies. The supplied checker corroborates finitely many cases but does not independently prove the infinite assertion. The literature comparison remains bounded.

Self-review: passed. Independent audit: not yet performed.
