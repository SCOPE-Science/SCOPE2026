# Independent mathematical audit

## correctness

PASS

The claim concerns the exactly specified singular degree-four plane curve Y^4+X^3 Z+XZ^3+XY^2 Z-X^2 Z^2=0 over F_3 and only its sets of distinct F_27/F_81-rational plane points. The affine equation follows by Z=1, and Y^4=0 at Z=0 gives the unique point (1:0:0). Distinct projective-point and dual-line normalization gives Q^2+Q+1 objects. A NEW independently written finite-field enumerator used polynomial quotient arithmetic over F_3, verified inverses of every nonzero element, evaluated the ORIGINAL homogeneous polynomial rather than the package alternative, and enumerated every curve point, line, four-secant and ambient center. It reproduced 31/79 curve points, 24/204 four-secants, line spectra (240,256,195,42,24)/(2520,2290,1515,114,204), center distributions as claimed, and precisely 282/108 uncovered exterior points. Four independent combinatorial double counts (lines, point-line pairs, curve-point pairs, four-secant-center pairs) agree in each field. The on-curve spectra are (0:7,4:24) and (0:3,10:72,24:4). At F_81 four of seven F_3-rational curve points are each on 24 four-secants, while the three nodes are uncovered. The original verify.cpp and check_parameter.py were inspected but NOT executed as proof substitutes. This is a genuine complete finite exhaustion, not a sample or a claim about arbitrary extension degree.

## originality

PASS

The full primary 2024 paper explicitly leaves the rational BKS r=3 and r=4 completeness cases open, and its Theorem 7.5 covers only r>=5. Its Theorem 8.2 addresses on-curve points and has an apparent contradictory small-even-field prediction; it does not give any of the verified full four-secant/ambient-center spectra. The earlier 2022 geometry study concerns the curve construction and automorphism group. Actual Resultary searches of the same curve/extensions and public metadata returned no exact earlier small-field line/center tables. Best of knowledge PASS, qualified by possible unindexed arithmetic tables and the primary-theorem tension; the absence of a search hit is not mathematical proof of uniqueness.

## value

PASS

This is an exact finite-arithmetic invariant of a canonical rational BKS plane curve at the two extensions expressly left unsettled by the motivating primary theorem, not an arbitrary choice of test sizes. Determining both completeness failures and the entire 757-/6643-line spectra plus ambient incidence distributions is useful for finite-plane arcs, splitting behavior and constructions in finite geometry. In addition, the F_81 on-curve distribution exposes a concrete, independently checkable tension with a printed theorem. The value is finite but substantive; no unproved all-extension generalization is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
